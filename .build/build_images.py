# -*- coding: utf-8 -*-
"""Derive web-ready images from Extracted-Image/ into prototype/assets/img/.

The source files are 2000-5000px PNGs at 3-6MB each. Referencing them raw would
wreck LCP on mobile, which the brief makes a launch condition. This crops each
one to the aspect ratio of the slot it fills, resizes, and writes WebP at a
1x and 2x width.

Nothing here re-labels a photo. Where a face could not be identified from the
source filename or the team photograph, the slot keeps its placeholder.
"""
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                      # prototype/
PROJ = os.path.dirname(ROOT)
SRC = os.path.join(PROJ, 'Extracted-Image')
OUT = os.path.join(ROOT, 'assets', 'img')

os.makedirs(OUT, exist_ok=True)

# Slots whose source carries transparent padding. Left un-trimmed, that
# padding becomes a visible indent when the asset is aligned against text.
TRIM = {'google-stars', 'google-wordmark'}

# Logos supplied as JPEGs on a white background. Dropped onto a coloured
# band they read as white rectangles, so the white matte is keyed out to
# alpha and the original colour recovered by un-premultiplying against it.
DEWHITE = {'assoc-aapsm', 'assoc-sports-med', 'assoc-podiatry-nsw', 'assoc-ahpra'}

# Slots cut from a region of the source rather than the whole frame.
# The composite badge is only 271px wide, so "5 Stars" and the stars are
# rebuilt as live text and SVG; only the Google wordmark stays a raster,
# because it is a trademark and should not be hand-drawn.
REGION = {'google-wordmark': (183, 0, 264, 35)}

# slot -> (source file, aspect w/h, 1x width, vertical focus, keep alpha)
JOBS = [
    # chrome
    ('logo',                '01LogoHorizontal-6.png',                None,      360, 'center', True),
    # reversed lockup, for the transparent header over the dark hero
    ('logo-white',          '01LogoHorizontal-7.png',                None,      360, 'center', True),

    # hero + about
    ('hero-practitioner',   'DR.ABBIECLINICSHOOT-097.jpg',           (4, 5),    720, 'top',    False),
    ('about-team',          'DrAbbieTeam-2-1-scaled.jpg',            (4, 3),    880, 'center', False),

    # treatment cards
    ('tx-biomechanics',     'Dr-Abbie-Najjarine-assessing_2.jpg',    (16, 10),  640, 'center', False),
    ('tx-orthotics',        'Orthotics.png',                         (16, 10),  640, 'center', False),
    ('tx-shockwave',        'Shockwave-Therapy.png',                 (16, 10),  640, 'center', False),
    ('tx-childrens',        'dr-abbie-looking-at-childs-feet-.png',  (16, 10),  640, 'center', False),

    # remaining treatment cards. Sports Podiatry and General Foot Care use
    # stock the client already licenses — subject-appropriate but not clinical
    # photography of this practice. Neural Therapy has no usable image at all.
    ('tx-dry-needling',     'Dry-Needling-1.png',                    (16, 10),  640, 'center', False),
    ('tx-mobilisation',     'mobilisation-1.png',                    (16, 10),  640, 'center', False),
    ('tx-strapping',        'yousef-performing-strapping-on-patient-35.png', (16,10), 640, 'center', False),
    ('tx-sports',           'Prevent-Sports-Injuries-Before-They-Happen.png', (16,10), 640, 'center', False),
    ('tx-foot-care',        'high-angle-hand-massaging-foot-with-special-tool-scaled.jpg', (16,10), 640, 'center', False),

    # Neural Therapy. Source is only 300x200 — the largest that exists, both
    # locally and on the live server — so the card renders it at native size.
    ('tx-neural',           '10.jpg',                                (16, 10),  300, 'center', False),

    # practitioners — only the two that can be identified with confidence
    ('dr-abbie-najjarine',  'Dr-Abbie-Clinics-Staff-Head-Shot.png',  (1, 1),    420, 'top',    False),
    ('dr-elissa-all',       '3-1.png',                               (1, 1),    420, 'center', False),
    # 3:4 portraits for the team carousel. The 1:1 slots above stay: the
    # location page and the other variants still render circular portraits.
    ('pc-najjarine',        'Dr-Abbie-Clinics-Staff-Head-Shot.png',  (3, 4),    480, 'top',    False),
    ('pc-attar',            '5-1.png',                               (3, 4),    480, 'center', False),
    ('pc-elissa',           '3-1.png',                               (3, 4),    480, 'center', False),
    ('pc-alheyoury',        '2-1.png',                               (3, 4),    480, 'center', False),
    ('pc-yousef',           '1-1.png',                               (3, 4),    480, 'center', False),

    # blog
    ('blog-heel-pain',      'Stretching.png',                    (16, 10),  640, 'center', False),
    ('blog-orthotics',      'orthotics-95-1-scaled.jpg',                         (16, 10),  640, 'top',    False),
    ('blog-children',       'Back-To-School.png',                    (16, 10),  640, 'center', False),
    ('blog-shockwave',      'treatments.jpg',                 (16, 10),  640, 'center', False),

    # clinic + associations
    # 3:2 = the camera's own frame. The old 16:9 derivative threw away 16% of
    # the height, which is the dimension the bleeding About panel needs most:
    # object-fit crops the width there, so headroom is what keeps faces whole.
    ('clinic-reception',    'DrAbbieReception-31-scaled.jpg',        (3, 2),   1000, 'center', False),
    ('assoc-aapsm',         'aapsm.jpg',                             None,      260, 'center', False),
    ('assoc-sports-med',    'sports-medicine.jpg',                   None,      260, 'center', False),
    ('assoc-podiatry-nsw',  'podiatry-nswact.jpg',                   None,      260, 'center', False),
    ('assoc-ahpra',         '968176-1467781592-wide.jpg',            None,      300, 'center', False),
    # health fund strip the client already has: medibank, Bupa, HCF, nib, ahm,
    # HICAPS. Baked onto a navy panel, so it stays one image.
    ('health-funds',        'logos.jpg.bv_.webp',                    None,      887, 'center', False),
    # V5 hero — full-bleed right panel. Wide 3:2 crop so a 6-person group
    # survives the cover-crop at panel proportions.
    ('hero-team',           'DrAbbieTeam-2-1-scaled.jpg',            (3, 2),   1200, 'center', False),

    # V5 full-bleed hero. Cropped to 21:9 at source, keeping heads and torsos
    # and dropping the floor, so the browser's cover-crop has almost nothing
    # left to remove and no one loses the top of their head.
    ('hero-band',           'DrAbbieTeam-2-1-scaled.jpg',            (21, 9),  2000, 'top',    False),

    # Full-height hero. The 21:9 band was cut for a short hero panel; in a
    # full-viewport box (~1.78) a 2.33 image loses the outer practitioners to
    # the cover-crop. 16:9 matches the box, so the whole group stays in frame.
    ('hero-wide',           'DrAbbieTeam-2-1-scaled.jpg',            (16, 9),  2200, 'topmost', False),

    # Mobile hero. A 21:9 band inside a portrait viewport shows ~21% of the
    # photo width, so phones get a 4:5 crop framed on the centre of the group.
    ('hero-portrait',       'DrAbbieTeam-2-1-scaled.jpg',            (4, 5),    800, 'top',    False),

    # Client's own Google review badge, colour wordmark version. Small
    # source (271x35), so it is used at ~140px where 2x still holds.
    ('google-stars',        '5stars_white_text_transparent.png',      None,      271, 'center', True),

    # Google wordmark only, cut from the composite badge.
    ('google-wordmark',     '5stars_white_text_transparent.png',      None,      160, 'center', True),

    # Hero service slider. 3:4 cards. Only treatments with real clinical
    # photography are included - General Foot Care, Neural Therapy and Sports
    # Podiatry have no supplied image and are left out rather than faked.
    ('svc-biomechanics',    'Dr-Abbie-Najjarine-assessing_2.jpg',    (3, 4),    440, 'center', False),
    ('svc-orthotics',       'Orthotics.png',                         (3, 4),    440, 'center', False),
    ('svc-shockwave',       'Shockwave-Therapy.png',                 (3, 4),    440, 'center', False),
    ('svc-childrens',       'dr-abbie-looking-at-childs-feet-.png',  (3, 4),    440, 'center', False),
    ('svc-dry-needling',    'Dry-Needling-1.png',                    (3, 4),    440, 'center', False),
    ('svc-mobilisation',    'mobilisation-1.png',                    (3, 4),    440, 'center', False),
    ('svc-strapping',       'yousef-performing-strapping-on-patient-35.png', (3, 4), 440, 'center', False),

    # V6 bento + feature crops
    ('bento-assess',        'Dr-Abbie-Najjarine-assessing_2.jpg',    (1, 1),    560, 'center', False),
    # NBA booking card. 1:1 to match the source exactly -- it is a four-panel
    # collage, so any reframing would cut through the sub-photos.
    ('nba-teaching',        '76903271_3087622707933631_6576746724440670208_n.jpg', (1, 1), 480, 'center', False),
    ('bento-reception',     'DrAbbieReception-31-scaled.jpg',        (1, 1),    560, 'center', False),
    ('bento-child',         'DrAbbie_assessing-a-child_crop.jpg',    (1, 1),    560, 'center', False),
    ('feature-care',        'dr-abbie-looking-at-childs-feet-.png',  (4, 5),    560, 'center', False),
    ('band-clinic',         'DrAbbieReception-31-scaled.jpg',        (21, 9),  1400, 'center', False),
    # Clinic-finder background. No build-time crop: the section's aspect moves
    # with the card grid, so object-position frames it at runtime. Source is
    # only 640x480.
    ('clinics-bg',          'IMG_2097.jpg',                          None,      640, 'center', False),
    # Kirrawee location hero. The clinic exterior with its signage and street
    # number -- the most place-specific photograph in the library. Source is
    # 1000px wide, so no build-time crop: object-position frames it.
    # Location hero. A practitioner examining a patient, with the empty wall on
    # the left where the copy sits and the clinical action on the right where
    # the scrim thins. No build-time crop; object-position frames it.
    ('hero-clinic',         'Dr-Abbie-Najjarine-assessing_2.jpg',     None,     1800, 'center', False),
    # Gait assessment for the location NBA cell, so the hero photograph is not
    # repeated further down the same page.
    ('nba-gait',            'DR.ABBIECLINICSHOOT-113.webp',           (16, 10),  640, 'center', False),
    # Service hero. No build-time crop: the band's aspect moves with the copy
    # height, so object-position frames it at runtime.
    ('hero-shockwave',      'Shockwave-Therapy.png',                 None,     1400, 'center', False),
    ('hero-biomechanics',     'Dr-Abbie-Najjarine-assessing_2.jpg',       None,     1400, 'center', False),
    ('hero-childrens',        'dr-abbie-looking-at-childs-feet-.png',     None,     1400, 'center', False),
    ('hero-orthotics',        'Orthotics.png',                            None,     1400, 'center', False),
    ('hero-dry-needling',     'Dry-Needling-1.png',                       None,     1400, 'center', False),
    ('hero-mobilisation',     'mobilisation-1.png',                       None,     1400, 'center', False),
    ('hero-foot-care',        'high-angle-hand-massaging-foot-with-special-tool-scaled.jpg',  None,     1400, 'center', False),
    ('hero-sports',           'Prevent-Sports-Injuries-Before-They-Happen.png',  None,     1400, 'center', False),
    ('hero-strapping',        'yousef-performing-strapping-on-patient-35.png',  None,     1400, 'center', False),
    # Neural Therapy. The one photograph that actually shows the treatment
    # (10.jpg, an injection into a foot) is 300x200 -- far too small for a
    # hero. It stays as the card image, where it can carry its own size, and
    # the hero uses a higher resolution clinical photograph instead.
    ('hero-neural', 'Foot-Pain-Causing-Your-Back-and-Hip-Problems.png', None, 1400, 'center', False),
    ('hero-heel-pain', 'Stretching.png', None, 1400, 'center', False),
    ('hero-plantar', 'mobilisation.png', None, 1400, 'center', False),
    ('hero-achilles', 'rugby-1310896.jpg', None, 1400, 'center', False),
    ('hero-shin-splints', 'Running-down-hill1.png', None, 1400, 'center', False),
    ('hero-running', 'running-down-hill-2.png', None, 1400, 'center', False),
    ('hero-knee', 'athlete-barbell-body-949126.jpg', None, 1400, 'center', False),
    ('hero-flat-feet', 'ballet-dark-3189782.jpg', None, 1400, 'center', False),
    ('hero-forefoot', 'ballet-2042851_1920.jpg', None, 1400, 'center', False),
    ('hero-ingrown', 'home-salon-pedicure-foot-care-treatment-nail-process-professional-pedicures-master-blue-gloves-apply-light-pink-gel-polish-scaled.jpg', None, 1400, 'center', False),
    ('hero-pigeon-toe', 'Healthy-Feet-Healthy-Future_-Early-Assessment-for-Children.png', None, 1400, 'center', False),
    ('hero-out-toe', '3-Simple-Stretches-to-Improve-Posture-at-Work.png', None, 1400, 'center', False),
    # Condition cards. The diagrams are the client's own branded artwork with
    # labels and a title inside the frame, so they are generated with NO crop --
    # a square crop cuts the labels off. The photographs crop safely.
    ('cond-heel-pain', 'Heel-spurs.jpg', None, 720, 'center', False),
    ('cond-plantar', 'Plantar-Fascitis.jpg', None, 720, 'center', False),
    ('cond-achilles', 'Achilles.jpg', None, 720, 'center', False),
    ('cond-shin-splints', 'Shin-splint-medial.jpg', None, 720, 'center', False),
    ('cond-forefoot', 'Mortons-Neuroma-1.jpg', None, 720, 'center', False),
    ('cond-knee', 'Osgood-Sclatter.jpg', None, 720, 'center', False),
    ('cond-flat-feet', 'orthotics-95-1-scaled.jpg', (1, 1), 720, 'center', False),
    ('cond-running', 'adult-condition.jpg', (1, 1), 720, 'center', False),
    ('cond-ingrown', 'high-angle-hand-massaging-foot-with-special-tool-scaled.jpg', (1, 1), 720, 'center', False),
    ('cond-children-gait', 'dr-abbie-looking-at-childs-feet-.png', (1, 1), 720, 'center', False),
    ('cond-out-toe', 'Pigeon-Toe-and-Out-Toe.jpg', (1, 1), 252, 'center', False),
    # Closing CTA band. The team outside the Kirrawee clinic -- a different
    # photograph from the hero lineup. No build-time crop: the band's aspect
    # moves with the copy height, so object-position does the framing at
    # runtime and nothing is baked in. Source is only 1000px wide.
    ('cta-band',            'Dr-Abbie-Clinics-Home-Page-Header-Image.png', None, 1000, 'center', False),
    ('testimonial',         'DrAbbie_assessing-a-child_crop.jpg',    (4, 3),    520, 'center', False),
]


# The blog cards used to share source files with the treatment cards, so the
# home page showed the orthotics, shockwave and mobilisation photographs twice.
# cond-running pointed at running-down-hill-3.jpg, which is byte-identical to
# the whiteboard sketch, under alt text describing a runner.
# blog: full-bleed post heroes, the fifth card, the hub hero, and the client's
# own shoe-fitting guides for the children's post
JOBS += [
    ('post-heel-pain',      'Stretching.png',                    None,      1400, 'center', False),
    ('post-orthotics',      'orthotics-95-1-scaled.jpg',                         None,      1400, 'center', False),
    ('post-children',       'Back-To-School.png',                    None,      1400, 'center', False),
    ('post-shockwave',      'Shockwave-Therapy.png',                 None,      1400, 'center', False),
    ('post-see-podiatrist', 'Dr-Abbie-Clinics-Website-Images-e1784699063514.png', None, 1400, 'center', False),
    ('blog-see-podiatrist', 'Dr-Abbie-Clinics-Website-Images-e1784699063514.png', (16, 10), 640, 'center', False),
    ('hero-blog',           'running-down-hill-3 (1).jpg',           None,      1400, 'center', False),
    ('guide-shoe-toe-box',  'Shoe-Toe-Box.gif',                      None,       528, 'center', False),
    ('guide-shoe-length',   'Shoe-Length2.gif',                      None,       539, 'center', False),
    ('guide-shoe-heel',     'Choosing-shoes_1.jpg',                  None,       439, 'center', False),
]
# The children's photograph has "Back To School" lettered across the bottom
# from y=1015. Cropped above it, so neither the card nor the hero carries
# someone else's campaign headline.
REGION['blog-children'] = (0, 0, 2240, 1008)
REGION['post-children'] = (0, 0, 2240, 1008)
# The reception photo is 2.5:1 with a person at each end; a centred 16:10 card
# cut both in half. Weighted right to keep the practitioner and the handover.
REGION['blog-see-podiatrist'] = (715, 0, 2000, 803)
# Portrait photograph: the orthotic is in the lower third, the practitioner's
# face in the upper. A centred crop showed the face and no orthotic.
REGION['blog-orthotics'] = (0, 1250, 1707, 2317)
REGION['post-orthotics'] = (0, 1100, 1707, 2400)

# team: a second portrait of Dr Abbie Najjarine for the founder section, so the
# team page does not show his headshot twice
JOBS += [
    ('founder-najjarine', 'Inside-the-Najjarine-Biomechanical-Assessment-NBA.png', (4, 5), 640, 'center', False),
]

# Dr Ahmad El-Jabali. kyle1.webp carries a baked-in name band from y=550; the
# portrait is cut above it. kyle2.webp, labelled Yousef Najjarine in the same
# style, matches the confirmed pc-yousef headshot, which is why the label on
# kyle1 is trusted for the name.
JOBS += [
    ('pc-eljabali', 'kyle1.webp', (3, 4), 480, 'top', False),
]
REGION['pc-eljabali'] = (135, 0, 540, 540)

# "Understanding ..." section images (client, 18 Sept 2026): one per page,
# none already shown elsewhere on that page. Natural aspect, so the
# branded diagrams are never cropped.
JOBS += [
    ('edu-heel-pain', 'heel-pain (2).jpg', None, 560, 'center', False),
    ('edu-plantar', 'heel-pain.jpg', None, 560, 'center', False),
    ('edu-achilles', 'Achilles-Tendonitis.jpg', None, 560, 'center', False),
    ('edu-shin', 'Shin-splint-ant.jpg', None, 560, 'center', False),
    ('edu-forefoot', 'Metatarsagalia.jpg', None, 560, 'center', False),
    ('edu-knee', 'knee-pain.jpg', None, 560, 'center', False),
    ('edu-flat-feet', 'orthotic.jpg', None, 560, 'center', False),
    ('edu-running', 'aching-legs.jpg', None, 560, 'center', False),
    ('edu-pigeon', 'Kid_walking-in-sand.jpg', None, 560, 'center', False),
    ('edu-out-toe', 'Ballet_crop.jpg', None, 560, 'center', False),
    ('edu-biomechanics', 'Short-Leg.jpg', None, 560, 'center', False),
    ('edu-orthotics', 'Orthotic-styles.jpg', None, 560, 'center', False),
    ('edu-needling', 'dry-needling.png', None, 560, 'center', False),
    ('edu-mobilisation', 'foot-mobilisations.png', None, 560, 'center', False),
    ('edu-neural', 'Neutral-stance.jpg', None, 560, 'center', False),
    ('edu-shockwave', 'shockwave-therapy.jpg', None, 560, 'center', False),
    ('edu-strapping', 'Strapping.jpg', None, 560, 'center', False),
    ('edu-sports', 'sports-condition.jpg', None, 560, 'center', False),
    ('edu-childrens', 'SEVERS-DISEASE.jpg', None, 560, 'center', False),
]

def drop_white_matte(im):
    """Treat a logo on white as itself composited over white, and undo that.

    alpha = 1 - min(r,g,b)/255 recovers the coverage; the colour is then
    un-premultiplied so saturated marks keep their hue instead of washing out.
    """
    im = im.convert('RGB')
    px = im.load()
    w, h = im.size
    out = Image.new('RGBA', (w, h))
    op = out.load()
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            a = 255 - min(r, g, b)
            if a <= 0:
                op[x, y] = (0, 0, 0, 0)
                continue
            f = 255.0 / a
            op[x, y] = (
                max(0, min(255, int((r - (255 - a)) * f))),
                max(0, min(255, int((g - (255 - a)) * f))),
                max(0, min(255, int((b - (255 - a)) * f))),
                a,
            )
    return out


def crop_to(im, aspect, focus):
    """Centre-crop to an aspect ratio, biased upward for portraits."""
    tw, th = aspect
    w, h = im.size
    target = tw / th
    current = w / h
    if abs(current - target) < 0.01:
        return im
    if current > target:                      # too wide -> trim sides
        new_w = int(round(h * target))
        left = (w - new_w) // 2
        return im.crop((left, 0, left + new_w, h))
    new_h = int(round(w / target))            # too tall -> trim top/bottom
    if focus == 'topmost':
        top = 0                               # all of the cut comes off the floor
    elif focus == 'top':
        top = int(h * 0.04)                   # keep heads in frame
        top = min(top, h - new_h)
    else:
        top = (h - new_h) // 2
    return im.crop((0, top, w, top + new_h))


def run():
    total_src = total_out = 0
    rows = []

    for name, src, aspect, width, focus, alpha in JOBS:
        p = os.path.join(SRC, src)
        if not os.path.exists(p):
            rows.append((name, src, 'MISSING', '', ''))
            continue

        src_kb = os.path.getsize(p) // 1024
        total_src += src_kb

        im = Image.open(p)
        im = im.convert('RGBA' if alpha else 'RGB')
        if name in REGION:
            im = im.crop(REGION[name])
        if name in TRIM and im.mode == 'RGBA':
            # getbbox() keeps columns with alpha as low as 1, which left two
            # effectively invisible columns and a visible indent. Threshold 4
            # lands on fully opaque content and is stable up to 24.
            alpha = im.split()[3].point(lambda v: 255 if v > 4 else 0)
            box = alpha.getbbox()
            if box:
                im = im.crop(box)
        if name in DEWHITE:
            im = drop_white_matte(im)
            alpha = True
            box = im.split()[3].point(lambda v: 255 if v > 8 else 0).getbbox()
            if box:
                im = im.crop(box)

        if aspect:
            im = crop_to(im, aspect, focus)

        made = []
        for scale, suffix in ((1, ''), (2, '@2x')):
            w = width * scale
            if w > im.width:
                w = im.width
            h = int(round(im.height * w / im.width))
            out = im.resize((w, h), Image.LANCZOS)
            dest = os.path.join(OUT, '%s%s.webp' % (name, suffix))
            out.save(dest, 'WEBP', quality=82, method=6)
            kb = os.path.getsize(dest) // 1024
            total_out += kb
            made.append('%dx%d %dKB' % (w, h, kb))
            if scale == 1:
                dims = (w, h)

        rows.append((name, src, '%dKB' % src_kb, ' | '.join(made), '%dx%d' % dims))

    print('%-22s %-42s %8s  %s' % ('SLOT', 'SOURCE', 'SRC', '1x | 2x'))
    print('-' * 118)
    for r in rows:
        print('%-22s %-42s %8s  %s' % (r[0], r[1][:42], r[2], r[3]))
    print('-' * 118)
    print('source total %d KB  ->  output total %d KB  (%.0f%% smaller)'
          % (total_src, total_out, 100 - (total_out * 100.0 / max(total_src, 1))))

    # emit the intrinsic sizes so the HTML can carry width/height and avoid CLS
    print('\nwidth/height for markup:')
    for r in rows:
        if r[4]:
            print('  %-22s %s' % (r[0], r[4]))


if __name__ == '__main__':
    run()
