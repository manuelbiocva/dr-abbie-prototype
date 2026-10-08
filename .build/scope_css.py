# -*- coding: utf-8 -*-
"""Raise the prototype stylesheet's specificity for the WordPress build.

Elementor ships `.elementor img { height: auto }`. That selector scores
(0,1,1), which beats the prototype's own single-class rules such as
`.logo-strip__item { height: ... }` at (0,1,0), so every explicitly sized
image fell back to its natural size.

Prefixing each selector with `body ` lifts the prototype rules to (0,1,1) as
well. A tie is broken by source order, and the prototype sheet is enqueued
last, so the approved design wins without a single !important.

Selectors already anchored to html/body/:root are left alone, as are
@keyframes and @font-face blocks.

Run:  python .build/scope_css.py
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'assets', 'css')
OUT = os.path.join(ROOT, 'wp-html', 'css')

SKIP_PREFIX = ('html', 'body', ':root', ':where(html', ':where(body', 'from', 'to', '@')
SKIP_AT = ('@keyframes', '@-webkit-keyframes', '@font-face', '@import', '@charset', '@property')


def prefix_selector(sel):
    out = []
    for part in sel.split(','):
        s = part.strip()
        if not s:
            continue
        if s.startswith(SKIP_PREFIX) or re.match(r'^\d', s):
            out.append(s)
        else:
            out.append('body ' + s)
    return ', '.join(out)


def scope(css):
    result = []
    i = 0
    n = len(css)
    while i < n:
        brace = css.find('{', i)
        if brace == -1:
            result.append(css[i:])
            break
        head = css[i:brace]
        stripped = head.strip()

        # at-rules that contain nested rule blocks
        if stripped.startswith('@media') or stripped.startswith('@supports'):
            depth = 1
            j = brace + 1
            while j < n and depth:
                if css[j] == '{':
                    depth += 1
                elif css[j] == '}':
                    depth -= 1
                j += 1
            inner = css[brace + 1:j - 1]
            result.append(head + '{' + scope(inner) + '}')
            i = j
            continue

        # at-rules whose contents are not selectors
        if stripped.startswith(SKIP_AT):
            depth = 1
            j = brace + 1
            while j < n and depth:
                if css[j] == '{':
                    depth += 1
                elif css[j] == '}':
                    depth -= 1
                j += 1
            result.append(css[i:j])
            i = j
            continue

        close = css.find('}', brace)
        if close == -1:
            result.append(css[i:])
            break
        body = css[brace + 1:close]
        # keep any comment that sits before the selector
        m = re.match(r'^(\s*(?:/\*.*?\*/\s*)*)(.*)$', head, re.S)
        lead, sel = m.group(1), m.group(2)
        result.append(lead + prefix_selector(sel) + '{' + body + '}')
        i = close + 1
    return ''.join(result)


def main():
    os.makedirs(OUT, exist_ok=True)
    for name in ('design-system.css', 'components.css', 'theme.css'):
        css = io.open(os.path.join(SRC, name), encoding='utf-8').read()
        out = scope(css)
        io.open(os.path.join(OUT, name), 'w', encoding='utf-8').write(out)
        print('%-20s %7d -> %7d bytes' % (name, len(css), len(out)))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
