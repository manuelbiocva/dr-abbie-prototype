# -*- coding: utf-8 -*-
"""Add the circular arrow badge to every booking CTA.

Touches the shared header/footer parts and the V5 page sources, so the badge
renders identically wherever the booking button appears. The mobile sticky bar
is deliberately skipped: at 44px with two buttons side by side there is no room
for a badge without squeezing the label.
"""
import io
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

ARROW = ('<span class="btn__icon" aria-hidden="true">'
         '<svg width="14" height="14" viewBox="0 0 14 14" fill="none">'
         '<path d="M4.5 9.5 9.5 4.5M5.5 4.5h4v4" stroke="currentColor" '
         'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
         '</svg></span>')

TARGETS = [
    os.path.join(ROOT, '.header.part'),
    os.path.join(ROOT, '.footer.part'),
    os.path.join(HERE, 'v5-home.main.html'),
    os.path.join(HERE, 'v5-location.main.html'),
]

# <a ... class="btn btn--book ..." ...>Label</a>  ->  label + badge
PAT = re.compile(r'(<a class="btn btn--book[^"]*"[^>]*>)([^<]+?)(</a>)')

total = 0
for path in TARGETS:
    if not os.path.exists(path):
        print('missing:', path)
        continue
    s = io.open(path, encoding='utf-8').read()

    def sub(m):
        global total
        open_tag, label, close = m.group(1), m.group(2).strip(), m.group(3)
        # skip the mobile sticky bar - no room beside a second button
        if 'data-source="mobile-bar"' in open_tag:
            return m.group(0)
        if 'btn__icon' in label:
            return m.group(0)
        total += 1
        return '%s%s %s%s' % (open_tag, label, ARROW, close)

    s2 = PAT.sub(sub, s)
    if s2 != s:
        io.open(path, 'w', encoding='utf-8').write(s2)
    print('%-34s badges now: %d' % (os.path.basename(path), s2.count('btn__icon')))

print('\ntotal badges injected:', total)
