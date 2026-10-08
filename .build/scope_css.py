# -*- coding: utf-8 -*-
"""Raise the prototype stylesheet's specificity for the WordPress build.

Elementor ships `.elementor img { height: auto }`. That selector scores
(0,1,1) and beats the prototype's own single-class rules such as
`.logo-strip__item { height: ... }` at (0,1,0), so every explicitly sized
image fell back to its natural size.

Prefixing each selector with `body ` lifts the prototype rules to (0,1,1) too.
Ties are broken by source order and the prototype sheet is enqueued last, so
the approved design wins without a single !important.

The parser walks the file rather than using regular expressions: comments are
copied verbatim (a comma inside prose is not a selector list), closing braces
are left alone, @keyframes and @font-face bodies are untouched, and @media and
@supports blocks are scoped recursively. Selectors already anchored to
html/body/:root keep their own anchor.

Run:  python .build/scope_css.py
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'assets', 'css')
OUT = os.path.join(ROOT, 'wp-html', 'css')

ANCHORED = ('html', 'body', ':root')
NESTED_AT = ('@media', '@supports', '@container', '@layer')
VERBATIM_AT = ('@keyframes', '@-webkit-keyframes', '@font-face', '@import',
               '@charset', '@property', '@page', '@counter-style')


def split_selectors(sel):
    """Split a selector list on top-level commas only."""
    parts, depth, buf = [], 0, []
    for ch in sel:
        if ch in '([':
            depth += 1
        elif ch in ')]':
            depth -= 1
        if ch == ',' and depth == 0:
            parts.append(''.join(buf))
            buf = []
        else:
            buf.append(ch)
    parts.append(''.join(buf))
    return parts


def prefix(sel):
    out = []
    for part in split_selectors(sel):
        s = part.strip()
        if not s:
            continue
        out.append(s if s.startswith(ANCHORED) else 'body ' + s)
    return ', '.join(out)


def find_block_end(css, open_brace):
    depth, i, n = 1, open_brace + 1, len(css)
    while i < n and depth:
        if css.startswith('/*', i):
            j = css.find('*/', i + 2)
            i = n if j == -1 else j + 2
            continue
        if css[i] == '{':
            depth += 1
        elif css[i] == '}':
            depth -= 1
        i += 1
    return i  # index just past the closing brace


def scope(css):
    out, i, n = [], 0, len(css)
    while i < n:
        if css.startswith('/*', i):                     # comment: copy as-is
            j = css.find('*/', i + 2)
            j = n if j == -1 else j + 2
            out.append(css[i:j])
            i = j
            continue
        if css[i].isspace():
            j = i
            while j < n and css[j].isspace():
                j += 1
            out.append(css[i:j])
            i = j
            continue
        if css[i] == '}':                               # stray close brace
            out.append('}')
            i += 1
            continue

        # read the head up to the next top-level '{'
        j, depth = i, 0
        while j < n:
            if css.startswith('/*', j):
                k = css.find('*/', j + 2)
                j = n if k == -1 else k + 2
                continue
            c = css[j]
            if c in '([':
                depth += 1
            elif c in ')]':
                depth -= 1
            elif c == '{' and depth == 0:
                break
            elif c == '}' and depth == 0:
                break
            j += 1
        if j >= n:
            out.append(css[i:])
            break
        if css[j] == '}':
            out.append(css[i:j])
            i = j
            continue

        head = css[i:j]
        stripped = head.strip()
        end = find_block_end(css, j)
        body = css[j + 1:end - 1]

        if stripped.startswith(NESTED_AT):
            out.append(head + '{' + scope(body) + '}')
        elif stripped.startswith(VERBATIM_AT):
            out.append(css[i:end])
        else:
            out.append(prefix(head) + '{' + body + '}')
        i = end
    return ''.join(out)


def main():
    os.makedirs(OUT, exist_ok=True)
    for name in ('design-system.css', 'components.css', 'theme.css'):
        css = io.open(os.path.join(SRC, name), encoding='utf-8').read()
        scoped = scope(css)
        assert scoped.count('{') == css.count('{'), name + ': brace count changed'
        assert 'body }' not in scoped, name + ': prefixed a closing brace'
        io.open(os.path.join(OUT, name), 'w', encoding='utf-8').write(scoped)
        print('%-20s %7d -> %7d bytes' % (name, len(css), len(scoped)))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
