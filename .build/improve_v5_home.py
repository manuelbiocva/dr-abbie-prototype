# -*- coding: utf-8 -*-
"""V5 homepage improvements: trust strip, fifth practitioner, FAQ section.

Restores the trust signals the MindCare composition dropped, completes the
practitioner roster from the live site, and adds the FAQ block that earns the
FAQPage schema now injected by assemble.py.
"""
import io

p = 'v5-home.main.html'
s = io.open(p, encoding='utf-8').read()

CHEV = ('<svg width="20" height="20" viewBox="0 0 12 12" fill="none" aria-hidden="true">'
        '<path d="M3 4.5L6 7.5L9 4.5" stroke="currentColor" stroke-width="1.6" '
        'stroke-linecap="round" stroke-linejoin="round"/></svg>')
ARROW = ('<svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true">'
         '<path d="M3 7h8M7.5 3.5L11 7l-3.5 3.5" stroke="currentColor" stroke-width="1.7" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ---------------------------------------------------------------- trust strip
TRUST = u'''
  <!-- TRUST — the MindCare composition has no trust strip. Thirty-five years
       and 250,000 patients are this brand's strongest signals, so they go back in. -->
  <section class="section section--tight">
    <div class="container">
      <div class="trust" data-stagger>
        <div class="trust__item reveal"><span class="trust__figure">1990</span><span class="trust__label">Treating lower limb pain since</span></div>
        <div class="trust__item reveal"><span class="trust__figure">250,000+</span><span class="trust__label">Patients treated</span></div>
        <div class="trust__item reveal"><span class="trust__figure">11</span><span class="trust__label">Clinics across NSW</span></div>
        <div class="trust__item reveal"><span class="trust__figure">AHPRA</span><span class="trust__label">Registered practitioners</span></div>
      </div>
    </div>
  </section>

  <!-- ABOUT'''

assert s.count(u'\n  <!-- ABOUT') == 1, 'about anchor not unique'
s = s.replace(u'\n  <!-- ABOUT', TRUST, 1)

# ------------------------------------------------------- fifth practitioner
FIFTH = u'''
        <a class="card person-card reveal" href="practitioner.html">
          <div class="person-card__img person-card__figure"><span class="placeholder">[PHOTO]</span></div>
          <h3>Dr Mohemed Al-Heyoury</h3>
          <span class="person-card__role">Podiatrist</span>
          <p class="person-card__creds">B. Podiatric Medicine (Western Sydney University, 2023)</p>
          <span class="person-card__go">View profile %s</span>
        </a>

      </div>

      <div class="cluster mt-8">
        <a class="btn btn--call" href="team.html">Show all practitioners</a>
      </div>''' % ARROW

OLD_TEAM_TAIL = u'''
      </div>

      <div class="cluster mt-8">
        <a class="btn btn--call" href="team.html">Show all practitioners</a>
      </div>'''
assert s.count(OLD_TEAM_TAIL) == 1, 'team tail not unique'
s = s.replace(OLD_TEAM_TAIL, FIFTH, 1)

# --------------------------------------------------------------------- FAQ
FAQ = u'''
  <!-- FAQ — carries the FAQPage schema and answers the questions that stop a
       booking. Every answer the client has not supplied stays a placeholder. -->
  <section class="section">
    <div class="container container--narrow">
      <div class="section-head">
        <span class="eyebrow">Common questions</span>
        <h2 class="split-head"><span>Before you</span><span>book with us</span></h2>
      </div>

      <div class="accordion accordion--plain">
        <div class="acc-item">
          <h3><button class="acc-trigger" aria-expanded="false">Do I need a referral to see a podiatrist? %(c)s</button></h3>
          <div class="acc-panel"><div><div class="acc-panel__inner">
            <p><span class="placeholder">[CLIENT TO PROVIDE — answer copy]</span></p>
          </div></div></div>
        </div>
        <div class="acc-item">
          <h3><button class="acc-trigger" aria-expanded="false">What happens at a biomechanical assessment? %(c)s</button></h3>
          <div class="acc-panel"><div><div class="acc-panel__inner">
            <p>We assess how you stand, walk and load, identify the structure causing the pain, and
              explain what we found before any treatment starts. That is the
              <a href="index.html#about">Najjarine Biomechanical Assessment</a>.
              <span class="placeholder">[CLIENT TO CONFIRM — appointment length]</span></p>
          </div></div></div>
        </div>
        <div class="acc-item">
          <h3><button class="acc-trigger" aria-expanded="false">How much does an appointment cost? %(c)s</button></h3>
          <div class="acc-panel"><div><div class="acc-panel__inner">
            <p><span class="placeholder">[CLIENT TO PROVIDE — fees, and whether to publish a pricing table as competitors do]</span></p>
          </div></div></div>
        </div>
        <div class="acc-item">
          <h3><button class="acc-trigger" aria-expanded="false">Can I claim on the day? %(c)s</button></h3>
          <div class="acc-panel"><div><div class="acc-panel__inner">
            <p><span class="placeholder">[CLIENT TO PROVIDE — HICAPS / Medicare EPC / NDIS eligibility]</span></p>
          </div></div></div>
        </div>
        <div class="acc-item">
          <h3><button class="acc-trigger" aria-expanded="false">Which clinic should I book at? %(c)s</button></h3>
          <div class="acc-panel"><div><div class="acc-panel__inner">
            <p>Each of our <a href="index.html#clinics">eleven clinics</a> books into its own diary.
              Choose the one nearest you and you will see the practitioners who work there.</p>
          </div></div></div>
        </div>
      </div>
    </div>
  </section>

  <!-- CLOSING CTA''' % {'c': CHEV}

assert s.count(u'\n  <!-- CLOSING CTA') == 1, 'cta anchor not unique'
s = s.replace(u'\n  <!-- CLOSING CTA', FAQ, 1)

io.open(p, 'w', encoding='utf-8').write(s)

import re
print('sections   :', len(re.findall(r'<section[\s>]', s)))
print('practitioners:', s.count('class="card person-card'))
print('trust items:', s.count('trust__item'))
print('faq items  :', s.count('acc-trigger'))
for t in ('div', 'section', 'main', 'h2', 'h3', 'a'):
    o = len(re.findall(r'<%s[\s>]' % t, s))
    c = len(re.findall(r'</%s>' % t, s))
    if o != c:
        print('  MISMATCH %s %d/%d' % (t, o, c))
print('balanced ok')
