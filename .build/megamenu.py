# -*- coding: utf-8 -*-
"""Mega menus for Services, Conditions and Clinics.

Generated from the same data as the pages (services.py, condition_data.py,
blog_data.py), so a treatment or condition added there appears in the menu on
the next build, linked to its own page. The treatment icons are the ones from
the home page's treatments grid (menu_icons.json, extracted from that markup);
the one-line descriptions are shortened from each treatment's existing copy,
and the condition lines are the home page's condition-card lines.

The panels are hidden until opened, so the header is left out of the build's
repeated-photo check (see assemble.repeated_photos).
"""
import io
import json
import os

from services import SERVICES
from condition_data import CONDITIONS
from blog_data import POSTS
from clinics import CLINICS, REGIONS, TAGS, BOOKING

_HERE = os.path.dirname(os.path.abspath(__file__))
_SRC = json.load(io.open(os.path.join(_HERE, 'menu_icons.json'), encoding='utf-8'))
ICONS = _SRC['icons']
CONDITION_BLURBS = _SRC['conds']

SERVICE_BLURBS = {
    'biomechanics':       'Full lower limb assessment, from the feet up',
    'custom-orthotics':   'Prescribed devices, made on site at Kirrawee',
    'childrens-podiatry': 'Pigeon toe, flat feet and growing pains',
    'shockwave-therapy':  'For persistent heel and Achilles pain',
    'dry-needling':       'Fine needles to release trigger points',
    'foot-mobilisation':  'Hands-on work to restore joint movement',
    'sports-podiatry':    'Running injuries and return to sport',
    'general-foot-care':  'Ingrown toenails, corns and calluses',
    'neural-therapy':     'Injectable therapy to stimulate repair',
    'foot-strapping':     'Support that offloads tissue while it heals',
}

# Grouped by where the pain is and who has it, so a visitor scans three short
# lists rather than one long one.
CONDITION_GROUPS = [
    ('Heel &amp; foot', ['Heel Pain', 'Plantar Fasciitis', 'Forefoot Pain', 'Flat Feet',
                         'Ingrown Toenails']),
    ('Leg &amp; sport', ['Achilles Pain', 'Shin Splints', 'Knee Pain', 'Running Injuries']),
    ('Children', ['Pigeon Toe', 'Out Toe']),
]

ARROW = ('<svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true">'
         '<path d="M3 7h8M7.5 3.5L11 7l-3.5 3.5" stroke="currentColor" stroke-width="1.6" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')
NUMBER_WORDS = {10: 'Ten', 11: 'Eleven', 12: 'Twelve'}
NL = '\n'


def _feature(href, slot, eyebrow, title, more):
    return NL.join([
        '            <a class="mega__feature" href="%s">' % href,
        '              <span class="mega__feature-img"><img src="assets/img/%s.webp" '
        'srcset="assets/img/%s.webp 1x, assets/img/%s@2x.webp 2x" width="640" height="400" '
        'alt="" loading="lazy" decoding="async" sizes="260px"></span>' % (slot, slot, slot),
        '              <span class="mega__feature-body">',
        '                <span class="mega__eyebrow">%s</span>' % eyebrow,
        '                <span class="mega__feature-title">%s</span>' % title,
        '                <span class="mega__more">%s %s</span>' % (more, ARROW),
        '              </span>',
        '            </a>',
    ])


def _intro(eyebrow, title, text, all_href, all_label):
    return NL.join([
        '            <div class="mega__intro">',
        '              <span class="mega__eyebrow">%s</span>' % eyebrow,
        '              <p class="mega__title">%s</p>' % title,
        '              <p class="mega__text">%s</p>' % text,
        '              <a class="mega__all" href="%s">%s %s</a>' % (all_href, all_label, ARROW),
        '            </div>',
    ])


def services_menu():
    items = NL.join(
        '                <li><a class="mega__link" href="services/%s.html">'
        '<span class="mega__icon" aria-hidden="true">%s</span>'
        '<span class="mega__label"><span class="mega__name">%s</span>'
        '<span class="mega__desc">%s</span></span></a></li>'
        % (sv['SLUG'], ICONS[sv['SLUG']], sv['NAME'], SERVICE_BLURBS[sv['SLUG']])
        for sv in SERVICES)
    return NL.join([
        '          <div class="dropdown mega" id="mega-services">',
        '          <div class="mega__inner">',
        _intro('Treatments',
               '%s treatments, one starting point' % NUMBER_WORDS.get(len(SERVICES), len(SERVICES)),
               'Every treatment plan starts with an assessment, so what we prescribe is '
               'matched to what we find.', 'index.html#treatments', 'All treatments'),
        '            <ul class="mega__grid mega__grid--services">',
        items,
        '            </ul>',
        _feature('services/biomechanics.html', 'nba-gait', 'Not sure what you need?',
                 'Start with the Najjarine Biomechanical Assessment', 'How it works'),
        '          </div>',
        '          </div>',
    ])


def conditions_menu():
    by_name = dict((c['NAME'], c) for c in CONDITIONS)
    groups = []
    for label, names in CONDITION_GROUPS:
        links = NL.join(
            '                  <li><a class="mega__link mega__link--plain" href="conditions/%s.html">'
            '<span class="mega__label"><span class="mega__name">%s</span>'
            '<span class="mega__desc">%s</span></span></a></li>'
            % (by_name[n]['SLUG'], n, CONDITION_BLURBS[n]) for n in names if n in by_name)
        groups.append(NL.join([
            '              <div class="mega__group">',
            '                <p class="mega__group-h">%s</p>' % label,
            '                <ul class="mega__list">',
            links,
            '                </ul>',
            '              </div>',
        ]))
    grouped = set(n for _, names in CONDITION_GROUPS for n in names)
    missing = [c['NAME'] for c in CONDITIONS if c['NAME'] not in grouped]
    assert not missing, 'conditions not in any menu group: %s' % missing
    post = POSTS[0]
    return NL.join([
        '          <div class="dropdown mega" id="mega-conditions">',
        '          <div class="mega__inner">',
        _intro('Conditions', 'Find what is causing your pain',
               'Each condition page covers the symptoms, the likely causes and how it is '
               'treated.', 'index.html#conditions', 'All conditions'),
        '            <div class="mega__grid mega__grid--conditions">',
        NL.join(groups),
        '            </div>',
        _feature('blog/%s.html' % post['SLUG'], post['CARD_IMG'], 'From the blog',
                 post['TITLE'], 'Read article'),
        '          </div>',
        '          </div>',
    ])


# Regions are laid out as three columns: Sydney has six clinics and fills one;
# the regional clinics share the other two, so no column runs much longer.
CLINIC_COLUMNS = [
    ['Sydney'],
    ['Southern Highlands', 'Newcastle &amp; Lake Macquarie'],
    ['Mid North Coast', 'North West NSW'],
]
NUMBER_WORDS_LC = {7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven'}


def clinics_menu():
    by_slug = dict((c[1], c) for c in CLINICS)
    regions = dict(REGIONS)
    placed = [r for col in CLINIC_COLUMNS for r in col]
    assert sorted(placed) == sorted(regions), 'regions missing from the clinics menu'

    def group(region):
        links = NL.join(
            '                  <li><a class="mega__link mega__link--plain" '
            'href="locations/podiatrist-%s.html"><span class="mega__label">'
            '<span class="mega__name">%s%s</span>'
            '<span class="mega__desc">%s</span></span></a></li>'
            % (slug, by_slug[slug][0],
               (' <span class="mega__tag">%s</span>' % TAGS[slug]) if slug in TAGS else '',
               by_slug[slug][2])
            for slug in regions[region])
        return NL.join([
            '              <div class="mega__group">',
            '                <p class="mega__group-h">%s</p>' % region,
            '                <ul class="mega__list">',
            links,
            '                </ul>',
            '              </div>',
        ])

    columns = NL.join(
        '            <div class="mega__col">\n%s\n            </div>' % NL.join(group(r) for r in col)
        for col in CLINIC_COLUMNS)
    return NL.join([
        '          <div class="dropdown mega" id="mega-clinics">',
        '          <div class="mega__inner">',
        _intro('Clinics',
               '%s clinics across New South Wales' % NUMBER_WORDS.get(len(CLINICS), len(CLINICS)),
               'Each clinic books into its own diary. %s take online bookings; for the others, '
               'call and we will book you in.' % NUMBER_WORDS_LC.get(len(BOOKING), len(BOOKING)).capitalize(),
               'locations.html', 'All clinics'),
        '            <div class="mega__grid mega__grid--conditions mega__grid--clinics">',
        columns,
        '            </div>',
        _feature('locations.html', 'bento-reception', 'Book an appointment',
                 'Choose your clinic and book straight into its diary', 'Choose a clinic'),
        '          </div>',
        '          </div>',
    ])
