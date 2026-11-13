// Portada «cara a cara» con monigotes: protagonista + rival/entrevistador, cita gigante en bocadillo.
// Se carga dentro de slp.html (usa monoSVG, MONO_ANIM). Campos: g.portada.{serie,titulo,mini.rojo,monos:[{who,cara,gesto}]}
function _coverPeople(g){
  const P=g.portada||{};
  if(P.monos) return P.monos;
  const cnt={};(g.scenes||[]).forEach(sc=>sc.segments.forEach(s=>s.show.forEach(e=>{if(e.type==='mono'&&e.who!=='tu')cnt[e.who]=(cnt[e.who]||0)+(e.say?2:1)})));
  const ks=Object.keys(cnt).sort((a,b)=>cnt[b]-cnt[a]);
  let main=ks.find(k=>k!=='wild')||ks[0];let sec=ks.includes('wild')&&main!=='wild'?'wild':ks.find(k=>k!==main);
  const t=(P.titulo||'')+' '+((P.mini||{}).texto||'');
  // si el título empieza por "Wild a X", el que habla es Wild
  if(/^Wild\b/i.test(P.titulo||'')&&ks.includes('wild')){const o=main;main='wild';sec=o}
  const NM={sanchez:/s[áa]nchez|pedro/i,feijoo:/feij[óo]o/i,abascal:/abascal|vox/i,colau:/colau/i,wild:/\bwild\b/i,diaz:/yolanda|d[íi]az/i,motos:/motos/i,broncano:/broncano/i,ayuso:/ayuso/i};
  const named=Object.keys(NM).filter(k=>k!==main&&k!=='ayuso'&&NM[k].test(P.titulo||''));if(named.length&&!(main==='wild')) sec=named.find(k=>k!=='wild')||sec;
  const out=[{who:main,cara:'enfado',gesto:'senala'}];if(sec)out.push({who:sec,cara:'sorpresa',gesto:'brazos'});return out;
}
async function renderCoverMono(g){
  const P=g.portada||{};const ppl=_coverPeople(g);
  const quote=((P.mini||{}).rojo||(P.titulo||'').replace(/^[^*]*\*|\*.*$/g,'')).replace(/^«|»$/g,'');
  const tit=(P.titulo||'').replace(/\*(.+?)\*/g,'<span class="hl">$1</span>');
  const PC={sanchez:'#E1251B',feijoo:'#1D84CE',abascal:'#63BE21',colau:'#E5007D',diaz:'#E5007D',montero:'#E1251B',wild:'#F2B705',motos:'#FF7A00',broncano:'#8A5CF6'};
  const c1=PC[ppl[0].who]||'#C8F03C',c2=ppl[1]?(PC[ppl[1].who]||'#C8F03C'):'#C8F03C';
  document.body.innerHTML=`<div id="cv" style="position:fixed;inset:0;width:1080px;height:1920px;overflow:hidden;background:#101A30">
   <div style="position:absolute;inset:0;background:linear-gradient(115deg, ${c1} 0 49.6%, ${c2} 50.4% 100%);opacity:.92"></div>
   <div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 46%, rgba(255,255,255,.28), rgba(0,0,0,.0) 45%), repeating-linear-gradient(115deg, rgba(0,0,0,.07) 0 14px, transparent 14px 28px)"></div>
   <div style="position:absolute;left:0;right:0;top:0;height:300px;background:linear-gradient(#101A30,rgba(16,26,48,0))"></div>
   <div style="position:absolute;left:0;right:0;bottom:0;height:820px;background:linear-gradient(rgba(16,26,48,0),rgba(16,26,48,.92) 42%,#101A30 70%)"></div>
   <div style="position:absolute;left:50%;top:300px;transform:translateX(-50%);font:900 40px I;letter-spacing:3px;color:#101A30;background:#C8F03C;padding:8px 26px;border-radius:10px;white-space:nowrap">${P.serie||''}</div>
   <div id="bub" style="position:absolute;left:70px;right:70px;top:390px;background:#fff;border:9px solid #101A30;border-radius:44px;padding:30px 34px;box-shadow:0 16px 0 rgba(0,0,0,.35);text-align:center;font:900 ${quote.length>34?84:quote.length>22?98:112}px/1.02 I;color:#101A30;text-transform:uppercase">«${quote}»<i style="position:absolute;left:${ppl[0].who==='wild'?'auto':'190px'};${ppl[0].who==='wild'?'right:190px;':''}bottom:-58px;width:0;height:0;border-left:34px solid transparent;border-right:34px solid transparent;border-top:58px solid #101A30"></i><i style="position:absolute;left:${ppl[0].who==='wild'?'auto':'200px'};${ppl[0].who==='wild'?'right:200px;':''}bottom:-40px;width:0;height:0;border-left:24px solid transparent;border-right:24px solid transparent;border-top:42px solid #fff"></i></div>
   <div id="m1" style="position:absolute;left:${ppl[0].who==='wild'?'auto':'40px'};${ppl[0].who==='wild'?'right:30px;':''}top:740px;width:540px;filter:drop-shadow(0 18px 0 rgba(0,0,0,.25))">${monoSVG(ppl[0].who)}</div>
   ${ppl[1]?`<div id="m2" style="position:absolute;${ppl[0].who==='wild'?'left:70px;':'right:50px;'}top:860px;width:420px;transform:${ppl[0].who==='wild'?'none':'scaleX(-1)'};filter:drop-shadow(0 14px 0 rgba(0,0,0,.25))">${monoSVG(ppl[1].who)}</div>`:''}
   <div style="position:absolute;left:50px;right:50px;top:1360px;background:rgba(16,26,48,.9);border:5px solid #C8F03C;border-radius:30px;padding:26px 24px 18px;text-align:center;box-shadow:0 12px 0 rgba(0,0,0,.3)"><div style="font:900 70px/1.06 F;color:#fff">${tit}</div><div style="font:900 32px I;color:#C8F03C;margin-top:12px;letter-spacing:1px">@politizatehoy</div></div>
   <style>.hl{background:#C8F03C;color:#101A30;padding:0 12px;border-radius:10px;box-decoration-break:clone;-webkit-box-decoration-break:clone}</style>
  </div>`;
  const s1=document.querySelector('#m1 svg'),s2=document.querySelector('#m2 svg');
  [s1,s2].forEach(s=>{if(s){s.style.width='100%';s.style.height='auto';s.style.overflow='visible'}});
  const pose=(sel,p)=>{const n=document.querySelector(sel);if(!n)return;try{MONO_ANIM(n,0.35,1,p.habla!==false,{cara:p.cara,gesto:p.gesto,g:{t0:0,t1:1},habla:true,tf:[0,1]},0)}catch(e){console.log(e)}};
  pose('#m1',ppl[0]);if(ppl[1])pose('#m2',ppl[1]);
  // la cita no debe pisar a los monigotes
  const b=document.getElementById('bub');let fs=parseInt(getComputedStyle(b).fontSize);while(b.getBoundingClientRect().bottom>800&&fs>56){fs-=6;b.style.fontSize=fs+'px'}
}
