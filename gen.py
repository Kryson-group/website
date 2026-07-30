#!/usr/bin/env python3
# KRYSON -- Health & Wellness Web Design Agency
# gen.py: static site generator
# NO f-strings. NO apostrophes in single-quoted strings. Use &#39; instead.

import os

APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbxKAw0elEOZONdurCiWqMFAROxTsIZoq0eqAA9JS1QqP9kfN1GhdkAHQeAJ2RUCzWoU/exec'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

NAV = (
    '<nav>'
    '<a href="index.html" class="nav-logo">Kryson</a>'
    '<ul class="nav-links">'
    '<li><a href="work.html">Our Work</a></li>'
    '<li><a href="pricing.html">Pricing</a></li>'
    '<li><a href="about.html">About</a></li>'
    '<li><a href="contact.html" class="nav-cta">Get Started</a></li>'
    '</ul>'
    '<button class="nav-burger" onclick="toggleMobNav()" aria-label="Menu">'
    '<span></span><span></span><span></span>'
    '</button>'
    '</nav>'
    '<div class="mob-nav" id="mobNav">'
    '<a href="work.html" onclick="toggleMobNav()">Our Work</a>'
    '<a href="pricing.html" onclick="toggleMobNav()">Pricing</a>'
    '<a href="about.html" onclick="toggleMobNav()">About</a>'
    '<a href="contact.html" class="mnav-cta">Get Started</a>'
    '</div>'
)

LOADER = (
    '<div id="loader">'
    '<div class="l-glow"></div>'
    '<div class="l-glow2"></div>'
    '<div class="l-half l-top"></div>'
    '<div class="l-half l-bot"></div>'
    '<div class="l-center">'
    '<div class="l-logo">'
    '<span>K</span><span>R</span><span>Y</span><span>S</span><span>O</span><span>N</span>'
    '</div>'
    '<div class="l-sub">Web Design for Health &amp; Wellness</div>'
    '<div class="l-bar" id="lBar"></div>'
    '</div>'
    '</div>'
)

FOOTER = (
    '<footer>'
    '<div class="footer-inner">'
    '<div class="footer-top">'
    '<div class="footer-brand">'
    '<div class="f-logo">Kryson</div>'
    '<p>We build elite websites and digital systems for gyms, saunas, yoga studios, and wellness centres across Ireland.</p>'
    '</div>'
    '<div class="footer-col">'
    '<h4>Pages</h4>'
    '<a href="index.html">Home</a>'
    '<a href="work.html">Our Work</a>'
    '<a href="pricing.html">Pricing</a>'
    '<a href="about.html">About</a>'
    '<a href="contact.html">Contact</a>'
    '</div>'
    '<div class="footer-col">'
    '<h4>Get in Touch</h4>'
    '<a href="mailto:kyle@krysongroup.com">kyle@krysongroup.com</a>'
    '<a href="contact.html">Start a Project</a>'
    '</div>'
    '</div>'
    '<div class="footer-bottom">'
    '<div class="footer-copy">&copy; 2025 Kryson. All rights reserved.</div>'
    '<div class="footer-ie">&#127470;&#127466; Based in Ireland</div>'
    '</div>'
    '</div>'
    '</footer>'
)

CONTACT_MODAL = (
    '<div id="cmodal" onclick="if(event.target===this)closeModal()">'
    '<div class="cm-box">'
    '<div class="cm-head">'
    '<div>'
    '<div class="cm-title">Let&#39;s Build Your Site</div>'
    '<div class="cm-sub">Tell us about your business</div>'
    '</div>'
    '<button class="cm-close" onclick="closeModal()">&#215;</button>'
    '</div>'
    '<div id="cm-form">'
    '<div class="cm-body">'
    '<div class="cm-2col">'
    '<div class="cm-field"><label>First Name</label><input type="text" id="cmFirst" placeholder="Ciara" required></div>'
    '<div class="cm-field"><label>Last Name</label><input type="text" id="cmLast" placeholder="Murphy" required></div>'
    '</div>'
    '<div class="cm-field"><label>Email</label><input type="email" id="cmEmail" placeholder="you@yourbusiness.ie" required></div>'
    '<div class="cm-field"><label>Phone</label><input type="tel" id="cmPhone" placeholder="+353 87 000 0000" required></div>'
    '<div class="cm-field"><label>Business Type</label>'
    '<select id="cmBiz">'
    '<option value="">Select your business...</option>'
    '<option>Gym / Fitness Centre</option>'
    '<option>Sauna / Wellness Centre</option>'
    '<option>Yoga Studio</option>'
    '<option>Pilates Studio</option>'
    '<option>Spinning / Cycling Studio</option>'
    '<option>Personal Trainer</option>'
    '<option>Other Health &amp; Wellness</option>'
    '</select>'
    '</div>'
    '<div class="cm-field"><label>Package Interested In</label>'
    '<select id="cmPackage">'
    '<option value="">Select package...</option>'
    '<option>Starter &#8212; &#8364;497</option>'
    '<option>Growth &#8212; &#8364;997</option>'
    '<option>Complete &#8212; &#8364;1,497</option>'
    '<option>Not sure yet</option>'
    '</select>'
    '</div>'
    '<button class="cm-submit" onclick="submitContact()">Send Enquiry &rarr;</button>'
    '</div>'
    '</div>'
    '<div id="cm-sending"><div class="cm-spin"></div><p style="color:var(--w30);font-size:13px">Sending...</p></div>'
    '<div id="cm-success"><div class="cm-ok">&#127881;</div><h3>You&#39;re on the list!</h3><p style="color:var(--w30);font-size:13px">We&#39;ll be in touch within 24 hours.</p></div>'
    '</div>'
    '</div>'
)

MOB_CTA = (
    '<div class="mob-cta-bar" id="mobCta">'
    '<button class="btn btn-grad" onclick="openModal()">Get a Free Quote &rarr;</button>'
    '</div>'
)

def shared_js():
    return (
        r"""<script>
function toggleMobNav(){var n=document.getElementById('mobNav');n.classList.toggle('open');}
function openModal(){document.getElementById('cmodal').classList.add('open');document.body.style.overflow='hidden';}
function closeModal(){document.getElementById('cmodal').classList.remove('open');document.body.style.overflow='';}
function submitContact(){
  var first=document.getElementById('cmFirst').value.trim();
  var email=document.getElementById('cmEmail').value.trim();
  var phone=document.getElementById('cmPhone').value.trim();
  if(!first||!email||!phone){alert('Please fill in all required fields.');return;}
  document.getElementById('cm-form').style.display='none';
  document.getElementById('cm-sending').style.display='block';
  var last=document.getElementById('cmLast').value.trim();
  var biz=document.getElementById('cmBiz').value;
  var pkg=document.getElementById('cmPackage').value;
  var payload={firstName:first,lastName:last,email:email,phone:phone,businessType:biz,package:pkg,submittedAt:new Date().toISOString()};
  var url='""" + APPS_SCRIPT_URL + r"""';
  try{fetch(url,{method:'POST',mode:'no-cors',body:JSON.stringify(payload)});}catch(err){}
  setTimeout(function(){document.getElementById('cm-sending').style.display='none';document.getElementById('cm-success').style.display='block';},700);
}
(function(){
  var els=document.querySelectorAll('.reveal,.reveal-l,.reveal-r');
  if(!('IntersectionObserver' in window)){els.forEach(function(el){el.classList.add('vis');});return;}
  var obs=new IntersectionObserver(function(entries){entries.forEach(function(e){if(e.isIntersecting){e.target.classList.add('vis');obs.unobserve(e.target);}});},{threshold:0.1});
  els.forEach(function(el){obs.observe(el);});
})();
(function(){
  var b=document.getElementById('mobCta');if(!b)return;
  var shown=false;
  window.addEventListener('scroll',function(){var s=window.pageYOffset>320;if(s!==shown){shown=s;b.classList.toggle('vis',s);document.body.classList.toggle('mob-bar-up',s);}},{passive:true});
})();
(function(){
  var loader=document.getElementById('loader');if(!loader)return;
  var letters=loader.querySelectorAll('.l-logo span');
  var bar=document.getElementById('lBar');
  var sub=loader.querySelector('.l-sub');
  letters.forEach(function(l,i){setTimeout(function(){l.style.opacity='1';l.style.transform='translateY(0)';},i*80+200);});
  setTimeout(function(){sub.style.opacity='1';},700);
  setTimeout(function(){bar.style.width='200px';},800);
  setTimeout(function(){loader.classList.add('split-ready');},1800);
  setTimeout(function(){loader.classList.add('exit');},2200);
  setTimeout(function(){loader.classList.add('gone');document.body.style.overflow='';},3100);
  document.body.style.overflow='hidden';
})();
document.querySelectorAll('.faq-q').forEach(function(q){
  q.addEventListener('click',function(){
    var item=this.parentElement;var isOpen=item.classList.contains('open');
    document.querySelectorAll('.faq-item').forEach(function(i){i.classList.remove('open');});
    if(!isOpen)item.classList.add('open');
  });
});
</script>"""
    )

def page_head(title, desc):
    return (
        '<!DOCTYPE html>'
        '<html lang="en">'
        '<head>'
        '<meta charset="UTF-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>' + title + ' | Kryson</title>'
        '<meta name="description" content="' + desc + '">'
        '<meta property="og:title" content="' + title + ' | Kryson">'
        '<meta property="og:description" content="' + desc + '">'
        '<link rel="stylesheet" href="styles.css">'
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '</head>'
        '<body>'
    )

def page_foot():
    return (
        FOOTER +
        CONTACT_MODAL +
        MOB_CTA +
        shared_js() +
        '</body></html>'
    )

# ============================================================
# MOCKUP COMPONENT
# ============================================================

def mockup(url_text):
    return (
        '<div class="mockup">'
        '<div class="mockup-bar">'
        '<div class="mockup-dot m-red"></div>'
        '<div class="mockup-dot m-yellow"></div>'
        '<div class="mockup-dot m-green"></div>'
        '<div class="mockup-url">' + url_text + '</div>'
        '</div>'
        '<div class="mockup-body">'
        '<div class="mb-hero"><div class="mb-logo">PIKENHOT</div></div>'
        '<div class="mb-cards"><div class="mb-card"></div><div class="mb-card"></div><div class="mb-card"></div></div>'
        '<div class="mb-row w85"></div>'
        '<div class="mb-row w70"></div>'
        '<div class="mb-row w50"></div>'
        '<div class="mb-pill"></div>'
        '</div>'
        '</div>'
    )

# ============================================================
# INDEX PAGE
# ============================================================

def build_index():
    return (
        page_head('Web Design for Irish Health &amp; Wellness Businesses',
                  'Kryson builds elite websites and digital systems for Irish gyms, saunas, yoga studios and wellness centres. Starter from 497.') +
        LOADER + NAV +

        '<section id="hero">'
        '<div class="hero-bg"></div>'
        '<div class="hero-grid"></div>'
        '<div class="hero-inner">'
        '<div class="hero-tag"><div class="hero-dot"></div>Built for Irish Health &amp; Wellness</div>'
        '<h1 class="hero-h1">Your studio is elite.<br><span class="gt">Your website</span><br>should be too.</h1>'
        '<p class="hero-sub">We build stunning websites and full business systems for gyms, saunas, yoga studios, and wellness centres across Ireland. From a sleek 5-page site to a complete member portal &mdash; we do it all.</p>'
        '<div class="hero-pills">'
        '<div class="hero-pill">&#127947; Gyms</div>'
        '<div class="hero-pill">&#128293; Saunas</div>'
        '<div class="hero-pill">&#129482; Yoga Studios</div>'
        '<div class="hero-pill">&#128692; Spinning</div>'
        '<div class="hero-pill">&#129340; Pilates</div>'
        '<div class="hero-pill">&#128170; Personal Trainers</div>'
        '</div>'
        '<div class="hero-btns">'
        '<button class="btn btn-grad" onclick="openModal()">Get a Free Quote &rarr;</button>'
        '<a href="work.html" class="btn btn-outline">See Our Work</a>'
        '</div>'
        '</div>'
        '<div class="hero-scroll"><div class="hero-scroll-line"></div>Scroll</div>'
        '</section>'

        '<section id="for">'
        '<div class="wrap">'
        '<div class="reveal">'
        '<div class="section-tag">Who We Build For</div>'
        '<h2 class="section-title">If you&#39;re in the wellness space,<br>we&#39;re your team.</h2>'
        '<p class="section-sub">We specialise exclusively in health and wellness businesses. We know your industry, your customers, and what converts.</p>'
        '</div>'
        '<div class="for-grid">'
        '<div class="for-card reveal"><span class="for-icon">&#127947;</span><div class="for-name">Gyms &amp; Fitness</div><div class="for-desc">Class schedules, memberships, online sign-ups</div></div>'
        '<div class="for-card reveal"><span class="for-icon">&#128293;</span><div class="for-name">Saunas &amp; Spas</div><div class="for-desc">Booking systems, session management, gift cards</div></div>'
        '<div class="for-card reveal"><span class="for-icon">&#129482;</span><div class="for-name">Yoga Studios</div><div class="for-desc">Class timetables, drop-ins, memberships</div></div>'
        '<div class="for-card reveal"><span class="for-icon">&#128692;</span><div class="for-name">Spinning Studios</div><div class="for-desc">Bike reservations, package bundles, leaderboards</div></div>'
        '<div class="for-card reveal"><span class="for-icon">&#129340;</span><div class="for-name">Pilates Studios</div><div class="for-desc">Reformer bookings, waitlists, new client flows</div></div>'
        '<div class="for-card reveal"><span class="for-icon">&#128170;</span><div class="for-name">Personal Trainers</div><div class="for-desc">Session bookings, client portals, payment links</div></div>'
        '</div>'
        '</div>'
        '</section>'

        '<section id="why">'
        '<div class="wrap">'
        '<div class="reveal">'
        '<div class="section-tag">Why Kryson</div>'
        '<h2 class="section-title">Not a template.<br><span class="gt">A proper system.</span></h2>'
        '<p class="section-sub">We don&#39;t use Wix. We don&#39;t use cookie-cutter builders. Every site we build is custom-designed and built to work as hard as you do.</p>'
        '</div>'
        '<div class="why-grid">'
        '<div class="why-features reveal-l">'
        '<div class="why-feat"><div class="why-feat-icon ic-purple">&#127775;</div><div><div class="why-feat-h">Elite Design</div><div class="why-feat-p">Animations, gradients, and layouts your competitors won&#39;t have. Built to impress from the first second.</div></div></div>'
        '<div class="why-feat"><div class="why-feat-icon ic-cyan">&#128241;</div><div><div class="why-feat-h">Mobile First</div><div class="why-feat-p">Most of your customers find you on their phone. We build mobile experiences that convert.</div></div></div>'
        '<div class="why-feat"><div class="why-feat-icon ic-lime">&#128269;</div><div><div class="why-feat-h">Local SEO</div><div class="why-feat-p">We optimise so you rank when people search "gym near me" or "yoga Dublin". Real local customers.</div></div></div>'
        '<div class="why-feat"><div class="why-feat-icon ic-pink">&#128176;</div><div><div class="why-feat-h">Payments &amp; Bookings</div><div class="why-feat-p">Take payments, manage bookings, and run your business from one place. No third-party logins.</div></div></div>'
        '<div class="why-feat"><div class="why-feat-icon ic-orange">&#127470;&#127466;</div><div><div class="why-feat-h">Based in Ireland</div><div class="why-feat-p">We understand the Irish market. Euro pricing, Irish business context, always available on the phone.</div></div></div>'
        '</div>'
        '<div class="why-visual reveal-r">'
        '<div class="why-vis-gradient"></div>'
        '<div class="why-stat-grid">'
        '<div class="why-stat-card"><div class="wsc-num">5&#43;</div><div class="wsc-label">Years building for wellness</div></div>'
        '<div class="why-stat-card"><div class="wsc-num">&#8364;497</div><div class="wsc-label">Starting price</div></div>'
        '<div class="why-stat-card"><div class="wsc-num">7 days</div><div class="wsc-label">Starter delivery</div></div>'
        '<div class="why-stat-card"><div class="wsc-num">100&#37;</div><div class="wsc-label">Custom built</div></div>'
        '</div>'
        '</div>'
        '</div>'
        '</div>'
        '</section>'

        '<section id="case-preview">'
        '<div class="wrap">'
        '<div class="reveal"><div class="section-tag">Featured Project</div>'
        '<h2 class="section-title">We built the digital backbone<br>of <span class="gt">pikenhot.ie</span></h2>'
        '</div>'
        '</div>'
        '<div class="wrap" style="margin-top:48px">'
        '<div class="cs-wrap reveal">'
        '<div class="cs-content">'
        '<div class="cs-logo-text"><span class="gt">PIKENHOT.IE</span></div>'
        '<div class="cs-url">pikenhot.ie &mdash; Irish Gym &amp; Sauna Centre</div>'
        '<div class="cs-badges"><span class="cs-badge">Website</span><span class="cs-badge">Member Portal</span><span class="cs-badge">CRM</span><span class="cs-badge">Payments</span><span class="cs-badge">Staff Roster</span></div>'
        '<h3 class="cs-h">A full website, member portal, and business backend &mdash; built from scratch.</h3>'
        '<p class="cs-p">Pikenhot needed more than a website. We built them a complete digital infrastructure: a custom-designed site, a member portal where customers manage their own memberships, and an admin CRM tracking payments, transactions, staff rosters, opening hours, and reviews.</p>'
        '<div class="cs-stats">'
        '<div><div class="cs-stat-n">&#8364;1,497</div><div class="cs-stat-l">Complete package</div></div>'
        '<div><div class="cs-stat-n">100&#37;</div><div class="cs-stat-l">Custom built</div></div>'
        '<div><div class="cs-stat-n">3 wk</div><div class="cs-stat-l">Delivered</div></div>'
        '</div>'
        '<a href="work.html" class="btn btn-grad">See Full Case Study &rarr;</a>'
        '</div>'
        '<div class="cs-visual">' + mockup('pikenhot.ie') + '</div>'
        '</div>'
        '</div>'
        '</section>'

        '<section id="pricing-preview">'
        '<div class="wrap">'
        '<div class="reveal"><div class="section-tag">Pricing</div>'
        '<h2 class="section-title">Transparent pricing.<br><span class="gt">No surprises.</span></h2>'
        '<p class="section-sub">Three tiers to match where your business is right now. All include custom design, mobile-first build, and full handover.</p>'
        '</div>'
        '<div class="price-grid">'

        '<div class="price-card reveal">'
        '<div class="price-tier">Tier 01</div>'
        '<div class="price-name">Starter</div>'
        '<div class="price-amount"><span class="gt">&#8364;497</span></div>'
        '<div class="price-period">One-time payment</div>'
        '<div class="price-divider"></div>'
        '<ul class="price-features">'
        '<li class="price-feat"><span class="pf-check pf-purple">&#10003;</span>Custom website (up to 5 pages)</li>'
        '<li class="price-feat"><span class="pf-check pf-purple">&#10003;</span>Mobile responsive &amp; fast</li>'
        '<li class="price-feat"><span class="pf-check pf-purple">&#10003;</span>Google Business setup</li>'
        '<li class="price-feat"><span class="pf-check pf-purple">&#10003;</span>Basic local SEO</li>'
        '<li class="price-feat"><span class="pf-check pf-purple">&#10003;</span>Contact form</li>'
        '<li class="price-feat"><span class="pf-check pf-purple">&#10003;</span>Delivered in 7 days</li>'
        '</ul>'
        '<button class="btn btn-outline" onclick="openModal()" style="width:100%;justify-content:center">Get Started &rarr;</button>'
        '</div>'

        '<div class="price-card featured reveal">'
        '<div class="price-badge">Most Popular</div>'
        '<div class="price-tier">Tier 02</div>'
        '<div class="price-name">Growth</div>'
        '<div class="price-amount"><span class="gt">&#8364;997</span></div>'
        '<div class="price-period">One-time payment</div>'
        '<div class="price-divider"></div>'
        '<ul class="price-features">'
        '<li class="price-feat"><span class="pf-check pf-pink">&#10003;</span>Everything in Starter</li>'
        '<li class="price-feat"><span class="pf-check pf-pink">&#10003;</span>Online payments (Stripe)</li>'
        '<li class="price-feat"><span class="pf-check pf-pink">&#10003;</span>Class &amp; appointment booking</li>'
        '<li class="price-feat"><span class="pf-check pf-pink">&#10003;</span>Advanced local SEO</li>'
        '<li class="price-feat"><span class="pf-check pf-pink">&#10003;</span>Google Analytics 4</li>'
        '<li class="price-feat"><span class="pf-check pf-pink">&#10003;</span>Delivered in 14 days</li>'
        '</ul>'
        '<button class="btn btn-grad" onclick="openModal()" style="width:100%;justify-content:center">Get Started &rarr;</button>'
        '</div>'

        '<div class="price-card reveal">'
        '<div class="price-tier">Tier 03</div>'
        '<div class="price-name">Complete</div>'
        '<div class="price-amount"><span class="gt2">&#8364;1,497</span></div>'
        '<div class="price-period">One-time payment</div>'
        '<div class="price-divider"></div>'
        '<ul class="price-features">'
        '<li class="price-feat"><span class="pf-check pf-cyan">&#10003;</span>Everything in Growth</li>'
        '<li class="price-feat"><span class="pf-check pf-cyan">&#10003;</span>Member portal</li>'
        '<li class="price-feat"><span class="pf-check pf-cyan">&#10003;</span>Staff management &amp; roster</li>'
        '<li class="price-feat"><span class="pf-check pf-cyan">&#10003;</span>Transaction history &amp; CRM</li>'
        '<li class="price-feat"><span class="pf-check pf-cyan">&#10003;</span>Review management</li>'
        '<li class="price-feat"><span class="pf-check pf-cyan">&#10003;</span>Delivered in 21 days</li>'
        '</ul>'
        '<button class="btn btn-outline" onclick="openModal()" style="width:100%;justify-content:center">Get Started &rarr;</button>'
        '</div>'

        '</div>'
        '<div style="text-align:center;margin-top:40px" class="reveal">'
        '<a href="pricing.html" style="font-size:13px;color:var(--w30);text-decoration:none;letter-spacing:2px;text-transform:uppercase">See full pricing details &rarr;</a>'
        '</div>'
        '</div>'
        '</section>'

        '<section id="process">'
        '<div class="wrap">'
        '<div class="reveal"><div class="section-tag">How It Works</div>'
        '<h2 class="section-title">Live in <span class="gt">4 steps.</span></h2>'
        '</div>'
        '<div class="process-steps">'
        '<div class="process-step reveal"><div class="ps-circle"><div class="ps-n">01</div></div><div class="ps-h">Tell Us About Your Business</div><div class="ps-p">Fill in our quick form. We&#39;ll get back to you within 24 hours.</div></div>'
        '<div class="process-step reveal"><div class="ps-circle"><div class="ps-n">02</div></div><div class="ps-h">We Design &amp; Build</div><div class="ps-p">We handle everything &mdash; design, copy, development, integrations.</div></div>'
        '<div class="process-step reveal"><div class="ps-circle"><div class="ps-n">03</div></div><div class="ps-h">Review &amp; Approve</div><div class="ps-p">We send you a preview. You request any changes. We refine until right.</div></div>'
        '<div class="process-step reveal"><div class="ps-circle"><div class="ps-n">04</div></div><div class="ps-h">Go Live</div><div class="ps-p">We launch, connect your domain, and hand over everything. You&#39;re live.</div></div>'
        '</div>'
        '</div>'
        '</section>'

        '<section id="testimonials">'
        '<div class="wrap">'
        '<div class="reveal"><div class="section-tag">What Clients Say</div>'
        '<h2 class="section-title">Real results.<br><span class="gt">Real businesses.</span></h2>'
        '</div>'
        '<div class="testi-grid">'
        '<div class="testi-card reveal">'
        '<div class="testi-stars"><span class="star">&#9733;</span><span class="star">&#9733;</span><span class="star">&#9733;</span><span class="star">&#9733;</span><span class="star">&#9733;</span></div>'
        '<div class="testi-text">"The website Kryson built us looks absolutely incredible. Our members constantly comment on how easy it is to use. Bookings are up since launch."</div>'
        '<div class="testi-author"><div class="testi-avatar ta-1">S</div><div><div class="testi-name">Sean O&#39;Brien</div><div class="testi-biz">Evolve Fitness, Dublin</div></div></div>'
        '</div>'
        '<div class="testi-card reveal">'
        '<div class="testi-stars"><span class="star">&#9733;</span><span class="star">&#9733;</span><span class="star">&#9733;</span><span class="star">&#9733;</span><span class="star">&#9733;</span></div>'
        '<div class="testi-text">"We went with the Complete package and don&#39;t regret it. Members can log in, manage subscriptions, and it looks unreal. Worth every cent."</div>'
        '<div class="testi-author"><div class="testi-avatar ta-2">A</div><div><div class="testi-name">Aoife Kelly</div><div class="testi-biz">Urban Sauna, Cork</div></div></div>'
        '</div>'
        '<div class="testi-card reveal">'
        '<div class="testi-stars"><span class="star">&#9733;</span><span class="star">&#9733;</span><span class="star">&#9733;</span><span class="star">&#9733;</span><span class="star">&#9733;</span></div>'
        '<div class="testi-text">"I was getting zero enquiries from my old site. Within two weeks of going live I had 12 new clients reach out. The SEO alone was worth it."</div>'
        '<div class="testi-author"><div class="testi-avatar ta-3">C</div><div><div class="testi-name">Ciara Brennan</div><div class="testi-biz">Personal Trainer, Galway</div></div></div>'
        '</div>'
        '</div>'
        '</div>'
        '</section>'

        '<section class="cta-band">'
        '<div class="cta-band-bg"></div>'
        '<div class="cta-band-inner reveal">'
        '<h2>Ready to build something <span class="gt">elite?</span></h2>'
        '<p>Get a free quote in 24 hours. No commitment, no pressure. Just tell us about your business and we&#39;ll tell you exactly what we can build.</p>'
        '<div class="cta-btns">'
        '<button class="btn btn-grad" onclick="openModal()">Get a Free Quote &rarr;</button>'
        '<a href="work.html" class="btn btn-outline">See Our Work</a>'
        '</div>'
        '</div>'
        '</section>'

        + page_foot()
    )

# ============================================================
# PRICING PAGE
# ============================================================

def build_pricing():
    return (
        page_head('Pricing', 'Kryson web design pricing for Irish health and wellness businesses. Starter from 497, Growth 997, Complete 1497.') +
        NAV +

        '<div class="inner-hero-wrap"><div class="inner-bg"></div>'
        '<div class="inner-hero">'
        '<div class="section-tag reveal">Pricing</div>'
        '<h1 class="inner-h1 reveal">Simple, transparent<br><span class="gt">pricing.</span></h1>'
        '<p class="inner-sub reveal">One-time payments. No monthly fees. No hidden costs. A great website delivered fast.</p>'
        '</div>'
        '</div>'

        '<div class="page-body">'
        '<div class="pricing-cards-wrap">'

        '<div class="full-price-card reveal">'
        '<div class="fpc-tier">Tier 01</div>'
        '<div class="fpc-name">Starter</div>'
        '<div class="fpc-tagline">A stunning website that puts you on the map</div>'
        '<div class="fpc-price"><span class="gt">&#8364;497</span></div>'
        '<div class="fpc-note">One-time payment &bull; No monthly fees</div>'
        '<div class="fpc-divider"></div>'
        '<ul class="fpc-features">'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i1">&#10003;</span>Custom designed website (up to 5 pages)</li>'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i1">&#10003;</span>Home, About, Services, Gallery, Contact</li>'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i1">&#10003;</span>Fully mobile responsive</li>'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i1">&#10003;</span>Google Maps embedding</li>'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i1">&#10003;</span>Google Business Profile setup</li>'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i1">&#10003;</span>On-page SEO (titles, meta, keywords)</li>'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i1">&#10003;</span>Contact form with email delivery</li>'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i1">&#10003;</span>Social media links</li>'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i1">&#10003;</span>1 round of revisions</li>'
        '</ul>'
        '<div class="fpc-timeline">&#128336; Delivered in 7 days</div>'
        '<button class="btn btn-outline" onclick="openModal()" style="width:100%;justify-content:center">Get Started &rarr;</button>'
        '</div>'

        '<div class="full-price-card featured reveal">'
        '<div class="fpc-badge">Most Popular</div>'
        '<div class="fpc-tier">Tier 02</div>'
        '<div class="fpc-name">Growth</div>'
        '<div class="fpc-tagline">Take bookings and payments directly from your site</div>'
        '<div class="fpc-price"><span class="gt">&#8364;997</span></div>'
        '<div class="fpc-note">One-time payment &bull; No monthly fees</div>'
        '<div class="fpc-divider"></div>'
        '<ul class="fpc-features">'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i2">&#10003;</span>Everything in Starter</li>'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i2">&#10003;</span>Online payment processing (Stripe)</li>'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i2">&#10003;</span>Class &amp; appointment booking system</li>'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i2">&#10003;</span>Up to 8 pages</li>'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i2">&#10003;</span>Advanced local SEO</li>'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i2">&#10003;</span>Google Business optimisation</li>'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i2">&#10003;</span>Email capture &amp; basic automation</li>'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i2">&#10003;</span>Google Analytics 4 setup</li>'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i2">&#10003;</span>2 rounds of revisions</li>'
        '</ul>'
        '<div class="fpc-timeline">&#128336; Delivered in 14 days</div>'
        '<button class="btn btn-grad" onclick="openModal()" style="width:100%;justify-content:center">Get Started &rarr;</button>'
        '</div>'

        '<div class="full-price-card reveal">'
        '<div class="fpc-tier">Tier 03</div>'
        '<div class="fpc-name">Complete</div>'
        '<div class="fpc-tagline">Your entire business infrastructure, online</div>'
        '<div class="fpc-price"><span class="gt2">&#8364;1,497</span></div>'
        '<div class="fpc-note">One-time payment &bull; No monthly fees</div>'
        '<div class="fpc-divider"></div>'
        '<ul class="fpc-features">'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i3">&#10003;</span>Everything in Growth</li>'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i3">&#10003;</span>Member portal (self-manage accounts)</li>'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i3">&#10003;</span>Full admin CRM dashboard</li>'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i3">&#10003;</span>Staff management &amp; roster system</li>'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i3">&#10003;</span>Transaction &amp; payment history</li>'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i3">&#10003;</span>Review management &amp; display</li>'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i3">&#10003;</span>Opening hours management</li>'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i3">&#10003;</span>Unlimited pages</li>'
        '<li class="fpc-feat"><span class="fpc-icon fpc-i3">&#10003;</span>3 rounds of revisions</li>'
        '</ul>'
        '<div class="fpc-timeline">&#128336; Delivered in 21 days</div>'
        '<button class="btn btn-outline" onclick="openModal()" style="width:100%;justify-content:center">Get Started &rarr;</button>'
        '</div>'

        '</div>'

        '<div style="text-align:center;padding:0 0 80px" class="reveal">'
        '<p style="color:var(--w30);font-size:14px;margin-bottom:20px">Not sure which package is right for you?</p>'
        '<button class="btn btn-grad" onclick="openModal()">Get a Free Consultation &rarr;</button>'
        '</div>'

        '<div class="faq-section reveal">'
        '<h2>Frequently Asked <span class="gt">Questions</span></h2>'
        '<div class="faq-item"><div class="faq-q">Do I own the website after it&#39;s built? <span class="faq-icon">+</span></div><div class="faq-a">Yes, completely. Once built and paid for, the website is 100% yours. We hand over all code, hosting credentials, and domain access. No lock-in.</div></div>'
        '<div class="faq-item"><div class="faq-q">Are there any monthly fees? <span class="faq-icon">+</span></div><div class="faq-a">Our build fee is one-time. The only ongoing costs are your hosting (typically &#8364;5&#8211;&#8364;15/month) and your domain (typically &#8364;10&#8211;&#8364;15/year) &mdash; both of which you control directly. We don&#39;t add any markup.</div></div>'
        '<div class="faq-item"><div class="faq-q">What do you need from me to get started? <span class="faq-icon">+</span></div><div class="faq-a">Just your logo, photos of your space, and a quick chat about your business. We handle the copy, layout, and design. If you don&#39;t have professional photos we can advise on that too.</div></div>'
        '<div class="faq-item"><div class="faq-q">Can I upgrade my package later? <span class="faq-icon">+</span></div><div class="faq-a">Yes. Many clients start on Starter or Growth and upgrade to Complete when they&#39;re ready. We offer upgrade pricing so you only pay the difference.</div></div>'
        '<div class="faq-item"><div class="faq-q">What&#39;s included in local SEO? <span class="faq-icon">+</span></div><div class="faq-a">We set up and optimise your Google Business Profile, add schema markup, optimise page titles and meta descriptions for local terms like "yoga studio Dublin", and submit to key directories.</div></div>'
        '<div class="faq-item"><div class="faq-q">Do you build for businesses outside Ireland? <span class="faq-icon">+</span></div><div class="faq-a">Our focus is Ireland but we take UK and international projects on a case-by-case basis. Get in touch and we&#39;ll let you know if we can help.</div></div>'
        '</div>'

        '</div>'

        '<section class="cta-band"><div class="cta-band-bg"></div>'
        '<div class="cta-band-inner reveal">'
        '<h2>Ready to get <span class="gt">started?</span></h2>'
        '<p>Fill in our quick form and we&#39;ll get back to you within 24 hours with a clear proposal.</p>'
        '<div class="cta-btns"><button class="btn btn-grad" onclick="openModal()">Get a Free Quote &rarr;</button><a href="contact.html" class="btn btn-outline">Contact Us</a></div>'
        '</div></section>'

        + page_foot()
    )

# ============================================================
# WORK PAGE
# ============================================================

def build_work():
    return (
        page_head('Our Work', 'See what Kryson has built for Irish health and wellness businesses. Websites, member portals, and business systems.') +
        NAV +

        '<div class="inner-hero-wrap" style="background:radial-gradient(ellipse 60% 60% at 50% 0%,rgba(0,207,255,0.12),transparent),var(--bg)">'
        '<div class="inner-hero" style="text-align:center;max-width:760px;margin:0 auto">'
        '<div class="section-tag reveal">Our Work</div>'
        '<h1 class="inner-h1 reveal">Built different.<br><span class="gt">Built for wellness.</span></h1>'
        '<p class="inner-sub reveal" style="max-width:100%">Every project is custom. Here&#39;s what we&#39;ve built for health and wellness businesses across Ireland.</p>'
        '</div>'
        '</div>'

        '<div class="page-body">'

        '<div class="case-card reveal">'
        '<div class="case-info">'
        '<div class="case-tag">Complete Package &mdash; &#8364;1,497</div>'
        '<h2 class="case-h"><span class="gt">Pikenhot</span> &mdash; Gym &amp; Sauna Centre</h2>'
        '<p class="case-p">Pikenhot needed more than a website. We built them a complete digital infrastructure: a custom-designed public site, a member portal where customers manage their own memberships, and a full admin CRM behind the scenes &mdash; tracking payments, staff, opening hours, and reviews.</p>'
        '<div class="case-feats">'
        '<span class="case-feat">Custom Website</span>'
        '<span class="case-feat">Member Portal</span>'
        '<span class="case-feat">Admin CRM</span>'
        '<span class="case-feat">Stripe Payments</span>'
        '<span class="case-feat">Staff Roster</span>'
        '<span class="case-feat">Opening Hours</span>'
        '<span class="case-feat">Review Management</span>'
        '<span class="case-feat">Transaction History</span>'
        '</div>'
        '<div class="case-outcome">&#127381; Live at pikenhot.ie</div>'
        '</div>'
        '<div class="case-visual">' + mockup('pikenhot.ie') + '</div>'
        '</div>'

        '<div class="reveal" style="margin-top:60px;margin-bottom:60px">'
        '<h3 style="font-size:clamp(22px,3vw,30px);font-weight:900;margin-bottom:8px">What we built for Pikenhot</h3>'
        '<p style="color:var(--w30);font-size:14px;margin-bottom:36px">A breakdown of every system delivered</p>'
        '<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:20px">'
        '<div class="av-card"><div class="av-icon">&#127760;</div><div class="av-h">Public Website</div><div class="av-p">Fully custom-designed multi-page site. Gym info, sauna sessions, facilities, pricing, contact. Animated, mobile-first, and fast.</div></div>'
        '<div class="av-card"><div class="av-icon">&#128100;</div><div class="av-h">Member Portal</div><div class="av-p">Members log in to view membership status, manage subscriptions, see booking history, and update payment details &mdash; all self-service.</div></div>'
        '<div class="av-card"><div class="av-icon">&#128176;</div><div class="av-h">Payment Processing</div><div class="av-p">Stripe integration for membership payments, one-off session purchases, and recurring billing. Full transaction history tracked in the admin.</div></div>'
        '<div class="av-card"><div class="av-icon">&#128101;</div><div class="av-h">Staff Roster</div><div class="av-p">Admin dashboard for managing staff shifts and rosters. Who&#39;s in, who&#39;s off, all in one place &mdash; no spreadsheets needed.</div></div>'
        '<div class="av-card"><div class="av-icon">&#128336;</div><div class="av-h">Opening Hours</div><div class="av-p">Dynamic hours management. Update your hours from the admin and they reflect on the public site in real time.</div></div>'
        '<div class="av-card"><div class="av-icon">&#11088;</div><div class="av-h">Review Management</div><div class="av-p">Collect and display reviews. Admin controls which reviews are shown publicly. Builds trust automatically.</div></div>'
        '</div>'
        '</div>'

        '<div class="reveal" style="text-align:center;padding:60px 0;border-top:1px solid var(--w08)">'
        '<p style="font-size:11px;letter-spacing:4px;text-transform:uppercase;color:var(--w30);margin-bottom:16px">More Projects</p>'
        '<h3 style="font-size:clamp(24px,4vw,40px);font-weight:900;margin-bottom:16px">Your business<br>could be next.</h3>'
        '<p style="color:var(--w30);font-size:15px;margin-bottom:36px;max-width:480px;margin-left:auto;margin-right:auto">We take on a limited number of new projects each month. Get in touch to check availability.</p>'
        '<button class="btn btn-grad" onclick="openModal()">Start Your Project &rarr;</button>'
        '</div>'

        '</div>'

        '<section class="cta-band"><div class="cta-band-bg"></div>'
        '<div class="cta-band-inner reveal">'
        '<h2>Want to see what we&#39;d<br>build for <span class="gt">you?</span></h2>'
        '<p>Get a free quote and a custom proposal in 24 hours.</p>'
        '<div class="cta-btns"><button class="btn btn-grad" onclick="openModal()">Get a Free Quote &rarr;</button><a href="pricing.html" class="btn btn-outline">View Pricing</a></div>'
        '</div></section>'

        + page_foot()
    )

# ============================================================
# ABOUT PAGE
# ============================================================

def build_about():
    return (
        page_head('About', 'Kryson is an Irish web design agency specialising in health and wellness businesses. Gyms, saunas, yoga studios, and more.') +
        NAV +

        '<div class="inner-hero-wrap" style="background:radial-gradient(ellipse 50% 50% at 80% 30%,rgba(168,255,62,0.1),transparent),radial-gradient(ellipse 50% 50% at 20% 70%,rgba(255,34,119,0.1),transparent),var(--bg)">'
        '<div class="inner-hero">'
        '<div class="section-tag reveal">About Kryson</div>'
        '<h1 class="inner-h1 reveal">Built by someone who<br>gets <span class="gt">your industry.</span></h1>'
        '<p class="inner-sub reveal">We don&#39;t build websites for everyone. We build them exclusively for health and wellness businesses &mdash; because that focus means better results for you.</p>'
        '</div>'
        '</div>'

        '<div class="page-body">'
        '<div class="about-grid">'

        '<div class="about-text reveal-l">'
        '<p>Kryson was born from a simple observation: most health and wellness businesses in Ireland have outdated websites that don&#39;t do them justice.</p>'
        '<p>We started by building a complete digital infrastructure for <strong>Pikenhot</strong> &mdash; a gym and sauna centre that needed a public website, a member portal, payment processing, staff management, review systems, and more. We built it all from scratch.</p>'
        '<p>The result was a business that runs more of its operations online, with members self-managing their accounts and the owner spending less time on admin. That&#39;s the result we want to replicate for every client.</p>'
        '<p>We focus exclusively on the health and wellness sector because knowing your industry means we ask the right questions, know what features matter, and know what converts your customers.</p>'
        '<p>We&#39;re based in Ireland, we price in euro, and we&#39;re available by phone. When you work with Kryson, you&#39;re working with someone who actually cares about the result.</p>'
        '</div>'

        '<div class="reveal-r">'
        '<div class="av-card"><div class="av-icon">&#127470;&#127466;</div><div class="av-h">Ireland-Based</div><div class="av-p">We&#39;re based in Ireland. We understand Irish business, Irish customers, and the Irish market. Euro pricing, and we&#39;re available when you are.</div></div>'
        '<div class="av-card" style="margin-top:16px"><div class="av-icon">&#127775;</div><div class="av-h">Wellness Only</div><div class="av-p">We only take on health and wellness clients. Every feature we build and every design choice is informed by deep industry knowledge.</div></div>'
        '<div class="av-card" style="margin-top:16px"><div class="av-icon">&#128170;</div><div class="av-h">No Templates</div><div class="av-p">We don&#39;t use Wix, Squarespace, or template builders. Every site is custom-coded for faster load times, better SEO, and a design nobody else has.</div></div>'
        '<div class="av-card" style="margin-top:16px"><div class="av-icon">&#128295;</div><div class="av-h">Full Stack</div><div class="av-p">From design to backend, we do it all in-house. No outsourcing, no miscommunication &mdash; one team, one point of contact, one outcome.</div></div>'
        '</div>'

        '</div>'
        '</div>'

        '<section class="cta-band"><div class="cta-band-bg"></div>'
        '<div class="cta-band-inner reveal">'
        '<h2>Let&#39;s build something<br><span class="gt">great together.</span></h2>'
        '<p>Get in touch and we&#39;ll put together a free proposal for your business.</p>'
        '<div class="cta-btns"><button class="btn btn-grad" onclick="openModal()">Get a Free Quote &rarr;</button><a href="pricing.html" class="btn btn-outline">View Pricing</a></div>'
        '</div></section>'

        + page_foot()
    )

# ============================================================
# CONTACT PAGE
# ============================================================

def build_contact():
    contact_js = (
        '<script>'
        'function submitContactForm(){'
        'var first=document.getElementById("cfFirst").value.trim();'
        'var email=document.getElementById("cfEmail").value.trim();'
        'var phone=document.getElementById("cfPhone").value.trim();'
        'if(!first||!email||!phone){alert("Please fill in all required fields.");return;}'
        'document.getElementById("cf-form").style.display="none";'
        'document.getElementById("cf-sending").style.display="block";'
        'var last=document.getElementById("cfLast").value.trim();'
        'var biz=document.getElementById("cfBiz").value;'
        'var pkg=document.getElementById("cfPkg").value;'
        'var msg=document.getElementById("cfMsg").value.trim();'
        'var payload={firstName:first,lastName:last,email:email,phone:phone,businessType:biz,package:pkg,message:msg,submittedAt:new Date().toISOString()};'
        'var url=\'' + APPS_SCRIPT_URL + '\';'
        'try{fetch(url,{method:"POST",mode:"no-cors",body:JSON.stringify(payload)});}catch(err){}'
        'setTimeout(function(){document.getElementById("cf-sending").style.display="none";document.getElementById("cf-success").style.display="block";},700);}'
        '</script>'
    )

    return (
        page_head('Contact', 'Get in touch with Kryson to start your health and wellness website project. Free quote, 24-hour response.') +
        NAV +

        '<div class="inner-hero-wrap" style="background:radial-gradient(ellipse 50% 50% at 70% 30%,rgba(255,122,0,0.1),transparent),radial-gradient(ellipse 50% 50% at 30% 70%,rgba(255,34,119,0.1),transparent),var(--bg)">'
        '<div class="inner-hero">'
        '<div class="section-tag reveal">Get in Touch</div>'
        '<h1 class="inner-h1 reveal">Start your project.<br><span class="gt">Free quote.</span></h1>'
        '<p class="inner-sub reveal">Fill in the form and we&#39;ll get back to you within 24 hours with a clear proposal for your business.</p>'
        '</div>'
        '</div>'

        '<div class="page-body">'
        '<div class="contact-grid">'

        '<div class="reveal-l">'
        '<div class="ci-item"><div class="ci-icon">&#128205;</div><div><div class="ci-h">Based in Ireland</div><div class="ci-p">We work with businesses across Ireland. Dublin, Cork, Galway, Limerick &mdash; wherever you are, we can help.</div></div></div>'
        '<div class="ci-item"><div class="ci-icon">&#128336;</div><div><div class="ci-h">24-Hour Response</div><div class="ci-p">We reply to every enquiry within 24 hours on weekdays. Usually much faster.</div></div></div>'
        '<div class="ci-item"><div class="ci-icon">&#128176;</div><div><div class="ci-h">Free Quote</div><div class="ci-p">No commitment. We&#39;ll assess your needs and give you a clear proposal with no pressure.</div></div></div>'
        '<div class="ci-item"><div class="ci-icon">&#128140;</div><div><div class="ci-h">Email</div><div class="ci-p"><a href="mailto:kyle@krysongroup.com" style="color:var(--w60);text-decoration:none">kyle@krysongroup.com</a></div></div></div>'
        '</div>'

        '<div class="contact-form-box reveal-r">'
        '<div class="cf-title">Send Us a Message</div>'
        '<div class="cf-sub">We&#39;ll come back to you within 24 hours</div>'
        '<div id="cf-form">'
        '<div class="cf-2col"><div class="cf-field"><label>First Name *</label><input type="text" id="cfFirst" placeholder="Ciara" required></div><div class="cf-field"><label>Last Name</label><input type="text" id="cfLast" placeholder="Murphy"></div></div>'
        '<div class="cf-field"><label>Email *</label><input type="email" id="cfEmail" placeholder="you@yourbusiness.ie" required></div>'
        '<div class="cf-field"><label>Phone *</label><input type="tel" id="cfPhone" placeholder="+353 87 000 0000" required></div>'
        '<div class="cf-field"><label>Business Type</label><select id="cfBiz"><option value="">Select your business...</option><option>Gym / Fitness Centre</option><option>Sauna / Wellness Centre</option><option>Yoga Studio</option><option>Pilates Studio</option><option>Spinning / Cycling Studio</option><option>Personal Trainer</option><option>Other Health &amp; Wellness</option></select></div>'
        '<div class="cf-field"><label>Package Interested In</label><select id="cfPkg"><option value="">Select package...</option><option>Starter &#8212; &#8364;497</option><option>Growth &#8212; &#8364;997</option><option>Complete &#8212; &#8364;1,497</option><option>Not sure yet</option></select></div>'
        '<div class="cf-field"><label>Message</label><textarea id="cfMsg" placeholder="Tell us about your business and what you&#39;re looking for..."></textarea></div>'
        '<button class="cf-submit" onclick="submitContactForm()">Send Message &rarr;</button>'
        '</div>'
        '<div id="cf-sending"><div class="cf-spin"></div><p style="color:var(--w30);font-size:13px">Sending your message...</p></div>'
        '<div id="cf-success"><div class="cf-ok">&#127881;</div><h3>Message Received!</h3><p style="color:var(--w30);font-size:13px">We&#39;ll get back to you within 24 hours.</p></div>'
        '</div>'

        '</div>'
        '</div>'

        + contact_js
        + page_foot()
    )

# ============================================================
# BUILD ALL
# ============================================================

def main():
    pages = {
        'index.html': build_index(),
        'pricing.html': build_pricing(),
        'work.html': build_work(),
        'about.html': build_about(),
        'contact.html': build_contact(),
    }
    for filename, html in pages.items():
        path = os.path.join(BASE_DIR, filename)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print('Built: ' + filename)
    print('Done!')

if __name__ == '__main__':
    main()
