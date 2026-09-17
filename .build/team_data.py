# -*- coding: utf-8 -*-
"""Practitioner profiles for /team/.

SOURCE: dr-abbie.com/practitioners/, read 16 September 2026. Names, titles,
qualifications, memberships, interests and biography facts are taken from that
page. The copy is edited for grammar and consistency only -- nothing is added.
Two edits worth knowing about:
  - "30 years of clinical practice" is written as "in private practice since
    1990". The live page dates from 2018, so the number is already stale;
    the year cannot go out of date.
  - Dr Attar-Hamoui's name. The live page heads his profile "Dr Abdulla
    Attar-Hamoui" and then calls him "Dr Abdalla Attar" in the bio. This uses
    the heading spelling throughout, matching people.py and the planned URL,
    and the spelling is still an open question for the client (PROJECT-PLAN §8).

"Dr" and "(Podiatrist)". AHPRA's advertising guidance expects a practitioner
using the title Dr who is not a medical practitioner to make their profession
clear. The live site does this with "(Podiatrist)", and every page here shows
"Podiatrist" beside the name.

Which clinics each practitioner takes bookings at is NOT held here. It is read
off the clinics' Nookal pages and lives in clinics.ROSTER, so there is one
place to change it. Still not known: consulting days, and AHPRA registration
numbers.

Two practitioners are known only from Nookal (17 September 2026): Dr Ahmad
El-Jabali and Arega Sarkisian. They are not on the live practitioners page, so
their profiles state only what Nookal shows -- name, title, and for Arega the
"B Pod" qualification. No biography, interests or treatments are written for
them. Arega has no photograph in the supplied assets (PHOTO is None).

Nookal lists Dr Najjarine as "Principal Podiatrist", used in ROLE below.

SERVICES are service slugs, chosen from each practitioner's stated interests.
Where an interest has no service page (prolotherapy, massage, injection
therapy) it stays in INTERESTS but gets no card.
"""

TEAM = [
    {
        'NAME': 'Dr Abbie Najjarine',
        'FIRST': 'Abbie',
        'SLUG': 'dr-abbie-najjarine',
        'ROLE': 'Principal Podiatrist &middot; Owner &amp; Director',
        'ROLE_PLAIN': 'Principal Podiatrist, Owner and Director',
        'PHOTO': 'pc-najjarine',
        'INTRO': 'Podiatric biomechanical practitioner, developer of the Najjarine '
                 'Biomechanical Assessment, and in private practice since 1990.',
        'QUALIFICATIONS': [
            'B.Sc Pod (QMU), United Kingdom',
            'Dip Hlth Sc Pod (NSW)',
            'Dip Sport Inj (ACNT)',
            'Dip Rem M (ACNT)',
        ],
        'MEMBERSHIPS': [
            'Australian Podiatry Association (APodA)',
            'Sports Medicine Australia (SMA)',
            'American Academy of Podiatric Sports Medicine (AAPSM)',
        ],
        'INTERESTS': [
            'Lower limb biomechanical assessment',
            'Orthotic therapy',
            'Joint mobilisation',
            'Prolotherapy and neural therapy',
            'Dry needling',
            'Strapping',
        ],
        'SERVICES': ['biomechanics', 'custom-orthotics', 'foot-mobilisation', 'neural-therapy'],
        'BIO': [
            'Dr Abbie Najjarine (Podiatrist) is a podiatric biomechanical practitioner and '
            'lectures in his Najjarine Biomechanical Assessment (NBA) technique, the '
            'assessment behind every treatment plan at Dr. Abbie Clinics. He has been in '
            'private practice since 1990, treating patients with lower limb biomechanical '
            'dysfunction, which has given him extensive experience in the prescription and '
            'application of orthotic therapy.',
            'Alongside his clinical work, Abbie has lectured extensively throughout Australia, '
            'New Zealand, the United Kingdom, Europe and Asia, teaching medical and allied '
            'health professionals lower limb biomechanical assessment and treatment '
            'techniques, joint mobilisation, prolotherapy, neural therapy, dry needling, '
            'strapping and physical therapy treatments.',
            'He is co-founder and inventor of the patented ICB Dual Density Orthotic, invented '
            'the patented Footronics Football Kick Trainer, and is the author of '
            '<em>The Orthotic Revolution</em>.',
            'Abbie is the owner and Director of Dr. Abbie Clinics, and has been Director of AOL '
            'Footcare Centre since 1993. He was Director and Founder of the International '
            'College of Biomechanics from 1996 to 2019, Director of ICB Medical from 2000 to '
            '2019 and of ICB Gait and Posture Clinics from 2003 to 2019, and a board member of '
            'the Australian Podiatry Association (NSW &amp; ACT) from 2010 to 2013.',
        ],
        'QUOTE': '',
    },
    {
        'NAME': 'Dr Abdulla Attar-Hamoui',
        'FIRST': 'Abdulla',
        'SLUG': 'dr-abdulla-attar-hamoui',
        'ROLE': 'Podiatrist',
        'ROLE_PLAIN': 'Podiatrist',
        'PHOTO': 'pc-attar',
        'INTRO': 'Podiatrist with a background in footwear technology and a passion for '
                 'sports-centred biomechanics.',
        'QUALIFICATIONS': ['Bachelor of Podiatry (Western Sydney University)'],
        'MEMBERSHIPS': ['Sports Medicine Australia (SMA)'],
        'INTERESTS': ['Sports-centred biomechanics', 'Footwear technology'],
        'SERVICES': ['sports-podiatry', 'biomechanics'],
        'BIO': [
            'Dr Abdulla Attar-Hamoui (Podiatrist) graduated from Western Sydney University with '
            'a Bachelor of Podiatry. Throughout his time at university he worked as a Fit '
            'Technician at The Athlete’s Foot, and he brings to the team detailed knowledge of '
            'modern footwear technology as well as a passion for sports-centred biomechanics.',
            'Having grown up as an active member of his local rugby league club, with an '
            'ambition to play first grade, he now finds his reward in patient-centred care. As '
            'an active member of Sports Medicine Australia, Abdulla is driven to keep learning, '
            'so his professional development continues in and outside the clinic.',
        ],
        'QUOTE': 'Life lived for the betterment of others is a life worth living.',
    },
    {
        'NAME': 'Dr Elissa All',
        'FIRST': 'Elissa',
        'SLUG': 'dr-elissa-all',
        'ROLE': 'Podiatrist',
        'ROLE_PLAIN': 'Podiatrist',
        'PHOTO': 'pc-elissa',
        'INTRO': 'Podiatrist with further training in lower limb biomechanics, graduated with '
                 'distinction from Western Sydney University.',
        'QUALIFICATIONS': ['Bachelor of Podiatric Medicine, with distinction '
                           '(Western Sydney University)'],
        'MEMBERSHIPS': ['Australian Podiatry Association (APodA)'],
        'INTERESTS': [
            'Lower limb biomechanics',
            'Massage therapy',
            'Foot mobilisations',
            'Dry needling',
            'Orthotic prescription',
            'Injection therapies',
        ],
        'SERVICES': ['foot-mobilisation', 'dry-needling', 'custom-orthotics', 'biomechanics'],
        'BIO': [
            'Dr Elissa All (Podiatrist) graduated with distinction from Western Sydney '
            'University with a Bachelor of Podiatric Medicine. She has further training in '
            'lower limb biomechanics, with a core focus on massage therapy, foot mobilisations, '
            'dry needling, orthotic prescription and injection therapies.',
            'Having grown up with lower limb abnormalities herself, Elissa was inspired to '
            'focus on biomechanics, and is passionate about helping others through quality, '
            'patient-centred care. As a member of the Australian Podiatry Association, she is '
            'committed to her ongoing professional development.',
        ],
        'QUOTE': '',
    },
    {
        'NAME': 'Dr Yousef Najjarine',
        'FIRST': 'Yousef',
        'SLUG': 'dr-yousef-najjarine',
        'ROLE': 'Podiatrist',
        'ROLE_PLAIN': 'Podiatrist',
        'PHOTO': 'pc-yousef',
        'INTRO': 'Podiatrist with further biomechanical training in dry needling, foot '
                 'mobilisation, shockwave and orthotic therapy.',
        'QUALIFICATIONS': ['Bachelor of Podiatric Medicine (Western Sydney University), 2023'],
        'MEMBERSHIPS': [],
        'INTERESTS': [
            'Dry needling',
            'Foot mobilisations',
            'Shockwave therapy',
            'Orthotic therapy',
            'Injection therapy',
        ],
        'SERVICES': ['dry-needling', 'foot-mobilisation', 'shockwave-therapy', 'custom-orthotics'],
        'BIO': [
            'Dr Yousef Najjarine (Podiatrist) completed his Bachelor of Podiatric Medicine at '
            'Western Sydney University in 2023.',
            'He has since taken part in further biomechanical training covering dry needling, '
            'foot mobilisations, shockwave therapy, orthotic therapy and injection therapy.',
        ],
        'QUOTE': '',
    },
    {
        'NAME': 'Dr Mohemed Al-Heyoury',
        'FIRST': 'Mohemed',
        'SLUG': 'dr-mohemed-al-heyoury',
        'ROLE': 'Podiatrist',
        'ROLE_PLAIN': 'Podiatrist',
        'PHOTO': 'pc-alheyoury',
        'INTRO': 'Western Sydney University graduate with further biomechanical training in '
                 'shockwave therapy, orthotic therapy and dry needling.',
        'QUALIFICATIONS': ['Bachelor of Podiatric Medicine (Western Sydney University), 2023'],
        'MEMBERSHIPS': [],
        'INTERESTS': [
            'Dry needling',
            'Foot mobilisations',
            'Shockwave therapy',
            'Orthotic therapy',
            'Injection therapy',
        ],
        'SERVICES': ['shockwave-therapy', 'dry-needling', 'foot-mobilisation', 'custom-orthotics'],
        'BIO': [
            'Dr Mohemed Al-Heyoury (Podiatrist) completed his Bachelor of Podiatric Medicine at '
            'Western Sydney University in 2023.',
            'He has since taken part in further biomechanical training covering dry needling, '
            'foot mobilisations, shockwave therapy, orthotic therapy and injection therapy.',
        ],
        'QUOTE': '',
    },
    {
        'NAME': 'Dr Ahmad El-Jabali',
        'FIRST': 'Ahmad',
        'SLUG': 'dr-ahmad-el-jabali',
        'ROLE': 'Podiatrist',
        'ROLE_PLAIN': 'Podiatrist',
        'PHOTO': 'pc-eljabali',
        'INTRO': 'Podiatric biomechanical practitioner at Dr. Abbie Clinics.',
        'QUALIFICATIONS': [],
        'MEMBERSHIPS': [],
        'INTERESTS': [],
        'SERVICES': [],
        'BIO': [
            'Dr Ahmad El-Jabali (Podiatrist) is a podiatric biomechanical practitioner at '
            'Dr. Abbie Clinics.',
        ],
        'QUOTE': '',
    },
    {
        'NAME': 'Arega Sarkisian',
        'FIRST': 'Arega',
        'SLUG': 'arega-sarkisian',
        'ROLE': 'Podiatrist',
        'ROLE_PLAIN': 'Podiatrist',
        'PHOTO': None,
        'INTRO': 'Podiatrist at Dr. Abbie Clinics.',
        'QUALIFICATIONS': ['B Pod'],
        'MEMBERSHIPS': [],
        'INTERESTS': [],
        'SERVICES': [],
        'BIO': [
            'Arega Sarkisian (B Pod) is a podiatrist at Dr. Abbie Clinics.',
        ],
        'QUOTE': '',
    },
]
