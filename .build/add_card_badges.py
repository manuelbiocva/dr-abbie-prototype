# -*- coding: utf-8 -*-
"""Add a circular icon badge over each treatment card's photograph.

Glyphs are the ones the cards carried before the photography went in, so the
icon set stays consistent with the rest of the page.
"""
import io
import re

ICONS = {
    'Biomechanics':
        '<path d="M12 3v8m0 0 3.5 3.5M12 11 8.5 14.5M5 19h14" '
        'stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/>',
    'Custom Orthotics':
        '<path d="M4 16c0-5 3-9 8-9s8 4 8 9c0 2-1 3-3 3H7c-2 0-3-1-3-3Z" '
        'stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/>',
    'Shockwave Therapy':
        '<path d="M12 5v14M8 8v8M16 8v8M4 11v2M20 11v2" '
        'stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/>',
    "Children's Podiatry":
        '<path d="M8 21s.5-5 4-5 4 5 4 5M9.5 9a2.5 2.5 0 1 0 5 0 2.5 2.5 0 0 0-5 0ZM5 13c0-4 3-7 7-7s7 3 7 7" '
        'stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/>',
}

p = 'v5-home.main.html'
s = io.open(p, encoding='utf-8').read()

if 'card__badge' in s:
    print('badges already present')
    raise SystemExit

sec = re.search(r'\n  <!-- TREATMENTS.*?\n  </section>\n', s, re.S)
assert sec, 'treatments section not found'
body = sec.group(0)

added = 0
for title, path in ICONS.items():
    # find this card's media div and inject the badge inside it
    pat = re.compile(
        r'(<div class="card__media">)(<img[^>]+>)(</div>\s*<h3>' + re.escape(title) + r'</h3>)')
    badge = ('<span class="card__badge" aria-hidden="true">'
             '<svg viewBox="0 0 24 24" fill="none">' + path + '</svg></span>')
    body, n = pat.subn(lambda m: m.group(1) + badge + m.group(2) + m.group(3), body)
    if n:
        added += 1
    else:
        print('  !! no match for', title)

s = s[:sec.start()] + body + s[sec.end():]
io.open(p, 'w', encoding='utf-8').write(s)

print('badges added   :', added, 'of', len(ICONS))
print('aria-hidden    :', body.count('class="card__badge" aria-hidden="true"'))
print('inside media   :', body.count('<div class="card__media"><span class="card__badge"'))
for t in ('div', 'span', 'a', 'p', 'section', 'main', 'picture'):
    o = len(re.findall(r'<%s[\s>]' % t, s))
    c = len(re.findall(r'</%s>' % t, s))
    if o != c:
        print('  MISMATCH %s %d/%d' % (t, o, c))
print('balanced ok')
