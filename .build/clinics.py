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

# --------------------------------------------------------------------------
# Google. Client request (Loom, 18 Sept 2026): every clinic listing links to its
# Google Business Profile, and every location page embeds it.
#
# Taken from the live dr-abbie.com/clinics/ page, which already carries a
# Google map per clinic. Only THREE of those are Business Profiles (kind
# 'profile'): Kirrawee, Bowral and Forster/Tuncurry. The rest are Google pins
# on the street address ('address'), and Manly and Wallsend only have raw
# coordinates ('search' -- a Maps search for the business name).
# CLIENT TO PROVIDE for every non-profile clinic: the Business Profile's
# Share -> Copy link (MAPS) and Share -> Embed a map src (EMBED). Paste them
# here; nothing else changes.
#
# MAPS links use ?cid=, Google's stable ID for the place in the embed, so they
# open the same place as the map.
# --------------------------------------------------------------------------
def _cid(n):
    return 'https://maps.google.com/?cid=%d' % n


def _embed(pb):
    return 'https://www.google.com/maps/embed?pb=' + pb


GOOGLE = {
    'kirrawee': ('profile', _cid(10499536010005564975), _embed(
        '!1m18!1m12!1m3!1d26452.13763005133!2d151.03543677431637!3d-34.030601700000005!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b12c768feddef85%3A0x91b5d85f46cdce2f!2sDr.%20Abbie%20Clinics%20-%20Podiatry%2C%20Lower%20Limb%20Biomechanics!5e0!3m2!1sen!2sau!4v1784779046058!5m2!1sen!2sau')),
    'bowral': ('profile', _cid(6356753673856291458), _embed(
        '!1m18!1m12!1m3!1d3288.9106999630176!2d150.4137165757349!3d-34.47978957299905!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b13a296b836c485%3A0x5837b9c96edd1282!2sThe%20Bowral%20Foot%20Clinic!5e0!3m2!1sen!2sau!4v1784782206580!5m2!1sen!2sau')),
    'forster-tuncurry': ('profile', _cid(10310421264267720003), _embed(
        '!1m18!1m12!1m3!1d3376.4374385683864!2d152.51164147563867!3d-32.1924415739134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b7437114f27484b%3A0x8f15f9834d4fb543!2sPodiatrist%20Forster%20Tuncurry%20Sports%20Podiatry!5e0!3m2!1sen!2sau!4v1784783138796!5m2!1sen!2sau')),
    'sydney-city': ('address', _cid(12836701620138019130), _embed(
        '!1m18!1m12!1m3!1d3312.8799405829755!2d151.20623277570854!3d-33.866984873227324!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b12ae40389f5703%3A0xb225201c9c02093a!2sSte%2035%20Level%207%2F88%20Pitt%20St%2C%20Sydney%20NSW%202000!5e0!3m2!1sen!2sau!4v1784784971780!5m2!1sen!2sau')),
    'hornsby': ('address', _cid(8602366673586220600), _embed(
        '!1m18!1m12!1m3!1d3319.1084996368027!2d151.09956257570178!3d-33.70614127328921!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b12a784fec66f1b%3A0x7761bee98ec3ee38!2sUnit%2015%2F14%20Edgeworth%20David%20Ave%2C%20Hornsby%20NSW%202077!5e0!3m2!1sen!2sau!4v1784783708687!5m2!1sen!2sau')),
    'glenhaven': ('address', _cid(10101308842849973922), _embed(
        '!1m18!1m12!1m3!1d3319.4120019518223!2d150.99858057570134!3d-33.69828647329237!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b12a0f6066fffff%3A0x8c2f0edfa095b6a2!2sshop%209%2F78%20Glenhaven%20Rd%2C%20Glenhaven%20NSW%202156!5e0!3m2!1sen!2sau!4v1784783590655!5m2!1sen!2sau')),
    'morisset': ('address', _cid(10864524636155690434), _embed(
        '!1m18!1m12!1m3!1d3342.0585825930775!2d151.4871770756764!3d-33.107543673527346!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b732842a46f95ed%3A0x96c68b98078a3dc2!2s59%20Dora%20St%2C%20Morisset%20NSW%202264!5e0!3m2!1sen!2sau!4v1784781848507!5m2!1sen!2sau')),
    'narrabri': ('address', _cid(1703924822551671635), _embed(
        '!1m18!1m12!1m3!1d3443.9349992407706!2d149.77965337556446!3d-30.324366674783896!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6ba73444dcbb2ea9%3A0x17a58e992c29b353!2s4%2F159%20Maitland%20St%2C%20Narrabri%20NSW%202390!5e0!3m2!1sen!2sau!4v1784783948622!5m2!1sen!2sau')),
    'mortlake': ('address', _cid(2623586381872282655), _embed(
        '!1m18!1m12!1m3!1d417.098395416091!2d151.10716852532522!3d-33.84485690217039!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b12a53d05e1edcf%3A0x2468d9e9f90cbc1f!2sLevel%201%2F15%20Tennyson%20Rd%2C%20Mortlake%20NSW%202137!5e0!3m2!1sen!2sau!4v1784780044269!5m2!1sen!2sau')),
    'manly': ('search', 'https://www.google.com/maps/search/?api=1&query=Dr+Abbie+Clinics+Manly+NSW',
              'https://maps.google.com/maps?q=-33.79686386496303,151.28604594638827&z=16&output=embed'),
    'wallsend': ('search', 'https://www.google.com/maps/search/?api=1&query=Dr+Abbie+Clinics+Wallsend+NSW',
                 'https://maps.google.com/maps?q=-32.90391048516466,151.66938021069777&z=16&output=embed'),
}

# Phone per clinic. Client: "the numbers are different per location, some have
# tracking numbers and some don't". Four clinic numbers are known (Nookal pages
# and the live site's clinic pages); every other clinic shows the head office number
# until the client supplies its own (or its CallRail number).
HEAD_OFFICE_PHONE = ('+61295454378', '(02) 9545 4378')
PHONES = {
    'bowral':   ('+61248613123', '(02) 4861 3123'),
    'morisset': ('+61249732532', '(02) 4973 2532'),
    # from each clinic's page on the live site (dr-abbie.com/clinics/...)
    'forster-tuncurry': ('+61265572034', '(02) 6557 2034'),
    'narrabri': ('+61438922249', '0438 922 249'),
}


def phone(slug):
    return PHONES.get(slug, HEAD_OFFICE_PHONE)


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
