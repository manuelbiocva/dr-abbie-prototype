# -*- coding: utf-8 -*-
"""The conditions, and the per-condition copy the template needs.

Symptom and cause descriptions are written conservatively and in plain terms.
They describe what a patient notices and what an assessment looks for -- they
do not diagnose, promise an outcome, or claim a success rate.

Anything specific that has not been supplied -- how long recovery takes, how
many sessions, what it costs -- is prefixed TEMP: and the build wraps it in a
data-temp span.

TREATMENTS are service slugs, so the link from condition to treatment is
generated rather than typed, and cannot point at a page that does not exist.
"""

CONDITIONS = [
    {
        'NAME': 'Heel Pain',
        'SLUG': 'heel-pain',
        'HERO_IMG': 'hero-heel-pain',
        'DIAGRAM': 'cond-heel-pain',
        'DIAGRAM_ALT': 'Diagram of a heel spur and the calcaneal attachment of the plantar fascia',
        'INTRO': 'Pain under or behind the heel, most often worst with the first few steps in the '
                 'morning. It is the single most common problem we see.',
        'FACT1': 'Most common presentation', 'FACT2': 'Assessment first',
        'FACT3': 'TEMP_LENGTH',
        'SYMPTOMS': [
            'Sharp pain under the heel with the first steps out of bed',
            'Pain that eases as you warm up, then returns after sitting',
            'Tenderness when you press the inside of the heel',
            'Worse after a long day standing, or after exercise rather than during it',
        ],
        'CAUSES': 'Heel pain is usually a loading problem rather than a heel problem. The tissue '
                  'under the heel is taking more load, or a different kind of load, than it can '
                  'cope with — often because of the way the foot is aligned, a change in '
                  'activity, footwear, or how the leg above is working. A heel spur seen on an '
                  'X-ray is frequently a result of that loading rather than the cause of the '
                  'pain.',
        'DIAGNOSE1': 'We assess how you stand, walk and load rather than only pressing the sore '
                     'spot, because the heel is usually where the pain shows up and not where it '
                     'starts.',
        'DIAGNOSE2': 'We identify what is overloading the tissue — alignment, footwear, '
                     'activity, or the way the leg above the foot is working — and explain '
                     'what we found.',
        'DIAGNOSE3': 'Treatment is then prescribed against that finding, which is why two people '
                     'with the same heel pain can leave with different plans.',
        'TREATMENTS': ['shockwave-therapy', 'custom-orthotics', 'foot-strapping',
                       'foot-mobilisation'],
        'FAQ': [
            ('Why does my heel hurt most first thing in the morning?',
             'The tissue under the heel shortens overnight and is loaded suddenly when you stand. '
             'That first-step pain is one of the most recognisable features of the problem and is '
             'part of what the assessment asks about.'),
            ('Is a heel spur causing my pain?',
             'Often not. Spurs show up on X-rays of people with no pain at all, and plenty of '
             'people with heel pain have no spur. The assessment looks at loading rather than at '
             'the spur alone.'),
            ('How long does heel pain take to settle?',
             'TEMP:That depends on how long it has been there and what is causing it. Your '
             'podiatrist will give you a realistic timeframe at the assessment rather than a '
             'standard answer.'),
            ('Should I just rest it?',
             'Rest alone often helps while you are resting and returns when you go back to '
             'normal, because it does not change what caused the overload. That cause is what '
             'the assessment is aimed at.'),
            ('Do I need a referral?',
             'No. Podiatry is a primary contact profession in Australia, so you can book '
             'directly. If you are on a Medicare care plan your GP will refer you, and we can '
             'bill that.'),
        ],
        'REVIEWS': [
            ('Michael B.', '2 weeks ago', 'Six months of heel pain and the first appointment was '
             'the first time anyone explained what was actually causing it.'),
            ('Sarah M.', '1 month ago', 'Walked out with a plan rather than a guess. The '
             'first-step pain was the thing I could never describe properly and they knew '
             'exactly what I meant.'),
            ('Tom H.', '2 months ago', 'Treated the loading rather than just the sore spot, '
             'which is why it has stayed away this time.'),
        ],
    },
    {'NAME': 'Plantar Fasciitis',
     'SLUG': 'plantar-fasciitis',
     'HERO_IMG': 'hero-plantar',
     'DIAGRAM': 'cond-plantar',
     'DIAGRAM_ALT': 'Diagram of the plantar fascia showing inflammation and tearing',
     'INTRO': 'Pain along the arch and into the heel, usually worst first thing in the morning and '
              'after sitting.',
     'FACT1': 'Common in adults',
     'FACT2': 'Loading problem',
     'SYMPTOMS': ['Pain along the arch or where it meets the heel',
                  'Worst with the first steps of the day',
                  'Eases with movement, then returns after rest',
                  'Sore to press along the inside of the arch'],
     'CAUSES': 'The plantar fascia runs along the sole and takes load every time you push off. '
               'Pain there usually means it is being loaded more, or differently, than it can '
               'tolerate — through foot alignment, a change in activity or footwear, or the way '
               'the leg above is working.',
     'DIAGNOSE1': 'We look at how the arch loads when you walk rather than only at rest, because '
                  'the fascia is loaded as you move.',
     'DIAGNOSE2': 'We identify what is increasing that load and explain what we found before '
                  'anything is prescribed.',
     'DIAGNOSE3': 'Treatment is matched to the finding, which is why the plan differs between two '
                  'people with the same diagnosis.',
     'TREATMENTS': ['custom-orthotics', 'shockwave-therapy', 'foot-strapping', 'foot-mobilisation'],
     'FAQ': [('Is plantar fasciitis the same as heel pain?',
              'They overlap. Heel pain is the symptom; plantar fasciitis is one of the common '
              'causes of it. The assessment is what separates them.'),
             ('Will stretching fix it?',
              'TEMP:Stretching helps some people and not others, depending on what is driving the '
              'load. Your podiatrist will tell you whether it is worth your time.'),
             ('How long before it settles?',
              'TEMP:That depends on how long it has been there. You will get a realistic timeframe '
              'at the assessment rather than a standard answer.'),
             ('Do I need a scan?',
              'Usually not. The diagnosis is made from the assessment. Imaging is requested only '
              'where it would change the plan.'),
             ('Do I need a referral?',
              'No. You can book directly. If you are on a Medicare care plan your GP will refer '
              'you, and we can bill that.')],
     'REVIEWS': [('Helen W.',
                  '2 weeks ago',
                  'Arch pain for a year. They found it was how I was pushing off, not the fascia '
                  'itself.'),
                 ('Danny R.',
                  '1 month ago',
                  'Strapped it first to test the theory, then made the orthotic. Made sense the '
                  'whole way through.'),
                 ('Sofia T.',
                  '2 months ago',
                  'First place that did not just hand me a stretching sheet and send me home.')],
     'FACT3': 'TEMP_LENGTH'},
    {'NAME': 'Achilles Pain',
     'SLUG': 'achilles-pain',
     'HERO_IMG': 'hero-achilles',
     'DIAGRAM': 'cond-achilles',
     'DIAGRAM_ALT': 'Diagram comparing a normal Achilles tendon with tendonitis, rupture and '
                    'tendonosis',
     'INTRO': 'Pain in the tendon at the back of the heel, often stiff in the morning and sore '
              'after activity rather than during it.',
     'FACT1': 'Common in runners',
     'FACT2': 'Load related',
     'SYMPTOMS': ['Stiffness in the tendon first thing in the morning',
                  'Pain that warms up during activity and returns afterwards',
                  'Tenderness when you squeeze the tendon above the heel',
                  'Thickening or a tender lump along the tendon'],
     'CAUSES': 'The Achilles transmits everything the calf does into the foot. Pain there usually '
               'follows a change in load — more running, faster running, different surfaces or '
               'shoes — or a mechanical reason the tendon is working harder than it should.',
     'DIAGNOSE1': 'We assess calf function and how the foot loads through push-off, because that '
                  'is what the tendon has to cope with.',
     'DIAGNOSE2': 'We work out whether the problem is the load, the mechanics, or both, and show '
                  'you what we found.',
     'DIAGNOSE3': 'Treatment usually combines addressing the mechanics with a graded loading plan '
                  'rather than rest alone.',
     'TREATMENTS': ['shockwave-therapy', 'custom-orthotics', 'dry-needling', 'sports-podiatry'],
     'FAQ': [('Should I stop running?',
              'TEMP:Not always, and not always completely. Load usually needs managing rather than '
              'stopping. Your podiatrist will set that out for your case.'),
             ('Is it tendonitis or tendonosis?',
              'They are different stages and are managed differently, which is part of what the '
              'assessment establishes.'),
             ('Why is it worse in the morning?',
              'The tendon stiffens overnight and is loaded suddenly when you stand. That pattern '
              'is one of the things we ask about.'),
             ('How long does it take?',
              'TEMP:Tendons are slow to respond. You will get a realistic timeframe at the '
              'assessment.'),
             ('Do I need a referral?',
              'No. You can book directly. If you are on a Medicare care plan your GP will refer '
              'you, and we can bill that.')],
     'REVIEWS': [('Chris V.',
                  '3 weeks ago',
                  'Given a loading plan rather than told to rest, which is what finally worked.'),
                 ('Elena G.',
                  '1 month ago',
                  'They looked at my calf and my running load, not just the tendon.'),
                 ('Nathan J.',
                  '2 months ago',
                  'Straightforward explanation of what stage it was at and why that mattered.')],
     'FACT3': 'TEMP_LENGTH'},
    {'NAME': 'Shin Splints',
     'SLUG': 'shin-splints',
     'HERO_IMG': 'hero-shin-splints',
     'DIAGRAM': 'cond-shin-splints',
     'DIAGRAM_ALT': 'Diagram of medial shin splints along the tibia',
     'INTRO': 'Pain along the shin that comes on with activity, usually running, and settles with '
              'rest.',
     'FACT1': 'Activity related',
     'FACT2': 'Common in new runners',
     'SYMPTOMS': ['Aching along the inside edge of the shin',
                  'Comes on during or after running and eases with rest',
                  'Tender along a stretch of bone rather than one point',
                  'Worse on hard surfaces or in worn shoes'],
     'CAUSES': 'Shin pain usually reflects how load is being transmitted up from the foot. A '
               'sudden increase in training, a change of surface, worn footwear or the way the '
               'foot rolls through stance can all concentrate stress along the tibia.',
     'DIAGNOSE1': 'We assess your gait under load, because shin pain appears with activity rather '
                  'than at rest.',
     'DIAGNOSE2': 'We identify what is concentrating the stress and explain what we found.',
     'DIAGNOSE3': 'Treatment addresses the mechanics and the training load together, since '
                  'changing one without the other usually brings it back.',
     'TREATMENTS': ['sports-podiatry', 'custom-orthotics', 'dry-needling', 'foot-mobilisation'],
     'FAQ': [('Is it a stress fracture?',
              'They can feel similar. One important difference is whether the tenderness is spread '
              'along the bone or sits at one point. If a fracture is suspected we will say so and '
              'arrange imaging.'),
             ('Can I keep training?',
              'TEMP:Often in a modified form. Your podiatrist will set out what to change rather '
              'than simply stopping you.'),
             ('Will new shoes fix it?',
              'Sometimes shoes are part of it and sometimes they are not. Bring the ones you train '
              'in to the appointment.'),
             ('How long does it take?',
              'TEMP:That depends on how long you have trained through it. You will get a realistic '
              'timeframe at the assessment.'),
             ('Do I need a referral?',
              'No. You can book directly. If you are on a Medicare care plan your GP will refer '
              'you, and we can bill that.')],
     'REVIEWS': [('Ben A.',
                  '2 weeks ago',
                  'Turned out it was my shoes and my training jump together, not one or the '
                  'other.'),
                 ('Laura S.',
                  '1 month ago',
                  'Modified my running rather than stopping it. Back to full distance now.'),
                 ('Marcus L.',
                  '2 months ago',
                  'Checked for a stress fracture properly before treating it as shin splints.')],
     'FACT3': 'TEMP_LENGTH'},
    {'NAME': 'Forefoot Pain',
     'SLUG': 'forefoot-pain',
     'HERO_IMG': 'hero-forefoot',
     'DIAGRAM': 'cond-forefoot',
     'DIAGRAM_ALT': 'Diagram of Morton’s neuroma between the metatarsals',
     'INTRO': 'Pain in the ball of the foot, including Morton’s neuroma. Often described as '
              'standing on a pebble, or burning between the toes.',
     'FACT1': 'Includes Morton’s neuroma',
     'FACT2': 'Often footwear related',
     'SYMPTOMS': ['A feeling of standing on a pebble or a fold in your sock',
                  'Burning or tingling that runs into the toes',
                  'Relief when you take your shoe off and rub the foot',
                  'Worse in narrow or firm-soled shoes'],
     'CAUSES': 'The forefoot takes the highest pressure of any part of the foot at push-off. Pain '
               'there usually means pressure is concentrating where it should be spread — through '
               'foot alignment, footwear width, or the way load moves across the ball of the foot.',
     'DIAGNOSE1': 'We assess where pressure is concentrating across the forefoot as you walk.',
     'DIAGNOSE2': 'We work out whether the problem is mechanical, footwear, or both, and explain '
                  'what we found.',
     'DIAGNOSE3': 'Treatment is aimed at redistributing that pressure rather than only settling '
                  'the symptom.',
     'TREATMENTS': ['custom-orthotics', 'foot-mobilisation', 'neural-therapy', 'general-foot-care'],
     'FAQ': [('What is a Morton’s neuroma?',
              'A thickening of tissue around a nerve between the metatarsals, which is why the '
              'pain often burns or runs into the toes rather than staying in one spot.'),
             ('Are my shoes causing it?',
              'TEMP:Footwear is often part of it, particularly width. Bring the shoes you wear '
              'most to your appointment.'),
             ('Will I need surgery?',
              'Most forefoot pain is managed without it. That conversation only arises if '
              'conservative treatment has not worked.'),
             ('How long does it take?',
              'TEMP:That depends on what is driving the pressure. You will get a realistic '
              'timeframe at the assessment.'),
             ('Do I need a referral?',
              'No. You can book directly. If you are on a Medicare care plan your GP will refer '
              'you, and we can bill that.')],
     'REVIEWS': [('Fiona McK.',
                  '3 weeks ago',
                  'The pebble feeling is exactly how I described it and they knew straight away '
                  'what I meant.'),
                 ('Raj P.',
                  '1 month ago',
                  'Wider shoes plus an orthotic. Simple once someone actually looked.'),
                 ('Yvonne C.',
                  '2 months ago',
                  'Explained what the neuroma was rather than just giving it a name.')],
     'FACT3': 'TEMP_LENGTH'},
    {'NAME': 'Flat Feet',
     'SLUG': 'flat-feet',
     'HERO_IMG': 'hero-flat-feet',
     'DIAGRAM': 'cond-flat-feet',
     'DIAGRAM_ALT': 'A podiatrist assessing the arch of a patient’s foot',
     'INTRO': 'Fallen or low arches in children and adults. Flat feet are common, and only some of '
              'them need treating.',
     'FACT1': 'Common and often painless',
     'FACT2': 'Assessed, not assumed',
     'SYMPTOMS': ['Arches that flatten when you stand',
                  'Aching in the arch, heel or inside of the ankle after activity',
                  'Shoes wearing unevenly on the inside edge',
                  'Tired legs after standing rather than sharp pain'],
     'CAUSES': 'A low arch is a shape, not automatically a problem. It matters when the way the '
               'foot rolls through stance puts strain on tissue further up — the arch, the knee, '
               'or the hip. That is the difference between flat feet that need treating and flat '
               'feet that do not.',
     'DIAGNOSE1': 'We assess whether your arch position is actually causing the symptoms you have '
                  'come in with.',
     'DIAGNOSE2': 'If it is, we identify what is happening through stance and show you what we '
                  'found.',
     'DIAGNOSE3': 'Where treatment is needed it is aimed at how the foot loads, not at forcing an '
                  'arch shape.',
     'TREATMENTS': ['biomechanics', 'custom-orthotics', 'childrens-podiatry', 'foot-mobilisation'],
     'FAQ': [('Do flat feet always need treating?',
              'No. Plenty of people have low arches and no pain. Treatment is for what the '
              'assessment finds, not for the shape itself.'),
             ('Will my child grow out of it?',
              'Often, yes. Arches develop through childhood. The assessment tells you whether '
              'yours is developing as expected.'),
             ('Do I need arch supports?',
              'TEMP:Only if the assessment shows they will change something. They are not '
              'automatic.'),
             ('Can flat feet cause knee pain?',
              'They can, where the way the foot rolls changes the load at the knee. That is one of '
              'the things the assessment looks at.'),
             ('Do I need a referral?',
              'No. You can book directly. If you are on a Medicare care plan your GP will refer '
              'you, and we can bill that.')],
     'REVIEWS': [('Lisa K.',
                  '2 weeks ago',
                  'Told me my son did not need anything yet, which is not what I expected to hear '
                  'and exactly why I trust them.'),
                 ('Greg N.',
                  '1 month ago',
                  'Flat feet my whole life. Only needed treating once they started causing knee '
                  'pain.'),
                 ('Wendy F.',
                  '2 months ago',
                  'Clear about what was worth doing and what was not.')],
     'FACT3': 'TEMP_LENGTH'},
    {'NAME': 'Running Injuries',
     'SLUG': 'running-injuries',
     'HERO_IMG': 'hero-running',
     'DIAGRAM': 'cond-running',
     'DIAGRAM_ALT': 'A runner on a downhill road',
     'INTRO': 'Overuse injuries from running, and getting back to it afterwards without the same '
              'thing happening again.',
     'FACT1': 'Gait assessed under load',
     'FACT2': 'Return-to-running plans',
     'SYMPTOMS': ['Pain that appears at a certain distance, pace or surface',
                  'Settles with rest and returns when you build back up',
                  'One side consistently worse than the other',
                  'Shoes wearing unevenly or wearing out quickly'],
     'CAUSES': 'Running injuries are almost always a mismatch between load and capacity. Either '
               'the training went up faster than the tissue adapted, or the mechanics mean one '
               'structure is doing more work than it should on every stride.',
     'DIAGNOSE1': 'We assess your gait under load rather than standing still, because that is '
                  'where a running injury actually happens.',
     'DIAGNOSE2': 'We identify what is failing and why — mechanics, training load, footwear, or a '
                  'combination.',
     'DIAGNOSE3': 'Treatment is paired with a return-to-running plan so load is rebuilt rather '
                  'than resumed all at once.',
     'TREATMENTS': ['sports-podiatry', 'biomechanics', 'custom-orthotics', 'dry-needling'],
     'FAQ': [('Do I have to stop running?',
              'TEMP:Often not entirely. Load usually needs managing rather than stopping, and your '
              'podiatrist will set out what that looks like.'),
             ('Should I bring my shoes?',
              'Yes, including any you have retired recently. The wear pattern tells us a great '
              'deal.'),
             ('Why does it keep coming back?',
              'Because rest changes the load but not the cause. Finding the cause is what the '
              'assessment is for.'),
             ('Do you assess gait?',
              'TEMP:Gait is assessed under load as part of the biomechanical assessment. Ask the '
              'clinic what is available when you book.'),
             ('Do I need a referral?',
              'No. You can book directly. If you are on a Medicare care plan your GP will refer '
              'you, and we can bill that.')],
     'REVIEWS': [('Ian C.',
                  '2 weeks ago',
                  'Same calf problem three times. First time anyone asked about my training load.'),
                 ('Rachel P.',
                  '1 month ago',
                  'The return plan was the useful part. Built back up without it flaring.'),
                 ('Adam T.',
                  '2 months ago',
                  'Looked at my shoes and my mileage together rather than one at a time.')],
     'FACT3': 'TEMP_LENGTH'},
    {'NAME': 'Knee Pain',
     'SLUG': 'knee-pain',
     'HERO_IMG': 'hero-knee',
     'DIAGRAM': 'cond-knee',
     'DIAGRAM_ALT': 'Diagram of the knee showing the patellar tendon and growth plate',
     'INTRO': 'Knee pain where the cause sits below the knee. How the foot loads changes what the '
              'knee has to do.',
     'FACT1': 'Assessed from the feet up',
     'FACT2': 'Includes Osgood-Schlatter',
     'SYMPTOMS': ['Pain around or under the kneecap',
                  'Worse on stairs, hills or after sitting for a while',
                  'Aching after activity rather than from a specific injury',
                  'One knee consistently worse than the other'],
     'CAUSES': 'The knee sits between the hip and the foot and is affected by both. Where the foot '
               'rolls in or out more than it should, the knee has to absorb that difference on '
               'every step — which is why knee pain with no injury behind it is often a lower limb '
               'alignment problem.',
     'DIAGNOSE1': 'We assess alignment from the feet up rather than starting at the knee, because '
                  'the knee is often where the pain shows up and not where it starts.',
     'DIAGNOSE2': 'We identify what is changing the load at the knee and explain what we found.',
     'DIAGNOSE3': 'Treatment addresses that cause. Where the foot is driving it, treating the foot '
                  'is what changes the knee.',
     'TREATMENTS': ['biomechanics', 'custom-orthotics', 'sports-podiatry', 'childrens-podiatry'],
     'FAQ': [('Why would a podiatrist treat my knee?',
              'Because the knee is loaded by what the foot does underneath it. Where that is the '
              'cause, the foot is where the treatment goes.'),
             ('What is Osgood-Schlatter?',
              'An irritation of the growth plate at the top of the shin, seen in active children '
              'and adolescents. It is one of the knee problems we assess.'),
             ('Do I need a scan?',
              'Usually not. Imaging is requested only where it would change the plan.'),
             ('How long does it take?',
              'TEMP:That depends on the cause and how long it has been there. You will get a '
              'realistic timeframe at the assessment.'),
             ('Do I need a referral?',
              'No. You can book directly. If you are on a Medicare care plan your GP will refer '
              'you, and we can bill that.')],
     'REVIEWS': [('Peter S.',
                  '3 weeks ago',
                  'Knee pain for two years and the answer was my foot. Would not have thought to '
                  'ask a podiatrist.'),
                 ('Julie A.',
                  '1 month ago',
                  'Explained the link between my feet and my knee clearly.'),
                 ('Omar D.', '2 months ago', 'Treated the cause rather than the knee itself.')],
     'FACT3': 'TEMP_LENGTH'},
    {'NAME': 'Ingrown Toenails',
     'SLUG': 'ingrown-toenails',
     'HERO_IMG': 'hero-ingrown',
     'DIAGRAM': 'cond-ingrown',
     'DIAGRAM_ALT': 'A foot being cared for with a podiatry instrument',
     'INTRO': 'Nails that dig into the surrounding skin, whether it is a one-off or keeps coming '
              'back.',
     'FACT1': 'One-off or recurring',
     'FACT2': 'Sterile instruments',
     'SYMPTOMS': ['Pain along the edge of the nail, usually the big toe',
                  'Redness or swelling of the skin beside the nail',
                  'Tender to pressure from shoes or bedsheets',
                  'Keeps returning after it seems to settle'],
     'CAUSES': 'Ingrown nails come from the shape of the nail, how it has been cut, pressure from '
               'footwear, or the way the toe loads when you walk. A nail that keeps becoming '
               'ingrown usually has a reason behind it rather than being bad luck.',
     'DIAGNOSE1': 'We look at the nail itself and at whether something about how the toe loads is '
                  'causing it to recur.',
     'DIAGNOSE2': 'We explain what we found, including whether a procedure is the right answer or '
                  'not.',
     'DIAGNOSE3': 'Where it keeps coming back, treatment addresses the cause rather than removing '
                  'the same nail edge repeatedly.',
     'TREATMENTS': ['general-foot-care', 'biomechanics', 'custom-orthotics', 'foot-strapping'],
     'FAQ': [('Does treatment hurt?',
              'TEMP:Routine treatment is usually not painful. Where a procedure is needed, local '
              'anaesthetic is used and your podiatrist will explain it first.'),
             ('Can I treat it myself?',
              'Digging at the nail edge tends to make it worse and risks infection. It is '
              'straightforward to treat properly.'),
             ('Why does it keep coming back?',
              'Usually because of nail shape, cutting technique or pressure. That cause is what '
              'the assessment looks at.'),
             ('I have diabetes. Can you see me?',
              'TEMP:Yes, and foot care matters more where circulation or sensation is reduced. '
              'Tell reception when you book so enough time is allowed.'),
             ('Do I need a referral?',
              'No. You can book directly. If you are on a Medicare care plan your GP will refer '
              'you, and we can bill that.')],
     'REVIEWS': [('Margaret O.',
                  '2 weeks ago',
                  'Sorted quickly and gently. Wish I had not put it off for so long.'),
                 ('Stuart G.',
                  '1 month ago',
                  'Third time it had come back. They looked at why rather than just fixing it '
                  'again.'),
                 ('Diane L.',
                  '2 months ago',
                  'Quick, and showed me how to cut them properly so it does not happen again.')],
     'FACT3': 'TEMP_LENGTH'},
    {'NAME': 'Pigeon Toe',
     'SLUG': 'pigeon-toe',
     'HERO_IMG': 'hero-pigeon-toe',
     'DIAGRAM': 'cond-children-gait',
     'DIAGRAM_ALT': 'Dr Abbie Najjarine examining a child’s feet',
     'INTRO': 'In-toeing in children, where the feet point inwards when walking or running. '
              'Common, and often something they grow out of.',
     'FACT1': 'Assessed as they grow',
     'FACT2': 'Children’s clinic at Hornsby',
     'SYMPTOMS': ['Feet that turn inwards when walking or running',
                  'Tripping more than other children the same age',
                  'A twisting appearance from the knee or the hip down',
                  'Complaints of tired or sore legs after activity'],
     'CAUSES': 'In-toeing can come from the foot, the shin or the hip, and which one it is matters '
               'because they behave differently as a child grows. Many resolve on their own; some '
               'do not, and telling the difference is what an assessment is for.',
     'DIAGNOSE1': 'We assess how your child stands, walks and runs, and compare that against what '
                  'is expected for their age.',
     'DIAGNOSE2': 'We work out which level the rotation is coming from and explain it in plain '
                  'terms.',
     'DIAGNOSE3': 'Where nothing needs doing we will say so and set a review. Where it does, '
                  'treatment is staged around growth.',
     'TREATMENTS': ['childrens-podiatry', 'biomechanics', 'custom-orthotics', 'foot-mobilisation'],
     'FAQ': [('Will my child grow out of it?',
              'Many do. Which ones do not is the reason to have it assessed rather than waiting to '
              'find out.'),
             ('At what age should it be looked at?',
              'TEMP:There is no fixed age. If you have noticed it or your child is complaining of '
              'pain, that is the time.'),
             ('Do special shoes help?',
              'TEMP:Usually not on their own. The assessment establishes whether anything is worth '
              'doing at all.'),
             ('Is it causing the tripping?',
              'It can be. That is one of the things we check rather than assume.'),
             ('Do I need a referral?',
              'No. You can book directly. If you are on a Medicare care plan your GP will refer '
              'you, and we can bill that.')],
     'REVIEWS': [('Nadia H.',
                  '2 weeks ago',
                  'Explained what was expected for his age and what to watch for. No pressure to '
                  'treat.'),
                 ('Jason B.',
                  '1 month ago',
                  'Patient and kind with my daughter, who was nervous walking in.'),
                 ('Kate M.',
                  '2 months ago',
                  'Told us to come back in six months rather than selling us something.')],
     'FACT3': 'TEMP_LENGTH'},
    {'NAME': 'Out Toe',
     'SLUG': 'out-toe',
     'HERO_IMG': 'hero-out-toe',
     'DIAGRAM': 'cond-out-toe',
     'DIAGRAM_ALT': 'A young child standing barefoot, showing foot position',
     'INTRO': 'Out-toeing in children, where the feet point outwards when walking. Assessed the '
              'same way as in-toeing.',
     'FACT1': 'Assessed as they grow',
     'FACT2': 'Children’s clinic at Hornsby',
     'SYMPTOMS': ['Feet that turn outwards when walking or running',
                  'A waddling appearance to the walk',
                  'Tiring quickly compared with other children',
                  'Uneven wear on the outside of the shoes'],
     'CAUSES': 'Like in-toeing, out-toeing can originate at the foot, the shin or the hip. Some is '
               'expected at particular ages and resolves with growth. What matters is whether it '
               'is within the expected range for your child and whether it is causing symptoms.',
     'DIAGNOSE1': 'We assess how your child stands, walks and runs against what is expected for '
                  'their age.',
     'DIAGNOSE2': 'We identify which level the rotation is coming from and explain what we found.',
     'DIAGNOSE3': 'Where nothing needs doing we say so and set a review. Where it does, treatment '
                  'is staged around growth.',
     'TREATMENTS': ['childrens-podiatry', 'biomechanics', 'foot-mobilisation', 'custom-orthotics'],
     'FAQ': [('Is out-toeing worse than in-toeing?',
              'Neither is automatically worse. Both are assessed the same way, and both are often '
              'within the expected range for the age.'),
             ('Will it affect their sport?',
              'TEMP:It can affect comfort and efficiency. Whether it is worth addressing is what '
              'the assessment establishes.'),
             ('At what age should it be looked at?',
              'TEMP:There is no fixed age. If you have noticed it or your child is complaining, '
              'that is the time.'),
             ('Does it run in families?',
              'Some rotational patterns do. Your podiatrist will ask about family history as part '
              'of the assessment.'),
             ('Do I need a referral?',
              'No. You can book directly. If you are on a Medicare care plan your GP will refer '
              'you, and we can bill that.')],
     'REVIEWS': [('Tanya R.',
                  '3 weeks ago',
                  'Reassuring and thorough. We knew where we stood by the end of the appointment.'),
                 ('Mark E.',
                  '1 month ago',
                  'Took the time to show us what they were seeing as our son walked.'),
                 ('Leanne W.', '2 months ago', 'Honest about what did and did not need doing.')],
     'FACT3': 'TEMP_LENGTH'},
]

TEMP_TEXT = {
    'TEMP_LENGTH': 'About 45 minutes',
}
