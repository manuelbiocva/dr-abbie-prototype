# -*- coding: utf-8 -*-
"""Google-review widget markup, and the stand-in reviews for each service.

EVERY review below is invented. They exist so the widget can be judged at the
right size and density before a real feed is connected, and they render inside
data-temp spans so they can be found and removed.

No Review or AggregateRating schema is emitted anywhere that uses this.
Publishing fabricated reviews as structured data is a Google policy breach, so
the stand-ins stay visible-only.
"""

STAR = ('<svg viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">'
        '<path d="m10 1 2.6 5.3 5.9.9-4.3 4.2 1 5.8L10 14.5 4.8 17.2l1-5.8L1.5 7.2l5.9-.9z"/>'
        '</svg>')
STARS = '<span class="gstars" aria-hidden="true">%s</span>' % (STAR * 5)


def _mark(depth=''):
    return ('<img class="gcard__mark" src="%sassets/img/google-wordmark.webp" '
            'srcset="%sassets/img/google-wordmark.webp 1x, '
            '%sassets/img/google-wordmark@2x.webp 2x" width="81" height="35" alt="Google" '
            'loading="lazy" decoding="async">' % (depth, depth, depth))


def cards(items, clinic_line='Dr. Abbie Clinics'):
    """Three review cards. `items` is (name, when, text)."""
    out = []
    for i, (name, when, text) in enumerate(items):
        delay = '' if i == 0 else ' data-reveal-delay="%d"' % (i * 60)
        out.append('\n'.join([
            '        <article class="gcard reveal"%s>' % delay,
            '          <div class="gcard__head">',
            '            <span class="gcard__avatar" aria-hidden="true">%s</span>' % name[0],
            '            <span class="gcard__who">',
            '              <span class="gcard__name" data-temp>%s</span>' % name,
            '              <span class="gcard__meta" data-temp>%s &middot; %s</span>'
            % (clinic_line, when),
            '            </span>',
            '            %s' % _mark(),
            '          </div>',
            '          %s' % STARS,
            '          <p class="gcard__text" data-temp>%s</p>' % text,
            '        </article>',
        ]) + '\n')
    return ''.join(out)


def rating_block(count_line):
    return '\n'.join([
        '        <div class="grating">',
        '          %s' % _mark().replace('gcard__mark', 'grating__mark'),
        '          <span class="grating__body">',
        '            <span class="grating__row">%s'
        '<span class="grating__score" data-temp>4.9</span></span>' % STARS,
        '            <span class="grating__count" data-temp>%s</span>' % count_line,
        '          </span>',
        '        </div>',
    ]) + '\n'


# Three stand-in reviews per treatment. Written to sound like different people
# rather than one voice repeated ten times, which is how a duplicated block
# reads on a site with ten service pages.
REVIEWS = {
    'biomechanics': [
        ('Rachel P.', '2 weeks ago', 'First appointment anywhere that looked at my hips as well '
         'as my feet. Turned out that was the whole problem.'),
        ('Ian C.', '1 month ago', 'Showed me on screen what my gait was doing and why it hurt '
         'where it did. No guesswork and no upsell.'),
        ('Marcus L.', '1 month ago', 'Thorough is the word. Took the time to explain what they '
         'found before anything was prescribed.'),
    ],
    'custom-orthotics': [
        ('Helen W.', '3 weeks ago', 'Made on site and fitted the same week. Adjusted them once '
         'and they have been comfortable since.'),
        ('Danny R.', '1 month ago', 'I had chemist insoles for two years doing nothing. These '
         'were made for my actual foot and the difference was obvious.'),
        ('Sofia T.', '2 months ago', 'They asked to see the shoes I actually wear, which nobody '
         'had done before. Makes sense in hindsight.'),
    ],
    'childrens-podiatry': [
        ('Kate M.', '2 weeks ago', 'Took my six year old in for in-toeing. They explained what '
         'was normal for his age and what to watch. No pressure at all.'),
        ('Jason B.', '1 month ago', 'Great with kids. My daughter was nervous and left happy.'),
        ('Nadia H.', '2 months ago', 'Honest advice. We were told nothing needed doing yet and '
         'to come back in six months, which I appreciated.'),
    ],
    'shockwave-therapy': [
        ('Michael B.', '2 weeks ago', 'Six months of heel pain and this was the first thing that '
         'shifted it. Uncomfortable but not painful.'),
        ('Anita K.', '3 weeks ago', 'Explained exactly what it does and what to expect before '
         'starting. Walked out and drove home.'),
        ('Tom H.', '1 month ago', 'Paired it with orthotics rather than selling me shockwave on '
         'its own, which is why I trusted the advice.'),
    ],
    'dry-needling': [
        ('Priya R.', '3 weeks ago', 'Calf had been tight for months. Two sessions and it finally '
         'let go.'),
        ('Ben A.', '1 month ago', 'Not as bad as I expected. More of a dull ache than a sharp '
         'pain, and they checked in throughout.'),
        ('Laura S.', '2 months ago', 'Combined with stretches to do at home, which is what made '
         'it stick.'),
    ],
    'foot-mobilisation': [
        ('Greg N.', '2 weeks ago', 'Hands-on and no equipment. My midfoot had not moved properly '
         'in years and I could feel the difference walking out.'),
        ('Wendy F.', '1 month ago', 'Gentle. Nothing was forced and it did not hurt.'),
        ('Omar D.', '2 months ago', 'Given exercises to keep the range. Explained why that '
         'mattered rather than just handing me a sheet.'),
    ],
    'sports-podiatry': [
        ('Chris V.', '2 weeks ago', 'Brought in my running shoes as asked. The wear pattern told '
         'them more than I could.'),
        ('Elena G.', '1 month ago', 'Back running after a shin problem that had stopped me twice '
         'before. The return plan was the part that worked.'),
        ('Nathan J.', '2 months ago', 'Did not just tell me to rest, which is what I had been '
         'told everywhere else.'),
    ],
    'general-foot-care': [
        ('Margaret O.', '2 weeks ago', 'Ingrown nail sorted quickly and painlessly. Should have '
         'come in months earlier.'),
        ('Peter S.', '1 month ago', 'I am diabetic and they allowed extra time without me having '
         'to ask twice.'),
        ('Julie A.', '2 months ago', 'Explained why the callus kept coming back rather than just '
         'removing it again.'),
    ],
    'foot-strapping': [
        ('Adam T.', '2 weeks ago', 'Taped it and I knew within a day it had helped. That told '
         'them what the orthotic needed to do.'),
        ('Fiona McK.', '1 month ago', 'Immediate relief while we waited on the longer-term plan.'),
        ('Raj P.', '2 months ago', 'Showed me a simple version to do myself between '
         'appointments.'),
    ],
    'neural-therapy': [
        ('Diane L.', '3 weeks ago', 'Talked me through exactly what was involved before anything '
         'went ahead. No surprises.'),
        ('Stuart G.', '1 month ago', 'Persistent problem that had not responded to anything else. '
         'Glad I asked about it.'),
        ('Yvonne C.', '2 months ago', 'Used alongside the rest of the plan rather than on its '
         'own, which is how it was explained to me.'),
    ],
}
