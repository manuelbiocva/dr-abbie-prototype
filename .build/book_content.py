# -*- coding: utf-8 -*-
"""'Understanding ...' sections for the condition and treatment pages.

SOURCE: Dr A.R. Najjarine, "Clinical Biomechanics of the Lower Limbs using the
NBA(TM) System" (FINAL BOOK 2026.pdf, supplied by the client 18 Sept 2026 with
the instruction to use it as the context for every condition and service
page, "in a very snapshot way, for someone to easily understand").

Rules followed:
  - Only what the book says, rewritten in plain English for patients. The
    book is written for practitioners, so measurements and terms are
    explained rather than copied.
  - The book's outcome language ("tremendous results", "quick pain relief",
    "excellent treatment regime") is left out. Advertising of a health
    service may not promise results (AHPRA), and the rest of the site does
    not either.
  - Where the book has nothing on a topic (ingrown toenails, general foot
    care), the page gets no section. Nothing is invented to fill it.
  - Each entry records the chapter it comes from (PAGES = the book's own
    page numbers) so the client can check every line.

TYPES: optional "where it hurts / which type" strip, (label, sub, text).
POINTS: snapshot cards, (heading, html).
"""

BOOK = ('Adapted from <cite>Clinical Biomechanics of the Lower Limbs using the NBA&trade; '
        'System</cite> by Dr A.R. Najjarine')

CONDITIONS = {
    'heel-pain': {
        'PAGES': 'Chapter 15 (pp. 297&ndash;299) and Chapter 7 (p. 124)',
        'INTRO': 'Most heel pain comes from the thick band of tissue under the foot (the plantar '
                 'fascia) pulling where it attaches to the heel bone. Where on the heel it hurts '
                 'is a clue to how your foot is moving.',
        'TYPES_TITLE': 'Where it hurts points to why',
        'TYPES': [
            ('Inner heel', 'Foot rolls in', 'Linked with the foot rolling inwards too far '
             '(over-pronation), which stretches the inner edge of the fascia.'),
            ('Centre of the heel', 'Rolls out, then in', 'The foot lands on its outer edge, then '
             'rolls in. The heel becomes a pivot point for both movements.'),
            ('Outer heel', 'Foot rolls out', 'Linked with the foot rolling outwards (supination), '
             'loading the outer attachment.'),
        ],
        'POINTS': [
            ('Why the first steps hurt most',
             '<p>People often describe it as a hot, sharp pain through the heel when they get out '
             'of bed, taking 5&ndash;10 minutes to ease. It returns after sitting, and burns '
             'after a long day standing.</p>'),
            ('Three names, one process',
             '<ul><li><strong>Plantar fasciitis</strong>: repeated strain causes tiny tears and '
             'inflammation at the attachment.</li><li><strong>Plantarfasciosis</strong>: over '
             'time the tissue thickens and scars, often without inflammation. It can be seen on '
             'ultrasound and is harder to treat the longer it is left.</li><li><strong>Heel '
             'spur</strong>: a bony growth that forms as the body compensates. The pain feels '
             'the same.</li></ul>'),
            ('Same diagnosis, different plan',
             '<p>Two people can both be told they have plantar fasciitis for opposite reasons: '
             'one whose longer leg rolls in to level up with the shorter one, another whose foot '
             'rolls out. The treatment is different for each, which is why the assessment comes '
             'first.</p>'),
            ('What a plan can include',
             '<p>Orthotics with additions, strapping, massage and foot adjustments, '
             '<a href="services/shockwave-therapy.html">shockwave</a>, '
             '<a href="services/dry-needling.html">dry needling</a> and injection therapy, '
             'each aimed at the area that hurts.</p>'),
        ],
    },
    'plantar-fasciitis': {
        'PAGES': 'Chapter 15 (pp. 297&ndash;299) and Chapter 6 (p. 111)',
        'INTRO': 'The plantar fascia is a band of tissue running from the heel bone to the ball of '
                 'the foot. Plantar fasciitis is what happens when it is repeatedly over-stretched '
                 'at its attachment on the heel.',
        'TYPES_TITLE': 'How it progresses',
        'TYPES': [
            ('Plantar fasciitis', 'Early', 'Constant, repetitive strain causes tiny tears and '
             'inflammation where the fascia attaches to the heel.'),
            ('Plantarfasciosis', 'Longer term', 'The body lays down thickening and scar tissue. '
             'There is usually no longer inflammation, and it becomes harder to treat.'),
            ('Heel spur', 'Compensation', 'A small bony growth forms at the attachment. It causes '
             'the same pain rather than being a separate problem.'),
        ],
        'POINTS': [
            ('What is actually happening',
             '<p>When the foot rolls in too far, the arch drops and the foot lengthens. That '
             'stretches the fascia at its heel attachment on every step. Overnight it is not '
             'under load, which is why getting out of bed hurts most.</p>'),
            ('Inner, centre or outer heel',
             '<p>The fascia has inner, central and outer bands. Inner heel pain is linked with '
             'rolling in, outer heel pain with rolling out, and central pain with a foot that '
             'does both in one step.</p>'),
            ('Why leg length can matter',
             '<p>If one leg is longer, that foot may roll in more to level the body up, '
             'straining the inner heel. The plan can then include raising the shorter leg, not '
             'just supporting the arch.</p>'),
            ('What a plan can include',
             '<p><a href="services/custom-orthotics.html">Orthotics</a> and additions, '
             '<a href="services/foot-strapping.html">strapping</a>, massage and foot '
             'adjustments, shockwave, dry needling and injection therapy.</p>'),
        ],
    },
    'achilles-pain': {
        'PAGES': 'Chapter 15 (pp. 305&ndash;311)',
        'INTRO': 'The Achilles tendon joins the calf to the back of the heel. Our '
                 'assessment looks at which side of the tendon hurts, because each side points to a '
                 'different way the foot is moving.',
        'TYPES_TITLE': 'Which side of the tendon',
        'TYPES': [
            ('Inner side', 'Foot rolls in', 'Burning pain and inflammation on the inside of the '
             'ankle, behind the ankle bone. Rolling in puts extra strain on the inner tendon.'),
            ('Both sides', 'Rolls out, then in', 'Burning, sharp pain and swelling either side '
             'of the attachment, sometimes with a hard lump on the tendon.'),
            ('Outer side', 'Foot rolls out', 'Pain and swelling on the outer side. Often a '
             'high-arched foot that stays rolled out through the whole step.'),
        ],
        'POINTS': [
            ('Tendonitis or tendonosis?',
             '<p>The main difference is time. <strong>Tendonitis</strong> is short-term '
             'inflammation, often after a direct injury. <strong>Tendonosis</strong> is '
             'long-term, from repeated strain or an injury that has not healed.</p>'),
            ('The name matters less than the cause',
             '<p>It matters less what the diagnosis is called than '
             'finding the biomechanical reason for it. That reason is what the treatment is '
             'aimed at.</p>'),
            ('Why it should not be ignored',
             '<p>Over time, strain can cause small tears, scarring and adhesions in the tendon. '
             'Pain on both sides of the tendon puts it under strain from two directions at '
             'once.</p>'),
            ('What a plan can include',
             '<p><a href="services/custom-orthotics.html">Orthotics</a> (with forefoot '
             'additions where needed), <a href="services/shockwave-therapy.html">shockwave</a>, '
             'dry needling, manipulation and massage, and injection therapy.</p>'),
        ],
    },
    'shin-splints': {
        'PAGES': 'Chapter 15 (pp. 300&ndash;304)',
        'INTRO': 'There are three types of shin splints. Each is named for the part of '
                 'the shin that hurts, and each is linked to a different muscle and a different '
                 'way the foot moves.',
        'TYPES_TITLE': 'Three types of shin splints',
        'TYPES': [
            ('Inner edge (medial)', 'Foot rolls in', 'The arch drops and the foot lengthens, '
             'stretching the tibialis posterior muscle until it develops tiny tears.'),
            ('Front (anterior)', 'Rolls out, then in', 'The foot lands on its outer edge, then '
             'snaps inwards. The sudden change strains the tibialis anterior muscle at the '
             'front.'),
            ('Outer edge (lateral)', 'Foot rolls out', 'The foot stays rolled out through the '
             'whole step, straining the peroneal muscles on the outside of the leg.'),
        ],
        'POINTS': [
            ('Why it builds with training',
             '<p>The strain is repetitive, so it gets worse as training volume and intensity go '
             'up, because the same foot movement repeats with every step.</p>'),
            ('Where it hurts guides the orthotic',
             '<p>An inner-edge type usually needs the rolling-in controlled. Front and outer '
             'types need the forefoot corrected so the foot stops landing on its outer '
             'edge.</p>'),
            ('What a plan can include',
             '<p><a href="services/custom-orthotics.html">Orthotics</a>, '
             '<a href="services/dry-needling.html">dry needling</a>, '
             '<a href="services/shockwave-therapy.html">shockwave</a>, manipulation and '
             'massage.</p>'),
        ],
    },
    'forefoot-pain': {
        'PAGES': 'Chapter 15 (pp. 294&ndash;296)',
        'INTRO': 'Pain in the ball of the foot falls into two main types. They feel '
                 'different and have different causes.',
        'TYPES_TITLE': 'Two main types',
        'TYPES': [
            ('Metatarsalgia', 'General, burning', 'Pain spread across the ball of the foot. As a '
             'rolled-in foot lengthens, it creates shearing forces on the long bones’ heads '
             'and loses the arch across the forefoot.'),
            ('Morton’s neuroma', 'Localised, nerve', 'A nerve between the long bones becomes '
             'trapped and swells, usually between the 2nd/3rd or 3rd/4th toes.'),
        ],
        'POINTS': [
            ('How a neuroma changes over time',
             '<p>It starts as localised pain, then numbness, tingling or pins and needles into '
             'the toes. Over time the body forms scar tissue around the nerve to protect '
             'it.</p>'),
            ('Why it needs a proper look',
             '<p>A cyst between the toes, bursitis or a torn plantar plate can feel similar. '
             'Telling them apart is part of the assessment.</p>'),
            ('What a plan can include',
             '<p><a href="services/custom-orthotics.html">Orthotics</a> with a metatarsal dome, '
             'which supports the arch across the forefoot, '
             '<a href="services/dry-needling.html">dry needling</a>, foot mobilisation and '
             'massage. For a neuroma, an injection can help separate the bones.</p>'),
        ],
    },
    'knee-pain': {
        'PAGES': 'Chapter 15 (pp. 312&ndash;322)',
        'INTRO': 'Knee pain without an injury often starts at the foot. There are three '
                 'areas of the knee, each linked to a different foot movement.',
        'TYPES_TITLE': 'Which part of the knee',
        'TYPES': [
            ('Inner knee', 'Foot rolls in', 'For every degree the foot rolls in, the shin turns '
             'in by about the same amount, straining the inner knee ligament. The hip muscles '
             'tighten to compensate.'),
            ('Front of the knee', 'Rolls out, then in', 'The shin turns out, then suddenly in, '
             'twisting the knee so the kneecap tracks from side to side.'),
            ('Outer knee', 'Foot rolls out', 'Rolling out through the whole step strains the '
             'outer knee ligament and can contribute to ITB syndrome.'),
        ],
        'POINTS': [
            ('Osgood-Schlatter in teenagers',
             '<p>A tender lump just below the kneecap, most often in active teenagers aged about '
             '13&ndash;17 and more often boys. The kneecap tendon pulls on the growing area of '
             'the shin bone, and a twist in the leg can add to that pull.</p>'),
            ('Why the hips come into it',
             '<p>When the shin is twisted, the hip muscles tighten to straighten the leg up. '
             'The knee is caught between the two, which is why the assessment includes the '
             'hips.</p>'),
            ('What a plan can include',
             '<p><a href="services/custom-orthotics.html">Orthotics</a>, knee '
             '<a href="services/foot-strapping.html">taping</a>, dry needling, strengthening '
             'and stretching, mobilisation, shockwave and injection therapy.</p>'),
        ],
    },
    'flat-feet': {
        'PAGES': 'Chapters 6 and 11 (pp. 109&ndash;112, 229&ndash;235)',
        'INTRO': 'A flat or rolled-in foot is called over-pronation. Some rolling in '
                 'is normal: it is how the foot absorbs shock. The problem is when it goes too far '
                 'for too long.',
        'TYPES_TITLE': 'How far should a foot roll in?',
        'TYPES': [
            ('Ideal', 'Heel upright', 'Standing relaxed, the heel sits between upright and a few '
             'degrees tilted: 0&ndash;4&deg;.'),
            ('Normal shock absorption', 'Up to 4&deg;', 'When walking, the foot should only roll '
             'in about 4&deg; from its neutral position to absorb impact.'),
            ('Over-pronation', 'Beyond that', 'The arch drops, the foot lengthens and the '
             'strain moves up the leg.'),
        ],
        'POINTS': [
            ('When the foundation drops',
             '<p>The foot is the body’s foundation: when it collapses, '
             'it brings everything above with it. A common pattern is inner heel pain in the '
             'morning, inner shin pain and inner knee pain together.</p>'),
            ('It runs in families',
             '<p>These biomechanical traits are often inherited and '
             'passed down through generations, often alongside a twist in the shin '
             '(pigeon-toed or out-toed).</p>'),
            ('Checking an orthotic',
             '<p>A support that flattens like a pancake under thumb pressure is not supporting '
             'much. An orthotic should also sit stable on a flat surface without wobbling.</p>'),
            ('Matched to you',
             '<p>How firm the orthotic needs to be depends on how far your foot rolls in and on '
             'your body weight. Different shoes may need different styles.</p>'),
        ],
    },
    'running-injuries': {
        'PAGES': 'Chapter 13 (pp. 255&ndash;262)',
        'INTRO': 'Running multiplies every small misalignment. This is '
                 'why a foot that copes with walking can break down with mileage.',
        'TYPES_TITLE': 'What changes when you run',
        'TYPES': [
            ('4&ndash;5&times; body weight', 'Every stride', 'The force through the feet when '
             'running on hard ground is four to five times your body weight.'),
            ('Hard, flat surfaces', 'Roads and synthetic turf', 'Hard, flat ground returns more '
             'force to the body than natural terrain, and footwear has not changed to match.'),
            ('Hidden compensation', 'Shows up downhill', 'A twisted shin the hips have been '
             'compensating for can show up as ankle and knee pain, often worse running '
             'downhill.'),
        ],
        'POINTS': [
            ('One pair may not be enough',
             '<p>A running orthotic needs different materials and angles from an everyday one, '
             'because the forces are so much higher. Many runners wear the same pair for '
             'everything.</p>'),
            ('What to look for in a sports shoe',
             '<ul><li>Does not lean in when viewed from behind</li><li>Sturdy through the middle '
             'of the sole</li><li>Bends only at the toes</li><li>Firm heel counter</li><li>Laces '
             'up high to support the foot</li></ul>'),
            ('More than the foot',
             '<p>A plan can include strengthening the inner quadriceps (VMO), stretching the glutes '
             'and ITB, <a href="services/foot-mobilisation.html">foot mobilisation</a> and '
             '<a href="services/dry-needling.html">dry needling</a> of the muscles that have '
             'been compensating.</p>'),
        ],
    },
    'pigeon-toe': {
        'PAGES': 'Chapters 6, 8 and 13 (pp. 110, 191&ndash;192, 260&ndash;261)',
        'INTRO': 'Pigeon toe often comes from the shin bone being twisted inwards, called '
                 'internal tibial torsion. It is often inherited, passed down '
                 'from a parent.',
        'TYPES_TITLE': 'The measurements behind it',
        'TYPES': [
            ('Shin angle', '13&ndash;18&deg; from age 6', 'Measured at the ankle, a healthy shin '
             'turns slightly outwards. A negative angle means it turns in.'),
            ('Hip rotation', '45&deg; each way', 'Ideally the hip turns equally in and out. '
             'Tight outer hip muscles show the body is compensating.'),
            ('Heel position', '0&ndash;4&deg;', 'A twisted shin often makes the feet roll in as '
             'well.'),
        ],
        'POINTS': [
            ('"They’ll grow out of it"',
             '<p>The in-toeing you can see often lessens. But '
             'where it comes from the shin, the body usually hides it rather than '
             'correcting it: the hip muscles tighten to turn the leg back out. That is why it '
             'is worth assessing rather than waiting.</p>'),
            ('How it shows up later',
             '<p>With the shin turning in below the knee and the thigh turning out above it, '
             'the knee is caught in the middle. In adults this is linked to knee pain, '
             'especially running downhill.</p>'),
            ('What a plan can include',
             '<p>Monitoring as your child grows, stretches for the hip muscles that have '
             'tightened to compensate, orthotics where the feet roll in, and regular '
             're-measurement. See '
             '<a href="services/childrens-podiatry.html">children’s podiatry</a>.</p>'),
        ],
    },
    'out-toe': {
        'PAGES': 'Chapters 6, 13 and 15 (pp. 110, 257&ndash;259, 320)',
        'INTRO': 'Out-toeing often comes from the shin bone being twisted outwards, called '
                 'external tibial torsion. Like pigeon toe, it is often inherited.',
        'TYPES_TITLE': 'The measurements behind it',
        'TYPES': [
            ('Shin angle', '13&ndash;18&deg; from age 6', 'Some outward turn is healthy. Well '
             'beyond that range, the foot points out from the knee down.'),
            ('Hip rotation', '45&deg; each way', 'Tight groin and hip-flexor muscles show the '
             'body is compensating for an outward-turned shin.'),
            ('Heel position', '0&ndash;4&deg;', 'Checked alongside the shin, because the two '
             'affect each other.'),
        ],
        'POINTS': [
            ('Turnout from the hip, not the foot',
             '<p>In dancers, forcing turnout from the knee or '
             'foot, rather than the hip, can lead to knee, groin, lower back and stomach pain '
             'over time.</p>'),
            ('A link to Osgood-Schlatter',
             '<p>An outward-turned shin compensated by tight groin muscles twists the knee. That '
             'adds to the pull on the growing area below the kneecap in active teenagers.</p>'),
            ('What a plan can include',
             '<p>Stretches, in-toe gait-plate orthotics to guide an outward-turned shin, a slim '
             'orthotic for dance or sport shoes, and re-measuring every few months. See '
             '<a href="services/childrens-podiatry.html">children’s podiatry</a>.</p>'),
        ],
    },
}

SERVICES = {
    'biomechanics': {
        'PAGES': 'Chapter 7 (pp. 121&ndash;124)',
        'INTRO': 'The Najjarine Biomechanical Assessment (NBA&trade;) was developed by Dr Abbie '
                 'Najjarine to find the reason behind pain that has no injury behind it. It has '
                 'three parts.',
        'TYPES_TITLE': 'Assess, diagnose, treat',
        'TYPES': [
            ('NBA', 'Assessment', 'Seven measurements of how your legs and feet are built and how '
             'they move.'),
            ('NBD', 'Diagnosis', 'A biomechanical diagnosis: not just what hurts, but why it '
             'hurts.'),
            ('NBT', 'Treatment', 'A plan aimed at that cause, then at easing the symptoms.'),
        ],
        'POINTS': [
            ('The seven measurements',
             '<ol><li>Heel position standing relaxed</li><li>Heel position in neutral</li>'
             '<li>Shin twist, measured at the ankle</li><li>Hip rotation, leg straight</li>'
             '<li>Hip rotation, leg bent</li><li>Leg length difference</li><li>Forefoot '
             'position (six types)</li></ol>'),
            ('Fixing the crack, or the foundation?',
             '<p>Think of a cracked wall. Patching the crack does not help if a '
             'tree root is lifting the foundation. The NBA looks for the foundation.</p>'),
            ('What it can reveal',
             '<p>Which muscles have tightened or weakened to compensate, twists in the shin or '
             'thigh bone, a structural or functional leg length difference, and how the rear '
             'and front of the foot affect the rest of the body.</p>'),
        ],
    },
    'custom-orthotics': {
        'PAGES': 'Chapter 11 (pp. 229&ndash;235)',
        'INTRO': 'An orthotic is a device that changes the ground '
                 'to suit the individual needs of the person, child or adult.',
        'TYPES_TITLE': 'Three levels of orthotic',
        'TYPES': [
            ('Off the shelf', 'Minimal correction', 'A generic pre-made insole. It offers little '
             'correction, does not last long and does not correct the forefoot.'),
            ('Heat-moulded', 'Customised pre-made', 'Moulded with heat to your ideal foot '
             'position, in soft, medium or firm densities.'),
            ('Custom-made', 'Made from a cast', 'Made to a cast of your feet in the ideal '
             'position. Casts are taken standing, as they have been in our clinics since 1990.'),
        ],
        'POINTS': [
            ('Matched to your foot and weight',
             '<p>How firm the orthotic needs to be depends on how far your foot rolls in and on '
             'your body weight. The higher of the two decides.</p>'),
            ('Like glasses',
             '<p>You might have one pair of glasses for driving and another for reading. Running '
             'shoes, work shoes and flats may each need a different style of orthotic.</p>'),
            ('Two quick checks',
             '<p>The arch should not flatten like a pancake under thumb pressure, and the '
             'orthotic should sit stable on a flat surface. If it rocks, it needs '
             'balancing.</p>'),
            ('Orthotics are not the whole plan',
             '<p>Tight muscles work like a kink in a hose, blocking the correction. Plans often '
             'add <a href="services/dry-needling.html">dry needling</a>, massage, stretches, '
             '<a href="services/foot-mobilisation.html">mobilisation</a> or shockwave, sometimes '
             'for a few weeks before orthotics are made.</p>'),
        ],
    },
    'dry-needling': {
        'PAGES': 'Chapter 12 (p. 240)',
        'INTRO': 'Muscles, tendons and ligaments can develop tight, taut bands: trigger points, '
                 'scar tissue or adhesions. These limit how far and how smoothly a joint moves, '
                 'and cause pain.',
        'POINTS': [
            ('How it works',
             '<p>A fine acupuncture needle is placed in or around the taut band. It can cause a '
             'small twitch in the muscle.</p>'),
            ('The body’s own response',
             '<p>The body treats the needle as a foreign object, like a splinter or bee sting. '
             'It releases histamine and increases blood flow, bringing in the cells responsible '
             'for repair.</p>'),
            ('Calming the pain signal',
             '<p>The needle also stimulates sensory nerve fibres that help turn down the pain '
             'messages reaching the brain.</p>'),
            ('Where it is used',
             '<p>Most often the calves, the ITB and around the knees, usually alongside '
             '<a href="services/custom-orthotics.html">orthotics</a> so the tight muscle is not '
             'working against the correction.</p>'),
        ],
    },
    'foot-mobilisation': {
        'PAGES': 'Chapters 12 and 17 (pp. 239, 371&ndash;372)',
        'INTRO': 'The foot has 26 bones and two sesamoids. Joints can become stiff or partly '
                 'dislocated (subluxed), which limits how well the foot moves.',
        'POINTS': [
            ('A common example',
             '<p>Cuboid syndrome: a bone on the outer side of the foot partly dislocates, often '
             'after an ankle sprain or with a foot that rolls in too far.</p>'),
            ('What mobilisation aims to do',
             '<ul><li>Increase how far the joint moves</li><li>Reduce joint swelling</li>'
             '<li>Restore normal muscle tone</li><li>Stretch tight tissue and break down '
             'adhesions</li></ul>'),
            ('Foot, ankle, knee and hip',
             '<p>Mobilisation works through the foot, ankle, knee and hip joints. '
             'It is best used alongside <a href="services/custom-orthotics.html">orthotics</a> '
             'and exercises.</p>'),
            ('When it is not used',
             '<p>Past fractures or stress fractures, a history of blood clots (DVT), fresh '
             'sprains and inflammation, severe osteoporosis or infection. Your podiatrist checks '
             'these first.</p>'),
        ],
    },
    'neural-therapy': {
        'PAGES': 'Chapter 12 (pp. 241&ndash;242)',
        'INTRO': 'Our injection therapies include prolotherapy, short for proliferation therapy: '
                 'an injection that encourages the body to grow new tissue where it has become '
                 'weak.',
        'TYPES_TITLE': 'The order we follow',
        'TYPES': [
            ('1. Assess', 'Biomechanically', 'Find the reason the joint or tendon is under '
             'strain.'),
            ('2. Align and adjust', 'Orthotics and joints', 'Correct the foundation with '
             'orthotics and free up the joints.'),
            ('3. Inject', 'Last, not first', 'Only then inject, so the repaired tissue is not '
             'put straight back under the same strain.'),
        ],
        'POINTS': [
            ('How prolotherapy works',
             '<p>A dextrose (sugar-water) solution is injected where a ligament or tendon '
             'attaches to bone. It causes local inflammation, which increases blood supply and '
             'prompts the tissue to repair itself.</p>'),
            ('Where it is used',
             '<p>Ankles, knees and hips: joint wear, weakened ligaments and long-standing '
             'tendon problems.</p>'),
            ('How many treatments',
             '<p>It varies with how each person heals. Your practitioner will talk you through '
             'what to expect for your condition.</p>'),
        ],
    },
    'shockwave-therapy': {
        'PAGES': 'Chapter 12 (p. 243) and Chapter 15',
        'INTRO': 'Shockwave uses acoustic waves driven by compressed air to deliver kinetic energy '
                 'into the tissue, much like a small hand-held jackhammer.',
        'POINTS': [
            ('What it is aiming for',
             '<p>Like dry needling, it deliberately triggers the body’s own inflammatory '
             'repair response in tissue that has stopped healing on its own.</p>'),
            ('Soft and hard tissue',
             '<p>It works on both. It aims to reduce long-term inflammation, improve collagen, '
             'release trigger points and break down adhesions.</p>'),
            ('Where it is used',
             '<p>For both recent and long-standing problems, including '
             '<a href="conditions/plantar-fasciitis.html">plantar fasciitis</a>, heel spurs, '
             '<a href="conditions/achilles-pain.html">Achilles pain</a>, shin splints and knee '
             'pain.</p>'),
            ('Part of a plan',
             '<p>It is aimed at the area that hurts, alongside orthotics that address why that '
             'area was overloaded.</p>'),
        ],
    },
    'foot-strapping': {
        'PAGES': 'Chapter 12 (pp. 245&ndash;252)',
        'INTRO': 'Strapping stimulates the nerve endings in the skin that sense pressure and '
                 'position, improving how the body senses and controls the foot.',
        'TYPES_TITLE': 'Four strapping techniques',
        'TYPES': [
            ('Low Dye', 'Arch and heel', 'A figure-8 under the foot for plantar fasciitis, heel '
             'spurs and Sever’s disease.'),
            ('Heel lock', 'Ankle', 'Supports ankle stability.'),
            ('Knee anchor', 'Knee', 'For knee pain around the kneecap.'),
            ('Osgood-Schlatter', 'Teenage knee', 'For pain at the growth area below the '
             'kneecap.'),
        ],
        'POINTS': [
            ('Prevention or short-term treatment',
             '<p>Strapping can protect against injury or give short-term support while other '
             'treatment takes effect.</p>'),
            ('A test for your orthotic',
             '<p>How your foot responds to strapping helps show how much correction an orthotic '
             'will need.</p>'),
            ('Direction matters',
             '<p>For a foot that rolls in, the tape starts on the outer side to pull against it. '
             'For a foot that rolls out, it starts on the inner side.</p>'),
        ],
    },
    'sports-podiatry': {
        'PAGES': 'Chapter 13 (pp. 255&ndash;262)',
        'INTRO': 'Football, dance and running each load the feet differently. Across all '
                 'three, the aim is the same: find the cause of the pain and prevent the next '
                 'injury.',
        'TYPES_TITLE': 'By sport',
        'TYPES': [
            ('Football', 'Synthetic pitches', 'Harder, flatter turf returns more force to the '
             'body, but boots have not changed to match.'),
            ('Dance', 'Turnout', 'Turnout should come from the hip. Forcing it from the knee or '
             'foot causes knee, hip and back problems.'),
            ('Running', '4&ndash;5&times; body weight', 'The force through each foot on every '
             'stride, which magnifies small misalignments.'),
        ],
        'POINTS': [
            ('What to look for in a sports shoe',
             '<ul><li>Does not lean in when viewed from behind</li><li>Sturdy mid-sole</li><li>Bends '
             'only at the toes</li><li>Firm heel counter</li><li>Laces up high</li></ul>'),
            ('Young athletes',
             '<p>Sever’s disease (heel) and Osgood-Schlatter (knee) are common in active '
             'children, where growing bone is pulled on by tendons during repetitive '
             'training.</p>'),
            ('A pair for sport',
             '<p>Sport orthotics need different materials from everyday ones, and a slimmer style '
             'for boots or ballet shoes.</p>'),
        ],
    },
    'childrens-podiatry': {
        'PAGES': 'Chapters 6, 13 and 15 (pp. 110, 260&ndash;261, 320&ndash;326)',
        'INTRO': 'Children’s feet and legs are still forming. It is important to assess the '
                 'child’s biomechanics rather than putting pain down to growing pains.',
        'TYPES_TITLE': 'Common in growing children',
        'TYPES': [
            ('Sever’s disease', 'Heel, age 8&ndash;14', 'Soreness at the back of the heel, '
             'worse after running and when getting up. Linked to feet that roll in or out, not '
             'only to growth.'),
            ('Osgood-Schlatter', 'Knee, age 13&ndash;17', 'A tender lump below the kneecap where '
             'the tendon pulls on the growing shin bone.'),
            ('In- and out-toeing', 'Any age', 'Often a twist in the shin bone, inherited from a '
             'parent.'),
        ],
        'POINTS': [
            ('"Growing out of it"',
             '<p>Where in-toeing comes from a twisted shin, '
             'the body often hides it by tightening the hip muscles rather than correcting '
             'it. Measuring it is how you know.</p>'),
            ('Who Sever’s affects most',
             '<p>Active, fast-growing children, more often boys, whose feet roll in or out and '
             'put repeated stress on the heel growth plate.</p>'),
            ('What a plan can include',
             '<p>Orthotics, heel lifts, foot mobilisation, strapping and calf massage, reviewed '
             'as your child grows.</p>'),
        ],
    },
}


# slug -> (image slot, alt). Sources in build_images.py.
EDU_IMAGES = {
    'heel-pain': ('edu-heel-pain', 'A hand holding a painful heel'),
    'plantar-fasciitis': ('edu-plantar', 'Pain highlighted under the heel where the plantar fascia attaches'),
    'achilles-pain': ('edu-achilles', 'A thickened Achilles tendon at the back of the heel'),
    'shin-splints': ('edu-shin', 'Diagram of anterior shin splints along the front of the shin'),
    'forefoot-pain': ('edu-forefoot', 'Diagram of metatarsalgia, pain across the ball of the foot'),
    'knee-pain': ('edu-knee', 'Pain highlighted at the knee joint'),
    'flat-feet': ('edu-flat-feet', 'Heels rolling in before an orthotic and upright after it'),
    'running-injuries': ('edu-running', 'Pain highlighted along the lower leg'),
    'pigeon-toe': ('edu-pigeon', 'A young child walking on the sand'),
    'out-toe': ('edu-out-toe', 'A dancer on pointe, where turnout should come from the hip'),
    'biomechanics': ('edu-biomechanics', 'Diagram of short leg syndrome and the body corrected to level'),
    'custom-orthotics': ('edu-orthotics', 'Different styles of orthotic for different shoes'),
    'dry-needling': ('edu-needling', 'Fine needles placed in a muscle'),
    'foot-mobilisation': ('edu-mobilisation', 'A practitioner mobilising the joints of a foot'),
    'neural-therapy': ('edu-neural', 'Dr Abbie Najjarine assessing a patient before treatment'),
    'shockwave-therapy': ('edu-shockwave', 'A shockwave applicator held against the back of the heel'),
    'foot-strapping': ('edu-strapping', 'Strapping tape applied around the foot and ankle'),
    'sports-podiatry': ('edu-sports', 'A football player running with the ball'),
    'childrens-podiatry': ('edu-childrens', 'Diagram of Sever’s disease at the heel growth plate'),
}
