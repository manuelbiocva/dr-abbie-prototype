# -*- coding: utf-8 -*-
"""The five launch posts (PROJECT-PLAN.md, /blog/).

Written as general patient information in the same register as the condition
pages. They explain what is commonly going on, what an assessment looks for and
when to get help. They do not diagnose, promise an outcome, quote a success
rate, or cite a statistic nobody has supplied.

Things that are not known yet stay visibly temporary (data-temp):
  - DATE: the posts publish at launch, so the dates are stand-ins. No date is
    written into the Article schema for the same reason; WordPress supplies
    datePublished when the post is actually published.
  - the byline. The plan calls for a practitioner byline, but which
    practitioner wrote or reviewed each post is the client's call. Attributing
    medical advice to a named clinician who did not write it is not something
    to guess, so the byline reads as the clinical team until that is supplied.
  - any number (session counts, turnaround, recovery time), wrapped in
    <span data-temp> inside BODY.

BODY is authored HTML. Every <h2> carries an id; the table of contents is built
from those, so a heading added here appears in the contents on the next build.
Links are written root-relative (conditions/heel-pain.html) and the build lifts
them for the /blog/ subfolder.

RELATED is ('condition', name) or ('service', slug), four per post. They are
chosen so no card repeats a photograph already on the page -- the build checks
this and refuses to write the page if one does.
"""

AUTHOR = 'Dr. Abbie Clinics clinical team'

POSTS = [
    {
        'SLUG': 'sharp-heel-pain-when-waking-up',
        'TITLE': 'Sharp Heel Pain When Waking Up in the Morning: Causes and Treatment',
        'META_TITLE': 'Sharp Heel Pain in the Morning: Causes and Treatment',
        'CATEGORY': 'Heel pain',
        'DATE': '2 September 2026',
        'EXCERPT': 'Why the first steps out of bed hurt the most, what usually causes it, and '
                   'when heel pain is worth having assessed rather than waiting out.',
        'CARD_IMG': 'blog-heel-pain',
        'HERO_IMG': 'post-heel-pain',
        'CARD_ALT': 'Hands supporting the heel and sole of a patient’s foot',
        'ABOUT': ['Heel Pain', 'Plantar Fasciitis'],
        'SUMMARY': [
            'First-step pain happens because the tissue under the heel tightens overnight and '
            'is loaded suddenly when you stand.',
            'Plantar fasciitis is a common cause, but not the only one, and a heel spur is '
            'often not the source of the pain.',
            'Rest alone tends to help only while you are resting. Finding what is overloading '
            'the heel is what changes it.',
            'Heel pain after an injury, with swelling, heat or numbness, should be seen '
            'promptly rather than waited out.',
        ],
        'RELATED': [('condition', 'Heel Pain'), ('condition', 'Plantar Fasciitis'),
                    ('service', 'shockwave-therapy'), ('service', 'custom-orthotics')],
        'BODY': """
<p>If the first few steps out of bed feel like standing on a bruise, or a sharp point under the heel, you are describing one of the most common problems a podiatrist sees. It often eases as you move around, which makes it easy to ignore, and then returns after sitting down or at the end of a long day.</p>

<h2 id="why-mornings">Why the first steps hurt the most</h2>
<p>The tissue under your foot does not carry load while you sleep, so it shortens and stiffens overnight. When you stand, it is stretched and loaded all at once. If that tissue is already irritated, those first steps are where you feel it most.</p>
<p>As you keep walking the tissue warms up and the pain often settles, which is why so many people describe it as “fine once I get going.” That pattern is useful: it points towards a loading problem rather than a sudden injury.</p>

<h2 id="causes">What usually causes it</h2>
<p><a href="conditions/plantar-fasciitis.html">Plantar fasciitis</a> is the cause most people have heard of. The plantar fascia is a thick band of tissue running along the sole from the heel to the toes, and it takes load every time you push off. When it is loaded more, or differently, than it can tolerate, the attachment at the heel becomes painful.</p>
<p>It is not the only cause of <a href="conditions/heel-pain.html">heel pain</a>, though. Pain at the back of the heel rather than underneath it often involves the Achilles tendon. Irritated nerves can produce burning or tingling. In active children, heel pain is commonly linked to the growth plate at the back of the heel. Each of these is managed differently, which is why the location and pattern of the pain matter.</p>
<p>Behind most of them sits the same question: why is the heel taking more load than it can cope with? Common contributors include:</p>
<ul>
  <li>the way the foot is aligned and rolls as you walk</li>
  <li>a change in activity, such as more walking, running or standing at work</li>
  <li>footwear that is worn, flat or unsupportive, or a lot of time barefoot on hard floors</li>
  <li>tightness or weakness further up the leg changing how the foot is loaded</li>
</ul>

<h2 id="heel-spurs">Is a heel spur causing the pain?</h2>
<p>Often not. A heel spur is a small bony growth that can show up on an X-ray, and it is easy to assume that is what hurts. But spurs appear in plenty of people who have no pain at all, and many people with heel pain have no spur. A spur is frequently a result of long-term loading at the heel rather than the source of the pain, so treatment is aimed at the loading, not the spur.</p>

<h2 id="meantime">What you can do in the meantime</h2>
<p>While you are waiting for an appointment, a few general measures are reasonable for most people:</p>
<ul>
  <li>avoid walking barefoot on hard floors, especially first thing in the morning</li>
  <li>wear supportive shoes rather than flat, worn-out or very soft ones</li>
  <li>notice what makes it worse, such as a particular activity, shoe or surface, and bring that to your appointment</li>
  <li>ease back on the activity that flares it rather than pushing through sharp pain</li>
</ul>
<p>These can take the edge off. What they do not do is change the reason the heel is overloaded, which is why pain that settles with rest so often comes back when normal activity resumes.</p>

<h2 id="assessment">How we assess and treat it</h2>
<p>Pressing on the sore spot confirms where it hurts. It does not tell you why. At Dr. Abbie Clinics, heel pain is assessed with the <a href="services/biomechanics.html">Najjarine Biomechanical Assessment</a>, which looks at how you stand, walk and load from the feet up, so treatment is prescribed against a finding rather than a symptom.</p>
<p>Depending on what the assessment shows, a plan may include <a href="services/custom-orthotics.html">custom orthotics</a> to change how load passes through the foot, <a href="services/foot-strapping.html">strapping</a> to offload the tissue in the short term, <a href="services/foot-mobilisation.html">foot mobilisation</a>, footwear changes, or <a href="services/shockwave-therapy.html">shockwave therapy</a> for pain that has persisted. Most plans combine more than one, and two people with the same heel pain can leave with different plans.</p>

<h2 id="when-to-book">When to book an assessment</h2>
<p>It is worth having heel pain looked at if it has not settled within a few weeks, if it keeps coming back, or if it is changing the way you walk. Pain that has been there for months is not something you simply have to live with.</p>
<aside class="post-note">
  <h3>Get it seen promptly if</h3>
  <ul>
    <li>the pain started after a fall or injury and you cannot put weight on the foot</li>
    <li>the heel is swollen, red or hot, or you feel unwell</li>
    <li>you have numbness or tingling in the foot</li>
    <li>you have diabetes or reduced circulation and notice any change in the foot</li>
  </ul>
  <p>In these situations, see your GP or seek urgent care rather than waiting for a routine appointment.</p>
</aside>
""",
    },

    {
        'SLUG': 'custom-orthotics-flat-feet-nba-assessment',
        'TITLE': 'Custom Orthotics for Flat Feet: How the NBA Assessment Shapes the Prescription',
        'META_TITLE': 'Custom Orthotics for Flat Feet and the NBA Assessment',
        'CATEGORY': 'Orthotics',
        'DATE': '19 August 2026',
        'EXCERPT': 'Not every flat foot needs an orthotic. How the assessment decides whether '
                   'yours does, and what a custom device is actually designed to change.',
        'CARD_IMG': 'blog-orthotics',
        'HERO_IMG': 'post-orthotics',
        'CARD_ALT': 'A podiatrist holding a custom orthotic against a patient’s foot',
        'ABOUT': ['Flat Feet'],
        'SUMMARY': [
            'A low arch is a shape, not automatically a problem. Many people with flat feet '
            'have no pain.',
            'Flat feet matter when the way the foot rolls puts strain on tissue in the arch, '
            'heel, knee or hip.',
            'A custom orthotic is made to a prescription from your assessment, not picked '
            'off a shelf.',
            'Orthotics are one option among several and are only prescribed when the '
            'assessment shows they will change something.',
        ],
        'RELATED': [('service', 'custom-orthotics'), ('service', 'biomechanics'),
                    ('condition', 'Knee Pain'), ('condition', 'Heel Pain')],
        'BODY': """
<p>“You have flat feet, you need orthotics” is advice a lot of people have been given. Sometimes it is right. Often it skips the most important step, which is working out whether the shape of your foot is actually causing the problem you came in with.</p>

<h2 id="flat-feet">Flat feet are not automatically a problem</h2>
<p><a href="conditions/flat-feet.html">Flat feet</a> simply means the arch sits low, or flattens noticeably when you stand. It is common in both children and adults, and plenty of people with low arches never have any pain from them.</p>
<p>A low arch becomes relevant when the way the foot rolls through each step places strain somewhere that cannot tolerate it. That strain can show up in the arch or heel, but it can also appear further up, at the shin, the <a href="conditions/knee-pain.html">knee</a> or the hip, because each step’s load travels up the leg.</p>

<h2 id="what-we-assess">What the assessment looks at</h2>
<p>The <a href="services/biomechanics.html">Najjarine Biomechanical Assessment</a> was developed at Dr. Abbie Clinics and draws on engineering principles. For a flat foot, the questions it sets out to answer are practical ones:</p>
<ul>
  <li>How does your foot and leg line up when you stand, and how does that change when you walk?</li>
  <li>Where is the load going with each step, and which structure is being strained by it?</li>
  <li>Does that strain match the pain you have come in with?</li>
  <li>What are your shoes doing, and what does their wear pattern show?</li>
</ul>
<p>The foot is assessed moving and under load, not only lying on a treatment table, because that is when the arch is doing its work. The findings are explained to you before anything is prescribed.</p>

<h2 id="custom-vs-off-the-shelf">What a custom orthotic is, and is not</h2>
<p>An off-the-shelf insole is a generic shape designed to suit as many feet as possible. A <a href="services/custom-orthotics.html">custom orthotic</a> is made to a prescription written from your own assessment, to change a specific problem that assessment identified.</p>
<p>The aim is not to force the foot into an idealised arch shape. It is to change the way load passes through the foot and up the leg, so the structure that has been overloaded is no longer taking the strain. That is why the prescription for two people with similar-looking flat feet can be quite different.</p>
<p>Our orthotics are manufactured on site at our Kirrawee head office rather than sent to an external laboratory.</p>

<h2 id="what-to-expect">What to expect if orthotics are prescribed</h2>
<ol>
  <li><strong>Assessment and prescription.</strong> The device is designed around what the assessment found, and around the shoes you actually wear. Bring them.</li>
  <li><strong>Manufacture.</strong> The orthotic is made to that prescription. <span data-temp>This usually takes around 7 to 10 days.</span></li>
  <li><strong>Fitting.</strong> The device is fitted to your shoes and checked while you stand and walk.</li>
  <li><strong>Settling in.</strong> <span data-temp>There is usually a break-in period.</span> Your podiatrist will tell you how to introduce them.</li>
  <li><strong>Review.</strong> The fit and your symptoms are checked, and the device is adjusted if needed.</li>
</ol>

<h2 id="not-always-orthotics">When orthotics are not the answer</h2>
<p>Orthotics are one of several treatments, not a default. If the assessment shows your flat feet are not the cause of your pain, there is nothing for an orthotic to fix. If they are part of the picture, other approaches may be used alongside or instead, including <a href="services/foot-mobilisation.html">mobilisation</a>, footwear changes or a strengthening programme.</p>
<p><a href="services/foot-strapping.html">Strapping</a> is sometimes used first. If taping the foot a certain way relieves the pain, that tells us something useful about what an orthotic would need to do. For children, whose arches are still developing, the answer is often monitoring rather than a device.</p>

<h2 id="questions-to-ask">Questions worth asking at your appointment</h2>
<ul>
  <li>Is my foot shape actually connected to my pain?</li>
  <li>What would an orthotic change, specifically?</li>
  <li>What else could we try, and why is this the better option for me?</li>
  <li>Will it fit the shoes I wear most?</li>
  <li>How will we know whether it is working?</li>
</ul>
<p>A good answer to each should be possible after the assessment. If it is not, the prescription is a guess.</p>
""",
    },

    {
        'SLUG': 'growing-pains-pigeon-toe-flat-feet-children',
        'TITLE': 'Growing Pains, Pigeon Toe and Flat Feet: When to Get Your Child Assessed',
        'META_TITLE': 'Growing Pains, Pigeon Toe and Flat Feet in Children',
        'CATEGORY': 'Children',
        'DATE': '5 August 2026',
        'EXCERPT': 'Many things that look worrying in a child’s feet settle on their own. The '
                   'signs that mean it is worth having them assessed, and what to check in a '
                   'school shoe.',
        'CARD_IMG': 'blog-children',
        'HERO_IMG': 'post-children',
        'CARD_ALT': 'School children in uniform sitting on a brick wall',
        'ABOUT': ['Pigeon Toe', 'Out Toe', 'Flat Feet'],
        'SUMMARY': [
            'Children’s feet and legs are still developing, and many differences in the way '
            'they walk settle with growth.',
            'In-toeing, out-toeing and flexible flat feet are common in young children and '
            'often need monitoring rather than treatment.',
            'Pain that limits activity, a limp, one side behaving differently, or things '
            'getting worse rather than better are reasons to book.',
            'A good school shoe bends at the toes, is firm along its length, and has a '
            'straight, supportive heel.',
        ],
        'RELATED': [('service', 'childrens-podiatry'), ('condition', 'Out Toe'),
                    ('condition', 'Flat Feet'), ('condition', 'Knee Pain')],
        'BODY': """
<p>Parents notice things. A child whose feet turn in when they run, who trips more than their friends, or who complains that their legs ache at night. Some of these settle on their own as a child grows. Some do not. The difficulty is telling which is which, and that is what an assessment is for.</p>

<h2 id="still-developing">Children’s feet are still developing</h2>
<p>A child’s foot is not a small adult foot. The bones, the arch and the rotation of the legs all change through childhood, and what is typical at three can look quite different from what is typical at eight. That is why the same observation can be entirely expected in one child and worth addressing in another.</p>

<h2 id="pigeon-toe">Pigeon toe (in-toeing)</h2>
<p><a href="conditions/pigeon-toe.html">Pigeon toe</a> describes feet that point inwards when a child walks or runs. The rotation can come from the foot, the shin or the hip, and which one matters, because they behave differently as a child grows. Many children grow out of it.</p>
<p>It is worth having it assessed if it is getting more noticeable rather than less, if it is much more obvious on one side, if your child is tripping frequently, or if they are complaining of pain or tiring quickly.</p>

<h2 id="out-toe">Out-toeing</h2>
<p><a href="conditions/out-toe.html">Out-toeing</a> is the reverse: feet that turn outwards, sometimes with a waddling look to the walk. Like in-toeing, some out-toeing is expected at particular ages and resolves with growth, and it is assessed in the same way.</p>

<h2 id="flat-feet">Flat feet in children</h2>
<p>Young children often look flat-footed, and arches typically develop through childhood. A foot that looks flat when standing but shows an arch when the child stands on tiptoe is often described as flexible, and in many children needs nothing more than monitoring.</p>
<p><a href="conditions/flat-feet.html">Flat feet</a> are worth assessing when they come with pain, when the foot seems stiff, when one foot is noticeably different from the other, or when a child is avoiding activity because their feet or legs hurt.</p>

<h2 id="growing-pains">Growing pains</h2>
<p>Many children go through periods of aching legs, usually in the evening or at night, often after an active day, and typically in both legs rather than one spot. These episodes are common and usually settle.</p>
<p>Leg pain in an active child can also come from how the feet and legs are loading during sport, including pain around the heel or just below the kneecap, where growth plates can become irritated. That kind of pain tends to relate to activity and sit in a particular place, and it is worth having looked at.</p>

<h2 id="when-to-book">Signs it is time to book</h2>
<ul>
  <li>pain that stops your child doing things they enjoy, or that they are avoiding sport because of it</li>
  <li>a limp, or one leg or foot behaving differently from the other</li>
  <li>tripping or falling noticeably more than other children their age</li>
  <li>pain that sits in one specific spot, or happens during the day as well as at night</li>
  <li>something that is getting worse over months rather than better</li>
  <li>shoes that wear out very unevenly or quickly</li>
</ul>
<aside class="post-note">
  <h3>See your GP promptly if</h3>
  <ul>
    <li>there is swelling, redness or warmth around a joint, or your child has a fever</li>
    <li>they have a limp that has not settled within a few days, or will not put weight on a leg</li>
    <li>pain repeatedly wakes them from sleep in the same place</li>
    <li>the pain followed a fall or injury</li>
  </ul>
</aside>

<h2 id="the-appointment">What happens at the appointment</h2>
<p>A <a href="services/childrens-podiatry.html">children’s podiatry</a> assessment looks at how your child stands, walks and runs, and compares that against what is expected for their age. We explain what we found in plain terms, including when the answer is that nothing needs doing yet. Where something does, treatment is staged around growth and reviewed as they develop.</p>
<p>Our Hornsby clinic sees children only, and children are also seen at our other clinics. Bring the shoes your child wears most, including school shoes.</p>

<h2 id="school-shoes">What to check in a school shoe</h2>
<p>Children spend a large part of the week in their school shoes, so they are worth choosing carefully. Three quick checks you can do in the shop:</p>
<div class="post-figures">
  <figure>
    <img src="assets/img/guide-shoe-toe-box.webp" width="528" height="264" alt="Illustration: a shoe should bend only at the toe box, should not have cut-outs in the arch area, and should not collapse in the arch" loading="lazy" decoding="async">
    <figcaption><strong>Bend.</strong> The shoe should bend at the toes only, not through the middle.</figcaption>
  </figure>
  <figure>
    <img src="assets/img/guide-shoe-length.webp" width="539" height="220" alt="Illustration: the length of a shoe should be firm, the heel should not collapse, and the shoe should not twist from side to side" loading="lazy" decoding="async">
    <figcaption><strong>Twist.</strong> It should be firm along its length and not twist from side to side.</figcaption>
  </figure>
  <figure>
    <img src="assets/img/guide-shoe-heel.webp" width="439" height="347" alt="Illustration: the heel seam should be straight and centred, and the heel counter firm enough not to collapse under mild thumb pressure" loading="lazy" decoding="async">
    <figcaption><strong>Heel.</strong> A straight, centred heel seam, and a heel counter that does not collapse under thumb pressure.</figcaption>
  </figure>
</div>
""",
    },

    {
        'SLUG': 'shockwave-therapy-heel-achilles-pain',
        'TITLE': 'Shockwave Therapy for Heel and Achilles Pain: What to Expect',
        'META_TITLE': 'Shockwave Therapy for Heel and Achilles Pain: What to Expect',
        'CATEGORY': 'Shockwave',
        'DATE': '22 July 2026',
        'EXCERPT': 'What shockwave therapy is, who it is usually considered for, and what '
                   'happens before, during and after a session.',
        'CARD_IMG': 'blog-shockwave',
        'HERO_IMG': 'post-shockwave',
        'CARD_ALT': 'A practitioner holding a handheld applicator against a patient’s heel',
        'ABOUT': ['Heel Pain', 'Achilles Pain'],
        'SUMMARY': [
            'Shockwave delivers pulses of acoustic energy to tissue that has stopped settling '
            'on its own.',
            'It is usually considered for heel or Achilles pain that has persisted despite '
            'rest, footwear changes and load management.',
            'A session takes a few minutes, needs no anaesthetic, and most people describe it '
            'as uncomfortable rather than painful.',
            'It is rarely used alone. The assessment decides whether it suits you and what '
            'needs to be addressed alongside it.',
        ],
        'RELATED': [('condition', 'Heel Pain'), ('condition', 'Achilles Pain'),
                    ('service', 'custom-orthotics'), ('service', 'biomechanics')],
        'BODY': """
<p>If your heel or Achilles pain has hung around for months despite rest, new shoes and doing everything you were told, shockwave therapy may have come up as an option. Here is what it involves, so you know what to expect before you decide.</p>

<h2 id="what-it-is">What shockwave therapy is</h2>
<p><a href="services/shockwave-therapy.html">Shockwave therapy</a> delivers pulses of acoustic energy through the skin to the tissue underneath, using a handheld applicator. The intention is to provoke the body’s own repair response in tissue that has stopped settling on its own, such as a long-standing irritation where the plantar fascia attaches to the heel, or in the Achilles tendon.</p>
<p>Despite the name, it has nothing to do with electric shocks. The “shockwave” is a pressure wave, and what you feel is a rapid tapping.</p>

<h2 id="who-its-for">Who it is usually considered for</h2>
<p>Shockwave is most often considered for pain that has persisted despite the usual first steps: relative rest, footwear changes and managing load. At Dr. Abbie Clinics we use it most often for persistent <a href="conditions/heel-pain.html">heel pain</a>, including <a href="conditions/plantar-fasciitis.html">plantar fasciitis</a>, and <a href="conditions/achilles-pain.html">Achilles pain</a>.</p>
<p>It is not a first resort, and it is not suitable for everyone. Before recommending it, your podiatrist will ask about your medical history, any medications you take, and whether you are or could be pregnant.</p>

<h2 id="before">Before: the assessment comes first</h2>
<p>Shockwave treats the painful tissue. It does not change why that tissue was overloaded in the first place. So before shockwave is considered, a full <a href="services/biomechanics.html">biomechanical assessment</a> establishes what is loading the heel or tendon and why. That finding decides whether shockwave is appropriate, and what else the plan needs.</p>

<h2 id="during">During a session</h2>
<ul>
  <li>You lie or sit comfortably with the foot supported.</li>
  <li>A gel is applied to the skin, and the applicator is worked over the painful area <span data-temp>for a few minutes</span>.</li>
  <li>You will feel a strong, rapid tapping. <span data-temp>Most patients describe it as uncomfortable rather than painful, and the intensity is adjusted during the session.</span></li>
  <li><span data-temp>No anaesthetic is used.</span></li>
</ul>

<h2 id="after">After a session</h2>
<p><span data-temp>There is no recovery period, so you can walk out and drive straight away.</span> The area can feel tender for a short time afterwards. Your podiatrist will tell you what activity is fine in the days after treatment and what to avoid.</p>

<h2 id="how-many">How many sessions?</h2>
<p><span data-temp>That depends on how long the problem has been there and how the tissue responds. Your podiatrist will discuss the likely course with you before you commit to it, rather than after.</span></p>

<h2 id="not-alone">Why it is rarely used on its own</h2>
<p>If the reason your heel or tendon was overloaded is still there, the pain has every chance of returning. That is why shockwave is normally paired with something that addresses the cause, such as <a href="services/custom-orthotics.html">custom orthotics</a>, footwear changes or a loading programme for the tendon.</p>

<h2 id="is-it-right">Is it right for you?</h2>
<p>That is decided at the assessment, not before. If your pain has been going on for a while and has not responded to the usual measures, it is worth asking about. <span data-temp>Shockwave is available at selected clinics, so call the clinic nearest you before booking if it is the treatment you are after.</span></p>
""",
    },

    {
        'SLUG': 'when-should-you-see-a-podiatrist',
        'TITLE': 'When Should You See a Podiatrist? Signs It Is Time to Book',
        'META_TITLE': 'When Should You See a Podiatrist? Signs It Is Time to Book',
        'CATEGORY': 'Getting started',
        'DATE': '8 July 2026',
        'EXCERPT': 'What a podiatrist actually treats, the signs that mean it is worth booking, '
                   'and when to see your GP or seek urgent care instead.',
        'CARD_IMG': 'blog-see-podiatrist',
        'HERO_IMG': 'post-see-podiatrist',
        'CARD_ALT': 'A practitioner handing paperwork to a patient at reception',
        'ABOUT': [],
        'SUMMARY': [
            'Podiatrists assess and treat the feet and lower limb, including pain that shows '
            'up at the shin, knee or hip.',
            'You do not need a referral to book.',
            'Pain that lasts, keeps coming back or changes the way you walk is worth having '
            'assessed.',
            'Sudden severe pain, an injury you cannot walk on, or signs of infection need '
            'prompt medical care instead.',
        ],
        'RELATED': [('service', 'biomechanics'), ('service', 'general-foot-care'),
                    ('condition', 'Heel Pain'), ('condition', 'Running Injuries')],
        'BODY': """
<p>Most people put up with foot and leg pain for longer than they need to, often because they are not sure whether it is “bad enough” to see someone, or who to see. This is a practical guide to when a podiatrist is the right call.</p>

<h2 id="what-podiatrists-do">What a podiatrist does</h2>
<p>A podiatrist assesses, diagnoses and treats problems of the feet and lower limb. That includes everyday care such as nails, corns and calluses, but also pain that starts in the way the feet and legs load, which can show up at the heel, the arch, the shin, the <a href="conditions/knee-pain.html">knee</a> or the hip.</p>
<p>Podiatry is a primary contact profession in Australia, so you can book directly without a referral. If you are on a Medicare care plan, your GP will refer you.</p>

<h2 id="signs">Signs it is time to book</h2>

<h3>1. Pain that has lasted more than a few weeks</h3>
<p>Aches that settle in a day or two after a long walk are normal. Pain that is still there weeks later, or that has become part of your routine, such as <a href="conditions/heel-pain.html">heel pain</a> every morning, is worth having assessed.</p>

<h3>2. Pain that keeps coming back</h3>
<p>If a problem settles with rest and returns as soon as you go back to normal activity, rest is treating the symptom and not the cause. Finding that cause is what a <a href="services/biomechanics.html">biomechanical assessment</a> is for.</p>

<h3>3. You have changed the way you walk</h3>
<p>Limping, walking on the outside of the foot, or favouring one leg shifts load elsewhere, and can create a second problem on top of the first.</p>

<h3>4. Pain during or after exercise</h3>
<p>Shin, calf, Achilles or knee pain that appears at a certain distance or pace, or stops you training, is typical of a <a href="conditions/running-injuries.html">running injury</a> and usually has a load or mechanical reason behind it.</p>

<h3>5. Nail and skin problems you cannot manage yourself</h3>
<p>An <a href="conditions/ingrown-toenails.html">ingrown toenail</a>, a painful corn or a callus that keeps returning is straightforward to treat properly through <a href="services/general-foot-care.html">general foot care</a>, and usually worse for being dug at at home.</p>

<h3>6. You have noticed something about your child’s walking</h3>
<p>Feet that turn in or out, frequent tripping, or leg pain that limits activity are worth having assessed, even if the answer is that nothing needs doing yet.</p>

<h3>7. You have diabetes or reduced circulation</h3>
<p>Where sensation or circulation in the feet is reduced, small problems can become serious without much warning. Regular foot checks matter more, and so does having any change looked at early.</p>

<aside class="post-note">
  <h3>See your GP or seek urgent care instead if</h3>
  <ul>
    <li>you have had an injury and cannot put weight on the foot, or it looks misshapen</li>
    <li>the pain is sudden and severe, without an obvious cause</li>
    <li>there is spreading redness, heat or swelling, or you have a fever</li>
    <li>you have diabetes and notice a wound, a change in colour, or new numbness</li>
    <li>the calf is suddenly painful, swollen and warm</li>
  </ul>
</aside>

<h2 id="what-to-bring">What to bring to your first appointment</h2>
<ul>
  <li>the shoes you wear most, including work or sports shoes</li>
  <li>any orthotics or insoles you already use</li>
  <li>any scans, X-rays or reports you have</li>
  <li>a list of your medications</li>
  <li><span data-temp>shorts, or loose trousers, if your knees or hips are involved</span></li>
</ul>

<h2 id="booking">Booking an appointment</h2>
<p>Each of our eleven clinics books into its own diary, so choose the clinic nearest you and book straight in, or call and we will point you to the right practitioner. <span data-temp>Allow about 45 minutes for a first appointment.</span> That covers the assessment, the diagnosis and an explanation of the plan before any treatment starts. For fees and rebates, call the clinic you want to attend and reception will quote you before you book.</p>
""",
    },
]
