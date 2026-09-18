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
    ('Mortlake', 'mortlake', '15 Tennyson Rd, cnr Herbert St', 'NSW 2137', {}),
    ('Sydney City', 'sydney-city', 'Suite 35, Level 7, 88 Pitt St', 'NSW 2000', {}),
    ('Manly', 'manly', 'Shop 8/48–52 Sydney Rd', 'NSW 2095', {}),
    ('Hornsby', 'hornsby', 'Unit 15/14 Edgeworth David Ave', 'NSW 2077', {
        'INTRO': 'Our children-only clinic on Edgeworth David Ave.',
        'FACT4': 'Children only',
        'CTA_EYEBROW': 'Children only &middot; treating young feet since 1990',
        'FAQ3_A': 'Hornsby is our children-only clinic. Every appointment here is a paediatric '
                  'assessment &mdash; in-toeing, out-toeing, flat feet and growing pains.',
    }),
    ('Glenhaven', 'glenhaven', 'Shop 9/78 Glenhaven Rd', 'NSW 2156', {}),
    ('Bowral', 'bowral', 'Shop 3, 2–4 Boolwey St', 'NSW 2576', {}),
    ('Wallsend', 'wallsend', '8 Metcalfe St', 'NSW 2287', {}),
    ('Morisset', 'morisset', 'Shop 4/59 Dora St', 'NSW 2264', {}),
    ('Forster/Tuncurry', 'forster-tuncurry', '111 MacIntosh St', 'NSW 2428', {}),
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
    # Google Business Profiles found on Google Maps, 18 Sept 2026 (place IDs from each
    # listing; the link opens that exact listing, the embed shows its pin and card).
    'kirrawee': ('profile', _cid(10499536010005564975), _embed(
        '!1m18!1m12!1m3!1d1650!2d151.0735456!3d-34.0306017!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b12c768feddef85%3A0x91b5d85f46cdce2f!2sDr.%20Abbie%20Clinics%20-%20Podiatry%2C%20Lower%20Limb%20Biomechanics!5e0!3m2!1sen!2sau!4v1726617600000!5m2!1sen!2sau')),  # Dr. Abbie Clinics - Podiatry, Lower Limb Biomechanics
    'mortlake': ('profile', _cid(17770434117263619916), _embed(
        '!1m18!1m12!1m3!1d1650!2d151.1079126!3d-33.8449173!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b12a5c5fd0b6a83%3A0xf69d43ad87faf74c!2sDr%20Abbie%20Clinics%20Mortlake%20Podiatrists!5e0!3m2!1sen!2sau!4v1726617600000!5m2!1sen!2sau')),  # Dr Abbie Clinics Mortlake Podiatrists
    'manly': ('profile', _cid(17765673780551382427), _embed(
        '!1m18!1m12!1m3!1d1650!2d151.2858639!3d-33.7968317!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b12ab416f3e3625%3A0xf68c5a2d453c759b!2sDr%20Abbie%20Clinics%20-%20Podiatry%20Lower%20Limb%20Biomechanics%20%28Manly%29!5e0!3m2!1sen!2sau!4v1726617600000!5m2!1sen!2sau')),  # Dr Abbie Clinics - Podiatry Lower Limb Biomechanics (Manly)
    'hornsby': ('profile', _cid(12950514141101368338), _embed(
        '!1m18!1m12!1m3!1d1650!2d151.1021375!3d-33.7061413!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b12a759f889033d%3A0xb3b977ff1f052412!2sDr%20Abbie%20Clinics%20-%20Podiatry%20Lower%20Limb%20Biomechanics%20%28Hornsby%29!5e0!3m2!1sen!2sau!4v1726617600000!5m2!1sen!2sau')),  # Dr Abbie Clinics - Podiatry Lower Limb Biomechanics (Hornsby)
    'glenhaven': ('profile', _cid(2245276739669225483), _embed(
        '!1m18!1m12!1m3!1d1650!2d151.0011555!3d-33.6982865!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b12a1cf69e190ef%3A0x1f28d34c7a6e700b!2sDr%20Abbie%20Clinics%20-%20Podiatry%20Lower%20Limb%20Biomechanics%20%28Glenhaven%29!5e0!3m2!1sen!2sau!4v1726617600000!5m2!1sen!2sau')),  # Dr Abbie Clinics - Podiatry Lower Limb Biomechanics (Glenhaven)
    'bowral': ('profile', _cid(6356753673856291458), _embed(
        '!1m18!1m12!1m3!1d1650!2d150.4162915!3d-34.4797896!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b13a296b836c485%3A0x5837b9c96edd1282!2sThe%20Bowral%20Foot%20Clinic!5e0!3m2!1sen!2sau!4v1726617600000!5m2!1sen!2sau')),  # The Bowral Foot Clinic
    'morisset': ('profile', _cid(18170367588417253921), _embed(
        '!1m18!1m12!1m3!1d1650!2d151.489752!3d-33.1075437!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b732842a37926c3%3A0xfc2a1d0d09e1b221!2sPodiatrist%20Morisset%20%7C%20Custom%20Foot%20Australia!5e0!3m2!1sen!2sau!4v1726617600000!5m2!1sen!2sau')),  # Podiatrist Morisset | Custom Foot Australia
    'forster-tuncurry': ('profile', _cid(10310421264267720003), _embed(
        '!1m18!1m12!1m3!1d1650!2d152.5142164!3d-32.1924416!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b7437114f27484b%3A0x8f15f9834d4fb543!2sPodiatrist%20Forster%20Tuncurry%20Sports%20Podiatry!5e0!3m2!1sen!2sau!4v1726617600000!5m2!1sen!2sau')),  # Podiatrist Forster Tuncurry Sports Podiatry
    # No Business Profile found on Google Maps for these three (searched by name and
    # by street address). CLIENT TO CONFIRM whether one exists.
    'sydney-city': ('address', _cid(12836701620138019130), _embed(
        '!1m18!1m12!1m3!1d3312.8799405829755!2d151.20623277570854!3d-33.866984873227324!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b12ae40389f5703%3A0xb225201c9c02093a!2sSte%2035%20Level%207%2F88%20Pitt%20St%2C%20Sydney%20NSW%202000!5e0!3m2!1sen!2sau!4v1784784971780!5m2!1sen!2sau')),
    'narrabri': ('address', _cid(1703924822551671635), _embed(
        '!1m18!1m12!1m3!1d3443.9349992407706!2d149.77965337556446!3d-30.324366674783896!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6ba73444dcbb2ea9%3A0x17a58e992c29b353!2s4%2F159%20Maitland%20St%2C%20Narrabri%20NSW%202390!5e0!3m2!1sen!2sau!4v1784783948622!5m2!1sen!2sau')),
    'wallsend': ('search', 'https://www.google.com/maps/search/?api=1&query=Dr+Abbie+Clinics+Wallsend+NSW',
                 'https://maps.google.com/maps?q=-32.90391048516466,151.66938021069777&z=16&output=embed'),
}

# Phone per clinic. Client: "the numbers are different per location, some have
# tracking numbers and some don't". Four clinic numbers are known (Nookal pages
# and the live site's clinic pages); every other clinic shows the head office number
# until the client supplies its own (or its CallRail number).
HEAD_OFFICE_PHONE = ('+61295454378', '(02) 9545 4378')
PHONES = {
    # The number shown on each clinic's Google Business Profile (18 Sept 2026), so
    # the website and the listing match, as the client asked. Kirrawee, Hornsby and
    # Glenhaven list the head office number there too.
    'mortlake': ('+61258393160', '(02) 5839 3160'),
    'manly': ('+61295387183', '(02) 9538 7183'),
    'bowral': ('+61240052668', '(02) 4005 2668'),
    'morisset': ('+61250185116', '(02) 5018 5116'),
    'forster-tuncurry': ('+61264216618', '(02) 6421 6618'),
    # no Google listing: from the clinic's page on the live site
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
