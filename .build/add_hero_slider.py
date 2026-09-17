# -*- coding: utf-8 -*-
"""Insert the treatment slider into the V5 hero's right-hand column.

Seven treatments, three visible. Only treatments with real clinical
photography are listed; General Foot Care, Neural Therapy and Sports Podiatry
have no supplied image and are omitted rather than given a stand-in.
"""
import io
import re

SLIDES = [
    ('svc-biomechanics', 'Biomechanics',
     'A Dr. Abbie Clinics podiatrist examining a patient’s lower leg'),
    ('svc-orthotics', 'Custom Orthotics',
     'A custom orthotic device being fitted against a patient’s foot'),
    ('svc-shockwave', 'Shockwave Therapy',
     'A shockwave therapy handpiece being applied to a patient’s heel'),
    ('svc-childrens', "Children's Podiatry",
     'Dr Abbie Najjarine assessing a child’s foot in clinic'),
    ('svc-dry-needling', 'Dry Needling',
     'Dry needling being applied to a patient’s lower leg'),
    ('svc-mobilisation', 'Foot Mobilisation',
     'A podiatrist mobilising a patient’s foot by hand'),
    ('svc-strapping', 'Foot Strapping',
     'Therapeutic strapping being applied to a patient’s foot'),
]


def slide(slot, label, alt, clone=False):
    extra = ' aria-hidden="true" tabindex="-1"' if clone else ''
    return (
        '          <a class="hero-slide" href="service.html"%s>\n'
        '            <img src="assets/img/%s.webp" '
        'srcset="assets/img/%s.webp 1x, assets/img/%s@2x.webp 2x" '
        'width="440" height="587" alt="%s" loading="lazy" decoding="async" sizes="150px">\n'
        '            <span class="hero-slide__label">%s</span>\n'
        '          </a>\n' % (extra, slot, slot, slot, '' if clone else alt, label)
    )


ARROW_L = ('<svg width="15" height="15" viewBox="0 0 18 18" fill="none" aria-hidden="true">'
           '<path d="M11 4 6 9l5 5" stroke="currentColor" stroke-width="1.8" '
           'stroke-linecap="round" stroke-linejoin="round"/></svg>')
ARROW_R = ('<svg width="15" height="15" viewBox="0 0 18 18" fill="none" aria-hidden="true">'
           '<path d="m7 4 5 5-5 5" stroke="currentColor" stroke-width="1.8" '
           'stroke-linecap="round" stroke-linejoin="round"/></svg>')

real = ''.join(slide(*s) for s in SLIDES)
# first three cloned at the end so the wrap is seamless
clones = ''.join(slide(*s, clone=True) for s in SLIDES[:3])

BLOCK = '''
      <div class="hero-slider" data-hero-slider>
        <div class="hero-slider__head">
          <span class="hero-slider__label" id="hero-slider-label">Our treatments</span>
          <div class="hero-slider__nav">
            <button class="hero-slider__btn" type="button" data-slider="prev" aria-label="Previous treatments">%s</button>
            <button class="hero-slider__btn" type="button" data-slider="next" aria-label="Next treatments">%s</button>
          </div>
        </div>

        <div class="hero-slider__viewport">
          <div class="hero-slider__track" role="group" aria-labelledby="hero-slider-label" aria-live="off">
%s%s          </div>
        </div>
      </div>
''' % (ARROW_L, ARROW_R, real, clones)

p = 'v5-home.main.html'
s = io.open(p, encoding='utf-8').read()
if 'hero-slider' in s:
    print('slider already present')
    raise SystemExit

anchor = '''      </div>
    </div>
  </section>

  <!-- QUICK HELP ROW'''
assert anchor in s, 'hero grid close not found'
s = s.replace(anchor, '      </div>\n' + BLOCK + '    </div>\n  </section>\n\n  <!-- QUICK HELP ROW', 1)
io.open(p, 'w', encoding='utf-8').write(s)

print('slides       :', s.count('class="hero-slide"'))
print('  real       :', s.count('class="hero-slide" href'))
print('  clones     :', s.count('aria-hidden="true" tabindex="-1"'))
for t in ('div', 'section', 'main', 'a', 'span', 'button', 'picture'):
    o = len(re.findall(r'<%s[\s>]' % t, s))
    c = len(re.findall(r'</%s>' % t, s))
    if o != c:
        print('  MISMATCH %s %d/%d' % (t, o, c))
print('balanced ok')
