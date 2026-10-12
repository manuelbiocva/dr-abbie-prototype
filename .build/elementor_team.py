# -*- coding: utf-8 -*-
"""Build a practitioner page out of native Elementor widgets.

The first WordPress build served each page as one Elementor HTML widget holding
the prototype's markup. That matched the design exactly but left the client with
a single block of HTML to edit. This rebuilds the same page as Elementor
containers and native widgets -- heading, text-editor, image, button, icon-list
-- so each piece is selectable and editable in the builder.

Layout is set with Elementor's own container controls, because that is what the
client can change. The prototype's class names ride along on the containers so
typography, colour and decoration keep coming from the approved stylesheet
rather than being re-invented in the builder.

Two parts stay as HTML widgets, for reasons worth knowing:
  * the clinic booking cards, whose per-clinic data-track attributes feed GA4 --
    custom attributes are an Elementor Pro control
  * the inline arrow/pin SVGs inside those cards

Run:  python .build/elementor_team.py <slug>   (writes wp-html/elementor/<slug>.json)
"""
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'wp-html', 'pages')
OUT = os.path.join(ROOT, 'wp-html', 'elementor')
ASSETS = 'https://dr-abbie.com/wp-content/dr-abbie-assets/img/'

_uid = [0]


def uid():
    """Elementor ids are 7 hex chars and only need to be unique in the page."""
    _uid[0] += 1
    return ('%07x' % (0xd0a000 + _uid[0] * 7919))[-7:]


# --------------------------------------------------------------------------
# element builders
# --------------------------------------------------------------------------

def px(v):
    return {'unit': 'px', 'size': v, 'sizes': []}


def spacing(top=0, right=0, bottom=0, left=0):
    return {'unit': 'px', 'top': str(top), 'right': str(right),
            'bottom': str(bottom), 'left': str(left), 'isLinked': False}


BOXED = 1240          # --container
SECTION_Y = 112       # --section-y resolves to its 7rem cap on desktop
SECTION_Y_SM = 64     # and to roughly 4rem on a phone
DEEP_BLUE = '#0C2E47'
PALE_BLUE = '#DDF0FB'


def bg(color):
    """Background as an Elementor setting, so the client can change it."""
    return {'background_background': 'classic', 'background_color': color}


def band(color=None, pad_y=SECTION_Y, pad_y_sm=None):
    """A full-width strip: the design's section rhythm, set in the builder."""
    small = pad_y_sm if pad_y_sm is not None else min(pad_y, SECTION_Y_SM)
    s = {'padding': spacing(pad_y, 0, pad_y, 0),
         'padding_mobile': spacing(small, 0, small, 0)}
    if color:
        s.update(bg(color))
    return s


def boxed():
    """The design's centred column, as Elementor's own boxed width."""
    return {'content_width': 'boxed',
            'boxed_width': {'unit': 'px', 'size': BOXED, 'sizes': []},
            'padding': spacing(0, 24, 0, 24)}


def container(children, classes='', direction='column', gap=None, width=None,
              content_width='full', extra=None, link=None, tag=None):
    # padding is deliberately not forced to zero: the design's own classes
    # carry the padding for panels like .aside-box and .card, and an
    # explicit 0 here would outrank them
    s = {'content_width': content_width}
    if direction:
        s['flex_direction'] = direction
    if gap is not None:
        s['flex_gap'] = {'column': str(gap), 'row': str(gap), 'isLinked': True,
                         'unit': 'px', 'size': gap}
    if width is not None:
        s['width'] = width
        s['_flex_size'] = 'none'
    if classes:
        # containers take 'css_classes'; only widgets use the
        # underscored '_css_classes'
        s['css_classes'] = classes
    if link:
        s['link'] = {'url': link, 'is_external': '', 'nofollow': ''}
    if tag:
        s['_element_tag'] = tag
    if extra:
        s.update(extra)
    return {'id': uid(), 'elType': 'container', 'settings': s,
            'elements': children, 'isInner': False}


def widget(kind, settings, classes=''):
    if classes:
        settings['_css_classes'] = classes
    return {'id': uid(), 'elType': 'widget', 'widgetType': kind,
            'settings': settings, 'elements': []}


def heading(text, size='h2', classes=''):
    return widget('heading', {'title': text, 'header_size': size}, classes)


def text(html, classes=''):
    return widget('text-editor', {'editor': html}, classes)


def image(url, alt='', classes='', width=None, height=None):
    s = {'image': {'url': url, 'id': '', 'alt': alt, 'source': 'library'},
         'image_size': 'full'}
    if width:
        s['width'] = px(width)
    return widget('image', s, classes)


def button(label, url, classes='', external=False):
    return widget('button', {
        'text': label,
        'link': {'url': url, 'is_external': 'on' if external else '',
                 'nofollow': ''},
        'button_type': '',
        'size': 'md',
    }, classes)


def icon_list(items, classes=''):
    return widget('icon-list', {
        'icon_list': [{'text': i, 'selected_icon': {'value': '', 'library': ''},
                       '_id': uid()} for i in items],
        'space_between': {'unit': 'px', 'size': 6},
    }, classes)


def raw_html(html, classes=''):
    return widget('html', {'html': html}, classes)


# --------------------------------------------------------------------------
# reading the built page
# --------------------------------------------------------------------------

def grab(pattern, html, group=1, default=''):
    m = re.search(pattern, html, re.S)
    return m.group(group).strip() if m else default


def section_html(html, index):
    """The nth top-level <section> of the page, inner HTML."""
    spans = []
    depth = 0
    start = None
    for m in re.finditer(r'<(/?)section\b[^>]*>', html):
        if m.group(1) == '':
            if depth == 0:
                start = m
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                spans.append((start, m))
    if index >= len(spans):
        return '', ''
    a, b = spans[index]
    return a.group(0), html[a.end():b.start()]


def cards_from(grid_html):
    """Each <a class="card ..."> in a grid, as (href, img, alt, title, blurb)."""
    out = []
    for m in re.finditer(r'<a class="card [^"]*"[^>]*href="([^"]+)"[^>]*>(.*?)</a>',
                         grid_html, re.S):
        href, inner = m.group(1), m.group(2)
        img = grab(r'<img[^>]+src="([^"]+)"', inner)
        alt = grab(r'<img[^>]+alt="([^"]*)"', inner)
        title = re.sub(r'<[^>]+>', '', grab(r'<h3[^>]*>(.*?)</h3>', inner)).strip()
        blurb = re.sub(r'<[^>]+>', '', grab(r'<p[^>]*>(.*?)</p>', inner)).strip()
        media_cls = 'cond-card__media'
        if 'cond-card__media--diagram' in inner:
            media_cls += ' cond-card__media--diagram'
        out.append((href, img, alt, title, blurb, media_cls))
    return out


def card_grid(cards, grid_classes):
    """A row of cards, each a linked container holding native widgets."""
    items = []
    for href, img, alt, title, blurb, media_cls in cards:
        items.append(container([
            container([image(img, alt)], classes=media_cls, gap=0),
            heading(title, 'h3'),
            text('<p>%s</p>' % blurb) if blurb else text(''),
            text('<span class="card__more card__more--arrow">Read more</span>'),
        ], classes='card cond-card reveal', gap=0, link=href,
            width={'unit': 'px', 'size': 272}, extra={
                'background_background': 'classic',
                'background_color': '#FFFFFF',
                'border_border': 'solid',
                'border_width': spacing(1, 1, 1, 1),
                'border_color': 'rgba(12, 46, 71, 0.12)',
                'border_radius': spacing(16, 16, 16, 16),
                'overflow': 'hidden',
            }))
    return container(items, classes=grid_classes, direction='row', gap=24,
                     extra={'flex_wrap': 'wrap'})


def split_head(eyebrow, line1, line2, lede):
    return container([
        container([
            heading(eyebrow, 'div', classes='eyebrow'),
            heading('<span>%s</span><span>%s</span>' % (line1, line2), 'h2',
                    classes='split-head'),
        ], gap=12, width={'unit': '%', 'size': 55}),
        text('<p>%s</p>' % lede, classes='lede'),
    ], classes='section-head section-head--split reveal', direction='row',
        gap=32, extra={'flex_wrap': 'wrap'})


# --------------------------------------------------------------------------
# the page
# --------------------------------------------------------------------------

def build(slug):
    from team_data import TEAM
    person = [t for t in TEAM if t['SLUG'] == slug][0]
    first = person['FIRST']
    html = io.open(os.path.join(SRC, 'team--%s.html' % slug),
                   encoding='utf-8').read()

    # ---- hero ------------------------------------------------------------
    _, hero = section_html(html, 0)
    crumbs = grab(r'<nav class="crumbs[^"]*"[^>]*>(.*?)</nav>', hero)
    quals_line = grab(r'<p class="profile-hero__quals">(.*?)</p>', hero)
    intro = grab(r'<p class="hero__intro">(.*?)</p>', hero)
    portrait = grab(r'<figure class="profile-hero__photo">.*?<img[^>]+src="([^"]+)"', hero)
    portrait_alt = grab(r'<figure class="profile-hero__photo">.*?<img[^>]+alt="([^"]*)"', hero)
    phone = grab(r'<a class="btn btn--ghost-invert" href="tel:([^"]+)"', hero)
    phone_text = grab(r'<span class="callrail-number">(.*?)</span>', hero)

    hero_copy = container([
        text('<nav class="crumbs crumbs--invert" aria-label="Breadcrumb">%s</nav>' % crumbs),
        heading(person['ROLE'], 'div', classes='eyebrow eyebrow--invert'),
        heading(person['NAME'], 'h1'),
        text('<p class="profile-hero__quals">%s</p>' % quals_line),
        text('<p class="hero__intro">%s</p>' % intro),
        container([
            button('Book with %s' % first, '#book', classes='dra-btn dra-btn--book'),
            button('Call %s' % phone_text, 'tel:%s' % phone,
                   classes='dra-btn dra-btn--ghost-invert'),
        ], classes='hero__actions', direction='row', gap=12,
            extra={'flex_wrap': 'wrap'}),
    # the copy column takes whatever the portrait leaves, the way the design
    # lays it out: pinning it to a percentage narrowed it and wrapped the
    # headline onto extra lines
    ], classes='hero__anchor', gap=8, extra={'_flex_size': 'grow'})

    hero_photo = container([image(portrait, portrait_alt)],
                           classes='profile-hero__photo', gap=0,
                           width={'unit': 'px', 'size': 340})

    hero_section = container([
        container([
            container([hero_copy, hero_photo], classes='profile-hero',
                      direction='row', gap=48,
                      extra={'flex_wrap': 'wrap', 'align_items': 'center'}),
        ], classes='container', extra=boxed()),
    ], classes='hero hero--photo hero--compact hero--profile hex-texture', gap=0,
        extra=band(DEEP_BLUE, 24, 24))

    # ---- about + aside ---------------------------------------------------
    _, about = section_html(html, 1)
    prose = grab(r'<div class="prose mt-6">(.*?)</div>', about)
    bio_paras = re.findall(r'<p>(.*?)</p>', prose, re.S)

    bio_col = container([
        heading('About %s' % first, 'div', classes='eyebrow'),
        heading('<span>Meet</span><span>%s</span>' % person['NAME'], 'h2',
                classes='split-head'),
        text(''.join('<p>%s</p>' % p.strip() for p in bio_paras), classes='prose'),
    ], classes='profile-bio', gap=16, width={'unit': '%', 'size': 62})

    facts = []
    for label, key in (('Qualifications', 'QUALIFICATIONS'),
                       ('Memberships', 'MEMBERSHIPS'),
                       ('Special interests', 'INTERESTS')):
        if person.get(key):
            facts.append(heading(label, 'h3'))
            facts.append(icon_list(person[key], classes='profile-facts__list'))

    aside_book_text = grab(r'<div class="aside-book">.*?<p>(.*?)</p>', about)
    aside = container([
        container(facts, classes='aside-box profile-facts', gap=8),
        container([
            heading('Book', 'div', classes='eyebrow eyebrow--invert'),
            heading('See %s' % first, 'h2', classes='aside-book__h'),
            text('<p>%s</p>' % aside_book_text),
            button('Book with %s' % first, '#book',
                   classes='dra-btn dra-btn--book dra-btn--sm'),
            text('<a class="aside-book__call" href="tel:%s">Or call %s</a>'
                 % (phone, phone_text)),
        ], classes='aside-book', gap=10),
    ], classes='article__aside', gap=20, width={'unit': 'px', 'size': 300})

    about_section = container([
        container([
            container([bio_col, aside], classes='article', direction='row',
                      gap=48, extra={'flex_wrap': 'wrap'}),
        ], classes='container', extra=boxed()),
    ], classes='section section--white', gap=0, extra=band('#FFFFFF'))

    # ---- treatments and conditions --------------------------------------
    grids = []
    for idx, (eyebrow, l1, l2) in ((2, ('Treatments', 'Treatments',
                                        '%s provides' % first)),
                                   (3, ('Conditions', 'Conditions',
                                        'commonly treated'))):
        tag, body = section_html(html, idx)
        lede = re.sub(r'\s+', ' ',
                      re.sub(r'<[^>]+>', '',
                             grab(r'<p class="lede">(.*?)</p>', body))).strip()
        cards = cards_from(body)
        shade = 'section--pale' if 'section--pale' in tag else 'section--white'
        tone = PALE_BLUE if shade == 'section--pale' else '#FFFFFF'
        grids.append(container([
            container([
                split_head(eyebrow, l1, l2, lede),
                card_grid(cards, 'grid-auto cond-grid'),
            ], classes='container', gap=40, extra=boxed()),
        ], classes='section %s' % shade, gap=0, extra=band(tone)))

    # ---- where to book: stays HTML, see the module docstring -------------
    book_tag, book_body = section_html(html, 4)
    book_extra = band(PALE_BLUE)
    book_extra['_element_id'] = 'book'
    book_section = container([
        container([raw_html('<div class="dra-booking-cards">%s</div>' % book_body)],
                  classes='container', extra=boxed()),
    ], classes='section section--pale', gap=0, extra=book_extra)

    # ---- other practitioners and the closing CTA stay as the design has
    #      them: both are built from shared partials used across the site ---
    other_tag, other_body = section_html(html, 5)
    other_section = container([
        container([raw_html(other_body)], classes='container', extra=boxed()),
    ], classes='section section--white', gap=0, extra=band('#FFFFFF'))

    cta_m = re.search(r'<section class="cta-band[^"]*"[^>]*>(.*?)</section>', html, re.S)
    cta_section = raw_html('<section class="cta-band cta-band--photo">%s</section>'
                           % cta_m.group(1)) if cta_m else None

    page = [hero_section, about_section, grids[0], grids[1], book_section,
            other_section]
    if cta_section:
        page.append(container([cta_section], gap=0))
    return page


def main():
    slug = sys.argv[1] if len(sys.argv) > 1 else 'dr-elissa-all'
    data = build(slug)
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    path = os.path.join(OUT, slug + '.json')
    io.open(path, 'w', encoding='utf-8').write(
        json.dumps(data, ensure_ascii=False, separators=(',', ':')))
    widgets = len(re.findall(r'"elType":"widget"', json.dumps(data)))
    htmls = len(re.findall(r'"widgetType":"html"', json.dumps(data)))
    print('%s  %d bytes  %d widgets (%d still html)'
          % (path, os.path.getsize(path), widgets, htmls))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
