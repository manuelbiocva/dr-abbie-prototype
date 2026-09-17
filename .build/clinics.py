# -*- coding: utf-8 -*-
"""The eleven clinics, and the per-clinic text the location template needs.

Addresses come from the live site and the developer brief. Everything marked
TEMP below is invented stand-in copy at the client's request -- it renders
inside a data-temp span so it can be found again. Nothing here asserts a
clinic-specific fact that is not already published, with two exceptions that
ARE published: Kirrawee is the head office where orthotics are made on site,
and Hornsby is children only.
"""

GENERIC = {
    'ORTHO_SUFFIX':    '',
    'ORTHO_BLURB':     'Custom orthotics are prescribed here and manufactured at our Kirrawee head office.',
    'TREATMENTS_NOTE': 'All ten treatments are available at %s.',
    'NBA_BLURB':       'The assessment that sets the treatment plan.',
    'FACT4':           'Full biomechanical assessment',
    'FAQ2_Q':          'Do you make custom orthotics at %s?',
    'FAQ2_A':          'Orthotics are prescribed here from your assessment and manufactured at our '
                       'Kirrawee head office. <span data-temp>Usually ready within 7 to 10 days.</span>',
    'CTA_EYEBROW':     'Treating lower limb pain since 1990',
    'REVIEW1':         'Explained exactly what was causing the pain before anything was prescribed. '
                       'First time anyone had done that.',
    'INTRO':           'Biomechanical assessment, custom orthotics and sports podiatry in %s.',
}

# name, slug, street, postcode, then any overrides
CLINICS = [
    ('Kirrawee', 'kirrawee', '27 Monro Ave', 'NSW 2232', {
        'INTRO': 'Our head office on Monro Ave, where custom orthotics are made on site.',
        'FACT4': 'Orthotics made on site',
        'ORTHO_SUFFIX': ' &mdash; made on site',
        'ORTHO_BLURB': 'Kirrawee is our head office, where orthotics are manufactured on site.',
        'TREATMENTS_NOTE': 'All ten treatments are available at Kirrawee, including orthotics manufactured on site.',
        'NBA_BLURB': 'The assessment that sets the treatment plan. Orthotics are made on site here.',
        'FAQ2_Q': 'Are orthotics made on site at Kirrawee?',
        'FAQ2_A': 'Kirrawee is our head office and orthotics are manufactured on site. '
                  '<span data-temp>Usually ready within 7 to 10 days.</span>',
        'CTA_EYEBROW': 'Head office &middot; orthotics made on site',
        'REVIEW1': 'Orthotics made on site and fitted the same week. First time in years I have '
                   'walked the dog without heel pain afterwards.',
    }),
    ('Mortlake', 'mortlake', 'Level 1/15 Tennyson Rd', 'NSW 2137', {}),
    ('Sydney City', 'sydney-city', 'Suite 35, Level 7, 88 Pitt St', 'NSW 2000', {}),
    ('Manly', 'manly', 'Shop 8/48–52 Sydney Rd', 'NSW 2095', {}),
    ('Hornsby', 'hornsby', '15/14 Edgeworth David Ave', 'NSW 2077', {
        'INTRO': 'Our children-only clinic on Edgeworth David Ave.',
        'FACT4': 'Children only',
        'CTA_EYEBROW': 'Children only &middot; treating young feet since 1990',
        'FAQ3_A': 'Hornsby is our children-only clinic. Every appointment here is a paediatric '
                  'assessment &mdash; in-toeing, out-toeing, flat feet and growing pains.',
    }),
    ('Glenhaven', 'glenhaven', 'Shop 9/78 Glenhaven Rd', 'NSW 2156', {}),
    ('Bowral', 'bowral', 'Shop 3, 2–4 Boolwey St', 'NSW 2576', {}),
    ('Wallsend', 'wallsend', '8 Metcalfe St', 'NSW 2287', {}),
    ('Morisset', 'morisset', '4/59 Dora St', 'NSW 2264', {}),
    ('Forster/Tuncurry', 'forster-tuncurry', '111 Macintosh St', 'NSW 2428', {}),
    ('Narrabri', 'narrabri', 'Suite 4/159 Maitland St', 'NSW 2390', {}),
]

# --------------------------------------------------------------------------
# Online booking. SUPPLIED BY THE CLIENT, 17 September 2026: one Nookal link per
# clinic, for seven of the eleven. Every booking button on a clinic's page goes
# to that clinic's link and nowhere else -- a wrong-clinic link is a launch
# blocker. Manly, Wallsend, Forster/Tuncurry and Narrabri have no link yet, so
# their pages book by phone instead of pointing at another clinic's diary.
#
# Two addresses above were corrected to match the same Nookal pages: Sydney
# City (Suite 35) and Morisset (4/59). Bowral's "Shop 3, 2-4 Boolwey St" is
# confirmed by its Nookal page. Mortlake is NOT changed: Nookal shows
# "15 Tennyson Road" where the live site shows "Level 1/15" -- client to confirm.
# --------------------------------------------------------------------------
NOOKAL = 'https://book.nookal.com/bookings/book/9E0edcA3-35A8-9fFF-0C33-59ECb896F885/location/'
BOOKING = {
    'kirrawee':    NOOKAL + 'TJJQH',
    'sydney-city': NOOKAL + 'EUHHG',
    'hornsby':     NOOKAL + 'JTJPP',
    'glenhaven':   NOOKAL + 'QVAEG',
    'mortlake':    NOOKAL + 'YPPNN',
    'bowral':      NOOKAL + 'BVMNW',
    'morisset':    NOOKAL + 'MSHVU',
}

# Who takes bookings where, read off the "Select Practitioner" step of each
# clinic's Nookal page (same date). Team slugs, from team_data.py. A clinic
# with no Nookal link has no roster: nobody is claimed to work there.
ROSTER = {
    'kirrawee':    ['dr-abbie-najjarine', 'dr-abdulla-attar-hamoui', 'dr-ahmad-el-jabali',
                    'dr-elissa-all', 'dr-mohemed-al-heyoury', 'dr-yousef-najjarine'],
    'sydney-city': ['dr-abbie-najjarine', 'dr-yousef-najjarine'],
    'hornsby':     ['dr-abbie-najjarine', 'dr-abdulla-attar-hamoui'],
    'glenhaven':   ['dr-abbie-najjarine', 'dr-mohemed-al-heyoury'],
    'mortlake':    ['dr-abbie-najjarine', 'dr-ahmad-el-jabali', 'dr-yousef-najjarine'],
    'bowral':      ['arega-sarkisian', 'dr-ahmad-el-jabali', 'dr-elissa-all',
                    'dr-mohemed-al-heyoury', 'dr-yousef-najjarine'],
    'morisset':    ['dr-abdulla-attar-hamoui', 'dr-elissa-all', 'dr-mohemed-al-heyoury'],
}

# Geography only, for grouping the booking page so a visitor from the Hunter
# does not scroll past six Sydney clinics to find theirs.
REGIONS = [
    ('Sydney', ['kirrawee', 'mortlake', 'sydney-city', 'manly', 'hornsby', 'glenhaven']),
    ('Southern Highlands', ['bowral']),
    ('Newcastle &amp; Lake Macquarie', ['wallsend', 'morisset']),
    ('Mid North Coast', ['forster-tuncurry']),
    ('North West NSW', ['narrabri']),
]

# Published labels shown on clinic cards.
TAGS = {'kirrawee': 'Head office', 'hornsby': 'Children only'}


# TEMP, and deliberately generic: real parking, transport and rosters are
# per-clinic facts nobody has supplied.
TEMP = {
    'PARKING':   'Street parking is available nearby. Call the clinic if you need accessible parking.',
    'TRANSPORT': 'Reachable by train and local bus routes. Call the clinic for the nearest stop.',
    'ROSTER':    'Our podiatrists consult across the eleven clinics. Call to check who is at %s on the day you want.',
    'FAQ3_A':    'Yes. Children’s podiatry is available here, including assessment for '
                 'in-toeing, flat feet and growing pains. Our Hornsby clinic sees children only.',
}


def fields(name, slug, street, post, overrides):
    """Merge generic defaults, temp stand-ins and per-clinic overrides."""
    try:
        from urllib.parse import quote
    except ImportError:
        from urllib import quote
    f = {}
    for src in (GENERIC, TEMP):
        for k, v in src.items():
            f[k] = v % name if '%s' in v else v
    f.update(overrides)
    plain_street = street.replace('&mdash;', '-')
    f.update({
        'NAME': name, 'SLUG': slug, 'STREET': street, 'POST': post,
        'MAPQ': quote('%s, %s %s, Australia' % (
            plain_street.replace('–', '-'), name, post), safe=''),
    })
    return f
