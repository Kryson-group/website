import os

NAV = '''<nav id="nav">
<a href="index.html" class="logo">
<svg viewBox="0 0 520 120" xmlns="http://www.w3.org/2000/svg"><text x="0" y="95" font-family="'Times New Roman','CG Times',Times,serif" font-size="120" fill="#FFF" letter-spacing="2">K</text><line x1="62" y1="30" x2="78" y2="10" stroke="#FFF" stroke-width="3.5" stroke-linecap="round"/><polygon points="78,2 85,12 76,14" fill="#FFF"/><text x="82" y="95" font-family="'Times New Roman','CG Times',Times,serif" font-size="76" fill="#FFF" letter-spacing="16">RYSON</text></svg>
</a>
<div class="nr">
<a href="services.html" class="na">What We Do</a>
<a href="results.html" class="na">Results</a>
<a href="about.html" class="na">About</a>
<a href="faq.html" class="na">FAQ</a>
<a href="" onclick="Calendly.initPopupWidget({url:'https://calendly.com/kyle-krysongroup/introduction?background_color=000000&amp;text_color=ffffff&amp;primary_color=c9a84c'});return false;"><button class="nb">Book an Audit</button></a>
</div>
<button class="burger" id="burg"><span></span><span></span><span></span></button>
</nav>
<div class="mob" id="mob">
<button class="mob-x" id="mobX">&times;</button>
<a href="services.html" class="ml">What We Do</a>
<a href="results.html" class="ml">Results</a>
<a href="about.html" class="ml">About</a>
<a href="about.html#careers" class="ml">Careers</a>
<a href="faq.html" class="ml">FAQ</a>
<a href="" onclick="Calendly.initPopupWidget({url:'https://calendly.com/kyle-krysongroup/introduction?background_color=000000&amp;text_color=ffffff&amp;primary_color=c9a84c'});return false;" class="ml" style="color:var(--gold)">Book an Audit</a>
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

BOOKING_MODAL = ''

CALENDLY_BADGE = '''<script src="https://assets.calendly.com/assets/external/widget.js" type="text/javascript" async></script>
<script type="text/javascript">window.onload=function(){if(typeof Calendly!=='undefined'){Calendly.initBadgeWidget({url:'https://calendly.com/kyle-krysongroup/introduction?background_color=000000&text_color=ffffff&primary_color=c9a84c',text:'Schedule time with me',color:'#c9a84c',textColor:'#ffffff',branding:true});}}</script>'''

CDN = '''<link href="https://assets.calendly.com/assets/external/widget.css" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>'''

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
const burg=document.getElementById('burg'),mob=document.getElementById('mob'),mobX=document.getElementById('mobX');
burg.addEventListener('click',()=>{mob.classList.add('open');document.body.style.overflow='hidden'});
mobX.addEventListener('click',()=>{mob.classList.remove('open');document.body.style.overflow=''});
document.querySelectorAll('.ml').forEach(l=>{l.addEventListener('click',()=>{mob.classList.remove('open');document.body.style.overflow=''})});
document.querySelectorAll('a[href^="#"]').forEach(a=>{
  a.addEventListener('click',function(e){const href=this.getAttribute('href');if(href==='#')return;e.preventDefault();const t=document.querySelector(href);if(t)window.scrollTo({top:t.getBoundingClientRect().top+window.pageYOffset-64,behavior:'smooth'})});
});
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
<a href="" onclick="Calendly.initPopupWidget({url:'https://calendly.com/kyle-krysongroup/introduction?background_color=000000&amp;text_color=ffffff&amp;primary_color=c9a84c'});return false;"><button class="btn bp" style="font-size:13px;padding:16px 40px">Book Your Revenue Audit</button></a>
<p class="cta-note">No commitment required. Founder to founder.</p>
</div>
</section>'''

def inner_page(title, desc, canonical, schema, hero_label, hero_h1, hero_sub, body, extra_js=''):
    nav_js = "gsap.to('#nav',{opacity:1,y:0,duration:.5,ease:'power2.out'});"
    return (
        head(title, desc, canonical, schema) +
        '\n<body>\n' + NAV +
        '\n<section class="ph" style="background:var(--bg2);padding:clamp(120px,14vw,180px) clamp(48px,7vw,120px) clamp(64px,8vw,100px);position:relative;overflow:hidden">'
        '\n<div class="hero-glow" style="opacity:.5"></div>'
        '\n<div class="sl">' + hero_label + '</div>'
        '\n<h1 class="sh" style="max-width:800px;font-size:clamp(32px,5vw,72px)">' + hero_h1 + '</h1>'
        '\n<p class="sp" style="max-width:560px">' + hero_sub + '</p>'
        '\n</section>\n<div class="glow-div"></div>\n' +
        body +
        cta_section() + '\n' + KG_BAND + '\n' + FOOTER +
        '\n<script>\n' + nav_js + '\n' + SHARED_JS + '\n' + extra_js + '\n</script>\n' +
        CALENDLY_BADGE + '\n</body></html>'
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
<p class="hs">You have leads, calls, and proposals going out. Revenue still feels like guesswork. The problem is never the top of the funnel. It is the system underneath it.</p>
<div class="hb">
<a href="" onclick="Calendly.initPopupWidget({url:'https://calendly.com/kyle-krysongroup/introduction?background_color=000000&amp;text_color=ffffff&amp;primary_color=c9a84c'});return false;"><button class="btn bp" style="font-size:13px;padding:16px 36px;letter-spacing:2.5px">Book a Revenue Audit</button></a>
<a href="results.html"><button class="btn bs" style="font-size:11px;padding:12px 24px">See Client Results</button></a>
</div>
</div>
</div>
<div class="stats">
<div class="st"><div class="st-n"><span class="ctr" data-to="3.2" data-pre="&pound;" data-suf="M+">£0</span></div><div class="st-l">Additional Revenue Generated</div></div>
<div class="st"><div class="st-n">2x to 3x</div><div class="st-l">Conversion Rate Uplift</div></div>
<div class="st"><div class="st-n">60 to 90 Days</div><div class="st-l">From Audit to Measurable Results</div></div>
</div>
</section>
<section id="problem" class="sec" style="background:var(--bg2)">
<div class="sl">The Real Problem</div>
<h2 class="prob-intro rv" style="font-size:clamp(22px,3.5vw,48px);line-height:1.25;margin-bottom:clamp(48px,6vw,80px);font-weight:400;color:var(--w95)">You do not need more leads.<br>You need to <em>stop losing the ones you already have.</em></h2>
<div class="prob-grid-2">
<div class="prob-card rv"><div class="prob-num">01</div><h3>You are the entire sales department.</h3><p>Every discovery call, every proposal, every follow-up runs through you. When you deliver, you stop selling. Revenue swings because the whole thing depends on your calendar.</p></div>
<div class="prob-card rv"><div class="prob-num">02</div><h3>Prospects go quiet and you have no idea why.</h3><p>You send a proposal. Silence. Three out of five proposals go cold &mdash; not because your service is wrong, but because there is no system catching them.</p></div>
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
<div class="wwd-card rv"><div class="wwd-card-head"><div class="wwd-num">Phase 02</div><h3>Conversion System Rebuild</h3></div><p>We rebuild everything between the first conversation and the signed contract. One working deliverable per week.</p><ul class="wwd-delivers"><li>Qualification criteria and discovery framework</li><li>Proposal structure and follow-up sequences</li><li>CRM architecture rebuilt from scratch</li></ul></div>
<div class="wwd-card rv"><div class="wwd-card-head"><div class="wwd-num">Phase 03</div><h3>Revenue Operating System</h3></div><p>We install the structure that keeps the system running and improving week after week.</p><ul class="wwd-delivers"><li>KPI dashboards and conversion tracking</li><li>Weekly pipeline and call review cadences</li><li>Team trained to run it independently</li></ul></div>
<div class="wwd-card rv"><div class="wwd-card-head"><div class="wwd-num">Phase 04</div><h3>Scale</h3></div><p>Once the system is proven, we build the team to run it at scale &mdash; so the founder steps back from every deal.</p><ul class="wwd-delivers"><li>Role design and hiring criteria</li><li>Scripts, objection libraries, call frameworks</li><li>Team running proven system independently</li></ul></div>
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
    '\n<body>\n' + LOADER + '\n' + NAV + '\n' + INDEX_BODY +
    cta_section() + '\n' + KG_BAND + '\n' + FOOTER +
    '\n<script>\n' + LOADER_JS + '\n' + SHARED_JS + "\ninitP('pC',30);initP('ctaC',15);\n</script>\n" +
    CALENDLY_BADGE + '\n</body></html>'
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
<div class="case-cta"><a href="" onclick="Calendly.initPopupWidget({url:'https://calendly.com/kyle-krysongroup/introduction?background_color=000000&amp;text_color=ffffff&amp;primary_color=c9a84c'});return false;"><button class="btn bp" style="font-size:11px;padding:12px 24px">Book Your Revenue Audit</button></a></div>
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
<div><h5>The Situation</h5><p>Strong inbound lead flow but only a 21% close rate. The founder pitched immediately after a short intro call with no structured discovery. Proposals were generic PDFs with no follow-up system behind them. When a prospect went quiet, the founder assumed they were not interested and moved on.</p></div>
<div><h5>What We Installed</h5><ul>
<li>Pain-based discovery framework with 12 core questions covering urgency, budget, current situation, and decision process</li>
<li>Engagement-tracked proposal system that was value-led, referenced specific pain points, and had a clear next step built in</li>
<li>Structured closing cadence with defined touchpoints and escalation triggers</li>
<li>7-touch post-proposal follow-up sequence with specific messaging for each stage</li>
<li>CRM rebuild with six pipeline stages and mandatory next-action fields</li>
<li>Weekly pipeline review and close rate tracking from Week 1</li>
</ul></div>
</div>
<div class="case-quote"><p>'I was generating the leads. I just could not close them consistently. Kryson showed me exactly where I was losing deals and gave me the tools to fix it. Close rate went from 21% to 38% and the revenue followed.'</p></div>
<div class="case-cta"><a href="" onclick="Calendly.initPopupWidget({url:'https://calendly.com/kyle-krysongroup/introduction?background_color=000000&amp;text_color=ffffff&amp;primary_color=c9a84c'});return false;"><button class="btn bp" style="font-size:11px;padding:12px 24px">Book Your Revenue Audit</button></a></div>
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
<li>Structured proposal-to-close process with commitment gates at every stage</li>
<li>Weekly pipeline review, call review, and conversion review cadences</li>
<li>Lost deal tracking system to identify recurring patterns and feed learnings back into the process</li>
</ul></div>
</div>
<div class="case-quote"><p>'We had no idea what was working and what was not. Kryson gave us the visibility to actually manage the business instead of just hoping. The revenue nearly doubled before we changed anything about our service.'</p></div>
<div class="case-cta"><a href="" onclick="Calendly.initPopupWidget({url:'https://calendly.com/kyle-krysongroup/introduction?background_color=000000&amp;text_color=ffffff&amp;primary_color=c9a84c'});return false;"><button class="btn bp" style="font-size:11px;padding:12px 24px">Book Your Revenue Audit</button></a></div>
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
<div><h5>The Situation</h5><p>A two-partner consulting firm generating most revenue through referrals. When referrals slowed, they had no outbound motion and no way to convert inbound enquiries that did come in. Proposals took over a week to send. The average deal cycle was 47 days because neither partner followed a structured process.</p></div>
<div><h5>What We Installed</h5><ul>
<li>Inbound response system with a 4-hour speed-to-lead target and automated booking flow</li>
<li>Structured discovery call framework tailored to their consulting services and ICP</li>
<li>Proposal template system that cut turnaround from 8 days to 48 hours</li>
<li>5-touch follow-up cadence with value-add content at each stage</li>
<li>CRM implementation from scratch with pipeline visibility for both partners</li>
<li>Fortnightly deal review replacing ad-hoc conversations about pipeline</li>
</ul></div>
</div>
<div class="case-quote"><p>'We went from hoping the phone would ring to actually controlling our revenue. The proposal system alone was a game changer. We stopped losing deals to slow follow-up overnight.'</p></div>
<div class="case-cta"><a href="" onclick="Calendly.initPopupWidget({url:'https://calendly.com/kyle-krysongroup/introduction?background_color=000000&amp;text_color=ffffff&amp;primary_color=c9a84c'});return false;"><button class="btn bp" style="font-size:11px;padding:12px 24px">Book Your Revenue Audit</button></a></div>
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
<div class="case-cta"><a href="" onclick="Calendly.initPopupWidget({url:'https://calendly.com/kyle-krysongroup/introduction?background_color=000000&amp;text_color=ffffff&amp;primary_color=c9a84c'});return false;"><button class="btn bp" style="font-size:11px;padding:12px 24px">Book Your Revenue Audit</button></a></div>
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
<div><h5>The Situation</h5><p>A founder-led creative agency that had grown to &pound;14K/mo through word of mouth but had no sales process at all. Every deal was different. The founder quoted based on gut feel, gave discounts when pushed, and had no follow-up system. Three out of every five proposals went cold with no response.</p></div>
<div><h5>What We Installed</h5><ul>
<li>Standardised discovery framework replacing the founder's unstructured chemistry calls</li>
<li>Tiered pricing structure with three packages, removing the guesswork from quoting</li>
<li>Proposal system with built-in urgency triggers and a 72-hour expiry on pricing</li>
<li>Objection pre-handling built directly into the discovery and proposal stages</li>
<li>Lost deal debrief process to capture why deals did not close and feed learnings back in</li>
<li>Commission-only setter brought in at Week 6 to handle initial qualification and booking</li>
</ul></div>
</div>
<div class="case-quote"><p>'I did not even realise I had a sales problem. I thought I just needed more leads. Turns out I was losing half the deals I already had because I had no system. The structure Kryson put in changed everything.'</p></div>
<div class="case-cta"><a href="" onclick="Calendly.initPopupWidget({url:'https://calendly.com/kyle-krysongroup/introduction?background_color=000000&amp;text_color=ffffff&amp;primary_color=c9a84c'});return false;"><button class="btn bp" style="font-size:11px;padding:12px 24px">Book Your Revenue Audit</button></a></div>
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
<div style="font-size:11px;color:var(--w20);letter-spacing:.5px;margin-bottom:20px;font-style:italic">Based on published B2B agency conversion benchmarks &mdash; not Kryson internal data</div>
<div class="funnel-row"><span class="funnel-label">100 Conversations</span><div class="funnel-track"><div class="funnel-fill" data-width="100"></div></div><span class="funnel-pct">100%</span></div>
<div class="funnel-row"><span class="funnel-label">65 Discovery Calls</span><div class="funnel-track"><div class="funnel-fill" data-width="65"></div></div><span class="funnel-pct">65%</span></div>
<div class="funnel-row"><span class="funnel-label">32 Proposals Sent</span><div class="funnel-track"><div class="funnel-fill" data-width="32"></div></div><span class="funnel-pct">32%</span></div>
<div class="funnel-row"><span class="funnel-label">7 Clients Closed</span><div class="funnel-track"><div class="funnel-fill" data-width="7"></div></div><span class="funnel-pct" style="color:rgba(201,168,76,1)">7%</span></div>
<div class="funnel-note">The average agency closes 7% of the conversations it starts. Our clients typically 2x to 3x their conversion rate &mdash; regardless of where they start.</div>
</div>
<div class="prob-grid-2" style="margin-top:clamp(32px,4vw,56px)">
<div class="prob-card rv"><div class="prob-num">01</div><h3>You are the entire sales department.</h3><p>Every discovery call, every proposal, every follow-up runs through you. When you deliver, you stop selling.</p></div>
<div class="prob-card rv"><div class="prob-num">02</div><h3>Prospects go quiet and you have no idea why.</h3><p>Three out of five proposals go cold. Not because your service is wrong. Because there is no system catching them.</p></div>
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
<div class="wwd-card rv"><div class="wwd-card-head"><div class="wwd-num">Phase 02</div><h3>Conversion System Rebuild</h3></div><p>We rebuild everything between the first conversation and the signed contract. One working deliverable per week, tested on live calls.</p><ul class="wwd-delivers"><li>Qualification criteria and discovery framework</li><li>Proposal structure and follow-up sequences</li><li>Objection handling and closing process</li><li>CRM architecture rebuilt from scratch</li></ul></div>
<div class="wwd-card rv"><div class="wwd-card-head"><div class="wwd-num">Phase 03</div><h3>Revenue Operating System</h3></div><p>We install the structure that keeps it running and improving week after week.</p><ul class="wwd-delivers"><li>KPI dashboards and conversion tracking</li><li>Weekly pipeline and call review cadences</li><li>Deal ownership by stage</li><li>Team training to run it independently</li></ul></div>
<div class="wwd-card rv"><div class="wwd-card-head"><div class="wwd-num">Phase 04</div><h3>Scale</h3></div><p>Once the system is proven, we build the team to run it at scale.</p><ul class="wwd-delivers"><li>Role design and hiring criteria</li><li>Scripts, objection libraries, and call frameworks</li><li>Onboarding and performance standards</li><li>Team running proven system independently</li></ul></div>
</div>
<div style="text-align:center;margin-top:clamp(32px,4vw,56px)"><a href="" onclick="Calendly.initPopupWidget({url:'https://calendly.com/kyle-krysongroup/introduction?background_color=000000&amp;text_color=ffffff&amp;primary_color=c9a84c'});return false;"><button class="btn bp" style="font-size:11px;padding:12px 28px">Book a Revenue Audit</button></a></div>
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
<div class="ph-del"><div class="ph-del-num">02</div><div class="ph-del-content"><div class="ph-del-title">Rebuilt Sales System</div><p>New scripts, frameworks, proposal structure, follow-up cadences, CRM architecture — built and tested on live conversations.</p></div></div>
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
<div style="text-align:center;margin-top:clamp(32px,4vw,56px)"><a href="" onclick="Calendly.initPopupWidget({url:'https://calendly.com/kyle-krysongroup/introduction?background_color=000000&amp;text_color=ffffff&amp;primary_color=c9a84c'});return false;"><button class="btn bp" style="font-size:11px;padding:12px 28px">Book a Revenue Audit</button></a></div>
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
<div style="text-align:center"><a href="" onclick="Calendly.initPopupWidget({url:'https://calendly.com/kyle-krysongroup/introduction?background_color=000000&amp;text_color=ffffff&amp;primary_color=c9a84c'});return false;"><button class="btn bp" style="font-size:11px">Book a Revenue Audit</button></a></div>
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
<div class="fq rv"><button class="fq-q">What is the difference between Kryson and a sales coach?</button><div class="fq-a"><div class="fq-a-in">A sales coach gives you advice. We build the system. By the end of an engagement you have a working CRM architecture, qualification criteria, discovery frameworks, proposal templates, follow-up sequences, and an operating cadence &mdash; not notes from a workshop.</div></div></div>
<div class="fq rv"><button class="fq-q">What results can I expect?</button><div class="fq-a"><div class="fq-a-in">Across our client base, the typical outcome is a 2x to 3x conversion rate improvement within 60 to 90 days of system installation. Our highest recorded multiple is 6.68x revenue growth in 90 days. Results depend on starting point, industry, and how broken the existing process is. The Revenue Leak Audit in Week 1 will give you a realistic picture of what is achievable in your specific situation.</div></div></div>
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

print("\nAll pages rebuilt cleanly.")
