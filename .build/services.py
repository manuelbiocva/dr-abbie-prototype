# -*- coding: utf-8 -*-
"""The ten treatments, and the per-service copy the template needs.

The clinical description of each treatment is the client's own, taken from the
treatment cards already published on the site. Everything around it -- how long
a course runs, what it feels like, which clinics have the equipment -- is a
stand-in prefixed TEMP:, which the build wraps in a data-temp span. None of it
has been supplied.

Two things are deliberately NOT claimed anywhere below: that a given treatment
is available at every clinic, and any outcome or success rate.
"""

SERVICES = [
    {
        'NAME': 'Biomechanics',
        'SLUG': 'biomechanics',
        'HERO_IMG': 'hero-biomechanics',
        'CARD_IMG': 'tx-biomechanics',
        'ALT': 'Dr Abbie Najjarine assessing a patient’s lower limb',
        'INTRO': 'A full lower limb assessment from the feet up. It is the foundation of every '
                 'treatment plan we prescribe.',
        'FACT1': 'The NBA method', 'FACT2': 'Assessment first',
        'FACT3': 'TEMP_LENGTH',
        'WHAT': 'A biomechanical assessment looks at how you stand, walk and load — not just '
                'the area that hurts. The Najjarine Biomechanical Assessment was developed here '
                'and draws on engineering principles to work out which structure is actually '
                'causing the pain.',
        'WHO': 'Anyone whose pain has not settled, or who has been treated for the sore spot '
               'without the cause being found. It is the starting point for every other '
               'treatment on this site.',
        'STEP1': 'We examine your alignment from the feet up, and watch how you move under load '
                 'rather than only at rest.',
        'STEP2': 'We identify the structural or muscular irregularity causing the pain, and show '
                 'you what we found before anything is prescribed.',
        'STEP3': 'Treatment is then prescribed against that diagnosis — orthotics, '
                 'mobilisation, shockwave or a loading programme, depending on what the '
                 'assessment showed.',
        'CONDITIONS': [
            ('Heel Pain', 'Including first-step pain in the morning'),
            ('Knee Pain', 'Where the cause sits below the knee'),
            ('Shin Splints', 'Pain along the shin with activity'),
            ('Flat Feet', 'Fallen arches in children and adults'),
        ],
        'FAQ': [
            ('What is the Najjarine Biomechanical Assessment?',
             'It is the assessment method developed by our founder, Dr. Abbie Najjarine. It '
             'assesses alignment from the feet up and originates in engineering principles, so '
             'treatment is prescribed against a diagnosis rather than a symptom.'),
            ('How long does the assessment take?',
             'TEMP:Allow about 45 minutes for a first appointment. That covers the assessment, '
             'the diagnosis and an explanation of the plan.'),
            ('Do I need a referral?',
             'No. Podiatry is a primary contact profession in Australia, so you can book '
             'directly. If you are on a Medicare care plan your GP will refer you, and we can '
             'bill that.'),
            ('Will I need orthotics?',
             'Not necessarily. Orthotics are one of ten treatments and are only prescribed if the '
             'assessment shows they are the right answer.'),
            ('What should I bring?',
             'TEMP:Bring the shoes you wear most, and any previous orthotics, scans or reports. '
             'Wear or bring shorts if your knees or hips are involved.'),
        ],
    },
    {
        'NAME': 'Custom Orthotics',
        'SLUG': 'custom-orthotics',
        'HERO_IMG': 'hero-orthotics',
        'CARD_IMG': 'tx-orthotics',
        'ALT': 'A custom orthotic device held against a patient’s foot',
        'INTRO': 'Prescribed devices that change how your foot meets the ground. Manufactured on '
                 'site at our Kirrawee head office.',
        'FACT1': 'Made on site', 'FACT2': 'Prescribed, not off the shelf',
        'FACT3': 'TEMP_TURNAROUND',
        'WHAT': 'A custom orthotic is made to your prescription, not picked off a shelf. It is '
                'designed to change the way load passes through the foot and up the leg, based on '
                'what the biomechanical assessment found.',
        'WHO': 'People whose assessment shows the way they load the foot is driving their pain — '
               'commonly heel pain, arch pain, forefoot pain or knee pain that traces back to '
               'the foot.',
        'STEP1': 'The assessment establishes what your foot is doing under load and why it is '
                 'causing pain where it does.',
        'STEP2': 'We take the prescription and the device is manufactured at our Kirrawee head '
                 'office rather than sent away.',
        'STEP3': 'You come back for fitting and adjustment. Orthotics are normally paired with '
                 'footwear advice so the device is not working against your shoes.',
        'CONDITIONS': [
            ('Flat Feet', 'Fallen arches in children and adults'),
            ('Plantar Fasciitis', 'Arch and heel pain under load'),
            ('Forefoot Pain', 'Including Morton’s neuroma'),
            ('Knee Pain', 'Where the cause sits below the knee'),
        ],
        'FAQ': [
            ('How long do custom orthotics take to make?',
             'TEMP:Usually 7 to 10 days. They are manufactured at our Kirrawee head office rather '
             'than sent to an external lab.'),
            ('Will they fit in my normal shoes?',
             'TEMP:That is part of the prescription. Bring the shoes you wear most to your '
             'appointment so the device is made for them.'),
            ('How are these different from chemist insoles?',
             'An off-the-shelf insole is a generic shape. A custom orthotic is made to a '
             'prescription from your own assessment, to change a specific problem the assessment '
             'identified.'),
            ('Do orthotics hurt to wear at first?',
             'TEMP:There is usually a break-in period. Your podiatrist will tell you how to '
             'introduce them and will adjust the device if needed.'),
            ('Can I claim orthotics on private health?',
             'TEMP:Yes, under most extras policies. We have HICAPS, so the rebate comes off at '
             'reception. Check your own limits with your fund.'),
        ],
    },
    {
        'NAME': "Children's Podiatry",
        'SLUG': 'childrens-podiatry',
        'HERO_IMG': 'hero-childrens',
        'CARD_IMG': 'tx-childrens',
        'ALT': 'Dr Abbie Najjarine examining a child’s feet',
        'INTRO': 'Pigeon toe, flat feet and growing pains, assessed while the foot is still '
                 'developing.',
        'FACT1': 'Hornsby is children only', 'FACT2': 'Assessed as they grow',
        'FACT3': 'TEMP_LENGTH',
        'WHAT': 'Children’s feet are still forming, and some things that look alarming settle '
                'on their own while others do not. An assessment tells you which you are looking '
                'at, and whether anything needs doing now.',
        'WHO': 'Parents who have noticed in-toeing, out-toeing, flat feet, tripping, or a child '
               'who complains of sore legs after activity or at night.',
        'STEP1': 'We assess how your child stands, walks and runs, and compare that against what '
                 'is normal for their age.',
        'STEP2': 'We explain what we found in plain terms, including when the answer is that no '
                 'treatment is needed yet.',
        'STEP3': 'If something does need addressing, treatment is staged around growth and '
                 'reviewed as they develop.',
        'CONDITIONS': [
            ('Pigeon Toe', 'In-toeing gait in children'),
            ('Out Toe', 'Out-toeing gait in children'),
            ('Flat Feet', 'Fallen arches in children and adults'),
            ('Heel Pain', 'Including first-step pain in the morning'),
        ],
        'FAQ': [
            ('At what age should my child be assessed?',
             'TEMP:There is no fixed age. If you have noticed something about the way they walk '
             'or they are complaining of pain, that is the time to have it looked at.'),
            ('Is in-toeing something they grow out of?',
             'It often looks better with age. Where it comes from a twist in the shin bone, the '
             'body tends to hide it by tightening the hip muscles rather than correcting it, so '
             'measuring it is how you know. That is the reason to have it looked at rather than '
             'waiting.'),
            ('Do you have a clinic just for children?',
             'Yes. Our Hornsby clinic sees children only. Children are also seen at our other '
             'clinics.'),
            ('Will my child need orthotics?',
             'Not necessarily. Many children need nothing beyond monitoring. Orthotics are only '
             'prescribed where the assessment shows they will change something.'),
            ('Do I need a referral?',
             'No. You can book directly. If you are on a Medicare care plan your GP will refer '
             'you, and we can bill that.'),
        ],
    },
    {
        'NAME': 'Shockwave Therapy',
        'SLUG': 'shockwave-therapy',
        'HERO_IMG': 'hero-shockwave',
        'CARD_IMG': 'tx-shockwave',
        'ALT': 'Shockwave therapy being applied to a patient’s heel',
        'INTRO': 'Acoustic waves using kinetic energy to stimulate repair in tendon and soft '
                 'tissue. We use it most often for persistent heel pain and Achilles pain.',
        'FACT1': 'Non-surgical', 'FACT2': 'No anaesthetic',
        'FACT3': 'TEMP_SESSIONS',
        'WHAT': 'Shockwave delivers pulses of acoustic energy through the skin to the tissue '
                'underneath. The intention is to provoke the body’s own repair response in '
                'tissue that has stopped settling on its own.',
        'WHO': 'It is usually considered for pain that has persisted despite rest, footwear '
               'changes and load management — most commonly under the heel or in the '
               'Achilles tendon. Whether it suits you is decided at the assessment, not before.',
        'STEP1': 'A full biomechanical examination establishes what is loading the tissue and '
                 'why. Shockwave treats the painful tissue; the assessment works out what put '
                 'the load there.',
        'STEP2': 'If shockwave is appropriate, the applicator is worked over the area for a few '
                 'minutes. No anaesthetic is needed and you can walk out and drive.',
        'STEP3': 'Shockwave is rarely used alone. It is normally paired with orthotic therapy, '
                 'footwear changes or a loading programme so the cause is addressed as well.',
        'CONDITIONS': [
            ('Heel Pain', 'Including first-step pain in the morning'),
            ('Plantar Fasciitis', 'Arch and heel pain under load'),
            ('Achilles Pain', 'Tendon pain and tendonitis'),
            ('Shin Splints', 'Pain along the shin with activity'),
        ],
        'FAQ': [
            ('Does shockwave therapy hurt?',
             'TEMP:Most patients describe it as uncomfortable rather than painful, and the '
             'intensity is adjusted during the session. No anaesthetic is used.'),
            ('How many sessions will I need?',
             'TEMP:That is decided at your assessment and depends on how long the problem has '
             'been there. Your podiatrist will tell you before you commit to a course.'),
            ('Can I walk and drive afterwards?',
             'TEMP:Yes. There is no recovery period and no anaesthetic, so you can leave and '
             'drive straight away.'),
            ('Is shockwave available at every clinic?',
             'TEMP:Shockwave is available at selected clinics. Call the clinic nearest you, or '
             'check the clinic list below, before you book.'),
            ('Do I need a referral?',
             'No. Podiatry is a primary contact profession in Australia, so you can book '
             'directly. If you are on a Medicare care plan your GP will refer you, and we can '
             'bill that.'),
        ],
    },
    {
        'NAME': 'Dry Needling',
        'SLUG': 'dry-needling',
        'HERO_IMG': 'hero-dry-needling',
        'CARD_IMG': 'tx-dry-needling',
        'ALT': 'Dry needling being applied to a patient’s lower leg',
        'INTRO': 'Fine needles inserted into trigger points to break down restrictive tissue.',
        'FACT1': 'Fine needles', 'FACT2': 'No medication injected',
        'FACT3': 'TEMP_SESSIONS',
        'WHAT': 'A fine needle is placed into a trigger point in the muscle or fascia. Nothing is '
                'injected — the needle itself is the treatment, used to release tissue that '
                'has become restrictive.',
        'WHO': 'People with tight or restricted soft tissue in the calf, foot or lower leg that '
               'is contributing to how they load and where they hurt.',
        'STEP1': 'The assessment identifies which tissue is restricted and whether that '
                 'restriction is part of what is causing your pain.',
        'STEP2': 'Needles are placed into the trigger points and left briefly. Most people feel a '
                 'dull ache or a twitch rather than a sharp pain.',
        'STEP3': 'Needling is normally combined with mobilisation, stretching or orthotic therapy '
                 'so the tissue does not simply tighten again.',
        'CONDITIONS': [
            ('Shin Splints', 'Pain along the shin with activity'),
            ('Achilles Pain', 'Tendon pain and tendonitis'),
            ('Heel Pain', 'Including first-step pain in the morning'),
            ('Running Injuries', 'Overuse injury and return to sport'),
        ],
        'FAQ': [
            ('Is dry needling the same as acupuncture?',
             'They use similar needles but not the same reasoning. Dry needling targets specific '
             'trigger points identified in your assessment.'),
            ('Does it hurt?',
             'TEMP:Most people describe a dull ache or a brief twitch rather than a sharp pain. '
             'Tell your podiatrist during the session if it is uncomfortable.'),
            ('Is anything injected?',
             'No. Nothing is injected in dry needling — the needle itself is the treatment. '
             'Injectable treatment is a separate service, Neural Therapy.'),
            ('How will I feel afterwards?',
             'TEMP:Some people feel mild soreness for a day, similar to after exercise. Your '
             'podiatrist will tell you what to expect for your case.'),
            ('How many sessions will I need?',
             'TEMP:It depends on what the assessment found. Your podiatrist will set that out '
             'before you commit to a course.'),
        ],
    },
    {
        'NAME': 'Foot Mobilisation',
        'SLUG': 'foot-mobilisation',
        'HERO_IMG': 'hero-mobilisation',
        'CARD_IMG': 'tx-mobilisation',
        'ALT': 'A podiatrist mobilising a patient’s foot by hand',
        'INTRO': 'Hands-on work addressing restrictions across the foot’s 26 bones.',
        'FACT1': 'Hands-on', 'FACT2': 'No equipment needed',
        'FACT3': 'TEMP_SESSIONS',
        'WHAT': 'There are 26 bones in the foot and each joint between them has a range it should '
                'move through. Mobilisation is hands-on work to restore movement where a joint '
                'has become restricted.',
        'WHO': 'People whose assessment shows a joint is not moving as it should, and that the '
               'restriction is changing how load passes through the foot.',
        'STEP1': 'The assessment establishes which joints are restricted and whether that '
                 'restriction is relevant to your pain.',
        'STEP2': 'The joint is mobilised by hand, working through its range rather than forcing '
                 'it.',
        'STEP3': 'Mobilisation is usually paired with exercises or orthotic therapy so the range '
                 'gained is kept.',
        'CONDITIONS': [
            ('Forefoot Pain', 'Including Morton’s neuroma'),
            ('Flat Feet', 'Fallen arches in children and adults'),
            ('Heel Pain', 'Including first-step pain in the morning'),
            ('Knee Pain', 'Where the cause sits below the knee'),
        ],
        'FAQ': [
            ('Is foot mobilisation the same as a massage?',
             'No. Massage works on soft tissue. Mobilisation works on the joints themselves and '
             'is directed at specific restrictions the assessment found.'),
            ('Does it hurt?',
             'TEMP:It should not. The joint is worked through its range rather than forced. Tell '
             'your podiatrist if anything is uncomfortable.'),
            ('How many sessions will I need?',
             'TEMP:That depends on what the assessment found and how long the restriction has '
             'been there. Your podiatrist will tell you before you commit.'),
            ('Will I need exercises at home?',
             'TEMP:Usually. Range gained in the clinic is easier to keep if it is loaded between '
             'appointments.'),
            ('Do I need a referral?',
             'No. You can book directly. If you are on a Medicare care plan your GP will refer '
             'you, and we can bill that.'),
        ],
    },
    {
        'NAME': 'Sports Podiatry',
        'SLUG': 'sports-podiatry',
        'HERO_IMG': 'hero-sports',
        'CARD_IMG': 'tx-sports',
        'ALT': 'A runner holding their knee',
        'INTRO': 'Running injuries, return to sport, and footwear that matches your gait.',
        'FACT1': 'Gait assessed under load', 'FACT2': 'Return-to-sport planning',
        'FACT3': 'TEMP_LENGTH',
        'WHAT': 'Sports podiatry looks at the demands your sport puts on the lower limb and where '
                'your mechanics are not coping with them. That includes footwear, which is often '
                'working against the athlete rather than for them.',
        'WHO': 'Runners and athletes with overuse injuries, anyone returning to sport after one, '
               'and people whose pain only appears at a certain distance, pace or surface.',
        'STEP1': 'We assess your gait under load rather than standing still, because that is '
                 'where a running injury actually happens.',
        'STEP2': 'We identify what is failing and why — mechanics, load, footwear, or a '
                 'combination.',
        'STEP3': 'Treatment is paired with a return-to-sport plan, so load is rebuilt rather than '
                 'resumed all at once.',
        'CONDITIONS': [
            ('Running Injuries', 'Overuse injury and return to sport'),
            ('Shin Splints', 'Pain along the shin with activity'),
            ('Achilles Pain', 'Tendon pain and tendonitis'),
            ('Knee Pain', 'Where the cause sits below the knee'),
        ],
        'FAQ': [
            ('Do I need to bring my running shoes?',
             'TEMP:Yes. Bring the shoes you train in, including any you have retired recently. '
             'The wear pattern tells us a great deal.'),
            ('Do you do video gait analysis?',
             'TEMP:Gait is assessed under load as part of the biomechanical assessment. Ask the '
             'clinic what is available when you book.'),
            ('How soon can I get back to running?',
             'That depends entirely on what the assessment finds. A return-to-sport plan is part '
             'of the treatment rather than an afterthought.'),
            ('Will you just tell me to rest?',
             'Rest alone rarely fixes an overuse injury, because it does not change what caused '
             'the overload. The assessment is aimed at that cause.'),
            ('Do I need a referral?',
             'No. You can book directly. If you are on a Medicare care plan your GP will refer '
             'you, and we can bill that.'),
        ],
    },
    {
        'NAME': 'General Foot Care',
        'SLUG': 'general-foot-care',
        'HERO_IMG': 'hero-foot-care',
        'CARD_IMG': 'tx-foot-care',
        'ALT': 'A foot being treated with a podiatry tool',
        'INTRO': 'Routine care including ingrown toenails, corns and calluses.',
        'FACT1': 'Routine and recurrent', 'FACT2': 'Sterile instruments',
        'FACT3': 'TEMP_LENGTH',
        'WHAT': 'The everyday work of podiatry: nails, corns, calluses and skin. Straightforward '
                'to treat, and worth treating properly rather than at home.',
        'WHO': 'Anyone with an ingrown nail, painful callus or corn, or who needs nail care they '
               'cannot manage themselves — including patients with diabetes or reduced '
               'circulation, where foot care matters more.',
        'STEP1': 'We look at the problem itself and at whether something about how you load the '
                 'foot is causing it to keep coming back.',
        'STEP2': 'The nail, corn or callus is treated with sterile instruments.',
        'STEP3': 'Where a callus or corn keeps returning, that is usually a loading problem, and '
                 'the assessment is what addresses it.',
        'CONDITIONS': [
            ('Ingrown Toenails', 'Routine and recurrent'),
            ('Forefoot Pain', 'Including Morton’s neuroma'),
            ('Heel Pain', 'Including first-step pain in the morning'),
            ('Flat Feet', 'Fallen arches in children and adults'),
        ],
        'FAQ': [
            ('Does treating an ingrown toenail hurt?',
             'TEMP:Routine treatment is usually not painful. If a procedure is needed, local '
             'anaesthetic is used and your podiatrist will explain it first.'),
            ('Why does my callus keep coming back?',
             'A callus forms where load concentrates. Removing it treats the symptom; the '
             'assessment is what identifies why the load is there.'),
            ('I have diabetes. Can you see me?',
             'TEMP:Yes. Foot care matters more where circulation or sensation is reduced. Tell '
             'reception when you book so enough time is allowed.'),
            ('How often should I come in?',
             'TEMP:That depends on the problem. Your podiatrist will recommend an interval '
             'rather than booking you in indefinitely.'),
            ('Do I need a referral?',
             'No. You can book directly. If you are on a Medicare care plan your GP will refer '
             'you, and we can bill that.'),
        ],
    },
    {
        'NAME': 'Foot Strapping',
        'SLUG': 'foot-strapping',
        'HERO_IMG': 'hero-strapping',
        'CARD_IMG': 'tx-strapping',
        'ALT': 'Therapeutic strapping being applied to a patient’s foot',
        'INTRO': 'Therapeutic support to offload tissue while it recovers.',
        'FACT1': 'Immediate support', 'FACT2': 'Often a diagnostic step',
        'FACT3': 'TEMP_DURATION',
        'WHAT': 'Strapping applies tape to change how load passes through the foot, taking it off '
                'the tissue that is painful while that tissue settles.',
        'WHO': 'People who need support straight away, and people for whom strapping is a test: '
               'if taping the foot a certain way relieves the pain, that tells us something '
               'useful about what an orthotic would need to do.',
        'STEP1': 'The assessment establishes which tissue is overloaded and which direction needs '
                 'supporting.',
        'STEP2': 'Tape is applied to offload that tissue. You will usually know within a day or '
                 'two whether it has helped.',
        'STEP3': 'Strapping is short-term by design. Where it works, it often points towards '
                 'orthotic therapy as the longer-term answer.',
        'CONDITIONS': [
            ('Plantar Fasciitis', 'Arch and heel pain under load'),
            ('Heel Pain', 'Including first-step pain in the morning'),
            ('Flat Feet', 'Fallen arches in children and adults'),
            ('Running Injuries', 'Overuse injury and return to sport'),
        ],
        'FAQ': [
            ('How long does strapping stay on?',
             'TEMP:Usually a few days. Your podiatrist will tell you when to remove it and what '
             'to watch for.'),
            ('Can I shower with it on?',
             'TEMP:Ask your podiatrist — it depends on the tape used. Most strapping '
             'tolerates a shower if it is dried properly afterwards.'),
            ('Is strapping a long-term fix?',
             'No, and it is not meant to be. It offloads tissue while it settles, and it helps '
             'confirm what a longer-term treatment would need to do.'),
            ('Can I strap my own foot at home?',
             'TEMP:Your podiatrist can show you a simple version. Getting the direction and '
             'tension right is what makes it work, and that comes from the assessment.'),
            ('Do I need a referral?',
             'No. You can book directly. If you are on a Medicare care plan your GP will refer '
             'you, and we can bill that.'),
        ],
    },
    {
        'NAME': 'Neural Therapy',
        'SLUG': 'neural-therapy',
        'HERO_IMG': 'hero-neural',
        'CARD_IMG': 'tx-neural',
        'ALT': 'A podiatrist supporting a patient’s foot during treatment',
        'INTRO': 'Injectable therapy to stimulate a repair response. Paired with prolotherapy.',
        'FACT1': 'Injectable', 'FACT2': 'Paired with prolotherapy',
        'FACT3': 'TEMP_SESSIONS',
        'WHAT': 'Neural therapy uses injection to stimulate a repair response in tissue that is '
                'not healing on its own. At Dr. Abbie Clinics it is used alongside prolotherapy.',
        'WHO': 'It is considered for persistent problems where other treatment has not resolved '
               'the pain. Whether it is appropriate for you is decided at the assessment.',
        'STEP1': 'The assessment establishes the diagnosis and whether injectable therapy is a '
                 'reasonable step for it.',
        'STEP2': 'If it is, your podiatrist will explain what is involved, including what to '
                 'expect afterwards, before anything goes ahead.',
        'STEP3': 'As with every treatment here, it is paired with addressing the mechanical cause '
                 'rather than used on its own.',
        'CONDITIONS': [
            ('Heel Pain', 'Including first-step pain in the morning'),
            ('Achilles Pain', 'Tendon pain and tendonitis'),
            ('Plantar Fasciitis', 'Arch and heel pain under load'),
            ('Forefoot Pain', 'Including Morton’s neuroma'),
        ],
        'FAQ': [
            ('What is neural therapy?',
             'An injectable treatment used to stimulate a repair response in tissue that has not '
             'healed on its own. It is used here alongside prolotherapy.'),
            ('Is it painful?',
             'TEMP:Your podiatrist will explain what to expect before anything goes ahead, '
             'including how the injection is managed.'),
            ('How many treatments are needed?',
             'TEMP:That is decided case by case at the assessment rather than set in advance.'),
            ('Is it available at every clinic?',
             'TEMP:Neural therapy is available at selected clinics. Call the clinic nearest you '
             'before booking if this is what you are after.'),
            ('Do I need a referral?',
             'No. You can book directly. If you are on a Medicare care plan your GP will refer '
             'you, and we can bill that.'),
        ],
    },
]

# Stand-ins the build swaps in, then wraps in a data-temp span.
TEMP_TEXT = {
    'TEMP_SESSIONS':   'Course length set at assessment',
    'TEMP_LENGTH':     'About 45 minutes',
    'TEMP_TURNAROUND': 'Usually 7 to 10 days',
    'TEMP_DURATION':   'Support for a few days',
}
