// Monigotes SVG de políticos, v2. Rig: cabeza (forma, pelo, cejas, ojos, gafas, barba, boca),
// cuerpo (traje/camiseta), brazos con antebrazo y mano, piernas. Expresiones y gestos.
// Uso: monoSVG(quien, opciones) -> <svg>;  MONO_ANIM(nodo, t, a, habla, e) en cada fotograma.
// Mismo trato para todos: mismo estilo, mismas proporciones de cabezón, sin deformar a nadie.
window.MONOS = {
  sanchez: {skin:'#EDBE9A', fw:49, chin:194, jaw:.55, hair:'lado', hc:'#57524E', hl:'#9A948E', brow:'#3A3532', bw:7, suit:'#1E2A44', shirt:'#fff', tie:null, alto:1.08, smile:1, teeth:1, lips:'#9B4B45'},
  feijoo:  {skin:'#F0C6A6', fw:53, chin:184, jaw:.25, hair:'entradas', hc:'#B9B2AA', hl:'#DCD6CF', brow:'#9C958D', bw:5, gafas:'#3A3A3A', suit:'#3B414D', shirt:'#fff', tie:'#2F5E9E', alto:1.0, smile:.4, lips:'#A35A50'},
  abascal: {skin:'#E7B790', fw:51, chin:190, jaw:.95, hair:'rapado', hc:'#2D2926', hl:'#6B6661', brow:'#26221F', bw:8, barba:'#47423D', barbaHl:'#8A847E', suit:'#1A1D25', shirt:'#fff', tie:'#2B3A55', alto:1.03, smile:0, lips:'#8E4A42'},
  diaz:    {skin:'#F2CBAE', fw:47, chin:180, jaw:.15, hair:'bob', hc:'#E3C07E', hl:'#F6E0AA', brow:'#B99559', bw:5, suit:'#141414', shirt:'#fff', tie:null, alto:0.94, mujer:1, smile:.7, lips:'#B54452', pend:'#E2B84B'},
  colau:   {skin:'#EBBB97', fw:50, chin:181, jaw:.2, hair:'rizos', hc:'#3D291D', hl:'#6E4C36', brow:'#3A271C', bw:6, suit:'#2E2E36', shirt:'#E8E1D3', tie:null, alto:0.92, mujer:1, smile:.9, teeth:1, lips:'#A9564E'},
  montero: {skin:'#EEC2A2', fw:46, chin:183, jaw:.15, hair:'larga', hc:'#382417', hl:'#5E4130', brow:'#2E1E14', bw:6, suit:'#2F2A3B', shirt:'#fff', tie:null, alto:0.93, mujer:1, smile:.5, lips:'#B04D58', pend:'#CFCFCF'},
  motos:   {skin:'#EFC09B', fw:51, chin:186, jaw:.6, hair:'pincho', hc:'#8C8783', hl:'#C4BFBA', brow:'#6E6965', bw:6, barba:'#B57C55', corta:1, suit:'#141414', shirt:'#fff', tie:null, alto:0.98, smile:1, teeth:1, lips:'#9B4B45'},
  broncano:{skin:'#E8B791', fw:45, chin:196, jaw:.4, hair:'rizocorto', hc:'#1F1814', hl:'#3D322B', brow:'#1F1814', bw:7, barba:'#1F1814', barbaHl:'#3D322B', suit:'#262626', camiseta:1, alto:1.0, smile:.3, ojos:1.15, lips:'#8E4A42'},
  wild:    {skin:'#E5AF87', fw:55, chin:188, jaw:.85, hair:'calvo', hc:'#C99A76', hl:'#C99A76', brow:'#2E2219', bw:8, barba:'#33271E', barbaHl:'#5A4636', suit:'#5B5F66', tirantes:1, tatuajes:1, alto:1.03, smile:.6, teeth:1, lips:'#8E4A42', brazos:1.25},
  tu:      {skin:'#E9BC98', fw:49, chin:184, jaw:.35, hair:'lado', hc:'#6B4A33', hl:'#8E6A50', brow:'#4A3324', bw:6, suit:'#E4572E', camiseta:1, alto:0.97, smile:.6, teeth:1, lips:'#A35A50', sudadera:1},
  ministra:{skin:'#EEC6A6', fw:47, chin:182, jaw:.15, hair:'bob', hc:'#4B3A30', hl:'#6E5A4C', brow:'#3A2C24', bw:5, suit:'#7A2E3B', shirt:'#fff', tie:null, alto:0.94, mujer:1, smile:.4, lips:'#A84A55'},
  diputado:{skin:'#EAC0A0', fw:51, chin:186, jaw:.5, hair:'entradas', hc:'#5A4E46', hl:'#80746B', brow:'#3D342E', bw:6, suit:'#2E3B2E', shirt:'#fff', tie:'#6B7F3A', alto:1.0, smile:.2, lips:'#9B4B45'},
  generico:{skin:'#EBC0A0', fw:50, chin:186, jaw:.4, hair:'lado', hc:'#4A3C32', hl:'#6b5a4c', brow:'#3a2e26', bw:6, suit:'#2B3448', shirt:'#fff', tie:'#888', alto:1, smile:.5, lips:'#9B4B45'}
};
const _c=152;
function _face(p){const w=p.fw,ch=p.chin,j=p.jaw;const L=_c-w,R=_c+w;
  // mandíbula: j=0 redonda, j=1 cuadrada
  const jy=128+j*18, jx=w*(0.62+0.3*j);
  return `M${L} 96 Q${L} 44 ${_c} 42 Q${R} 44 ${R} 96 L${R-1} ${jy} Q${R-2} ${ch-14-j*6} ${_c+jx*0.55} ${ch-4} Q${_c} ${ch+3} ${_c-jx*0.55} ${ch-4} Q${L+2} ${ch-14-j*6} ${L+1} ${jy}Z`}
function _hair(p,back){const h=p.hc,l=p.hl,w=p.fw,L=_c-w,R=_c+w;
  switch(p.hair){
  case 'lado': return back?'':`<path d="M${L-4} 104 Q${L-8} 36 ${_c+4} 28 Q${R+12} 30 ${R+4} 106 Q${R-6} 72 ${R-24} 62 Q${_c+20} 50 ${_c-6} 60 Q${L+20} 66 ${L+6} 92Z" fill="${h}"/><path d="M${_c-30} 44 Q${_c+10} 30 ${R-6} 52" stroke="${l}" stroke-width="7" fill="none" stroke-linecap="round" opacity=".75"/><path d="M${L+2} 96 Q${L} 76 ${L+10} 70" stroke="${l}" stroke-width="5" fill="none" opacity=".8"/><path d="M${R-2} 96 Q${R} 76 ${R-10} 70" stroke="${l}" stroke-width="5" fill="none" opacity=".8"/>`;
  case 'entradas': return back?'':`<path d="M${L-2} 102 Q${L-4} 50 ${L+26} 40 Q${_c-16} 50 ${_c-10} 58 Q${_c} 40 ${_c+16} 52 Q${R-20} 36 ${R+2} 54 Q${R+6} 70 ${R+2} 102 Q${R-6} 80 ${R-14} 74 Q${_c} 64 ${L+14} 74 Q${L+4} 84 ${L-2} 102Z" fill="${h}"/><path d="M${L+12} 70 Q${L+20} 56 ${L+30} 52 M${R-12} 70 Q${R-20} 56 ${R-30} 52" stroke="${l}" stroke-width="4" fill="none" opacity=".8"/>`;
  case 'rapado': return back?'':`<path d="M${L} 98 Q${L-2} 40 ${_c} 36 Q${R+2} 40 ${R} 98 Q${R-8} 66 ${_c} 62 Q${L+8} 66 ${L} 98Z" fill="${h}"/><path d="M${L+2} 96 L${L+2} 80 M${R-2} 96 L${R-2} 80" stroke="${l}" stroke-width="6" opacity=".9"/>`;
  case 'pincho': return back?'':`<path d="M${L-2} 100 L${L+2} 56 L${L+16} 62 L${L+20} 36 L${_c-24} 52 L${_c-12} 26 L${_c+2} 48 L${_c+16} 24 L${_c+26} 50 L${R-16} 32 L${R-12} 58 L${R+2} 52 L${R+2} 100 Q${R-6} 72 ${_c} 66 Q${L+6} 72 ${L-2} 100Z" fill="${h}"/><path d="M${_c-12} 32 L${_c-6} 50 M${_c+16} 30 L${_c+14} 50" stroke="${l}" stroke-width="4" opacity=".8"/>`;
  case 'rizocorto': return back?'':`<g fill="${h}">${[[-46,64,20],[-30,46,22],[-8,36,24],[16,36,24],[36,46,22],[50,64,20],[-50,86,16],[54,86,16],[-18,52,18],[24,52,18]].map(([x,y,r])=>`<circle cx="${_c+x}" cy="${y}" r="${r}"/>`).join('')}<path d="M${L} 100 Q${L} 62 ${_c} 60 Q${R} 62 ${R} 100 Q${R-10} 76 ${_c} 74 Q${L+10} 76 ${L} 100Z"/></g><g fill="none" stroke="${l}" stroke-width="3" opacity=".7">${[[-30,46],[-8,36],[16,36],[36,46]].map(([x,y])=>`<path d="M${_c+x-8} ${y-4} q8 -8 14 2"/>`).join('')}</g>`;
  case 'calvo': return back?'':`<path d="M${L+6} 70 Q${_c} 30 ${R-6} 70" stroke="#fff" stroke-opacity=".25" stroke-width="8" fill="none"/>`;
  case 'bob': return back?`<path d="M${L-10} 104 Q${L-14} 34 ${_c+2} 28 Q${R+16} 32 ${R+12} 104 L${R+18} 178 Q${R} 190 ${R-12} 176 L${L+10} 176 Q${L-4} 190 ${L-16} 178Z" fill="${h}"/>`:`<path d="M${L-6} 112 Q${L-6} 34 ${_c+8} 32 Q${R+10} 36 ${R+6} 108 Q${R-6} 70 ${_c+24} 58 Q${_c-6} 84 ${L-6} 112Z" fill="${h}"/><path d="M${_c-28} 50 Q${_c+20} 34 ${R-4} 66 M${L+4} 100 Q${L+14} 70 ${_c-10} 58" stroke="${l}" stroke-width="6" fill="none" stroke-linecap="round" opacity=".8"/>`;
  case 'rizos': return back?`<g fill="${h}">${[[-58,96,28],[-62,132,28],[-56,168,26],[-44,196,22],[58,96,28],[62,132,28],[56,168,26],[44,196,22],[-40,50,30],[0,36,32],[40,50,30]].map(([x,y,r])=>`<circle cx="${_c+x}" cy="${y}" r="${r}"/>`).join('')}</g>`:`<g fill="${h}"><circle cx="${_c-30}" cy="58" r="24"/><circle cx="${_c}" cy="50" r="26"/><circle cx="${_c+30}" cy="58" r="24"/><circle cx="${L+2}" cy="86" r="16"/><circle cx="${R-2}" cy="86" r="16"/><path d="M${L} 104 Q${L+4} 66 ${_c} 64 Q${R-4} 66 ${R} 104 Q${R-14} 80 ${_c} 78 Q${L+14} 80 ${L} 104Z"/></g><g fill="none" stroke="${l}" stroke-width="3" opacity=".6"><path d="M${_c-40} 52 q10 -10 18 0"/><path d="M${_c-8} 44 q10 -10 18 0"/><path d="M${_c+22} 52 q10 -10 18 0"/></g>`;
  case 'larga': return back?`<path d="M${L-8} 100 Q${L-10} 32 ${_c} 28 Q${R+10} 32 ${R+8} 100 L${R+14} 252 Q${R-6} 262 ${R-16} 240 L${L+16} 240 Q${L+6} 262 ${L-14} 252Z" fill="${h}"/>`:`<path d="M${L-2} 120 Q${L-2} 36 ${_c} 34 Q${R+2} 36 ${R+2} 120 Q${R-4} 70 ${_c+4} 58 L${_c} 52 L${_c-4} 58 Q${L+4} 70 ${L-2} 120Z" fill="${h}"/><path d="M${_c} 40 L${_c} 56" stroke="${l}" stroke-width="3" opacity=".7"/>`;
  }return ''}
function monoSVG(name, opts={}){
  const p=Object.assign({}, MONOS[name]||MONOS.generico, opts);const S=p.skin,w=p.fw,L=_c-w,R=_c+w,ch=p.chin;const eo=p.ojos||1;
  const pant=p.camiseta||p.tirantes?'#2B3448':p.suit;
  const legs=`<g class="mlegs"><g class="leg l" style="transform-origin:134px 330px"><rect x="122" y="328" width="24" height="122" rx="9" fill="${pant}"/><path d="M112 446 h40 v14 h-46 q-2-10 6-14Z" fill="#141414"/></g><g class="leg r" style="transform-origin:170px 330px"><rect x="158" y="328" width="24" height="122" rx="9" fill="${pant}"/><path d="M152 446 h40 q8 4 6 14 h-46Z" fill="#141414"/></g></g>`;
  let torso;
  if(p.tirantes) torso=`<path d="M106 204 Q152 192 198 204 L206 338 Q152 350 98 338Z" fill="${p.suit}"/><path d="M122 200 Q152 236 182 200" fill="${S}"/><path d="M106 204 L122 200 L118 250 Z M198 204 L182 200 L186 250Z" fill="${S}"/>`;
  else if(p.sudadera) torso=`<path d="M98 206 Q152 188 206 206 L214 340 Q152 352 90 340Z" fill="${p.suit}"/><path d="M120 200 Q152 232 184 200 Q152 214 120 200Z" fill="#000" opacity=".18"/><path d="M140 214 L138 262 M164 214 L166 262" stroke="#fff" stroke-width="4" stroke-linecap="round"/><rect x="122" y="290" width="60" height="30" rx="8" fill="#000" opacity=".12"/>`;
  else if(p.camiseta) torso=`<path d="M100 206 Q152 190 204 206 L212 338 Q152 350 92 338Z" fill="${p.suit}"/><path d="M130 198 Q152 222 174 198" stroke="#000" stroke-opacity=".3" stroke-width="5" fill="none"/>`;
  else torso=`<path d="M100 206 Q152 190 204 206 L212 338 Q152 350 92 338Z" fill="${p.suit}"/><path d="M132 198 L152 262 L172 198Z" fill="${p.shirt}"/>${p.tie?`<path d="M147 210 h10 l6 54 l-11 14 l-11-14Z" fill="${p.tie}"/><path d="M146 206 h12 l-2 8 h-8Z" fill="${p.tie}" style="filter:brightness(.8)"/>`:''}<path d="M132 198 L152 262 L124 252 L110 214Z" fill="${p.suit}" style="filter:brightness(1.15)"/><path d="M172 198 L152 262 L180 252 L194 214Z" fill="${p.suit}" style="filter:brightness(1.15)"/>${p.mujer?'':`<circle cx="152" cy="290" r="3" fill="#000" opacity=".35"/><circle cx="152" cy="312" r="3" fill="#000" opacity=".35"/>`}`;
  const ab=p.brazos||1, sleeve=(p.tirantes)?S:p.suit;
  const tat=(x)=>p.tatuajes?`<g stroke="#2E3A4A" stroke-width="3" fill="none" opacity=".75"><path d="M${x-8} 228 q8 8 16 0 M${x-9} 244 l18 6 M${x-6} 258 q6 -6 12 0"/><path d="M${x-7} 290 q7 6 14 0 M${x-7} 304 l14 -6"/></g>`:'';
  const arm=(side)=>{const x=side==='l'?104:200;return `<g class="arm ${side}" style="transform-origin:${x}px 214px"><rect x="${x-12*ab}" y="208" width="${24*ab}" height="72" rx="${11*ab}" fill="${sleeve}"/><g class="fore" style="transform-origin:${x}px 276px"><rect x="${x-11*ab}" y="272" width="${22*ab}" height="62" rx="${10*ab}" fill="${sleeve}"/>${tat(x)}<g class="hand"><circle cx="${x}" cy="342" r="14" fill="${S}"/><rect class="finger" x="${x-3.5}" y="342" width="7" height="22" rx="3.5" fill="${S}" opacity="0"/></g></g></g>`};
  const beard=p.barba?(p.corta?`<path d="M${L+4} 126 Q${L+8} ${ch-6} ${_c} ${ch+2} Q${R-8} ${ch-6} ${R-4} 126 Q${R-12} 148 ${_c+22} 150 Q${_c} 142 ${_c-22} 150 Q${L+12} 148 ${L+4} 126Z" fill="${p.barba}" opacity=".55"/>`:`<path d="M${L+1} 118 Q${L+2} ${ch+8} ${_c} ${ch+16} Q${R-2} ${ch+8} ${R-1} 118 Q${R-8} 150 ${_c+24} 152 Q${_c} 142 ${_c-24} 152 Q${L+8} 150 ${L+1} 118Z" fill="${p.barba}"/>${p.barbaHl?`<path d="M${_c-20} ${ch+2} q20 10 40 0 M${L+10} 140 q4 20 16 30 M${R-10} 140 q-4 20 -16 30" stroke="${p.barbaHl}" stroke-width="3" fill="none" opacity=".7"/>`:''}<path d="M${_c-26} 148 Q${_c} 138 ${_c+26} 148 Q${_c} 144 ${_c-26} 148Z" fill="${p.barba}"/>`):'';
  const ey=(x)=>`<g class="eye" style="transform-origin:${x}px 112px"><ellipse cx="${x}" cy="112" rx="${9*eo}" ry="${10*eo}" fill="#fff"/><circle class="pup" cx="${x+1}" cy="113" r="${5.2*eo}" fill="#1b1b1b"/><circle cx="${x+3}" cy="110" r="1.6" fill="#fff"/><path class="lid" d="M${x-10*eo} 112 Q${x} ${100} ${x+10*eo} 112" fill="${S}" opacity="0"/></g>`;
  const head=`<g class="mhead" style="transform-origin:152px 192px">${_hair(p,true)}
    <rect x="137" y="164" width="30" height="40" fill="${S}"/><path d="M137 186 h30 v10 Q152 204 137 196Z" fill="#000" opacity=".12"/>
    <ellipse cx="${L+1}" cy="118" rx="10" ry="15" fill="${S}"/><ellipse cx="${R-1}" cy="118" rx="10" ry="15" fill="${S}"/>
    <path d="${_face(p)}" fill="${S}"/>
    <path d="${_face(p)}" fill="none" stroke="#000" stroke-opacity=".08" stroke-width="3"/>
    ${p.mujer?`<ellipse cx="${_c-30}" cy="138" rx="10" ry="6" fill="#E88" opacity=".25"/><ellipse cx="${_c+30}" cy="138" rx="10" ry="6" fill="#E88" opacity=".25"/>`:''}
    ${beard}
    <g class="eyes">${ey(_c-22)}${ey(_c+22)}</g>
    <g class="brows"><path class="brow l" d="M${_c-36} 96 Q${_c-22} 89 ${_c-9} 95" stroke="${p.brow}" stroke-width="${p.bw}" stroke-linecap="round" fill="none" style="transform-origin:${_c-22}px 94px"/><path class="brow r" d="M${_c+9} 95 Q${_c+22} 89 ${_c+36} 96" stroke="${p.brow}" stroke-width="${p.bw}" stroke-linecap="round" fill="none" style="transform-origin:${_c+22}px 94px"/></g>
    ${p.gafas?`<g fill="rgba(255,255,255,.12)" stroke="${p.gafas}" stroke-width="3.5"><rect x="${_c-40}" y="100" width="34" height="24" rx="5"/><rect x="${_c+6}" y="100" width="34" height="24" rx="5"/><path d="M${_c-6} 108 h12 M${_c-40} 106 L${L-2} 102 M${_c+40} 106 L${R+2} 102" fill="none"/></g>`:''}
    <path d="M${_c-2} 116 Q${_c-8} 136 ${_c-4} 140 Q${_c+2} 144 ${_c+8} 140" stroke="#000" stroke-opacity=".28" stroke-width="3.5" fill="none" stroke-linecap="round"/>
    <g class="mouth" style="transform-origin:${_c}px 160px">
      <path class="mclosed" d="M${_c-18} 158 Q${_c} ${158+10*p.smile} ${_c+18} 158" stroke="${p.lips}" stroke-width="5" fill="none" stroke-linecap="round"/>
      <g class="mopen" style="transform-origin:${_c}px 158px;opacity:0"><path d="M${_c-18} 156 Q${_c} 186 ${_c+18} 156 Q${_c} 162 ${_c-18} 156Z" fill="#5E1F22"/>${p.teeth?`<path d="M${_c-15} 158 Q${_c} 164 ${_c+15} 158 L${_c+13} 163 Q${_c} 167 ${_c-13} 163Z" fill="#fff"/>`:''}<ellipse cx="${_c}" cy="174" rx="8" ry="4" fill="#C0545A" opacity=".8"/></g>
    </g>
    ${p.pend?`<circle cx="${L+1}" cy="136" r="4.5" fill="${p.pend}"/><circle cx="${R-1}" cy="136" r="4.5" fill="${p.pend}"/>`:''}
    <g class="hairf" style="transform-origin:152px 60px">${_hair(p,false)}</g></g>`;
  return `<svg viewBox="40 20 224 450" class="mono" style="overflow:visible;width:100%;height:100%"><ellipse class="shadow" cx="152" cy="462" rx="78" ry="12" fill="#000" opacity=".14"/><g class="ink">${legs}<g class="mbody">${torso}${arm('l')}${arm('r')}</g>${head}</g></svg>`;
}
// expresiones: neutral, sonrie, enfado, sorpresa, risa, duda
const EXPR={neutral:{bl:0,br:0,by:0,sq:0,mo:0},sonrie:{bl:-4,br:4,by:-2,sq:.15,mo:.15},enfado:{bl:14,br:-14,by:4,sq:.25,mo:0},sorpresa:{bl:-8,br:8,by:-9,sq:-.15,mo:.55},risa:{bl:-6,br:6,by:-5,sq:.75,mo:.75},duda:{bl:10,br:-4,by:-6,sq:.1,mo:0}};
function MONO_ANIM(n, t, a, talk, e, exitP){
  const q=s=>n.querySelector(s), qa=s=>n.querySelectorAll(s);
  const ent=e.from&&a<0.75, walk=ent||(exitP>0);
  const sw=walk?Math.sin((ent?a:exitP*2.2)*22)*26:0;
  q('.leg.l').style.transform=`rotate(${sw}deg)`;q('.leg.r').style.transform=`rotate(${-sw}deg)`;
  const br=Math.sin(t*2.2+e.x)*1.6;q('.mbody').style.transform=`translateY(${br+(walk?-Math.abs(Math.sin((ent?a:exitP*2.2)*22))*6:0)}px)`;
  // expresión vigente (e.cara o keyframes e.caras:[{f:0..1 del segmento, c:'enfado'}])
  let ex=e.cara||'neutral';if(e.caras){const f=(t-e.g.t0)/(e.g.t1-e.g.t0);e.caras.forEach(k=>{if(f>=k.f)ex=k.c})}
  const X=EXPR[ex]||EXPR.neutral;
  const hd=q('.mhead');const nod=talk?Math.sin(t*7.3)*3.5+Math.sin(t*3.1)*2:Math.sin(t*1.6)*1.8;const tilt=ex==='duda'?7:0;
  hd.style.transform=`translateY(${br*0.8+(talk?-Math.abs(Math.sin(t*8))*3:0)+(ex==='risa'?-Math.abs(Math.sin(t*16))*5:0)}px) rotate(${nod+tilt}deg) scale(1.24)`;
  const hf=q('.hairf');if(hf)hf.style.transform=`rotate(${-nod*0.35}deg) translateY(${talk?Math.abs(Math.sin(t*8))*1.5:0}px)`;
  // boca
  const amp=talk?0.3+0.7*Math.abs(Math.sin(t*15+Math.sin(t*4)*2)):X.mo;
  const mo=q('.mopen'),mc=q('.mclosed');mo.style.opacity=amp>0.05?1:0;const vis=talk?[1,0.7,1.15,0.8][Math.floor(t*9)%4]:1;mo.style.transform=`scaleY(${0.25+amp*1.0}) scaleX(${ex==='sorpresa'?0.6:vis})`;mc.style.opacity=amp>0.05?0:1;
  mc.style.transformBox='fill-box';mc.style.transformOrigin='center';mc.style.transform=(ex==='enfado'||ex==='duda')?'scaleY(-0.7)':'';
  // ojos: parpadeo + entornar
  const bl=((t+e.x*0.07)%3.6)<0.12;qa('.eye').forEach(x=>{x.style.transform=`scaleY(${bl?0.08:1-Math.max(0,X.sq)*0.55}) scale(${X.sq<0?1.15:1})`});
  // pupilas: miran hacia e.mira ('l'/'r') o al frente
  const px=e.mira==='l'?-3:e.mira==='r'?3:0;qa('.pup').forEach(x=>x.setAttribute('transform',`translate(${px},0)`));
  // cejas
  const em=talk?Math.max(0,Math.sin(t*5.1))*-4:0;
  q('.brow.l').style.transform=`translateY(${X.by+em}px) rotate(${X.bl}deg)`;q('.brow.r').style.transform=`translateY(${X.by+em}px) rotate(${X.br}deg)`;
  // brazos según gesto
  const al=q('.arm.l'),ar=q('.arm.r'),fl=al.querySelector('.fore'),fr=ar.querySelector('.fore'),fing=ar.querySelector('.finger');fing.style.opacity=0;
  let g=e.gesto||(talk?'habla':'quieto');if(walk)g='anda';
  const R2=(el,d)=>el.style.transform=`rotate(${d}deg)`;
  if(g==='anda'){R2(al,-sw*0.8);R2(ar,sw*0.8);R2(fl,-10);R2(fr,-10)}
  else if(g==='habla'){const s=Math.sin(t*4.2);R2(ar,-38-18*s);R2(fr,-62-22*Math.sin(t*6.3));R2(al,8+4*Math.sin(t*2));R2(fl,6)}
  else if(g==='senala'){R2(ar,-82+Math.sin(t*3)*3);R2(fr,-8);fing.style.opacity=1;R2(al,8);R2(fl,4)}
  else if(g==='brazos'){R2(al,-28);R2(fl,-118);R2(ar,28);R2(fr,118)}
  else if(g==='manos'){const s=Math.sin(t*5);R2(al,30+6*s);R2(fl,70);R2(ar,-30-6*s);R2(fr,-70)}
  else if(g==='puno'){R2(ar,-150+Math.sin(t*9)*8);R2(fr,-20);R2(al,8);R2(fl,4)}
  else {R2(al,6+Math.sin(t*1.5)*2);R2(ar,-6-Math.sin(t*1.5)*2);R2(fl,0);R2(fr,0)}
}
