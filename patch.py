import re

with open('gen.py', 'r') as f:
    c = f.read()

# ── 1. All Calendly popup buttons → direct link ──────────────────────────────
DIRECT = 'href="https://calendly.com/kyle-krysongroup/introduction" target="_blank"'

# onclick popup pattern in href=""
c = re.sub(
    r'href="" onclick="Calendly\.initPopupWidget\(\{url:\\\'[^\'\\]*\\\'\}\);return false;"',
    DIRECT,
    c
)
# Also the mobile nav version (no backslash escapes)
c = re.sub(
    r'href="" onclick="Calendly\.initPopupWidget\(\{url:\'[^\']*\'\}\);return false;"',
    DIRECT,
    c
)

# ── 2. Remove CALENDLY_BADGE entirely (replace with empty string) ─────────────
c = re.sub(
    r"CALENDLY_BADGE = '''.*?'''",
    "CALENDLY_BADGE = ''",
    c,
    flags=re.DOTALL
)

# Also remove CDN calendly link since badge is gone
c = c.replace('<link href="https://assets.calendly.com/assets/external/widget.css" rel="stylesheet">\n', '')

# ── 3. Remove ALL em dashes ──────────────────────────────────────────────────
# Ticker: replace " &mdash; " with " / "
c = c.replace(' &mdash; Limitless Fitness Coaching &mdash; ', ' / Limitless Fitness Coaching / ')
c = c.replace(' &mdash; eCom Revenue Mastery &mdash; ', ' / eCom Revenue Mastery / ')
c = c.replace(' &mdash; Elevate Coaching &mdash; ', ' / Elevate Coaching / ')
c = c.replace(' &mdash; Peak State Performance &mdash; ', ' / Peak State Performance / ')
# Stats band sub
c = c.replace('Sarah T. &mdash; Elevate Coaching, 90 days', 'Sarah T., Elevate Coaching, 90 days')
# Kyle attribution
c = c.replace('Kyle Read &mdash; Founder, Kryson Limited', 'Kyle Read, Founder of Kryson')
# About role
c = c.replace('Founder &amp; Managing Director &mdash; Kryson Limited, est. 2024',
               'Founder &amp; Managing Director, Kryson Limited')
# Credentials
c = c.replace('Founded Kryson in 2024 &mdash; &pound;5M+ in client revenue since launch',
               'Founded Kryson in 2024. &pound;5M+ in client revenue since launch.')
# General: remaining &mdash; with space around → comma+space
c = re.sub(r'\s+&mdash;\s+', ', ', c)
c = re.sub(r'&mdash;\s+', '', c)
c = re.sub(r'\s+&mdash;', '', c)
c = c.replace('&mdash;', '')

# ── 4. Language: coaching lingo ──────────────────────────────────────────────
replacements = [
    ('100 Enquiries', '100 Applications'),
    ('enquiries. Our clients move that number', 'applications. Our clients move that number'),
    ('closes 12% of enquiries', 'closes 12% of applications'),
    ('No shortage of enquiries', 'No shortage of applications'),
    ('no shortage of enquiries', 'no shortage of applications'),
    ('not having enough enquiries', 'not getting enough applications'),
    ('enough enquiries', 'enough applications'),
    ('initial enquiry and the follow-up', 'initial application and the first call'),
    ('between the initial enquiry', 'between the initial application'),
    ('from first enquiry to closed deal', 'from application to closed deal'),
    ('first enquiry to closed deal', 'from application to closed deal'),
    ('new enquiry', 'new application'),
    ('an enquiry', 'an application'),
    ('every enquiry', 'every application'),
    ('taking every enquiry', 'taking every application'),
    ('respond to a new enquiry', 'respond to a new application'),
    ('enquiry', 'application'),
    ('Enquiries', 'Applications'),
    # "Leads go cold" → coaching lingo
    ('Leads go cold and nobody chases them.',
     'Applications sit unanswered and prospects go cold.'),
    ('There is no system catching them. No one following up consistently. You are losing warm, interested leads every single week.',
     'There is no system following up. Warm prospects who applied and showed genuine interest disappear every week because no one is reaching back out.'),
    ('losing warm, interested leads every single week',
     'losing warm, interested prospects every single week'),
    # "leads" in other contexts
    ('More leads into a broken sales process', 'More applications into a broken sales process'),
    ('More leads means more pressure', 'More applications means more pressure'),
    ('More leads means more revenue', 'More applications means more revenue'),
    ('More leads into a broken system', 'More applications into a broken system'),
    ('getting 40 enquiries a month', 'getting 40 applications a month'),
    ('no shortage of applications. The problem is that the conversion rate between application and enrolled client',
     'no shortage of applications. The problem is that the conversion rate between application and enrolled client'),
    ('If you are getting 40 applications a month', 'If you are getting 40 applications a month'),
    ('Fix show rate before close rate. Fix speed to lead before the script.',
     'Fix show rate before close rate. Fix speed to application response before the script.'),
    ('speed to lead', 'speed to response'),
    ('Speed to lead', 'Speed to response'),
    ('Leads were coming in consistently through organic content but a large proportion were going cold',
     'Applications were coming in consistently through organic content but a large proportion were going cold'),
    # discovery call → sales call where appropriate
    ('The average coaching business closes 12% of applications',
     'The average coaching business closes 12% of applications'),
]

for old, new in replacements:
    c = c.replace(old, new)

# ── 5. "Direct Access to Kyle" section → "Senior Oversight. No Handoffs." ────
OLD_KYLE_WWD = '''<div class="wwd-card rv"><div class="wwd-card-head"><div class="wwd-num">04</div><h3>Direct Access to Kyle</h3></div><p>Not a junior account manager. Kyle is involved directly in every engagement throughout. You get senior-level commercial leadership applied to your business from day one.</p><ul class="wwd-delivers"><li>Direct Slack access to Kyle</li><li>Weekly strategy and review calls</li><li>Deal coaching on live opportunities</li><li>No handoffs to junior staff</li></ul></div>'''
NEW_KYLE_WWD = '''<div class="wwd-card rv"><div class="wwd-card-head"><div class="wwd-num">04</div><h3>Senior-Led. No Handoffs.</h3></div><p>Every engagement is run by operators who have been inside coaching businesses. No junior account managers. No templates handed off on day one. Senior commercial leadership in your operation throughout.</p><ul class="wwd-delivers"><li>Direct Slack access throughout</li><li>Weekly strategy and review calls</li><li>Live deal coaching on active pipeline</li><li>No handoffs or junior intermediaries</li></ul></div>'''
c = c.replace(OLD_KYLE_WWD, NEW_KYLE_WWD)

OLD_KYLE_SERV = '''<div class="wwd-card rv"><div class="wwd-card-head"><div class="wwd-num">04</div><h3>Direct Access to Kyle</h3></div><p>Not a junior account manager. Kyle is involved directly in every engagement throughout. Senior-level commercial leadership applied to your business from day one.</p><ul class="wwd-delivers"><li>Direct Slack access throughout</li><li>Weekly strategy and review calls</li><li>Deal coaching on live opportunities</li><li>No handoffs or junior intermediaries</li><li>Strategic input on pricing and offer structure</li></ul></div>'''
NEW_KYLE_SERV = '''<div class="wwd-card rv"><div class="wwd-card-head"><div class="wwd-num">04</div><h3>Senior-Led. No Handoffs.</h3></div><p>Every engagement is run by operators who have lived inside coaching businesses. The people building your system have closed deals, managed closers, and run pipelines at scale. That context is what makes the work land.</p><ul class="wwd-delivers"><li>Direct Slack access throughout</li><li>Weekly strategy and review calls</li><li>Live deal coaching on active pipeline</li><li>No handoffs or junior intermediaries</li><li>Strategic input on pricing and offer structure</li></ul></div>'''
c = c.replace(OLD_KYLE_SERV, NEW_KYLE_SERV)

# ── 6. Homepage "The Founder" section → more firm-focused ────────────────────
OLD_FOUNDER_SECTION = '''<section class="sec" style="background:var(--bg2)">
<div class="sl">The Founder</div>
<h2 class="sh">I have been inside the room. <em>I know what is broken.</em></h2>
<div class="gr"></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:clamp(32px,5vw,80px);align-items:start" class="rv">
<div>
<p style="font-size:clamp(16px,1.8vw,20px);color:var(--w60);line-height:1.85;margin-bottom:20px">Before building Kryson, Kyle spent years working directly inside high-ticket coaching businesses. He went through several coaching mentorships himself &mdash; as a student, as a sales team member, and eventually as the person running the commercial operation.</p>
<p style="font-size:15px;color:var(--w60);line-height:1.85">He watched coaches with brilliant programmes and genuine results lose tens of thousands of pounds every month because the sales process underneath was either non-existent or held together with WhatsApp messages and gut feel. The pattern was identical every time: strong offer, real demand, broken system. Kryson exists to fix that.</p>
</div>
<div>
<div style="background:var(--bg3);padding:clamp(24px,3vw,40px);border-left:4px solid var(--lime);margin-bottom:20px">
<p style="font-size:15px;color:var(--w60);line-height:1.85;margin-bottom:14px">"I have sat in the programmes. I have been on the calls. I know exactly where coaches lose people and why. That context is what makes the systems we build actually work in coaching environments."</p>
<p style="font-family:var(--f);font-size:12px;color:var(--coral);letter-spacing:1px">Kyle Read &mdash; Founder, Kryson Limited</p>
</div>
<p style="font-size:15px;color:var(--w60);line-height:1.85;margin-bottom:20px">Kryson clients have closed over <strong style="color:var(--dark)">&pound;5M+ in revenue</strong> since we launched in 2024. We work with a small number of coaches at a time.</p>
<a href="about.html"><button class="btn bs" style="font-size:11px;padding:12px 28px">About the Firm &rarr;</button></a>
</div>
</div>
</section>'''

NEW_FOUNDER_SECTION = '''<section class="sec" style="background:var(--bg2)">
<div class="sl">Why Kryson Works</div>
<h2 class="sh">Built by people who have been <em>inside coaching businesses.</em></h2>
<div class="gr"></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:clamp(32px,5vw,80px);align-items:start" class="rv">
<div>
<p style="font-size:clamp(16px,1.8vw,20px);color:var(--w60);line-height:1.85;margin-bottom:20px">Kryson is not a sales consultancy that read a book about coaching. The team has worked directly inside coaching businesses at every level. We have been on the sales calls, reviewed the recordings, rebuilt broken pipelines, and trained closers from scratch inside live operations.</p>
<p style="font-size:15px;color:var(--w60);line-height:1.85">The pattern is always the same. A coach with a genuine offer and real results is losing revenue every week because the sales infrastructure underneath is either nonexistent or held together with WhatsApp messages and gut feel. The problem is not the coaching. It is the system. Kryson exists to fix that permanently.</p>
</div>
<div>
<div style="background:var(--bg3);padding:clamp(24px,3vw,40px);border-left:4px solid var(--lime);margin-bottom:20px">
<p style="font-size:15px;color:var(--w60);line-height:1.85;margin-bottom:14px">"We have sat in the programmes. We have been on the calls. We know exactly where coaches lose people and why. That context is what makes the systems we build actually work in coaching environments."</p>
<p style="font-family:var(--f);font-size:12px;color:var(--coral);letter-spacing:1px">Kyle Read, Founder of Kryson</p>
</div>
<p style="font-size:15px;color:var(--w60);line-height:1.85;margin-bottom:20px">Kryson clients have closed over <strong style="color:var(--dark)">&pound;5M+ in revenue</strong> since we launched in 2024. We work with a small number of coaches at a time.</p>
<a href="about.html"><button class="btn bs" style="font-size:11px;padding:12px 28px">About the Firm &rarr;</button></a>
</div>
</div>
</section>'''
c = c.replace(OLD_FOUNDER_SECTION, NEW_FOUNDER_SECTION)

# ── 7. FAQ: "leads" language fix ─────────────────────────────────────────────
c = c.replace(
    'Do you generate leads for coaches?',
    'Do you generate applications or leads for coaches?'
)
c = c.replace(
    'No. We work with coaches who already have consistent demand. Our job is to convert that demand at a much higher rate. If your primary problem is not getting enough applications, we are not the right fit at this stage.',
    'No. We work with coaches who already have applications and sales calls coming in. Our job is to convert those at a much higher rate. If your primary problem is not getting enough traffic or applications, we are not the right fit at this stage.'
)

# ── 8. Replace insights with fresh coaching-specific research-based content ───
OLD_INSIGHTS_BODY_START = "INSIGHTS_BODY = '''<section id=\"insights\" class=\"sec\" style=\"background:var(--bg)\">"
NEW_INSIGHTS_BODY = '''INSIGHTS_BODY = \'\'\'<section id="insights" class="sec" style="background:var(--bg)">
<p class="sp" style="margin-bottom:clamp(40px,5vw,64px)">Practical thinking on sales systems, closer management, and building coaching businesses that scale. Written from inside real operations, not from the outside looking in.</p>
<div class="ins-list">

<div class="ins-item rv">
<div class="ins-head" onclick="toggleIns(this)">
<div class="ins-meta"><span class="ins-date">14 January 2025</span><span class="ins-cat">Close Strategy</span></div>
<div class="ins-title">The 1-Call Close vs. 2-Call Close: Which Model Is Right for Your Coaching Business</div>
<button class="ins-btn"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke-width="1.5"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></button>
</div>
<div class="ins-body"><div class="ins-inner">
<p>Most coaches default to a 1-call close model without ever consciously choosing it. They book a strategy call, go through their process, make the offer, and hope for a yes on that same call. For some offers and audiences, this works well. For others, it leaves significant revenue on the table.</p>
<p>The 1-call close works best when the ticket price is under £3,000 to £5,000, the prospect has already consumed a lot of your content and arrives warm, and your application pre-qualifies intent and financial readiness before anyone books. If these conditions are met, a 1-call model can run at 30 to 40 percent close rates consistently.</p>
<p>The 2-call model works better for higher ticket offers above £5,000, audiences that require more trust-building, or businesses where the closer is not the founder. Call one is a discovery and qualification call. Call two is the solution and offer presentation. The decision is expected on call two. This structure allows the closer to do a deeper diagnosis on call one and tailor the presentation on call two with precision. It also filters out low-intent prospects before spending time on a full pitch.</p>
<p>The mistake most coaches make is running a 1-call close model on a high-ticket offer without a proper application to pre-qualify. They end up in 90-minute calls with people who were never going to buy. An application that captures current revenue, investment budget, and specific goal before the call is booked changes the entire quality of calls in the calendar.</p>
<p>Choose your model based on your ticket price and audience temperature. Then build the system to match it. The model you choose should be intentional, not accidental.</p>
</div></div></div>

<div class="ins-item rv">
<div class="ins-head" onclick="toggleIns(this)">
<div class="ins-meta"><span class="ins-date">28 February 2025</span><span class="ins-cat">Team Building</span></div>
<div class="ins-title">The Setter Role: How to Build a Pipeline of Booked Sales Calls Without Doing It Yourself</div>
<button class="ins-btn"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke-width="1.5"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></button>
</div>
<div class="ins-body"><div class="ins-inner">
<p>The setter is one of the most underutilised roles in online coaching businesses. Most coaches either do their own DM outreach and call booking, or they skip this function entirely and rely on inbound. A well-trained setter sits between your content and your closer and converts interest into booked sales calls at a consistent rate.</p>
<p>What a setter actually does: responds to comments, DMs, and story replies on social media; qualifies prospects through a short conversational script; and books qualified people into the sales calendar. A good setter should be booking 15 to 30 qualified calls per week at scale. A bad setter books anyone who will say yes, which produces low show rates and wasted closer time.</p>
<p>The setter script matters more than the setter. Most setters fail not because they lack ability but because they have no framework. They improvise each conversation, qualify inconsistently, and book calls with people who have no money, no urgency, or no decision authority. A proper setter script covers four things: identifying the pain or desire, confirming financial seriousness, establishing timeline, and creating genuine expectation for what the call will involve.</p>
<p>On compensation: setters are typically paid a small base plus a per-booked-call bonus, with an additional bonus for calls that close. The per-close bonus keeps them incentivised to qualify properly rather than just hitting a booking number. A setter paid only per booking will fill your closer\'s calendar with people who cannot buy.</p>
<p>The setter-to-closer pipeline, when built properly, is the engine behind coaching businesses at £100k per month and above. It does not require large volumes of followers. It requires consistent content output and a setter who treats every genuine comment as a potential conversation.</p>
</div></div></div>

<div class="ins-item rv">
<div class="ins-head" onclick="toggleIns(this)">
<div class="ins-meta"><span class="ins-date">19 March 2025</span><span class="ins-cat">Applications</span></div>
<div class="ins-title">Why Your Application Form Is Filtering Out Your Best Buyers</div>
<button class="ins-btn"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke-width="1.5"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></button>
</div>
<div class="ins-body"><div class="ins-inner">
<p>The application form is the first stage of the sales process for most high-ticket coaching businesses. Most coaches treat it as a filter to keep out the wrong people. The problem is that a badly designed application also filters out the right people and creates friction for exactly the buyers you want most.</p>
<p>Two common failure modes. The first is an application that asks too many questions and takes too long to complete. High-intent buyers with money and options will not fill out a 25-question form before they have any relationship with you. If your application takes more than four minutes, you are losing qualified people at the top of the funnel before a conversation ever starts.</p>
<p>The second failure mode is an application that does not qualify at all. A form that asks only name, email, and "what are your goals" does not filter for financial readiness or decision-making authority. Your closer ends up on calls with people who are interested but not ready. Close rate drops. Closer morale drops. Founder assumes the closer is the problem.</p>
<p>A well-designed application for a high-ticket coaching offer covers five things concisely: current situation and main goal, what they have already tried, current monthly revenue or investment budget (framed as a qualifier, not a gatekeep), timeline and urgency, and how they found you. That is it. Five fields, easy to complete, and it tells your closer exactly how to open the call.</p>
<p>The application form also serves a priming function. The act of completing it raises commitment to the process. Prospects who have invested five minutes in an application show up to calls with higher intent than those who just clicked "book a call" from a link in bio.</p>
</div></div></div>

<div class="ins-item rv">
<div class="ins-head" onclick="toggleIns(this)">
<div class="ins-meta"><span class="ins-date">3 April 2025</span><span class="ins-cat">Show Rate</span></div>
<div class="ins-title">The Show Rate Problem: Why Coaches Lose Revenue Before the Call Even Starts</div>
<button class="ins-btn"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke-width="1.5"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></button>
</div>
<div class="ins-body"><div class="ins-inner">
<p>Most coaches obsess over close rate. Few obsess over show rate. That is a mistake because a prospect who does not show up costs you a booked slot, a prepared closer, and produces nothing. Average show rates across coaching businesses sit between 60 and 70 percent. The best operations get to 85 to 90 percent.</p>
<p>The difference between 65 percent and 85 percent on 40 booked calls per month is 8 additional attended calls. At a 35 percent close rate, that is roughly 3 extra clients per month before you change a single thing about how you sell. That is significant recurring revenue sitting in a problem most coaches do not even track.</p>
<p>Show rate is a nurture problem. The gap between booking and attending is where doubt grows. The prospect has time to talk themselves out of it, get distracted, or simply forget. If no one reaches out during that window, a meaningful percentage will not show.</p>
<p>A basic pre-call sequence that consistently moves show rates: a confirmation message immediately after booking with the call link and what to expect, a short piece of social proof 24 to 48 hours before, a reminder with the link and a specific prompt two hours before, and a message from the closer introducing themselves the evening before the call. This sequence alone moves show rates by 10 to 15 points for most coaching businesses.</p>
<p>Build a rescheduling process for no-shows too. Message within one hour of the missed call. Follow up the next morning. Offer to rebook 48 hours later. Recovered no-shows are among the highest-converting prospects in any pipeline because the intent was already demonstrated.</p>
</div></div></div>

<div class="ins-item rv">
<div class="ins-head" onclick="toggleIns(this)">
<div class="ins-meta"><span class="ins-date">22 April 2025</span><span class="ins-cat">Objections</span></div>
<div class="ins-title">"I Need to Think About It" Is Not an Objection. Here Is What It Actually Is.</div>
<button class="ins-btn"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke-width="1.5"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></button>
</div>
<div class="ins-body"><div class="ins-inner">
<p>"I need to think about it" is the most common thing a closer hears after making an offer. Most training tells closers to treat it as an objection and overcome it. That framing is wrong, and it is the reason the response so rarely works.</p>
<p>"I need to think about it" is not an objection. It is a symptom. It is what happens when a prospect reaches the offer and still has an unresolved concern they have not voiced. The real objection is still in the call somewhere. The closer\'s job is to find it, not to rebut the surface statement.</p>
<p>The most effective response is a question: "Of course. When you say you need to think about it, what specifically is sitting with you?" This opens the conversation back up. In most cases, the prospect will name the real concern: the price feels high relative to a specific outcome they are not yet sure about, they need to talk to a partner, or they are not fully convinced the programme is the right fit for their situation. Each of these is addressable.</p>
<p>The better long-term solution is to prevent "I need to think about it" from appearing at all. It shows up when the discovery stage was not deep enough. If the closer has genuinely understood the prospect\'s situation, surfaced the real cost of staying stuck, and connected the programme directly to what the prospect said they needed, there is almost nothing to think about. The decision makes itself.</p>
<p>"I need to think about it" is feedback about the quality of the call up to that point, not a closing problem. Train your closers to hear it that way and watch the pattern disappear.</p>
</div></div></div>

<div class="ins-item rv">
<div class="ins-head" onclick="toggleIns(this)">
<div class="ins-meta"><span class="ins-date">7 June 2025</span><span class="ins-cat">Hiring</span></div>
<div class="ins-title">How to Hire a Closer for Your Coaching Business Without Getting Burned</div>
<button class="ins-btn"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke-width="1.5"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></button>
</div>
<div class="ins-body"><div class="ins-inner">
<p>Hiring a closer is one of the highest-risk decisions in a coaching business. Done right, it removes you from the sales function and unlocks significant scale. Done wrong, it costs you three to four months of time, money, and close rate damage before you accept it is not working.</p>
<p>The most common hiring mistake is hiring on claimed track record. A closer tells you they were closing at 40 percent for another coach. You hire them. Within 30 days they are closing at 22 percent and you do not understand why. The reason: close rate is context-dependent. Their previous 40 percent was the product of a strong offer, a warm audience, a proper system, and a closer who had been trained into that specific environment. Drop them into a different system and that number often does not transfer.</p>
<p>What to assess in the hiring process instead: Can they run a structured discovery without leaping to the pitch? How do they handle a prospect who is interested but uncertain? Can they clearly articulate why they ask each question in a discovery call? Do they have a genuine interest in coaching or are they purely transactional? Attitude to coaching feedback matters as much as current ability because you will be building their skill from scratch in your specific system.</p>
<p>Always run a paid trial with clear performance criteria before committing to a full engagement. Two weeks, 10 to 15 calls, with weekly call reviews. You will know more from those two weeks than any interview process.</p>
<p>The right closer in the wrong system fails. The wrong closer in the right system also fails. The combination you are building toward is a capable, coachable person dropped into a working framework with weekly training and accountability built in. That combination has a very high success rate.</p>
</div></div></div>

<div class="ins-item rv">
<div class="ins-head" onclick="toggleIns(this)">
<div class="ins-meta"><span class="ins-date">15 July 2025</span><span class="ins-cat">Operations</span></div>
<div class="ins-title">GoHighLevel for Coaching Businesses: What to Set Up and What to Ignore</div>
<button class="ins-btn"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke-width="1.5"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></button>
</div>
<div class="ins-body"><div class="ins-inner">
<p>GoHighLevel has become the default CRM and automation platform for many online coaching businesses. It is powerful, reasonably priced, and purpose-built for the kind of pipeline management that coaching sales requires. It is also easy to over-build and end up with a system that is more impressive than useful.</p>
<p>What to set up first. A pipeline with five to seven stages that map to your actual sales process, not a generic template. Each stage should have a clear definition of what it means for a prospect to be there and what action is needed to move them forward. Suggested stages for a 1-call coaching model: Application Received, Call Booked, Call Attended, Offer Made, Follow-Up In Progress, Enrolled, Lost. Every prospect who is active should be in one of these stages with a next action and a date.</p>
<p>Second, set up your pre-call automated sequence: confirmation message, reminder sequence, and a no-show follow-up workflow. These can be built in GHL in under two hours and they run without anyone touching them. Show rate improvement from automated sequences alone is consistently 10 to 15 percent across coaching businesses we have worked with.</p>
<p>What to ignore, at least initially: complex automations, multi-step nurture sequences, email newsletters, and social proof drip campaigns. These are valuable eventually but they are not what moves close rate in the first 90 days. A clean pipeline, a working pre-call sequence, and a consistent follow-up process for non-conversions will generate more revenue than an elaborate automation library.</p>
<p>The most important thing about any CRM is that your team uses it consistently. A simple setup that everyone trusts and updates daily produces far better outcomes than a sophisticated system that gets abandoned after week three.</p>
</div></div></div>

<div class="ins-item rv">
<div class="ins-head" onclick="toggleIns(this)">
<div class="ins-meta"><span class="ins-date">2 August 2025</span><span class="ins-cat">Performance</span></div>
<div class="ins-title">Close Rate Benchmarks for High-Ticket Coaching (And Where You Should Be)</div>
<button class="ins-btn"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke-width="1.5"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></button>
</div>
<div class="ins-body"><div class="ins-inner">
<p>Close rate is the most tracked metric in coaching sales and also the most misunderstood. What counts as a good close rate depends entirely on what you are counting. Coaches who include every booked call (including no-shows and completely unqualified prospects) will always report a lower close rate than coaches who count only attended calls with qualified prospects. Make sure you are comparing the right number.</p>
<p>Attended call close rate benchmarks by offer type and ticket price. For offers between £1,500 and £3,000: industry average is 25 to 35 percent with a properly trained closer, 15 to 22 percent without one. For offers between £3,000 and £8,000: industry average is 20 to 30 percent with a good system, 12 to 18 percent without. For offers above £8,000: 15 to 25 percent is strong; anything above 30 percent consistently suggests either exceptional positioning or a very warm inbound audience.</p>
<p>What moves close rate most reliably is not closer talent. It is call quality, which is a function of three things: how well the prospect was qualified before the call, how deeply the closer diagnoses the problem in the first 20 minutes, and how directly the solution is positioned to what the prospect said they needed. A closer running a proper framework on a qualified prospect will outperform a naturally talented closer with no framework in every comparison.</p>
<p>The metric that matters alongside close rate is revenue per call. A closer at 35 percent on a £5,000 offer generates £1,750 per call. A closer at 25 percent on a £10,000 offer generates £2,500 per call. Close rate without ticket context is incomplete information.</p>
<p>Track both. Review weekly. And if your close rate has been flat for more than six weeks, the answer is not a new script. It is a call review.</p>
</div></div></div>

<div class="ins-item rv">
<div class="ins-head" onclick="toggleIns(this)">
<div class="ins-meta"><span class="ins-date">19 September 2025</span><span class="ins-cat">Objections</span></div>
<div class="ins-title">The Price Objection in High-Ticket Coaching: What It Means and How to Handle It</div>
<button class="ins-btn"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke-width="1.5"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></button>
</div>
<div class="ins-body"><div class="ins-inner">
<p>The price objection in high-ticket coaching almost never means "that is too much money." It means one of three things: they do not yet believe the result is certain enough to justify the investment, they have not made the emotional connection between their current pain and what the programme resolves, or there is a practical constraint (payment timing, partner buy-in) that has not been surfaced yet.</p>
<p>Treating it as a money problem produces the worst responses. Discounting immediately trains prospects that the price is negotiable and undermines the value of the offer. Pushing harder on price creates resistance. Offering payment plans before exploring what is really happening misses the actual concern.</p>
<p>The right response to "that feels like a lot of money" is a question: "Compared to what?" This is not a rebuttal. It is a genuine invitation to explore whether the price has been correctly contextualised. If they say compared to their current monthly revenue, the conversation is about ROI. If they say compared to other programmes they have looked at, the conversation is about differentiation. The answer tells you exactly which direction to go.</p>
<p>Most price objections can be prevented entirely through good discovery. If the closer has properly surfaced the cost of the prospect\'s current situation and genuinely understood what resolving it is worth to them, the price conversation becomes a maths question, not an emotional one. A coach who is losing £15,000 a month to a broken sales process and knows it does not argue about an investment to fix it.</p>
<p>Prevention is better than handling. Build your discovery framework around surfacing financial impact, not just pain. The price objection disappears when the ROI is vivid before the offer is made.</p>
</div></div></div>

<div class="ins-item rv">
<div class="ins-head" onclick="toggleIns(this)">
<div class="ins-meta"><span class="ins-date">8 October 2025</span><span class="ins-cat">Scaling</span></div>
<div class="ins-title">From Self-Closing to a Sales Team: The 90-Day Transition Framework</div>
<button class="ins-btn"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke-width="1.5"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></button>
</div>
<div class="ins-body"><div class="ins-inner">
<p>Transitioning from self-closing to a sales team is the most significant commercial decision in a coaching business. The founders who do it well follow a specific sequence. The founders who do it badly all make the same mistake: they skip the system-building stage and go straight to hiring.</p>
<p>Month one is system documentation. Before anyone else can sell your offer, your sales process needs to exist as something external to your head. This means writing out your discovery framework question by question, scripting how you handle each common objection, documenting what a qualified application looks like, and defining what the offer presentation should cover. This work is harder than it sounds. Most founders discover during this process that they sell largely on intuition and have never articulated why they ask what they ask.</p>
<p>Month two is parallel operation with a closer in place. The closer goes through your framework, you review their calls weekly, and you give specific structured feedback rather than general commentary. The goal is not to make them sound like you. The goal is to get them reliably running the framework at a standard that produces consistent close rates. Expect close rate to be below yours for the first four to six weeks. This is normal and expected, not a sign that the closer is wrong.</p>
<p>Month three is managed handoff. You are off the calls. You review the weekly pipeline report and join the weekly closer coaching. You are available for escalations on genuinely unusual situations. By the end of month three, the system should be closing consistently at 30 to 40 percent and improving week by week as the closer builds pattern recognition inside a proper framework.</p>
<p>The 90-day window feels long. In practice, founders who attempt shortcuts arrive at month six with a closer who is still underperforming and a process that never got properly built. The 90-day investment produces a sales function that compounds for years.</p>
</div></div></div>

<div class="ins-item rv">
<div class="ins-head" onclick="toggleIns(this)">
<div class="ins-meta"><span class="ins-date">3 November 2025</span><span class="ins-cat">Growth</span></div>
<div class="ins-title">Why Coaching Businesses Plateau at £20k to £50k Per Month (And What Fixes It)</div>
<button class="ins-btn"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke-width="1.5"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></button>
</div>
<div class="ins-body"><div class="ins-inner">
<p>The £20,000 to £50,000 per month range is where the majority of coaching businesses stall. The content is working. The offer is proven. The results are real. But revenue has been flat for three to six months and the founder cannot identify a clear reason why. In almost every case, the reason is the same: the sales infrastructure was built for a smaller business and has not been upgraded.</p>
<p>At £10,000 to £20,000 per month, a founder doing their own sales calls with a basic follow-up process can hold the business together. Beyond that, the volume of sales activity required outpaces what one person can handle without the quality of every conversation declining. Call preparation gets shorter. Follow-up becomes sporadic. Objection handling gets lazy because the closer (usually the founder) is tired. Revenue plateaus even as the audience and inbound demand continue to grow.</p>
<p>The fix is not more content or a new offer. It is a sales infrastructure upgrade: a proper CRM with pipeline stages that the team uses every day, a trained closer who handles calls end to end, a structured follow-up sequence for every non-conversion, and a weekly performance review cadence so nothing sits in the pipeline without action.</p>
<p>The data across coaching businesses we have worked with shows the same pattern: close rate before system installation sits between 18 and 25 percent; after 60 to 90 days with a proper system in place, it sits between 32 and 48 percent. That improvement alone, applied to existing call volume, typically produces a 40 to 80 percent revenue increase without any change to marketing or content output.</p>
<p>The plateau is not a content problem. It is a conversion problem. And conversion problems are always systems problems.</p>
</div></div></div>

<div class="ins-item rv">
<div class="ins-head" onclick="toggleIns(this)">
<div class="ins-meta"><span class="ins-date">12 December 2025</span><span class="ins-cat">Management</span></div>
<div class="ins-title">Call Review That Actually Improves Close Rate: A Framework for Coaches</div>
<button class="ins-btn"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke-width="1.5"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></button>
</div>
<div class="ins-body"><div class="ins-inner">
<p>Weekly call review is the single highest-leverage management activity in a coaching sales operation. A 45-minute structured review, done properly every week, compounds into a material close rate improvement over 90 days. Most call reviews in coaching businesses either do not happen at all or happen in a way that produces defensiveness rather than growth.</p>
<p>The failure mode is a review structured around what the closer did wrong. The coach listens to a 60-minute call and spends 20 minutes explaining everything they would have said differently. The closer walks away feeling criticised rather than developed. Performance does not improve because the closer is in defensive mode, not learning mode.</p>
<p>The framework that works: start with the closer\'s self-assessment. Before you say anything, ask them what they felt went well and where they felt the call changed direction. This establishes genuine self-awareness as the foundation. Then pick one or two specific moments from the recording, with timestamps, and explore the decision-making: "At 14 minutes when they mentioned they had already tried a programme before, you moved past it quickly. What were you thinking there?"</p>
<p>The goal is to develop the closer\'s judgment, not to correct their behaviour. A closer who understands why a conversation shifted can make better decisions in real time on future calls. A closer who has been told what to say differently is pattern-matching without understanding, which breaks down as soon as a prospect says something unexpected.</p>
<p>Commit to one improvement focus per week. Not ten. One. The compound effect of a single genuine improvement each week, reviewed and reinforced the following week, is remarkable over three months.</p>
</div></div></div>

<div class="ins-item rv">
<div class="ins-head" onclick="toggleIns(this)">
<div class="ins-meta"><span class="ins-date">27 January 2026</span><span class="ins-cat">Team Building</span></div>
<div class="ins-title">Commission Structures That Keep Good Closers and Filter Out the Wrong Ones</div>
<button class="ins-btn"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke-width="1.5"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></button>
</div>
<div class="ins-body"><div class="ins-inner">
<p>Commission structure design in coaching businesses is almost always an afterthought. Most coaches either pay a flat percentage with no retainer, copy what they heard another coach was paying, or invent something on the spot when they are about to make a hire. All three approaches produce avoidable problems.</p>
<p>Pure commission with no retainer attracts closers who need to close fast because their income depends on it. Financial desperation in a sales conversation destroys close quality for high-ticket coaching. Prospects can feel urgency that comes from the closer\'s circumstances rather than genuine belief in the offer. The closers worth hiring have enough options that they will not work on pure commission without a relationship and a track record with you. If a closer is willing to work pure commission immediately, ask yourself why.</p>
<p>The structure that works in most coaching businesses: a base retainer sufficient to remove financial pressure (not large, typically £1,000 to £2,000 per month), plus 10 to 12 percent on collected revenue. Add a claw-back clause on refunds within 30 days. This keeps the closer focused on selling to the right people, not just closing numbers.</p>
<p>Build a performance accelerator above a target close rate or revenue number. If the closer hits 40 percent close rate or £30k collected in a month, the commission rate increases to 14 percent on everything above target. This creates real upside without inflating your baseline cost. Good closers will work hard for an accelerator that is achievable and meaningful.</p>
<p>Review the structure every three months as the closer\'s skill and your call volume grow. A structure that was right at 20 calls per month may need adjusting at 50. The commercial arrangement should evolve with the relationship.</p>
</div></div></div>

<div class="ins-item rv">
<div class="ins-head" onclick="toggleIns(this)">
<div class="ins-meta"><span class="ins-date">18 April 2026</span><span class="ins-cat">Kryson</span></div>
<div class="ins-title">What Building Sales Systems Inside Coaching Businesses Actually Teaches You</div>
<button class="ins-btn"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke-width="1.5"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></button>
</div>
<div class="ins-body"><div class="ins-inner">
<p>After working inside coaching businesses across fitness, mindset, ecommerce, business, and performance, including some of the biggest names in the space and the largest fitness brand in Romania, the patterns in what breaks and what works are consistent enough to be worth sharing directly.</p>
<p>The businesses that grow fastest are not the ones with the best content. They are the ones where the founder makes a genuine operational commitment to building a sales function and then stays out of it once it is built. The instinct to stay involved in every sales call, every objection, every decision is understandable and usually comes from a real place. It is also the most reliable way to slow everything down.</p>
<p>The highest-leverage change in every coaching business we have worked with is the same: a structured sales call framework that the closer runs consistently, reviewed weekly. Not the CRM setup. Not the follow-up automation. Not the commission structure. The framework. When a closer understands not just what to ask but why, and is coached on their decision-making in real calls each week, close rate moves materially and it stays moved.</p>
<p>The businesses that stall do so because they want results without the operational investment. They want a closer without a system. They want a CRM without a process. They want a weekly report without a weekly review cadence. These things cannot be separated. The system is the result. There is no shortcut past building it properly.</p>
<p>The coaches who go from £20k to £100k per month are not more talented than the ones who stay stuck. They are more willing to build the infrastructure that makes the talent irrelevant.</p>
</div></div></div>

</div>
</section>
<div class="glow-div"></div>\'\'\''''

# Find and replace the full INSIGHTS_BODY
import re
# Match everything from INSIGHTS_BODY = \'\'\'  to the closing \'\'\' 
c = re.sub(
    r"INSIGHTS_BODY = '''.*?'''",
    NEW_INSIGHTS_BODY,
    c,
    flags=re.DOTALL
)

with open('gen.py', 'w') as f:
    f.write(c)

print("patch.py done")
