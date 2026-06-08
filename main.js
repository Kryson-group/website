// Cursor

// Loader
const lt=document.getElementById('lt'),lb=document.getElementById('lb'),ld=document.getElementById('loader');
'KRYSON LIMITED'.split('').forEach(c=>{const s=document.createElement('span');s.textContent=c===' '?'\u00A0\u00A0':c;lt.appendChild(s)});
document.body.style.overflow='hidden';
setTimeout(()=>{lt.querySelectorAll('span').forEach((s,i)=>{setTimeout(()=>{s.style.transition='opacity .35s ease,transform .35s ease';s.style.opacity='1';s.style.transform='translateY(0)'},i*50)})},300);
setTimeout(()=>lb.style.width='100px',1200);
setTimeout(()=>{ld.classList.add('exit');setTimeout(()=>{ld.style.display='none';initSite()},1000)},3000);

function initSite(){
document.body.style.overflow='';
gsap.to('#nav',{opacity:1,y:0,duration:.5,ease:'power2.out'});
gsap.to('.ho',{opacity:1,duration:.4,delay:.15});
document.querySelectorAll('.hh .ln span').forEach((s,i)=>{gsap.to(s,{y:0,duration:.6,delay:.3+i*.12,ease:'power3.out'})});
gsap.to('.hs',{opacity:1,duration:.4,delay:.9});
gsap.to('.hb',{opacity:1,duration:.4,delay:1.05});
document.querySelectorAll('.st').forEach((s,i)=>{gsap.to(s,{opacity:1,y:0,duration:.4,delay:1.2+i*.08,ease:'power2.out'})});
}

// Three.js particles — pre-allocated buffers, no per-frame allocation
function initP(id,n){
const cv=document.getElementById(id);if(!cv)return;
const pa=cv.parentElement;
const scene=new THREE.Scene();
const cam=new THREE.PerspectiveCamera(75,pa.clientWidth/pa.clientHeight,.1,1000);
const r=new THREE.WebGLRenderer({canvas:cv,alpha:true,antialias:false});
r.setSize(pa.clientWidth,pa.clientHeight);
r.setPixelRatio(1); // force pixel ratio 1 for performance

// Particles
const pos=new Float32Array(n*3);
const vel=[];
for(let i=0;i<n;i++){
  pos[i*3]=(Math.random()-.5)*20;pos[i*3+1]=(Math.random()-.5)*12;pos[i*3+2]=(Math.random()-.5)*8;
  vel.push({vx:(Math.random()-.5)*.0015,vy:(Math.random()-.5)*.0015,vz:0});
}
const ptGeo=new THREE.BufferGeometry();
const ptBuf=new THREE.BufferAttribute(pos,3);ptBuf.setUsage(THREE.DynamicDrawUsage);
ptGeo.setAttribute('position',ptBuf);
scene.add(new THREE.Points(ptGeo,new THREE.PointsMaterial({color:0xC9A84C,size:.035,transparent:true,opacity:.4,blending:THREE.AdditiveBlending,depthWrite:false})));

// Lines — pre-allocate max possible connections
const maxLines=n*(n-1)/2;
const lineBuf=new Float32Array(maxLines*6);
const lineGeo=new THREE.BufferGeometry();
const lineAttr=new THREE.BufferAttribute(lineBuf,3);lineAttr.setUsage(THREE.DynamicDrawUsage);
lineGeo.setAttribute('position',lineAttr);
lineGeo.setDrawRange(0,0);
scene.add(new THREE.LineSegments(lineGeo,new THREE.LineBasicMaterial({color:0xC9A84C,transparent:true,opacity:.04,blending:THREE.AdditiveBlending,depthWrite:false})));

cam.position.z=6;
let visible=true;
const obs=new IntersectionObserver(e=>{visible=e[0].isIntersecting},{threshold:0});
obs.observe(pa);

let af;
function tick(){
  af=requestAnimationFrame(tick);
  if(!visible)return;
  // move particles
  for(let i=0;i<n;i++){
    pos[i*3]+=vel[i].vx;pos[i*3+1]+=vel[i].vy;
    if(Math.abs(pos[i*3])>10)vel[i].vx*=-1;
    if(Math.abs(pos[i*3+1])>6)vel[i].vy*=-1;
  }
  ptBuf.needsUpdate=true;
  // update lines in place
  let lc=0;
  for(let i=0;i<n;i++)for(let j=i+1;j<n;j++){
    const dx=pos[i*3]-pos[j*3],dy=pos[i*3+1]-pos[j*3+1];
    if(dx*dx+dy*dy<6.25){ // distance < 2.5, avoid sqrt
      const b=lc*6;
      lineBuf[b]=pos[i*3];lineBuf[b+1]=pos[i*3+1];lineBuf[b+2]=pos[i*3+2];
      lineBuf[b+3]=pos[j*3];lineBuf[b+4]=pos[j*3+1];lineBuf[b+5]=pos[j*3+2];
      lc++;
    }
  }
  lineAttr.needsUpdate=true;
  lineGeo.setDrawRange(0,lc*2);
  r.render(scene,cam);
}
tick();
window.addEventListener('resize',()=>{cam.aspect=pa.clientWidth/pa.clientHeight;cam.updateProjectionMatrix();r.setSize(pa.clientWidth,pa.clientHeight)},{passive:true});
}
initP('pC',30);initP('ctaC',15);

// GSAP ScrollTrigger
gsap.registerPlugin(ScrollTrigger);
document.querySelectorAll('.rv').forEach(el=>{gsap.to(el,{scrollTrigger:{trigger:el,start:'top 88%'},opacity:1,y:0,duration:.5,ease:'power2.out'})});

// Timeline
ScrollTrigger.create({trigger:'.tl',start:'top 70%',onEnter:()=>{
document.getElementById('tlF').style.height='100%';
document.querySelectorAll('.ts').forEach((s,i)=>{gsap.to(s,{opacity:1,y:0,duration:.45,delay:.15+i*.12,ease:'power2.out',onComplete:()=>s.classList.add('on')})});
}});

// Counter animation
document.querySelectorAll('.ctr').forEach(c=>{ScrollTrigger.create({trigger:c,start:'top 90%',once:true,onEnter:()=>{const t=parseFloat(c.dataset.to),pre=c.dataset.pre||'',suf=c.dataset.suf||'';const s=performance.now();!function u(now){const p=Math.min((now-s)/1500,1);c.textContent=pre+(t*(1-Math.pow(1-p,3))).toFixed(1)+suf;if(p<1)requestAnimationFrame(u)}(s)}})});

// Funnel bar animation
const fv=document.querySelector('.funnel-vis');
if(fv){ScrollTrigger.create({trigger:fv,start:'top 80%',once:true,onEnter:()=>{document.querySelectorAll('.funnel-fill').forEach((f,i)=>{setTimeout(()=>{f.style.width=f.dataset.width+'%'},i*180)})}})}

// Stats band underline animation
document.querySelectorAll('.sb-item').forEach(s=>{ScrollTrigger.create({trigger:s,start:'top 85%',once:true,onEnter:()=>s.classList.add('vis')})});

// FAQ
document.querySelectorAll('.fq-q').forEach(b=>{b.addEventListener('click',()=>{const f=b.parentElement,a=f.querySelector('.fq-a'),o=f.classList.contains('open');document.querySelectorAll('.fq.open').forEach(x=>{x.classList.remove('open');x.querySelector('.fq-a').style.maxHeight='0'});if(!o){f.classList.add('open');a.style.maxHeight=a.scrollHeight+'px'}})});

// Case toggle
function toggleCase(top){const c=top.parentElement,b=c.querySelector('.case-body'),o=c.classList.contains('open');document.querySelectorAll('.case.open').forEach(x=>{x.classList.remove('open');x.querySelector('.case-body').style.maxHeight='0'});if(!o){c.classList.add('open');b.style.maxHeight=b.scrollHeight+'px'}}

// Mobile
const burg=document.getElementById('burg'),mob=document.getElementById('mob'),mobX=document.getElementById('mobX');
burg.addEventListener('click',()=>{mob.classList.add('open');document.body.style.overflow='hidden'});
mobX.addEventListener('click',()=>{mob.classList.remove('open');document.body.style.overflow=''});
document.querySelectorAll('.ml').forEach(l=>l.addEventListener('click',()=>{mob.classList.remove('open');document.body.style.overflow=''}));

// Smooth scroll (skip booking links — handled separately)
document.querySelectorAll('a[href^="#"]').forEach(a=>{
  if(a.classList.contains('booking-link'))return;
  a.addEventListener('click',function(e){
    const href=this.getAttribute('href');
    if(href==='#')return;
    e.preventDefault();
    const t=document.querySelector(href);
    if(t)window.scrollTo({top:t.getBoundingClientRect().top+window.pageYOffset-64,behavior:'smooth'});
  });
});

// ── BOOKING MODAL ──
const bModal=document.getElementById('bookingModal');
const bmClose=document.getElementById('bmClose');

let bookingLoaded=false;
function openBooking(){
  if(!bookingLoaded){
    bookingLoaded=true;
    const wrap=document.getElementById('bmIframeWrap');
    const ifr=document.createElement('iframe');
    ifr.src='https://api.leadconnectorhq.com/widget/booking/ucM2wiPjxGC5ekOnTM8E';
    ifr.scrolling='no';
    ifr.style.cssText='width:100%;border:none;display:block;min-height:580px';
    wrap.appendChild(ifr);
    const s=document.createElement('script');
    s.src='https://link.msgsndr.com/js/form_embed.js';
    document.body.appendChild(s);
  }
  bModal.classList.add('open');document.body.style.overflow='hidden';
}
function closeBooking(){bModal.classList.remove('open');document.body.style.overflow=''}

bmClose.addEventListener('click',closeBooking);
bModal.addEventListener('click',e=>{if(e.target===bModal)closeBooking()});
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeBooking()});

// Intercept all booking button clicks
document.querySelectorAll('.bp,.nb').forEach(btn=>{
  const a=btn.closest('a');
  if(a){a.addEventListener('click',e=>{e.preventDefault();openBooking()})}
});
// Mobile menu booking link
document.querySelectorAll('.ml').forEach(a=>{
  if(a.textContent.includes('Book')||a.textContent.includes('Audit')){
    a.addEventListener('click',e=>{
      e.preventDefault();
      mob.classList.remove('open');
      document.body.style.overflow='';
      openBooking();
    });
  }
});
