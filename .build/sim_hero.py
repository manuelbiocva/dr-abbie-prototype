# -*- coding: utf-8 -*-
"""Simulate the hero's right-hand panel crop at several viewport widths.

object-fit: cover on a wide group photograph is where people get sliced off,
so this renders what the browser will actually show before it ships.
"""
import os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(os.path.dirname(HERE), 'assets', 'img', 'hero-team@2x.webp')
OUT = os.environ.get('SCRATCH', HERE)

PANEL_VW = 0.54          # .hero__media width
def min_h(vw):           # clamp(420px, 36vw, 680px)
    return max(420, min(int(vw*0.36), 680))
OBJ_X = 0.50             # object-position x
OBJ_Y = 0.40             # object-position y

VIEWPORTS = [1920, 1440, 1280, 1024]

src = Image.open(IMG).convert('RGB')
sw, sh = src.size

cells = []
for vw in VIEWPORTS:
    pw = int(vw * PANEL_VW)
    ph = min_h(vw)
    scale = max(pw / sw, ph / sh)
    nw, nh = int(sw * scale), int(sh * scale)
    big = src.resize((nw, nh), Image.LANCZOS)
    left = int((nw - pw) * OBJ_X)
    top = int((nh - ph) * OBJ_Y)
    crop = big.crop((left, top, left + pw, top + ph))
    lost_l = left / nw * 100
    lost_r = (nw - pw - left) / nw * 100
    cells.append((vw, pw, ph, crop, lost_l, lost_r))
    print('%dpx viewport -> panel %dx%d  side loss L%.1f%% R%.1f%%'
          % (vw, pw, ph, lost_l, lost_r))

TH = 300
sheet_w = sum(int(c[3].width * TH / c[3].height) + 10 for c in cells) + 10
sheet = Image.new('RGB', (sheet_w, TH + 34), '#20242a')
d = ImageDraw.Draw(sheet)
x = 10
for vw, pw, ph, crop, ll, lr in cells:
    t = crop.resize((int(crop.width * TH / crop.height), TH), Image.LANCZOS)
    sheet.paste(t, (x, 10))
    d.text((x, TH + 16), '%dpx  panel %dx%d  loss %.0f%%/%.0f%%'
           % (vw, pw, ph, ll, lr), fill='#cfd6dd')
    x += t.width + 10

dest = os.path.join(OUT, 'hero-sim.jpg')
sheet.save(dest, 'JPEG', quality=86)
print('\n', dest)
