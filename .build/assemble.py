#!/usr/bin/env python3
"""Assemble the prototype pages from shared header/footer + per-page main.

Global chrome stays byte-identical across every variant, so a reviewer is only
comparing the design direction — and so header/footer lift into WordPress once
rather than four times.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from clinics import CLINICS, fields, BOOKING, ROSTER, REGIONS, TAGS
from services import SERVICES, TEMP_TEXT
import people
import conditions
import reviews
from condition_data import CONDITIONS as COND_PAGES, TEMP_TEXT as COND_TEMP
import re
import math
import html as html_lib
from blog_data import POSTS, AUTHOR as POST_AUTHOR
from team_data import TEAM
import build_images
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

HEADER = open(os.path.join(ROOT, '.header.part'), encoding='utf-8').read()
# The Services and Conditions mega menus are generated from the page data.
import megamenu
HEADER = (HEADER.replace('{{MEGA_SERVICES}}', megamenu.services_menu())
                .replace('{{MEGA_CONDITIONS}}', megamenu.conditions_menu())
                .replace('{{MEGA_CLINICS}}', megamenu.clinics_menu()))
FOOTER = open(os.path.join(ROOT, '.footer.part'), encoding='utf-8').read()

# The direction signed off for the build. It renders without the review banner.


UTILITY_BAR = """
<!-- UTILITY BAR (V4 only) — phone, reach and booking above the sticky header -->
<div class="utility-bar">
  <div class="container utility-bar__inner">
    <span class="utility-bar__hide"><strong>Eleven clinics</strong> across New South Wales</span>
    <span class="utility-bar__hide">Podiatry since 1990</span>
    <span class="utility-bar__sep">
      <a href="tel:+61295454378">(02) 9545 4378</a>
    </span>
    <span><a href="locations.html">Find your clinic</a></span>
  </div>
</div>
"""

# --------------------------------------------------------------------------
# JSON-LD. Every variant page carries the same structured data as V1 — the
# rebuild is SEO-led, so a design variant that ships without schema is not a
# fair comparison. Nothing here is invented: unsupplied values stay as
# [CLIENT TO PROVIDE] and Review schema is omitted entirely until a real
# review feed is connected.
# --------------------------------------------------------------------------

SCHEMA = {}

SCHEMA['home'] = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalOrganization",
  "name": "Dr. Abbie Clinics",
  "alternateName": "AOL Footcare Centres",
  "url": "https://dr-abbie.com/",
  "telephone": "+61295454378",
  "email": "reception@dr-abbie.com",
  "foundingDate": "1990",
  "medicalSpecialty": "Podiatric",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "27 Monro Ave",
    "addressLocality": "Kirrawee",
    "addressRegion": "NSW",
    "postalCode": "2232",
    "addressCountry": "AU"
  },
  "sameAs": [
    "https://www.facebook.com/",
    "https://www.linkedin.com/",
    "https://www.youtube.com/"
  ]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I need a referral to see a podiatrist?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Podiatry is a primary contact profession in Australia, so you can book directly. If you are on a Medicare care plan your GP will refer you, and we can bill that."
      }
    },
    {
      "@type": "Question",
      "name": "What happens at a biomechanical assessment?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We assess how you stand, walk and load, identify the structure causing the pain, and explain what we found before any treatment starts. That is the Najjarine Biomechanical Assessment."
      }
    },
    {
      "@type": "Question",
      "name": "How much does an appointment cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Fees vary by appointment type and by clinic. Call the clinic you want to attend and reception will quote you before you book."
      }
    },
    {
      "@type": "Question",
      "name": "Can I claim on the day?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. We have HICAPS at every clinic, so private health rebates come off on the spot. Medicare care plans and NDIS plans are accepted."
      }
    },
    {
      "@type": "Question",
      "name": "Which clinic should I book at?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Each of our eleven clinics books into its own diary. Choose the one nearest you and you will see the practitioners who work there."
      }
    }
  ]
}
</script>"""


# Location template. Every [CLIENT TO PROVIDE] value becomes an ACF field on the
# WordPress location post type, so the eleven clinics share one template.
SCHEMA['location'] = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalClinic",
  "name": "Dr. Abbie Clinics — {{NAME}}",
  "parentOrganization": {
    "@type": "MedicalOrganization",
    "name": "Dr. Abbie Clinics"
  },
  "medicalSpecialty": "Podiatric",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "{{STREET}}",
    "addressLocality": "{{NAME}}",
    "addressRegion": "NSW",
    "postalCode": "{{POSTCODE}}",
    "addressCountry": "AU"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "[CLIENT TO PROVIDE]",
    "longitude": "[CLIENT TO PROVIDE]"
  },
  "telephone": "[CLIENT TO PROVIDE - CallRail tracking number for {{NAME}}]",
  "url": "https://dr-abbie.com/locations/podiatrist-{{SLUG}}/",{{RESERVE_ACTION}}
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"
      ],
      "opens": "[CLIENT TO PROVIDE]",
      "closes": "[CLIENT TO PROVIDE]"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Saturday",
      "opens": "[CLIENT TO PROVIDE]",
      "closes": "[CLIENT TO PROVIDE]"
    }
  ],
  "hasMap": "[CLIENT TO PROVIDE - Google Business Profile URL]"
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I need a referral to see a podiatrist at {{NAME}}?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Podiatry is a primary contact profession in Australia, so you can book directly. If you are on a Medicare care plan your GP will refer you, and we can bill that."
      }
    },
    {
      "@type": "Question",
      "name": "{{FAQ2_Q}}",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{{FAQ2_A_TEXT}}"
      }
    },
    {
      "@type": "Question",
      "name": "Do you treat children at this clinic?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{{FAQ3_A_TEXT}}"
      }
    },
    {
      "@type": "Question",
      "name": "How long is a first appointment?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Allow about 45 minutes. That covers the biomechanical assessment, the diagnosis and an explanation of the treatment plan before anything is prescribed."
      }
    },
    {
      "@type": "Question",
      "name": "Can I claim my health fund rebate on the spot?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. {{NAME}} has HICAPS, so private health rebates come off at reception. Medicare care plans and NDIS plans are accepted."
      }
    }
  ]
}
</script>"""


# Service template. MedicalProcedure rather than Service: these are clinical
# treatments, and the more specific type is what Google expects for them.
SCHEMA['service'] = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalProcedure",
  "name": "{{NAME}}",
  "procedureType": "https://schema.org/NoninvasiveProcedure",
  "bodyLocation": "Foot and lower limb",
  "url": "https://dr-abbie.com/services/{{SLUG}}/",
  "provider": {
    "@type": "MedicalOrganization",
    "name": "Dr. Abbie Clinics",
    "url": "https://dr-abbie.com/"
  }
}
</script>
<script type="application/ld+json">
{{FAQ_SCHEMA}}
</script>"""


# Condition template. MedicalCondition is the type Google expects for a page
# about a health problem, as distinct from MedicalProcedure for a treatment.
SCHEMA['condition'] = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalCondition",
  "name": "{{NAME}}",
  "url": "https://dr-abbie.com/conditions/{{SLUG}}/",
  "associatedAnatomy": { "@type": "AnatomicalStructure", "name": "Foot and lower limb" },
  "possibleTreatment": {{TREATMENT_SCHEMA}}
}
</script>
<script type="application/ld+json">
{{FAQ_SCHEMA}}
</script>"""

TOPBAR = """
<!-- UTILITY BAR (V6 only) - address, hours and phone above the header -->
<div class="topbar">
  <div class="container topbar__inner">
    <span class="topbar__item topbar__item--hide">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 21s7-5.6 7-11a7 7 0 1 0-14 0c0 5.4 7 11 7 11Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><circle cx="12" cy="10" r="2.5" stroke="currentColor" stroke-width="1.7"/></svg>
      27 Monro Ave, Kirrawee NSW 2232
    </span>
    <span class="topbar__item topbar__item--hide">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.7"/><path d="M12 7v5l3 2" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
      <span class="placeholder">[OPENING HOURS]</span>
    </span>
    <span class="topbar__item topbar__end">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M7.5 3.5 9.6 7.9 7.7 9.8a12 12 0 0 0 6.2 6.2l1.9-1.9 4.4 2.1v3.4a1.5 1.5 0 0 1-1.6 1.5A17.4 17.4 0 0 1 2.9 5.6 1.5 1.5 0 0 1 4.4 4h3.1Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
      <strong>Reception:</strong> <a href="tel:+61295454378">(02) 9545 4378</a>
    </span>
  </div>
</div>
"""

# Blog. The posts use BlogPosting, the Article subtype for blog content, so the
# hub's Blog.blogPost list and the post pages describe the same thing. No
# datePublished and no named author: both are unknown until launch, and a
# made-up date or byline in structured data is exactly what it must not carry.
SCHEMA['blog'] = """
<script type="application/ld+json">
{{BLOG_SCHEMA}}
</script>"""

# Team. Person, not Physician: the brief lists "Person + Physician", but in
# schema.org Physician is a medical-practice organisation type for medical
# doctors, and a podiatrist marked up as one is exactly the misleading claim
# the title "Dr" already has to be qualified against. jobTitle says Podiatrist.
SCHEMA['locations'] = """
<script type="application/ld+json">
{{CLINICS_SCHEMA}}
</script>"""

SCHEMA['contact'] = """
<script type="application/ld+json">
{{CONTACT_SCHEMA}}
</script>"""

SCHEMA['team'] = """
<script type="application/ld+json">
{{TEAM_SCHEMA}}
</script>"""

SCHEMA['practitioner'] = """
<script type="application/ld+json">
{{PERSON_SCHEMA}}
</script>
<script type="application/ld+json">
{{BREADCRUMB_SCHEMA}}
</script>"""

SCHEMA['post'] = """
<script type="application/ld+json">
{{ARTICLE_SCHEMA}}
</script>
<script type="application/ld+json">
{{BREADCRUMB_SCHEMA}}
</script>"""


HEAD = """<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<link rel="stylesheet" href="assets/css/design-system.css">
<link rel="stylesheet" href="assets/css/components.css">
<link rel="stylesheet" href="assets/css/theme.css">
{schema}
</head>
<body>

<a class="skip-link" href="#main">Skip to content</a>

"""


def service_card(sv, href_prefix='services/'):
    """Treatment card that links a condition page to a service page."""
    arrow = ('<svg width="14" height="14" viewBox="0 0 14 14" fill="none" '
             'aria-hidden="true"><path d="M3 7h8M7.5 3.5L11 7l-3.5 3.5" stroke="currentColor" '
             'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    return ('        <a class="card cond-card reveal" href="%s%s.html">' + chr(10) +
            '          <div class="cond-card__media"><img src="assets/img/%s.webp" '
            'srcset="assets/img/%s.webp 1x, assets/img/%s@2x.webp 2x" width="640" '
            'height="400" alt="%s" loading="lazy" decoding="async" '
            'sizes="(min-width: 900px) 25vw, 100vw"></div>' + chr(10) +
            '          <h3>%s</h3>' + chr(10) +
            '          <p>%s</p>' + chr(10) +
            '          <span class="card__more">Read more %s</span>' + chr(10) +
            '        </a>' + chr(10)) % (
        href_prefix, sv['SLUG'], sv['CARD_IMG'], sv['CARD_IMG'], sv['CARD_IMG'],
        sv['ALT'], sv['NAME'], sv['INTRO'], arrow)


# Templates link conditions to the generic condition.html. Every condition now
# has its own page, so a link whose text names one is pointed at that page.
# Resolved from the data rather than typed into each template, so a condition
# added to condition_data.py is linked everywhere on the next build. Links that
# name no single condition ("Conditions" in the nav) are left alone.
COND_SLUGS = {c['NAME'].lower(): c['SLUG'] for c in COND_PAGES}
UNRESOLVED_COND_LINKS = set()


def link_conditions(html, out_name):
    def _one(m):
        body = m.group(2)
        h3 = re.search(r'<h3>(.*?)</h3>', body, re.S)
        text = re.sub(r'<[^>]+>', '', h3.group(1) if h3 else body)
        text = re.sub(r'\s+', ' ', text).strip().lower()
        slug = COND_SLUGS.get(text)
        if not slug:
            if text not in ('conditions', 'all conditions'):
                UNRESOLVED_COND_LINKS.add((out_name, text))
            return m.group(0)
        return m.group(0).replace('href="condition.html"',
                                  'href="conditions/%s.html"' % slug, 1)
    return re.sub(r'(<a\b[^>]*href="condition\.html"[^>]*>)(.*?)</a>', _one, html,
                  flags=re.S)


# Same idea for people. The home team rail and the slider/grid in people.py
# link every portrait to the generic practitioner.html; a link that names a
# practitioner now goes to that practitioner's page.
PEOPLE_SLUGS = [(t['NAME'], t['SLUG']) for t in TEAM]
UNRESOLVED_PEOPLE_LINKS = set()


SERVICE_BY_NAME = dict((sv['NAME'].replace('’', "'"), sv['SLUG']) for sv in SERVICES)


def link_services(html, out_name):
    """Links to the generic service.html whose text names one treatment
    ("Shockwave Therapy", "About Shockwave Therapy") go to that treatment."""
    def _one(m):
        text = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', m.group(2)))
        text = text.replace('&rsquo;', "'").replace('’', "'").replace('&#39;', "'")
        hits = [slug for name, slug in SERVICE_BY_NAME.items() if name in text]
        if len(hits) != 1:
            return m.group(0)
        return m.group(0).replace('href="service.html"', 'href="services/%s.html"' % hits[0], 1)
    return re.sub(r'(<a\b[^>]*href="service\.html"[^>]*>)(.*?)</a>', _one, html, flags=re.S)


# --------------------------------------------------------------------------
# Booking. Every button marked data-track="book" is authored with href="#";
# where it goes is decided here, per page, so the rule lives in one place:
#   - a clinic with a Nookal link: that clinic's link, on every book button on
#     its page (header, hero, treatments, closing, mobile bar). Opens in a new
#     tab so the site stays open behind the booking and the click is tracked
#     before the browser leaves.
#   - a clinic without one: the button becomes "Call to book". It never points
#     at another clinic's diary.
#   - a practitioner page: #book, the list of clinics where they take bookings.
#   - everywhere else: locations.html, the choose-your-clinic page.
# --------------------------------------------------------------------------
PHONE = '+61295454378'
NEW_TAB = '<span class="sr-only"> (opens online booking in a new tab)</span>'


def book_button(url, location, source, label, cls='btn btn--book btn--sm', sr_place=''):
    """A single booking button for a known clinic, online or by phone."""
    if url:
        return ('<a class="%s" href="%s" target="_blank" rel="noopener" data-track="book" '
                'data-book-method="online" data-location="%s" data-source="%s">%s'
                '<span class="sr-only">%s (opens online booking in a new tab)</span></a>'
                % (cls, url, location, source, label, sr_place))
    return ('<a class="%s" href="tel:%s" data-track="book" data-book-method="phone" '
            'data-location="%s" data-source="%s">Call to book<span class="sr-only">%s</span></a>'
            % (cls, PHONE, location, source, sr_place))


def apply_booking(html, mode, target=None, location=None):
    def _one(m):
        tag, body = m.group(1), m.group(2)
        if 'href="#"' not in tag:
            return m.group(0)
        if mode == 'online':
            tag = tag.replace('href="#"', 'href="%s" target="_blank" rel="noopener" '
                              'data-book-method="online"' % target, 1)
            body = body + NEW_TAB
        elif mode == 'phone':
            tag = tag.replace('href="#"', 'href="tel:%s" data-book-method="phone"' % PHONE, 1)
            body = re.sub(r'^\s*[^<]+', 'Call to book ', body, count=1)
        else:
            tag = tag.replace('href="#"', 'href="%s"' % target, 1)
        if location and 'data-location=' not in tag:
            tag = tag.replace('data-track="book"', 'data-track="book" data-location="%s"' % location, 1)
        return tag + body + '</a>'
    return re.sub(r'(<a\b[^>]*data-track="book"[^>]*>)(.*?)</a>', _one, html, flags=re.S)


def link_people(html, out_name):
    def _one(m):
        text = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', m.group(2)))
        hits = [slug for name, slug in PEOPLE_SLUGS if name in text]
        if len(hits) != 1:
            UNRESOLVED_PEOPLE_LINKS.add((out_name, text.strip()[:40]))
            return m.group(0)
        return m.group(0).replace('href="practitioner.html"',
                                  'href="team/%s.html"' % hits[0], 1)
    return re.sub(r'(<a\b[^>]*href="practitioner\.html"[^>]*>)(.*?)</a>', _one, html,
                  flags=re.S)


# --------------------------------------------------------------------------
# Photographs. Two slots cut from the same source file look like one picture
# used twice, which is how the home page ended up showing the orthotics,
# shockwave and mobilisation photographs twice each. The build checks every
# page against the source each slot was cut from.
# --------------------------------------------------------------------------
SLOT_SOURCE = dict((job[0], job[1]) for job in build_images.JOBS)
IMG_DIR = os.path.join(ROOT, 'assets', 'img')
ARROW = ('<svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true">'
         '<path d="M3 7h8M7.5 3.5L11 7l-3.5 3.5" stroke="currentColor" stroke-width="1.7" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')


def slots_in(html):
    return set(re.findall(r'assets/img/([A-Za-z0-9_-]+?)(?:@2x)?\.webp', html))


# Art-directed cuts of one photograph, served to different viewports through
# <picture>. Only one is ever on screen, so they are not a repeat.
SAME_PHOTO_BY_DESIGN = {'hero-portrait'}


def repeated_photos(html):
    # the header's mega menu images are hidden until a menu is opened
    html = re.sub(r'<header class="site-header">.*?</header>', '', html, flags=re.S)
    by_source = {}
    for slot in slots_in(html):
        if slot in SLOT_SOURCE and slot not in SAME_PHOTO_BY_DESIGN:
            by_source.setdefault(SLOT_SOURCE[slot], set()).add(slot)
    return sorted('/'.join(sorted(v)) for v in by_source.values() if len(v) > 1)


def img_size(slot):
    with Image.open(os.path.join(IMG_DIR, slot + '.webp')) as im:
        return im.size


def img_tag(slot, alt, sizes, eager=False):
    w, h = img_size(slot)
    return ('<img src="assets/img/%s.webp" srcset="assets/img/%s.webp 1x, assets/img/%s@2x.webp 2x" '
            'width="%d" height="%d" alt="%s" loading="%s" decoding="async" sizes="%s">'
            % (slot, slot, slot, w, h, alt, 'eager' if eager else 'lazy', sizes))


def read_time(post):
    text = re.sub(r'<[^>]+>', ' ', post['BODY'] + ' '.join(post['SUMMARY']))
    return max(1, int(math.ceil(len(text.split()) / 200.0)))


def word_count(post):
    return len(re.sub(r'<[^>]+>', ' ', post['BODY']).split())


def post_card(post, detail=False, delay=0):
    """A blog card. The home page shows the short form; the hub and the post
    pages add the excerpt and reading time."""
    lines = [
        '        <a class="card post-card reveal" href="blog/%s.html"%s>'
        % (post['SLUG'], (' data-reveal-delay="%d"' % delay) if delay else ''),
        '          <div class="post-card__img">%s</div>'
        % img_tag(post['CARD_IMG'], post['CARD_ALT'], '(min-width: 1100px) 25vw, 100vw'),
        '          <div class="post-card__body">',
        '            <span class="post-card__cat">%s</span>' % post['CATEGORY'],
        '            <h3>%s</h3>' % post['TITLE'],
    ]
    if detail:
        lines += [
            '            <p class="post-card__excerpt">%s</p>' % post['EXCERPT'],
            '            <span class="post-card__meta">%d min read</span>' % read_time(post),
        ]
    lines += [
        '            <span class="card__more">Read article %s</span>' % ARROW,
        '          </div>',
        '        </a>',
    ]
    return '\n'.join(lines) + '\n'


def post_feature(post):
    return '\n'.join([
        '      <a class="card post-feature reveal" href="blog/%s.html">' % post['SLUG'],
        '        <div class="post-feature__img">%s</div>'
        % img_tag(post['CARD_IMG'], post['CARD_ALT'], '(min-width: 900px) 55vw, 100vw'),
        '        <div class="post-feature__body">',
        '          <span class="post-card__cat">Latest &middot; %s</span>' % post['CATEGORY'],
        '          <h2 class="post-feature__title">%s</h2>' % post['TITLE'],
        '          <p class="post-feature__excerpt">%s</p>' % post['EXCERPT'],
        '          <span class="post-feature__meta"><span data-temp>%s</span> &middot; %d min read</span>'
        % (post['DATE'], read_time(post)),
        '          <span class="card__more">Read article %s</span>' % ARROW,
        '        </div>',
        '      </a>',
    ])


def clinic_cards():
    return ('\n').join(
        '        <a class="loc-card reveal" href="locations/podiatrist-%s.html">'
        '<h3>%s</h3><span class="loc-card__meta">%s, %s</span></a>'
        % (slug, name, street, post)
        for name, slug, street, post, _ in CLINICS)


def build(page, out_name, title, desc, canonical, booklabel='Book a Session',
          subdir='', tokens=None, booking=('chooser', 'locations.html', None),
          blocks=None):
    main = open(os.path.join(HERE, '%s.main.html' % page), encoding='utf-8').read()
    for key, on in (blocks or {}).items():
        main = re.sub(r'<!--IF:%s-->(.*?)<!--/IF:%s-->' % (key, key),
                      (lambda m: m.group(1)) if on else '', main, flags=re.S)

    head = HEAD.format(title=title, desc=desc, canonical=canonical,
                       schema=SCHEMA.get(page, ''),
                       p='' if page == 'home' else 'location.html#')

    chrome = HEADER

    footer = FOOTER
    if booklabel != 'Book a Session':
        footer = footer.replace(
            '<a class="btn btn--book btn--sm" href="#" data-track="book" data-source="mobile-bar">Book a Session</a>',
            '<a class="btn btn--book btn--sm" href="#" data-track="book" data-source="mobile-bar">%s</a>' % booklabel)

    out = head + chrome + main + footer
    if tokens:
        # the schema lives in <head>, so substitution runs over the whole page
        for k, v in tokens.items():
            # the data modules also carry structured values (condition lists,
            # FAQ pairs) that the loop turns into markup; only strings get
            # substituted directly
            if isinstance(v, str):
                out = out.replace('{{%s}}' % k, v)
    out = link_conditions(out, out_name)
    out = link_people(out, out_name)
    out = link_services(out, out_name)
    out = apply_booking(out, *booking)
    out = bust(out)

    if subdir:
        # Everything is authored as if it sat at the site root. A page written
        # into a subfolder needs those paths lifted one level -- except links
        # to its own siblings, which lose the folder prefix instead.
        # One pass, not two. Stripping the sibling prefix first and then
        # prefixing everything else meant the just-stripped links were caught
        # by the second rule and pushed up a level as well.
        def _depth(m):
            attr, url = m.group(1), m.group(2)
            if url.startswith(subdir + '/'):
                return '%s="%s' % (attr, url[len(subdir) + 1:])   # sibling
            return '%s="../%s' % (attr, url)                      # up one level
        out = re.sub(r'(href|src)="(?!https?:|//|#|mailto:|tel:|\.\./)([^"]*)',
                     _depth, out)

        # srcset too. It holds a comma separated list of "url descriptor"
        # pairs, so each url is lifted individually. Missing this left every
        # image broken: src was rewritten correctly but the browser prefers
        # srcset when both are present, so the corrected src was never used.
        def _srcset(m):
            out_parts = []
            for part in m.group(1).split(','):
                part = part.strip()
                if not part:
                    continue
                bits = part.split(None, 1)
                url = bits[0]
                rest = (' ' + bits[1]) if len(bits) > 1 else ''
                if not re.match(r'https?:|//|\.\./|data:', url):
                    url = (url[len(subdir) + 1:] if url.startswith(subdir + '/')
                           else '../' + url)
                out_parts.append(url + rest)
            return 'srcset="' + ', '.join(out_parts) + '"'
        out = re.sub(r'srcset="([^"]*)"', _srcset, out)
    name = os.path.join(subdir, out_name) if subdir else out_name
    dest = os.path.join(ROOT, name)
    if subdir:
        d = os.path.dirname(dest)
        if not os.path.isdir(d):
            os.makedirs(d)
    open(dest, 'w', encoding='utf-8').write(out)

    problems = []
    for tag in ('div', 'section', 'main', 'nav'):
        o = len(re.findall(r'<%s[\s>]' % tag, out))
        c = len(re.findall(r'</%s>' % tag, out))
        if o != c:
            problems.append('<%s> %d/%d' % (tag, o, c))
    for pair in repeated_photos(out):
        problems.append('same photo twice: ' + pair)
    if '{{' in out:
        problems.append('unreplaced ' + ', '.join(sorted(set(re.findall(r'\{\{\w+\}\}', out)))))
    flag = ('  !! ' + ', '.join(problems)) if problems else '  ok'
    print('  %-22s %6d bytes%s' % (name, len(out), flag))


# page fragment, output filename, title, meta description, canonical, book label.
# The location filename carries its clinic slug -- one page per clinic, named
# the way the live URL will be (/locations/podiatrist-kirrawee/).
# page fragment, output filename, title, meta description, canonical, book label
PAGES = [
    ('home', 'index.html',
     'Podiatrist in Sydney &amp; NSW | Dr. Abbie Clinics',
     'Podiatry across 11 NSW clinics since 1990. The Najjarine Biomechanical Assessment finds the cause of lower limb pain, not just the symptoms.',
     'https://dr-abbie.com/', 'Book a Session'),
]

def asset_version(rel):
    """Short content hash for a stylesheet or script.

    Reviewers open these pages straight off disk, where the browser will hold
    on to a cached main.js or theme css indefinitely -- a change can look like
    it simply did not happen. Appending the hash makes every edit a new URL.
    """
    import hashlib
    path = os.path.join(HERE, '..', rel)
    if not os.path.exists(path):
        return ''
    with open(path, 'rb') as fh:
        return '?v=' + hashlib.sha1(fh.read()).hexdigest()[:8]


def bust(html):
    """Stamp every local css/js reference with its content hash."""
    def sub(m):
        rel = m.group(2)
        return m.group(1) + rel + asset_version(rel) + m.group(3)
    return re.sub(r'(href="|src=")(assets/(?:css|js)/[A-Za-z0-9._-]+)(")', sub, html)


def check_css():
    """Structural check on every stylesheet before a build.

    A lost comment opener does not raise anywhere -- the browser silently drops
    every rule until it resyncs, so a whole section can go unstyled while the
    HTML still looks correct. That happened once to the logo carousel; this
    catches it at build time instead of in a screenshot.
    """
    import glob
    bad = []
    for f in sorted(glob.glob(os.path.join(HERE, '..', 'assets', 'css', '*.css'))):
        css = open(f, encoding='utf-8').read()
        name = os.path.basename(f)
        stripped = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
        if css.count('/*') != css.count('*/'):
            bad.append('%s: %d /* vs %d */' % (name, css.count('/*'), css.count('*/')))
        elif '*/' in stripped or '/*' in stripped:
            bad.append('%s: orphaned comment delimiter' % name)
        if stripped.count('{') != stripped.count('}'):
            bad.append('%s: braces %d/%d' % (name, stripped.count('{'), stripped.count('}')))
    for b in bad:
        print('  !! CSS ' + b)
    return not bad


if __name__ == '__main__':
    if not check_css():
        raise SystemExit('stylesheet is structurally broken -- fix before building')
    print('assembling pages...')
    for page, out_name, title, desc, canon, bl in PAGES:
        src = os.path.join(HERE, '%s.main.html' % page)
        if os.path.exists(src):
            tokens = None
            if page == 'home':
                tokens = {
                    'HOME_POST_CARDS': ''.join(
                        post_card(pt, delay=i * 60) for i, pt in enumerate(POSTS[:4])),
                    'HOME_TEAM_RAIL': people.team_rail(4),
                    # Generated so each card links to its own clinic. The hand-written
                    # version sent all eleven to the Kirrawee page.
                    'HOME_CLINIC_FINDER': '\n'.join(
                        '        <a class="loc-card reveal" href="locations/podiatrist-%s.html">'
                        '<h3>%s%s</h3><span class="loc-card__meta">%s, %s</span>'
                        '<span class="loc-card__hours">%s</span></a>'
                        % (slug, name,
                           (' <span class="loc-card__tag">%s</span>' % TAGS[slug]) if slug in TAGS else '',
                           street, post,
                           'Book online' if slug in BOOKING else 'Book by phone')
                        for name, slug, street, post, _ in CLINICS),
                }
            build(page, out_name, title, desc, canon, bl, tokens=tokens)
        else:
            print('  !! missing fragment: %s.main.html' % page)

    # One template, eleven clinics, written into /locations/ so the prototype
    # matches the live URL shape (/locations/podiatrist-kirrawee/).
    for name, slug, street, post, overrides in CLINICS:
        f = fields(name, slug, street, post, overrides)
        f['POSTCODE'] = post.replace('NSW ', '')
        # The FAQ schema carries the same question and answer the page shows. It
        # used to hard-code Kirrawee's answer ("our head office, orthotics made
        # on site") into every clinic's structured data.
        for k in ('FAQ2_A', 'FAQ3_A'):
            f[k + '_TEXT'] = json.dumps(html_lib.unescape(re.sub(r'<[^>]+>', '', f[k])),
                                        ensure_ascii=False)[1:-1]
        url = BOOKING.get(slug)
        if url:
            here = [people.BY_SLUG[s] for s in ROSTER[slug]]
            f['PRACTITIONER_SLIDER'] = people.hero_slider('Practitioners at %s' % name, here)
            f['PRACTITIONER_GRID'] = people.card_grid(here)
            f['PRAC_EYEBROW'] = 'At this clinic'
            f['PRAC_H1'], f['PRAC_H2'] = 'Practitioners', 'at %s' % name
            f['ROSTER_LEDE'] = ('%s take%s online bookings at %s. Choose who you would like '
                                'to see when you book, or choose Any Available for the '
                                'soonest appointment.' % (
                                    'These %s practitioners' % {2: 'two', 3: 'three', 4: 'four',
                                                                5: 'five', 6: 'six'}[len(here)]
                                    if len(here) > 1 else here[0]['NAME'],
                                    '' if len(here) > 1 else 's', name))
            f['TREATMENT_LEDE'] = ('Every treatment below books online into the %s diary.' % name)
            f['BOOKING_STEPS'] = '\n'.join([
                '      <div class="book-steps reveal">',
                '        <ol class="book-steps__list">',
                '          <li><span class="book-steps__n">1</span><span><strong>Open the %s diary</strong> '
                'from any Book at %s button.</span></li>' % (name, name),
                '          <li><span class="book-steps__n">2</span><span><strong>Choose a practitioner</strong>, '
                'or Any Available.</span></li>',
                '          <li><span class="book-steps__n">3</span><span><strong>Pick a time</strong> '
                'and confirm your details.</span></li>',
                '        </ol>',
                '        ' + book_button(url, slug, 'practitioners', 'Book at %s' % name,
                                         cls='btn btn--book'),
                '      </div>',
            ])
            f['RESERVE_ACTION'] = ('\n  "potentialAction": {\n    "@type": "ReserveAction",\n'
                                   '    "target": "%s"\n  },' % url)
            booking = ('online', url, slug)
        else:
            # No Nookal link and no roster: the whole team, headed as the
            # team, and booking by phone.
            f['PRACTITIONER_SLIDER'] = people.hero_slider('Our practitioners')
            f['PRACTITIONER_GRID'] = people.card_grid(people.WITH_PHOTO)
            f['PRAC_EYEBROW'] = 'Our team'
            f['PRAC_H1'], f['PRAC_H2'] = 'Our', 'practitioners'
            f['ROSTER_LEDE'] = ('<span data-temp>Call <a href="tel:%s" data-location="%s">'
                                '(02) 9545 4378</a> to check who is consulting at %s, and we '
                                'will book you in.</span>' % (PHONE, slug, name))
            f['TREATMENT_LEDE'] = ('Call to book any of these treatments at %s.' % name)
            f['BOOKING_STEPS'] = ''
            f['RESERVE_ACTION'] = ''
            booking = ('phone', None, slug)
        plain = street.replace('&mdash;', '-').replace('–', '-')
        build('location', 'podiatrist-%s.html' % slug,
              'Podiatrist in %s | Dr. Abbie Clinics' % name,
              'Podiatrist in %s at %s. Biomechanical assessment, custom orthotics, '
              'shockwave therapy and sports podiatry.' % (name, plain),
              'https://dr-abbie.com/locations/podiatrist-%s/' % slug,
              'Book at %s' % name if url else 'Call to book',
              subdir='locations', tokens=f, booking=booking)

    # One template, ten treatments, written into /services/ so the prototype
    # matches the live URL shape (/services/shockwave-therapy/).
    for sv in SERVICES:
        f = dict(sv)
        for k, v in TEMP_TEXT.items():
            f = dict((kk, v if vv == k else vv) for kk, vv in f.items())
        f['NAME_LC'] = sv['NAME'][0].lower() + sv['NAME'][1:]
        f['PRACTITIONER_SLIDER'] = people.hero_slider('Our practitioners')
        f['REVIEW_CARDS'] = reviews.cards(reviews.REVIEWS[sv['SLUG']])
        f['RATING_BLOCK'] = reviews.rating_block('Based on 286 Google reviews across our clinics')

        f['CONDITION_CARDS'] = ''.join(
            conditions.card(n, d) for n, d in sv['CONDITIONS'])

        f['CLINIC_CARDS'] = ('\n').join(
            '        <a class="loc-card reveal" href="locations/podiatrist-%s.html">'
            '<h3>%s</h3><span class="loc-card__meta">%s, %s</span></a>'
            % (slug, name, street, post)
            for name, slug, street, post, _ in CLINICS)

        def _answer(a):
            return ('<span data-temp>%s</span>' % a[5:]) if a.startswith('TEMP:') else a

        f['FAQ_ITEMS'] = ('\n').join(
            '        <div class="acc-item reveal">'
            + '\n          <h3><button class="acc-trigger" aria-expanded="false">'
            + q + ' <svg width="20" height="20" viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M3 4.5L6 7.5L9 4.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></button></h3>'
            + '\n          <div class="acc-panel"><div><div class="acc-panel__inner">'
            + '<p>' + _answer(a) + '</p></div></div></div>'
            + '\n        </div>'
            for q, a in sv['FAQ'])

        f['FAQ_SCHEMA'] = json.dumps({
            '@context': 'https://schema.org', '@type': 'FAQPage',
            'mainEntity': [{'@type': 'Question', 'name': q,
                            'acceptedAnswer': {'@type': 'Answer',
                                               'text': a[5:] if a.startswith('TEMP:') else a}}
                           for q, a in sv['FAQ']]}, indent=2, ensure_ascii=False)

        build('service', '%s.html' % sv['SLUG'],
              '%s | Dr. Abbie Clinics' % sv['NAME'],
              sv['INTRO'][:155],
              'https://dr-abbie.com/services/%s/' % sv['SLUG'],
              'Book a Session', subdir='services', tokens=f)

    # One template, eleven conditions, written into /conditions/.
    for cd in COND_PAGES:
        f = dict(cd)
        for k, v in COND_TEMP.items():
            f = dict((kk, v if vv == k else vv) for kk, vv in f.items())
        f['NAME_LC'] = cd['NAME'][0].lower() + cd['NAME'][1:]
        f['PRACTITIONER_SLIDER'] = people.hero_slider('Our practitioners')

        f['SYMPTOM_ITEMS'] = ('\n').join(
            '            <li>%s</li>' % x for x in cd['SYMPTOMS'])

        by_slug = dict((s['SLUG'], s) for s in SERVICES)
        f['TREATMENT_CARDS'] = ''.join(
            service_card(by_slug[sl]) for sl in cd['TREATMENTS'] if sl in by_slug)

        f['CLINIC_CARDS'] = ('\n').join(
            '        <a class="loc-card reveal" href="locations/podiatrist-%s.html">'
            '<h3>%s</h3><span class="loc-card__meta">%s, %s</span></a>'
            % (slug, name, street, post)
            for name, slug, street, post, _ in CLINICS)

        f['REVIEW_CARDS'] = reviews.cards(cd['REVIEWS'])
        f['RATING_BLOCK'] = reviews.rating_block(
            'Based on 286 Google reviews across our clinics')

        def _ans(a):
            return ('<span data-temp>%s</span>' % a[5:]) if a.startswith('TEMP:') else a
        f['FAQ_ITEMS'] = ('\n').join(
            '        <div class="acc-item reveal">'
            + '\n          <h3><button class="acc-trigger" aria-expanded="false">'
            + q + ' <svg width="20" height="20" viewBox="0 0 12 12" fill="none" '
            'aria-hidden="true"><path d="M3 4.5L6 7.5L9 4.5" stroke="currentColor" '
            'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
            '</button></h3>'
            + '\n          <div class="acc-panel"><div><div class="acc-panel__inner">'
            + '<p>' + _ans(a) + '</p></div></div></div>'
            + '\n        </div>'
            for q, a in cd['FAQ'])

        f['FAQ_SCHEMA'] = json.dumps({
            '@context': 'https://schema.org', '@type': 'FAQPage',
            'mainEntity': [{'@type': 'Question', 'name': q,
                            'acceptedAnswer': {'@type': 'Answer',
                                               'text': a[5:] if a.startswith('TEMP:') else a}}
                           for q, a in cd['FAQ']]}, indent=2, ensure_ascii=False)
        f['TREATMENT_SCHEMA'] = json.dumps(
            [{'@type': 'MedicalProcedure', 'name': by_slug[sl]['NAME'],
              'url': 'https://dr-abbie.com/services/%s/' % sl}
             for sl in cd['TREATMENTS'] if sl in by_slug], indent=2, ensure_ascii=False)

        build('condition', '%s.html' % cd['SLUG'],
              '%s | Dr. Abbie Clinics' % cd['NAME'],
              cd['INTRO'][:155],
              'https://dr-abbie.com/conditions/%s/' % cd['SLUG'],
              'Book a Session', subdir='conditions', tokens=f)

    # Blog: the hub at /blog.html, and one template, five posts, in /blog/.
    by_slug = dict((sv['SLUG'], sv) for sv in SERVICES)
    cond_by_name = dict((c['NAME'], c) for c in COND_PAGES)
    SITE = 'https://dr-abbie.com'
    ORG = {'@type': 'Organization', 'name': 'Dr. Abbie Clinics', 'url': SITE + '/'}

    def first_sentence(text):
        return text.split('. ')[0].rstrip('.') + '.'

    hub = {
        'FEATURED_POST': post_feature(POSTS[0]),
        'POST_CARDS': ''.join(post_card(pt, detail=True, delay=i * 60)
                              for i, pt in enumerate(POSTS[1:])),
        'CONDITION_LINKS': '\n'.join(
            '            <li><a href="conditions/%s.html">%s</a></li>' % (c['SLUG'], c['NAME'])
            for c in COND_PAGES),
        'SERVICE_LINKS': '\n'.join(
            '            <li><a href="services/%s.html">%s</a></li>' % (sv['SLUG'], sv['NAME'])
            for sv in SERVICES),
        'BLOG_SCHEMA': json.dumps({
            '@context': 'https://schema.org', '@type': 'Blog',
            'name': 'Dr. Abbie Clinics blog', 'url': SITE + '/blog/', 'inLanguage': 'en-AU',
            'publisher': ORG,
            'blogPost': [{'@type': 'BlogPosting', 'headline': pt['TITLE'],
                          'url': '%s/blog/%s/' % (SITE, pt['SLUG'])} for pt in POSTS],
        }, indent=2, ensure_ascii=False),
    }
    build('blog', 'blog.html',
          'Podiatry Advice and Foot Health Blog | Dr. Abbie Clinics',
          'Plain-English advice from our podiatrists on heel pain, orthotics, children&rsquo;s '
          'feet, shockwave therapy and when to see a podiatrist.',
          SITE + '/blog/', 'Book a Session', tokens=hub)

    for n, pt in enumerate(POSTS):
        f = dict((k, v) for k, v in pt.items() if isinstance(v, str))
        f['AUTHOR'] = POST_AUTHOR
        f['READ_TIME'] = str(read_time(pt))
        f['HERO_W'], f['HERO_H'] = [str(x) for x in img_size(pt['HERO_IMG'])]
        f['SUMMARY_ITEMS'] = '\n'.join('              <li>%s</li>' % x for x in pt['SUMMARY'])
        f['TOC_ITEMS'] = '\n'.join(
            '              <li><a href="#%s">%s</a></li>' % (hid, re.sub(r'<[^>]+>', '', text))
            for hid, text in re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', pt['BODY']))

        cards = []
        for i, (kind, key) in enumerate(pt['RELATED']):
            if kind == 'condition':
                c = cond_by_name[key]
                cards.append(conditions.card(key, first_sentence(c['INTRO']),
                                             'conditions/%s.html' % c['SLUG']))
            else:
                cards.append(service_card(by_slug[key]))
        f['RELATED_CARDS'] = ''.join(cards)
        f['CLINIC_CARDS'] = clinic_cards()

        # Three other posts, in order after this one, skipping any whose card
        # photograph is already on this page.
        taken = set(SLOT_SOURCE.get(sl) for sl in
                    slots_in(pt['BODY'] + f['RELATED_CARDS']) | {pt['HERO_IMG'], 'cta-band'})
        more = []
        for other in POSTS[n + 1:] + POSTS[:n]:
            if SLOT_SOURCE.get(other['CARD_IMG']) in taken:
                continue
            more.append(other)
            taken.add(SLOT_SOURCE.get(other['CARD_IMG']))
            if len(more) == 3:
                break
        f['MORE_POSTS'] = ''.join(post_card(o, detail=True, delay=i * 60)
                                  for i, o in enumerate(more))

        url = '%s/blog/%s/' % (SITE, pt['SLUG'])
        article = {
            '@context': 'https://schema.org', '@type': 'BlogPosting',
            'headline': pt['TITLE'], 'description': pt['EXCERPT'],
            'url': url, 'mainEntityOfPage': {'@type': 'WebPage', '@id': url},
            'articleSection': pt['CATEGORY'], 'inLanguage': 'en-AU',
            'wordCount': word_count(pt),
            'author': ORG, 'publisher': ORG,
        }
        if pt['ABOUT']:
            article['about'] = [{'@type': 'MedicalCondition', 'name': a,
                                 'url': '%s/conditions/%s/' % (SITE, cond_by_name[a]['SLUG'])}
                                for a in pt['ABOUT']]
        f['ARTICLE_SCHEMA'] = json.dumps(article, indent=2, ensure_ascii=False)
        f['BREADCRUMB_SCHEMA'] = json.dumps({
            '@context': 'https://schema.org', '@type': 'BreadcrumbList',
            'itemListElement': [
                {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'},
                {'@type': 'ListItem', 'position': 2, 'name': 'Blog', 'item': SITE + '/blog/'},
                {'@type': 'ListItem', 'position': 3, 'name': pt['TITLE'], 'item': url},
            ]}, indent=2, ensure_ascii=False)

        build('post', '%s.html' % pt['SLUG'],
              '%s | Dr. Abbie Clinics' % pt['META_TITLE'],
              pt['EXCERPT'][:155], url, 'Book a Session', subdir='blog', tokens=f)

    # ----------------------------------------------------------------------
    # Booking cards: one clinic, its address, who books there, and one button
    # that is either that clinic's own Nookal link or "Call to book". Used on
    # the booking page, the team hub and every practitioner page.
    # ----------------------------------------------------------------------
    CL = dict((c[1], c) for c in CLINICS)
    NUMBER_WORDS = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
                    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven'}

    def join_names(xs):
        return xs[0] if len(xs) == 1 else ', '.join(xs[:-1]) + ' and ' + xs[-1]

    def book_card(slug, source, show_roster=False, delay=0, level=3):
        name, _, street, post, _ = CL[slug]
        url = BOOKING.get(slug)
        lines = [
            '        <article class="book-card reveal"%s>'
            % ((' data-reveal-delay="%d"' % delay) if delay else ''),
            '          <h%d class="book-card__name">%s%s</h%d>'
            % (level, name,
               (' <span class="loc-card__tag">%s</span>' % TAGS[slug]) if slug in TAGS else '',
               level),
            '          <p class="book-card__addr">%s, %s</p>' % (street, post),
        ]
        if show_roster:
            if url:
                lines.append('          <p class="book-card__who"><span class="book-card__label">'
                             'Book with</span> %s</p>'
                             % join_names([people.BY_SLUG[s]['NAME'] for s in ROSTER[slug]]))
            else:
                lines.append('          <p class="book-card__who">Online booking is not available '
                             'for this clinic yet. Call and we will book you in.</p>')
        lines += [
            '          <div class="book-card__actions">',
            '            ' + book_button(url, slug, source, 'Book online',
                                         sr_place=' at %s' % name),
            '            <a class="book-card__link" href="locations/podiatrist-%s.html">Clinic '
            'details<span class="sr-only"> for %s</span></a>' % (slug, name),
            '          </div>',
            '        </article>',
        ]
        return '\n'.join(lines) + '\n'

    def strip_blocks(html, keep):
        """<!--IF:X--> ... <!--/IF:X--> is kept when keep[X] is true."""
        for key, on in keep.items():
            pat = r'<!--IF:%s-->(.*?)<!--/IF:%s-->' % (key, key)
            html = re.sub(pat, (lambda m: m.group(1)) if on else '', html, flags=re.S)
        return html

    def honorific(t):
        return {'honorificPrefix': 'Dr'} if t['NAME'].startswith('Dr ') else {}

    def schema_name(t):
        return t['NAME'][3:] if t['NAME'].startswith('Dr ') else t['NAME']

    online_count = len(BOOKING)

    # ----------------------------------------------------------------------
    # Booking page: every clinic, grouped by region. Every generic "Book a
    # Session" button on the site lands here.
    # ----------------------------------------------------------------------
    regions = []
    for region, slugs in REGIONS:
        regions.append('\n'.join([
            '      <div class="region reveal">',
            '        <h3 class="region__h">%s <span class="region__count">%s clinic%s</span></h3>'
            % (region, NUMBER_WORDS[len(slugs)].capitalize(), '' if len(slugs) == 1 else 's'),
            '        <div class="book-grid" data-stagger>',
            ''.join(book_card(s, 'booking-page', show_roster=True, delay=i * 60, level=4)
                    for i, s in enumerate(slugs)) + '        </div>',
            '      </div>',
        ]))
    build('locations', 'locations.html',
          'Book a Podiatrist Near You: 11 NSW Clinics | Dr. Abbie Clinics',
          'Choose your nearest Dr. Abbie Clinics podiatry clinic and book online, or call. '
          'Eleven clinics across Sydney, the Southern Highlands, Hunter and regional NSW.',
          SITE + '/locations/', 'Book a Session', tokens={
              'ONLINE_COUNT': NUMBER_WORDS[online_count],
              'ONLINE_COUNT_CAP': NUMBER_WORDS[online_count].capitalize(),
              'REGION_BLOCKS': '\n'.join(regions),
              'CLINICS_SCHEMA': json.dumps({
                  '@context': 'https://schema.org', '@type': 'ItemList',
                  'name': 'Dr. Abbie Clinics locations',
                  'itemListElement': [
                      {'@type': 'ListItem', 'position': i + 1,
                       'item': dict([('@type', 'MedicalClinic'),
                                     ('name', 'Dr. Abbie Clinics — %s' % c[0]),
                                     ('url', '%s/locations/podiatrist-%s/' % (SITE, c[1]))]
                                    + ([('potentialAction', {'@type': 'ReserveAction',
                                                             'target': BOOKING[c[1]]})]
                                       if c[1] in BOOKING else []))}
                      for i, c in enumerate(CLINICS)]}, indent=2, ensure_ascii=False),
          }, booking=('chooser', '#choose', None))

    # ----------------------------------------------------------------------
    # Contact, Privacy Policy and Terms and Conditions. The legal text is
    # converted from the live pages (legal_*.html, wording unchanged) and keeps
    # the live URLs, so none of the three needs a redirect at launch.
    # ----------------------------------------------------------------------
    build('contact', 'contact.html',
          'Contact Dr. Abbie Clinics | Podiatry Clinics in NSW',
          'Call (02) 9545 4378, email reception@dr-abbie.com or book online at your nearest '
          'Dr. Abbie Clinics podiatry clinic. Head office: 27 Monro Ave, Kirrawee NSW.',
          SITE + '/contact/', 'Book a Session', tokens={
              'CLINIC_OPTIONS': chr(10).join('                  <option>%s</option>' % c[0] for c in CLINICS),
              'ONLINE_COUNT_CAP': NUMBER_WORDS[online_count].capitalize(),
              'CLINIC_CARDS': ''.join(book_card(c[1], 'contact-clinics', delay=(i % 3) * 60)
                                      for i, c in enumerate(CLINICS)),
              'CONTACT_SCHEMA': json.dumps({
                  '@context': 'https://schema.org', '@type': 'ContactPage',
                  'url': SITE + '/contact/',
                  'mainEntity': {
                      '@type': 'MedicalOrganization', 'name': 'Dr. Abbie Clinics',
                      'url': SITE + '/', 'telephone': '+61295454378',
                      'email': 'reception@dr-abbie.com', 'faxNumber': '+61295217444',
                      'address': {'@type': 'PostalAddress', 'streetAddress': '27 Monro Ave',
                                  'addressLocality': 'Kirrawee', 'addressRegion': 'NSW',
                                  'postalCode': '2232', 'addressCountry': 'AU'},
                  }}, indent=2, ensure_ascii=False),
          })

    LEGAL = [
        ('privacy', 'privacy-policy.html', 'Privacy Policy', 'policy', '/privacy-policy/',
         'How Dr. Abbie Clinics collects, uses, stores, discloses and protects your personal '
         'and health information.',
         '4 December 2025',
         ('dr-abbie-clinics-terms-and-conditions.html', 'Read our Terms and Conditions')),
        ('terms', 'dr-abbie-clinics-terms-and-conditions.html', 'Terms and Conditions',
         'document', '/dr-abbie-clinics-terms-and-conditions/',
         'The terms that apply when you use our services, book an appointment or use this '
         'website, including cancellations, payments and complaints.',
         '4 December 2025',
         ('privacy-policy.html', 'Read our Privacy Policy')),
    ]
    for key, out_name, title, noun, path, intro, effective, other in LEGAL:
        body = open(os.path.join(HERE, 'legal_%s.html' % key), encoding='utf-8').read()
        toc = [line.split(chr(9), 1) for line in
               open(os.path.join(HERE, 'legal_%s.toc' % key), encoding='utf-8').read().splitlines()
               if line.strip()]
        build('legal', out_name, '%s | Dr. Abbie Clinics' % title, intro[:155], SITE + path,
              'Book a Session', tokens={
                  'TITLE': title, 'NOUN': noun, 'INTRO': intro, 'EFFECTIVE': effective,
                  'BODY': body, 'OTHER_HREF': other[0], 'OTHER_LABEL': other[1],
                  'TOC_ITEMS': chr(10).join('              <li><a href="#%s">%s</a></li>' % (h, t)
                                         for h, t in toc),
              })

    # ----------------------------------------------------------------------
    # Team: the hub at /team.html, and one page per practitioner in /team/.
    # ----------------------------------------------------------------------
    band = img_tag('hero-band', '', '100vw', eager=True)
    build('team', 'team.html',
          'Meet Our Podiatrists | Dr. Abbie Clinics',
          'Meet the podiatrists at Dr. Abbie Clinics: qualifications, special interests, the '
          'treatments they provide and the clinics where they take bookings.',
          SITE + '/team/', 'Book a Session', tokens={
              'HERO_IMG_TAG': band,
              'TEAM_COUNT': NUMBER_WORDS[len(TEAM)].capitalize(),
              'TEAM_GRID': people.card_grid(TEAM),
              'ONLINE_COUNT_CAP': NUMBER_WORDS[online_count].capitalize(),
              'CLINIC_CARDS': ''.join(book_card(c[1], 'team-clinics', show_roster=True,
                                                delay=(i % 3) * 60)
                                      for i, c in enumerate(CLINICS)),
              'TEAM_SCHEMA': json.dumps({
                  '@context': 'https://schema.org', '@type': 'ItemList',
                  'name': 'Practitioners at Dr. Abbie Clinics',
                  'itemListElement': [
                      {'@type': 'ListItem', 'position': i + 1,
                       'item': dict([('@type', 'Person'), ('name', schema_name(t))]
                                    + list(honorific(t).items())
                                    + [('jobTitle', t['ROLE_PLAIN']),
                                       ('url', '%s/team/%s/' % (SITE, t['SLUG']))])}
                      for i, t in enumerate(TEAM)]}, indent=2, ensure_ascii=False),
          })

    for t in TEAM:
        f = dict((k, v) for k, v in t.items() if isinstance(v, str))
        f['QUALS_LINE'] = ' &middot; '.join(t['QUALIFICATIONS'])
        f['BIO_PARAS'] = '\n'.join('            <p>%s</p>' % p for p in t['BIO'])
        f['QUOTE_BLOCK'] = ((
            '          <blockquote class="profile-quote">\n'
            '            <p>“%s”</p>\n'
            '            <cite>The notion %s stands by</cite>\n'
            '          </blockquote>') % (t['QUOTE'], t['FIRST'])) if t['QUOTE'] else ''

        def fact_list(title, xs):
            if not xs:
                return ''
            return ('            <h3>%s</h3>\n            <ul class="profile-facts__list">\n%s\n'
                    '            </ul>\n' % (title, '\n'.join('              <li>%s</li>' % x
                                                           for x in xs)))
        facts = (fact_list('Qualifications', t['QUALIFICATIONS'])
                 + fact_list('Memberships', t['MEMBERSHIPS'])
                 + fact_list('Special interests', t['INTERESTS']))
        f['FACTS_BLOCK'] = ('          <div class="aside-box profile-facts">\n%s          </div>'
                            % facts) if facts else ''
        f['PHOTO_BLOCK'] = (
            '<img src="assets/img/%s.webp" srcset="assets/img/%s.webp 1x, assets/img/%s@2x.webp 2x" '
            'width="480" height="640" alt="%s" loading="eager" decoding="async" '
            'sizes="(min-width: 900px) 340px, 320px">' % (t['PHOTO'], t['PHOTO'], t['PHOTO'],
                                                           people.alt(t))
            if t['PHOTO'] else
            '<div class="profile-hero__initials" aria-hidden="true">%s</div>' % people.initials(t))

        f['SERVICE_CARDS'] = ''.join(service_card(by_slug[s]) for s in t['SERVICES'])

        # Conditions come from the practitioner's treatments, in order, so the
        # page never claims a condition none of their treatments is used for.
        # Any whose card photograph is already on the page is skipped.
        taken = set(SLOT_SOURCE.get(sl) for sl in slots_in(f['SERVICE_CARDS'])
                    | ({t['PHOTO']} if t['PHOTO'] else set()))
        conds = []
        for s in t['SERVICES']:
            for name, desc in by_slug[s]['CONDITIONS']:
                if name in [c[0] for c in conds] or name not in cond_by_name:
                    continue
                src = SLOT_SOURCE.get(conditions.CONDITIONS[name][0])
                if src in taken:
                    continue
                conds.append((name, desc))
                taken.add(src)
        f['CONDITION_CARDS'] = ''.join(
            conditions.card(n, d, 'conditions/%s.html' % cond_by_name[n]['SLUG'])
            for n, d in conds[:4])

        # Where this practitioner takes bookings, from the clinics' Nookal pages.
        mine = [c[1] for c in CLINICS if t['SLUG'] in ROSTER.get(c[1], [])]
        places = join_names([CL[s][0] for s in mine])
        f['BOOK_H2'] = ('at %s clinics' % NUMBER_WORDS[len(mine)]) if len(mine) > 1 \
            else 'at %s' % CL[mine[0]][0]
        f['BOOK_LEDE'] = ('%s takes online bookings at %s. Open the clinic’s diary and choose %s '
                          'at the practitioner step.' % (t['FIRST'], places, t['FIRST']))
        f['ASIDE_BOOK_TEXT'] = 'Online bookings at %s. Choose %s at the practitioner step.' % (
            places, t['FIRST'])
        f['BOOK_CARDS'] = ''.join(book_card(s, 'practitioner-clinics', delay=i * 60)
                                  for i, s in enumerate(mine))
        f['OTHER_TEAM'] = people.card_grid([x for x in TEAM if x is not t])
        if len(mine) == 1:
            booking = ('online', BOOKING[mine[0]], mine[0])
        else:
            booking = ('chooser', '#book', None)

        url = '%s/team/%s/' % (SITE, t['SLUG'])
        person = dict([('@context', 'https://schema.org'), ('@type', 'Person'),
                       ('name', schema_name(t))] + list(honorific(t).items()))
        person.update({
            'jobTitle': t['ROLE_PLAIN'], 'url': url,
            'description': t['INTRO'],
            'worksFor': {'@type': 'MedicalOrganization', 'name': 'Dr. Abbie Clinics',
                         'url': SITE + '/'},
            'workLocation': [{'@type': 'MedicalClinic',
                              'name': 'Dr. Abbie Clinics — %s' % CL[s][0],
                              'url': '%s/locations/podiatrist-%s/' % (SITE, s)} for s in mine],
        })
        if t['QUALIFICATIONS']:
            person['hasCredential'] = [{'@type': 'EducationalOccupationalCredential', 'name': q}
                                       for q in t['QUALIFICATIONS']]
        if t['INTERESTS']:
            person['knowsAbout'] = t['INTERESTS']
        if t['MEMBERSHIPS']:
            person['memberOf'] = [{'@type': 'Organization', 'name': m} for m in t['MEMBERSHIPS']]
        f['PERSON_SCHEMA'] = json.dumps(person, indent=2, ensure_ascii=False)
        f['BREADCRUMB_SCHEMA'] = json.dumps({
            '@context': 'https://schema.org', '@type': 'BreadcrumbList',
            'itemListElement': [
                {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'},
                {'@type': 'ListItem', 'position': 2, 'name': 'Meet the Team',
                 'item': SITE + '/team/'},
                {'@type': 'ListItem', 'position': 3, 'name': t['NAME'], 'item': url},
            ]}, indent=2, ensure_ascii=False)

        build('practitioner', '%s.html' % t['SLUG'],
              '%s, %s | Dr. Abbie Clinics' % (t['NAME'], t['ROLE_PLAIN']),
              t['INTRO'][:155], url, 'Book with %s' % t['FIRST'],
              subdir='team', tokens=f, booking=booking,
              blocks={'SERVICES': bool(t['SERVICES']), 'CONDITIONS': bool(conds)})

    for page, text in sorted(UNRESOLVED_PEOPLE_LINKS):
        print('  unresolved practitioner link: %s -> %r' % (page, text))
    for page, text in sorted(UNRESOLVED_COND_LINKS):
        print('  unresolved condition link: %s -> %r' % (page, text))
    print('done.')
