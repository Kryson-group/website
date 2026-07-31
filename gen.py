#!/usr/bin/env python3
# KRYSON -- Health & Wellness Web Design Agency (WHITE REDESIGN)
# gen.py: static site generator
# NO f-strings. NO apostrophes in single-quoted strings.
# Use &#39; for apostrophes, &euro; for euros.

import os

APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbwJdvzoi0NBXMrJGpiHKn3ylMkxagH3Rrt81_hyAsnT8JywbrZRLWKTdFez9BZ3b28c/exec'
# Replace these with your actual Stripe payment links from stripe.com/payment-links
STRIPE_497  = 'https://buy.stripe.com/cNi7sEgeh2Yq1qb0EYgw000'
STRIPE_997  = 'https://buy.stripe.com/8x228kfad2Yqfh173mgw001'
STRIPE_1497 = 'https://buy.stripe.com/00w9AM8LP8iK7Oz73mgw002'
SITE_URL = 'https://krysonlimited.com'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# SVG ICONS
# ============================================================

def icon(name, cls=''):
    extra = ' class="' + cls + '"' if cls else ''
    icons = {
        'star':     '<svg' + extra + ' viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>',
        'check':    '<svg' + extra + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>',
        'clock':    '<svg' + extra + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
        'map':      '<svg' + extra + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
        'mail':     '<svg' + extra + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>',
        'phone':    '<svg' + extra + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 12a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.6 1.18h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 8.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
        'star-award':'<svg' + extra + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="8" r="6"/><path d="M15.477 12.89L17 22l-5-3-5 3 1.523-9.11"/></svg>',
        'mobile':   '<svg' + extra + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>',
        'seo':      '<svg' + extra + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>',
        'payment':  '<svg' + extra + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"/><line x1="1" y1="10" x2="23" y2="10"/></svg>',
        'ireland':  '<svg' + extra + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 22s-8-4.5-8-11.8A8 8 0 0 1 12 2a8 8 0 0 1 8 8.2c0 7.3-8 11.8-8 11.8z"/></svg>',
        'dumbbell': '<svg' + extra + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M6.5 6.5h11M6.5 17.5h11M6.5 6.5v11M17.5 6.5v11M2 9h4M2 15h4M18 9h4M18 15h4"/></svg>',
        'flame':    '<svg' + extra + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>',
        'lotus':    '<svg' + extra + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 22V12M12 12c0-3.5-2-6.5-5-8 0 4.5 1.5 7 5 8M12 12c0-3.5 2-6.5 5-8 0 4.5-1.5 7-5 8M12 12c-4.5 0-7.5-2-9-5 3.5 0 6.5 1.5 9 5M12 12c4.5 0 7.5-2 9-5-3.5 0-6.5 1.5-9 5"/></svg>',
        'bike':     '<svg' + extra + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="18.5" cy="17.5" r="3.5"/><circle cx="5.5" cy="17.5" r="3.5"/><circle cx="15" cy="5" r="1"/><path d="M12 17.5V14l-3-3 4-3 2 3h2"/></svg>',
        'person':   '<svg' + extra + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
        'shield':   '<svg' + extra + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
        'wave':     '<svg' + extra + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M2 6c.6.5 1.2 1 2.5 1C7 7 7 5 9.5 5c2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2v11c-2.5 0-2.5 2-5 2-2.6 0-2.4-2-5-2C7 17 7 19 4.5 19c-1.3 0-1.9-.5-2.5-1"/></svg>',
        'golf':     '<svg' + extra + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><line x1="12" y1="2" x2="12" y2="15"/><path d="M12 2l7 4-7 4V2z"/><path d="M8 20c0-2.2 1.8-4 4-4s4 1.8 4 4"/><line x1="6" y1="22" x2="18" y2="22"/></svg>',
        'heart':    '<svg' + extra + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>',
        'leaf':     '<svg' + extra + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M6 3v12a6 6 0 0 0 6 6 6 6 0 0 0 6-6 6 6 0 0 0-6-6H3"/></svg>',
        'hand':     '<svg' + extra + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M18 11V6a2 2 0 0 0-2-2 2 2 0 0 0-2 2M14 10V4a2 2 0 0 0-2-2 2 2 0 0 0-2 2v2M10 10.5V6a2 2 0 0 0-2-2 2 2 0 0 0-2 2v8"/><path d="M18 11a2 2 0 1 1 4 0v3a8 8 0 0 1-8 8h-2c-2.8 0-4.5-.86-5.99-2.34l-3.6-3.6a2 2 0 0 1 2.83-2.82L7 15"/></svg>',
        'dance':    '<svg' + extra + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="4" r="2"/><path d="M15 9H9l-2 7h10L15 9z"/><path d="M9 16l-2 5M15 16l2 5M9 12l-2-2M15 12l2-2"/></svg>',
        'brain':    '<svg' + extra + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96-.46 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.24 2.5 2.5 0 0 1 1.44-4.14z"/><path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96-.46 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.24 2.5 2.5 0 0 0-1.44-4.14z"/></svg>',
        'rocket':   '<svg' + extra + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="M12 15l-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/></svg>',
    }
    return icons.get(name, '')

# ============================================================
# SEO / SCHEMA HELPERS
# ============================================================

def schema_org():
    return (
        '<script type="application/ld+json">'
        '{"@context":"https://schema.org","@graph":['
        '{"@type":"WebSite","@id":"' + SITE_URL + '/#website","url":"' + SITE_URL + '",'
        '"name":"Kryson","description":"Web Design for Health and Wellness Businesses in Ireland"},'
        '{"@type":"ProfessionalService","@id":"' + SITE_URL + '/#business",'
        '"name":"Kryson Web Design","url":"' + SITE_URL + '",'
        '"description":"Web design agency specialising in gyms, saunas, yoga studios and wellness businesses across Ireland.",'
        '"email":"kyle@krysongroup.com",'
        '"address":{"@type":"PostalAddress","addressCountry":"IE"},'
        '"areaServed":['
        '{"@type":"City","name":"Dublin"},'
        '{"@type":"City","name":"Cork"},'
        '{"@type":"City","name":"Galway"},'
        '{"@type":"City","name":"Limerick"},'
        '{"@type":"City","name":"Waterford"},'
        '{"@type":"City","name":"Kilkenny"},'
        '{"@type":"Country","name":"Ireland"}'
        '],'
        '"serviceType":["Web Design","Website Development","Local SEO","E-Commerce Development","Member Portal Development","Booking System Integration"],'
        '"priceRange":"&#8364;&#8364;",'
        '"knowsAbout":["Gym Website Design","Yoga Studio Websites","Wellness Business Websites","Health and Fitness Web Design"]'
        '}'
        ']}'
        '</script>'
    )

def page_head(title, desc, canonical='', extra_schema=''):
    can = canonical if canonical else SITE_URL + '/'
    return (
        '<!DOCTYPE html>'
        '<html lang="en-IE">'
        '<head>'
        '<meta charset="UTF-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>' + title + '</title>'
        '<meta name="description" content="' + desc + '">'
        '<link rel="canonical" href="' + can + '">'
        '<link rel="stylesheet" href="styles.css">'
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<meta name="robots" content="index, follow">'
        '<meta name="geo.region" content="IE">'
        '<meta name="geo.placename" content="Ireland">'
        '<meta property="og:type" content="website">'
        '<meta property="og:title" content="' + title + '">'
        '<meta property="og:description" content="' + desc + '">'
        '<meta property="og:url" content="' + can + '">'
        '<meta property="og:site_name" content="Kryson">'
        '<meta property="og:locale" content="en_IE">'
        '<meta name="twitter:card" content="summary_large_image">'
        '<meta name="twitter:title" content="' + title + '">'
        '<meta name="twitter:description" content="' + desc + '">'
        '<link rel="alternate" hreflang="en-IE" href="' + can + '">'
        '<link rel="alternate" hreflang="en" href="' + can + '">'
        + schema_org()
        + extra_schema
        + '</head><body>'
    )

# ============================================================
# SHARED COMPONENTS
# ============================================================

NAV = (
    '<nav>'
    '<a href="index.html" class="nav-logo">Kryson</a>'
    '<ul class="nav-links">'
    '<li><a href="work.html">Our Work</a></li>'
    '<li><a href="pricing.html">Pricing</a></li>'
    '<li><a href="insights.html">Insights</a></li>'
    '<li><a href="about.html">About</a></li>'
    '<li><a href="pricing.html" class="nav-cta">Buy Now</a></li>'
    '</ul>'
    '<button class="nav-burger" onclick="toggleMobNav()" aria-label="Menu">'
    '<span></span><span></span><span></span>'
    '</button>'
    '</nav>'
    '<div class="mob-nav" id="mobNav">'
    '<a href="work.html" onclick="toggleMobNav()">Our Work</a>'
    '<a href="pricing.html" onclick="toggleMobNav()">Pricing</a>'
    '<a href="insights.html" onclick="toggleMobNav()">Insights</a>'
    '<a href="about.html" onclick="toggleMobNav()">About</a>'
    '<a href="pricing.html" class="mnav-cta">Buy Now</a>'
    '</div>'
)

def loader():
    return (
        '<div id="loader">'
        '<div class="l-brand" id="lBrand">'
        '<span class="l-logo-text">Kryson</span>'
        '<div class="l-tagline">Web Design for Health &amp; Wellness</div>'
        '</div>'
        '<div class="l-laptop-wrap" id="lLaptop">'
        '<div class="l-laptop">'
        '<div class="l-screen-outer">'
        '<div class="l-screen" id="lScreen">'
        '<div class="l-screen-inner">'
        '<div class="ls-nav"><div class="ls-dots"><div class="ls-dot ls-d1"></div><div class="ls-dot ls-d2"></div><div class="ls-dot ls-d3"></div></div><div class="ls-url"></div></div>'
        '<div class="ls-hero"><div class="ls-hero-logo">KRYSON LIMITED</div><div class="ls-hero-sub"></div></div>'
        '<div class="ls-body">'
        '<div class="ls-row w80"></div><div class="ls-row w60"></div><div class="ls-row w70"></div>'
        '<div class="ls-cards"><div class="ls-card"></div><div class="ls-card"></div><div class="ls-card"></div></div>'
        '</div>'
        '</div>'
        '</div>'
        '</div>'
        '<div class="l-hinge"></div>'
        '<div class="l-base-inner"></div>'
        '<div class="l-base-foot"></div>'
        '</div>'
        '</div>'
        '</div>'
    )

FOOTER = (
    '<footer>'
    '<div class="footer-inner">'
    '<div class="footer-top">'
    '<div class="footer-brand">'
    '<div class="f-logo">Kryson</div>'
    '<p>Elite web design for gyms, saunas, yoga studios, and wellness businesses across Ireland. No templates. No lock-in. Just results.</p>'
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
    '<h4>Contact</h4>'
    '<a href="mailto:kyle@krysongroup.com">kyle@krysongroup.com</a>'
    '<a href="contact.html">Get a Free Quote</a>'
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
    '<div><div class="cm-title">Let&#39;s Build Your Site</div><div class="cm-sub">Free quote &mdash; reply within 24 hours</div></div>'
    '<button class="cm-close" onclick="closeModal()">&#215;</button>'
    '</div>'
    '<div id="cm-form">'
    '<div class="cm-body">'
    '<div class="cm-2col">'
    '<div class="cm-field"><label>First Name</label><input type="text" id="cmFirst" placeholder="Ciara" required></div>'
    '<div class="cm-field"><label>Last Name</label><input type="text" id="cmLast" placeholder="Murphy"></div>'
    '</div>'
    '<div class="cm-field"><label>Email</label><input type="email" id="cmEmail" placeholder="you@yourbusiness.ie" required></div>'
    '<div class="cm-field"><label>Phone</label><input type="tel" id="cmPhone" placeholder="+353 87 000 0000" required></div>'
    '<div class="cm-field"><label>Business Type</label>'
    '<select id="cmBiz">'
    '<option value="">Select your business...</option>'
    '<option>Gym / Fitness Centre</option><option>Sauna / Wellness Centre</option>'
    '<option>Yoga Studio</option><option>Pilates Studio</option>'
    '<option>Spinning / Cycling Studio</option><option>CrossFit Box</option>'
    '<option>Martial Arts (MMA / Boxing / BJJ)</option><option>Dance Studio</option>'
    '<option>Swimming School / Club</option><option>Golf Academy</option>'
    '<option>Physiotherapy / Sports Rehab</option><option>Holistic Therapy / Massage</option>'
    '<option>Nutritionist / Dietitian</option><option>Personal Trainer</option>'
    '<option>Other Health &amp; Wellness</option>'
    '</select>'
    '</div>'
    '<div class="cm-field"><label>Package</label>'
    '<select id="cmPackage">'
    '<option value="">Not sure yet</option>'
    '<option>Starter &mdash; &euro;497</option>'
    '<option>Growth &mdash; &euro;997</option>'
    '<option>Complete &mdash; &euro;1,497</option>'
    '</select>'
    '</div>'
    '<button class="cm-submit" onclick="submitContact()">Send Enquiry &rarr;</button>'
    '</div>'
    '</div>'
    '<div id="cm-sending"><div class="cm-spin"></div><p style="color:var(--text3);font-size:13px">Sending...</p></div>'
    '<div id="cm-success">'
    '<div class="cm-ok">&#10003;</div>'
    '<h3>Message received!</h3>'
    '<p style="color:var(--text3);font-size:13px;margin-bottom:16px">We&#39;ll be in touch within 24 hours to discuss your website.</p>'
    '<a href="https://calendly.com/kyle-krysongroup/kryson-limited-website-kick-off-call" target="_blank" rel="noopener" class="btn btn-grad" style="font-size:13px;justify-content:center">Schedule a Call Now &rarr;</a>'
    '</div>'
    '</div>'
    '</div>'
)

MOB_CTA = (
    '<div class="mob-cta-bar" id="mobCta">'
    '<button class="btn btn-grad" style="width:100%" onclick="openModal()">Get a Free Quote &rarr;</button>'
    '</div>'
)

def shared_js():
    return (
        r"""<script>
function toggleMobNav(){document.getElementById('mobNav').classList.toggle('open')}
function openModal(){document.getElementById('cmodal').classList.add('open');document.body.style.overflow='hidden'}
function closeModal(){document.getElementById('cmodal').classList.remove('open');document.body.style.overflow=''}
function submitContact(){
  var first=document.getElementById('cmFirst').value.trim();
  var email=document.getElementById('cmEmail').value.trim();
  var phone=document.getElementById('cmPhone').value.trim();
  if(!first||!email||!phone){alert('Please fill in your name, email, and phone.');return;}
  document.getElementById('cm-form').style.display='none';
  document.getElementById('cm-sending').style.display='block';
  var payload={firstName:first,lastName:document.getElementById('cmLast').value.trim(),email:email,phone:phone,
    businessType:document.getElementById('cmBiz').value,package:document.getElementById('cmPackage').value,
    submittedAt:new Date().toISOString()};
  """ + 'var url=\'' + APPS_SCRIPT_URL + '\';' + r"""
  try{fetch(url,{method:'POST',mode:'no-cors',body:JSON.stringify(payload)});}catch(e){}
  setTimeout(function(){document.getElementById('cm-sending').style.display='none';document.getElementById('cm-success').style.display='block';},700);
}
(function(){
  var els=document.querySelectorAll('.reveal,.reveal-l,.reveal-r');
  if(!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('vis')});return}
  var obs=new IntersectionObserver(function(entries){entries.forEach(function(e){if(e.isIntersecting){e.target.classList.add('vis');obs.unobserve(e.target)}})},{threshold:0.1});
  els.forEach(function(e){obs.observe(e)});
})();
(function(){
  var b=document.getElementById('mobCta');if(!b)return;var shown=false;
  window.addEventListener('scroll',function(){var s=window.pageYOffset>280;if(s!==shown){shown=s;b.classList.toggle('vis',s);document.body.classList.toggle('mob-bar-up',s)}},{passive:true});
})();
(function(){
  var loader=document.getElementById('loader');if(!loader)return;
  document.body.style.overflow='hidden';
  var brand=document.getElementById('lBrand');
  var laptop=document.getElementById('lLaptop');
  var screen=document.getElementById('lScreen');
  setTimeout(function(){brand.classList.add('show')},100);
  setTimeout(function(){laptop.classList.add('show')},700);
  setTimeout(function(){screen.classList.add('open')},1300);
  setTimeout(function(){laptop.classList.add('zoom')},2800);
  setTimeout(function(){loader.classList.add('fade')},3500);
  setTimeout(function(){loader.classList.add('gone');document.body.style.overflow=''},3900);
})();
document.querySelectorAll('.faq-q').forEach(function(q){
  q.addEventListener('click',function(){
    var item=this.parentElement;var open=item.classList.contains('open');
    document.querySelectorAll('.faq-item').forEach(function(i){i.classList.remove('open')});
    if(!open)item.classList.add('open');
  });
});
</script>"""
    )

def page_foot(include_contact_js=False):
    extra = ''
    if include_contact_js:
        extra = (
            '<script>'
            'function submitContactForm(){'
            'var first=document.getElementById("cfFirst").value.trim();'
            'var email=document.getElementById("cfEmail").value.trim();'
            'var phone=document.getElementById("cfPhone").value.trim();'
            'if(!first||!email||!phone){alert("Please fill in your name, email, and phone.");return;}'
            'document.getElementById("cf-form").style.display="none";'
            'document.getElementById("cf-sending").style.display="block";'
            'var payload={firstName:first,lastName:document.getElementById("cfLast").value.trim(),'
            'email:email,phone:phone,businessType:document.getElementById("cfBiz").value,'
            'package:document.getElementById("cfPkg").value,message:document.getElementById("cfMsg").value.trim(),'
            'submittedAt:new Date().toISOString()};'
            'var url=\'' + APPS_SCRIPT_URL + '\';'
            'try{fetch(url,{method:"POST",mode:"no-cors",body:JSON.stringify(payload)});}catch(e){}'
            'setTimeout(function(){document.getElementById("cf-sending").style.display="none";document.getElementById("cf-success").style.display="block";},700);}'
            '</script>'
        )
    return FOOTER + CONTACT_MODAL + MOB_CTA + shared_js() + extra + '</body></html>'

# ============================================================
# MOCKUP
# ============================================================

def browser_mockup(url_text='pikenhot.ie'):
    return (
        '<div class="mockup">'
        '<div class="mockup-bar">'
        '<div class="mockup-dots"><div class="mockup-dot m-r"></div><div class="mockup-dot m-y"></div><div class="mockup-dot m-g"></div></div>'
        '<div class="mockup-url">' + url_text + '</div>'
        '</div>'
        '<div class="mockup-body">'
        '<div class="mb-head"><div class="mb-logo-text">PIKENHOT</div></div>'
        '<div class="mb-content">'
        '<div class="mb-row w80"></div><div class="mb-row w60"></div><div class="mb-row w70"></div>'
        '<div class="mb-cards"><div class="mb-card"></div><div class="mb-card"></div><div class="mb-card"></div></div>'
        '</div>'
        '</div>'
        '</div>'
    )

# ============================================================
# CHECK ICON HELPER
# ============================================================

def check(colour_class):
    return '<span class="pf-check ' + colour_class + '">&#10003;</span>'

def fpc_check(colour_class):
    return '<span class="fpc-icon ' + colour_class + '">&#10003;</span>'

# ============================================================
# INDEX PAGE
# ============================================================

INDEX_SCHEMA = (
    '<script type="application/ld+json">'
    '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
    '{"@type":"Question","name":"How much does a gym website cost in Ireland?",'
    '"acceptedAnswer":{"@type":"Answer","text":"Kryson web design starts at &#8364;497 for a fully custom gym website with mobile-responsive design and basic SEO. Our Growth package at &#8364;997 includes online booking and payments."}},'
    '{"@type":"Question","name":"How long does it take to build a wellness website?",'
    '"acceptedAnswer":{"@type":"Answer","text":"Our Starter websites are delivered in 7 days. Growth packages take 14 days. Our Complete infrastructure package takes 21 days."}}'
    ']}'
    '</script>'
)

def build_index():
    return (
        page_head(
            'Web Design for Gyms, Yoga Studios &amp; Wellness Businesses in Ireland | Kryson',
            'Kryson builds professional websites for gyms, saunas, yoga studios, pilates and wellness businesses across Ireland. Custom design from &#8364;497. Dublin, Cork, Galway and nationwide.',
            SITE_URL + '/',
            INDEX_SCHEMA
        ) +
        loader() + NAV +

        # HERO
        '<section id="hero">'
        '<div class="hero-bg"></div>'
        '<div class="hero-inner">'
        '<div class="hero-left">'
        '<div class="hero-tag">'
        '<div class="hero-dot"></div>'
        'Ireland&#39;s Wellness Web Agency'
        '</div>'
        '<h1 class="hero-h1">'
        'Your studio is elite.<br>'
        '<span class="gt">Your website</span><br>'
        'should be too.'
        '</h1>'
        '<p class="hero-sub">'
        'We build professional websites and digital systems for gyms, saunas, yoga studios, and wellness businesses across Ireland. Custom-built from scratch. No templates, ever.'
        '</p>'
        '<div class="hero-btns">'
        '<a href="pricing.html" class="btn btn-grad">See Packages &amp; Buy &rarr;</a>'
        '<a href="work.html" class="btn btn-outline">See Our Work</a>'
        '</div>'
        '<div class="hero-trust">'
        '<div class="hero-trust-item"><div class="trust-check">&#10003;</div>Based in Ireland</div>'
        '<div class="hero-trust-item"><div class="trust-check">&#10003;</div>From &euro;497</div>'
        '<div class="hero-trust-item"><div class="trust-check">&#10003;</div>No monthly fees</div>'
        '</div>'
        '</div>'
        '<div class="hero-device">'
        '<div class="hero-browser">'
        '<div class="hb-bar">'
        '<div class="hb-dots"><div class="hb-dot hb-r"></div><div class="hb-dot hb-y"></div><div class="hb-dot hb-g"></div></div>'
        '<div class="hb-url">krysonlimited.com</div>'
        '</div>'
        '<div class="hb-body">'
        '<div class="hb-hero-section">'
        '<div class="hb-brand">KRYSON LIMITED</div>'
        '<div class="hb-nav-mock"></div>'
        '</div>'
        '<div class="hb-content">'
        '<div class="hb-row w85"></div>'
        '<div class="hb-row w75"></div>'
        '<div class="hb-row w55"></div>'
        '<div class="hb-row w40"></div>'
        '<div class="hb-cards"><div class="hb-card"></div><div class="hb-card"></div><div class="hb-card"></div></div>'
        '<div class="hb-btn"></div>'
        '</div>'
        '</div>'
        '</div>'
        '<div class="hero-badge">'
        '<div class="hbadge-icon">&#10003;</div>'
        '<div class="hbadge-text"><strong>krysonlimited.com</strong><span>Live &mdash; Complete Package</span></div>'
        '</div>'
        '<div class="hero-badge2">'
        '<div class="hb2-dot"></div>'
        '<div class="hb2-text">3 new bookings today</div>'
        '</div>'
        '</div>'
        '</div>'
        '</section>'

        # WHO WE BUILD FOR
        '<section id="for">'
        '<div class="wrap">'
        '<div class="reveal">'
        '<div class="section-tag">Who We Build For</div>'
        '<h2 class="section-title">Built exclusively for<br>health &amp; wellness.</h2>'
        '<p class="section-sub">We don&#39;t build websites for everyone. We specialise exclusively in health and wellness &mdash; which means we know your customers, your industry, and what converts.</p>'
        '</div>'
        '<div class="for-grid">'

        + ''.join([
            '<div class="for-card reveal">'
            '<div class="for-icon-wrap">' + icon(ic) + '</div>'
            '<div class="for-name">' + name + '</div>'
            '<div class="for-desc">' + desc + '</div>'
            '</div>'
            for ic, name, desc in [
                ('dumbbell', 'Gyms &amp; Fitness', 'Class schedules, memberships, online sign-ups'),
                ('flame',    'Saunas &amp; Spas', 'Session bookings, gift cards, pricing tiers'),
                ('lotus',    'Yoga Studios', 'Class timetables, drop-in passes, packages'),
                ('bike',     'Spinning Studios', 'Bike reservations, bundles, leaderboards'),
                ('person',   'Pilates Studios', 'Reformer bookings, waitlists, introductory offers'),
                ('shield',   'CrossFit Boxes', 'On-ramp booking, whiteboard scores, merch shop'),
                ('hand',     'Martial Arts', 'Trial class sign-ups, grade tracking, timetables'),
                ('dance',    'Dance Studios', 'Class levels, term bookings, performance pages'),
                ('wave',     'Swimming Schools', 'Level-based booking, term management, waivers'),
                ('golf',     'Golf Academies', 'Lesson booking, video analysis, membership'),
                ('heart',    'Physiotherapy', 'Appointment booking, condition info, referral forms'),
                ('leaf',     'Holistic Therapy', 'Service menus, booking, gift vouchers'),
                ('brain',    'Nutritionists', 'Consultation booking, blog, meal plan access'),
                ('person',   'Personal Trainers', 'Session booking, client portals, payment links'),
            ]
        ]) +

        '</div>'
        '</div>'
        '</section>'

        # WHY KRYSON
        '<section id="why">'
        '<div class="wrap">'
        '<div class="reveal">'
        '<div class="section-tag">Why Kryson</div>'
        '<h2 class="section-title">Custom-built.<br><span class="gt">Not templated.</span></h2>'
        '<p class="section-sub">No Wix. No Squarespace. No cookie-cutter builders. Every site we build is coded from scratch &mdash; faster, better SEO, and a design your competitors won&#39;t have.</p>'
        '</div>'
        '<div class="why-grid">'
        '<div class="why-features reveal-l">'

        '<div class="why-feat"><div class="wf-icon wf-i1">' + icon('star-award') + '</div>'
        '<div><div class="why-feat-h">Elite Custom Design</div>'
        '<div class="why-feat-p">Designed to impress from the first second. Animations and layouts your competitors won&#39;t have.</div></div></div>'

        '<div class="why-feat"><div class="wf-icon wf-i2">' + icon('mobile') + '</div>'
        '<div><div class="why-feat-h">Mobile-First</div>'
        '<div class="why-feat-p">Over 70% of your customers find you on their phone. We build mobile experiences that convert.</div></div></div>'

        '<div class="why-feat"><div class="wf-icon wf-i3">' + icon('seo') + '</div>'
        '<div><div class="why-feat-h">Local SEO</div>'
        '<div class="why-feat-p">We optimise so you rank when people search "gym near me" or "yoga Dublin". Real local customers.</div></div></div>'

        '<div class="why-feat"><div class="wf-icon wf-i4">' + icon('payment') + '</div>'
        '<div><div class="why-feat-h">Payments &amp; Bookings</div>'
        '<div class="why-feat-p">Take payments and bookings directly from your site. Stripe-integrated, no third-party logins needed.</div></div></div>'

        '<div class="why-feat"><div class="wf-icon wf-i5">' + icon('ireland') + '</div>'
        '<div><div class="why-feat-h">Based in Ireland</div>'
        '<div class="why-feat-p">We understand the Irish market. Euro pricing, Irish business context, and a real person at the end of the phone.</div></div></div>'

        '</div>'
        '<div class="why-visual reveal-r">'
        '<div class="why-stat-grid">'
        '<div class="why-stat-card"><div class="wsc-num">14</div><div class="wsc-label">Wellness niches served</div></div>'
        '<div class="why-stat-card"><div class="wsc-num">&euro;497</div><div class="wsc-label">Starting price</div></div>'
        '<div class="why-stat-card"><div class="wsc-num">7 days</div><div class="wsc-label">Starter delivery</div></div>'
        '<div class="why-stat-card"><div class="wsc-num">100%</div><div class="wsc-label">Custom built</div></div>'
        '</div>'
        '<div class="why-note">'
        '<strong>No lock-in.</strong> Every site we build is fully owned by you. All code, credentials, and content are handed over on completion. No ongoing fees to us.'
        '</div>'
        '</div>'
        '</div>'
        '</div>'
        '</section>'

        # CASE STUDY PREVIEW
        '<section id="case-preview">'
        '<div class="wrap">'
        '<div class="reveal">'
        '<div class="section-tag">Featured Project</div>'
        '<h2 class="section-title">We built the complete<br>digital infrastructure for <span class="gt">Pikenhot</span></h2>'
        '</div>'
        '</div>'
        '<div class="wrap" style="margin-top:40px">'
        '<div class="cs-wrap reveal">'
        '<div class="cs-content">'
        '<div class="cs-logo-text">PIKENHOT.IE</div>'
        '<div class="cs-url">Gym &amp; Sauna Centre, Ireland</div>'
        '<div class="cs-badges">'
        '<span class="cs-badge">Custom Website</span>'
        '<span class="cs-badge">Member Portal</span>'
        '<span class="cs-badge">Admin CRM</span>'
        '<span class="cs-badge">Stripe Payments</span>'
        '<span class="cs-badge">Staff Roster</span>'
        '</div>'
        '<h3 class="cs-h">A full website, member portal, and business backend &mdash; built from scratch.</h3>'
        '<p class="cs-p">Pikenhot needed more than a website. We built a complete digital system: a custom site, a member portal where customers self-manage their memberships, and an admin CRM tracking payments, staff, opening hours, and reviews.</p>'
        '<div class="cs-stats">'
        '<div><div class="cs-stat-n">&euro;1,497</div><div class="cs-stat-l">Complete package</div></div>'
        '<div><div class="cs-stat-n">100%</div><div class="cs-stat-l">Custom built</div></div>'
        '<div><div class="cs-stat-n">3 wk</div><div class="cs-stat-l">Delivered</div></div>'
        '</div>'
        '<div class="cs-ctas">'
        '<a href="work.html" class="btn btn-grad">See Case Study &rarr;</a>'
        '<a href="https://pikenhot.ie" target="_blank" rel="noopener" class="btn btn-outline">Visit pikenhot.ie &#8599;</a>'
        '</div>'
        '</div>'
        '<div class="cs-visual">' + browser_mockup() + '</div>'
        '</div>'
        '</div>'
        '</section>'

        # PRICING PREVIEW
        '<section id="pricing-preview">'
        '<div class="wrap">'
        '<div class="reveal">'
        '<div class="section-tag">Pricing</div>'
        '<h2 class="section-title">Transparent pricing.<br><span class="gt">No surprises.</span></h2>'
        '<p class="section-sub">Three packages to match where your business is now. All include custom design, mobile-first build, and full handover of everything.</p>'
        '</div>'
        '<div class="price-grid">'

        '<div class="price-card reveal">'
        '<div class="price-tier">Tier 01</div>'
        '<div class="price-name">Starter</div>'
        '<div class="price-amount"><span class="gt">&euro;497</span></div>'
        '<div class="price-period">One-time payment &bull; No monthly fees</div>'
        '<div class="price-divider"></div>'
        '<ul class="price-features">'
        '<li class="price-feat">' + check('pf-1') + 'Custom website (up to 5 pages)</li>'
        '<li class="price-feat">' + check('pf-1') + 'Mobile responsive &amp; fast</li>'
        '<li class="price-feat">' + check('pf-1') + 'Google Business setup</li>'
        '<li class="price-feat">' + check('pf-1') + 'On-page SEO &amp; schema markup</li>'
        '<li class="price-feat">' + check('pf-1') + 'Contact form</li>'
        '<li class="price-feat">' + check('pf-1') + 'Delivered in 7 days</li>'
        '</ul>'
        '<a href="' + STRIPE_497 + '" class="btn btn-grad" target="_blank" rel="noopener" style="width:100%;justify-content:center">Buy Now &mdash; &euro;497 &rarr;</a>'
        '<div class="stripe-safe">' + icon('payment') + ' Secure payment via Stripe</div>'
        '</div>'

        '<div class="price-card featured reveal">'
        '<div class="price-badge">Most Popular</div>'
        '<div class="price-tier">Tier 02</div>'
        '<div class="price-name">Growth</div>'
        '<div class="price-amount"><span class="gt">&euro;997</span></div>'
        '<div class="price-period">One-time payment &bull; No monthly fees</div>'
        '<div class="price-divider"></div>'
        '<ul class="price-features">'
        '<li class="price-feat">' + check('pf-2') + 'Everything in Starter</li>'
        '<li class="price-feat">' + check('pf-2') + 'Online payments (Stripe)</li>'
        '<li class="price-feat">' + check('pf-2') + 'Class &amp; appointment booking</li>'
        '<li class="price-feat">' + check('pf-2') + 'Advanced local SEO</li>'
        '<li class="price-feat">' + check('pf-2') + 'Google Analytics 4</li>'
        '<li class="price-feat">' + check('pf-2') + 'Delivered in 14 days</li>'
        '</ul>'
        '<a href="' + STRIPE_997 + '" class="btn btn-grad" target="_blank" rel="noopener" style="width:100%;justify-content:center">Buy Now &mdash; &euro;997 &rarr;</a>'
        '<div class="stripe-safe">' + icon('payment') + ' Secure payment via Stripe</div>'
        '</div>'

        '<div class="price-card reveal">'
        '<div class="price-tier">Tier 03</div>'
        '<div class="price-name">Complete</div>'
        '<div class="price-amount"><span class="gt2">&euro;1,497</span></div>'
        '<div class="price-period">One-time payment &bull; No monthly fees</div>'
        '<div class="price-divider"></div>'
        '<ul class="price-features">'
        '<li class="price-feat">' + check('pf-3') + 'Everything in Growth</li>'
        '<li class="price-feat">' + check('pf-3') + 'Member portal (self-manage accounts)</li>'
        '<li class="price-feat">' + check('pf-3') + 'Staff &amp; roster management</li>'
        '<li class="price-feat">' + check('pf-3') + 'Transaction history &amp; CRM</li>'
        '<li class="price-feat">' + check('pf-3') + 'Review management</li>'
        '<li class="price-feat">' + check('pf-3') + 'Delivered in 21 days</li>'
        '</ul>'
        '<a href="' + STRIPE_1497 + '" class="btn btn-grad" target="_blank" rel="noopener" style="width:100%;justify-content:center">Buy Now &mdash; &euro;1,497 &rarr;</a>'
        '<div class="stripe-safe">' + icon('payment') + ' Secure payment via Stripe</div>'
        '</div>'

        '</div>'
        '<div style="text-align:center;margin-top:32px" class="reveal">'
        '<a href="pricing.html" style="font-size:13px;color:var(--text3);text-decoration:none;font-weight:500">View full pricing &amp; FAQ &rarr;</a>'
        '</div>'
        '</div>'
        '</section>'

        # PROCESS
        '<section id="process">'
        '<div class="wrap">'
        '<div class="reveal">'
        '<div class="section-tag">How It Works</div>'
        '<h2 class="section-title">From quote to live<br>in <span class="gt">4 steps.</span></h2>'
        '</div>'
        '<div class="process-steps">'
        '<div class="process-step reveal"><div class="ps-num-wrap"><div class="ps-n">01</div></div><div class="ps-h">Tell Us About Your Business</div><div class="ps-p">Fill in our form. We reply within 24 hours with a clear proposal.</div></div>'
        '<div class="process-step reveal"><div class="ps-num-wrap"><div class="ps-n">02</div></div><div class="ps-h">We Design &amp; Build</div><div class="ps-p">We handle everything. Design, copy, development, SEO, integrations.</div></div>'
        '<div class="process-step reveal"><div class="ps-num-wrap"><div class="ps-n">03</div></div><div class="ps-h">Review &amp; Refine</div><div class="ps-p">We send you a live preview. Request changes. We refine until perfect.</div></div>'
        '<div class="process-step reveal"><div class="ps-num-wrap"><div class="ps-n">04</div></div><div class="ps-h">Go Live</div><div class="ps-p">We launch, connect your domain, and hand over everything. You own it all.</div></div>'
        '</div>'
        '</div>'
        '</section>'

        # CTA
        '<section class="cta-band">'
        '<div class="cta-band-inner reveal">'
        '<h2>Ready to build something <span class="gt">great?</span></h2>'
        '<p>Free quote, 24-hour response. No commitment and no pressure &mdash; just a clear proposal for your business.</p>'
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

PRICING_SCHEMA = (
    '<script type="application/ld+json">'
    '{"@context":"https://schema.org","@type":"ItemList","name":"Kryson Web Design Packages","itemListElement":['
    '{"@type":"ListItem","position":1,"item":{"@type":"Product","name":"Starter Web Design Package",'
    '"description":"Custom website up to 5 pages with mobile responsive design and basic local SEO for Irish health and wellness businesses.",'
    '"offers":{"@type":"Offer","price":"497","priceCurrency":"EUR","availability":"https://schema.org/InStock"}}},'
    '{"@type":"ListItem","position":2,"item":{"@type":"Product","name":"Growth Web Design Package",'
    '"description":"Custom website with online payments via Stripe, class booking system, and advanced local SEO.",'
    '"offers":{"@type":"Offer","price":"997","priceCurrency":"EUR","availability":"https://schema.org/InStock"}}},'
    '{"@type":"ListItem","position":3,"item":{"@type":"Product","name":"Complete Business Infrastructure Package",'
    '"description":"Full website plus member portal, admin CRM, staff management, review system and complete business backend.",'
    '"offers":{"@type":"Offer","price":"1497","priceCurrency":"EUR","availability":"https://schema.org/InStock"}}}'
    ']}'
    '</script>'
)

def build_pricing():
    return (
        page_head(
            'Web Design Pricing for Health &amp; Wellness Businesses Ireland | Kryson',
            'Transparent web design pricing for Irish gyms, yoga studios and wellness businesses. Starter &euro;497, Growth &euro;997, Complete &euro;1,497. One-time payments, no monthly fees.',
            SITE_URL + '/pricing',
            PRICING_SCHEMA
        ) +
        NAV +

        '<div class="inner-hero-wrap">'
        '<div class="inner-hero">'
        '<div class="section-tag reveal">Pricing</div>'
        '<h1 class="inner-h1 reveal">Simple, transparent<br><span class="gt">pricing.</span></h1>'
        '<p class="inner-sub reveal">One-time payments. No monthly fees to us. No hidden costs. A custom website delivered on time.</p>'
        '</div>'
        '</div>'

        '<div class="page-body">'
        '<div class="pricing-cards-wrap">'

        # STARTER
        '<div class="full-price-card reveal">'
        '<div class="fpc-tier">Tier 01</div>'
        '<div class="fpc-name">Starter</div>'
        '<div class="fpc-tagline">A professional website that puts you on the map and starts ranking in local search.</div>'
        '<div class="fpc-price"><span class="gt">&euro;497</span></div>'
        '<div class="fpc-note">One-time payment &bull; No monthly fees to Kryson</div>'
        '<div class="fpc-divider"></div>'
        '<ul class="fpc-features">'
        '<li class="fpc-feat">' + fpc_check('fpc-i1') + 'Custom designed website (up to 5 pages)</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i1') + 'Home, About, Services, Gallery, Contact</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i1') + 'Fully mobile responsive &amp; fast loading</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i1') + 'Google Business Profile setup &amp; verification</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i1') + 'On-page SEO (titles, meta, headings, keywords)</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i1') + 'LocalBusiness &amp; Service JSON-LD schema</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i1') + 'Contact form with email notifications</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i1') + 'Google Maps integration</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i1') + 'Social media links</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i1') + '1 round of revisions</li>'
        '</ul>'
        '<div class="fpc-timeline">Delivered in 7 days</div>'
        '<a href="' + STRIPE_497 + '" class="btn btn-grad" target="_blank" rel="noopener" style="width:100%;justify-content:center;margin-bottom:10px">Buy Now &mdash; &euro;497 &rarr;</a>'
        '<div class="stripe-safe">' + icon('payment') + ' Secure checkout via Stripe</div>'
        '<button class="fpc-enquire" onclick="openModal()">Have questions first? Get a free quote</button>'
        '</div>'

        # GROWTH
        '<div class="full-price-card featured reveal">'
        '<div class="fpc-badge">Most Popular</div>'
        '<div class="fpc-tier">Tier 02</div>'
        '<div class="fpc-name">Growth</div>'
        '<div class="fpc-tagline">Take bookings and payments directly on your site. Rank higher across your county.</div>'
        '<div class="fpc-price"><span class="gt">&euro;997</span></div>'
        '<div class="fpc-note">One-time payment &bull; No monthly fees to Kryson</div>'
        '<div class="fpc-divider"></div>'
        '<ul class="fpc-features">'
        '<li class="fpc-feat">' + fpc_check('fpc-i2') + 'Everything in Starter</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i2') + 'Online payment processing (Stripe)</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i2') + 'Class &amp; appointment booking system</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i2') + 'Up to 8 pages</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i2') + 'Advanced local SEO (Google Maps ranking)</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i2') + 'Google Business optimisation &amp; posts</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i2') + 'Local citation building (20+ directories)</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i2') + 'Email capture &amp; basic automation</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i2') + 'Google Analytics 4 &amp; Search Console setup</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i2') + '2 rounds of revisions</li>'
        '</ul>'
        '<div class="fpc-timeline">Delivered in 14 days</div>'
        '<a href="' + STRIPE_997 + '" class="btn btn-grad" target="_blank" rel="noopener" style="width:100%;justify-content:center;margin-bottom:10px">Buy Now &mdash; &euro;997 &rarr;</a>'
        '<div class="stripe-safe">' + icon('payment') + ' Secure checkout via Stripe</div>'
        '<button class="fpc-enquire" onclick="openModal()">Have questions first? Get a free quote</button>'
        '</div>'

        # COMPLETE
        '<div class="full-price-card reveal">'
        '<div class="fpc-tier">Tier 03</div>'
        '<div class="fpc-name">Complete</div>'
        '<div class="fpc-tagline">Your entire business infrastructure online. Like pikenhot.ie, but built for you.</div>'
        '<div class="fpc-price"><span class="gt2">&euro;1,497</span></div>'
        '<div class="fpc-note">One-time payment &bull; No monthly fees to Kryson</div>'
        '<div class="fpc-divider"></div>'
        '<ul class="fpc-features">'
        '<li class="fpc-feat">' + fpc_check('fpc-i3') + 'Everything in Growth</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i3') + 'Member portal (customers self-manage accounts)</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i3') + 'Full admin CRM dashboard</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i3') + 'Staff management &amp; roster system</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i3') + 'Transaction &amp; payment history</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i3') + 'Review collection &amp; management</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i3') + 'Dynamic opening hours management</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i3') + 'Unlimited pages</li>'
        '<li class="fpc-feat">' + fpc_check('fpc-i3') + '3 rounds of revisions</li>'
        '</ul>'
        '<div class="fpc-timeline">Delivered in 21 days</div>'
        '<a href="' + STRIPE_1497 + '" class="btn btn-grad" target="_blank" rel="noopener" style="width:100%;justify-content:center;margin-bottom:10px">Buy Now &mdash; &euro;1,497 &rarr;</a>'
        '<div class="stripe-safe">' + icon('payment') + ' Secure checkout via Stripe</div>'
        '<button class="fpc-enquire" onclick="openModal()">Have questions first? Get a free quote</button>'
        '</div>'

        '</div>'

        '<div style="text-align:center;padding:0 0 72px" class="reveal">'
        '<p style="color:var(--text3);font-size:14px;margin-bottom:16px">Not sure which package suits you?</p>'
        '<button class="btn btn-grad" onclick="openModal()">Get a Free Consultation &rarr;</button>'
        '</div>'

        # FAQ
        '<div class="faq-section reveal">'
        '<h2>Frequently Asked <span class="gt">Questions</span></h2>'
        '<div class="faq-item"><div class="faq-q">Do I own the website once it&#39;s built? <span class="faq-icon">+</span></div><div class="faq-a">Yes, 100%. Once the project is complete and paid, you own everything outright. We hand over all code, hosting credentials, and domain access. No lock-in, no ongoing fees to Kryson.</div></div>'
        '<div class="faq-item"><div class="faq-q">What are the ongoing costs after launch? <span class="faq-icon">+</span></div><div class="faq-a">Our build fee is a one-time payment. The only ongoing costs are hosting (typically &euro;5&ndash;&euro;15/month, paid directly to the host) and your domain name (around &euro;10&ndash;&euro;15/year). We don&#39;t add any markup to these. If you have the Growth or Complete package, Stripe charges a small transaction fee (currently 1.5% + 25c for European cards) directly to Stripe.</div></div>'
        '<div class="faq-item"><div class="faq-q">What do you need from me to get started? <span class="faq-icon">+</span></div><div class="faq-a">Your logo, photos of your space (or we&#39;ll advise on getting them), your pricing and services, and a 30-minute call to understand your business. We handle all copy, design, and technical setup.</div></div>'
        '<div class="faq-item"><div class="faq-q">Can I upgrade my package later? <span class="faq-icon">+</span></div><div class="faq-a">Yes. Many clients start on Starter or Growth and upgrade when they&#39;re ready. We offer upgrade pricing so you only pay the difference, not the full new package price.</div></div>'
        '<div class="faq-item"><div class="faq-q">What&#39;s included in local SEO? <span class="faq-icon">+</span></div><div class="faq-a">We set up and optimise your Google Business Profile, add structured data (JSON-LD schema) to your site, optimise page titles and meta descriptions for local search terms (e.g. "yoga studio Dublin", "gym near Galway"), build citations on 20+ Irish directories, and submit your sitemap to Google Search Console. For the Growth package, we also work on Google Maps ranking specifically.</div></div>'
        '<div class="faq-item"><div class="faq-q">How does the Stripe integration work? <span class="faq-icon">+</span></div><div class="faq-a">We connect your Stripe account directly to your website. Customers can pay for classes, memberships, and packages online. You see all payments in your Stripe dashboard in real time. Stripe charges go directly to your bank account &mdash; we never touch your funds.</div></div>'
        '<div class="faq-item"><div class="faq-q">Do you build for businesses outside of Ireland? <span class="faq-icon">+</span></div><div class="faq-a">Our focus is the Irish market but we take UK and international projects on a case-by-case basis. Get in touch and we&#39;ll let you know.</div></div>'
        '</div>'

        '</div>'

        '<section class="cta-band"><div class="cta-band-inner reveal">'
        '<h2>Ready to get <span class="gt">started?</span></h2>'
        '<p>Send us a message and we&#39;ll reply with a clear proposal within 24 hours.</p>'
        '<div class="cta-btns"><button class="btn btn-grad" onclick="openModal()">Get a Free Quote &rarr;</button><a href="contact.html" class="btn btn-outline">Contact Us</a></div>'
        '</div></section>'

        + page_foot()
    )

# ============================================================
# WORK PAGE
# ============================================================

def build_work():
    return (
        page_head(
            'Web Design Portfolio &mdash; Irish Health &amp; Wellness Websites | Kryson',
            'View Kryson&#39;s web design work for Irish health and wellness businesses. Pikenhot.ie &mdash; complete gym and sauna digital infrastructure built from scratch.',
            SITE_URL + '/work'
        ) +
        NAV +

        '<div class="inner-hero-wrap" style="background:var(--bg2)">'
        '<div class="inner-hero" style="text-align:center;max-width:680px;margin:0 auto">'
        '<div class="section-tag reveal">Our Work</div>'
        '<h1 class="inner-h1 reveal">Built for Irish<br><span class="gt">wellness businesses.</span></h1>'
        '<p class="inner-sub reveal" style="max-width:100%">Every project is custom. Here&#39;s what we&#39;ve built.</p>'
        '</div>'
        '</div>'

        '<div class="page-body">'

        '<div class="case-card reveal">'
        '<div class="case-info">'
        '<div class="case-tag">Complete Package &mdash; &euro;1,497</div>'
        '<h2 class="case-h"><span class="gt">Pikenhot</span> &mdash; Gym &amp; Sauna Centre</h2>'
        '<p class="case-p">Pikenhot needed more than a website. We built a complete digital infrastructure: a custom-designed public site, a member portal where customers self-manage their memberships, and a full admin CRM &mdash; tracking payments, staff, opening hours, and reviews &mdash; all in one place.</p>'
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
        '<div class="case-ctas">'
        '<div class="case-outcome">&#10003; Live at pikenhot.ie</div>'
        '</div>'
        '<div style="margin-top:20px;display:flex;gap:10px;flex-wrap:wrap">'
        '<a href="https://pikenhot.ie" target="_blank" rel="noopener" class="btn btn-grad">Visit pikenhot.ie &#8599;</a>'
        '<button class="btn btn-outline" onclick="openModal()">Build Mine &rarr;</button>'
        '</div>'
        '</div>'
        '<div class="case-visual">' + browser_mockup() + '</div>'
        '</div>'

        '<div class="reveal" style="margin-top:48px;margin-bottom:48px">'
        '<h3 style="font-size:clamp(20px,3vw,28px);font-weight:800;margin-bottom:8px;color:var(--text)">What we built for Pikenhot</h3>'
        '<p style="color:var(--text3);font-size:14px;margin-bottom:28px">Every system, in detail</p>'
        '<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px">'

        + ''.join([
            '<div class="av-card"><div class="av-icon">' + icon(ic) + '</div>'
            '<div class="av-h">' + h + '</div>'
            '<div class="av-p">' + p + '</div></div>'
            for ic, h, p in [
                ('rocket', 'Public Website', 'Fully custom-designed multi-page site. Gym info, sauna sessions, facilities, pricing, and contact. Animated, mobile-first, and fast.'),
                ('person', 'Member Portal', 'Members log in to view membership status, manage subscriptions, see booking history, and update payment details &mdash; entirely self-service.'),
                ('payment', 'Payment Processing', 'Stripe integration for memberships, one-off sessions, and recurring billing. Full transaction history visible in the admin panel.'),
                ('person', 'Staff Roster', 'Admin dashboard for managing staff shifts. Who&#39;s in, who&#39;s off &mdash; all in one place. No spreadsheets needed.'),
                ('clock', 'Opening Hours', 'Dynamic hours management. Update hours from the admin and they appear on the public site in real time.'),
                ('star-award', 'Review Management', 'Collect and display customer reviews. The admin controls which reviews are shown publicly, building trust automatically.'),
            ]
        ]) +

        '</div>'
        '</div>'

        '<div class="reveal" style="text-align:center;padding:56px 0;border-top:1px solid var(--border)">'
        '<p style="font-size:11px;letter-spacing:3px;text-transform:uppercase;color:var(--text3);margin-bottom:14px;font-weight:500">More Projects</p>'
        '<h3 style="font-size:clamp(22px,3.5vw,36px);font-weight:800;margin-bottom:12px;color:var(--text)">Your business could be next.</h3>'
        '<p style="color:var(--text3);font-size:15px;margin-bottom:28px;max-width:440px;margin-left:auto;margin-right:auto">We take on a small number of new projects each month. Get in touch to check availability.</p>'
        '<button class="btn btn-grad" onclick="openModal()">Start Your Project &rarr;</button>'
        '</div>'

        '</div>'

        '<section class="cta-band"><div class="cta-band-inner reveal">'
        '<h2>Want to see what we&#39;d<br>build for <span class="gt">you?</span></h2>'
        '<p>Get a free quote and a clear proposal in 24 hours.</p>'
        '<div class="cta-btns"><button class="btn btn-grad" onclick="openModal()">Get a Free Quote &rarr;</button><a href="pricing.html" class="btn btn-outline">View Pricing</a></div>'
        '</div></section>'

        + page_foot()
    )

# ============================================================
# ABOUT PAGE
# ============================================================

def build_about():
    return (
        page_head(
            'About Kryson &mdash; Irish Web Design Agency for Health &amp; Wellness | Kryson',
            'Kryson is an Irish web design agency specialising exclusively in gyms, saunas, yoga studios and wellness businesses. Based in Ireland, building elite websites from &euro;497.',
            SITE_URL + '/about'
        ) +
        NAV +

        '<div class="inner-hero-wrap">'
        '<div class="inner-hero">'
        '<div class="section-tag reveal">About Kryson</div>'
        '<h1 class="inner-h1 reveal">Built by someone who<br>knows <span class="gt">your industry.</span></h1>'
        '<p class="inner-sub reveal">We don&#39;t build websites for everyone. We build them exclusively for health and wellness businesses &mdash; because that focus gets better results for you.</p>'
        '</div>'
        '</div>'

        '<div class="page-body">'
        '<div class="about-grid">'

        '<div class="about-text reveal-l">'
        '<p>Kryson started from a straightforward idea: most health and wellness businesses in Ireland have websites that don&#39;t do them justice. Generic templates, slow load times, poor mobile experience &mdash; and no local SEO to speak of.</p>'
        '<p>We proved what was possible by building a complete digital infrastructure for <strong>Pikenhot</strong> &mdash; an Irish gym and sauna centre. Not just a website, but a member portal, admin CRM, Stripe payment integration, staff management, review system, and dynamic opening hours. All from scratch, all custom.</p>'
        '<p>That project became our standard. Now we offer the same quality to gyms, yoga studios, saunas, pilates centres, personal trainers, and every other kind of wellness business across Ireland.</p>'
        '<p>We work exclusively in health and wellness because knowing your industry inside out means better questions, better design decisions, and better results. We know what converts your kind of customer.</p>'
        '<p>We&#39;re based in Ireland. We price in euro. We reply to messages. When you work with Kryson, there&#39;s a real person on the other end who cares about the outcome.</p>'
        '</div>'

        '<div class="reveal-r">'
        + ''.join([
            '<div class="av-card"><div class="av-icon">' + icon(ic) + '</div>'
            '<div class="av-h">' + h + '</div><div class="av-p">' + p + '</div></div>'
            for ic, h, p in [
                ('ireland', 'Ireland-Based', 'We understand Irish business, Irish customers, and the Irish local search landscape. Euro pricing, no VAT complications, always available.'),
                ('star-award', 'Wellness Only', 'We only take on health and wellness clients. Every feature we build is informed by deep industry knowledge.'),
                ('rocket', 'No Templates', 'We don&#39;t use Wix, Squarespace, or page builders. Every site is custom-coded: faster, better SEO, and a design nobody else has.'),
                ('payment', 'Full Stack', 'From design to backend systems, we do it all in-house. One team, one point of contact, one clear outcome.'),
            ]
        ]) +
        '</div>'

        '</div>'
        '</div>'

        '<section class="cta-band"><div class="cta-band-inner reveal">'
        '<h2>Let&#39;s build something<br><span class="gt">great together.</span></h2>'
        '<p>Free quote and proposal within 24 hours.</p>'
        '<div class="cta-btns"><button class="btn btn-grad" onclick="openModal()">Get a Free Quote &rarr;</button><a href="pricing.html" class="btn btn-outline">View Pricing</a></div>'
        '</div></section>'

        + page_foot()
    )

# ============================================================
# CONTACT PAGE
# ============================================================

def build_contact():
    return (
        page_head(
            'Contact Kryson &mdash; Free Quote for Your Wellness Website | Kryson',
            'Get a free web design quote for your gym, sauna, yoga studio or wellness business in Ireland. Based in Ireland, 24-hour response, no commitment.',
            SITE_URL + '/contact'
        ) +
        NAV +

        '<div class="inner-hero-wrap">'
        '<div class="inner-hero">'
        '<div class="section-tag reveal">Get in Touch</div>'
        '<h1 class="inner-h1 reveal">Start your project.<br><span class="gt">Free quote.</span></h1>'
        '<p class="inner-sub reveal">Fill in the form and we&#39;ll reply within 24 hours with a clear proposal for your business.</p>'
        '</div>'
        '</div>'

        '<div class="page-body">'
        '<div class="contact-grid">'

        '<div class="reveal-l">'
        '<div class="ci-item"><div class="ci-icon">' + icon('map') + '</div><div><div class="ci-h">Based in Ireland</div><div class="ci-p">We work with businesses across Ireland &mdash; Dublin, Cork, Galway, Limerick, and everywhere in between.</div></div></div>'
        '<div class="ci-item"><div class="ci-icon">' + icon('clock') + '</div><div><div class="ci-h">24-Hour Response</div><div class="ci-p">We reply to every enquiry within 24 hours on weekdays. Usually much faster.</div></div></div>'
        '<div class="ci-item"><div class="ci-icon">' + icon('star-award') + '</div><div><div class="ci-h">Free Quote</div><div class="ci-p">No commitment. We&#39;ll assess your needs and give you a clear, itemised proposal at no cost.</div></div></div>'
        '<div class="ci-item"><div class="ci-icon">' + icon('mail') + '</div><div><div class="ci-h">Email</div><div class="ci-p"><a href="mailto:kyle@krysongroup.com" style="color:var(--text2);text-decoration:none;font-weight:500">kyle@krysongroup.com</a></div></div></div>'
        '</div>'

        '<div class="contact-form-box reveal-r">'
        '<div class="cf-title">Send Us a Message</div>'
        '<div class="cf-sub">We&#39;ll come back to you within 24 hours</div>'
        '<div id="cf-form">'
        '<div class="cf-2col"><div class="cf-field"><label>First Name *</label><input type="text" id="cfFirst" placeholder="Ciara" required></div><div class="cf-field"><label>Last Name</label><input type="text" id="cfLast" placeholder="Murphy"></div></div>'
        '<div class="cf-field"><label>Email *</label><input type="email" id="cfEmail" placeholder="you@yourbusiness.ie" required></div>'
        '<div class="cf-field"><label>Phone *</label><input type="tel" id="cfPhone" placeholder="+353 87 000 0000" required></div>'
        '<div class="cf-field"><label>Business Type</label>'
        '<select id="cfBiz"><option value="">Select...</option>'
        '<option>Gym / Fitness Centre</option><option>Sauna / Wellness Centre</option>'
        '<option>Yoga Studio</option><option>Pilates Studio</option>'
        '<option>Spinning / Cycling Studio</option><option>CrossFit Box</option>'
        '<option>Martial Arts (MMA / Boxing / BJJ)</option><option>Dance Studio</option>'
        '<option>Swimming School / Club</option><option>Golf Academy</option>'
        '<option>Physiotherapy / Sports Rehab</option><option>Holistic Therapy / Massage</option>'
        '<option>Nutritionist / Dietitian</option><option>Personal Trainer</option>'
        '<option>Other Health &amp; Wellness</option>'
        '</select></div>'
        '<div class="cf-field"><label>Package</label>'
        '<select id="cfPkg"><option value="">Not sure yet</option>'
        '<option>Starter &mdash; &euro;497</option>'
        '<option>Growth &mdash; &euro;997</option>'
        '<option>Complete &mdash; &euro;1,497</option>'
        '</select></div>'
        '<div class="cf-field"><label>Tell Us About Your Business</label>'
        '<textarea id="cfMsg" placeholder="What does your business do, where are you based, what&#39;s your main goal for the website?"></textarea>'
        '</div>'
        '<button class="cf-submit" onclick="submitContactForm()">Send Message &rarr;</button>'
        '</div>'
        '<div id="cf-sending"><div class="cf-spin"></div><p style="color:var(--text3);font-size:13px">Sending...</p></div>'
        '<div id="cf-success">'
        '<div class="cf-ok">&#10003;</div>'
        '<h3>Message received!</h3>'
        '<p style="color:var(--text3);font-size:13px;margin-bottom:16px">We&#39;ll be in touch within 24 hours to discuss your website.</p>'
        '<a href="https://calendly.com/kyle-krysongroup/kryson-limited-website-kick-off-call" target="_blank" rel="noopener" class="btn btn-grad" style="font-size:13px;justify-content:center">Schedule a Call Now &rarr;</a>'
        '</div>'
        '</div>'

        '</div>'
        '</div>'

        + page_foot(include_contact_js=True)
    )

# ============================================================
# SITEMAP
# ============================================================

def build_sitemap():
    pages = [
        (SITE_URL + '/', '1.0', 'weekly'),
        (SITE_URL + '/pricing', '0.9', 'monthly'),
        (SITE_URL + '/work', '0.8', 'monthly'),
        (SITE_URL + '/about', '0.7', 'monthly'),
        (SITE_URL + '/contact', '0.8', 'monthly'),
        (SITE_URL + '/insights', '0.8', 'weekly'),
        (SITE_URL + '/insight-gym-website-cost-ireland', '0.7', 'monthly'),
        (SITE_URL + '/insight-yoga-studio-website', '0.7', 'monthly'),
        (SITE_URL + '/insight-local-seo-fitness-ireland', '0.7', 'monthly'),
        (SITE_URL + '/insight-personal-trainer-website', '0.7', 'monthly'),
        (SITE_URL + '/insight-wellness-website-mistakes', '0.7', 'monthly'),
        (SITE_URL + '/insight-online-booking-wellness', '0.7', 'monthly'),
    ]
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"'
             ' xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for url, pri, freq in pages:
        lines.append('<url>')
        lines.append('<loc>' + url + '</loc>')
        lines.append('<changefreq>' + freq + '</changefreq>')
        lines.append('<priority>' + pri + '</priority>')
        lines.append('<xhtml:link rel="alternate" hreflang="en-IE" href="' + url + '"/>')
        lines.append('</url>')
    lines.append('</urlset>')
    return '\n'.join(lines)

# ============================================================
# INSIGHT PAGES
# ============================================================

def insight_head(title, desc, canonical, date):
    schema = (
        '<script type="application/ld+json">'
        '{"@context":"https://schema.org","@type":"Article",'
        '"headline":"' + title + '",'
        '"description":"' + desc + '",'
        '"datePublished":"' + date + '",'
        '"author":{"@type":"Person","name":"Kyle","url":"' + SITE_URL + '/about"},'
        '"publisher":{"@type":"Organization","name":"Kryson","url":"' + SITE_URL + '"},'
        '"mainEntityOfPage":"' + canonical + '"}'
        '</script>'
    )
    return page_head(title, desc, canonical, schema)

def insight_cta():
    return (
        '<div class="insight-cta-box">'
        '<div class="icta-tag">Ready to get started?</div>'
        '<h3>Get a professional wellness website.<br><span class="gt">Starting from &euro;497.</span></h3>'
        '<p>Custom-built, mobile-first, and fully optimised for local search. Delivered in as little as 7 days.</p>'
        '<div style="display:flex;gap:10px;flex-wrap:wrap;justify-content:center;margin-top:24px">'
        '<a href="pricing.html" class="btn btn-grad">See Packages &amp; Buy &rarr;</a>'
        '<a href="work.html" class="btn btn-outline">View Our Work</a>'
        '</div>'
        '<div class="stripe-safe" style="justify-content:center;margin-top:12px">' + icon('payment') + ' Secure checkout via Stripe</div>'
        '</div>'
    )

def build_insights():
    articles = [
        ('insight-gym-website-cost-ireland.html',  'How Much Does a Gym Website Cost in Ireland? (2025 Guide)',          'gym-cost'),
        ('insight-yoga-studio-website.html',        'What Every Yoga Studio Website Needs to Convert Visitors',           'yoga'),
        ('insight-local-seo-fitness-ireland.html',  'Local SEO for Gyms &amp; Fitness Studios in Ireland',               'seo'),
        ('insight-personal-trainer-website.html',   'Do Personal Trainers in Ireland Need a Website? Yes &mdash; Here&#39;s Why', 'pt'),
        ('insight-wellness-website-mistakes.html',  '7 Website Mistakes Irish Wellness Businesses Make',                  'mistakes'),
        ('insight-online-booking-wellness.html',    'Online Booking for Wellness Businesses: What Actually Works',        'booking'),
    ]
    cards = ''
    for slug, title, _ in articles:
        cards += (
            '<a href="' + slug + '" class="insight-card">'
            '<div class="ic-tag">Guide</div>'
            '<div class="ic-title">' + title + '</div>'
            '<div class="ic-read">Read guide &rarr;</div>'
            '</a>'
        )
    return (
        page_head(
            'Web Design Insights for Health &amp; Wellness Businesses in Ireland | Kryson',
            'Guides, tips, and expert advice on web design, local SEO, and online booking for gyms, yoga studios, and wellness businesses across Ireland.',
            SITE_URL + '/insights'
        ) +
        NAV +
        '<div class="inner-hero-wrap">'
        '<div class="inner-hero">'
        '<div class="section-tag reveal">Insights &amp; Guides</div>'
        '<h1 class="inner-h1 reveal">Web design knowledge<br><span class="gt">for wellness businesses.</span></h1>'
        '<p class="inner-sub reveal">Practical guides on websites, SEO, and online booking for Irish gyms, studios, and wellness businesses.</p>'
        '</div>'
        '</div>'
        '<div class="page-body">'
        '<div class="insight-grid reveal">' + cards + '</div>'
        '</div>'
        '<section class="cta-band"><div class="cta-band-inner reveal">'
        '<h2>Ready to build your <span class="gt">website?</span></h2>'
        '<p>Custom wellness websites from &euro;497. Delivered in 7 days.</p>'
        '<div class="cta-btns">'
        '<a href="pricing.html" class="btn btn-grad">See Packages &amp; Buy &rarr;</a>'
        '<a href="work.html" class="btn btn-outline">View Our Work</a>'
        '</div>'
        '</div></section>'
        + page_foot()
    )

def build_insight_gym_cost():
    body = (
        '<p class="insight-intro">If you run a gym or fitness centre in Ireland and you&#39;re thinking about getting a website, the first question is usually the same: <strong>how much is this going to cost?</strong> The honest answer depends on what you actually need &mdash; and what you&#39;re willing to sacrifice.</p>'

        '<h2>DIY Website Builders (Wix, Squarespace): &euro;0&ndash;&euro;30/month</h2>'
        '<p>Tools like Wix and Squarespace let you build a site yourself using drag-and-drop templates. On the surface they look affordable. In practice, the problems compound quickly.</p>'
        '<p>Template designs are used by thousands of other businesses. Your gym looks like every other gym. Load times are slow because the platforms are bloated. SEO is limited &mdash; you can&#39;t add proper schema markup, you&#39;re restricted to basic meta tags, and your rankings suffer. There&#39;s also an ongoing monthly fee that adds up to &euro;360+ per year, forever, for something you don&#39;t own.</p>'
        '<p>For a gym with a serious reputation, a Wix site undermines trust before a prospective member has even read a word.</p>'

        '<h2>Freelance Developers: &euro;500&ndash;&euro;3,000</h2>'
        '<p>Hiring a freelance developer gives you more flexibility but comes with risk. Quality varies enormously. Timelines slip. Communication breaks down. And you rarely get the local SEO knowledge that&#39;s critical for a gym trying to rank in their area.</p>'

        '<h2>Agencies (General): &euro;3,000&ndash;&euro;10,000+</h2>'
        '<p>A general web agency will build you something, but they&#39;re not specialists in health and wellness. You&#39;ll spend time educating them about your industry, your members, and what your customers actually search for. The price reflects their overheads, not necessarily better results for you.</p>'

        '<h2>Kryson: &euro;497&ndash;&euro;1,497 (One-Time)</h2>'
        '<p>We build exclusively for health and wellness businesses in Ireland. No monthly fees, no templates, no lock-in. Our three packages cover every stage of business:</p>'
        '<ul class="insight-list">'
        '<li><strong>Starter (&euro;497)</strong> &mdash; Custom website up to 5 pages, mobile-first, Google Business setup, on-page SEO, JSON-LD schema. Delivered in 7 days.</li>'
        '<li><strong>Growth (&euro;997)</strong> &mdash; Everything in Starter plus Stripe payments, class booking system, advanced local SEO, Google Analytics 4. Delivered in 14 days.</li>'
        '<li><strong>Complete (&euro;1,497)</strong> &mdash; Everything in Growth plus a member portal, admin CRM, staff roster, transaction history, and review management. Delivered in 21 days.</li>'
        '</ul>'
        '<p>It&#39;s a one-time payment. You own everything outright. No ongoing fees to us.</p>'

        '<h2>What Should a Gym Website Actually Include?</h2>'
        '<p>Regardless of how you build it, a gym website in Ireland needs at minimum:</p>'
        '<ul class="insight-list">'
        '<li>A clear homepage with your location, class types, and pricing</li>'
        '<li>Mobile-responsive design (over 70% of searches are on mobile)</li>'
        '<li>A contact form or online booking system</li>'
        '<li>Google Business Profile integration</li>'
        '<li>Local SEO targeting your town/city (e.g. "gym in Galway", "fitness centre Dublin")</li>'
        '<li>Fast load times &mdash; under 3 seconds on mobile</li>'
        '</ul>'

        '<h2>The Real Cost of a Bad Website</h2>'
        '<p>A gym website that doesn&#39;t rank in local search, doesn&#39;t load on mobile, or looks outdated is actively costing you members every month. If even one new member signs up as a result of a professional website &mdash; at &euro;50&ndash;&euro;80/month &mdash; it pays for itself within a year. Most gyms see a return on their website investment within the first 2&ndash;3 months.</p>'
    )
    return (
        insight_head(
            'How Much Does a Gym Website Cost in Ireland? (2025 Guide) | Kryson',
            'A complete breakdown of gym website costs in Ireland &mdash; from Wix to custom builds. Understand what you&#39;re paying for and what actually gets results.',
            SITE_URL + '/insight-gym-website-cost-ireland',
            '2025-01-15'
        ) +
        NAV +
        '<div class="insight-hero-wrap">'
        '<div class="insight-hero-inner">'
        '<div class="section-tag"><a href="insights.html">Insights</a> &rsaquo; Cost Guide</div>'
        '<h1 class="insight-h1">How Much Does a Gym Website<br>Cost in Ireland? <span class="gt">(2025 Guide)</span></h1>'
        '<div class="insight-meta">5 min read &bull; Web Design &bull; Ireland</div>'
        '</div>'
        '</div>'
        '<div class="insight-body">'
        '<div class="insight-article">' + body + '</div>'
        + insight_cta() +
        '</div>'
        '<section class="cta-band"><div class="cta-band-inner reveal">'
        '<h2>Ready to get <span class="gt">started?</span></h2>'
        '<p>Custom gym website from &euro;497. One-time payment. No monthly fees.</p>'
        '<div class="cta-btns"><a href="pricing.html" class="btn btn-grad">See Packages &amp; Buy &rarr;</a></div>'
        '</div></section>'
        + page_foot()
    )

def build_insight_yoga():
    body = (
        '<p class="insight-intro">Most yoga studio websites in Ireland have the same problems: they&#39;re built on a generic template, they don&#39;t show up in local search, and there&#39;s no easy way for visitors to actually book a class. Here&#39;s what a proper yoga studio website needs &mdash; and why it matters.</p>'

        '<h2>1. A Clear Class Timetable</h2>'
        '<p>Your class schedule should be front and centre. Visitors want to know immediately: when are your classes, what styles do you teach, and where are you located? A cluttered or hidden timetable loses potential students before they&#39;ve even considered booking.</p>'
        '<p>The timetable should update without you needing a developer every time something changes. Ideally it connects to your booking system so class availability is shown in real time.</p>'

        '<h2>2. Online Booking and Payment</h2>'
        '<p>If students can&#39;t book and pay directly on your site, you&#39;re losing a significant portion of the people who visit. People make decisions in the moment. A "call us to book" instruction adds friction that kills conversions.</p>'
        '<p>Drop-in passes, class bundles, and monthly memberships should all be purchasable online via Stripe &mdash; directly on your website, without redirecting to a third-party platform.</p>'

        '<h2>3. Mobile-First Design</h2>'
        '<p>Over 75% of yoga studio searches in Ireland happen on a phone. If your website isn&#39;t optimised for mobile &mdash; fast loading, large tap targets, readable text without zooming &mdash; you&#39;re turning away the majority of potential students.</p>'
        '<p>Mobile-first means the mobile experience is designed first, not adapted from a desktop layout as an afterthought.</p>'

        '<h2>4. Local SEO</h2>'
        '<p>When someone searches "yoga classes Dublin" or "yoga studio near me", your site needs to appear. This requires:</p>'
        '<ul class="insight-list">'
        '<li>A fully optimised Google Business Profile with your address, hours, and reviews</li>'
        '<li>Page titles and meta descriptions targeting local keywords</li>'
        '<li>LocalBusiness JSON-LD schema markup</li>'
        '<li>Your studio listed in Irish business directories (Golden Pages, Yelp IE, etc.)</li>'
        '</ul>'

        '<h2>5. Your Story and Instructors</h2>'
        '<p>Yoga is personal. Students want to know who will be teaching them before they walk through the door. An About page with real photos of your instructors &mdash; their experience, styles, and personality &mdash; builds the trust that converts a curious visitor into a paying student.</p>'

        '<h2>6. Social Proof</h2>'
        '<p>Reviews and testimonials from real students are highly persuasive. A dedicated section with genuine Google reviews, or a curated wall of testimonials, can be the deciding factor for someone choosing between your studio and a competitor&#39;s.</p>'

        '<h2>What Does a Yoga Studio Website Cost in Ireland?</h2>'
        '<p>A professionally built yoga studio website starts at &euro;497 with Kryson &mdash; custom designed, mobile-first, with local SEO and Google Business setup included. If you need online booking and Stripe payments, that&#39;s our &euro;997 Growth package.</p>'
    )
    return (
        insight_head(
            'What Every Yoga Studio Website Needs to Convert Visitors | Kryson',
            'Six things every yoga studio website in Ireland needs to turn visitors into paying students &mdash; from class timetables to local SEO and mobile-first design.',
            SITE_URL + '/insight-yoga-studio-website',
            '2025-02-01'
        ) +
        NAV +
        '<div class="insight-hero-wrap">'
        '<div class="insight-hero-inner">'
        '<div class="section-tag"><a href="insights.html">Insights</a> &rsaquo; Yoga Studios</div>'
        '<h1 class="insight-h1">What Every Yoga Studio Website<br>Needs to <span class="gt">Convert Visitors</span></h1>'
        '<div class="insight-meta">4 min read &bull; Web Design &bull; Yoga Studios</div>'
        '</div>'
        '</div>'
        '<div class="insight-body">'
        '<div class="insight-article">' + body + '</div>'
        + insight_cta() +
        '</div>'
        '<section class="cta-band"><div class="cta-band-inner reveal">'
        '<h2>Ready to build your <span class="gt">yoga studio website?</span></h2>'
        '<p>Custom-designed, mobile-first, with booking and payments built in. From &euro;497.</p>'
        '<div class="cta-btns"><a href="pricing.html" class="btn btn-grad">See Packages &amp; Buy &rarr;</a></div>'
        '</div></section>'
        + page_foot()
    )

def build_insight_seo():
    body = (
        '<p class="insight-intro">If you run a gym, sauna, or fitness studio in Ireland, local SEO is the single highest-return investment you can make in your marketing. When someone searches "gym near me" or "pilates classes Cork", appearing at the top of those results sends you customers who are already ready to buy &mdash; for free.</p>'

        '<h2>What Is Local SEO?</h2>'
        '<p>Local SEO is the process of optimising your online presence so your business appears when people nearby search for what you offer. Unlike paid advertising, local SEO drives ongoing organic traffic &mdash; you pay once to set it up properly, and it keeps working indefinitely.</p>'

        '<h2>Step 1: Your Google Business Profile</h2>'
        '<p>Your Google Business Profile (GBP) is the most important local SEO asset you have. It&#39;s the listing that appears in Google Maps and the "local pack" (the three businesses shown at the top of local search results).</p>'
        '<p>To optimise your GBP:</p>'
        '<ul class="insight-list">'
        '<li>Verify your business with a postcode</li>'
        '<li>Add accurate opening hours (and update them for bank holidays)</li>'
        '<li>Upload high-quality photos of your facilities &mdash; at least 10</li>'
        '<li>Write a keyword-rich business description (e.g. "CrossFit box in Limerick...")</li>'
        '<li>Choose the right primary and secondary categories</li>'
        '<li>Post updates at least once per week</li>'
        '</ul>'

        '<h2>Step 2: On-Page SEO for Your Website</h2>'
        '<p>Your website needs to signal to Google exactly what you do and where you are. Every page should have:</p>'
        '<ul class="insight-list">'
        '<li>A title tag containing your main keyword and location (e.g. "Yoga Classes in Dublin | Studio Name")</li>'
        '<li>A meta description that includes your city and a clear benefit</li>'
        '<li>Your address and phone number in the footer (matching your Google Business Profile exactly)</li>'
        '<li>An embedded Google Map on your contact page</li>'
        '<li>LocalBusiness JSON-LD schema markup &mdash; this tells Google your name, address, hours, and service area in structured form</li>'
        '</ul>'

        '<h2>Step 3: Local Keywords in Your Content</h2>'
        '<p>Write content that targets the phrases your customers actually search. For an Irish fitness business, that includes:</p>'
        '<ul class="insight-list">'
        '<li>"[your service] in [your city]" &mdash; e.g. "personal trainer in Galway"</li>'
        '<li>"[your service] near me" pages targeting your area</li>'
        '<li>Blog posts answering local questions ("best gyms in Cork", "how to start yoga in Dublin")</li>'
        '</ul>'

        '<h2>Step 4: Local Citations</h2>'
        '<p>Citations are mentions of your business name, address, and phone number on other websites. Consistent citations on directories like Golden Pages, Yelp Ireland, and local business directories tell Google you&#39;re a legitimate local business &mdash; which boosts your Maps ranking.</p>'

        '<h2>Step 5: Reviews</h2>'
        '<p>Google reviews directly influence your local ranking. Businesses with more reviews and higher ratings rank higher. Build a simple process for asking satisfied members to leave a review &mdash; a follow-up text, an email, or a card handed out after their session. Even getting from 3 reviews to 15 can move you from page 2 to the top 3.</p>'

        '<h2>How Long Does Local SEO Take?</h2>'
        '<p>You&#39;ll typically see movement in Google Maps rankings within 4&ndash;8 weeks of properly optimising your GBP and website. Organic search results take 3&ndash;6 months. The businesses that invest in SEO early and maintain it consistently dominate their local area for years.</p>'
    )
    return (
        insight_head(
            'Local SEO for Gyms &amp; Fitness Studios in Ireland: A Practical Guide | Kryson',
            'How to rank higher in local search for your gym, yoga studio, or wellness business in Ireland. Google Business Profile, on-page SEO, citations, and reviews explained.',
            SITE_URL + '/insight-local-seo-fitness-ireland',
            '2025-02-15'
        ) +
        NAV +
        '<div class="insight-hero-wrap">'
        '<div class="insight-hero-inner">'
        '<div class="section-tag"><a href="insights.html">Insights</a> &rsaquo; Local SEO</div>'
        '<h1 class="insight-h1">Local SEO for Gyms &amp; Fitness<br>Studios in <span class="gt">Ireland</span></h1>'
        '<div class="insight-meta">6 min read &bull; Local SEO &bull; Ireland</div>'
        '</div>'
        '</div>'
        '<div class="insight-body">'
        '<div class="insight-article">' + body + '</div>'
        + insight_cta() +
        '</div>'
        '<section class="cta-band"><div class="cta-band-inner reveal">'
        '<h2>Want local SEO <span class="gt">built in?</span></h2>'
        '<p>Every Kryson website includes schema markup, Google Business setup, and on-page SEO targeting your area.</p>'
        '<div class="cta-btns"><a href="pricing.html" class="btn btn-grad">See Packages &amp; Buy &rarr;</a></div>'
        '</div></section>'
        + page_foot()
    )

def build_insight_pt():
    body = (
        '<p class="insight-intro">A lot of personal trainers in Ireland rely entirely on Instagram and word of mouth. It works &mdash; until it doesn&#39;t. A website isn&#39;t just a nice-to-have. For a PT serious about building a sustainable client base, it&#39;s essential.</p>'

        '<h2>Instagram Followers Don&#39;t Equal Clients</h2>'
        '<p>Social media is great for visibility and engagement, but it&#39;s a platform you don&#39;t own. The algorithm changes. Reach drops. Your account could be restricted or compromised. And critically &mdash; Instagram isn&#39;t where people go when they&#39;re ready to book a session.</p>'
        '<p>When someone decides they want a personal trainer in Dublin or Cork, they search Google. If you don&#39;t have a website, you don&#39;t exist in that moment. The client goes to someone who does.</p>'

        '<h2>What a PT Website Should Do</h2>'
        '<p>A good personal trainer website isn&#39;t just a digital business card. It should actively convert visitors into paying clients. That means:</p>'
        '<ul class="insight-list">'
        '<li><strong>Clear service pages</strong> &mdash; 1-on-1 sessions, online coaching, nutrition plans. Each with pricing.</li>'
        '<li><strong>Online booking</strong> &mdash; Let clients book a consultation or their first session without picking up the phone.</li>'
        '<li><strong>Payment links</strong> &mdash; Take session packages and monthly retainer payments directly online via Stripe.</li>'
        '<li><strong>Transformation results</strong> &mdash; Before/after results (with client permission) and testimonials build trust fast.</li>'
        '<li><strong>About page with a real photo</strong> &mdash; People hire PTs they connect with. Your qualifications, your story, and your training philosophy matter.</li>'
        '</ul>'

        '<h2>Local SEO for Personal Trainers</h2>'
        '<p>The highest-intent searches for a PT look like this: "personal trainer Dublin 2", "online personal trainer Ireland", "personal trainer near Dundrum". Ranking for these terms puts you in front of people who are actively looking to hire &mdash; not just browse.</p>'
        '<p>A properly built website with local SEO can generate a consistent flow of inbound enquiries. Even one new long-term client per month from your website at &euro;200&ndash;&euro;400/month pays for the site many times over in year one.</p>'

        '<h2>What About Just Using a Booking App?</h2>'
        '<p>Apps like Calendly, Acuity, or Mindbody are useful tools &mdash; but they don&#39;t replace a website. They don&#39;t rank in Google. They don&#39;t tell your story. And they send clients to a generic platform rather than your brand. A proper website integrates booking and payment directly, keeping clients on your domain.</p>'

        '<h2>How Much Does a Personal Trainer Website Cost?</h2>'
        '<p>A custom PT website with Kryson starts at &euro;497 for the Starter package &mdash; a fully designed, mobile-first site with local SEO. If you want Stripe payments and online booking built in, that&#39;s the &euro;997 Growth package. Both are one-time payments. No monthly fees to us.</p>'
    )
    return (
        insight_head(
            'Do Personal Trainers in Ireland Need a Website? Yes &mdash; Here&#39;s Why | Kryson',
            'Why Instagram and word of mouth aren&#39;t enough for Irish personal trainers &mdash; and what a proper PT website should include to generate consistent clients.',
            SITE_URL + '/insight-personal-trainer-website',
            '2025-03-01'
        ) +
        NAV +
        '<div class="insight-hero-wrap">'
        '<div class="insight-hero-inner">'
        '<div class="section-tag"><a href="insights.html">Insights</a> &rsaquo; Personal Trainers</div>'
        '<h1 class="insight-h1">Do Personal Trainers in Ireland<br>Need a Website? <span class="gt">Yes.</span></h1>'
        '<div class="insight-meta">4 min read &bull; Web Design &bull; Personal Trainers</div>'
        '</div>'
        '</div>'
        '<div class="insight-body">'
        '<div class="insight-article">' + body + '</div>'
        + insight_cta() +
        '</div>'
        '<section class="cta-band"><div class="cta-band-inner reveal">'
        '<h2>Build your PT website <span class="gt">today.</span></h2>'
        '<p>From &euro;497. Custom design, booking, payments, and local SEO. Delivered in 7 days.</p>'
        '<div class="cta-btns"><a href="pricing.html" class="btn btn-grad">See Packages &amp; Buy &rarr;</a></div>'
        '</div></section>'
        + page_foot()
    )

def build_insight_mistakes():
    mistakes = [
        ('No Mobile Optimisation',
         'More than 70% of health and wellness searches in Ireland happen on a phone. If your website isn&#39;t designed mobile-first &mdash; fast, readable, easy to navigate on a small screen &mdash; you&#39;re turning away the majority of your potential customers before they&#39;ve seen anything about your business.'),
        ('Slow Load Times',
         'Google research shows that 53% of mobile visitors leave a page that takes longer than 3 seconds to load. Template-built sites loaded with stock photos and unused plugins regularly take 6&ndash;10 seconds. Every extra second costs you members and ranking.'),
        ('No Local SEO',
         'Having a website and being findable in local search are two different things. Without proper Google Business Profile setup, location-targeted title tags, and LocalBusiness schema markup, your site won&#39;t appear when people search "gym near me" or "yoga Dublin" &mdash; the searches with the highest buying intent.'),
        ('No Online Booking or Payment',
         'Making people call or email to book a class introduces friction that kills conversions. In 2025, customers expect to book and pay online in under 60 seconds. If your competitors offer this and you don&#39;t, you&#39;re losing clients who never even contact you.'),
        ('Generic Template Design',
         'Wix and Squarespace templates are used by thousands of businesses. When your gym or studio looks identical to every other wellness business online, you fail to build trust or differentiate your brand. Custom design builds credibility before anyone reads a single word.'),
        ('No Social Proof',
         'Real Google reviews, member testimonials, and before/after transformations (where relevant) are highly persuasive. A wellness website with zero reviews or testimonials looks like an unestablished business. Building social proof into your site &mdash; and making it easy for members to leave reviews &mdash; is one of the highest-return changes you can make.'),
        ('No Clear Call to Action',
         'Many wellness websites bury the most important action: join, book, or buy. Every page should have one primary call to action that&#39;s visible without scrolling. "View Membership Options", "Book a Free Trial", "Buy a Class Pack" &mdash; clear, prominent, and linked directly to the action.'),
    ]
    body = '<p class="insight-intro">After building websites for health and wellness businesses across Ireland, we&#39;ve seen the same mistakes repeatedly. Here are the seven that cost Irish wellness businesses the most customers &mdash; and how to fix them.</p>'
    for i, (title, text) in enumerate(mistakes, 1):
        body += (
            '<h2>' + str(i) + '. ' + title + '</h2>'
            '<p>' + text + '</p>'
        )
    body += '<p>If your website has any of these issues, they&#39;re actively costing you members every month. A professional rebuild pays for itself when even one additional client signs up as a result.</p>'
    return (
        insight_head(
            '7 Website Mistakes Irish Wellness Businesses Make (And How to Fix Them) | Kryson',
            'The seven most common website mistakes made by gyms, yoga studios, and wellness businesses in Ireland &mdash; and exactly how to fix each one.',
            SITE_URL + '/insight-wellness-website-mistakes',
            '2025-03-15'
        ) +
        NAV +
        '<div class="insight-hero-wrap">'
        '<div class="insight-hero-inner">'
        '<div class="section-tag"><a href="insights.html">Insights</a> &rsaquo; Web Design</div>'
        '<h1 class="insight-h1">7 Website Mistakes Irish Wellness<br><span class="gt">Businesses Make</span></h1>'
        '<div class="insight-meta">5 min read &bull; Web Design &bull; Ireland</div>'
        '</div>'
        '</div>'
        '<div class="insight-body">'
        '<div class="insight-article">' + body + '</div>'
        + insight_cta() +
        '</div>'
        '<section class="cta-band"><div class="cta-band-inner reveal">'
        '<h2>None of these mistakes<br>on <span class="gt">your website.</span></h2>'
        '<p>Every Kryson site is custom-built, mobile-first, and optimised for local search from day one.</p>'
        '<div class="cta-btns"><a href="pricing.html" class="btn btn-grad">See Packages &amp; Buy &rarr;</a></div>'
        '</div></section>'
        + page_foot()
    )

def build_insight_booking():
    body = (
        '<p class="insight-intro">Online booking is one of the highest-impact additions you can make to a wellness business website. But not all booking solutions are created equal. Here&#39;s what actually works for Irish gyms, studios, and wellness businesses &mdash; and what to avoid.</p>'

        '<h2>Why Online Booking Matters</h2>'
        '<p>Clients make decisions in moments. If someone is on your website at 10pm on a Tuesday thinking about joining your yoga class, and they can&#39;t book immediately, the moment passes. They&#39;ll either forget or find a competitor who lets them book instantly.</p>'
        '<p>Businesses that add online booking typically see a 20&ndash;40% increase in new client conversions. Not because they&#39;re getting more traffic &mdash; but because they&#39;re converting the traffic they already have.</p>'

        '<h2>Option 1: Direct Stripe Payment Links (Simplest)</h2>'
        '<p>For wellness businesses just starting out, Stripe Payment Links are the fastest path to taking online payments. You create a link for each product (e.g. "10-class bundle &mdash; &euro;120") and embed it directly on your website. Customers pay in 30 seconds. Money lands in your account.</p>'
        '<p>This works well for class bundles, membership sign-ups, personal training packages, and gift vouchers. It doesn&#39;t handle class scheduling, but it removes the biggest barrier &mdash; payment friction.</p>'

        '<h2>Option 2: Integrated Booking + Payment (Recommended)</h2>'
        '<p>For businesses with a regular class timetable, an integrated booking system lets customers see available slots and book (and pay) in real time. Built into your website via Stripe, this means:</p>'
        '<ul class="insight-list">'
        '<li>Customers select a class and time directly on your site</li>'
        '<li>They pay immediately via Stripe</li>'
        '<li>You receive a booking notification</li>'
        '<li>Class capacity is tracked automatically</li>'
        '</ul>'
        '<p>This is included in Kryson&#39;s Growth package (&euro;997).</p>'

        '<h2>Option 3: Member Portal (Full Infrastructure)</h2>'
        '<p>For established wellness businesses with a significant member base, a member portal takes booking to the next level. Members log in, view their membership status, manage their subscription, and book classes &mdash; all within your branded website. No third-party app. No redirects. Everything under your control.</p>'
        '<p>This is what we built for Pikenhot.ie &mdash; a gym and sauna centre in Ireland. Members self-manage their accounts, payment history is tracked, and the admin has a full CRM dashboard. This is our Complete package (&euro;1,497).</p>'

        '<h2>What to Avoid</h2>'
        '<ul class="insight-list">'
        '<li><strong>Generic booking apps bolted on as iframes</strong> &mdash; They break the design, load slowly, and send customers to a third-party domain.</li>'
        '<li><strong>Facebook-only booking</strong> &mdash; You don&#39;t own your audience. A platform change or account issue can cut off your bookings entirely.</li>'
        '<li><strong>Email-only enquiry forms</strong> &mdash; These introduce unnecessary delay. Every hour between a customer&#39;s enquiry and your reply is a chance for them to book elsewhere.</li>'
        '</ul>'

        '<h2>The Simple Recommendation</h2>'
        '<p>Start with Stripe payment links on your website. If you have a class timetable, add integrated booking (Growth package). If you have 50+ members, invest in a member portal (Complete package). Each step pays for itself quickly.</p>'
    )
    return (
        insight_head(
            'Online Booking for Wellness Businesses: What Actually Works | Kryson',
            'A practical guide to online booking systems for Irish gyms, yoga studios, and wellness businesses &mdash; Stripe links, integrated booking, and member portals explained.',
            SITE_URL + '/insight-online-booking-wellness',
            '2025-04-01'
        ) +
        NAV +
        '<div class="insight-hero-wrap">'
        '<div class="insight-hero-inner">'
        '<div class="section-tag"><a href="insights.html">Insights</a> &rsaquo; Booking Systems</div>'
        '<h1 class="insight-h1">Online Booking for Wellness<br>Businesses: <span class="gt">What Works</span></h1>'
        '<div class="insight-meta">5 min read &bull; Bookings &amp; Payments &bull; Ireland</div>'
        '</div>'
        '</div>'
        '<div class="insight-body">'
        '<div class="insight-article">' + body + '</div>'
        + insight_cta() +
        '</div>'
        '<section class="cta-band"><div class="cta-band-inner reveal">'
        '<h2>Get booking &amp; payments<br><span class="gt">built into your site.</span></h2>'
        '<p>Stripe-integrated. No third-party apps. Starts at &euro;997.</p>'
        '<div class="cta-btns"><a href="pricing.html" class="btn btn-grad">See Packages &amp; Buy &rarr;</a></div>'
        '</div></section>'
        + page_foot()
    )

# ============================================================
# BUILD ALL
# ============================================================

def main():
    pages = {
        'index.html':   build_index(),
        'pricing.html': build_pricing(),
        'work.html':    build_work(),
        'about.html':   build_about(),
        'contact.html': build_contact(),
        'insights.html':                        build_insights(),
        'insight-gym-website-cost-ireland.html': build_insight_gym_cost(),
        'insight-yoga-studio-website.html':      build_insight_yoga(),
        'insight-local-seo-fitness-ireland.html':build_insight_seo(),
        'insight-personal-trainer-website.html': build_insight_pt(),
        'insight-wellness-website-mistakes.html':build_insight_mistakes(),
        'insight-online-booking-wellness.html':  build_insight_booking(),
    }
    for filename, html in pages.items():
        path = os.path.join(BASE_DIR, filename)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print('Built: ' + filename)

    sitemap_path = os.path.join(BASE_DIR, 'sitemap.xml')
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(build_sitemap())
    print('Built: sitemap.xml')

    robots_path = os.path.join(BASE_DIR, 'robots.txt')
    with open(robots_path, 'w', encoding='utf-8') as f:
        f.write('User-agent: *\nAllow: /\nSitemap: ' + SITE_URL + '/sitemap.xml\n')
    print('Built: robots.txt')

    print('Done!')

if __name__ == '__main__':
    main()
