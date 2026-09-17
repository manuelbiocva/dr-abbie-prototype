# -*- coding: utf-8 -*-
"""Wire the derived images into the V5 homepage.

Every img carries explicit width/height (no CLS), srcset for retina, lazy
loading below the fold, and alt text that describes what is actually in the
frame. Two practitioners could not be identified from any source, so their
cards keep placeholders rather than being given a stranger's face.
"""
import io
import re

P = 'v5-home.main.html'
s = io.open(P, encoding='utf-8').read()


def img(slot, w, h, alt, cls='', eager=False, sizes=None):
    load = 'eager" fetchpriority="high' if eager else 'lazy'
    a = [
        'src="assets/img/%s.webp"' % slot,
        'srcset="assets/img/%s.webp 1x, assets/img/%s@2x.webp 2x"' % (slot, slot),
        'width="%d"' % w, 'height="%d"' % h,
        'alt="%s"' % alt,
        'loading="%s"' % load,
        'decoding="async"',
    ]
    if sizes:
        a.append('sizes="%s"' % sizes)
    if cls:
        a.insert(0, 'class="%s"' % cls)
    return '<img ' + ' '.join(a) + '>'


# ----------------------------------------------------------------- 1. HERO
OLD = ('<div class="hero__figure"><span class="placeholder">'
       '[CLIENT TO PROVIDE — hero portrait: practitioner with patient]</span></div>')
NEW = img('hero-practitioner', 720, 900,
          'A podiatrist at a Dr. Abbie Clinics practice',
          eager=True, sizes='(min-width: 960px) 40vw, 100vw')
assert OLD in s
s = s.replace(OLD, NEW)

# ------------------------------------------------------- 2. TREATMENT CARDS
TX = [
    ('Biomechanics', 'tx-biomechanics',
     'A Dr. Abbie Clinics podiatrist examining a patient’s lower leg and foot'),
    ('Custom Orthotics', 'tx-orthotics',
     'A custom orthotic device being fitted against a patient’s foot'),
    ('Shockwave Therapy', 'tx-shockwave',
     'A shockwave therapy handpiece being applied to a patient’s heel'),
    ("Children's Podiatry", 'tx-childrens',
     'Dr Abbie Najjarine assessing a child’s foot in clinic'),
]
for title, slot, alt in TX:
    # drop the icon, lead with the photograph
    pat = re.compile(
        r'(<a class="card reveal" href="service\.html">\s*)'
        r'<span class="card__icon".*?</span>\s*'
        r'(<h3>' + re.escape(title) + r'</h3>)', re.S)
    rep = r'\1<div class="card__media">' + img(slot, 640, 400, alt,
          sizes='(min-width: 900px) 30vw, 100vw') + r'</div>\n          \2'
    s, n = pat.subn(rep, s)
    assert n == 1, 'treatment card not matched: ' + title

# ------------------------------------------------------------- 3. ABOUT
OLD_ABOUT = '''    <div class="container split split--even">
      <div>
        <h2 class="split-head"><span>Treatment on your terms,</span><span>at eleven NSW clinics</span></h2>
      </div>
      <div>
        <span class="eyebrow">About Dr. Abbie Clinics</span>'''
NEW_ABOUT = '''    <div class="container split split--even">
      <div>
        <div class="media-frame media-frame--4x3">
          %s
        </div>
      </div>
      <div>
        <span class="eyebrow">About Dr. Abbie Clinics</span>
        <h2 class="split-head"><span>Treatment on your terms,</span><span>at eleven NSW clinics</span></h2>''' % img(
    'about-team', 880, 660,
    'The Dr. Abbie Clinics podiatry team, with founder Dr Abbie Najjarine at the centre',
    sizes='(min-width: 900px) 45vw, 100vw')
assert OLD_ABOUT in s
s = s.replace(OLD_ABOUT, NEW_ABOUT)
s = s.replace('''        <span class="eyebrow">About Dr. Abbie Clinics</span>
        <h2 class="split-head"><span>Treatment on your terms,</span><span>at eleven NSW clinics</span></h2>
        <div class="prose">''',
              '''        <span class="eyebrow">About Dr. Abbie Clinics</span>
        <h2 class="split-head"><span>Treatment on your terms,</span><span>at eleven NSW clinics</span></h2>
        <div class="prose mt-6">''')

# ------------------------------------------------------- 4. PRACTITIONERS
PEOPLE = [
    ('Dr Abbie Najjarine', 'dr-abbie-najjarine', 420,
     'Dr Abbie Najjarine, Owner and Director of Dr. Abbie Clinics'),
    ('Dr Elissa All', 'dr-elissa-all', 420,
     'Dr Elissa All, Podiatrist at Dr. Abbie Clinics'),
]
for name, slot, px, alt in PEOPLE:
    pat = re.compile(
        r'<div class="person-card__img person-card__figure"><span class="placeholder">\[PHOTO\]</span></div>\s*'
        r'(<h3>' + re.escape(name) + r'</h3>)')
    rep = img(slot, px, px, alt, cls='person-card__img') + r'\n          \1'
    s, n = pat.subn(rep, s)
    assert n == 1, 'practitioner not matched: ' + name

# --------------------------------------------------------------- 5. BLOG
BLOG = [
    ('Sharp Heel Pain', 'blog-heel-pain',
     'A podiatrist mobilising a patient’s foot by hand'),
    ('Custom Orthotics for Flat Feet', 'blog-orthotics',
     'A custom orthotic device held against a patient’s foot'),
    ('Growing Pains, Pigeon Toe', 'blog-children',
     'School children sitting on a wall in school shoes'),
]
for frag, slot, alt in BLOG:
    pat = re.compile(
        r'<div class="post-card__img"><span class="placeholder">\[IMAGE\]</span></div>\s*'
        r'(<div class="post-card__body">\s*<span class="post-card__cat">[^<]*</span>\s*'
        r'<h3>' + re.escape(frag) + r')')
    rep = ('<div class="post-card__img">'
           + img(slot, 640, 400, alt, sizes='(min-width: 900px) 33vw, 100vw')
           + r'</div>\n          \1')
    s, n = pat.subn(rep, s)
    assert n == 1, 'blog card not matched: ' + frag

# ------------------------------------------------- 6. ASSOCIATIONS (new)
ASSOC = '''
  <!-- ASSOCIATIONS — real membership logos from the client's asset library.
       AHPRA has no logo file supplied, so it renders as text. -->
  <section class="section section--tight">
    <div class="container">
      <p class="eyebrow" style="margin-inline:auto;display:flex;width:max-content">Professional memberships</p>
      <div class="assoc mt-6">
        <span class="assoc__item">%s</span>
        <span class="assoc__item">%s</span>
        <span class="assoc__item" style="font-weight:700;color:var(--ink-muted);letter-spacing:.04em">APodA</span>
        <span class="assoc__item" style="font-weight:700;color:var(--ink-muted);letter-spacing:.04em">AHPRA Registered</span>
      </div>
    </div>
  </section>

  <!-- CLINIC FINDER''' % (
    img('assoc-aapsm', 260, 135,
        'American Academy of Podiatric Sports Medicine (AAPSM) logo'),
    img('assoc-sports-med', 260, 135, 'Sports Medicine Australia logo'))

assert s.count('\n  <!-- CLINIC FINDER') == 1
s = s.replace('\n  <!-- CLINIC FINDER', ASSOC, 1)

io.open(P, 'w', encoding='utf-8').write(s)

print('images wired  :', s.count('<img '))
print('eager/priority:', s.count('fetchpriority="high"'))
print('lazy          :', s.count('loading="lazy"'))
print('placeholders  :', s.count('class="placeholder"'))
for t in ('div', 'section', 'main', 'a', 'span', 'h2', 'h3', 'p'):
    o = len(re.findall(r'<%s[\s>]' % t, s))
    c = len(re.findall(r'</%s>' % t, s))
    if o != c:
        print('  MISMATCH %s %d/%d' % (t, o, c))
print('balanced ok')
