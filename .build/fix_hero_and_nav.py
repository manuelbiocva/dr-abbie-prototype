# -*- coding: utf-8 -*-
"""Split the V5 hero into base + full-bleed, and make the header transparent.

Two jobs:

1. The full-bleed rewrite replaced the shared `.hero` rules, which broke the
   location page — it still uses the .hero__inner / .hero__copy / .hero__media
   structure and lost its layout. Base styles are restored and the full-bleed
   treatment is moved behind a .hero--bleed modifier.

2. The header goes transparent over the hero and turns solid white on scroll.
   Both V5 heroes sit on Deep Blue, so a reversed logo and light nav text stay
   legible in the transparent state.
"""
import io
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# ---------------------------------------------------------------- theme CSS
p = os.path.join(ROOT, 'assets', 'css', 'theme-v5.css')
s = io.open(p, encoding='utf-8').read()

start = s.index('/* ------')
start = s.index('   HERO — full-bleed photograph')
start = s.rindex('/* ------', 0, start)
end = s.index('/* --------------------------------------------------------------------------\n   QUICK HELP ROW')

NEW = '''/* --------------------------------------------------------------------------
   HERO
   Base = inner pages (location): copy left, image right, on Deep Blue.
   .hero--bleed = the home page: full-bleed photograph with copy overlaid.
   -------------------------------------------------------------------------- */

.hero {
  position: relative;
  overflow: hidden;
  background: var(--deep-blue);
  color: #fff;
  border-bottom: 0;
  padding-block: 0;
  /* pulled up under the transparent header, with the space paid back inside */
  margin-top: calc(var(--header-h) * -1);
  padding-top: var(--header-h);
}
.hero::before { display: none; }

.hero__inner {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--sp-7);
  align-items: center;
  padding-block: clamp(2.5rem, 6vw, 4.5rem);
}
@media (min-width: 960px) {
  .hero__inner { grid-template-columns: 6fr 5fr; gap: var(--sp-9); }
}

.hero__media img {
  width: 100%;
  height: auto;
  aspect-ratio: 4 / 3;
  object-fit: cover;
  border-radius: var(--radius-card);
}
.hero__figure {
  aspect-ratio: 4 / 3;
  border-radius: var(--radius-card);
  background: linear-gradient(155deg, #CFE4F2, #8FC5E6);
  color: var(--deep-blue);
}
.hero__sub { color: rgba(255,255,255,0.86); max-width: 46ch; margin-top: var(--sp-5); }

/* ---- full-bleed variant (home) ---- */

.hero--bleed {
  min-height: 100dvh;
  display: grid;
}
@media (max-width: 899px) {
  .hero--bleed { min-height: min(86dvh, 700px); }
  .hero--bleed .hero__bg img { object-position: 50% 12%; }
}

.hero__bg { position: absolute; inset: 0; z-index: 0; }
.hero__bg picture { display: block; width: 100%; height: 100%; }
.hero__bg img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  /* the band crop already drops the floor, so hold near the top of frame
     and no one loses the top of their head */
  object-position: 50% 18%;
  display: block;
}

/* Scrim. Directional rather than a flat wash: heavy on the left where the
   copy sits, clearing to almost nothing on the right so the team reads as a
   photograph instead of a blue silhouette. Contrast is measured in
   .build/sim_hero_full.py before shipping. */
.hero__bg::after {
  content: "";
  position: absolute;
  inset: 0;
  background:
    linear-gradient(100deg,
      rgba(12,46,71,0.92) 0%,
      rgba(12,46,71,0.86) 22%,
      rgba(12,46,71,0.55) 45%,
      rgba(12,46,71,0.22) 68%,
      rgba(12,46,71,0.12) 100%),
    linear-gradient(to top, rgba(12,46,71,0.55) 0%, rgba(12,46,71,0.18) 30%, rgba(12,46,71,0) 52%);
}

.hero__grid {
  position: relative;
  z-index: 2;
  width: 100%;
  display: grid;
  /* bottom-anchored: at this crop the faces sit in the upper third, so the
     copy block sits below them rather than across anyone. */
  align-content: end;
  padding-block: clamp(3rem, 7vw, 5rem) clamp(3.5rem, 8vw, 6rem);
}

.hero__intro {
  margin-top: var(--sp-5);
  max-width: 46ch;
  font-size: var(--fs-body-lg);
  line-height: 1.6;
  color: rgba(255,255,255,0.88);
}

/* Width in rem, not ch — a ch value here resolves against this element's own
   (body-sized) font, which crushed the headline into a narrow column. */
.hero__anchor { max-width: min(44rem, 62%); }
@media (max-width: 899px) { .hero__anchor { max-width: 100%; } }
.hero__anchor .hero__actions { margin-top: var(--sp-7); }

.hero h1 {
  color: #fff;
  font-size: clamp(2.5rem, 5.6vw, 4.5rem);
  font-weight: 300;
  line-height: 1.02;
  letter-spacing: -0.035em;
  text-wrap: balance;
}
/* The reference sets its headline entirely in bold. The brief's device is a
   light weight with the keyword in bold, so that is kept. */
.hero h1 strong { font-weight: 700; }
.hero--inner h1 { font-size: clamp(2.25rem, 4.6vw, 3.5rem); }

.hero__actions { margin-top: var(--sp-7); }

/* --------------------------------------------------------------------------
   HEADER — transparent over the hero, solid white once scrolled.
   Both V5 heroes sit on Deep Blue, so the reversed logo and light nav text
   hold contrast in the transparent state.
   -------------------------------------------------------------------------- */

.site-header {
  background: transparent;
  box-shadow: none;
  backdrop-filter: none;
  border-bottom: 1px solid transparent;
  transition: background-color var(--dur) var(--ease),
              border-color var(--dur) var(--ease),
              backdrop-filter var(--dur) var(--ease);
}
.site-header.is-scrolled {
  background: rgba(255, 255, 255, 0.94);
  backdrop-filter: saturate(180%) blur(10px);
  border-bottom-color: var(--hairline-soft);
}

/* Reversed state */
.site-header:not(.is-scrolled) .nav__link,
.site-header:not(.is-scrolled) .header-phone,
.site-header:not(.is-scrolled) .nav-toggle { color: #fff; }
.site-header:not(.is-scrolled) .header-phone svg { color: #fff; }
.site-header:not(.is-scrolled) .nav__link:hover,
.site-header:not(.is-scrolled) .nav__link[aria-expanded="true"],
.site-header:not(.is-scrolled) .header-phone:hover,
.site-header:not(.is-scrolled) .nav-toggle:hover {
  background: rgba(255, 255, 255, 0.16);
  color: #fff;
}
.site-header:not(.is-scrolled) .nav__link[aria-current="page"] { color: #fff; }

/* Logo swap. Both images are stacked so neither reflows on the change. */
.logo { position: relative; }
.logo__img--light { position: absolute; inset: 0; opacity: 0; }
.site-header:not(.is-scrolled) .logo__img--dark { opacity: 0; }
.site-header:not(.is-scrolled) .logo__img--light { opacity: 1; }
.logo__img { transition: opacity var(--dur) var(--ease); }

/* The dropdown panel is always a solid surface, so its links stay dark */
.site-header:not(.is-scrolled) .dropdown .dropdown__link { color: var(--ink); }

'''

s = s[:start] + NEW + s[end:]
io.open(p, 'w', encoding='utf-8').write(s)
print('theme-v5.css rewritten | braces %d/%d' % (s.count('{'), s.count('}')))

# ---------------------------------------------------------------- header part
hp = os.path.join(ROOT, '.header.part')
h = io.open(hp, encoding='utf-8').read()
if 'logo__img--light' not in h:
    h = h.replace(
        '<img class="logo__img" src="assets/img/logo.webp"',
        '<img class="logo__img logo__img--dark" src="assets/img/logo.webp"')
    h = h.replace(
        'loading="eager" decoding="async">',
        'loading="eager" decoding="async">\n'
        '      <img class="logo__img logo__img--light" src="assets/img/logo-white.webp" '
        'srcset="assets/img/logo-white.webp 1x, assets/img/logo-white@2x.webp 2x" '
        'width="360" height="183" alt="" aria-hidden="true" loading="eager" decoding="async">', 1)
    io.open(hp, 'w', encoding='utf-8').write(h)
print('.header.part logos:', h.count('logo__img'))

# ---------------------------------------------------------------- components
cp = os.path.join(ROOT, 'assets', 'css', 'components.css')
c = io.open(cp, encoding='utf-8').read()
if 'logo__img--light' not in c:
    c = c.replace('.logo__img { height: 54px; width: auto; }',
                  '.logo__img { height: 54px; width: auto; }\n'
                  '/* Reversed lockup. Hidden unless a theme opts into a transparent header. */\n'
                  '.logo__img--light { display: none; }')
    io.open(cp, 'w', encoding='utf-8').write(c)
print('components.css guard:', '.logo__img--light { display: none; }' in c)

# V5 opts in
s = io.open(p, encoding='utf-8').read()
if 'theme-v5 opts the reversed lockup in' not in s:
    s = s.replace('.logo { position: relative; }',
                  '/* theme-v5 opts the reversed lockup in */\n'
                  '.logo__img--light { display: block; }\n'
                  '.logo { position: relative; }')
    io.open(p, 'w', encoding='utf-8').write(s)
print('theme-v5 opt-in:', '.logo__img--light { display: block; }' in s)

# ---------------------------------------------------------------- home markup
mp = os.path.join(HERE, 'v5-home.main.html')
m = io.open(mp, encoding='utf-8').read()
if 'hero--bleed' not in m:
    m = m.replace('<section class="hero">', '<section class="hero hero--bleed">', 1)
    io.open(mp, 'w', encoding='utf-8').write(m)
print('home hero--bleed:', 'hero--bleed' in m)

# location page: mark its hero as the inner variant
lp = os.path.join(HERE, 'v5-location.main.html')
l = io.open(lp, encoding='utf-8').read()
if 'hero--inner' not in l:
    l = l.replace('<section class="hero hex-texture">', '<section class="hero hero--inner">', 1)
    io.open(lp, 'w', encoding='utf-8').write(l)
print('location hero--inner:', 'hero--inner' in l)
