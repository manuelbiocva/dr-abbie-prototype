# -*- coding: utf-8 -*-
"""Bring the treatments grid up to all ten, matching the heading.

Copy is drawn from the live dr-abbie.com treatment pages. Neural Therapy has
no usable image in the supplied assets, so its card keeps a visible
placeholder rather than borrowing another treatment's photograph.
"""
import io
import re

ARROW = ('<svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true">'
         '<path d="M3 7h8M7.5 3.5L11 7l-3.5 3.5" stroke="currentColor" stroke-width="1.7" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')

# title, image slot (None = no photograph supplied), icon path, copy
CARDS = [
    ('Dry Needling', 'tx-dry-needling',
     '<path d="m5 19 8-8m0 0 3-3 3 3-3 3m-3-3 3 3" stroke="currentColor" stroke-width="1.7" '
     'stroke-linecap="round" stroke-linejoin="round"/>',
     'Fine needles inserted into trigger points to break down restrictive tissue.',
     'Dry needling being applied to a patient’s lower leg'),

    ('Foot Mobilisation', 'tx-mobilisation',
     '<path d="M7 7v6a5 5 0 0 0 10 0V7M9 17l-1 4m8-4 1 4" stroke="currentColor" '
     'stroke-width="1.7" stroke-linecap="round"/>',
     'Hands-on work addressing restrictions across the foot’s 26 bones.',
     'A podiatrist mobilising a patient’s foot by hand'),

    ('Sports Podiatry', 'tx-sports',
     '<path d="M13 4a1.5 1.5 0 1 0 0-.01M7 21l3-6 3 2 1 4M5 12l3-3 4 1 3 4" '
     'stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>',
     'Running injuries, return to sport, and footwear that matches your gait.',
     'A runner holding their knee'),

    ('General Foot Care', 'tx-foot-care',
     '<path d="M12 4a8 8 0 1 0 8 8m-8-8v8h8m0-8-3 3" stroke="currentColor" '
     'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>',
     'Routine care including ingrown toenails, corns and calluses.',
     'A foot being treated with a podiatry tool'),

    ('Neural Therapy', None,
     '<path d="M4 12h3l2-5 3 10 3-8 2 3h3" stroke="currentColor" stroke-width="1.7" '
     'stroke-linecap="round" stroke-linejoin="round"/>',
     'Injectable therapy to stimulate a repair response. Paired with prolotherapy.',
     None),

    ('Foot Strapping', 'tx-strapping',
     '<path d="M5 9h14M5 15h14M9 5v14M15 5v14" stroke="currentColor" stroke-width="1.7" '
     'stroke-linecap="round"/>',
     'Therapeutic support to offload tissue while it recovers.',
     'Therapeutic strapping being applied to a patient’s foot'),
]


def card(title, slot, icon, copy, alt):
    if slot:
        media = ('<div class="card__media"><img src="assets/img/%s.webp" '
                 'srcset="assets/img/%s.webp 1x, assets/img/%s@2x.webp 2x" '
                 'width="640" height="400" alt="%s" loading="lazy" decoding="async" '
                 'sizes="(min-width: 900px) 30vw, 100vw"></div>' % (slot, slot, slot, alt))
    else:
        media = ('<div class="card__media"><span class="placeholder">'
                 '[CLIENT TO PROVIDE — Neural Therapy image]</span></div>')
    return (
        '\n        <a class="card reveal" href="service.html">\n'
        '          <span class="card__badge" aria-hidden="true">'
        '<svg viewBox="0 0 24 24" fill="none">%s</svg></span>\n'
        '          %s\n'
        '          <h3>%s</h3>\n'
        '          <p>%s</p>\n'
        '          <span class="card__more">Read more %s</span>\n'
        '        </a>\n' % (icon, media, title, copy, ARROW)
    )


p = 'v5-home.main.html'
s = io.open(p, encoding='utf-8').read()

sec = re.search(r'\n  <!-- TREATMENTS.*?\n  </section>\n', s, re.S)
assert sec, 'treatments section not found'
body = sec.group(0)
assert body.count('<a class="card reveal"') == 4, 'expected the original 4 cards'

new_cards = ''.join(card(*c) for c in CARDS)

# append after the last existing card, before the grid closes
close = '\n      </div>\n'
i = body.rindex('</a>\n')
body = body[:i + len('</a>\n')] + new_cards + body[i + len('</a>\n'):]

# all ten are on screen now, so "View all treatments" no longer says anything
body = re.sub(r'\n      <div class="cluster mt-8">\s*<a class="btn btn--call" href="service\.html">'
              r'View all treatments</a>\s*</div>\n', '\n', body)

s = s[:sec.start()] + body + s[sec.end():]
io.open(p, 'w', encoding='utf-8').write(s)

sec2 = re.search(r'\n  <!-- TREATMENTS.*?\n  </section>\n', s, re.S).group(0)
titles = re.findall(r'<h3>([^<]+)</h3>', sec2)
print('cards now:', len(titles))
for t in titles:
    print('  -', t)
print('\nbadges     :', sec2.count('card__badge'))
print('images     :', sec2.count('<img'))
print('placeholder:', sec2.count('class="placeholder"'))
print('stale CTA  :', 'View all treatments' in sec2)
for t in ('div', 'span', 'a', 'p', 'section', 'main', 'picture'):
    o = len(re.findall(r'<%s[\s>]' % t, s))
    c = len(re.findall(r'</%s>' % t, s))
    if o != c:
        print('  MISMATCH %s %d/%d' % (t, o, c))
print('balanced ok')
