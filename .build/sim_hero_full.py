# -*- coding: utf-8 -*-
"""Render the full-bleed hero as the browser composites it.

Models the radial bottom-left pool plus the even tint, then samples two
things: white-text contrast where the copy sits, and how much the faces in
the upper band are being darkened. The point of the radial is that the second
number stays low while the first stays above AA.
"""
import math
import os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(os.path.dirname(HERE), 'assets', 'img', 'hero-wide@2x.webp')
OUT = os.environ.get('SCRATCH', HERE)

DEEP = (12, 46, 71)
OBJ_X, OBJ_Y = 0.50, 0.18
GUTTER = 0.055
HEADER = 76
BASE_TINT = 0.16

# radial-gradient(125% 88% at 16% 104%, ...)
RX, RY, CX, CY = 1.25, 0.88, 0.16, 1.04
STOPS = [(0.00, 0.95), (0.26, 0.88), (0.46, 0.62), (0.68, 0.24), (0.86, 0.00)]


def radial_alpha(u, v):
    """u,v are 0..1 across the box."""
    dx = (u - CX) / RX
    dy = (v - CY) / RY
    r = math.sqrt(dx * dx + dy * dy)
    if r <= STOPS[0][0]:
        return STOPS[0][1]
    for i in range(1, len(STOPS)):
        p0, a0 = STOPS[i - 1]
        p1, a1 = STOPS[i]
        if r <= p1:
            return a0 + (a1 - a0) * ((r - p0) / (p1 - p0))
    return 0.0


def composite(px, u, v):
    r, g, b = px
    a = radial_alpha(u, v)
    r = a * DEEP[0] + (1 - a) * r
    g = a * DEEP[1] + (1 - a) * g
    b = a * DEEP[2] + (1 - a) * b
    t = BASE_TINT
    r = t * DEEP[0] + (1 - t) * r
    g = t * DEEP[1] + (1 - t) * g
    b = t * DEEP[2] + (1 - t) * b
    return r, g, b


def contrast_white(l8):
    c = l8 / 255.0
    lin = c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 1.05 / (lin + 0.05)


def sample(base, W, H, box):
    x0, y0, x1, y1 = box
    tot = 0.0
    n = 0
    for y in range(y0, y1, 4):
        for x in range(x0, x1, 4):
            r, g, b = composite(base.getpixel((x, y)), x / W, y / H)
            tot += 0.2126 * r + 0.7152 * g + 0.0722 * b
            n += 1
    return tot / n


src = Image.open(IMG).convert('RGB')
sw, sh = src.size
results = []

for vw, vh in ((1920, 1080), (1440, 900), (1280, 800)):
    W, H = vw, vh
    scale = max(W / sw, H / sh)
    nw, nh = int(sw * scale), int(sh * scale)
    big = src.resize((nw, nh), Image.LANCZOS)
    base = big.crop((int((nw - W) * OBJ_X), int((nh - H) * OBJ_Y),
                     int((nw - W) * OBJ_X) + W, int((nh - H) * OBJ_Y) + H))

    g = int(W * GUTTER)
    blockw = min(44 * 16, int(W * 0.62))
    head = (g, int(H * 0.50), g + blockw, int(H * 0.68))
    intro = (g, int(H * 0.70), g + blockw, int(H * 0.82))
    # faces: the upper band across the whole frame
    faces_l = (g, int(H * 0.10), int(W * 0.45), int(H * 0.34))
    faces_r = (int(W * 0.55), int(H * 0.10), W - g, int(H * 0.34))

    ch = contrast_white(sample(base, W, H, head))
    ci = contrast_white(sample(base, W, H, intro))
    fl = sample(base, W, H, faces_l)
    fr = sample(base, W, H, faces_r)
    raw_l = sum(base.crop(faces_l).convert('L').resize((16, 16)).getdata()) / 256.0

    results.append((vw, base, W, H, head, intro, faces_l, ch, ci, fl, fr, raw_l))
    print('%dx%d | headline %.1f:1  intro %.1f:1 | left faces %.0f/255 '
          '(unscrimmed %.0f) darkened %.0f%% | right faces %.0f/255'
          % (vw, vh, ch, ci, fl, raw_l, (1 - fl / raw_l) * 100, fr))

TH = 300
sheet = Image.new('RGB', (sum(int(r[2] * TH / r[3]) + 10 for r in results) + 10, TH + 34), '#20242a')
d = ImageDraw.Draw(sheet)
x = 10
for vw, base, W, H, head, intro, faces_l, ch, ci, fl, fr, raw in results:
    comp = Image.new('RGB', (W // 3, H // 3))
    for yy in range(0, H // 3):
        for xx in range(0, W // 3):
            r, g_, b = composite(base.getpixel((xx * 3, yy * 3)), xx * 3 / W, yy * 3 / H)
            comp.putpixel((xx, yy), (int(r), int(g_), int(b)))
    t = comp.resize((int(W * TH / H), TH), Image.LANCZOS)
    dd = ImageDraw.Draw(t)
    k = TH / H
    for box, col in ((head, '#F0682C'), (intro, '#1188CF'), (faces_l, '#8FE36B')):
        dd.rectangle([box[0] * k, box[1] * k, box[2] * k, box[3] * k], outline=col, width=2)
    sheet.paste(t, (x, 10))
    d.text((x, TH + 16), '%dpx  head %.1f  faces -%.0f%%' % (vw, ch, (1 - fl / raw) * 100),
           fill='#cfd6dd')
    x += t.width + 10

dest = os.path.join(OUT, 'hero-full-sim.jpg')
sheet.save(dest, 'JPEG', quality=88)
print('\n', dest)
print('AA needs 4.5:1. Green box = left-hand faces; lower "darkened %" is better.')
