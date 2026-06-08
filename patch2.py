import re

with open('gen.py', 'r') as f:
    c = f.read()

with open('modal_js.txt', 'r') as f:
    modal_js = f.read().strip()

# ── 1. All Apply buttons -> modal trigger ─────────────────────────────────────
c = re.sub(
    r'href="https://calendly\.com/kyle-krysongroup/introduction" target="_blank"',
    'href="javascript:void(0)" onclick="openApplyModal()"',
    c
)

# ── 2. Add modal JS to end of SHARED_JS ──────────────────────────────────────
old_shared_end = "});\n\"\"\""
new_shared_end = "});\n" + modal_js + '\n"""'
c = c.replace(old_shared_end, new_shared_end, 1)

# ── 3. APPLICATION_MODAL variable ────────────────────────────────────────────
AM_START = "BOOKING_MODAL = ''\n"
AM_INSERT = """BOOKING_MODAL = ''

APPLICATION_MODAL = (
'<div class="am-ov" id="applyModal">'
'<div class="am-box">'
'<button class="am-close" onclick="closeApplyModal()" aria-label="Close">&times;</button>'
'<div class="am-prog"><div class="am-prog-bar" id="amBar" style="width:0%"></div></div>'
'<div class="am-step active" id="amS1">'
'<div class="am-eye">Step 1 of 3</div>'
'<h3 class="am-h">What is your current monthly revenue?</h3>'
'<div class="am-opts">'
'<button class="am-opt" data-v="low" onclick="amPick(this,1)">Under &pound;5,000 /mo</button>'
'<button class="am-opt" data-v="mid" onclick="amPick(this,1)">&pound;5,000 to &pound;15,000 /mo</button>'
'<button class="am-opt" data-v="high" onclick="amPick(this,1)">&pound;15,000 to &pound;40,000 /mo</button>'
'<button class="am-opt" data-v="top" onclick="amPick(this,1)">&pound;40,000+ /mo</button>'
'</div></div>'
'<div class="am-step" id="amS2">'
'<div class="am-eye">Step 2 of 3</div>'
'<h3 class="am-h">What is your biggest sales problem right now?</h3>'
'<div class="am-opts">'
'<button class="am-opt" data-v="cr" onclick="amPick(this,2)">My close rate is too low</button>'
'<button class="am-opt" data-v="sc" onclick="amPick(this,2)">I am the only one closing</button>'
'<button class="am-opt" data-v="inc" onclick="amPick(this,2)">Revenue is inconsistent month to month</button>'
'<button class="am-opt" data-v="fu" onclick="amPick(this,2)">No follow-up system in place</button>'
'<button class="am-opt" data-v="sr" onclick="amPick(this,2)">Poor show rate on booked calls</button>'
'</div></div>'
'<div class="am-step" id="amS3">'
'<div class="am-eye">Step 3 of 3</div>'
'<h3 class="am-h">Are you ready to invest in fixing this in the next 30 days?</h3>'
'<div class="am-opts">'
'<button class="am-opt" data-v="yes" onclick="amPick(this,3)">Yes, I am ready to move</button>'
'<button class="am-opt" data-v="no" onclick="amPick(this,3)">Still exploring my options</button>'
'</div></div>'
'<div class="am-step am-result" id="amGo">'
'<div class="am-tick">&#10003;</div>'
'<h3 class="am-h am-h-ok">You look like a strong fit.</h3>'
'<p class="am-p">This is a 30-minute conversation. No pitch. We understand your situation and confirm fit before anything is discussed commercially.</p>'
'<a href="https://calendly.com/kyle-krysongroup/introduction" target="_blank" class="btn bp am-book-btn">Book Your Application Call &rarr;</a>'
'<p class="am-note">We do not take every application. Places are limited.</p>'
'</div>'
'<div class="am-step am-result" id="amNo">'
'<div class="am-cross">&#10007;</div>'
'<h3 class="am-h">Not the right fit yet.</h3>'
'<p class="am-p">We work with coaches doing &pound;5,000 per month or more who have consistent demand and sales calls coming in. If you are not there yet, we are not the right solution at this stage.</p>'
'<p class="am-p" style="font-size:14px;color:var(--w40);margin-top:4px">Read our Insights in the meantime. Come back when you are past &pound;5k per month with a proven offer.</p>'
'<div style="display:flex;gap:12px;margin-top:24px;flex-wrap:wrap">'
'<button class="btn bs" onclick="closeApplyModal()" style="font-size:11px;padding:10px 22px">Close</button>'
'<a href="insights.html"><button class="btn bs" style="font-size:11px;padding:10px 22px">Read Insights &rarr;</button></a>'
'</div></div></div></div>'
)

"""
c = c.replace(AM_START, AM_INSERT)

# ── 4. Inject APPLICATION_MODAL into pages ────────────────────────────────────
c = c.replace(
    "'\n<body>\n' + NAV +",
    "'\n<body>\n' + APPLICATION_MODAL + '\\n' + NAV +"
)
# INDEX body (check if already replaced to avoid double replace)
if "APPLICATION_MODAL + '\\n' + LOADER" not in c:
    c = c.replace(
        "'\n<body>\n' + LOADER + '\\n' + NAV + '\\n' + INDEX_BODY +",
        "'\n<body>\n' + APPLICATION_MODAL + '\\n' + LOADER + '\\n' + NAV + '\\n' + INDEX_BODY +"
    )

# ── 5. Hero headline (punchier) ───────────────────────────────────────────────
c = c.replace(
    '<span class="ln"><span>Your coaching</span></span>\n<span class="ln"><span>works. Your</span></span>\n<span class="ln"><span>sales system <em>does not.</em></span></span>',
    '<span class="ln"><span>Your offer works.</span></span>\n<span class="ln"><span>Your sales calls</span></span>\n<span class="ln"><span>do <em>not.</em></span></span>'
)

# ── 6. Spots badge in hero (before .hb div) ───────────────────────────────────
SPOTS = '<div class="spots-badge rv"><span class="spots-dot"></span><span>Accepting applications for <strong>June 2026</strong> &nbsp;&bull;&nbsp; <strong>2 spots</strong> remaining</span></div>\n'
c = c.replace(
    '<div class="hb">\n<a href="javascript:void(0)" onclick="openApplyModal()"><button class="btn bp" style="font-size:13px',
    SPOTS + '<div class="hb">\n<a href="javascript:void(0)" onclick="openApplyModal()"><button class="btn bp" style="font-size:13px'
)

# ── 7. Spots badge in CTA section ────────────────────────────────────────────
c = c.replace(
    '<p class="cta-note">We do not take every application. Places are limited.</p>',
    '<div class="spots-badge spots-badge-cta"><span class="spots-dot"></span><span>Accepting applications for <strong>June 2026</strong> &nbsp;&bull;&nbsp; <strong>2 spots</strong> remaining</span></div>'
)

# ── 8. Video Coming Soon section in INDEX_BODY ────────────────────────────────
VIDEO_CS = (
    '<div class="glow-div"></div>\n'
    '<section class="sec vcs-sec" style="background:var(--dark);padding:clamp(64px,8vw,100px) clamp(24px,5vw,80px)">\n'
    '<div style="text-align:center;max-width:880px;margin:0 auto">\n'
    '<div class="sl" style="color:var(--lime)">See It In Action</div>\n'
    '<h2 style="font-family:var(--f);font-size:clamp(26px,4vw,52px);font-weight:700;color:#FFFFFF;line-height:1.15;margin-bottom:clamp(32px,4vw,56px)">Watch how the system works.</h2>\n'
    '<div class="vcs-wrap">\n'
    '<div class="vcs-scanlines"></div>\n'
    '<div class="vcs-rings"><div class="vcs-ring r1"></div><div class="vcs-ring r2"></div><div class="vcs-ring r3"></div></div>\n'
    '<div class="vcs-play"><svg width="22" height="26" viewBox="0 0 22 26" fill="none"><path d="M1 1.5L21 13L1 24.5V1.5Z" fill="#C8F135" stroke="#C8F135" stroke-width="1.5" stroke-linejoin="round"/></svg></div>\n'
    '<div class="vcs-text"><div class="vcs-coming">Coming Soon</div><div class="vcs-dots"><span></span><span></span><span></span></div></div>\n'
    '</div></div></section>\n'
)
c = c.replace(
    '<div class="glow-div"></div>\n<section class="sec" style="background:var(--bg2)">\n<div class="sl">Why Kryson Works</div>',
    VIDEO_CS + '<div class="glow-div"></div>\n<section class="sec" style="background:var(--bg2)">\n<div class="sl">Why Kryson Works</div>'
)

# ── 9. Pricing FAQ item ───────────────────────────────────────────────────────
PRICE_FAQ = (
    '<div class="fq rv"><button class="fq-q">What is the investment?</button>'
    '<div class="fq-a"><div class="fq-a-in">Our engagements are structured on a monthly retainer plus a performance element. '
    'We are transparent about exact figures on the application call. What we can say: the model is designed so that if the '
    'system does not move your revenue, the commercial structure reflects that. Most clients recover the full investment within '
    'the first month of improved conversion. We work with coaches who see sales infrastructure as an investment, not a cost.'
    '</div></div></div>\n'
)
c = c.replace(
    '<div class="fq rv"><button class="fq-q">Who is Kryson for?</button>',
    PRICE_FAQ + '<div class="fq rv"><button class="fq-q">Who is Kryson for?</button>'
)

with open('gen.py', 'w') as f:
    f.write(c)

print("patch2.py done - verifying gen.py syntax...")
