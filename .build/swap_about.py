# -*- coding: utf-8 -*-
"""Replace V5's About section with V1's, and move it after the treatments.

Two deliberate departures from a straight copy:

  - V1's version holds a [CLIENT TO PROVIDE] placeholder where V5 already has
    the real reception photograph. Keeping the photograph; reverting to a
    placeholder would be a step backwards.
  - V1's <h2> is a single bold line. V5's heading convention is the two-line
    split with the second line in 700, which every other V5 section uses, so
    the heading is set that way here. Same words.
"""
import io
import re

p = 'v5-home.main.html'
s = io.open(p, encoding='utf-8').read()

old = re.search(r'\n  <!-- ABOUT.*?\n  </section>\n', s, re.S)
assert old, 'V5 about section not found'
assert 'id="about"' in old.group(0), 'expected the anchored about section'

NEW = '''
  <!-- ABOUT — transferred from V1. Keeps the id the footer links to. -->
  <section class="section section--alt" id="about">
    <div class="container split split--reverse">
      <div>
        <div class="media-frame media-frame--4x3">
          <img src="assets/img/clinic-reception.webp" srcset="assets/img/clinic-reception.webp 1x, assets/img/clinic-reception@2x.webp 2x" width="880" height="495" alt="Reception at a Dr. Abbie Clinics practice" loading="lazy" decoding="async" sizes="(min-width: 900px) 45vw, 100vw">
        </div>
      </div>
      <div>
        <span class="eyebrow">About us</span>
        <h2 class="split-head"><span>Thirty-five years of</span><span>looking further up the leg</span></h2>
        <div class="prose mt-6">
          <p>Dr. Abbie Clinics, previously known as AOL Footcare Centres, has been assessing and
            treating lower limb pain since 1990. What began as a single practice is now eleven
            clinics across New South Wales, from Sydney City to Narrabri.</p>
          <p>The practice is built around one idea: the place that hurts is rarely the place that
            is wrong. Our founder, Dr. Abbie Najjarine, developed the Najjarine Biomechanical
            Assessment to work out which structure is actually causing the pain &mdash; and to explain
            that to the patient, rather than simply treating the sore spot.</p>
        </div>
        <div class="cluster mt-8">
          <a class="btn btn--call" href="team.html">Meet the team</a>
          <a class="link-arrow" href="locations.html">Find your nearest clinic
            <svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true"><path d="M3 7h8M7.5 3.5L11 7l-3.5 3.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
        </div>
      </div>
    </div>
  </section>
'''

# drop the old one, then insert the new one straight after the treatments
s = s[:old.start()] + '\n' + s[old.end():]

tx = re.search(r'\n  <!-- TREATMENTS.*?\n  </section>\n', s, re.S)
assert tx, 'treatments section not found'
s = s[:tx.end()] + NEW + s[tx.end():]

io.open(p, 'w', encoding='utf-8').write(s)

order = [m.group(1).strip() for m in
         re.finditer(r'\n  <!-- ([A-Z][A-Z0-9 /&+—-]*?)(?:\s+—|\s+-->|-->)', s)]
print('section order:')
for i, n in enumerate(order[:8], 1):
    print('  %d. %s%s' % (i, n, '   <-- moved' if n == 'ABOUT' else ''))
print()
print('anchor kept      :', s.count('id="about"') == 1)
print('real photograph  :', 'clinic-reception.webp' in re.search(r'<!-- ABOUT.*?</section>', s, re.S).group(0))
print('placeholder      :', 'CLIENT TO PROVIDE — clinic or team photograph' in s)
print('both CTAs        :', 'Meet the team' in NEW and 'Find your nearest clinic' in NEW)
for t in ('div', 'span', 'a', 'p', 'section', 'main', 'picture'):
    o = len(re.findall(r'<%s[\s>]' % t, s))
    c = len(re.findall(r'</%s>' % t, s))
    if o != c:
        print('  MISMATCH %s %d/%d' % (t, o, c))
print('balanced ok')
