import os

def fix_paths(html):
    base = '../'
    html = html.replace('href="styles.css"', 'href="' + base + 'styles.css"')
    html = html.replace('"Kryson Logos.png"', '"' + base + 'Kryson Logos.png"')
    for page in ['index.html','services.html','results.html','about.html','insights.html','faq.html']:
        html = html.replace('href="' + page + '"', 'href="' + base + page + '"')
        html = html.replace('href="' + page + '#', 'href="' + base + page + '#')
    return html

NAV = '''<nav id="nav">
<a href="index.html" class="logo">
<svg viewBox="0 0 520 120" xmlns="http://www.w3.org/2000/svg"><text x="0" y="95" font-family="'Times New Roman','CG Times',Times,serif" font-size="120" fill="#FFF" letter-spacing="2">K</text><line x1="62" y1="30" x2="78" y2="10" stroke="#FFF" stroke-width="3.5" stroke-linecap="round"/><polygon points="78,2 85,12 76,14" fill="#FFF"/><text x="82" y="95" font-family="'Times New Roman','CG Times',Times,serif" font-size="76" fill="#FFF" letter-spacing="16">RYSON</text></svg>
</a>
<div class="nr">
<a href="services.html" class="na">What We Do</a>
<a href="results.html" class="na">Results</a>
<a href="about.html" class="na">About</a>
<a href="insights.html" class="na">Insights</a>
<a href="faq.html" class="na">FAQ</a>
<a href="javascript:void(0)" onclick="openApplyModal()"><button class="nb">Apply Now</button></a>
</div>
<button class="burger" id="burg"><span></span><span></span><span></span></button>
</nav>
<div class="mob" id="mob">
<button class="mob-x" id="mobX">&times;</button>
<a href="services.html" class="ml">What We Do</a>
<a href="results.html" class="ml">Results</a>
<a href="about.html" class="ml">About</a>
<a href="insights.html" class="ml">Insights</a>
<a href="about.html#careers" class="ml">Careers</a>
<a href="faq.html" class="ml">FAQ</a>
<a href="javascript:void(0)" onclick="openApplyModal()" class="ml" style="color:var(--gold)">Apply Now</a>
</div>'''

LOADER = '''<div id="loader">
<div class="l-half l-top"></div>
<div class="l-half l-bot"></div>
<div class="l-center">
<div class="l-text" id="lt"></div>
<div class="l-bar" id="lb"></div>
</div>
</div>'''

KG_BAND = '''<div class="kg-band">
<div class="kg-band-inner">
<span class="kg-band-text">Kryson Limited is a member of the <strong>Kryson Group</strong></span>
<span class="kg-band-divider">|</span>
<span class="kg-band-sub">A privately held group of commercial advisory and service businesses</span>
</div>
</div>'''

FOOTER = '''<footer>
<div class="fg">
<div class="fb">
<a href="index.html" class="logo">
<svg viewBox="0 0 520 120" xmlns="http://www.w3.org/2000/svg" style="height:20px;width:auto"><text x="0" y="95" font-family="'Times New Roman','CG Times',Times,serif" font-size="120" fill="#C9A84C" letter-spacing="2">K</text><line x1="62" y1="30" x2="78" y2="10" stroke="#C9A84C" stroke-width="3.5" stroke-linecap="round"/><polygon points="78,2 85,12 76,14" fill="#C9A84C"/><text x="82" y="95" font-family="'Times New Roman','CG Times',Times,serif" font-size="76" fill="#C9A84C" letter-spacing="16">RYSON</text></svg>
</a>
<p>Revenue Architecture for Founder-Led B2B Companies</p>
</div>
<div class="fc"><h5>Navigate</h5><ul>
<li><a href="services.html">What We Do</a></li>
<li><a href="results.html">Results</a></li>
<li><a href="about.html">About</a></li>
<li><a href="insights.html">Insights</a></li>
<li><a href="about.html#careers">Careers</a></li>
<li><a href="faq.html">FAQ</a></li>
</ul></div>
<div class="fc"><h5>Contact</h5><ul>
<li><a href="mailto:Kyle@krysongroup.com" style="color:var(--gold)">Kyle@krysongroup.com</a></li>
<li><span style="color:var(--w40)">UK &amp; Ireland</span></li>
</ul></div>
</div>
<div class="fbot">
<span>&copy; 2026 Kryson Limited. All rights reserved.</span>
<div><a href="#">Privacy</a> &middot; <a href="#">Terms</a></div>
</div>
</footer>'''

APPS_SCRIPT_URL = 'https://script.google.com/a/macros/krysongroup.com/s/AKfycbyFAabkwB0JALB8t9LQYbPghN-MEdYnlPDqygc-38xtaay1q2C28lz6zcZFrkB0x5Dl/exec'

APPLICATION_MODAL = (
'<div class="am-ov" id="applyModal">'
'<div class="am-box" id="amBox">'
'<button class="am-close" onclick="closeApplyModal()" aria-label="Close">&times;</button>'

# Progress bar
'<div class="am-prog"><div class="am-prog-bar" id="amBar" style="width:25%"></div></div>'

# Step 1 — Revenue gate
'<div class="am-step active" id="amS1">'
'<div class="am-eye">Step 1 of 3</div>'
'<h3 class="am-h">What is your agency\'s current monthly revenue?</h3>'
'<div class="am-opts">'
'<button class="am-opt" onclick="amPick(this,1)" data-val="low">Under &pound;10,000 / month</button>'
'<button class="am-opt" onclick="amPick(this,1)" data-val="mid">&pound;10,000 &ndash; &pound;30,000 / month</button>'
'<button class="am-opt" onclick="amPick(this,1)" data-val="high">&pound;30,000 &ndash; &pound;80,000 / month</button>'
'<button class="am-opt" onclick="amPick(this,1)" data-val="top">Over &pound;80,000 / month</button>'
'</div>'
'</div>'

# Step 2 — Sales bottleneck
'<div class="am-step" id="amS2">'
'<div class="am-eye">Step 2 of 3</div>'
'<h3 class="am-h">Where is your biggest revenue bottleneck right now?</h3>'
'<div class="am-opts">'
'<button class="am-opt" onclick="amPick(this,2)" data-val="conv">Low call-to-close rate</button>'
'<button class="am-opt" onclick="amPick(this,2)" data-val="pipe">Pipeline dries up when I\'m busy delivering</button>'
'<button class="am-opt" onclick="amPick(this,2)" data-val="vis">No visibility. I cannot forecast next month with confidence</button>'
'<button class="am-opt" onclick="amPick(this,2)" data-val="team">Trying to build or fix a sales team</button>'
'</div>'
'</div>'

# Step 3 — Timeline
'<div class="am-step" id="amS3">'
'<div class="am-eye">Step 3 of 3</div>'
'<h3 class="am-h">How soon are you looking to fix this?</h3>'
'<div class="am-opts">'
'<button class="am-opt" onclick="amPick(this,3)" data-val="now">Right now. It is costing me today</button>'
'<button class="am-opt" onclick="amPick(this,3)" data-val="soon">Within the next 30 days</button>'
'<button class="am-opt" onclick="amPick(this,3)" data-val="plan">Planning for next quarter</button>'
'</div>'
'</div>'

# Step 4 — Contact form
'<div class="am-step" id="amS4">'
'<div class="am-eye">Almost there</div>'
'<h3 class="am-h">Where should we send the audit confirmation?</h3>'
'<form class="am-form" id="amForm" onsubmit="amSubmit(event)">'
'<div class="am-row">'
'<div class="am-field"><label>First name</label><input type="text" id="amFirst" placeholder="James" required></div>'
'<div class="am-field"><label>Last name</label><input type="text" id="amLast" placeholder="Whitfield" required></div>'
'</div>'
'<div class="am-field"><label>Work email</label><input type="email" id="amEmail" placeholder="james@agency.com" required></div>'
'<div class="am-field"><label>Phone number</label><input type="tel" id="amPhone" placeholder="+44 7700 000000" required></div>'
'<button type="submit" class="btn bp am-submit" id="amSubmitBtn" style="width:100%;margin-top:20px;font-size:12px;padding:16px 28px;letter-spacing:2px">Submit Application &rarr;</button>'
'<p class="am-note">We review every application personally. If you\'re a fit, you\'ll hear from us within 24 hours.</p>'
'</form>'
'</div>'

# Result — Qualified
'<div class="am-step am-result" id="amGo">'
'<div class="am-tick">&#10003;</div>'
'<h3 class="am-h am-h-ok">Application received.</h3>'
'<p class="am-p">Calendly has opened in a new tab. Pick a time that works and we will take it from there.</p>'
'<p class="am-p">If it didn\'t open, use the link below.</p>'
'<a href="https://calendly.com/kyle-krysongroup/introduction" target="_blank" class="btn bp am-book-btn" style="font-size:12px;padding:14px 32px;letter-spacing:2px;display:inline-block;margin-top:16px">Open Calendly &rarr;</a>'
'<p class="am-note">We take a maximum of 5 clients per quarter. Spots are reviewed in order of application.</p>'
'</div>'

# Result — Submitting
'<div class="am-step am-result" id="amSending">'
'<div class="am-spin"></div>'
'<p class="am-p" style="margin-top:20px">Submitting your application...</p>'
'</div>'

# Result — DQ
'<div class="am-step am-result" id="amNo">'
'<div class="am-cross">&#8212;</div>'
'<h3 class="am-h">Not quite the right fit yet.</h3>'
'<p class="am-p">Our work is best suited to agencies doing at least &pound;10,000 per month. At that stage the commercial infrastructure work we do has the most impact.</p>'
'<p class="am-p">If you\'re building toward that, we\'d encourage you to revisit when you\'re there.</p>'
'<button onclick="closeApplyModal()" class="btn bs" style="font-size:11px;padding:12px 24px;margin-top:16px;border-color:var(--w20)">Close</button>'
'</div>'

'</div>'
'</div>'
)

CALENDLY_BADGE = ''

CDN = (
'<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>\n'
'<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>\n'
'<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>'
)

SHARED_JS = r"""
function initP(id,n){
const cv=document.getElementById(id);if(!cv)return;
const pa=cv.parentElement;
const scene=new THREE.Scene();
const cam=new THREE.PerspectiveCamera(75,pa.clientWidth/pa.clientHeight,.1,1000);
const r=new THREE.WebGLRenderer({canvas:cv,alpha:true,antialias:false});
r.setSize(pa.clientWidth,pa.clientHeight);r.setPixelRatio(1);
const pos=new Float32Array(n*3);const vel=[];
for(let i=0;i<n;i++){pos[i*3]=(Math.random()-.5)*20;pos[i*3+1]=(Math.random()-.5)*12;pos[i*3+2]=(Math.random()-.5)*8;vel.push({vx:(Math.random()-.5)*.0015,vy:(Math.random()-.5)*.0015,vz:0});}
const ptGeo=new THREE.BufferGeometry();const ptBuf=new THREE.BufferAttribute(pos,3);ptBuf.setUsage(THREE.DynamicDrawUsage);ptGeo.setAttribute('position',ptBuf);
scene.add(new THREE.Points(ptGeo,new THREE.PointsMaterial({color:0xC9A84C,size:.035,transparent:true,opacity:.4,blending:THREE.AdditiveBlending,depthWrite:false})));
const maxLines=n*(n-1)/2;const lineBuf=new Float32Array(maxLines*6);const lineGeo=new THREE.BufferGeometry();const lineAttr=new THREE.BufferAttribute(lineBuf,3);lineAttr.setUsage(THREE.DynamicDrawUsage);lineGeo.setAttribute('position',lineAttr);lineGeo.setDrawRange(0,0);
scene.add(new THREE.LineSegments(lineGeo,new THREE.LineBasicMaterial({color:0xC9A84C,transparent:true,opacity:.04,blending:THREE.AdditiveBlending,depthWrite:false})));
cam.position.z=6;let visible=true;
const obs=new IntersectionObserver(e=>{visible=e[0].isIntersecting},{threshold:0});obs.observe(pa);
function tick(){requestAnimationFrame(tick);if(!visible)return;
for(let i=0;i<n;i++){pos[i*3]+=vel[i].vx;pos[i*3+1]+=vel[i].vy;if(Math.abs(pos[i*3])>10)vel[i].vx*=-1;if(Math.abs(pos[i*3+1])>6)vel[i].vy*=-1;}
ptBuf.needsUpdate=true;let lc=0;
for(let i=0;i<n;i++)for(let j=i+1;j<n;j++){const dx=pos[i*3]-pos[j*3],dy=pos[i*3+1]-pos[j*3+1];if(dx*dx+dy*dy<6.25){const b=lc*6;lineBuf[b]=pos[i*3];lineBuf[b+1]=pos[i*3+1];lineBuf[b+2]=pos[i*3+2];lineBuf[b+3]=pos[j*3];lineBuf[b+4]=pos[j*3+1];lineBuf[b+5]=pos[j*3+2];lc++;}}
lineAttr.needsUpdate=true;lineGeo.setDrawRange(0,lc*2);r.render(scene,cam);}
tick();window.addEventListener('resize',()=>{cam.aspect=pa.clientWidth/pa.clientHeight;cam.updateProjectionMatrix();r.setSize(pa.clientWidth,pa.clientHeight)},{passive:true});}

gsap.registerPlugin(ScrollTrigger);
document.querySelectorAll('.rv').forEach(el=>{gsap.to(el,{scrollTrigger:{trigger:el,start:'top 88%'},opacity:1,y:0,duration:.5,ease:'power2.out'})});
document.querySelectorAll('.ctr').forEach(c=>{ScrollTrigger.create({trigger:c,start:'top 90%',once:true,onEnter:()=>{const t=parseFloat(c.dataset.to),pre=c.dataset.pre||'',suf=c.dataset.suf||'';const s=performance.now();!function u(now){const p=Math.min((now-s)/1500,1);c.textContent=pre+(t*(1-Math.pow(1-p,3))).toFixed(1)+suf;if(p<1)requestAnimationFrame(u)}(s)}})});
const fv=document.querySelector('.funnel-vis');if(fv){ScrollTrigger.create({trigger:fv,start:'top 80%',once:true,onEnter:()=>{document.querySelectorAll('.funnel-fill').forEach((f,i)=>{setTimeout(()=>{f.style.width=f.dataset.width+'%'},i*180)})}})}
document.querySelectorAll('.sb-item').forEach(s=>{ScrollTrigger.create({trigger:s,start:'top 85%',once:true,onEnter:()=>s.classList.add('vis')})});
const tl=document.querySelector('.tl');if(tl){ScrollTrigger.create({trigger:tl,start:'top 70%',onEnter:()=>{document.getElementById('tlF')&&(document.getElementById('tlF').style.height='100%');document.querySelectorAll('.ts').forEach((s,i)=>{gsap.to(s,{opacity:1,y:0,duration:.45,delay:.15+i*.12,ease:'power2.out',onComplete:()=>s.classList.add('on')})})}})}
document.querySelectorAll('.fq-q').forEach(b=>{b.addEventListener('click',()=>{const f=b.parentElement,a=f.querySelector('.fq-a'),o=f.classList.contains('open');document.querySelectorAll('.fq.open').forEach(x=>{x.classList.remove('open');x.querySelector('.fq-a').style.maxHeight='0'});if(!o){f.classList.add('open');a.style.maxHeight=a.scrollHeight+'px'}})});
function toggleCase(top){const c=top.parentElement,b=c.querySelector('.case-body'),o=c.classList.contains('open');document.querySelectorAll('.case.open').forEach(x=>{x.classList.remove('open');x.querySelector('.case-body').style.maxHeight='0'});if(!o){c.classList.add('open');b.style.maxHeight=b.scrollHeight+'px'}}
function toggleIns(el){const item=el.closest('.ins-item'),body=item.querySelector('.ins-body'),open=item.classList.contains('open');document.querySelectorAll('.ins-item.open').forEach(x=>{x.classList.remove('open');x.querySelector('.ins-body').style.maxHeight='0'});if(!open){item.classList.add('open');body.style.maxHeight=body.scrollHeight+'px'}}
const burg=document.getElementById('burg'),mob=document.getElementById('mob'),mobX=document.getElementById('mobX');
burg.addEventListener('click',()=>{mob.classList.add('open');document.body.style.overflow='hidden'});
mobX.addEventListener('click',()=>{mob.classList.remove('open');document.body.style.overflow=''});
document.querySelectorAll('.ml').forEach(l=>{l.addEventListener('click',()=>{mob.classList.remove('open');document.body.style.overflow=''})});
document.querySelectorAll('a[href^="#"]').forEach(a=>{
  a.addEventListener('click',function(e){const href=this.getAttribute('href');if(href==='#')return;e.preventDefault();const t=document.querySelector(href);if(t)window.scrollTo({top:t.getBoundingClientRect().top+window.pageYOffset-64,behavior:'smooth'})});
});
var amRev=null,amBottleneck=null,amTimeline=null;
var progMap={amS1:25,amS2:50,amS3:75,amS4:95,amGo:100,amNo:100,amSending:95};
function openApplyModal(){setTimeout(function(){var el=document.getElementById('applyModal');if(!el)return;amShow('amS1');el.classList.add('open');document.body.style.overflow='hidden'},20);}
function closeApplyModal(){var el=document.getElementById('applyModal');if(!el)return;el.classList.remove('open');document.body.style.overflow='';}
function amShow(id){document.querySelectorAll('.am-step').forEach(function(s){s.classList.remove('active')});var t=document.getElementById(id);if(t)t.classList.add('active');var bar=document.getElementById('amBar');if(bar&&progMap[id])bar.style.width=progMap[id]+'%';}
function amPick(btn,step){var v=btn.getAttribute('data-val');
  btn.parentElement.querySelectorAll('.am-opt').forEach(function(b){b.classList.remove('sel')});btn.classList.add('sel');
  setTimeout(function(){
    if(step===1){amRev=v;if(v==='low'){amShow('amNo');}else{amShow('amS2');}}
    else if(step===2){amBottleneck=btn.textContent.trim();amShow('amS3');}
    else if(step===3){amTimeline=btn.textContent.trim();amShow('amS4');}
  },280);
}
function amSubmit(e){e.preventDefault();
  var first=document.getElementById('amFirst').value.trim();
  var last=document.getElementById('amLast').value.trim();
  var email=document.getElementById('amEmail').value.trim();
  var phone=document.getElementById('amPhone').value.trim();
  amShow('amSending');
  var payload={firstName:first,lastName:last,email:email,phone:phone,monthlyRevenue:amRev,bottleneck:amBottleneck,timeline:amTimeline,submittedAt:new Date().toISOString()};
  var url='""" + "'+APPS_SCRIPT_URL+'" + r"""';
  try{fetch(url,{method:'POST',mode:'no-cors',body:JSON.stringify(payload)});}catch(err){}
  setTimeout(function(){window.open('https://calendly.com/kyle-krysongroup/introduction','_blank');amShow('amGo');},600);
}
document.addEventListener('keydown',function(e){if(e.key==='Escape')closeApplyModal();});
document.addEventListener('click',function(e){if(e.target&&e.target.id==='applyModal')closeApplyModal();});
"""

LOADER_JS = r"""
const lt=document.getElementById('lt'),lb=document.getElementById('lb'),ld=document.getElementById('loader');
'KRYSON LIMITED'.split('').forEach(c=>{const s=document.createElement('span');s.textContent=c===' '?'\u00A0\u00A0':c;lt.appendChild(s)});
document.body.style.overflow='hidden';
setTimeout(()=>{lt.querySelectorAll('span').forEach((s,i)=>{setTimeout(()=>{s.style.transition='opacity .35s ease,transform .35s ease';s.style.opacity='1';s.style.transform='translateY(0)'},i*50)})},300);
setTimeout(()=>lb.style.width='100px',1200);
setTimeout(()=>{ld.classList.add('exit');setTimeout(()=>{ld.style.display='none';
document.body.style.overflow='';
gsap.to('#nav',{opacity:1,y:0,duration:.5,ease:'power2.out'});
gsap.to('.ho',{opacity:1,duration:.4,delay:.15});
document.querySelectorAll('.hh .ln span').forEach((s,i)=>{gsap.to(s,{y:0,duration:.6,delay:.3+i*.12,ease:'power3.out'})});
gsap.to('.hs',{opacity:1,duration:.4,delay:.9});
gsap.to('.hb',{opacity:1,duration:.4,delay:1.05});
gsap.to('.hero-cap-note',{opacity:1,duration:.4,delay:1.25});
document.querySelectorAll('.st').forEach((s,i)=>{gsap.to(s,{opacity:1,y:0,duration:.4,delay:1.2+i*.08,ease:'power2.out'})});
},1000)},3000);
"""

def head(title, desc, canonical='', schema=''):
    return (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
        '<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1.0">\n'
        '<title>' + title + '</title>\n'
        '<meta name="description" content="' + desc + '">\n'
        '<link rel="canonical" href="https://krysonlimited.com/' + canonical + '">\n'
        '<link rel="icon" type="image/png" href="Kryson Logos.png">\n'
        '<link rel="stylesheet" href="styles.css">\n' +
        CDN + '\n' + schema + '\n</head>'
    )

def cta_section():
    return '''<section id="cta">
<canvas id="ctaC"></canvas>
<div class="cta-glow"></div>
<div class="cta-decor">KRYSON</div>
<div class="cta-in">
<div class="sl">Get Started</div>
<h2 class="sh">Stop losing revenue you already earned.</h2>
<p class="sp">90 minutes. Your pipeline, conversion data, and sales process examined and mapped. No pitch. Just diagnosis.</p>
<a href="javascript:void(0)" onclick="openApplyModal()"><button class="btn bp" style="font-size:13px;padding:16px 40px">Apply for a Revenue Audit</button></a>
<p class="cta-note">We take a maximum of 5 clients per quarter. If you are a fit, you will hear from us within 24 hours.</p>
</div>
</section>'''

def inner_page(title, desc, canonical, schema, hero_label, hero_h1, hero_sub, body, extra_js=''):
    nav_js = "gsap.to('#nav',{opacity:1,y:0,duration:.5,ease:'power2.out'});"
    return (
        head(title, desc, canonical, schema) +
        '\n<body>\n' + APPLICATION_MODAL + '\n' + NAV +
        '\n<section class="ph" style="background:var(--bg2);padding:clamp(120px,14vw,180px) clamp(48px,7vw,120px) clamp(64px,8vw,100px);position:relative;overflow:hidden">'
        '\n<div class="hero-glow" style="opacity:.5"></div>'
        '\n<div class="sl">' + hero_label + '</div>'
        '\n<h1 class="sh" style="max-width:800px;font-size:clamp(32px,5vw,72px)">' + hero_h1 + '</h1>'
        '\n<p class="sp" style="max-width:560px">' + hero_sub + '</p>'
        '\n</section>\n<div class="glow-div"></div>\n' +
        body +
        cta_section() + '\n' + KG_BAND + '\n' + FOOTER +
        '\n<script>\n' + nav_js + '\n' + SHARED_JS + '\n' + extra_js + '\n</script>\n' +
        '\n</body></html>'
    )


# INDEX
INDEX_SCHEMA = '''<script type="application/ld+json">
{"@context":"https://schema.org","@graph":[
{"@type":"Organization","name":"Kryson Limited","url":"https://krysonlimited.com","description":"Revenue architecture for founder-led B2B agencies and professional service firms.","email":"Kyle@krysongroup.com","founder":{"@type":"Person","name":"Kyle Read","jobTitle":"Founder & Managing Director"},"areaServed":["GB","IE","EU"]},
{"@type":"Service","name":"Revenue Architecture","provider":{"@type":"Organization","name":"Kryson Limited"},"description":"We diagnose where revenue is leaking, rebuild the commercial system, and install a revenue operating system that runs without us.","serviceType":"Revenue Operations Consulting"}
]}</script>'''

INDEX_BODY = '''<section id="hero">
<canvas id="pC"></canvas>
<div class="hero-glow"></div><div class="hero-glow2"></div>
<div class="hi-wrap">
<div class="hi">
<h1 class="hh">
<span class="ho" style="display:block">Revenue Architecture</span>
<span class="ln"><span>Your pipeline</span></span>
<span class="ln"><span>is full. Your</span></span>
<span class="ln"><span>revenue is <em>flat.</em></span></span>
</h1>
<p class="hs">You have leads, calls, and conversations going out. Revenue still feels like guesswork. The problem is never the top of the funnel. It is the system underneath it.</p>
<div class="hb">
<a href="javascript:void(0)" onclick="openApplyModal()"><button class="btn bp" style="font-size:13px;padding:16px 36px;letter-spacing:2.5px">Apply for a Revenue Audit</button></a>
<a href="results.html"><button class="btn bs" style="font-size:11px;padding:12px 24px">See Client Results</button></a>
</div>
<p class="hero-cap-note rv">We work with a maximum of 5 clients per quarter. Q3 2026 intake is currently open.</p>
</div>
</div>
<div class="stats">
<div class="st"><div class="st-n"><span class="ctr" data-to="3.2" data-pre="&pound;" data-suf="M+">£0</span></div><div class="st-l">Additional Revenue Generated</div></div>
<div class="st"><div class="st-n">2x to 3x</div><div class="st-l">Conversion Rate Uplift</div></div>
<div class="st"><div class="st-n">60 to 90 Days</div><div class="st-l">From Audit to Measurable Results</div></div>
</div>
</section>
<section class="sec vsl-home-sec" style="background:var(--bg);text-align:center;padding:clamp(48px,6vw,80px) clamp(24px,6vw,80px)">
<div class="sl">Watch</div>
<h2 class="sh" style="max-width:640px;margin:0 auto 16px">The Revenue Architecture Breakdown</h2>
<p class="sp" style="max-width:500px;margin:0 auto 40px">A full walkthrough of how we diagnose, rebuild, and install a commercial system that runs without the founder. Coming soon.</p>
<div class="vsl-wrap rv" style="max-width:640px;margin:0 auto">
<div class="vsl-scanlines"></div>
<div class="vsl-rings"><div class="vsl-ring r1"></div><div class="vsl-ring r2"></div><div class="vsl-ring r3"></div></div>
<div class="vsl-play"><svg width="22" height="22" viewBox="0 0 24 24" fill="none"><polygon points="6,3 20,12 6,21" fill="rgba(201,168,76,0.9)"/></svg></div>
<div class="vsl-label">
<div class="vsl-coming">Coming Soon</div>
<div class="vsl-dots"><span></span><span></span><span></span></div>
</div>
</div>
</section>
<div class="glow-div"></div>
<section id="problem" class="sec" style="background:var(--bg2)">
<div class="sl">The Real Problem</div>
<h2 class="prob-intro rv" style="font-size:clamp(22px,3.5vw,48px);line-height:1.25;margin-bottom:clamp(48px,6vw,80px);font-weight:400;color:var(--w95)">You do not need more leads.<br>You need to <em>stop losing the ones you already have.</em></h2>
<div class="prob-grid-2">
<div class="prob-card rv"><div class="prob-num">01</div><h3>You are the entire sales department.</h3><p>Every discovery call, every close call, every follow-up runs through you. When you deliver, you stop selling. Revenue swings because the whole thing depends on your calendar.</p></div>
<div class="prob-card rv"><div class="prob-num">02</div><h3>Prospects go quiet and you have no idea why.</h3><p>You have a good discovery call. Then silence. Three out of five prospects go quiet after the first call. Not because your service is wrong, but because there is no system catching them.</p></div>
<div class="prob-card rv"><div class="prob-num">03</div><h3>Your CRM is a graveyard. Your pipeline is a guess.</h3><p>No visibility. No accountability. No way to forecast next month with any confidence.</p></div>
<div class="prob-card rv"><div class="prob-num">04</div><h3>You keep buying more leads into a system that leaks.</h3><p>Volume does not fix conversion. Structure does. More leads into a broken process just means more money lost.</p></div>
</div>
<div style="text-align:center;margin-top:clamp(32px,4vw,56px)">
<a href="services.html"><button class="btn bp" style="font-size:11px;padding:12px 28px">See How We Fix It &rarr;</button></a>
</div>
</section>
<div class="glow-div"></div>
<section id="whatwedo" class="sec">
<div class="sl">What We Do</div>
<h2 class="sh">Revenue architecture: we rebuild the engine between your first conversation and the signed contract.</h2>
<div class="gr"></div>
<p class="sp">Four phases. One system. Every piece designed to run without us once it is installed.</p>
<div class="wwd-grid">
<div class="wwd-card rv"><div class="wwd-card-head"><div class="wwd-num">Phase 01</div><h3>Revenue Leak Audit</h3></div><p>We map every step from first contact to signed contract and identify exactly where money is falling out.</p><ul class="wwd-delivers"><li>Full pipeline and CRM review</li><li>Live call analysis</li><li>Revenue Leak Map delivered end of Week 1</li></ul></div>
<div class="wwd-card rv"><div class="wwd-card-head"><div class="wwd-num">Phase 02</div><h3>Conversion System Rebuild</h3></div><p>We rebuild everything between the first conversation and the signed contract. One working deliverable per week.</p><ul class="wwd-delivers"><li>Qualification criteria and discovery framework</li><li>Close call framework and follow-up sequences</li><li>CRM architecture rebuilt from scratch</li></ul></div>
<div class="wwd-card rv"><div class="wwd-card-head"><div class="wwd-num">Phase 03</div><h3>Revenue Operating System</h3></div><p>We install the structure that keeps the system running and improving week after week.</p><ul class="wwd-delivers"><li>KPI dashboards and conversion tracking</li><li>Weekly pipeline and call review cadences</li><li>Team trained to run it independently</li></ul></div>
<div class="wwd-card rv"><div class="wwd-card-head"><div class="wwd-num">Phase 04</div><h3>Scale</h3></div><p>Once the system is proven, we build the team to run it at scale so the founder steps back from every deal.</p><ul class="wwd-delivers"><li>Role design and hiring criteria</li><li>Scripts, objection libraries, call frameworks</li><li>Team running proven system independently</li></ul></div>
</div>
<div style="text-align:center;margin-top:clamp(32px,4vw,56px)">
<a href="services.html"><button class="btn bp" style="font-size:11px;padding:12px 28px">Full Service Detail &rarr;</button></a>
</div>
</section>
<div class="glow-div"></div>
<div class="stats-band">
<div class="sb-item rv"><div class="sb-num">6.68x</div><div class="sb-label">Highest Recorded Multiple</div><div class="sb-sub">North Star Solutions, 90 days</div></div>
<div class="sb-item rv"><div class="sb-num">2&ndash;3x</div><div class="sb-label">Conversion Rate Uplift</div><div class="sb-sub">Regardless of starting point</div></div>
<div class="sb-item rv"><div class="sb-num">100%</div><div class="sb-label">System Retention Rate</div><div class="sb-sub">Every system built is still operational</div></div>
</div>
<section id="results" class="sec">
<div class="sl">Results</div>
<h2 class="sh">Pipeline conversion results: real numbers, real agencies, real timelines.</h2>
<div class="gr"></div>
<div class="feat-results">
<div class="fr-card rv"><div class="fr-ind">B2B Marketing Agency</div><div class="fr-name">TeamCTC Ltd</div><div class="fr-num">&pound;8K &rarr; &pound;61K <span>/mo</span></div><div class="fr-meta">6.63x in 90 days</div><div class="fr-quote">'Close rate went from 21% to 38% and the revenue followed.'</div></div>
<div class="fr-card rv"><div class="fr-ind">B2B Professional Services</div><div class="fr-name">Wise Enterprises</div><div class="fr-num">&pound;27K &rarr; &pound;127.5K <span>/mo</span></div><div class="fr-meta">3.72x in 60 days</div><div class="fr-quote">'The revenue almost felt like a side effect of getting the system right.'</div></div>
<div class="fr-card rv"><div class="fr-ind">B2B Services Agency</div><div class="fr-name">North Star Solutions</div><div class="fr-num">$12.5K &rarr; $96K <span>/mo</span></div><div class="fr-meta">6.68x in 90 days</div><div class="fr-quote">'The revenue nearly doubled before we changed anything about our service.'</div></div>
</div>
<div style="text-align:center;margin-top:clamp(32px,4vw,56px)">
<a href="results.html"><button class="btn bs" style="font-size:11px;padding:12px 28px">View All 6 Case Studies &rarr;</button></a>
</div>
</section>
<div class="glow-div"></div>
<section class="sec" style="background:var(--bg2)">
<div class="sl">The Firm</div>
<h2 class="sh">Built by operators. Not advisors.</h2>
<div class="gr"></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:clamp(32px,5vw,80px);align-items:start" class="rv">
<p style="font-size:clamp(16px,1.8vw,20px);color:var(--w60);line-height:1.85">Kyle has led 8-figure revenue closes across the UK energy sector and served as VP of Sales in a private credit enterprise firm, where he drove a full market pivot and closed $1.3M in new revenue in 4 months.<br><br>He built Kryson after seeing the same pattern across dozens of agencies: strong services, real demand, and a sales process held together with duct tape and good intentions.</p>
<div><p style="font-size:15px;color:var(--w60);line-height:1.85;margin-bottom:20px">Over <strong style="color:var(--gold)">&pound;3.2M</strong> in additional client revenue generated. Every system we build is designed to run without us once it is installed.</p>
<a href="about.html"><button class="btn bs" style="font-size:11px;padding:12px 28px">About the Firm &rarr;</button></a></div>
</div>
</section>
<div class="glow-div"></div>'''

INDEX = (
    head("Kryson Limited | Revenue Architecture",
         "Revenue architecture for founder-led B2B agencies and professional service firms. We fix pipeline conversion, rebuild the sales process, and install revenue operating systems that run without us.",
         "", INDEX_SCHEMA) +
    '\n<body>\n' + APPLICATION_MODAL + '\n' + LOADER + '\n' + NAV + '\n' + INDEX_BODY +
    cta_section() + '\n' + KG_BAND + '\n' + FOOTER +
    '\n<script>\n' + LOADER_JS + '\n' + SHARED_JS + "\ninitP('pC',30);initP('ctaC',15);\n</script>\n" +
    '\n</body></html>'
)

with open('index.html','w') as f: f.write(INDEX)
print("index.html: {:,}".format(len(INDEX)))

# CASE STUDIES (shared)
CASES = '''
<div class="case rv">
<div class="case-top" onclick="toggleCase(this)">
<div class="case-info"><div><div class="case-name">Wise Enterprises</div><div class="case-ind">B2B Professional Services</div></div>
<div class="case-nums"><div class="case-rev">&pound;27K &rarr; &pound;127.5K /mo</div><div class="case-mult">3.72x in 60 days</div></div></div>
<button class="case-btn"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke-width="1.5"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></button>
</div>
<div class="case-body"><div class="case-inner">
<div class="case-hero-nums"><div class="chn"><div class="chn-label">Before</div><div class="chn-val">&pound;27,000 /mo</div></div><div class="chn"><div class="chn-label">After</div><div class="chn-val">&pound;127,500 /mo</div></div><div class="chn"><div class="chn-label">Growth</div><div class="chn-val">+&pound;100,500 /mo</div></div></div>
<div class="case-story">
<div><h5>The Situation</h5><p>The founder ran every deal personally. Over 60% of their week was spent on unqualified prospects who should never have made it past the first call. There was no pipeline visibility, no qualification criteria, and revenue was completely capped by the founder's availability. When delivery got busy, sales stopped dead.</p></div>
<div><h5>What We Installed</h5><ul>
<li>Automated qualification gate with four mandatory criteria before any prospect entered the active pipeline</li>
<li>Seven structured pipeline stages with clear entry and exit criteria for each</li>
<li>Dedicated setter process so the founder only attended pre-qualified, confirmed opportunities</li>
<li>Commission-only setter hired and onboarded within the first four weeks</li>
<li>Weekly accountability cadence: pipeline review, conversion review, and deal debrief every Monday</li>
<li>Full pipeline migration into Close CRM with real-time reporting dashboards</li>
</ul></div>
</div>
<div class="case-quote"><p>'I had no idea how much time I was wasting on the wrong conversations. Once the qualification gate was in and the setter was running, I could not believe how much headspace I got back. The revenue almost felt like a side effect of getting the system right.'</p></div>
<div class="case-cta"><a href="javascript:void(0)" onclick="openApplyModal()"><button class="btn bp" style="font-size:11px;padding:12px 24px">Apply for a Revenue Audit</button></a></div>
</div></div></div>

<div class="case rv">
<div class="case-top" onclick="toggleCase(this)">
<div class="case-info"><div><div class="case-name">TeamCTC Ltd</div><div class="case-ind">B2B Marketing Agency</div></div>
<div class="case-nums"><div class="case-rev">&pound;8K &rarr; &pound;61K /mo</div><div class="case-mult">6.63x in 90 days</div></div></div>
<button class="case-btn"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke-width="1.5"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></button>
</div>
<div class="case-body"><div class="case-inner">
<div class="case-hero-nums"><div class="chn"><div class="chn-label">Before</div><div class="chn-val">&pound;8,000 /mo</div></div><div class="chn"><div class="chn-label">After</div><div class="chn-val">&pound;61,000 /mo</div></div><div class="chn"><div class="chn-label">Growth</div><div class="chn-val">+&pound;53,000 /mo</div></div></div>
<div class="case-story">
<div><h5>The Situation</h5><p>Strong inbound lead flow but only a 21% close rate. The founder pitched immediately on the first call with no structured discovery. There was no framework for the close call and no follow-up system when prospects went quiet. When someone stopped responding, the founder assumed they were not interested and moved on.</p></div>
<div><h5>What We Installed</h5><ul>
<li>Pain-based discovery framework with 12 core questions covering urgency, budget, current situation, and decision process</li>
<li>Two-call close framework: structured discovery on call one, committed close call on call two</li>
<li>Structured close call process with commitment gates and escalation triggers</li>
<li>7-touch post-discovery follow-up sequence with specific messaging for each stage</li>
<li>CRM rebuild with six pipeline stages and mandatory next-action fields</li>
<li>Weekly pipeline review and close rate tracking from Week 1</li>
</ul></div>
</div>
<div class="case-quote"><p>'I was generating the leads. I just could not close them consistently. Kryson showed me exactly where I was losing deals and gave me the tools to fix it. Close rate went from 21% to 38% and the revenue followed.'</p></div>
<div class="case-cta"><button class="btn bp booking-trigger" style="font-size:11px;padding:12px 24px">Book Your Revenue Audit</button></div>
</div></div></div>

<div class="case rv">
<div class="case-top" onclick="toggleCase(this)">
<div class="case-info"><div><div class="case-name">North Star Solutions</div><div class="case-ind">B2B Services Agency</div></div>
<div class="case-nums"><div class="case-rev">$12.5K &rarr; $96K /mo</div><div class="case-mult">6.68x in 90 days</div></div></div>
<button class="case-btn"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke-width="1.5"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></button>
</div>
<div class="case-body"><div class="case-inner">
<div class="case-hero-nums"><div class="chn"><div class="chn-label">Before</div><div class="chn-val">$12,500 /mo</div></div><div class="chn"><div class="chn-label">After</div><div class="chn-val">$96,000 /mo</div></div><div class="chn"><div class="chn-label">Growth</div><div class="chn-val">+$83,500 /mo</div></div></div>
<div class="case-story">
<div><h5>The Situation</h5><p>Zero visibility into sales metrics or channel profitability. Reps were self-reporting deal status with no objective criteria. Follow-up was sporadic. Forecasting was guesswork. The founder had no reliable way to predict next month's revenue or understand why good months happened and bad months kept repeating.</p></div>
<div><h5>What We Installed</h5><ul>
<li>Full Revenue Operating System with real-time KPI dashboards in Close CRM</li>
<li>Eight pipeline stages with objective entry and exit criteria for each</li>
<li>Pain-based discovery framework adapted for the agency's specific service lines</li>
<li>Structured close call process with commitment gates at every stage</li>
<li>Weekly pipeline review, call review, and conversion review cadences</li>
<li>Lost deal tracking system to identify recurring patterns and feed learnings back into the process</li>
</ul></div>
</div>
<div class="case-quote"><p>'We had no idea what was working and what was not. Kryson gave us the visibility to actually manage the business instead of just hoping. The revenue nearly doubled before we changed anything about our service.'</p></div>
<div class="case-cta"><button class="btn bp booking-trigger" style="font-size:11px;padding:12px 24px">Book Your Revenue Audit</button></div>
</div></div></div>

<div class="case rv">
<div class="case-top" onclick="toggleCase(this)">
<div class="case-info"><div><div class="case-name">UK Consulting Practice</div><div class="case-ind">B2B Consulting Firm</div></div>
<div class="case-nums"><div class="case-rev">&pound;18K &rarr; &pound;74K /mo</div><div class="case-mult">4.11x in 75 days</div></div></div>
<button class="case-btn"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke-width="1.5"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></button>
</div>
<div class="case-body"><div class="case-inner">
<div class="case-hero-nums"><div class="chn"><div class="chn-label">Before</div><div class="chn-val">&pound;18,000 /mo</div></div><div class="chn"><div class="chn-label">After</div><div class="chn-val">&pound;74,000 /mo</div></div><div class="chn"><div class="chn-label">Growth</div><div class="chn-val">+&pound;56,000 /mo</div></div></div>
<div class="case-story">
<div><h5>The Situation</h5><p>A two-partner consulting firm generating most revenue through referrals. When referrals slowed, they had no outbound motion and no way to convert inbound enquiries that did come in. The average deal cycle was 47 days because neither partner followed a structured process and there was no close call framework.</p></div>
<div><h5>What We Installed</h5><ul>
<li>Inbound response system with a 4-hour speed-to-lead target and automated booking flow</li>
<li>Structured discovery call framework tailored to their consulting services and ICP</li>
<li>Close call framework that cut average deal cycle from 47 days to under 14</li>
<li>5-touch follow-up cadence with value-add content at each stage</li>
<li>CRM implementation from scratch with pipeline visibility for both partners</li>
<li>Fortnightly deal review replacing ad-hoc conversations about pipeline</li>
</ul></div>
</div>
<div class="case-quote"><p>'We went from hoping the phone would ring to actually controlling our revenue. The close call framework alone changed everything. We stopped losing deals we should have won overnight.'</p></div>
<div class="case-cta"><button class="btn bp booking-trigger" style="font-size:11px;padding:12px 24px">Book Your Revenue Audit</button></div>
</div></div></div>

<div class="case rv">
<div class="case-top" onclick="toggleCase(this)">
<div class="case-info"><div><div class="case-name">UK Performance Marketing Agency</div><div class="case-ind">Performance Marketing Agency</div></div>
<div class="case-nums"><div class="case-rev">&pound;32K &rarr; &pound;89K /mo</div><div class="case-mult">2.78x in 60 days</div></div></div>
<button class="case-btn"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke-width="1.5"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></button>
</div>
<div class="case-body"><div class="case-inner">
<div class="case-hero-nums"><div class="chn"><div class="chn-label">Before</div><div class="chn-val">&pound;32,000 /mo</div></div><div class="chn"><div class="chn-label">After</div><div class="chn-val">&pound;89,000 /mo</div></div><div class="chn"><div class="chn-label">Growth</div><div class="chn-val">+&pound;57,000 /mo</div></div></div>
<div class="case-story">
<div><h5>The Situation</h5><p>A 12-person agency with strong delivery but 35% annual client churn. The founder closed deals on price rather than value. There was no onboarding structure to set expectations after signing. Clients churned at months 3 to 4 because the initial engagement felt disjointed.</p></div>
<div><h5>What We Installed</h5><ul>
<li>Value-based sales process replacing the price-led pitch with ROI-focused discovery</li>
<li>Client onboarding framework with structured first-30-days touchpoints</li>
<li>Retention review cadence at day 30, 60, and 90 to catch early churn signals</li>
<li>Upsell and expansion playbook identifying trigger points for additional services</li>
<li>Pipeline segmented into new business and expansion tracks with separate KPIs</li>
<li>Monthly revenue review cadence replacing the founder's ad-hoc check-ins</li>
</ul></div>
</div>
<div class="case-quote"><p>'We were so focused on winning new clients that we forgot to keep the ones we had. Kryson showed us the churn was costing more than the new business was making. Fixing retention was the single highest-leverage move we could have made.'</p></div>
<div class="case-cta"><button class="btn bp booking-trigger" style="font-size:11px;padding:12px 24px">Book Your Revenue Audit</button></div>
</div></div></div>

<div class="case rv">
<div class="case-top" onclick="toggleCase(this)">
<div class="case-info"><div><div class="case-name">UK Creative &amp; Strategy Agency</div><div class="case-ind">Creative and Strategy Agency</div></div>
<div class="case-nums"><div class="case-rev">&pound;14K &rarr; &pound;52K /mo</div><div class="case-mult">3.71x in 90 days</div></div></div>
<button class="case-btn"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke-width="1.5"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></button>
</div>
<div class="case-body"><div class="case-inner">
<div class="case-hero-nums"><div class="chn"><div class="chn-label">Before</div><div class="chn-val">&pound;14,000 /mo</div></div><div class="chn"><div class="chn-label">After</div><div class="chn-val">&pound;52,000 /mo</div></div><div class="chn"><div class="chn-label">Growth</div><div class="chn-val">+&pound;38,000 /mo</div></div></div>
<div class="case-story">
<div><h5>The Situation</h5><p>A founder-led creative agency that had grown to &pound;14K/mo through word of mouth but had no sales process at all. Every deal was different. The founder priced on gut feel, gave discounts when pushed, and had no follow-up system. Three out of every five discovery calls led nowhere.</p></div>
<div><h5>What We Installed</h5><ul>
<li>Standardised discovery framework replacing the founder's unstructured chemistry calls</li>
<li>Tiered pricing structure with three packages, removing the guesswork from quoting</li>
<li>Close call script with built-in urgency framing and committed next steps</li>
<li>Objection pre-handling built directly into the discovery and close call stages</li>
<li>Lost deal debrief process to capture why deals did not close and feed learnings back in</li>
<li>Commission-only setter brought in at Week 6 to handle initial qualification and booking</li>
</ul></div>
</div>
<div class="case-quote"><p>'I did not even realise I had a sales problem. I thought I just needed more leads. Turns out I was losing half the deals I already had because I had no system. The structure Kryson put in changed everything.'</p></div>
<div class="case-cta"><button class="btn bp booking-trigger" style="font-size:11px;padding:12px 24px">Book Your Revenue Audit</button></div>
</div></div></div>'''

# SERVICES
SERVICES_SCHEMA = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Service","name":"Revenue Architecture","provider":{"@type":"Organization","name":"Kryson Limited","url":"https://krysonlimited.com"},"description":"Four-phase revenue architecture service.","serviceType":"Revenue Operations Consulting"}
</script>'''

SERVICES_BODY = '''<section id="problem" class="sec" style="background:var(--bg)">
<div class="sl">The Real Problem</div>
<h2 class="prob-intro rv" style="font-size:clamp(22px,3.5vw,48px);line-height:1.25;margin-bottom:clamp(48px,6vw,80px);font-weight:400;color:var(--w95)">You do not need more leads.<br>You need to <em>stop losing the ones you already have.</em></h2>
<div class="funnel-vis rv">
<div class="funnel-heading">Industry Benchmark: where agencies lose revenue on average</div>
<div style="font-size:11px;color:var(--w20);letter-spacing:.5px;margin-bottom:20px;font-style:italic">Based on published B2B agency conversion benchmarks, not Kryson internal data</div>
<div class="funnel-row"><span class="funnel-label">100 Conversations</span><div class="funnel-track"><div class="funnel-fill" data-width="100"></div></div><span class="funnel-pct">100%</span></div>
<div class="funnel-row"><span class="funnel-label">65 Discovery Calls</span><div class="funnel-track"><div class="funnel-fill" data-width="65"></div></div><span class="funnel-pct">65%</span></div>
<div class="funnel-row"><span class="funnel-label">32 Close Calls Booked</span><div class="funnel-track"><div class="funnel-fill" data-width="32"></div></div><span class="funnel-pct">32%</span></div>
<div class="funnel-row"><span class="funnel-label">7 Clients Closed</span><div class="funnel-track"><div class="funnel-fill" data-width="7"></div></div><span class="funnel-pct" style="color:rgba(201,168,76,1)">7%</span></div>
<div class="funnel-note">The average agency closes 7% of the conversations it starts. Our clients average a 34% close rate on close calls. Most start well below that.</div>
</div>
<div class="prob-grid-2" style="margin-top:clamp(32px,4vw,56px)">
<div class="prob-card rv"><div class="prob-num">01</div><h3>You are the entire sales department.</h3><p>Every discovery call, every close call, every follow-up runs through you. When you deliver, you stop selling.</p></div>
<div class="prob-card rv"><div class="prob-num">02</div><h3>Prospects go quiet and you have no idea why.</h3><p>Three out of five prospects go quiet after the first call. Not because your service is wrong. Because there is no system catching them.</p></div>
<div class="prob-card rv"><div class="prob-num">03</div><h3>Your CRM is a graveyard. Your pipeline is a guess.</h3><p>No visibility. No accountability. No way to forecast next month with any confidence.</p></div>
<div class="prob-card rv"><div class="prob-num">04</div><h3>You keep buying more leads into a system that leaks.</h3><p>Volume does not fix conversion. Structure does.</p></div>
</div>
</section>
<div class="glow-div"></div>
<section id="whatwedo" class="sec" style="background:var(--bg2)">
<div class="sl">What We Do</div>
<h2 class="sh">Revenue architecture: we rebuild the engine between your first conversation and the signed contract.</h2>
<div class="gr"></div>
<p class="sp">Four phases. One system. Every piece designed to run without us once it is installed.</p>
<div class="wwd-grid">
<div class="wwd-card rv"><div class="wwd-card-head"><div class="wwd-num">Phase 01</div><h3>Revenue Leak Audit</h3></div><p>We map every step from first contact to signed contract and show you exactly where money is falling out.</p><ul class="wwd-delivers"><li>Full pipeline and CRM review</li><li>Live call analysis</li><li>Founder dependency assessment</li><li>Prioritised Revenue Leak Map delivered end of Week 1</li></ul></div>
<div class="wwd-card rv"><div class="wwd-card-head"><div class="wwd-num">Phase 02</div><h3>Conversion System Rebuild</h3></div><p>We rebuild everything between the first conversation and the signed contract. One working deliverable per week, tested on live calls.</p><ul class="wwd-delivers"><li>Qualification criteria and discovery framework</li><li>Close call structure and follow-up sequences</li><li>Objection handling and closing process</li><li>CRM architecture rebuilt from scratch</li></ul></div>
<div class="wwd-card rv"><div class="wwd-card-head"><div class="wwd-num">Phase 03</div><h3>Revenue Operating System</h3></div><p>We install the structure that keeps it running and improving week after week.</p><ul class="wwd-delivers"><li>KPI dashboards and conversion tracking</li><li>Weekly pipeline and call review cadences</li><li>Deal ownership by stage</li><li>Team training to run it independently</li></ul></div>
<div class="wwd-card rv"><div class="wwd-card-head"><div class="wwd-num">Phase 04</div><h3>Scale</h3></div><p>Once the system is proven, we build the team to run it at scale.</p><ul class="wwd-delivers"><li>Role design and hiring criteria</li><li>Scripts, objection libraries, and call frameworks</li><li>Onboarding and performance standards</li><li>Team running proven system independently</li></ul></div>
</div>
<div style="text-align:center;margin-top:clamp(32px,4vw,56px)"><a href="javascript:void(0)" onclick="openApplyModal()"><button class="btn bp" style="font-size:11px;padding:12px 28px">Apply for a Revenue Audit</button></a></div>
</section>
<div class="glow-div"></div>
<section id="process" class="sec" style="background:var(--bg)">
<div class="sl">How It Works</div>
<h2 class="sh">B2B sales process optimisation: from broken to predictable in 90 days.</h2>
<div class="gr"></div>
<div class="process-wrap">
<div class="tl">
<div class="tl-fill" id="tlF"></div>
<div class="ts"><div class="td"></div><div class="tt">Today</div><h4>Strategic Fit Call</h4><p>We align on your goals, bottlenecks, and commercial reality. No pitch. Just diagnosis.</p></div>
<div class="ts"><div class="td"></div><div class="tt">Week 1</div><h4>Revenue Leak Audit</h4><p>90 minutes with the founder. Full pipeline and CRM review. By end of week we deliver the Revenue Leak Map.</p></div>
<div class="ts"><div class="td"></div><div class="tt">Weeks 2 to 6</div><h4>System Rebuild</h4><p>Highest-leverage fixes first. One working deliverable per week. Everything tested on live conversations.</p></div>
<div class="ts"><div class="td"></div><div class="tt">Month 2</div><h4>Prove It Works</h4><p>The system is live. We measure close rate, show rate, pipeline accuracy, and follow-up compliance weekly.</p></div>
<div class="ts"><div class="td"></div><div class="tt">Month 3</div><h4>Scale the System</h4><p>System is proven. We help you build the team around it.</p></div>
</div>
<div class="process-visual">
<div class="growth-panel">
<div class="growth-panel-header"><div class="growth-panel-tag">What Each Phase Delivers</div><div class="growth-panel-title">The outputs you leave each phase with</div></div>
<div class="growth-chart-wrap">
<div class="phase-deliverables">
<div class="ph-del"><div class="ph-del-num">01</div><div class="ph-del-content"><div class="ph-del-title">Revenue Leak Map</div><p>A ranked breakdown of where you are losing money with priorities ordered by commercial impact.</p></div></div>
<div class="ph-del"><div class="ph-del-num">02</div><div class="ph-del-content"><div class="ph-del-title">Rebuilt Sales System</div><p>New scripts, frameworks, close call structure, follow-up cadences, CRM architecture. All built and tested on live conversations.</p></div></div>
<div class="ph-del"><div class="ph-del-num">03</div><div class="ph-del-content"><div class="ph-del-title">Revenue Operating System</div><p>KPI dashboards, weekly review cadences, conversion tracking, and a trained team running the full system.</p></div></div>
<div class="ph-del"><div class="ph-del-num">04</div><div class="ph-del-content"><div class="ph-del-title">Scale</div><p>Role design, hiring criteria, onboarding frameworks, and performance standards built around the proven system.</p></div></div>
</div>
</div>
<div class="growth-mini-stats">
<div class="gms-cell"><div class="gms-val">Week 1</div><div class="gms-label">Leak Map Delivered</div></div>
<div class="gms-cell"><div class="gms-val">Week 6</div><div class="gms-label">System Live</div></div>
<div class="gms-cell"><div class="gms-val">Month 2</div><div class="gms-label">Proven Results</div></div>
<div class="gms-cell"><div class="gms-val">Month 3</div><div class="gms-label">Scale or Step Back</div></div>
</div>
</div>
</div>
</div>
<div style="text-align:center;margin-top:clamp(32px,4vw,56px)"><button class="btn bp booking-trigger" style="font-size:11px;padding:12px 28px">Book a Revenue Audit</button></div>
</section>
<div class="glow-div"></div>
<section id="pricing" class="sec" style="background:var(--bg2)">
<div class="sl">Investment</div>
<h2 class="sh">Aligned incentives. We earn when you earn more.</h2>
<div class="gr"></div>
<p class="sp">If the system does not improve your revenue, we do not benefit. That is the only model we believe in.</p>
<div class="pr-grid">
<div class="pr-card rv"><div class="pr-lab">Setup Fee</div><div class="pr-val">On Application</div><p>Covers the full Revenue Leak Audit, system rebuild, CRM architecture, framework design, and initial training. Payable on signing.</p></div>
<div class="pr-card rv"><div class="pr-lab">Revenue Share</div><div class="pr-val">Performance-Based</div><p>Applied to incremental revenue above your established baseline. If your revenue does not grow, we do not earn. Minimum 3-month engagement.</p></div>
</div>
<div style="text-align:center"><a href="javascript:void(0)" onclick="openApplyModal()"><button class="btn bp" style="font-size:11px">Apply for a Revenue Audit</button></a></div>
</section>
<div class="glow-div"></div>'''

SERVICES_HTML = inner_page(
    "Revenue Architecture Services | Kryson Limited",
    "Four-phase revenue architecture for founder-led B2B agencies: Revenue Leak Audit, Conversion System Rebuild, Revenue Operating System, and Scale.",
    "services.html", SERVICES_SCHEMA,
    "Revenue Architecture",
    "B2B sales process optimisation: from broken to <em>predictable.</em>",
    "Four phases. One system designed to fix every structural gap between your first conversation and the signed contract.",
    SERVICES_BODY,
    "initP('ctaC',15);"
)
with open('services.html','w') as f: f.write(SERVICES_HTML)
print("services.html: {:,}".format(len(SERVICES_HTML)))

# RESULTS
RESULTS_SCHEMA = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"ItemList","name":"Kryson Client Results","numberOfItems":6}
</script>'''

RESULTS_BODY = (
    '<div class="stats-band">\n'
    '<div class="sb-item rv"><div class="sb-num">6.68x</div><div class="sb-label">Highest Recorded Multiple</div><div class="sb-sub">North Star Solutions, 90 days</div></div>\n'
    '<div class="sb-item rv"><div class="sb-num">2&ndash;3x</div><div class="sb-label">Conversion Rate Uplift</div><div class="sb-sub">Regardless of starting point</div></div>\n'
    '<div class="sb-item rv"><div class="sb-num">100%</div><div class="sb-label">System Retention Rate</div><div class="sb-sub">Every system built is still operational</div></div>\n'
    '</div>\n'
    '<section id="results" class="sec" style="background:var(--bg)">\n'
    "<p class=\"res-note\">Some studies are anonymised at the client's request. All figures are verified.</p>\n"
    '<div class="case-list">\n' +
    CASES +
    '\n</div>\n</section>\n<div class="glow-div"></div>\n'
)

RESULTS_HTML = inner_page(
    "B2B Pipeline Conversion Results | Kryson Limited",
    "Six case studies from founder-led B2B agencies and professional service firms. Revenue multiples from 2.78x to 6.68x. All figures verified.",
    "results.html", RESULTS_SCHEMA,
    "Results",
    "Pipeline conversion results: real numbers, real agencies, real timelines.",
    "Six founder-led B2B firms. Six revenue systems installed. All figures verified.",
    RESULTS_BODY,
    "initP('ctaC',15);"
)
with open('results.html','w') as f: f.write(RESULTS_HTML)
print("results.html: {:,}".format(len(RESULTS_HTML)))

# ABOUT
ABOUT_BODY = '''<section id="about" class="sec" style="background:var(--bg)">
<div class="ab-grid">
<div class="ab-portrait-col rv">
<div class="kyle-portrait">
<img src="Kyle headshot (black).png" alt="Kyle Read, Founder and Managing Director, Kryson Limited" class="kyle-portrait-img">
<div class="kyle-portrait-corner tl"></div><div class="kyle-portrait-corner tr"></div><div class="kyle-portrait-corner bl"></div><div class="kyle-portrait-corner br"></div>
<div class="kyle-portrait-tag"><div class="kyle-portrait-name">Kyle Read</div><div class="kyle-portrait-role">Founder &amp; MD</div></div>
</div>
</div>
<div class="ab-l rv">
<h2>Kyle</h2>
<div class="ab-role">Founder &amp; Managing Director</div>
<p>Kyle has led 8-figure revenue closes across the UK energy sector and served as VP of Sales in a private credit enterprise firm, where he drove a full market pivot and closed $1.3M in new revenue in 4 months.</p>
<p>He built Kryson after seeing the same pattern across dozens of agencies: strong services, real demand, and a sales process held together with duct tape and good intentions. The revenue was there. The system to capture it was not.</p>
<ul class="creds">
<li>8-figure revenue closes led in the UK energy sector</li>
<li>VP of Sales in a private credit enterprise</li>
<li>$1.3M closed in 4 months post-pivot</li>
<li>Commercial leadership across B2B services and professional services</li>
</ul>
</div>
<div class="ab-r rv">
<h2>The Firm</h2>
<p>Kryson works with agencies and professional service firms that already have demand but are losing revenue because the commercial system underneath is broken or nonexistent.</p>
<p>We diagnose where revenue is leaking, rebuild the broken parts, and install the operating structure that makes growth repeatable. Every system we build is designed to run without us.</p>
<p style="color:var(--gold);font-style:italic">Over &pound;3.2M in additional client revenue generated in the last 12 months.</p>
<div class="diff">
<div class="diff-i"><p><strong>Diagnose before we fix.</strong> Most firms start building before they understand what is actually broken.</p></div>
<div class="diff-i"><p><strong>Fix conversion before volume.</strong> More leads into a broken system just produces more waste.</p></div>
<div class="diff-i"><p><strong>Build to run without us.</strong> The goal is independence, not dependency.</p></div>
<div class="diff-i"><p><strong>Small client base by design.</strong> Every engagement gets our full attention.</p></div>
<div class="diff-i"><p><strong>Operators, not coaches.</strong> We build things. We do not just talk about them.</p></div>
</div>
</div>
</div>
</section>
<div class="glow-div"></div>
<section id="careers" class="sec" style="background:var(--bg2)">
<div class="sl">Careers</div>
<h2 class="sh">Build with us.</h2>
<div class="gr"></div>
<p class="sp">Kryson is early-stage and intentionally lean. We hire when we find someone who raises the standard.</p>
<div class="car-grid">
<div class="car-col rv"><h4>What we look for</h4><ul>
<li>Operators who have built, run, or fixed revenue systems</li>
<li>Clear thinkers who diagnose before they prescribe</li>
<li>High standards. We do not ship average work</li>
<li>Comfort with ambiguity in an early-stage firm</li>
<li>Honesty about what you do not know</li>
</ul></div>
<div class="car-col rv"><h4>Focus areas</h4><ul>
<li>Revenue Operations: CRM architecture, pipeline design, dashboards</li>
<li>Sales: setter or closer experience in B2B services or agencies</li>
<li>Client Delivery: running diagnosis and rebuild engagements</li>
<li>Commercial Advisors: senior operators, fractional or part-time</li>
</ul></div>
</div>
<div class="car-box rv">
<h4>How to apply</h4>
<p>No formal application. Send a short message with three things:</p>
<p style="color:var(--w95)">1. What you have built or fixed commercially. Be specific.<br>2. Why Kryson and why now.<br>3. What you would contribute in the first 90 days.</p>
<div style="margin-top:18px"><a href="mailto:Kyle@krysongroup.com"><button class="btn bs" style="font-size:11px;padding:10px 22px">Get in Touch</button></a></div>
</div>
</section>
<div class="glow-div"></div>'''

ABOUT_HTML = inner_page(
    "About Kryson Limited | Revenue Architecture Firm",
    "Founded by Kyle Read, VP of Sales with 8-figure revenue close experience. Kryson builds revenue systems for founder-led B2B agencies and professional service firms.",
    "about.html", "",
    "The Firm",
    "Built by operators. <em>Not advisors.</em>",
    "Commercial leadership and 8-figure revenue close experience applied to founder-led agencies and professional service firms.",
    ABOUT_BODY,
    "initP('ctaC',15);"
)
with open('about.html','w') as f: f.write(ABOUT_HTML)
print("about.html: {:,}".format(len(ABOUT_HTML)))

# FAQ
FAQ_SCHEMA = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"Who is Kryson for?","acceptedAnswer":{"@type":"Answer","text":"Founder-led B2B companies that have leads and pipeline activity but are losing revenue due to weak commercial structure."}},
{"@type":"Question","name":"What happens in the first week?","acceptedAnswer":{"@type":"Answer","text":"Week 1 is entirely diagnostic. A 90-minute audit call, CRM and pipeline review, call recording analysis. By end of Week 1 we deliver the Revenue Leak Map."}},
{"@type":"Question","name":"How long does an engagement last?","acceptedAnswer":{"@type":"Answer","text":"Minimum 3 months."}},
{"@type":"Question","name":"Do you run the sales process for us?","acceptedAnswer":{"@type":"Answer","text":"No. We design the system and your team runs it."}},
{"@type":"Question","name":"How is the revenue share calculated?","acceptedAnswer":{"@type":"Answer","text":"Applied only to incremental revenue above your baseline. The baseline is locked in writing before we start."}},
{"@type":"Question","name":"Do you work outside the UK?","acceptedAnswer":{"@type":"Answer","text":"Yes, across the UK, Ireland, and Europe. All engagement work is remote."}},
{"@type":"Question","name":"What if I already have a CRM set up?","acceptedAnswer":{"@type":"Answer","text":"We audit and rebuild the architecture inside it."}},
{"@type":"Question","name":"How many clients do you take at one time?","acceptedAnswer":{"@type":"Answer","text":"A small number, by design. We do not scale by volume."}}
]}</script>'''

FAQ_BODY = '''<section id="faq" class="sec" style="background:var(--bg)">
<div class="faq-list">
<div class="fq rv"><button class="fq-q">Who is Kryson for?</button><div class="fq-a"><div class="fq-a-in">Founder-led B2B companies that have leads and pipeline activity but are losing revenue due to weak commercial structure. Agencies, professional service firms, and consultancies. If revenue is inconsistent and the founder is involved in every deal, we are likely the right fit.</div></div></div>
<div class="fq rv"><button class="fq-q">What happens in the first week?</button><div class="fq-a"><div class="fq-a-in">Week 1 is entirely diagnostic. A 90-minute audit call with the founder, CRM and pipeline review, analysis of 2 to 3 call recordings, and full process review. By end of Week 1 we deliver the Revenue Leak Map: a prioritised breakdown of where money is being lost and what to fix first.</div></div></div>
<div class="fq rv"><button class="fq-q">How long does an engagement last?</button><div class="fq-a"><div class="fq-a-in">Minimum 3 months. That is the time needed to diagnose, rebuild, prove conversion improves, and install the operating rhythm. Most clients continue as the revenue share becomes meaningful and the system continues to scale.</div></div></div>
<div class="fq rv"><button class="fq-q">Do you run the sales process for us?</button><div class="fq-a"><div class="fq-a-in">No. We design the system, rebuild the broken parts, and install the operating structure. Your team runs it. We make sure it is built well enough to run without us. We are architects, not an outsourced department.</div></div></div>
<div class="fq rv"><button class="fq-q">How is the revenue share calculated?</button><div class="fq-a"><div class="fq-a-in">Applied only to incremental revenue above your baseline at the start of the engagement. If you were at &pound;12K/month and move to &pound;18K/month, the share applies to the &pound;6K increase. The baseline is locked in writing before we start.</div></div></div>
<div class="fq rv"><button class="fq-q">Do you work outside the UK?</button><div class="fq-a"><div class="fq-a-in">Yes. We work across the UK, Ireland, and Europe. All engagement work is remote via video, Slack, and shared tools. The system and cadence work the same regardless of location.</div></div></div>
<div class="fq rv"><button class="fq-q">What if I already have a CRM set up?</button><div class="fq-a"><div class="fq-a-in">Most of our clients do. The issue is rarely the tool. It is how it is configured, what stages exist, what data is being captured, and whether anyone is actually using it as a management system rather than a contact database. We audit what you have and rebuild the architecture inside it.</div></div></div>
<div class="fq rv"><button class="fq-q">How many clients do you take at one time?</button><div class="fq-a"><div class="fq-a-in">A small number, by design. Every engagement gets full attention. We do not scale by volume. If we are at capacity, we maintain a waitlist.</div></div></div>
<div class="fq rv"><button class="fq-q">What is the difference between Kryson and a sales coach?</button><div class="fq-a"><div class="fq-a-in">A sales coach gives you advice. We build the system. By the end of an engagement you have a working CRM architecture, qualification criteria, discovery frameworks, close call scripts, follow-up sequences, and an operating cadence. Not notes from a workshop.</div></div></div>
<div class="fq rv"><button class="fq-q">What results can I expect?</button><div class="fq-a"><div class="fq-a-in">Across our client base, clients average a 34% close rate on close calls after system installation, and the typical outcome is a 2x to 3x conversion rate improvement within 60 to 90 days. Our highest recorded multiple is 6.68x revenue growth in 90 days. Results depend on starting point, industry, and how broken the existing process is. The Revenue Leak Audit in Week 1 will give you a realistic picture of what is achievable in your specific situation.</div></div></div>
</div>
</section>
<div class="glow-div"></div>'''

FAQ_HTML = inner_page(
    "FAQ | Kryson Limited Revenue Architecture",
    "Answers to the most common questions about Kryson's revenue architecture service for founder-led B2B agencies and professional service firms.",
    "faq.html", FAQ_SCHEMA,
    "Questions",
    "Everything you need to know before we talk.",
    "The most common questions from founders considering a revenue architecture engagement.",
    FAQ_BODY,
    "initP('ctaC',15);"
)
with open('faq.html','w') as f: f.write(FAQ_HTML)
print("faq.html: {:,}".format(len(FAQ_HTML)))

INSIGHTS_SCHEMA = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Blog","name":"Kryson Insights","url":"https://krysonlimited.com/insights","description":"Practical thinking on revenue architecture, sales process, and commercial systems for founder-led B2B agencies.","publisher":{"@type":"Organization","name":"Kryson Limited","url":"https://krysonlimited.com"}}</script>'''


def ins_card(num, title, date, tag, teaser, slug):
    return (
    '<a href="' + slug + '" class="ins-card rv">'
    '<div class="ins-card-num">' + num + '</div>'
    '<div class="ins-card-body">'
    '<div class="ins-card-meta"><span class="ins-tag">' + tag + '</span><span class="ins-date">' + date + '</span></div>'
    '<h3 class="ins-card-title">' + title + '</h3>'
    '<p class="ins-card-teaser">' + teaser + '</p>'
    '</div>'
    '<div class="ins-card-arr">&rarr;</div>'
    '</a>'
    )

INSIGHTS_CARDS = ''.join([
ins_card('01','What makes a great closer','14 Jan 2025','Sales Process',
    'Closers who consistently convert above 30 percent share one thing: a structured framework, not a personality.',
    'insight-01.html'),
ins_card('02','What makes a great setter','3 Mar 2025','Sales Process',
    'The setter is the front door. Show rate, not personality, is the metric that tells you if they are doing their job.',
    'insight-02.html'),
ins_card('03','The pre-call confirmation sequence','22 Apr 2025','Sales Process',
    'Agencies running a four-touch confirmation sequence consistently show 70 percent or higher on their close calls.',
    'insight-03.html'),
ins_card('04','No-show recovery: the playbook','9 May 2025','Sales Process',
    'A no-show is not a lost deal. It is a mismanaged one. The 10-minute rule changes the outcome.',
    'insight-04.html'),
ins_card('05','The discovery call framework that actually converts','1 Jul 2025','Sales Process',
    'Discovery is not an interview. It is the process by which a prospect talks themselves into buying.',
    'insight-05.html'),
ins_card('06','Frame: the invisible variable in every sales call','18 Aug 2025','Sales Psychology',
    'Two calls with identical scripts produce different outcomes. The difference is almost always frame.',
    'insight-06.html'),
ins_card('07','The one-call close: structure and timing','5 Oct 2025','Sales Process',
    'A one-call close is not a shorter pitch. It is a complete arc from pain to decision in a single session.',
    'insight-07.html'),
ins_card('08','The two-call close: why call one ending right is everything','29 Nov 2025','Sales Process',
    'The second call is won or lost on how the first one ends. Most agencies get this backwards.',
    'insight-08.html'),
ins_card('09','Post-call follow-up: the 14-day sequence','14 Jan 2026','Sales Process',
    '71 percent of leads never receive follow-up within the first hour. That gap is where revenue disappears.',
    'insight-09.html'),
ins_card('10','The four real objections and how to handle each','28 Feb 2026','Sales Process',
    'Every objection is one of four things: trust, money, urgency, or authority. The handle changes for each.',
    'insight-10.html'),
ins_card('11','Why close rates collapse when founders hire closers','15 Apr 2026','Revenue Architecture',
    'The failure is almost never the closer. It is what was missing before the closer arrived.',
    'insight-11.html'),
ins_card('12','Building a revenue operating system that runs without you','2 Jun 2026','Revenue Architecture',
    'Most agency founders cannot take two weeks off without the pipeline suffering. That is structural.',
    'insight-12.html'),
])

INSIGHTS_BODY = (
'<section class="sec" style="background:var(--bg)">'
'<div class="sl">Insights</div>'
'<h2 class="sh" style="max-width:640px;margin-bottom:12px">Thinking on revenue, sales, and commercial systems.</h2>'
'<p class="sp">Practical perspectives for founder-led B2B agencies. No frameworks sold separately.</p>'
'<div class="ins-cards">' +
INSIGHTS_CARDS +
'</div>'
'</section>'
'<div class="glow-div"></div>'
)

INSIGHTS_HTML = inner_page(
    "Insights | Kryson Limited Revenue Architecture",
    "Practical thinking on revenue architecture, sales process, and commercial systems for founder-led B2B agencies.",
    "insights.html", INSIGHTS_SCHEMA,
    "Insights",
    "Revenue thinking, without the noise.",
    "Practical perspectives on sales process, pipeline architecture, and building commercial systems that do not depend on the founder.",
    INSIGHTS_BODY
)
with open('insights.html','w') as f: f.write(INSIGHTS_HTML)
print("insights.html: {:,}".format(len(INSIGHTS_HTML)))

# =====================================================================
# INDIVIDUAL ARTICLE PAGES
# =====================================================================

def art_body(svg_code, content_html):
    return (
    '<section class="sec" style="background:var(--bg2);padding:clamp(24px,4vw,56px) clamp(24px,6vw,80px)">'
    '<div class="art-svg-wrap rv">' + svg_code + '</div>'
    '</section>'
    '<div class="glow-div"></div>'
    '<section class="sec" style="background:var(--bg)">'
    '<div class="art-content">'
    '<a href="insights.html" class="art-back">&larr; Back to Insights</a>'
    + content_html +
    '</div>'
    '</section>'
    '<div class="glow-div"></div>'
    )

# ---- ARTICLE 01: What makes a great closer ----
ART01_SVG = (
'<svg viewBox="0 0 760 310" xmlns="http://www.w3.org/2000/svg" style="background:#111;border-radius:6px">'
'<text x="380" y="26" text-anchor="middle" fill="rgba(255,255,255,0.25)" font-size="10" font-family="sans-serif" letter-spacing="3">THE CLOSER FRAMEWORK (ACQ MODEL)</text>'
'<rect x="30" y="42" width="105" height="220" rx="4" fill="rgba(201,168,76,0.07)" stroke="rgba(201,168,76,0.18)" stroke-width="1"/>'
'<text x="82" y="86" text-anchor="middle" fill="#c9a84c" font-size="22" font-family="sans-serif" font-weight="700">C</text>'
'<text x="82" y="108" text-anchor="middle" fill="rgba(255,255,255,0.85)" font-size="12" font-family="sans-serif" font-weight="600">Clarify</text>'
'<text x="82" y="126" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="10" font-family="sans-serif">Why are</text>'
'<text x="82" y="140" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="10" font-family="sans-serif">you here?</text>'
'<rect x="148" y="42" width="105" height="220" rx="4" fill="rgba(201,168,76,0.09)" stroke="rgba(201,168,76,0.22)" stroke-width="1"/>'
'<text x="200" y="86" text-anchor="middle" fill="#c9a84c" font-size="22" font-family="sans-serif" font-weight="700">L</text>'
'<text x="200" y="108" text-anchor="middle" fill="rgba(255,255,255,0.85)" font-size="12" font-family="sans-serif" font-weight="600">Label</text>'
'<text x="200" y="126" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="10" font-family="sans-serif">Name the</text>'
'<text x="200" y="140" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="10" font-family="sans-serif">problem</text>'
'<rect x="266" y="42" width="105" height="220" rx="4" fill="rgba(201,168,76,0.11)" stroke="rgba(201,168,76,0.26)" stroke-width="1"/>'
'<text x="318" y="86" text-anchor="middle" fill="#c9a84c" font-size="22" font-family="sans-serif" font-weight="700">O</text>'
'<text x="318" y="108" text-anchor="middle" fill="rgba(255,255,255,0.85)" font-size="12" font-family="sans-serif" font-weight="600">Overview</text>'
'<text x="318" y="126" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="10" font-family="sans-serif">Past attempts,</text>'
'<text x="318" y="140" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="10" font-family="sans-serif">why failed</text>'
'<rect x="384" y="42" width="105" height="220" rx="4" fill="rgba(201,168,76,0.14)" stroke="rgba(201,168,76,0.3)" stroke-width="1"/>'
'<text x="436" y="86" text-anchor="middle" fill="#c9a84c" font-size="22" font-family="sans-serif" font-weight="700">S</text>'
'<text x="436" y="108" text-anchor="middle" fill="rgba(255,255,255,0.85)" font-size="12" font-family="sans-serif" font-weight="600">Sell</text>'
'<text x="436" y="126" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="10" font-family="sans-serif">Paint the</text>'
'<text x="436" y="140" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="10" font-family="sans-serif">future state</text>'
'<rect x="502" y="42" width="105" height="220" rx="4" fill="rgba(201,168,76,0.17)" stroke="rgba(201,168,76,0.35)" stroke-width="1"/>'
'<text x="554" y="86" text-anchor="middle" fill="#c9a84c" font-size="22" font-family="sans-serif" font-weight="700">E</text>'
'<text x="554" y="108" text-anchor="middle" fill="rgba(255,255,255,0.85)" font-size="12" font-family="sans-serif" font-weight="600">Explain</text>'
'<text x="554" y="126" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="10" font-family="sans-serif">Handle</text>'
'<text x="554" y="140" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="10" font-family="sans-serif">objections</text>'
'<rect x="620" y="42" width="110" height="220" rx="4" fill="rgba(201,168,76,0.22)" stroke="#c9a84c" stroke-width="1.5"/>'
'<text x="675" y="86" text-anchor="middle" fill="#c9a84c" font-size="22" font-family="sans-serif" font-weight="700">R</text>'
'<text x="675" y="108" text-anchor="middle" fill="rgba(255,255,255,0.9)" font-size="12" font-family="sans-serif" font-weight="600">Reinforce</text>'
'<text x="675" y="126" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="10" font-family="sans-serif">Confirm the</text>'
'<text x="675" y="140" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="10" font-family="sans-serif">decision</text>'
'<text x="380" y="296" text-anchor="middle" fill="rgba(255,255,255,0.18)" font-size="11" font-family="sans-serif" font-style="italic">Closers using a structured framework outperform unstructured closers by 2-3x on close rate.</text>'
'</svg>'
)

ART01_CONTENT = (
'<div class="art-stat-pull"><div class="asp-num">34%</div><div class="asp-label">Average close rate across Kryson clients on structured close calls. Most start well below this. The difference is not talent. It is system.</div></div>'
'<div class="art-stat-pull"><div class="asp-num">38%</div><div class="asp-label">Close rate achieved by TeamCTC after installing a structured close call framework. Up from 21%. Revenue went from &pound;8k to &pound;61k.</div></div>'
'<p>The most common myth in agency sales is that great closers are born, not built. That closing is a personality trait. That charisma and pressure are what move deals. This is wrong, and it is expensive to believe.</p>'
'<p>Closers who consistently convert at 30 percent or above share one thing: a repeatable framework. Not a script. A framework. One that lets them navigate any conversation, surface real objections, and guide a prospect to a decision without pushing.</p>'
'<h3>The CLOSER framework</h3>'
'<p>The most effective structure for a close call is the CLOSER model: Clarify, Label, Overview, Sell the vacation, Explain objections, Reinforce the decision. Each stage has a purpose. The closer who skips stages is the one who loses deals that should have closed.</p>'
'<p>Clarify means starting the call by asking the prospect why they showed up. Not what they do. Why they booked this call. This resets the frame from pitch to conversation. Label means naming the problem back to them in their own language. When a prospect hears their situation described accurately, trust spikes. Overview means walking through what they have already tried and why it failed. This positions the solution as the answer to a known problem rather than a new thing to evaluate.</p>'
'<p>Sell the vacation is the pivotal stage. Before presenting any price or deliverables, the closer paints a specific picture of what life looks like after the problem is solved. Revenue targets hit. Team running without founder involvement. Calendar clear. The prospect must see and want the outcome before any numbers are introduced.</p>'
'<h3>How the ANOT opener sets the frame</h3>'
'<p>Before CLOSER begins, top closers use the ANOT opener to set the conversational frame: Appreciate the time, Naturally tell them how the call will run, Obviously let them know they can ask questions, Typically confirm the call length. This takes 60 seconds and eliminates defensive posture before the conversation starts.</p>'
'<h3>The silence rule</h3>'
'<p>The single most measurable difference between closers who hit their number and those who do not is what happens after the price is stated. Elite closers say the number and stop. No filling the silence. No softening with caveats. The first person to speak after the price loses leverage. Most closers have never been trained on this. Once they learn it, close rate moves within two weeks.</p>'
'<div class="art-stat-pull"><div class="asp-num">2-3x</div><div class="asp-label">Close rate improvement when a structured framework replaces unstructured pitching. The framework is the closer.</div></div>'
)

ART01 = inner_page(
    'What makes a great closer | Kryson Limited',
    'Great closers use a structured framework, not personality. The CLOSER model and why silence after price is the most important skill.',
    'insight-01.html', '',
    'Insight 01',
    'What makes a great closer',
    'Sales Process &middot; 14 Jan 2025',
    art_body(ART01_SVG, ART01_CONTENT),
    "initP('ctaC',15);"
)
with open('insight-01.html','w') as f: f.write(ART01)
print("insight-01.html: {:,}".format(len(ART01)))

# ---- ARTICLE 02: What makes a great setter ----
ART02_SVG = (
'<svg viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" style="background:#111;border-radius:6px">'
'<text x="380" y="26" text-anchor="middle" fill="rgba(255,255,255,0.25)" font-size="10" font-family="sans-serif" letter-spacing="3">SETTER PERFORMANCE: WHAT THE METRICS ACTUALLY MEAN</text>'
'<rect x="30" y="44" width="210" height="210" rx="4" fill="rgba(201,168,76,0.06)" stroke="rgba(201,168,76,0.15)" stroke-width="1"/>'
'<text x="135" y="80" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="11" font-family="sans-serif" letter-spacing="2">SHOW RATE</text>'
'<text x="135" y="126" text-anchor="middle" fill="#c9a84c" font-size="42" font-family="sans-serif" font-weight="700">70%</text>'
'<text x="135" y="152" text-anchor="middle" fill="rgba(255,255,255,0.55)" font-size="11" font-family="sans-serif">benchmark</text>'
'<text x="135" y="170" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="10" font-family="sans-serif">65%+ acceptable</text>'
'<text x="135" y="186" text-anchor="middle" fill="rgba(255,120,120,0.6)" font-size="10" font-family="sans-serif">below 50% = broken</text>'
'<rect x="260" y="44" width="210" height="100" rx="4" fill="rgba(201,168,76,0.06)" stroke="rgba(201,168,76,0.15)" stroke-width="1"/>'
'<text x="365" y="76" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="11" font-family="sans-serif" letter-spacing="2">EXPLICIT AGREE</text>'
'<text x="365" y="112" text-anchor="middle" fill="#c9a84c" font-size="38" font-family="sans-serif" font-weight="700">9.7x</text>'
'<text x="365" y="132" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="10" font-family="sans-serif">more likely to show when</text>'
'<text x="365" y="146" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="10" font-family="sans-serif">prospect explicitly commits</text>'
'<rect x="260" y="154" width="210" height="100" rx="4" fill="rgba(201,168,76,0.06)" stroke="rgba(201,168,76,0.15)" stroke-width="1"/>'
'<text x="365" y="186" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="11" font-family="sans-serif" letter-spacing="2">SPEED TO LEAD</text>'
'<text x="365" y="218" text-anchor="middle" fill="#c9a84c" font-size="38" font-family="sans-serif" font-weight="700">21x</text>'
'<text x="365" y="238" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="10" font-family="sans-serif">qualify rate at 5-min response</text>'
'<text x="365" y="252" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="10" font-family="sans-serif">vs 30-min (Harvard Business Review)</text>'
'<rect x="490" y="44" width="240" height="210" rx="4" fill="rgba(201,168,76,0.06)" stroke="rgba(201,168,76,0.15)" stroke-width="1"/>'
'<text x="610" y="76" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="11" font-family="sans-serif" letter-spacing="2">SETTER JOB</text>'
'<text x="610" y="108" text-anchor="middle" fill="rgba(255,255,255,0.8)" font-size="12" font-family="sans-serif">Qualify intent</text>'
'<text x="610" y="130" text-anchor="middle" fill="rgba(255,255,255,0.8)" font-size="12" font-family="sans-serif">Book and confirm</text>'
'<text x="610" y="152" text-anchor="middle" fill="rgba(255,255,255,0.8)" font-size="12" font-family="sans-serif">Get explicit agree</text>'
'<text x="610" y="174" text-anchor="middle" fill="rgba(255,255,255,0.8)" font-size="12" font-family="sans-serif">Pre-frame the call</text>'
'<text x="610" y="210" text-anchor="middle" fill="rgba(255,120,120,0.6)" font-size="11" font-family="sans-serif">NOT: close the deal</text>'
'<text x="380" y="286" text-anchor="middle" fill="rgba(255,255,255,0.18)" font-size="11" font-family="sans-serif" font-style="italic">Source: SetSmart 828K conversation analysis; Harvard Business Review lead response study</text>'
'</svg>'
)

ART02_CONTENT = (
'<div class="art-stat-pull"><div class="asp-num">70%</div><div class="asp-label">Show rate benchmark for a well-run setter operation. Below 50% means the setter model is broken, not the closer.</div></div>'
'<p>The setter is the front door to your sales process. Everything the closer does depends on who the setter puts in front of them and how prepared that person is when they arrive. Most agencies treat the setter role as an administrative booking function. That is the first mistake.</p>'
'<p>A great setter does not just book calls. They qualify intent, establish the right expectation for the conversation, and get an explicit verbal commitment before the prospect leaves the booking interaction. Each of those three things independently moves show rate.</p>'
'<h3>Why explicit agreement changes the outcome</h3>'
'<p>A study of 828,000 sales conversations by SetSmart found that prospects who explicitly agree to a call are 9.7 times more likely to show up than those who passively book. The difference is not the calendar invite. It is the moment where the setter asks a version of: "Is this something you are genuinely looking to move forward on in the next 30 days?" and the prospect says yes. That response creates commitment. The prospect now has to justify not showing up to themselves.</p>'
'<h3>Speed to lead is a setter metric</h3>'
'<p>Harvard Business Review research found that responding to an inbound lead within five minutes makes you 21 times more likely to qualify that lead than if you wait 30 minutes. Most agencies respond to inbound within hours, or the next day. By that point, the prospect has moved on mentally, booked a call with someone else, or simply cooled off. Speed to lead is a setter discipline. The setter who calls or messages within five minutes of an opt-in is operating in a different conversion bracket than the one who batches their outreach.</p>'
'<h3>What setters are not responsible for</h3>'
'<p>The setter is not responsible for the close. A common failure mode in setter-closer models is that the closer, frustrated with low-quality leads, starts coaching the setter to do more pre-qualifying that bleeds into pitching. This creates a muddled conversation that serves neither role. The setter&#39;s job is show rate, intent confirmation, and pre-frame. The closer&#39;s job is everything that happens after the prospect joins the call.</p>'
'<p>A setter who books 20 calls with a 70 percent show rate and 15 qualified prospects is performing well. A closer who then converts 8 of those 15 is performing well. Those are the right metrics for each role. Keep them separate.</p>'
'<div class="art-stat-pull"><div class="asp-num">3-6</div><div class="asp-label">Months: typical tenure before setter turnover. The role requires constant coaching. Build the process around the seat, not the person.</div></div>'
)

ART02 = inner_page(
    'What makes a great setter | Kryson Limited',
    'The setter is the front door. Show rate, explicit commitment, and speed to lead are the metrics that tell you if the role is working.',
    'insight-02.html', '',
    'Insight 02',
    'What makes a great setter',
    'Sales Process &middot; 3 Mar 2025',
    art_body(ART02_SVG, ART02_CONTENT),
    "initP('ctaC',15);"
)
with open('insight-02.html','w') as f: f.write(ART02)
print("insight-02.html: {:,}".format(len(ART02)))

# ---- ARTICLE 03: Pre-call confirmation sequence ----
ART03_SVG = (
'<svg viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" style="background:#111;border-radius:6px">'
'<text x="380" y="26" text-anchor="middle" fill="rgba(255,255,255,0.25)" font-size="10" font-family="sans-serif" letter-spacing="3">THE FOUR-TOUCH PRE-CALL CONFIRMATION SEQUENCE</text>'
'<line x1="60" y1="148" x2="700" y2="148" stroke="rgba(201,168,76,0.2)" stroke-width="1.5"/>'
'<circle cx="60" cy="148" r="8" fill="#c9a84c"/>'
'<text x="60" y="120" text-anchor="middle" fill="rgba(255,255,255,0.85)" font-size="11" font-family="sans-serif" font-weight="600">Booking</text>'
'<text x="60" y="138" text-anchor="middle" fill="rgba(255,255,255,0.45)" font-size="10" font-family="sans-serif">Immediate</text>'
'<text x="60" y="172" text-anchor="middle" fill="rgba(255,255,255,0.45)" font-size="10" font-family="sans-serif">confirmation</text>'
'<text x="60" y="188" text-anchor="middle" fill="rgba(255,255,255,0.45)" font-size="10" font-family="sans-serif">+ calendar invite</text>'
'<text x="60" y="204" text-anchor="middle" fill="#c9a84c" font-size="10" font-family="sans-serif">Touch 1</text>'
'<circle cx="253" cy="148" r="8" fill="rgba(201,168,76,0.7)"/>'
'<text x="253" y="120" text-anchor="middle" fill="rgba(255,255,255,0.85)" font-size="11" font-family="sans-serif" font-weight="600">T minus 48h</text>'
'<text x="253" y="138" text-anchor="middle" fill="rgba(255,255,255,0.45)" font-size="10" font-family="sans-serif">Email with</text>'
'<text x="253" y="172" text-anchor="middle" fill="rgba(255,255,255,0.45)" font-size="10" font-family="sans-serif">case study or</text>'
'<text x="253" y="188" text-anchor="middle" fill="rgba(255,255,255,0.45)" font-size="10" font-family="sans-serif">social proof</text>'
'<text x="253" y="204" text-anchor="middle" fill="#c9a84c" font-size="10" font-family="sans-serif">Touch 2</text>'
'<circle cx="447" cy="148" r="8" fill="rgba(201,168,76,0.5)"/>'
'<text x="447" y="120" text-anchor="middle" fill="rgba(255,255,255,0.85)" font-size="11" font-family="sans-serif" font-weight="600">T minus 24h</text>'
'<text x="447" y="138" text-anchor="middle" fill="rgba(255,255,255,0.45)" font-size="10" font-family="sans-serif">SMS: anything</text>'
'<text x="447" y="172" text-anchor="middle" fill="rgba(255,255,255,0.45)" font-size="10" font-family="sans-serif">you want us</text>'
'<text x="447" y="188" text-anchor="middle" fill="rgba(255,255,255,0.45)" font-size="10" font-family="sans-serif">to cover?</text>'
'<text x="447" y="204" text-anchor="middle" fill="#c9a84c" font-size="10" font-family="sans-serif">Touch 3</text>'
'<circle cx="700" cy="148" r="10" fill="rgba(201,168,76,0.85)" stroke="#c9a84c" stroke-width="2"/>'
'<text x="700" y="120" text-anchor="middle" fill="rgba(255,255,255,0.95)" font-size="11" font-family="sans-serif" font-weight="600">T minus 2h</text>'
'<text x="700" y="138" text-anchor="middle" fill="rgba(255,255,255,0.55)" font-size="10" font-family="sans-serif">Final email:</text>'
'<text x="700" y="172" text-anchor="middle" fill="rgba(255,255,255,0.55)" font-size="10" font-family="sans-serif">meeting link +</text>'
'<text x="700" y="188" text-anchor="middle" fill="rgba(255,255,255,0.55)" font-size="10" font-family="sans-serif">what to expect</text>'
'<text x="700" y="204" text-anchor="middle" fill="#c9a84c" font-size="10" font-family="sans-serif">Touch 4</text>'
'<text x="380" y="252" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="12" font-family="sans-serif">No confirmation sequence = ~50% no-show rate</text>'
'<text x="380" y="272" text-anchor="middle" fill="#c9a84c" font-size="12" font-family="sans-serif">Four-touch sequence = 70%+ show rate consistently</text>'
'<text x="380" y="292" text-anchor="middle" fill="rgba(255,255,255,0.18)" font-size="10" font-family="sans-serif" font-style="italic">Based on LaunchLeads data across 152K+ booked appointments</text>'
'</svg>'
)

ART03_CONTENT = (
'<div class="art-stat-pull"><div class="asp-num">70%+</div><div class="asp-label">Show rate for agencies running a four-touch confirmation sequence. Without it, show rates routinely drop to 50% or below.</div></div>'
'<p>Most agencies send a calendar invite and assume the prospect will show up. Some add a reminder from their booking tool 24 hours before. That is the entire confirmation process. It is not enough.</p>'
'<p>LaunchLeads, which has set over 152,000 appointments, identifies 70 percent as the benchmark for a healthy show rate and 65 percent as the floor for an acceptable one. Below 50 percent, the model is broken. The difference between a 45 percent show rate and a 72 percent show rate is not better leads. It is a confirmation sequence.</p>'
'<h3>Touch 1: Immediate booking confirmation</h3>'
'<p>Send a confirmation email the moment the call is booked. Include the calendar invite, the meeting link, and a single sentence about what the call will cover. The purpose of this touch is to create certainty. The prospect should not be wondering whether the booking went through or what to expect.</p>'
'<h3>Touch 2: T minus 48 hours</h3>'
'<p>Send an email 48 hours before the call. Include a piece of social proof: a case study, a client result, or a short testimonial. The purpose of this touch is to maintain intent. The prospect booked the call three days ago. Between then and now, their circumstances have not changed, but their attention has moved on. The T-48 email brings them back into the context of why they booked.</p>'
'<h3>Touch 3: T minus 24 hours</h3>'
'<p>Send an SMS 24 hours before the call. Keep it short. A version that works well: "Looking forward to speaking with you tomorrow at [time]. Is there anything specific you would like to make sure we cover?" This message does two things: it confirms the appointment and it invites engagement. A prospect who replies has now interacted with you twice before the call, which moves show rate and warms the conversation.</p>'
'<h3>Touch 4: T minus 2 hours</h3>'
'<p>Send a final email two hours before the call. Include the meeting link, your name, and a one-line description of what you will cover. Keep it to three sentences. The purpose is to remove friction at the moment the prospect is deciding whether to join.</p>'
'<p>Agencies that run this sequence consistently report show rates of 70 percent or above. Those that run no sequence typically land between 40 and 55 percent. The 15 to 30 percentage point gap represents real revenue. At 10 close calls per week with an average deal value of &pound;5,000 per month, moving from 50 to 70 percent show rate is worth two extra calls per week, every week.</p>'
)

ART03 = inner_page(
    'The Pre-Call Confirmation Sequence | Kryson Limited',
    'A four-touch confirmation sequence that moves show rates from 50% to 70% or above. Timing, messaging, and why each touch matters.',
    'insight-03.html', '',
    'Insight 03',
    'The pre-call confirmation sequence',
    'Sales Process &middot; 22 Apr 2025',
    art_body(ART03_SVG, ART03_CONTENT),
    "initP('ctaC',15);"
)
with open('insight-03.html','w') as f: f.write(ART03)
print("insight-03.html: {:,}".format(len(ART03)))

# ---- ARTICLE 04: No-show recovery ----
ART04_SVG = (
'<svg viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" style="background:#111;border-radius:6px">'
'<text x="380" y="26" text-anchor="middle" fill="rgba(255,255,255,0.25)" font-size="10" font-family="sans-serif" letter-spacing="3">NO-SHOW RECOVERY: THE CRITICAL WINDOW</text>'
'<line x1="60" y1="100" x2="700" y2="100" stroke="rgba(201,168,76,0.15)" stroke-width="1"/>'
'<rect x="60" y="44" width="120" height="110" rx="4" fill="rgba(201,168,76,0.18)" stroke="#c9a84c" stroke-width="1.5"/>'
'<text x="120" y="72" text-anchor="middle" fill="#c9a84c" font-size="13" font-family="sans-serif" font-weight="700">0-10 min</text>'
'<text x="120" y="92" text-anchor="middle" fill="rgba(255,255,255,0.8)" font-size="11" font-family="sans-serif">Call or text</text>'
'<text x="120" y="108" text-anchor="middle" fill="rgba(255,255,255,0.6)" font-size="10" font-family="sans-serif">immediately</text>'
'<text x="120" y="124" text-anchor="middle" fill="#c9a84c" font-size="10" font-family="sans-serif">HIGHEST</text>'
'<text x="120" y="138" text-anchor="middle" fill="#c9a84c" font-size="10" font-family="sans-serif">RECOVERY RATE</text>'
'<rect x="200" y="60" width="120" height="94" rx="4" fill="rgba(201,168,76,0.1)" stroke="rgba(201,168,76,0.4)" stroke-width="1"/>'
'<text x="260" y="84" text-anchor="middle" fill="rgba(255,255,255,0.75)" font-size="13" font-family="sans-serif" font-weight="600">Same day</text>'
'<text x="260" y="104" text-anchor="middle" fill="rgba(255,255,255,0.55)" font-size="11" font-family="sans-serif">Reschedule while</text>'
'<text x="260" y="120" text-anchor="middle" fill="rgba(255,255,255,0.55)" font-size="11" font-family="sans-serif">they are still</text>'
'<text x="260" y="136" text-anchor="middle" fill="rgba(255,255,255,0.55)" font-size="11" font-family="sans-serif">apologetic</text>'
'<rect x="340" y="76" width="120" height="78" rx="4" fill="rgba(201,168,76,0.06)" stroke="rgba(201,168,76,0.25)" stroke-width="1"/>'
'<text x="400" y="100" text-anchor="middle" fill="rgba(255,255,255,0.55)" font-size="13" font-family="sans-serif" font-weight="600">24 hours</text>'
'<text x="400" y="120" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="11" font-family="sans-serif">Email with</text>'
'<text x="400" y="136" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="11" font-family="sans-serif">reschedule link</text>'
'<rect x="480" y="90" width="120" height="64" rx="4" fill="rgba(201,168,76,0.04)" stroke="rgba(201,168,76,0.15)" stroke-width="1"/>'
'<text x="540" y="112" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="13" font-family="sans-serif" font-weight="600">Day 3</text>'
'<text x="540" y="132" text-anchor="middle" fill="rgba(255,255,255,0.3)" font-size="11" font-family="sans-serif">Final short</text>'
'<text x="540" y="148" text-anchor="middle" fill="rgba(255,255,255,0.3)" font-size="11" font-family="sans-serif">message</text>'
'<rect x="620" y="106" width="80" height="48" rx="4" fill="rgba(255,60,60,0.04)" stroke="rgba(255,60,60,0.15)" stroke-width="1"/>'
'<text x="660" y="126" text-anchor="middle" fill="rgba(255,100,100,0.5)" font-size="13" font-family="sans-serif" font-weight="600">Day 7+</text>'
'<text x="660" y="144" text-anchor="middle" fill="rgba(255,100,100,0.4)" font-size="10" font-family="sans-serif">lead goes cold</text>'
'<text x="380" y="192" text-anchor="middle" fill="rgba(255,255,255,0.6)" font-size="12" font-family="sans-serif">Recovery rate drops sharply with every hour of delay</text>'
'<text x="380" y="216" text-anchor="middle" fill="rgba(201,168,76,0.8)" font-size="12" font-family="sans-serif" font-weight="600">The 10-minute rule: if they have not joined, reach out now</text>'
'<text x="380" y="250" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="11" font-family="sans-serif">Most no-shows are not rejections. They are schedule failures.</text>'
'<text x="380" y="270" text-anchor="middle" fill="rgba(255,255,255,0.18)" font-size="11" font-family="sans-serif" font-style="italic">Agencies with a recovery sequence rescue 40-60% of no-shows within 48 hours.</text>'
'</svg>'
)

ART04_CONTENT = (
'<div class="art-stat-pull"><div class="asp-num">40-60%</div><div class="asp-label">No-shows recovered within 48 hours by agencies running a structured recovery sequence. Without one, most are never rescheduled.</div></div>'
'<p>A no-show feels like a rejection. It is almost never one. In most cases the prospect is embarrassed, busy, or double-booked. They are not gone. They are waiting to see if you will reach out and make it easy for them to reschedule.</p>'
'<p>The agencies that recover the highest proportion of no-shows share one discipline: they act within 10 minutes. Not the next day. Not in an hour. Within 10 minutes of the scheduled call start time.</p>'
'<h3>The 10-minute rule</h3>'
'<p>When a prospect has not joined the call 10 minutes after the start time, reach out immediately. Call first. If they do not pick up, send a text within the same minute. The message should be simple: "Hey, we had our call booked for [time]. Still here if you can jump on now. Otherwise, when works for a quick reschedule today or tomorrow?"</p>'
'<p>This works for two reasons. First, the prospect is most reachable and most motivated to make it right in the first hour after a missed call. They are aware they missed it. They feel some social obligation. That window is short. Second, proposing same-day or next-day rather than "whenever works for you" creates urgency and eliminates the vague open-ended reschedule that never happens.</p>'
'<h3>Same-day reschedule is the fastest path back</h3>'
'<p>If a prospect picks up within 10 minutes, propose a same-day slot if your calendar allows. A prospect who missed a call and then gets back on one within the same day has essentially reset the appointment. The momentum is preserved. Their interest is confirmed. The deal is alive.</p>'
'<p>If same-day is not possible, get a specific time in the diary before the call ends. Not "let me send you a link." A live booking. The difference in show rate between "I will send you my calendar" and "I have you down for Thursday at 3pm, does that still work?" is substantial.</p>'
'<h3>The full recovery sequence</h3>'
'<p>If the immediate call and text produce no response, follow the sequence: a short email with a reschedule link the same day, a brief check-in 24 hours later, and a final one-liner at day three. After day three with no response, the prospect is cold. Three attempts over 72 hours is the right ratio. More than that reads as desperation. Less than that leaves recoverable deals on the table.</p>'
'<p>Most agencies send one follow-up email and write the no-show off as a lost lead. That single decision costs more revenue annually than almost any other process gap in the sales function.</p>'
)

ART04 = inner_page(
    'No-Show Recovery: The Playbook | Kryson Limited',
    'A no-show is not a lost deal. The 10-minute rule, same-day reschedule, and the three-touch recovery sequence that brings 40-60% of no-shows back.',
    'insight-04.html', '',
    'Insight 04',
    'No-show recovery: the playbook',
    'Sales Process &middot; 9 May 2025',
    art_body(ART04_SVG, ART04_CONTENT),
    "initP('ctaC',15);"
)
with open('insight-04.html','w') as f: f.write(ART04)
print("insight-04.html: {:,}".format(len(ART04)))

# ---- ARTICLE 05: Discovery call framework ----
ART05_SVG = (
'<svg viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" style="background:#111;border-radius:6px">'
'<text x="380" y="26" text-anchor="middle" fill="rgba(255,255,255,0.25)" font-size="10" font-family="sans-serif" letter-spacing="3">DISCOVERY CALL: STAGE BREAKDOWN AND TIME ALLOCATION</text>'
'<rect x="30" y="44" width="155" height="210" rx="4" fill="rgba(201,168,76,0.07)" stroke="rgba(201,168,76,0.18)" stroke-width="1"/>'
'<text x="107" y="84" text-anchor="middle" fill="#c9a84c" font-size="24" font-family="sans-serif" font-weight="700">01</text>'
'<text x="107" y="106" text-anchor="middle" fill="rgba(255,255,255,0.85)" font-size="13" font-family="sans-serif" font-weight="600">Situation</text>'
'<text x="107" y="126" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="10" font-family="sans-serif">Baseline context</text>'
'<text x="107" y="142" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="10" font-family="sans-serif">confirm research</text>'
'<text x="107" y="206" text-anchor="middle" fill="rgba(255,255,255,0.3)" font-size="11" font-family="sans-serif" font-style="italic">10-15%</text>'
'<text x="107" y="224" text-anchor="middle" fill="rgba(255,255,255,0.2)" font-size="10" font-family="sans-serif">of call time</text>'
'<rect x="201" y="44" width="155" height="210" rx="4" fill="rgba(201,168,76,0.1)" stroke="rgba(201,168,76,0.28)" stroke-width="1"/>'
'<text x="278" y="84" text-anchor="middle" fill="#c9a84c" font-size="24" font-family="sans-serif" font-weight="700">02</text>'
'<text x="278" y="106" text-anchor="middle" fill="rgba(255,255,255,0.85)" font-size="13" font-family="sans-serif" font-weight="600">Problem</text>'
'<text x="278" y="126" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="10" font-family="sans-serif">Surface pain in</text>'
'<text x="278" y="142" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="10" font-family="sans-serif">their own words</text>'
'<text x="278" y="206" text-anchor="middle" fill="rgba(255,255,255,0.3)" font-size="11" font-family="sans-serif" font-style="italic">30-35%</text>'
'<text x="278" y="224" text-anchor="middle" fill="rgba(255,255,255,0.2)" font-size="10" font-family="sans-serif">of call time</text>'
'<rect x="372" y="44" width="155" height="210" rx="4" fill="rgba(201,168,76,0.14)" stroke="rgba(201,168,76,0.38)" stroke-width="1"/>'
'<text x="449" y="84" text-anchor="middle" fill="#c9a84c" font-size="24" font-family="sans-serif" font-weight="700">03</text>'
'<text x="449" y="106" text-anchor="middle" fill="rgba(255,255,255,0.85)" font-size="13" font-family="sans-serif" font-weight="600">Impact</text>'
'<text x="449" y="126" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="10" font-family="sans-serif">Quantify cost in</text>'
'<text x="449" y="142" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="10" font-family="sans-serif">money and time</text>'
'<text x="449" y="206" text-anchor="middle" fill="rgba(255,255,255,0.3)" font-size="11" font-family="sans-serif" font-style="italic">25-30%</text>'
'<text x="449" y="224" text-anchor="middle" fill="rgba(255,255,255,0.2)" font-size="10" font-family="sans-serif">of call time</text>'
'<rect x="543" y="44" width="187" height="210" rx="4" fill="rgba(201,168,76,0.2)" stroke="#c9a84c" stroke-width="1.5"/>'
'<text x="636" y="84" text-anchor="middle" fill="#c9a84c" font-size="24" font-family="sans-serif" font-weight="700">04</text>'
'<text x="636" y="106" text-anchor="middle" fill="rgba(255,255,255,0.95)" font-size="13" font-family="sans-serif" font-weight="600">Implication</text>'
'<text x="636" y="126" text-anchor="middle" fill="rgba(255,255,255,0.6)" font-size="10" font-family="sans-serif">Project forward</text>'
'<text x="636" y="142" text-anchor="middle" fill="rgba(255,255,255,0.6)" font-size="10" font-family="sans-serif">cost of inaction</text>'
'<text x="636" y="180" text-anchor="middle" fill="#c9a84c" font-size="10" font-family="sans-serif" letter-spacing="1">CLOSE READY</text>'
'<text x="636" y="206" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="11" font-family="sans-serif" font-style="italic">20-25%</text>'
'<text x="636" y="224" text-anchor="middle" fill="rgba(255,255,255,0.3)" font-size="10" font-family="sans-serif">of call time</text>'
'<text x="380" y="282" text-anchor="middle" fill="rgba(255,255,255,0.18)" font-size="11" font-family="sans-serif" font-style="italic">80% of agency discovery calls never leave Stage 01. That is where close rates collapse.</text>'
'</svg>'
)

ART05_CONTENT = (
'<div class="art-stat-pull"><div class="asp-num">80%</div><div class="asp-label">Proportion of agency discovery calls spent on Stage 01 (situation). Stages 03 and 04 are where deals are won. Most founders never get there.</div></div>'
'<p>Discovery is not an interview. It is the process by which a prospect talks themselves into buying. The closer who understands this structures their discovery to make that internal journey inevitable. The one who does not spends 45 minutes explaining the service and wonders why conversion is low.</p>'
'<p>The four-stage framework addresses each phase of the prospect&#39;s decision-making process. Each stage has a specific purpose, and skipping or shortchanging a stage means arriving at the close without the foundation the close needs.</p>'
'<h3>Stage 01: Situation</h3>'
'<p>Establish baseline context. Confirm what you already know from research. Validate your assumptions. This stage should be short, 10 to 15 percent of the call. Its purpose is not to gather information you could have found before the call. It is to give the prospect the experience of being understood, which opens them up for the harder questions that follow.</p>'
'<h3>Stage 02: Problem</h3>'
'<p>Surface what is not working, in their words. Use open questions. Resist the urge to suggest the answer. The language the prospect uses to describe their problem in this stage is the language you mirror back on the close call. "You mentioned that your close rate has been stuck at 12 percent for six months and you&#39;ve already tried hiring one salesperson who did not work out" lands completely differently than any version of your service description.</p>'
'<h3>Stage 03: Impact</h3>'
'<p>Quantify the cost of the problem. Not in abstract terms. In specific numbers. "What does a bad month look like in your business?" "What would a 10-point improvement in close rate mean to your annual revenue?" This converts the problem from uncomfortable to urgent. A prospect who has articulated that staying where they are costs them &pound;15,000 per month in foregone revenue has a very different relationship with the investment required to fix it.</p>'
'<h3>Stage 04: Implication</h3>'
'<p>Help the prospect project the pattern forward. If nothing changes in the next six months, what does that look like? Not a catastrophe. A projection. "If your close rate stays at 12 percent and your lead volume stays flat, what does Q4 look like?" This stage creates the internal justification for change that no pitch can manufacture. The prospect has now reasoned their way to the conclusion that something needs to change. Your solution is what answers that conclusion.</p>'
'<p>By the time you reach the solution, you are not introducing something new. You are answering a question the prospect has already asked themselves.</p>'
)

ART05 = inner_page(
    'The Discovery Call Framework That Actually Converts | Kryson Limited',
    'Discovery is not an interview. The four-stage framework that moves prospects from situation to shared diagnosis and makes the close a natural next step.',
    'insight-05.html', '',
    'Insight 05',
    'The discovery call framework that actually converts',
    'Sales Process &middot; 1 Jul 2025',
    art_body(ART05_SVG, ART05_CONTENT),
    "initP('ctaC',15);"
)
with open('insight-05.html','w') as f: f.write(ART05)
print("insight-05.html: {:,}".format(len(ART05)))

# ---- ARTICLE 06: Frame: the invisible variable ----
ART06_SVG = (
'<svg viewBox="0 0 760 290" xmlns="http://www.w3.org/2000/svg" style="background:#111;border-radius:6px">'
'<text x="380" y="26" text-anchor="middle" fill="rgba(255,255,255,0.25)" font-size="10" font-family="sans-serif" letter-spacing="3">FRAME COMPARISON: SAME SCRIPT, DIFFERENT OUTCOME</text>'
'<rect x="30" y="44" width="335" height="210" rx="4" fill="rgba(255,80,80,0.04)" stroke="rgba(255,80,80,0.18)" stroke-width="1"/>'
'<text x="197" y="74" text-anchor="middle" fill="rgba(255,100,100,0.75)" font-size="13" font-family="sans-serif" font-weight="600" letter-spacing="1">SALES FRAME</text>'
'<text x="197" y="96" text-anchor="middle" fill="rgba(255,255,255,0.3)" font-size="11" font-family="sans-serif">You need to convince them</text>'
'<line x1="60" y1="110" x2="334" y2="110" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>'
'<text x="60" y="134" fill="rgba(255,255,255,0.45)" font-size="12" font-family="sans-serif">Answering objections defensively</text>'
'<text x="60" y="158" fill="rgba(255,255,255,0.45)" font-size="12" font-family="sans-serif">Justifying the price</text>'
'<text x="60" y="182" fill="rgba(255,255,255,0.45)" font-size="12" font-family="sans-serif">Giving away control to keep them</text>'
'<text x="60" y="206" fill="rgba(255,255,255,0.45)" font-size="12" font-family="sans-serif">Fear of the close</text>'
'<text x="60" y="230" fill="rgba(255,255,255,0.45)" font-size="12" font-family="sans-serif">Following the prospect&#39;s lead</text>'
'<rect x="395" y="44" width="335" height="210" rx="4" fill="rgba(201,168,76,0.07)" stroke="rgba(201,168,76,0.35)" stroke-width="1.5"/>'
'<text x="562" y="74" text-anchor="middle" fill="#c9a84c" font-size="13" font-family="sans-serif" font-weight="600" letter-spacing="1">INTERVIEW FRAME</text>'
'<text x="562" y="96" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="11" font-family="sans-serif">You are deciding if they qualify</text>'
'<line x1="425" y1="110" x2="699" y2="110" stroke="rgba(201,168,76,0.15)" stroke-width="1"/>'
'<text x="425" y="134" fill="rgba(255,255,255,0.8)" font-size="12" font-family="sans-serif">Curious about the objection</text>'
'<text x="425" y="158" fill="rgba(255,255,255,0.8)" font-size="12" font-family="sans-serif">Price is stated and held</text>'
'<text x="425" y="182" fill="rgba(255,255,255,0.8)" font-size="12" font-family="sans-serif">Willing to walk away</text>'
'<text x="425" y="206" fill="rgba(255,255,255,0.8)" font-size="12" font-family="sans-serif">Comfortable with silence</text>'
'<text x="425" y="230" fill="#c9a84c" font-size="12" font-family="sans-serif">Setting the pace of the conversation</text>'
'<text x="380" y="278" text-anchor="middle" fill="rgba(255,255,255,0.18)" font-size="11" font-family="sans-serif" font-style="italic">Frame is not what you say. It is the posture from which everything you say is delivered.</text>'
'</svg>'
)

ART06_CONTENT = (
'<div class="art-stat-pull"><div class="asp-num">Frame</div><div class="asp-label">The variable that explains why two closers with identical scripts produce different close rates. It is not confidence. It is posture.</div></div>'
'<p>Two salespeople can say the same words and produce completely different outcomes. One closes at 35 percent. The other closes at 12 percent. The words are the same. The frame is not.</p>'
'<p>Frame is the underlying posture from which a sales conversation is conducted. It is not tone, not script, not pitch structure. It is the implicit answer to the question: who has authority in this conversation? In a sales frame, the prospect has authority. In an interview frame, the seller does.</p>'
'<h3>The sales frame and why it loses</h3>'
'<p>A closer operating from a sales frame is trying to convince. They answer objections defensively because objections feel like threats. They justify the price because they are not sure it is right. They follow the prospect&#39;s lead because they are afraid that pushing back will cost the deal. The prospect senses this. Not consciously, but they do. And they respond the way people respond to desperation: they either take advantage of it or walk away.</p>'
'<h3>The interview frame and why it wins</h3>'
'<p>A closer operating from an interview frame is evaluating whether the prospect is a fit. They are curious about objections because objections are data. They hold the price because they believe in it. They are genuinely willing to walk away from deals that are not right, and the prospect knows it. This posture creates the conditions for a decision. The prospect stops evaluating whether to buy and starts evaluating whether they qualify.</p>'
'<h3>How to shift frame in a call</h3>'
'<p>Frame is established in the first three minutes of a call and is very difficult to recover once lost. The ANOT opener sets frame before any substantive conversation begins. Establishing that you will be asking questions, that both parties are deciding if there is a fit, and that you will be honest if this is not the right solution puts the call on interview ground from the start.</p>'
'<p>When frame breaks during a call, the most reliable recovery is to slow down, name the dynamic, and restate your position clearly. "Let me be honest with you. I am not going to tell you this is the right move if I do not think it is. What I am trying to understand is whether the problem you described is real enough to justify making a change." That sentence re-establishes frame in under 15 seconds.</p>'
'<p>Most closer training focuses on scripts and objection responses. Frame training does not make the headlines, but it is responsible for more of the variance in close rate than any technique.</p>'
)

ART06 = inner_page(
    'Frame: The Invisible Variable in Every Sales Call | Kryson Limited',
    'Two closers, same script, different close rates. Frame is the posture from which everything is delivered. How it is set, lost, and recovered.',
    'insight-06.html', '',
    'Insight 06',
    'Frame: the invisible variable in every sales call',
    'Sales Psychology &middot; 18 Aug 2025',
    art_body(ART06_SVG, ART06_CONTENT),
    "initP('ctaC',15);"
)
with open('insight-06.html','w') as f: f.write(ART06)
print("insight-06.html: {:,}".format(len(ART06)))

# ---- ARTICLE 07: One-call close structure ----
ART07_SVG = (
'<svg viewBox="0 0 760 290" xmlns="http://www.w3.org/2000/svg" style="background:#111;border-radius:6px">'
'<text x="380" y="26" text-anchor="middle" fill="rgba(255,255,255,0.25)" font-size="10" font-family="sans-serif" letter-spacing="3">ONE-CALL CLOSE: TIME AND STAGE BREAKDOWN (60 MIN)</text>'
'<rect x="30" y="44" width="90" height="196" rx="3" fill="rgba(201,168,76,0.08)" stroke="rgba(201,168,76,0.2)" stroke-width="1"/>'
'<text x="75" y="82" text-anchor="middle" fill="#c9a84c" font-size="18" font-family="sans-serif" font-weight="700">10m</text>'
'<text x="75" y="102" text-anchor="middle" fill="rgba(255,255,255,0.7)" font-size="11" font-family="sans-serif" font-weight="600">Rapport</text>'
'<text x="75" y="120" text-anchor="middle" fill="rgba(255,255,255,0.3)" font-size="10" font-family="sans-serif">ANOT opener</text>'
'<text x="75" y="136" text-anchor="middle" fill="rgba(255,255,255,0.3)" font-size="10" font-family="sans-serif">set the frame</text>'
'<rect x="134" y="44" width="120" height="196" rx="3" fill="rgba(201,168,76,0.1)" stroke="rgba(201,168,76,0.28)" stroke-width="1"/>'
'<text x="194" y="82" text-anchor="middle" fill="#c9a84c" font-size="18" font-family="sans-serif" font-weight="700">15m</text>'
'<text x="194" y="102" text-anchor="middle" fill="rgba(255,255,255,0.7)" font-size="11" font-family="sans-serif" font-weight="600">Discovery</text>'
'<text x="194" y="120" text-anchor="middle" fill="rgba(255,255,255,0.3)" font-size="10" font-family="sans-serif">Problem, impact</text>'
'<text x="194" y="136" text-anchor="middle" fill="rgba(255,255,255,0.3)" font-size="10" font-family="sans-serif">implication</text>'
'<rect x="268" y="44" width="120" height="196" rx="3" fill="rgba(201,168,76,0.12)" stroke="rgba(201,168,76,0.32)" stroke-width="1"/>'
'<text x="328" y="82" text-anchor="middle" fill="#c9a84c" font-size="18" font-family="sans-serif" font-weight="700">10m</text>'
'<text x="328" y="102" text-anchor="middle" fill="rgba(255,255,255,0.7)" font-size="11" font-family="sans-serif" font-weight="600">Future pace</text>'
'<text x="328" y="120" text-anchor="middle" fill="rgba(255,255,255,0.3)" font-size="10" font-family="sans-serif">Sell the vacation</text>'
'<text x="328" y="136" text-anchor="middle" fill="rgba(255,255,255,0.3)" font-size="10" font-family="sans-serif">before the price</text>'
'<rect x="402" y="44" width="120" height="196" rx="3" fill="rgba(201,168,76,0.15)" stroke="rgba(201,168,76,0.38)" stroke-width="1"/>'
'<text x="462" y="82" text-anchor="middle" fill="#c9a84c" font-size="18" font-family="sans-serif" font-weight="700">15m</text>'
'<text x="462" y="102" text-anchor="middle" fill="rgba(255,255,255,0.7)" font-size="11" font-family="sans-serif" font-weight="600">Present</text>'
'<text x="462" y="120" text-anchor="middle" fill="rgba(255,255,255,0.3)" font-size="10" font-family="sans-serif">Solution + price</text>'
'<text x="462" y="136" text-anchor="middle" fill="rgba(255,255,255,0.3)" font-size="10" font-family="sans-serif">then silence</text>'
'<rect x="536" y="44" width="100" height="196" rx="3" fill="rgba(201,168,76,0.18)" stroke="rgba(201,168,76,0.42)" stroke-width="1"/>'
'<text x="586" y="82" text-anchor="middle" fill="#c9a84c" font-size="18" font-family="sans-serif" font-weight="700">8m</text>'
'<text x="586" y="102" text-anchor="middle" fill="rgba(255,255,255,0.7)" font-size="11" font-family="sans-serif" font-weight="600">Objections</text>'
'<text x="586" y="120" text-anchor="middle" fill="rgba(255,255,255,0.3)" font-size="10" font-family="sans-serif">Diagnose first</text>'
'<text x="586" y="136" text-anchor="middle" fill="rgba(255,255,255,0.3)" font-size="10" font-family="sans-serif">then handle</text>'
'<rect x="650" y="44" width="80" height="196" rx="3" fill="rgba(201,168,76,0.25)" stroke="#c9a84c" stroke-width="2"/>'
'<text x="690" y="82" text-anchor="middle" fill="#c9a84c" font-size="18" font-family="sans-serif" font-weight="700">2m</text>'
'<text x="690" y="102" text-anchor="middle" fill="rgba(255,255,255,0.9)" font-size="11" font-family="sans-serif" font-weight="600">Close</text>'
'<text x="690" y="120" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="10" font-family="sans-serif">Ask + silence</text>'
'<text x="690" y="136" text-anchor="middle" fill="#c9a84c" font-size="10" font-family="sans-serif">HOLD IT</text>'
'<text x="380" y="278" text-anchor="middle" fill="rgba(255,255,255,0.18)" font-size="11" font-family="sans-serif" font-style="italic">The close takes 2 minutes. Everything before it is what makes the close possible.</text>'
'</svg>'
)

ART07_CONTENT = (
'<div class="art-stat-pull"><div class="asp-num">60 min</div><div class="asp-label">The full arc of a one-call close. Not a shorter pitch. A complete journey from pain to decision in a single session.</div></div>'
'<p>A one-call close is not a faster pitch. It is a complete arc: from the first question about why they are on the call, through the full discovery of their problem and its cost, through a picture of the future they want, all the way to a decision, in a single session.</p>'
'<p>It works for warm leads, founder-to-founder conversations, and lower-ticket services where the risk of a wrong decision is manageable. It does not work for cold traffic, high-ticket complex services, or situations where a decision-maker needs time to consult with a partner or board. Understanding which situation you are in is the first decision.</p>'
'<h3>The structure</h3>'
'<p>The first 10 minutes are the ANOT opener and rapport. Set the frame, establish how the call will run, and confirm the agenda. This is not small talk. It is frame-setting. A prospect who starts the call clear on what is about to happen and who asked them a few genuine questions about their business is in a completely different posture than one who was taken straight to a pitch.</p>'
'<p>The next 15 minutes are discovery. Situation, problem, impact, implication. Do not skip stages. Do not rush to the solution. The prospect needs to have articulated the problem and its cost in their own words before any solution is relevant to them.</p>'
'<p>The next 10 minutes are future pacing. Before the price, before the deliverables, paint the destination. What does the business look like with the problem solved? Specific outcomes. Revenue targets. Time back. The prospect must want the outcome before you introduce the investment required to get there. This is the stage most closers skip and then wonder why the price feels too high.</p>'
'<h3>The price and the silence</h3>'
'<p>After 15 minutes presenting the solution and the price, ask a version of "Does that make sense as a starting point?" and stop talking. The first person to speak after the price loses leverage. This is the most important and most consistently violated rule in closing. Most closers fill the silence because they are uncomfortable. Train yourself to hold it. The prospect will speak within 30 seconds. What they say next is the real conversation.</p>'
)

ART07 = inner_page(
    'The One-Call Close: Structure and Timing | Kryson Limited',
    'A one-call close is not a shorter pitch. The full 60-minute arc from pain to decision, and why the price silence is the most important moment.',
    'insight-07.html', '',
    'Insight 07',
    'The one-call close: structure and timing',
    'Sales Process &middot; 5 Oct 2025',
    art_body(ART07_SVG, ART07_CONTENT),
    "initP('ctaC',15);"
)
with open('insight-07.html','w') as f: f.write(ART07)
print("insight-07.html: {:,}".format(len(ART07)))

# ---- ARTICLE 08: Two-call close ----
ART08_SVG = (
'<svg viewBox="0 0 760 290" xmlns="http://www.w3.org/2000/svg" style="background:#111;border-radius:6px">'
'<text x="380" y="26" text-anchor="middle" fill="rgba(255,255,255,0.25)" font-size="10" font-family="sans-serif" letter-spacing="3">THE TWO-CALL CLOSE: WHERE CALL 2 IS WON OR LOST</text>'
'<rect x="30" y="44" width="330" height="205" rx="4" fill="rgba(201,168,76,0.06)" stroke="rgba(201,168,76,0.28)" stroke-width="1"/>'
'<text x="195" y="72" text-anchor="middle" fill="#c9a84c" font-size="13" font-family="sans-serif" font-weight="700" letter-spacing="1">CALL 1: DISCOVERY</text>'
'<text x="60" y="100" fill="rgba(255,255,255,0.65)" font-size="12" font-family="sans-serif">Situation, problem, impact</text>'
'<text x="60" y="122" fill="rgba(255,255,255,0.65)" font-size="12" font-family="sans-serif">Cost of inaction confirmed</text>'
'<text x="60" y="144" fill="rgba(255,255,255,0.65)" font-size="12" font-family="sans-serif">Decision process mapped</text>'
'<text x="60" y="166" fill="rgba(255,255,255,0.65)" font-size="12" font-family="sans-serif">Budget range confirmed</text>'
'<line x1="60" y1="182" x2="334" y2="182" stroke="rgba(201,168,76,0.15)" stroke-width="1"/>'
'<text x="60" y="206" fill="#c9a84c" font-size="12" font-family="sans-serif" font-weight="600">Ending correctly:</text>'
'<text x="60" y="224" fill="rgba(255,255,255,0.55)" font-size="11" font-family="sans-serif">"Based on what you told me, I think</text>'
'<text x="60" y="240" fill="rgba(255,255,255,0.55)" font-size="11" font-family="sans-serif">we can help. Let me show you Thursday."</text>'
'<rect x="400" y="44" width="330" height="205" rx="4" fill="rgba(201,168,76,0.1)" stroke="#c9a84c" stroke-width="1.5"/>'
'<text x="565" y="72" text-anchor="middle" fill="#c9a84c" font-size="13" font-family="sans-serif" font-weight="700" letter-spacing="1">CALL 2: CLOSE CALL</text>'
'<text x="420" y="100" fill="rgba(255,255,255,0.75)" font-size="12" font-family="sans-serif">Brief recap of the problem</text>'
'<text x="420" y="122" fill="rgba(255,255,255,0.75)" font-size="12" font-family="sans-serif">Present solution + investment</text>'
'<text x="420" y="144" fill="rgba(255,255,255,0.75)" font-size="12" font-family="sans-serif">Handle objections</text>'
'<text x="420" y="166" fill="rgba(255,255,255,0.75)" font-size="12" font-family="sans-serif">Ask for the decision</text>'
'<line x1="420" y1="182" x2="700" y2="182" stroke="rgba(201,168,76,0.25)" stroke-width="1"/>'
'<text x="420" y="204" fill="rgba(201,168,76,0.7)" font-size="12" font-family="sans-serif" font-weight="600">Won or lost on Call 1 ending</text>'
'<text x="420" y="222" fill="rgba(255,255,255,0.45)" font-size="11" font-family="sans-serif">If Call 1 ending was vague,</text>'
'<text x="420" y="238" fill="rgba(255,255,255,0.45)" font-size="11" font-family="sans-serif">Call 2 starts in the wrong frame.</text>'
'<text x="380" y="278" text-anchor="middle" fill="rgba(255,255,255,0.18)" font-size="11" font-family="sans-serif" font-style="italic">Most agencies spend all their prep time on Call 2. The outcome is decided on how Call 1 ends.</text>'
'</svg>'
)

ART08_CONTENT = (
'<div class="art-stat-pull"><div class="asp-num">Call 1</div><div class="asp-label">Where the two-call close is won or lost. Not on the close call. On how the discovery call ends. Most agencies get this backwards.</div></div>'
'<p>The two-call close model separates discovery from decision. Call 1 is for diagnosis. Call 2 is for commitment. Most agencies understand this at a structural level. What they miss is that Call 2 is not a standalone event. Its outcome is largely determined by how Call 1 ends.</p>'
'<p>If Call 1 ends with "I will send you some information," the prospect has no commitment to the next conversation and no frame for what it will be. They are going into Call 2 as an evaluator, not as someone who has already decided they have a problem worth solving.</p>'
'<h3>How Call 1 should end</h3>'
'<p>The ending of Call 1 needs to do three things. First, reflect back the problem and its cost in the prospect&#39;s own words. This confirms that you heard them and reinforces the urgency. Second, state your honest assessment: "Based on everything you&#39;ve shared, I think we can help you with this." Not a pitch. A diagnostic conclusion. Third, propose a specific next step: "Let me put together what that looks like for your situation and we can go through it on Thursday. Does that work?" Get a specific time agreed before the call ends. Not a calendar link. A confirmed slot.</p>'
'<h3>Why this changes the frame for Call 2</h3>'
'<p>A prospect who ends Call 1 having received a diagnostic conclusion and agreed to a specific follow-up arrives at Call 2 in a completely different posture than one who received "I will be in touch." They have already heard your honest assessment. They have already committed to another conversation. The second call is a decision, not an evaluation. That shift in frame is worth more than any presentation technique.</p>'
'<h3>When to use two calls vs one</h3>'
'<p>Two calls work well for higher-ticket services, complex engagements, or situations where the prospect needs to involve another decision maker. One call works for warmer audiences, lower ticket, or when the prospect has already done enough research that the discovery is brief. The tell is qualification: if budget, authority, need, and timeline are confirmed in the first 15 minutes, a one-call close is viable. If any of those are uncertain, book a second call.</p>'
)

ART08 = inner_page(
    'The Two-Call Close: Why Call One Ending Right Is Everything | Kryson Limited',
    'The second call is won or lost on how the first one ends. The exact ending structure that shifts the prospect from evaluator to decision-maker.',
    'insight-08.html', '',
    'Insight 08',
    'The two-call close: why call one ending right is everything',
    'Sales Process &middot; 29 Nov 2025',
    art_body(ART08_SVG, ART08_CONTENT),
    "initP('ctaC',15);"
)
with open('insight-08.html','w') as f: f.write(ART08)
print("insight-08.html: {:,}".format(len(ART08)))

# ---- ARTICLE 09: Post-call follow-up ----
ART09_SVG = (
'<svg viewBox="0 0 760 290" xmlns="http://www.w3.org/2000/svg" style="background:#111;border-radius:6px">'
'<text x="380" y="26" text-anchor="middle" fill="rgba(255,255,255,0.25)" font-size="10" font-family="sans-serif" letter-spacing="3">THE 14-DAY POST-CALL FOLLOW-UP SEQUENCE</text>'
'<line x1="60" y1="130" x2="700" y2="130" stroke="rgba(201,168,76,0.2)" stroke-width="1.5"/>'
'<circle cx="60" cy="130" r="7" fill="#c9a84c"/>'
'<text x="60" y="108" text-anchor="middle" fill="rgba(255,255,255,0.7)" font-size="11" font-family="sans-serif" font-weight="600">Call ends</text>'
'<text x="60" y="154" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="10" font-family="sans-serif">Confirm next</text>'
'<text x="60" y="168" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="10" font-family="sans-serif">step live</text>'
'<circle cx="200" cy="130" r="7" fill="rgba(201,168,76,0.8)"/>'
'<text x="200" y="108" text-anchor="middle" fill="rgba(255,255,255,0.7)" font-size="11" font-family="sans-serif" font-weight="600">Same day</text>'
'<text x="200" y="154" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="10" font-family="sans-serif">Recap email</text>'
'<text x="200" y="168" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="10" font-family="sans-serif">problem mirror</text>'
'<circle cx="340" cy="130" r="7" fill="rgba(201,168,76,0.65)"/>'
'<text x="340" y="108" text-anchor="middle" fill="rgba(255,255,255,0.7)" font-size="11" font-family="sans-serif" font-weight="600">Day 2</text>'
'<text x="340" y="154" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="10" font-family="sans-serif">Relevant</text>'
'<text x="340" y="168" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="10" font-family="sans-serif">case study</text>'
'<circle cx="480" cy="130" r="7" fill="rgba(201,168,76,0.5)"/>'
'<text x="480" y="108" text-anchor="middle" fill="rgba(255,255,255,0.7)" font-size="11" font-family="sans-serif" font-weight="600">Day 5</text>'
'<text x="480" y="154" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="10" font-family="sans-serif">Phone call</text>'
'<text x="480" y="168" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="10" font-family="sans-serif">surface blockers</text>'
'<circle cx="580" cy="130" r="7" fill="rgba(201,168,76,0.4)"/>'
'<text x="580" y="108" text-anchor="middle" fill="rgba(255,255,255,0.55)" font-size="11" font-family="sans-serif" font-weight="600">Day 7</text>'
'<text x="580" y="154" text-anchor="middle" fill="rgba(255,255,255,0.3)" font-size="10" font-family="sans-serif">Short value</text>'
'<text x="580" y="168" text-anchor="middle" fill="rgba(255,255,255,0.3)" font-size="10" font-family="sans-serif">touchpoint</text>'
'<circle cx="700" cy="130" r="9" fill="rgba(201,168,76,0.85)" stroke="#c9a84c" stroke-width="2"/>'
'<text x="700" y="108" text-anchor="middle" fill="rgba(255,255,255,0.9)" font-size="11" font-family="sans-serif" font-weight="600">Day 14</text>'
'<text x="700" y="154" text-anchor="middle" fill="#c9a84c" font-size="10" font-family="sans-serif">One-liner:</text>'
'<text x="700" y="168" text-anchor="middle" fill="#c9a84c" font-size="10" font-family="sans-serif">still a priority?</text>'
'<text x="380" y="210" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="12" font-family="sans-serif">71% of leads never receive follow-up in the first hour after a call</text>'
'<text x="380" y="232" text-anchor="middle" fill="rgba(201,168,76,0.75)" font-size="12" font-family="sans-serif" font-weight="600">A 5-touch sequence over 14 days is where most revenue is recovered</text>'
'<text x="380" y="272" text-anchor="middle" fill="rgba(255,255,255,0.18)" font-size="11" font-family="sans-serif" font-style="italic">Stalled deals are not lost deals. Most agencies treat them the same way.</text>'
'</svg>'
)

ART09_CONTENT = (
'<div class="art-stat-pull"><div class="asp-num">71%</div><div class="asp-label">Of leads never receive structured follow-up within the first hour after a call. The 14-day sequence is where most lost revenue actually lives.</div></div>'
'<p>Most agencies have two modes: following up immediately when they are excited about a deal, and going quiet when they are not sure what to say. Both are wrong. A systematic post-call follow-up sequence removes the reliance on motivation and creates a consistent process that moves deals forward regardless of how the call felt.</p>'
'<h3>Same day: the problem mirror</h3>'
'<p>Within a few hours of the call ending, send a short email that mirrors back the problem in the prospect&#39;s own language. Two or three sentences. Not a pitch, not a summary of your service, not "great to speak with you." A reflection of what they told you: "Based on what you shared, the core issue is that your close rate has been stuck at 12 percent despite adding leads, and you&#39;ve already tried one closer who did not work out." This confirms you listened. It reinforces the urgency. It gives the prospect something real from the conversation.</p>'
'<h3>Day 2: relevant case study</h3>'
'<p>Send a case study that matches their situation as closely as possible. Not your best result. The most relevant one. If they run a paid media agency, send a paid media agency result. Specificity is what builds credibility. A generic case study says you work with agencies. A specific one says you have solved their exact problem before.</p>'
'<h3>Day 5: phone call</h3>'
'<p>Call, do not email. Ask if any questions have come up since the conversation. Surface any concerns before they harden into objections. If no close call is booked, propose one now with a specific time. Getting a live yes on a phone call produces a fundamentally different level of commitment than a reply to an email.</p>'
'<h3>Day 7 and Day 14</h3>'
'<p>Day 7 is a light touchpoint: a relevant article, a short observation, something that keeps your name in their peripheral awareness without asking them to do anything. Day 14 is the decision-forcing close: "Is this still something you are looking to move on this quarter?" That question is three words and a question mark. It makes it easy to say no, which is valuable. The people who reply "yes, sorry I have been quiet" were never lost. They just needed one more reason to respond.</p>'
)

ART09 = inner_page(
    'Post-Call Follow-Up: The 14-Day Sequence | Kryson Limited',
    '71% of leads receive no follow-up within the first hour. The five-touch sequence that recovers stalled deals and turns quiet prospects into closed revenue.',
    'insight-09.html', '',
    'Insight 09',
    'Post-call follow-up: the 14-day sequence',
    'Sales Process &middot; 14 Jan 2026',
    art_body(ART09_SVG, ART09_CONTENT),
    "initP('ctaC',15);"
)
with open('insight-09.html','w') as f: f.write(ART09)
print("insight-09.html: {:,}".format(len(ART09)))

# ---- ARTICLE 10: The four real objections ----
ART10_SVG = (
'<svg viewBox="0 0 760 290" xmlns="http://www.w3.org/2000/svg" style="background:#111;border-radius:6px">'
'<text x="380" y="26" text-anchor="middle" fill="rgba(255,255,255,0.25)" font-size="10" font-family="sans-serif" letter-spacing="3">THE FOUR REAL OBJECTIONS BEHIND EVERY STALL</text>'
'<rect x="30" y="44" width="330" height="108" rx="4" fill="rgba(255,200,80,0.05)" stroke="rgba(255,200,80,0.25)" stroke-width="1"/>'
'<text x="195" y="72" text-anchor="middle" fill="rgba(255,200,80,0.85)" font-size="13" font-family="sans-serif" font-weight="700">MONEY</text>'
'<text x="195" y="94" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="11" font-family="sans-serif">"I can&#39;t afford it"</text>'
'<text x="195" y="112" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="10" font-family="sans-serif">Handle: "What does staying where you</text>'
'<text x="195" y="128" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="10" font-family="sans-serif">are cost you per month?"</text>'
'<rect x="400" y="44" width="330" height="108" rx="4" fill="rgba(100,180,255,0.05)" stroke="rgba(100,180,255,0.25)" stroke-width="1"/>'
'<text x="565" y="72" text-anchor="middle" fill="rgba(130,190,255,0.85)" font-size="13" font-family="sans-serif" font-weight="700">TRUST</text>'
'<text x="565" y="94" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="11" font-family="sans-serif">"I&#39;m not sure this will work"</text>'
'<text x="565" y="112" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="10" font-family="sans-serif">Handle: case study matching their</text>'
'<text x="565" y="128" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="10" font-family="sans-serif">exact situation + specific outcomes</text>'
'<rect x="30" y="166" width="330" height="108" rx="4" fill="rgba(255,130,80,0.05)" stroke="rgba(255,130,80,0.25)" stroke-width="1"/>'
'<text x="195" y="194" text-anchor="middle" fill="rgba(255,160,100,0.85)" font-size="13" font-family="sans-serif" font-weight="700">URGENCY</text>'
'<text x="195" y="216" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="11" font-family="sans-serif">"Now&#39;s not the right time"</text>'
'<text x="195" y="234" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="10" font-family="sans-serif">Handle: "What does Q4 look like if</text>'
'<text x="195" y="250" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="10" font-family="sans-serif">nothing changes between now and then?"</text>'
'<rect x="400" y="166" width="330" height="108" rx="4" fill="rgba(201,168,76,0.1)" stroke="#c9a84c" stroke-width="1.5"/>'
'<text x="565" y="194" text-anchor="middle" fill="#c9a84c" font-size="13" font-family="sans-serif" font-weight="700">AUTHORITY</text>'
'<text x="565" y="216" text-anchor="middle" fill="rgba(255,255,255,0.6)" font-size="11" font-family="sans-serif">"I need to talk to my partner"</text>'
'<text x="565" y="234" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="10" font-family="sans-serif">Handle: "What would they want to know?</text>'
'<text x="565" y="250" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="10" font-family="sans-serif">Let&#39;s go through that now together."</text>'
'<text x="380" y="282" text-anchor="middle" fill="rgba(255,255,255,0.18)" font-size="11" font-family="sans-serif" font-style="italic">Every objection maps to one of these four. The handle is different for each.</text>'
'</svg>'
)

ART10_CONTENT = (
'<div class="art-stat-pull"><div class="asp-num">4</div><div class="asp-label">Real objections behind every stall: Trust, Money, Urgency, Authority. The verbal packaging changes. The underlying concern does not.</div></div>'
'<p>Prospects rarely say what they actually mean when they object. "I need to think about it" is not a request for thinking time. "The timing is not right" is not a calendar problem. Every objection, regardless of how it is framed, is one of four things: trust, money, urgency, or authority. Identifying which one you are dealing with is the only thing that makes the response useful.</p>'
'<h3>Money</h3>'
'<p>The money objection is almost never about absolute affordability. It is about perceived ROI. The prospect is not sure the outcome is worth the investment. The handle is to bring them back to the impact calculation from discovery: "You mentioned the problem is costing you around 12k per month in lost deals. If we solve that, the investment pays for itself in the first month. What part of that maths does not add up for you?" Defending the price in isolation never works. Reconnecting the price to the problem always does.</p>'
'<h3>Trust</h3>'
'<p>Trust objections are solved with evidence, not reassurance. The prospect is not sure you can do what you say. Telling them you can makes it worse. Showing them a result from a client in their exact situation makes it better. The case study needs to match: same type of agency, same type of problem, specific outcomes. A generic case study says you do good work. A specific one says you have already solved this.</p>'
'<h3>Urgency</h3>'
'<p>Urgency objections mean the prospect does not feel enough pain to act now. The only thing that creates urgency is a vivid projection of what staying where they are costs over time. "If your close rate stays at 12 percent for the next six months and your lead volume stays flat, what does that mean for your revenue targets?" Let them calculate the cost of inaction themselves. It lands harder than you telling them.</p>'
'<h3>Authority</h3>'
'<p>Authority objections mean someone who can say yes is not in the room. The handle is not to wait for a callback. It is to offer to present directly to the other decision maker: "What would they want to know? Let me answer those questions with you now so you are not trying to relay a conversation secondhand." A prospect who agrees to that call is genuinely invested. One who declines is probably not close to a decision regardless.</p>'
)

ART10 = inner_page(
    'The Four Real Objections and How to Handle Each | Kryson Limited',
    'Every objection is Trust, Money, Urgency, or Authority. The surface language changes. The handle for each is completely different.',
    'insight-10.html', '',
    'Insight 10',
    'The four real objections and how to handle each',
    'Sales Process &middot; 28 Feb 2026',
    art_body(ART10_SVG, ART10_CONTENT),
    "initP('ctaC',15);"
)
with open('insight-10.html','w') as f: f.write(ART10)
print("insight-10.html: {:,}".format(len(ART10)))

# ---- ARTICLE 11: Why close rates collapse when founders hire closers ----
ART11_SVG = (
'<svg viewBox="0 0 760 290" xmlns="http://www.w3.org/2000/svg" style="background:#111;border-radius:6px">'
'<text x="380" y="26" text-anchor="middle" fill="rgba(255,255,255,0.25)" font-size="10" font-family="sans-serif" letter-spacing="3">WHY THE FIRST CLOSER FAILS: WHAT WAS MISSING</text>'
'<rect x="30" y="44" width="700" height="38" rx="3" fill="rgba(255,255,255,0.04)"/>'
'<text x="380" y="68" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="12" font-family="sans-serif">Founder hires closer. Closer starts. Close rate drops. Closer is blamed. Closer is replaced.</text>'
'<rect x="30" y="96" width="155" height="128" rx="4" fill="rgba(255,80,80,0.05)" stroke="rgba(255,80,80,0.2)" stroke-width="1"/>'
'<text x="107" y="122" text-anchor="middle" fill="rgba(255,100,100,0.75)" font-size="11" font-family="sans-serif" font-weight="700">NO QUAL GATE</text>'
'<text x="107" y="144" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="10" font-family="sans-serif">Closer gets</text>'
'<text x="107" y="160" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="10" font-family="sans-serif">unqualified leads</text>'
'<text x="107" y="192" text-anchor="middle" fill="rgba(255,100,100,0.5)" font-size="10" font-family="sans-serif">Close rate tanks</text>'
'<text x="107" y="208" text-anchor="middle" fill="rgba(255,100,100,0.5)" font-size="10" font-family="sans-serif">before call starts</text>'
'<rect x="200" y="96" width="155" height="128" rx="4" fill="rgba(255,80,80,0.05)" stroke="rgba(255,80,80,0.2)" stroke-width="1"/>'
'<text x="277" y="122" text-anchor="middle" fill="rgba(255,100,100,0.75)" font-size="11" font-family="sans-serif" font-weight="700">NO FRAMEWORK</text>'
'<text x="277" y="144" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="10" font-family="sans-serif">Founder never</text>'
'<text x="277" y="160" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="10" font-family="sans-serif">wrote it down</text>'
'<text x="277" y="192" text-anchor="middle" fill="rgba(255,100,100,0.5)" font-size="10" font-family="sans-serif">Closer improvises</text>'
'<text x="277" y="208" text-anchor="middle" fill="rgba(255,100,100,0.5)" font-size="10" font-family="sans-serif">with no baseline</text>'
'<rect x="370" y="96" width="155" height="128" rx="4" fill="rgba(255,80,80,0.05)" stroke="rgba(255,80,80,0.2)" stroke-width="1"/>'
'<text x="447" y="122" text-anchor="middle" fill="rgba(255,100,100,0.75)" font-size="11" font-family="sans-serif" font-weight="700">NO CRM SYSTEM</text>'
'<text x="447" y="144" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="10" font-family="sans-serif">Follow-up falls</text>'
'<text x="447" y="160" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="10" font-family="sans-serif">on whoever remembers</text>'
'<text x="447" y="192" text-anchor="middle" fill="rgba(255,100,100,0.5)" font-size="10" font-family="sans-serif">Pipeline invisible</text>'
'<text x="447" y="208" text-anchor="middle" fill="rgba(255,100,100,0.5)" font-size="10" font-family="sans-serif">to the founder</text>'
'<rect x="540" y="96" width="190" height="128" rx="4" fill="rgba(201,168,76,0.1)" stroke="#c9a84c" stroke-width="1.5"/>'
'<text x="635" y="122" text-anchor="middle" fill="#c9a84c" font-size="11" font-family="sans-serif" font-weight="700">THE FIX</text>'
'<text x="635" y="144" text-anchor="middle" fill="rgba(255,255,255,0.7)" font-size="10" font-family="sans-serif">Qual gate + framework</text>'
'<text x="635" y="162" text-anchor="middle" fill="rgba(255,255,255,0.7)" font-size="10" font-family="sans-serif">CRM + cadence</text>'
'<text x="635" y="178" text-anchor="middle" fill="rgba(255,255,255,0.7)" font-size="10" font-family="sans-serif">BEFORE the hire</text>'
'<text x="635" y="200" text-anchor="middle" fill="#c9a84c" font-size="10" font-family="sans-serif">Hire into a system</text>'
'<text x="635" y="216" text-anchor="middle" fill="#c9a84c" font-size="10" font-family="sans-serif">not into guesswork</text>'
'<text x="380" y="258" text-anchor="middle" fill="rgba(255,255,255,0.45)" font-size="12" font-family="sans-serif">TeamCTC: 21% to 38% close rate after system install + closer hired</text>'
'<text x="380" y="278" text-anchor="middle" fill="rgba(255,255,255,0.18)" font-size="11" font-family="sans-serif" font-style="italic">The closer was not the problem. The missing infrastructure was.</text>'
'</svg>'
)

ART11_CONTENT = (
'<div class="art-stat-pull"><div class="asp-num">50%</div><div class="asp-label">Typical close rate of a first closer relative to the founder. Not because closers are bad. Because the system was never built before they arrived.</div></div>'
'<p>The pattern is common enough that it has become predictable. Agency founder builds the business on the strength of their own selling. Revenue plateaus. They hire a closer. The closer underperforms. The closer is replaced. The founder concludes that closers do not work for agencies like theirs.</p>'
'<p>The failure is almost never the closer. It is the three things that were not in place before the closer arrived.</p>'
'<h3>No qualification gate</h3>'
'<p>When the founder is selling, they are unconsciously qualifying throughout the conversation. They know within the first few minutes whether a prospect is serious. They steer accordingly. A closer who has never been given a qualification framework takes every call that was booked. Some of those calls should never have been calls. The closer&#39;s close rate reflects that mix. The founder sees a low number and concludes the closer is not good enough. The closer was given bad material to work with.</p>'
'<h3>No documented framework</h3>'
'<p>The founder&#39;s discovery and close process exists in their head. They have never written it down because they have never needed to. When a closer arrives and asks how the calls work, the founder says something like "just be yourself and follow their lead." That is not a framework. A closer who cannot articulate what the process is in the first week cannot improve on it in the fourth month.</p>'
'<h3>No CRM architecture</h3>'
'<p>When the founder is selling, they remember everything. Which deals need follow-up. Which prospects went quiet. Which calls are scheduled for next week. When a closer is running the pipeline, none of that institutional memory transfers. Without a CRM with clear stage definitions, required next actions, and a review cadence, the pipeline is invisible to everyone including the founder. Deals fall out of the process silently.</p>'
'<h3>The right sequence</h3>'
'<p>Install the qualification gate, document the framework, and set up the CRM architecture before hiring the closer. Then the closer has something to operate within. TeamCTC went from a 21 percent close rate to 38 percent and from &pound;8k to &pound;61k per month. The closer was part of that. The system was the precondition for the closer working.</p>'
)

ART11 = inner_page(
    'Why Close Rates Collapse When Founders Hire Closers | Kryson Limited',
    'The failure is almost never the closer. It is the three things that were missing before they arrived. Qualification, framework, and CRM architecture.',
    'insight-11.html', '',
    'Insight 11',
    'Why close rates collapse when founders hire closers',
    'Revenue Architecture &middot; 15 Apr 2026',
    art_body(ART11_SVG, ART11_CONTENT),
    "initP('ctaC',15);"
)
with open('insight-11.html','w') as f: f.write(ART11)
print("insight-11.html: {:,}".format(len(ART11)))

# ---- ARTICLE 12: Revenue OS ----
ART12_SVG = (
'<svg viewBox="0 0 760 310" xmlns="http://www.w3.org/2000/svg" style="background:#111;border-radius:6px">'
'<text x="380" y="28" text-anchor="middle" fill="rgba(255,255,255,0.25)" font-size="10" font-family="sans-serif" letter-spacing="3">REVENUE OPERATING SYSTEM: THE SIX COMPONENTS</text>'
'<rect x="30" y="48" width="210" height="80" rx="4" fill="rgba(201,168,76,0.06)" stroke="rgba(201,168,76,0.2)" stroke-width="1"/>'
'<text x="135" y="74" text-anchor="middle" fill="#c9a84c" font-size="11" font-family="sans-serif" font-weight="600" letter-spacing="1">QUALIFICATION</text>'
'<text x="135" y="94" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="11" font-family="sans-serif">Gate anyone can</text>'
'<text x="135" y="110" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="11" font-family="sans-serif">run consistently</text>'
'<rect x="275" y="48" width="210" height="80" rx="4" fill="rgba(201,168,76,0.08)" stroke="rgba(201,168,76,0.25)" stroke-width="1"/>'
'<text x="380" y="74" text-anchor="middle" fill="#c9a84c" font-size="11" font-family="sans-serif" font-weight="600" letter-spacing="1">CRM ARCHITECTURE</text>'
'<text x="380" y="94" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="11" font-family="sans-serif">Stages with real criteria</text>'
'<text x="380" y="110" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="11" font-family="sans-serif">Next actions required</text>'
'<rect x="520" y="48" width="210" height="80" rx="4" fill="rgba(201,168,76,0.1)" stroke="rgba(201,168,76,0.3)" stroke-width="1"/>'
'<text x="625" y="74" text-anchor="middle" fill="#c9a84c" font-size="11" font-family="sans-serif" font-weight="600" letter-spacing="1">DISCOVERY PROCESS</text>'
'<text x="625" y="94" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="11" font-family="sans-serif">Documented and</text>'
'<text x="625" y="110" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="11" font-family="sans-serif">repeatable</text>'
'<line x1="135" y1="128" x2="135" y2="148" stroke="rgba(201,168,76,0.2)" stroke-width="1"/>'
'<line x1="380" y1="128" x2="380" y2="148" stroke="rgba(201,168,76,0.2)" stroke-width="1"/>'
'<line x1="625" y1="128" x2="625" y2="148" stroke="rgba(201,168,76,0.2)" stroke-width="1"/>'
'<rect x="30" y="148" width="210" height="80" rx="4" fill="rgba(201,168,76,0.12)" stroke="rgba(201,168,76,0.35)" stroke-width="1"/>'
'<text x="135" y="174" text-anchor="middle" fill="#c9a84c" font-size="11" font-family="sans-serif" font-weight="600" letter-spacing="1">CLOSE CALL SYSTEM</text>'
'<text x="135" y="194" text-anchor="middle" fill="rgba(255,255,255,0.55)" font-size="11" font-family="sans-serif">Framework anyone</text>'
'<text x="135" y="210" text-anchor="middle" fill="rgba(255,255,255,0.55)" font-size="11" font-family="sans-serif">can follow and improve</text>'
'<rect x="275" y="148" width="210" height="80" rx="4" fill="rgba(201,168,76,0.15)" stroke="rgba(201,168,76,0.4)" stroke-width="1.5"/>'
'<text x="380" y="174" text-anchor="middle" fill="#c9a84c" font-size="11" font-family="sans-serif" font-weight="600" letter-spacing="1">FOLLOW-UP CADENCE</text>'
'<text x="380" y="194" text-anchor="middle" fill="rgba(255,255,255,0.65)" font-size="11" font-family="sans-serif">Runs on schedule</text>'
'<text x="380" y="210" text-anchor="middle" fill="rgba(255,255,255,0.65)" font-size="11" font-family="sans-serif">without reminders</text>'
'<rect x="520" y="148" width="210" height="80" rx="4" fill="rgba(201,168,76,0.18)" stroke="#c9a84c" stroke-width="2"/>'
'<text x="625" y="174" text-anchor="middle" fill="#c9a84c" font-size="11" font-family="sans-serif" font-weight="600" letter-spacing="1">WEEKLY REVIEW</text>'
'<text x="625" y="194" text-anchor="middle" fill="rgba(255,255,255,0.75)" font-size="11" font-family="sans-serif">Pipeline, conversion,</text>'
'<text x="625" y="210" text-anchor="middle" fill="rgba(255,255,255,0.75)" font-size="11" font-family="sans-serif">call debrief every Monday</text>'
'<text x="380" y="266" text-anchor="middle" fill="rgba(201,168,76,0.6)" font-size="13" font-family="sans-serif" font-style="italic" font-weight="600">All six components working together = a business that runs without the founder in every deal</text>'
'<text x="380" y="294" text-anchor="middle" fill="rgba(255,255,255,0.18)" font-size="11" font-family="sans-serif" font-style="italic">Most agencies never build this. They are always too busy selling to document how they sell.</text>'
'</svg>'
)

ART12_CONTENT = (
'<p>Most agency founders cannot take a two-week holiday without the pipeline suffering. That is not a time management problem. It is a structural one. Revenue is dependent on the founder\'s presence because the commercial system only exists inside the founder\'s head.</p>'
'<h3>What a revenue operating system contains</h3>'
'<p>A revenue operating system is the set of processes, tools, and rhythms that mean sales activity continues and pipeline moves regardless of who is in which meeting. It includes a qualification framework that anyone can follow, a CRM architecture that surfaces the right actions at the right time, a discovery process that is documented and repeatable, a close call structure that a second person can follow, a follow-up cadence that runs on schedule, and a weekly review process that keeps the whole thing moving.</p>'
'<div class="art-stat-pull"><div class="asp-num">100%</div><div class="asp-label">Kryson system retention rate. Every revenue operating system we have built is still running in the client\'s business.</div></div>'
'<h3>Why most agencies never build it</h3>'
'<p>None of those components are complicated in isolation. The difficulty is that building them requires the founder to temporarily slow down and extract what they know, which feels counterproductive when there are active deals in the pipeline. This is why most agencies never build the system. They are always too busy selling to document how they sell.</p>'
'<h3>The forcing function</h3>'
'<p>The forcing function is to treat the documentation as a parallel activity rather than a replacement. Run your next five discovery calls and record them. Review the recordings and note what questions you asked, what answers moved the conversation forward, and where you handled an objection well. That is the beginning of your framework. It is not a separate project. It is a by-product of the work you are already doing.</p>'
'<p>The North Star Solutions engagement is the clearest example of what this produces. Before we started, the founder had no visibility into sales metrics or channel profitability. Reps were self-reporting deal status. Forecasting was guesswork. In 90 days we installed eight pipeline stages with objective criteria, a pain-based discovery framework, an 8-touch follow-up sequence, a weekly review cadence, and a rep scorecard. Revenue went from $12,500 to $96,000 per month. The system is still running.</p>'
'<h3>What independence looks like</h3>'
'<p>An agency with a documented revenue operating system can onboard a salesperson into a system, delegate follow-up with confidence, forecast revenue with accuracy, and take a holiday without checking the CRM every morning. That is not a luxury. That is what a functional commercial infrastructure looks like.</p>'
)

ART12 = inner_page(
    'Building a Revenue Operating System That Runs Without You | Kryson Limited',
    'The six components of a revenue operating system that runs without the founder. Why most agencies never build it and how to start.',
    'insight-12.html', '',
    'Insight 12',
    'Building a revenue operating system that runs without you',
    'Revenue Architecture &middot; 2 Jun 2026',
    art_body(ART12_SVG, ART12_CONTENT),
    "initP('ctaC',15);"
)
with open('insight-12.html','w') as f: f.write(ART12)
print("insight-12.html: {:,}".format(len(ART12)))

print("\nAll pages rebuilt cleanly.")
