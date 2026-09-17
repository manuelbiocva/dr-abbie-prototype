# -*- coding: utf-8 -*-
"""Generate the stand-in for the clinic-finder map background.

This is deliberately NOT a map. There is no coastline, no place name and no
real geography in it — it is an abstract street-grid texture that holds the
slot so the section's layout, scrim and card contrast can be judged now.
Anything closer to a real map would risk being read as showing where the
clinics actually are, which only the real Google map can do honestly.

Replaced at build time by the Google Static Maps image or embed once LH Media
supplies an API key. See the comment in the clinic-finder markup for the
ready-made URL.
"""
import random

from PIL import Image, ImageDraw, ImageFilter

W, H, SS = 1600, 900, 2
BASE = (246, 249, 251)      # --canvas
ROAD = (225, 233, 239)
ROAD_MINOR = (236, 241, 245)
BLOCK = (241, 246, 249)
WATER = (221, 240, 251)     # --pale-blue
GREEN = (232, 241, 234)
PIN = (17, 136, 207)        # --azure

random.seed(11)             # eleven clinics; deterministic so rebuilds match


def main():
    im = Image.new('RGB', (W * SS, H * SS), BASE)
    d = ImageDraw.Draw(im)

    # soft blocks so the grid does not read as graph paper
    for _ in range(70):
        x = random.randint(0, W * SS)
        y = random.randint(0, H * SS)
        w = random.randint(60, 260) * SS
        h = random.randint(50, 200) * SS
        d.rectangle([x, y, x + w, y + h], fill=BLOCK)

    # a river and a park, for the shapes a street map usually has
    d.polygon([(0, 640 * SS), (300 * SS, 600 * SS), (700 * SS, 700 * SS),
               (1100 * SS, 640 * SS), (W * SS, 690 * SS), (W * SS, H * SS), (0, H * SS)],
              fill=WATER)
    d.ellipse([980 * SS, 120 * SS, 1330 * SS, 330 * SS], fill=GREEN)

    # minor streets, then the arterials on top
    for i in range(0, W, 55):
        d.line([(i * SS, 0), (i * SS, H * SS)], fill=ROAD_MINOR, width=2 * SS)
    for i in range(0, H, 55):
        d.line([(0, i * SS), (W * SS, i * SS)], fill=ROAD_MINOR, width=2 * SS)
    for _ in range(9):
        if random.random() < 0.5:
            x = random.randint(0, W)
            d.line([(x * SS, 0), (x * SS + random.randint(-80, 80) * SS, H * SS)],
                   fill=ROAD, width=7 * SS)
        else:
            y = random.randint(0, H)
            d.line([(0, y * SS), (W * SS, y * SS + random.randint(-60, 60) * SS)],
                   fill=ROAD, width=7 * SS)

    im = im.filter(ImageFilter.GaussianBlur(1.2 * SS))
    d = ImageDraw.Draw(im)

    # eleven pins, scattered but never overlapping the card column centres
    spots = [(180, 250), (330, 470), (520, 200), (690, 380), (860, 260),
             (1010, 470), (1180, 210), (1320, 400), (450, 700), (900, 660), (1420, 640)]
    for x, y in spots:
        cx, cy, r = x * SS, y * SS, 13 * SS
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=PIN)
        d.polygon([(cx - r * 0.6, cy + r * 0.55), (cx + r * 0.6, cy + r * 0.55),
                   (cx, cy + r * 1.9)], fill=PIN)
        d.ellipse([cx - r * 0.38, cy - r * 0.38, cx + r * 0.38, cy + r * 0.38],
                  fill=(255, 255, 255))

    im = im.resize((W, H), Image.LANCZOS)
    im.save('assets/img/map-placeholder.webp', 'WEBP', quality=82, method=6)
    im.resize((W // 2, H // 2), Image.LANCZOS).save(
        'assets/img/map-placeholder-sm.webp', 'WEBP', quality=82, method=6)
    print('map-placeholder.webp     %dx%d' % im.size)
    print('map-placeholder-sm.webp  %dx%d' % (W // 2, H // 2))
    print('pins: %d' % len(spots))


if __name__ == '__main__':
    main()
