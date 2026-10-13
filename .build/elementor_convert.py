# -*- coding: utf-8 -*-
"""Turn a page's markup into native Elementor containers and widgets.

The WordPress build originally served each page as a single Elementor HTML
widget holding the approved markup. It matched the design exactly but left the
client one block of HTML to edit. This converts that markup into Elementor's
own elements, so every heading, paragraph, image and card is selectable in the
builder.

How it decides:

  * an element with block-level children becomes a **container**, keeping its
    class list so the approved stylesheet still lays it out
  * a heading becomes a **heading** widget, an image an **image** widget
  * anything whose children are only text and inline tags becomes a
    **text-editor** widget holding that markup verbatim

That last rule is what keeps the booking buttons safe. An anchor stays exactly
as it was written -- its href, target, and the data-track/data-location
attributes GA4 reads -- because it travels inside the text widget rather than
being rebuilt as a button widget, which cannot carry custom attributes without
Elementor Pro.

Anything with a shortcode or a form is left as an HTML widget on purpose: the
blog grid and the contact form have to keep working.

Run:  python .build/elementor_convert.py <in.json> <out.json>
      where in.json maps page slug -> that page's current HTML.
"""
import io
import json
import re
import sys
from html.parser import HTMLParser

# --------------------------------------------------------------------------
# tag classification
# --------------------------------------------------------------------------
VOID = {'img', 'br', 'hr', 'input', 'source', 'meta', 'link', 'path', 'circle',
        'rect', 'line', 'polygon', 'polyline', 'ellipse', 'use', 'stop'}

# tags that read as part of a line of text rather than a block of their own
INLINE = {'a', 'span', 'strong', 'em', 'b', 'i', 'small', 'sup', 'sub', 'code',
          'br', 'time', 'abbr', 'svg', 'path', 'circle', 'rect', 'line',
          'polygon', 'polyline', 'ellipse', 'g', 'defs', 'use', 'stop',
          'lineargradient', 'clippath', 'title', 'desc', 'mark', 'u', 's'}

HEADINGS = {'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}

# elements that hold other blocks and so become containers
BLOCKISH = {'div', 'section', 'article', 'aside', 'figure', 'header', 'footer',
            'main', 'nav', 'form', 'fieldset', 'picture'}

# kept whole: re-creating these as widgets would lose behaviour
KEEP_RAW = {'script', 'style', 'noscript', 'iframe', 'form', 'table', 'select',
            'textarea', 'video', 'audio', 'picture'}

# Attributes main.js reads to drive a component. A container cannot carry a
# data attribute without Elementor Pro, so an element holding one of these is
# kept as markup -- otherwise the slider, the parallax and the logo marquee
# simply never start. data-stagger is the exception: it is handled by a class.
BEHAVIOUR_ATTRS = {
    'data-slider-root', 'data-slider-track', 'data-slider', 'data-slide',
    'data-carousel', 'data-logo-marquee', 'data-parallax', 'data-toc',
    'data-enquiry-form', 'data-enquiry-done', 'data-day', 'data-interval',
    'data-per-view', 'data-single', 'data-dir',
}

MEDIA_TAGS = {'img', 'picture', 'svg', 'source', 'video'}

# Marks a widget whose job is only to carry markup through. The bridge gives
# it display:contents so the element inside sits where the design expects,
# rather than inside a wrapper box that breaks absolute positioning.
RAW_MARK = 'dra-raw'

SECTION_TONES = {
    'section--white': '#FFFFFF',
    'section--pale': '#DDF0FB',
    'section--deep': '#0C2E47',
}
BOXED = 1240
SECTION_Y = 112
SECTION_Y_SM = 64

_uid = [0]


def uid():
    _uid[0] += 1
    return ('%07x' % (0xb10000 + _uid[0] * 7919))[-7:]


# --------------------------------------------------------------------------
# a very small DOM
# --------------------------------------------------------------------------
class Node(object):
    __slots__ = ('tag', 'attrs', 'kids', 'text', 'parent')

    def __init__(self, tag, attrs=None, text=None):
        self.tag = tag
        self.attrs = attrs or {}
        self.kids = []
        self.text = text
        self.parent = None

    def cls(self):
        return self.attrs.get('class', '')

    def is_text(self):
        return self.tag is None


class Tree(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self, convert_charrefs=False)
        self.root = Node('#root')
        self.stack = [self.root]

    def _add(self, node):
        node.parent = self.stack[-1]
        self.stack[-1].kids.append(node)
        return node

    def handle_starttag(self, tag, attrs):
        node = self._add(Node(tag, dict(attrs)))
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self._add(Node(tag, dict(attrs)))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        if data.strip():
            self._add(Node(None, text=data))
        elif data and self.stack[-1].kids:
            self._add(Node(None, text=' '))

    def handle_entityref(self, name):
        self._add(Node(None, text='&%s;' % name))

    def handle_charref(self, name):
        self._add(Node(None, text='&#%s;' % name))

    def handle_comment(self, data):
        pass


def parse(html):
    t = Tree()
    t.feed(html)
    t.close()
    return t.root


# --------------------------------------------------------------------------
# serialising back to HTML (for leaves kept verbatim)
# --------------------------------------------------------------------------
def attrs_html(node):
    out = []
    for k, v in node.attrs.items():
        out.append(' %s="%s"' % (k, v.replace('"', '&quot;')) if v is not None
                   else ' %s' % k)
    return ''.join(out)


def to_html(node):
    if node.is_text():
        return node.text
    if node.tag == '#root':
        return ''.join(to_html(k) for k in node.kids)
    if node.tag in VOID:
        return '<%s%s>' % (node.tag, attrs_html(node))
    return '<%s%s>%s</%s>' % (node.tag, attrs_html(node),
                              ''.join(to_html(k) for k in node.kids), node.tag)


def inner_html(node):
    return ''.join(to_html(k) for k in node.kids)


def has_block_kids(node):
    for k in node.kids:
        if k.is_text():
            continue
        if k.tag in BLOCKISH or k.tag in HEADINGS or k.tag in KEEP_RAW:
            return True
        if k.tag in ('ul', 'ol', 'p', 'img', 'figcaption', 'dl'):
            return True
    return False


def needs_raw(node):
    """Shortcodes and forms must keep working, so they stay HTML."""
    html = to_html(node)
    if re.search(r'\[[a-zA-Z][a-zA-Z0-9_-]*[^\]]*\]', html):
        return True
    for t in KEEP_RAW:
        if '<' + t in html:
            return True
    return False


def drives_behaviour(node):
    """Does this element carry a hook main.js needs to start a component?"""
    for k in node.attrs:
        if k in BEHAVIOUR_ATTRS:
            return True
    return False


def is_media_frame(node):
    """A wrapper whose whole job is to hold a picture.

    The design sizes and crops these through CSS aimed at the exact shape of
    the markup -- `.about__media img`, `.bento__media img`. Rebuilding the
    picture as an image widget puts a wrapper in the middle of that, which is
    what left the About photo short of full width and the NBA tile empty. The
    frame is kept exactly as written.
    """
    if node.is_text() or node.tag not in BLOCKISH:
        return False
    if not node.cls():
        return False
    seen_media = False
    for k in node.kids:
        if k.is_text():
            if k.text.strip():
                return False
            continue
        if k.tag in MEDIA_TAGS:
            seen_media = True
            continue
        return False
    return seen_media


# --------------------------------------------------------------------------
# Elementor pieces
# --------------------------------------------------------------------------
def spacing(top=0, right=0, bottom=0, left=0):
    return {'unit': 'px', 'top': str(top), 'right': str(right),
            'bottom': str(bottom), 'left': str(left), 'isLinked': False}


def widget(kind, settings, classes='', el_id=''):
    if classes:
        settings['_css_classes'] = classes
    if el_id:
        settings['_element_id'] = el_id
    return {'id': uid(), 'elType': 'widget', 'widgetType': kind,
            'settings': settings, 'elements': []}


def container(children, settings=None):
    s = {'content_width': 'full'}
    s.update(settings or {})
    return {'id': uid(), 'elType': 'container', 'settings': s,
            'elements': children, 'isInner': False}


def band_settings(classes):
    """Section rhythm and ground, as builder settings the client can change."""
    s = {}
    tone = None
    for k, v in SECTION_TONES.items():
        if k in classes:
            tone = v
    if 'hero' in classes.split():
        return {'padding': spacing(24, 0, 24, 0),
                'padding_mobile': spacing(24, 0, 24, 0),
                'background_background': 'classic',
                'background_color': '#0C2E47'}
    if 'section' in classes.split():
        s['padding'] = spacing(SECTION_Y, 0, SECTION_Y, 0)
        s['padding_mobile'] = spacing(SECTION_Y_SM, 0, SECTION_Y_SM, 0)
    if tone:
        s['background_background'] = 'classic'
        s['background_color'] = tone
    return s


def boxed_settings():
    return {'content_width': 'boxed',
            'boxed_width': {'unit': 'px', 'size': BOXED, 'sizes': []},
            'padding': spacing(0, 24, 0, 24)}


# --------------------------------------------------------------------------
# the conversion
# --------------------------------------------------------------------------
def convert_node(node):
    """One source element -> one Elementor element (or None to skip)."""
    if node.is_text():
        txt = node.text.strip()
        return widget('text-editor', {'editor': txt}) if txt else None

    tag = node.tag
    classes = node.cls()
    el_id = node.attrs.get('id', '')

    if tag in ('script', 'style', 'noscript'):
        return widget('html', {'html': to_html(node)}, RAW_MARK)

    if tag == 'img':
        return widget('image', {
            'image': {'url': node.attrs.get('src', ''), 'id': '',
                      'alt': node.attrs.get('alt', ''), 'source': 'library'},
            'image_size': 'full',
        }, classes, el_id)

    if tag in HEADINGS:
        inner = inner_html(node).strip()
        # Elementor sanitises a heading's title, which drops inline SVG and
        # form controls. The FAQ question is a <button> with the open/close
        # chevron inside it, so converting it lost the icon.
        if '<svg' in inner or '<button' in inner or '<input' in inner:
            return widget('html', {'html': to_html(node)}, RAW_MARK)
        return widget('heading', {'title': inner, 'header_size': tag},
                      classes, el_id)

    # anything carrying a shortcode or a form keeps working as markup
    if needs_raw(node):
        return widget('html', {'html': to_html(node)}, RAW_MARK)

    # a frame holding only pictures becomes a container of image widgets, so
    # the client can swap the photo in the builder. The bridge gives those
    # widgets display:contents, so each <img> sits directly inside the
    # classed frame exactly as the design's CSS expects.
    if is_media_frame(node) and not drives_behaviour(node):
        kids = []
        for k in node.kids:
            if k.is_text() or k.tag != 'img':
                continue
            cls = 'dra-img ' + (k.attrs.get('class', '') or '')
            if 'data-parallax' in k.attrs:
                cls += ' js-parallax'
            kids.append(widget('image', {
                'image': {'url': k.attrs.get('src', ''), 'id': '',
                          'alt': k.attrs.get('alt', ''), 'source': 'library'},
                'image_size': 'full',
            }, cls.strip()))
        if kids:
            s = {'content_width': 'full', 'css_classes': classes}
            if el_id:
                s['_element_id'] = el_id
            return container(kids, s)

    # components main.js drives are kept as written -- see drives_behaviour
    if drives_behaviour(node) or is_media_frame(node):
        return widget('html', {'html': to_html(node)}, RAW_MARK)

    if tag in BLOCKISH and has_block_kids(node):
        kids = [c for c in (convert_node(k) for k in node.kids) if c]
        if not kids:
            return None
        s = {'content_width': 'full'}
        if classes:
            s['css_classes'] = classes
        if el_id:
            s['_element_id'] = el_id
        if 'data-stagger' in attrs_html(node):
            s['css_classes'] = (s.get('css_classes', '') + ' js-stagger').strip()
        href = node.attrs.get('href')
        if href:
            s['html_tag'] = 'a'
            s['link'] = {'url': href, 'is_external': '', 'nofollow': ''}
        s.update(band_settings(classes))
        if 'container' in classes.split():
            s.update(boxed_settings())
        return container(kids, s)

    # a link wrapping blocks (a whole card) is a container rendered as an
    # anchor, which is the only way Elementor will carry the link
    if tag == 'a' and has_block_kids(node):
        kids = [c for c in (convert_node(k) for k in node.kids) if c]
        if not kids:
            return None
        s = {'content_width': 'full', 'html_tag': 'a',
             'link': {'url': node.attrs.get('href', ''),
                      'is_external': 'on' if node.attrs.get('target') else '',
                      'nofollow': ''}}
        if classes:
            s['css_classes'] = classes
        if el_id:
            s['_element_id'] = el_id
        return container(kids, s)

    # everything else is a run of text: keep its markup exactly, which is what
    # preserves anchors, their tracking attributes and their inline icons
    html = to_html(node).strip()
    return widget('text-editor', {'editor': html}) if html else None


def convert_page(html):
    root = parse(html)
    main = None
    for k in root.kids:
        if not k.is_text() and k.tag == 'main':
            main = k
            break
    top = (main or root).kids
    out = []
    for k in top:
        el = convert_node(k)
        if el:
            out.append(el)
    return out


def stats(data):
    c = {}

    def walk(els):
        for e in els:
            k = e['elType'] if e['elType'] != 'widget' else 'widget:' + e['widgetType']
            c[k] = c.get(k, 0) + 1
            walk(e.get('elements', []))
    walk(data)
    return c


def main():
    src = json.load(io.open(sys.argv[1], encoding='utf-8'))
    out = {}
    report = []
    for slug in sorted(src):
        data = convert_page(src[slug])
        out[slug] = data
        s = stats(data)
        report.append((slug, sum(v for k, v in s.items() if k.startswith('widget:')),
                       s.get('widget:html', 0), s.get('container', 0)))
    io.open(sys.argv[2], 'w', encoding='utf-8').write(
        json.dumps(out, ensure_ascii=False, separators=(',', ':')))
    print('%-44s %8s %6s %6s' % ('page', 'widgets', 'html', 'cont'))
    for slug, w, h, c in report:
        print('%-44s %8d %6d %6d' % (slug, w, h, c))
    print('\n%d pages, %d html widgets left in total'
          % (len(report), sum(r[2] for r in report)))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
