# -*- coding: utf-8 -*-
"""Turn the built prototype into WordPress-ready HTML parts.

The prototype is the signed-off design. Rather than approximate it with stock
page-builder widgets, the WordPress build serves the same markup, stylesheet
and behaviour, with every link and image path rewritten to the live site.

Writes into prototype/wp-html/:
  parts/header.html   the header, with the three mega menus
  parts/footer.html   the footer, with the full clinic/treatment/condition lists
  pages/<name>.html   the <main> of each page

Run:  python .build/export_wp_html.py
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'wp-html')
SITE = 'https://dr-abbie.com'
ASSETS = SITE + '/wp-content/dr-abbie-assets/img/'


def rewrite(html, depth=0):
    """Point assets at the uploaded copies and links at WordPress permalinks."""
    # images: assets/img/x.webp and ../assets/img/x.webp both become absolute
    html = re.sub(r'(?:\.\./)*assets/img/', ASSETS, html)
    html = re.sub(r'(?:\.\./)*assets/(css|js)/[^"\']+', '', html)

    def link(m):
        href = m.group(2)
        if href.startswith('#') or href.startswith('http') or href.startswith('tel:') or href.startswith('mailto:'):
            return m.group(0)
        href = re.sub(r'^(?:\.\./)+', '', href)
        frag = ''
        if '#' in href:
            href, frag = href.split('#', 1)
            frag = '#' + frag
        if href in ('', 'index.html'):
            path = '/'
        elif href.endswith('.html'):
            path = '/' + href[:-5].strip('/') + '/'
        else:
            return m.group(0)
        return '%s="%s%s"' % (m.group(1), path, frag)

    html = re.sub(r'(href|action)="([^"]+)"', link, html)
    # the site's own absolute links stay absolute
    html = html.replace('href="/index/"', 'href="/"')
    return html


def split_page(path):
    src = io.open(path, encoding='utf-8').read()
    head_end = src.index('</head>')
    body_start = src.index('>', src.index('<body')) + 1
    main_start = src.index('<main')
    main_end = src.index('</main>') + len('</main>')
    footer_start = src.index('<footer')
    body_end = src.index('</body>')
    return {
        'chrome': src[body_start:main_start],
        'main': src[main_start:main_end],
        'footer': src[footer_start:body_end],
    }


def main():
    os.makedirs(os.path.join(OUT, 'parts'), exist_ok=True)
    os.makedirs(os.path.join(OUT, 'pages'), exist_ok=True)

    index = split_page(os.path.join(ROOT, 'index.html'))
    io.open(os.path.join(OUT, 'parts', 'header.html'), 'w', encoding='utf-8').write(rewrite(index['chrome']))
    io.open(os.path.join(OUT, 'parts', 'footer.html'), 'w', encoding='utf-8').write(rewrite(index['footer']))

    pages = {
        'home': 'index.html',
        'locations': 'locations.html',
        'team': 'team.html',
        'blog': 'blog.html',
        'contact': 'contact.html',
        'privacy-policy': 'privacy-policy.html',
        'dr-abbie-clinics-terms-and-conditions': 'dr-abbie-clinics-terms-and-conditions.html',
    }
    written = []
    for name, rel in pages.items():
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            continue
        io.open(os.path.join(OUT, 'pages', name + '.html'), 'w', encoding='utf-8').write(rewrite(split_page(p)['main']))
        written.append(name)

    for folder in ('conditions', 'services', 'locations', 'team', 'blog'):
        d = os.path.join(ROOT, folder)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if not f.endswith('.html'):
                continue
            slug = folder + '--' + f[:-5]
            io.open(os.path.join(OUT, 'pages', slug + '.html'), 'w', encoding='utf-8').write(
                rewrite(split_page(os.path.join(d, f))['main']))
            written.append(slug)

    print('header  %d bytes' % os.path.getsize(os.path.join(OUT, 'parts', 'header.html')))
    print('footer  %d bytes' % os.path.getsize(os.path.join(OUT, 'parts', 'footer.html')))
    print('pages   %d' % len(written))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
