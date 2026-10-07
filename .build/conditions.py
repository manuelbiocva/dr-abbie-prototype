# -*- coding: utf-8 -*-
"""Condition name -> card image and alt text.

Six of these are the client's own branded anatomical diagrams. They carry a
title and labels inside a blue frame, so they are generated uncropped and the
card displays them with object-fit: contain on white -- the same white their
own background uses, so the letterboxing is invisible. Cropping them square
cuts the labels off.

The remaining photographs have no diagram in the asset library and use a clinical
photograph instead.
"""

CONDITIONS = {
    'Heel Pain':         ('cond-heel-pain',     'Diagram of a heel spur and the calcaneal attachment of the plantar fascia', True),
    'Plantar Fasciitis': ('cond-plantar',       'Diagram of the plantar fascia showing inflammation and tearing', True),
    'Achilles Pain':     ('cond-achilles',      'Diagram comparing a normal Achilles tendon with tendonitis, rupture and tendonosis', True),
    'Shin Splints':      ('cond-shin-splints',  'Diagram of medial shin splints along the tibia', True),
    'Forefoot Pain':     ('cond-forefoot',      'Diagram of Morton\u2019s neuroma between the metatarsals', True),
    'Knee Pain':         ('cond-knee',          'Pain highlighted at the knee joint', False),
    'Flat Feet':         ('cond-flat-feet',     'A podiatrist assessing the arch of a patient\u2019s foot', False),
    'Running Injuries':  ('cond-running',       'A runner on a downhill road', False),
    'Ingrown Toenails':  ('cond-ingrown',       'A foot being treated with a podiatry tool', False),
    'Pigeon Toe':        ('cond-children-gait', 'Dr Abbie Najjarine examining a child\u2019s feet', False),
    'Out Toe':           ('cond-out-toe',       'A young child standing barefoot, showing foot position', False),
    "Sever's Disease":   ('cond-severs',        'Diagram of the heel in Sever\u2019s disease, showing the Achilles tendon, the calcaneus and the growth plate', True),
    'Osgood-Schlatter':  ('cond-osgood',        'Diagram of Osgood-Schlatter disease, showing the patellar tendon pulling on the growth plate at the top of the shin bone', True),
    'Bunions':           ('cond-bunions',       'Diagram of the four stages of a bunion, from a normal foot to the tertiary stage', True),
    'Bow Legs':          ('cond-bow-legs',      'A school-aged boy running', False),
    'Knock Knees':       ('cond-knock-knees',   'School children sitting on a wall with their legs hanging down', False),
}


def card(name, desc, href='condition.html'):
    """A condition card in the same shape as the treatment cards."""
    img, alt, diagram = CONDITIONS[name]
    arrow = ('<svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true">'
             '<path d="M3 7h8M7.5 3.5L11 7l-3.5 3.5" stroke="currentColor" stroke-width="1.7" '
             'stroke-linecap="round" stroke-linejoin="round"/></svg>')
    return '\n'.join([
        '        <a class="card cond-card reveal" href="%s">' % href,
        '          <div class="cond-card__media%s"><img src="assets/img/%s.webp" '
        'srcset="assets/img/%s.webp 1x, assets/img/%s@2x.webp 2x" width="720" height="720" '
        'alt="%s" loading="lazy" decoding="async" sizes="(min-width: 900px) 25vw, 100vw"></div>'
        % (' cond-card__media--diagram' if diagram else '', img, img, img, alt),
        '          <h3>%s</h3>' % name,
        '          <p>%s</p>' % desc,
        '          <span class="card__more">Read more %s</span>' % arrow,
        '        </a>',
    ]) + '\n'
