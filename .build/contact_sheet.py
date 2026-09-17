# -*- coding: utf-8 -*-
"""Build a contact sheet of candidate images so they can be reviewed at once."""
import os
from PIL import Image, ImageDraw

SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), 'Extracted-Image')
OUT = os.environ.get('SCRATCH', '.')

NAMES = [
    'Inside-the-Najjarine-Biomechanical-Assessment-NBA.png',
    'Dr.-Abbie-Najjarine.png',
    'Dr-Abbie-Najjarine-assessing_2.jpg',
    'DrAbbie_assessing-a-child_crop.jpg',
    'DrAbbieReception-31-scaled.jpg',
    'DR.ABBIECLINICSHOOT-077.jpg',
    'Orthotics.png',
    'Shockwave-Therapy.png',
    'Dry-Needling-1.png',
    'mobilisation-1.png',
    'dr-abbie-looking-at-childs-feet-.png',
    'yousef-performing-strapping-on-patient-35.png',
    'Back-To-School.png',
    'Achilles.jpg',
    'Healthy-Feet-Healthy-Future_-Early-Assessment-for-Children.png',
    '01LogoHorizontal-6.png',
    'aapsm.jpg',
    'Dr-Abbie-Clinics-Staff-Head-Shot.png',
]

COLS, CELL, PAD, LABEL = 6, 300, 8, 22
rows = (len(NAMES) + COLS - 1) // COLS
sheet = Image.new('RGB', (COLS * (CELL + PAD) + PAD,
                          rows * (CELL + PAD + LABEL) + PAD), '#20242a')
d = ImageDraw.Draw(sheet)

for i, n in enumerate(NAMES):
    p = os.path.join(SRC, n)
    x = PAD + (i % COLS) * (CELL + PAD)
    y = PAD + (i // COLS) * (CELL + PAD + LABEL)
    if not os.path.exists(p):
        d.text((x + 4, y + 4), 'MISSING ' + n[:28], fill='#ff8080')
        continue
    try:
        im = Image.open(p).convert('RGB')
        im.thumbnail((CELL, CELL))
        sheet.paste(im, (x + (CELL - im.width) // 2, y + (CELL - im.height) // 2))
        d.text((x, y + CELL + 4), '%d. %s' % (i + 1, n[:38]), fill='#cfd6dd')
    except Exception as e:
        d.text((x + 4, y + 4), 'ERR ' + str(e)[:30], fill='#ff8080')

dest = os.path.join(OUT, 'contact-sheet.jpg')
sheet.save(dest, 'JPEG', quality=80)
print(dest, sheet.size)
