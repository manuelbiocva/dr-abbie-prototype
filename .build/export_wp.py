# -*- coding: utf-8 -*-
"""Export every piece of prototype content as JSON for the WordPress import.

The prototype's data modules are the single source of truth for the rebuild:
clinics.py, services.py, condition_data.py, team_data.py and book_content.py.
This writes one file, wp-content.json, which the site pulls over HTTP and turns
into Clinics, Treatments, Conditions and Practitioners with their ACF fields.

Run:  python .build/export_wp.py
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from clinics import CLINICS, BOOKING, TAGS, GOOGLE, ROSTER, REGIONS, phone
from services import SERVICES
from condition_data import CONDITIONS as CONDS
from team_data import TEAM
import book_content
import conditions as cond_cards


def img(slot):
    """Published path of a generated image, relative to the prototype root."""
    return 'assets/img/%s.webp' % slot if slot else None


def clinics():
    out = []
    region_of = {}
    for region, slugs in REGIONS:
        for s in slugs:
            region_of[s] = region.replace('&amp;', '&')
    for name, slug, street, post, _ in CLINICS:
        tel, shown = phone(slug)
        g = GOOGLE.get(slug, (None, None, None))
        out.append({
            'slug': 'podiatrist-%s' % slug,
            'data_slug': slug,
            'title': 'Podiatrist in %s' % name,
            'name': name,
            'region': region_of.get(slug, ''),
            'fields': {
                'street': street,
                'suburb_state': post,
                'phone_display': shown,
                'phone_tel': tel,
                'booking_url': BOOKING.get(slug, ''),
                'maps_url': g[1] or '',
                'map_embed': g[2] or '',
                'tag': TAGS.get(slug, ''),
                'intro': 'Biomechanical assessment, custom orthotics and sports podiatry in %s.' % name,
            },
            'practitioners': ROSTER.get(slug, []),
        })
    return out


def treatments():
    out = []
    for s in SERVICES:
        out.append({
            'slug': s['SLUG'],
            'title': s['NAME'],
            'fields': {
                'intro': s.get('INTRO', ''),
                'fact1': s.get('FACT1', ''),
                'fact2': s.get('FACT2', ''),
                'who': s.get('WHO', ''),
                'step1': s.get('STEP1', ''),
                'step2': s.get('STEP2', ''),
                'step3': s.get('STEP3', ''),
            },
            'faq': [{'question': q, 'answer': a} for q, a in s.get('FAQ', [])],
            'conditions': [c[0] for c in s.get('CONDITIONS', [])],
            'hero': img(s.get('HERO_IMG')),
            'card': img(s.get('CARD_IMG') or s.get('ICON_SLOT')),
        })
    return out


def conditions():
    out = []
    for c in CONDS:
        card = cond_cards.CONDITIONS.get(c['NAME'])
        out.append({
            'slug': c['SLUG'],
            'title': c['NAME'],
            'fields': {
                'intro': c.get('INTRO', ''),
                'fact1': c.get('FACT1', ''),
                'fact2': c.get('FACT2', ''),
                'fact3': c.get('FACT3', ''),
                'causes': c.get('CAUSES', ''),
                'diagnose1': c.get('DIAGNOSE1', ''),
                'diagnose2': c.get('DIAGNOSE2', ''),
                'diagnose3': c.get('DIAGNOSE3', ''),
                'diagram_is_diagram': 1 if (card and card[2]) else 0,
            },
            'symptoms': list(c.get('SYMPTOMS', [])),
            'faq': [{'question': q, 'answer': a} for q, a in c.get('FAQ', [])],
            'treatments': list(c.get('TREATMENTS', [])),
            'hero': img(c.get('HERO_IMG')),
            'diagram': img(c.get('DIAGRAM')),
            'diagram_alt': c.get('DIAGRAM_ALT', ''),
            'understanding': understanding(c['SLUG']),
        })
    return out


def understanding(slug):
    e = book_content.CONDITIONS.get(slug) or book_content.SERVICES.get(slug)
    if not e:
        return None
    return {
        'intro': e.get('INTRO', ''),
        'types_title': e.get('TYPES_TITLE', ''),
        'types': [{'label': a, 'sub': b, 'text': t} for a, b, t in e.get('TYPES', [])],
        'points': [{'heading': h, 'html': html} for h, html in e.get('POINTS', [])],
    }


def practitioners():
    out = []
    for t in TEAM:
        out.append({
            'slug': t['SLUG'],
            'title': t['NAME'],
            'fields': {
                'role': t['ROLE'].replace('&middot;', '·'),
                'intro': t.get('INTRO', ''),
                'bio': ''.join('<p>%s</p>' % p for p in t.get('BIO', [])),
                'general_treatment_only': 1 if t.get('NOT_BIOMECHANICAL') else 0,
            },
            'qualifications': list(t.get('QUALIFICATIONS', [])),
            'memberships': list(t.get('MEMBERSHIPS', [])),
            'interests': list(t.get('INTERESTS', [])),
            'services': list(t.get('SERVICES', [])),
            'photo': img(t['PHOTO']) if t.get('PHOTO') else None,
        })
    return out


def main():
    data = {
        'generated': 'prototype/.build/export_wp.py',
        'clinics': clinics(),
        'treatments': treatments(),
        'conditions': conditions(),
        'practitioners': practitioners(),
    }
    out = os.path.join(os.path.dirname(HERE), 'wp-content.json')
    io.open(out, 'w', encoding='utf-8').write(json.dumps(data, ensure_ascii=False, indent=1))
    print('wrote %s' % out)
    for k in ('clinics', 'treatments', 'conditions', 'practitioners'):
        print('  %-14s %d' % (k, len(data[k])))
    print('  bytes %d' % os.path.getsize(out))


if __name__ == '__main__':
    main()
