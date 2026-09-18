# -*- coding: utf-8 -*-
"""Practitioner sliders and grids.

The people come from team_data.TEAM -- this module used to hold its own copy,
and the copies had already drifted once (a location page built with four of
the five). Every function takes the list of people to show, so a clinic page
can show only the practitioners who take bookings there.

Photographs are the ones dr-abbie.com/practitioners/ uses for each person, so
no face is guessed onto a name. A practitioner with no photograph (PHOTO None)
gets an initials tile in grids, and is left out of the photo sliders.
"""
from team_data import TEAM

BY_SLUG = dict((t['SLUG'], t) for t in TEAM)
WITH_PHOTO = [t for t in TEAM if t['PHOTO']]

PER_VIEW = 3   # slides visible in the hero slider; that many are cloned

ARROW_L = ('<svg width="15" height="15" viewBox="0 0 18 18" fill="none" aria-hidden="true">'
           '<path d="M11 4 6 9l5 5" stroke="currentColor" stroke-width="1.8" '
           'stroke-linecap="round" stroke-linejoin="round"/></svg>')
ARROW_R = ('<svg width="15" height="15" viewBox="0 0 18 18" fill="none" aria-hidden="true">'
           '<path d="m7 4 5 5-5 5" stroke="currentColor" stroke-width="1.8" '
           'stroke-linecap="round" stroke-linejoin="round"/></svg>')


def href(t):
    return 'team/%s.html' % t['SLUG']


def alt(t):
    return '%s, %s at Dr. Abbie Clinics' % (t['NAME'], t['ROLE_PLAIN'])


def initials(t):
    words = [w for w in t['NAME'].split() if w != 'Dr']
    return ''.join(w[0] for w in words[:2]).upper()


def photo(t, sizes):
    if not t['PHOTO']:
        return ('<div class="pcard__photo pcard__photo--initials">'
                '<span aria-hidden="true">%s</span></div>' % initials(t))
    return ('<div class="pcard__photo"><img src="assets/img/%s.webp" '
            'srcset="assets/img/%s.webp 1x, assets/img/%s@2x.webp 2x" width="480" '
            'height="640" alt="%s" loading="lazy" decoding="async" sizes="%s"></div>'
            % (t['PHOTO'], t['PHOTO'], t['PHOTO'], alt(t), sizes))


def _slide(t, clone=False):
    lines = [
        '          <a class="hero-slide" data-slide href="%s"%s>'
        % (href(t), ' aria-hidden="true" tabindex="-1"' if clone else ''),
        '            <img src="assets/img/%s.webp" srcset="assets/img/%s.webp 1x, '
        'assets/img/%s@2x.webp 2x" width="480" height="640" alt="%s" loading="lazy" '
        'decoding="async" sizes="180px">' % (t['PHOTO'], t['PHOTO'], t['PHOTO'],
                                              '' if clone else alt(t)),
        '            <span class="hero-slide__label">%s'
        '<span class="hero-slide__role">%s</span></span>' % (t['NAME'], t['ROLE']),
        '          </a>',
    ]
    return '\n'.join(lines) + '\n'


def hero_slider(label, people=None):
    """Hero slider markup, driven by the shared initSlider().

    With PER_VIEW people or fewer there is nothing to scroll: no clones and
    no arrows, and initSlider() leaves the row static (it needs more slides
    than it shows before it will move).
    """
    people = [t for t in (people or TEAM) if t['PHOTO']]
    moving = len(people) > PER_VIEW
    real = ''.join(_slide(t) for t in people)
    clones = ''.join(_slide(people[i], clone=True) for i in range(PER_VIEW)) if moving else ''
    nav = [
        '        <div class="hero-slider__nav">',
        '          <button class="hero-slider__btn" type="button" data-slider="prev" '
        'aria-label="Previous practitioners">%s</button>' % ARROW_L,
        '          <button class="hero-slider__btn" type="button" data-slider="next" '
        'aria-label="Next practitioners">%s</button>' % ARROW_R,
        '        </div>',
    ] if moving else []
    lines = [
        '    <div class="hero-slider%s" data-slider-root data-per-view="%d" '
        'data-interval="4600">' % ('' if moving else ' hero-slider--static', PER_VIEW),
        '      <div class="hero-slider__head">',
        '        <span class="hero-slider__label">%s</span>' % label,
    ] + nav + [
        '      </div>',
        '      <div class="hero-slider__viewport">',
        '        <div class="hero-slider__track" data-slider-track>',
    ]
    tail = [
        '        </div>',
        '      </div>',
        '    </div>',
    ]
    return '\n'.join(lines) + '\n' + real + clones + '\n'.join(tail) + '\n'


def card_grid(people=None, sizes='(min-width: 1000px) 25vw, (min-width: 560px) 50vw, 100vw'):
    """The static portrait grid used lower down a page."""
    out = []
    for i, t in enumerate(people or TEAM):
        out.append('\n'.join([
            '        <a class="pcard reveal" href="%s"%s>'
            % (href(t), (' data-reveal-delay="%d"' % (i * 60)) if i else ''),
            '          %s' % photo(t, sizes),
            '          <div class="pcard__plate">',
            '            <h3>%s</h3>' % t['NAME'],
            '            <span class="pcard__role">%s</span>' % t['ROLE'],
            '            <span class="pcard__more">View profile <svg width=\"12\" height=\"12\" viewBox=\"0 0 14 14\" fill=\"none\" aria-hidden=\"true\"><path d=\"M3 7h8M7.5 3.5L11 7l-3.5 3.5\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\" stroke-linejoin=\"round\"/></svg></span>',
            '          </div>',
            '        </a>',
        ]) + '\n')
    return ''.join(out)


def team_rail(per_view=4):
    """The home page's team carousel: everyone with a photograph, the first
    per_view cloned at the end for the seamless wrap."""
    def card(t, clone=False):
        return '\n'.join([
            '            <a class="pcard" data-slide href="%s"%s>'
            % (href(t), ' aria-hidden="true" tabindex="-1"' if clone else ''),
            '              <div class="pcard__photo"><img src="assets/img/%s.webp" '
            'srcset="assets/img/%s.webp 1x, assets/img/%s@2x.webp 2x" width="480" height="640" '
            'alt="%s" loading="lazy" decoding="async" sizes="(min-width: 1000px) 25vw, 80vw"></div>'
            % (t['PHOTO'], t['PHOTO'], t['PHOTO'], '' if clone else alt(t)),
            '              <div class="pcard__plate">',
            '                <h3>%s</h3>' % t['NAME'],
            '                <span class="pcard__role">%s</span>' % t['ROLE'],
            '                <span class="pcard__more">View profile <svg width=\"12\" height=\"12\" viewBox=\"0 0 14 14\" fill=\"none\" aria-hidden=\"true\"><path d=\"M3 7h8M7.5 3.5L11 7l-3.5 3.5\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\" stroke-linejoin=\"round\"/></svg></span>',
            '              </div>',
            '            </a>',
            '',
        ])
    people = WITH_PHOTO
    return ''.join(card(t) for t in people) + ''.join(
        card(people[i], clone=True) for i in range(min(per_view, len(people))))
