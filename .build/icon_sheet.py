# -*- coding: utf-8 -*-
"""Rasterise the treatment-card icons so they can be judged before shipping.

There is no SVG library available here, so this flattens the path subset the
icons use (M L H V C Q Z, absolute and relative) into polylines and strokes
them with Pillow. Arcs are deliberately not supported -- the icons are authored
without them so that this renderer stays small enough to trust.

Rendered at the real badge size, because an icon that reads at 200px and
turns to mush at 26px is the actual failure mode being checked for.
"""
import io
import math
import re
import sys

from PIL import Image, ImageDraw

SS = 6  # supersample factor

# every command is tokenised, not just the supported ones: dropping an
# unsupported letter silently shifts its operands onto the previous command
# and corrupts the whole path instead of failing.
TOK = re.compile(r'([MmLlHhVvCcSsQqTtAaZz])|(-?\d*\.?\d+(?:e-?\d+)?)')


def parse(d):
    """Flatten a path string to a list of polylines in viewBox units."""
    toks = [(c, n) for c, n in TOK.findall(d)]
    i = 0
    cmd = None
    cur = (0.0, 0.0)
    start = (0.0, 0.0)
    prev_c = None
    polys = []
    poly = []

    def nums(k):
        nonlocal i
        out = []
        while len(out) < k:
            if i >= len(toks) or toks[i][0]:
                raise ValueError('path ran out of operands near token %d: %r' % (i, d))
            out.append(float(toks[i][1]))
            i += 1
        return out

    while i < len(toks):
        c, n = toks[i]
        if c:
            cmd = c
            i += 1
            if cmd in 'Zz':
                if poly:
                    poly.append(start)
                    polys.append(poly)
                    poly = []
                cur = start
                continue
        if cmd is None:
            break
        rel = cmd.islower()
        k = cmd.upper()

        if k == 'M':
            x, y = nums(2)
            if rel:
                x, y = cur[0] + x, cur[1] + y
            if poly:
                polys.append(poly)
            poly = [(x, y)]
            cur = start = (x, y)
            cmd = 'l' if rel else 'L'
            prev_c = None
        elif k == 'L':
            x, y = nums(2)
            if rel:
                x, y = cur[0] + x, cur[1] + y
            poly.append((x, y))
            cur = (x, y)
            prev_c = None
        elif k == 'H':
            (x,) = nums(1)
            if rel:
                x = cur[0] + x
            poly.append((x, cur[1]))
            cur = (x, cur[1])
            prev_c = None
        elif k == 'V':
            (y,) = nums(1)
            if rel:
                y = cur[1] + y
            poly.append((cur[0], y))
            cur = (cur[0], y)
            prev_c = None
        elif k in ('A',):
            raise ValueError('arcs are not supported; author the icon with C instead: %r' % d)
        elif k in ('T',):
            raise ValueError('smooth quadratics are not supported: %r' % d)
        elif k in ('C', 'S', 'Q'):
            if k == 'S':
                x2, y2, x, y = nums(4)
                if rel:
                    x2, y2 = cur[0] + x2, cur[1] + y2
                    x, y = cur[0] + x, cur[1] + y
                # reflect the previous control point through the current point
                if prev_c is None:
                    x1, y1 = cur
                else:
                    x1, y1 = 2 * cur[0] - prev_c[0], 2 * cur[1] - prev_c[1]
            elif k == 'C':
                x1, y1, x2, y2, x, y = nums(6)
                if rel:
                    x1, y1 = cur[0] + x1, cur[1] + y1
                    x2, y2 = cur[0] + x2, cur[1] + y2
                    x, y = cur[0] + x, cur[1] + y
            else:
                qx, qy, x, y = nums(4)
                if rel:
                    qx, qy = cur[0] + qx, cur[1] + qy
                    x, y = cur[0] + x, cur[1] + y
                x1 = cur[0] + 2.0 / 3 * (qx - cur[0])
                y1 = cur[1] + 2.0 / 3 * (qy - cur[1])
                x2 = x + 2.0 / 3 * (qx - x)
                y2 = y + 2.0 / 3 * (qy - y)
            p0 = cur
            prev_c2 = (x2, y2)
            steps = 24
            for s in range(1, steps + 1):
                t = s / steps
                mt = 1 - t
                bx = (mt ** 3 * p0[0] + 3 * mt * mt * t * x1
                      + 3 * mt * t * t * x2 + t ** 3 * x)
                by = (mt ** 3 * p0[1] + 3 * mt * mt * t * y1
                      + 3 * mt * t * t * y2 + t ** 3 * y)
                poly.append((bx, by))
            cur = (x, y)
            prev_c = prev_c2
        else:
            break

    if poly:
        polys.append(poly)
    return polys


def draw_icon(d, size, stroke, colour):
    """Stroke a path onto a transparent RGBA tile of `size` px."""
    n = size * SS
    img = Image.new('RGBA', (n, n), (0, 0, 0, 0))
    dr = ImageDraw.Draw(img)
    w = max(1, int(round(stroke * SS * size / 24.0)))
    r = w / 2.0
    for poly in parse(d):
        pts = [(p[0] * n / 24.0, p[1] * n / 24.0) for p in poly]
        if len(pts) == 1:
            x, y = pts[0]
            dr.ellipse([x - r, y - r, x + r, y + r], fill=colour)
            continue
        dr.line(pts, fill=colour, width=w, joint='curve')
        for x, y in (pts[0], pts[-1]):           # round caps
            dr.ellipse([x - r, y - r, x + r, y + r], fill=colour)
    return img.resize((size, size), Image.LANCZOS)


def sheet(icons, out, badge=56, icon=26, cols=5):
    """Badge-size row plus a 3x detail row, on the real azure circle."""
    AZ = (17, 136, 207, 255)
    pad, labelh = 22, 16
    cellw = max(badge, icon * 3) + pad * 2
    rows = (len(icons) + cols - 1) // cols
    cellh = badge + icon * 3 + labelh + pad * 3
    W, H = cellw * cols, cellh * rows
    out_img = Image.new('RGB', (W, H), '#F6F9FB')
    dr = ImageDraw.Draw(out_img)
    for idx, (name, d) in enumerate(icons):
        cx = (idx % cols) * cellw + cellw // 2
        cy = (idx // cols) * cellh + pad
        for bs, isz in ((badge, icon), (icon * 3, icon * 3 - 12)):
            dr.ellipse([cx - bs // 2, cy, cx + bs // 2, cy + bs], fill=AZ)
            g = draw_icon(d, isz, 1.7, (255, 255, 255, 255))
            out_img.paste(g, (cx - isz // 2, cy + (bs - isz) // 2), g)
            cy += bs + pad // 2
        tw = dr.textlength(name)
        dr.text((cx - tw / 2, cy), name, fill='#232629')
    out_img.save(out)
    return out


if __name__ == '__main__':
    import json
    icons = json.load(io.open(sys.argv[1], encoding='utf-8'))
    print(sheet(list(icons.items()), sys.argv[2]))
