# -*- coding: utf-8 -*-
"""One clinic card, used wherever clinics are listed.

Client request (Loom, 18 Sept 2026): every clinic listing shows the address
linked to the clinic's Google Business Profile, a visible Book online button,
and a phone button in a different colour. The footer, the home clinic finder,
the booking page, the team and contact pages and every practitioner page all
render this one card, so the rule cannot drift between them.

Colour: Book online is orange (booking, as everywhere). Call is outlined
azure, so the two are visually different, as asked.
"""
from clinics import CLINICS, BOOKING, TAGS, GOOGLE, phone

CL = dict((c[1], c) for c in CLINICS)

PIN = ('<svg width="15" height="15" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
       '<path d="M12 21s7-5.6 7-11a7 7 0 1 0-14 0c0 5.4 7 11 7 11Z" stroke="currentColor" '
       'stroke-width="1.8" stroke-linejoin="round"/><circle cx="12" cy="10" r="2.5" '
       'stroke="currentColor" stroke-width="1.8"/></svg>')
TEL = ('<svg width="15" height="15" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
       '<path d="M6.5 3h3l1.5 4-2 1.5a12 12 0 0 0 5.5 5.5L16 12l4 1.5v3a2 2 0 0 1-2.2 2A16.5 '
       '16.5 0 0 1 4 6.2 2 2 0 0 1 6.5 3Z" stroke="currentColor" stroke-width="1.8" '
       'stroke-linejoin="round"/></svg>')
CAL = ('<svg width="15" height="15" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
       '<rect x="3.5" y="5" width="17" height="15.5" rx="2" stroke="currentColor" '
       'stroke-width="1.8"/><path d="M3.5 10h17M8 3v4M16 3v4" stroke="currentColor" '
       'stroke-width="1.8" stroke-linecap="round"/></svg>')


def maps_url(slug):
    return GOOGLE[slug][1]


def book_btn(slug, source, cls='btn btn--book btn--sm'):
    name = CL[slug][0]
    url = BOOKING.get(slug)
    if url:
        return ('<a class="%s" href="%s" target="_blank" rel="noopener" data-track="book" '
                'data-book-method="online" data-location="%s" data-source="%s">%s Book online'
                '<span class="sr-only"> at %s (opens in a new tab)</span></a>'
                % (cls, url, slug, source, CAL, name))
    # no online booking: the button is the phone number itself, so it is visible
    tel, shown = phone(slug)
    return ('<a class="%s" href="tel:%s" data-track="book" data-book-method="phone" '
            'data-location="%s" data-source="%s">%s Call <span class="callrail-number">%s'
            '</span><span class="sr-only"> to book at %s</span></a>' % (cls, tel, slug, source, TEL, shown, name))


def call_btn(slug, cls='btn btn--phone btn--sm'):
    tel, shown = phone(slug)
    return ('<a class="%s" href="tel:%s" data-location="%s">%s <span class="callrail-number">'
            '%s</span><span class="sr-only"> (%s clinic)</span></a>'
            % (cls, tel, slug, TEL, shown, CL[slug][0]))


def address_link(slug, cls='clinic-card__addr'):
    name, _, street, post, _ = CL[slug]
    return ('<a class="%s" href="%s" target="_blank" rel="noopener" data-track="maps" '
            'data-location="%s">%s<span>%s, %s</span><span class="sr-only"> (opens %s in '
            'Google Maps)</span></a>' % (cls, maps_url(slug), slug, PIN, street, post, name))


def card(slug, source, variant='', extra='', level=3, delay=0, name_prefix=''):
    """variant: '' (light), 'dark' (footer). extra: roster line etc."""
    name, _, street, post, _ = CL[slug]
    tag = (' <span class="loc-card__tag">%s</span>' % TAGS[slug]) if slug in TAGS else ''
    both_book_and_call = slug in BOOKING
    actions = [book_btn(slug, source)]
    if both_book_and_call:
        # "Call to book" already is the phone button for the others
        actions.append(call_btn(slug))
    return '\n'.join([
        '        <article class="clinic-card%s%s"%s>' % (
            (' clinic-card--' + variant) if variant else '', '' if variant else ' reveal',
            (' data-reveal-delay="%d"' % delay) if delay else ''),
        '          <h%d class="clinic-card__name"><a href="locations/podiatrist-%s.html">%s%s</a>%s</h%d>'
        % (level, slug, name_prefix, name, tag, level),
        '          %s' % address_link(slug),
        extra,
        '          <div class="clinic-card__actions">',
        '            ' + '\n            '.join(actions),
        '          </div>',
        '        </article>',
    ]).replace('\n\n', '\n') + '\n'


def footer_clinics():
    return ''.join(card(c[1], 'footer-clinics', variant='dark', level=4, name_prefix='Podiatrist ')
                   for c in CLINICS)
