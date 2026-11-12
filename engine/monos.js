// Monigotes SVG de políticos (rig simple): cabeza, pelo, gafas, barba, boca, ojos, brazos, piernas.
// Uso en slp.html: R.mono(e) -> html ; MONO_ANIM(e, n, t, talk) en el render.
window.MONOS = {
  sanchez: {skin:'#EDBE9A', hair:'#55514E', hl:'#8E8984', style:'corto', suit:'#1E2A44', shirt:'#fff', tie:null, alto:1.07, smile:1},
  feijoo:  {skin:'#EFC3A3', hair:'#A9A39B', hl:'#CFC9C1', style:'corto', suit:'#3A3F4A', shirt:'#fff', tie:'#2E5C9A', gafas:true, alto:1.0},
  abascal: {skin:'#E5B48E', hair:'#2E2A27', hl:'#555', style:'rapado', suit:'#1B1E26', shirt:'#fff', tie:'#2C3E50', barba:'#3B3733', alto:1.03},
  diaz:    {skin:'#F1C9AC', hair:'#E2BF7C', hl:'#F3DCA4', style:'media', suit:'#151515', shirt:'#fff', tie:null, alto:0.94, mujer:1},
  colau:   {skin:'#E9B996', hair:'#3E2A1E', hl:'#6A4A36', style:'rizos', suit:'#2B2B33', shirt:'#E9E2D4', tie:null, alto:0.92, mujer:1},
  montero: {skin:'#ECC0A0', hair:'#3A2618', hl:'#5C4030', style:'larga', suit:'#3C2B4F', shirt:'#fff', tie:null, alto:0.93, mujer:1},
  motos:   {skin:'#EDBE9A', hair:'#8F8A86', hl:'#B9B4AF', style:'pincho', suit:'#151515', shirt:'#fff', tie:null, barba:'#B07A52', barbaCorta:1, alto:0.98},
  broncano:{skin:'#E7B58F', hair:'#211A16', hl:'#3a302a', style:'rizocorto', suit:'#2A2A2A', shirt:'#2A2A2A', tie:null, barba:'#211A16', alto:1.0, camiseta:1},
  wild:    {skin:'#E6B28A', hair:'#E6B28A', hl:'#E6B28A', style:'calvo', suit:'#3A3A3A', shirt:'#3A3A3A', tie:null, barba:'#3A2C22', alto:1.02, camiseta:1},
  generico:{skin:'#EBC0A0', hair:'#4A3C32', hl:'#6b5a4c', style:'corto', suit:'#2B3448', shirt:'#fff', tie:'#888', alto:1}
};
function monoHair(p, back){
  const h=p.hair, l=p.hl;
  switch(p.style){
    case 'corto':  return back?'':`<path d="M98 92 Q100 40 150 34 Q205 32 206 92 Q196 66 168 62 Q130 70 112 64 Q102 74 98 92Z" fill="${h}"/><path d="M118 58 Q150 44 190 56" stroke="${l}" stroke-width="5" fill="none" opacity=".7"/>`;
    case 'rapado': return back?'':`<path d="M100 88 Q104 42 152 38 Q200 40 204 88 Q190 64 152 60 Q114 62 100 88Z" fill="${h}" opacity=".95"/>`;
    case 'pincho': return back?'':`<path d="M98 92 L104 52 L116 60 L122 38 L136 54 L148 32 L160 52 L174 34 L182 56 L196 44 L200 64 L206 92 Q190 68 152 66 Q116 68 98 92Z" fill="${h}"/>`;
    case 'rizocorto': return back?'':`<g fill="${h}">${[0,1,2,3,4,5,6].map(i=>`<circle cx="${104+i*16}" cy="${56+((i%2)*6)}" r="18"/>`).join('')}<path d="M98 92 Q100 60 150 54 Q204 58 206 92 Q190 72 150 70 Q112 72 98 92Z"/></g>`;
    case 'calvo':  return '';
    case 'media':  return back?`<path d="M88 100 Q86 40 152 32 Q218 40 216 104 L222 176 Q190 186 176 168 L128 168 Q114 186 82 176Z" fill="${h}"/>`:`<path d="M96 104 Q100 38 156 36 Q210 40 208 104 Q196 70 166 60 Q130 78 96 104Z" fill="${h}"/><path d="M120 54 Q160 40 196 62" stroke="${l}" stroke-width="6" fill="none" opacity=".7"/>`;
    case 'rizos':  return back?`<g fill="${h}">${[[92,100],[96,140],[104,176],[210,100],[208,140],[200,176],[150,40],[118,50],[184,50]].map(([x,y])=>`<circle cx="${x}" cy="${y}" r="30"/>`).join('')}</g>`:`<g fill="${h}"><circle cx="124" cy="62" r="24"/><circle cx="152" cy="54" r="26"/><circle cx="182" cy="62" r="24"/><path d="M98 100 Q104 60 152 58 Q200 60 206 100 Q186 80 152 78 Q118 80 98 100Z"/></g>`;
    case 'larga':  return back?`<path d="M90 100 Q88 38 152 32 Q216 38 214 100 L220 236 Q186 248 172 224 L132 224 Q118 248 84 236Z" fill="${h}"/>`:`<path d="M98 112 Q100 38 158 38 Q210 44 206 112 Q194 72 170 64 Q150 90 98 112Z" fill="${h}"/>`;
  }
  return '';
}
function monoSVG(name, opts={}){
  const p=Object.assign({}, MONOS[name]||MONOS.generico, opts);
  const S=p.skin, mujer=!!p.mujer;
  const legs=`<g class="mlegs"><g class="leg l" style="transform-origin:132px 330px"><rect x="122" y="330" width="22" height="120" rx="8" fill="${p.camiseta?'#2B3448':p.suit}"/><path d="M114 446 h38 v14 h-44 q-2-10 6-14Z" fill="#111"/></g><g class="leg r" style="transform-origin:170px 330px"><rect x="158" y="330" width="22" height="120" rx="8" fill="${p.camiseta?'#2B3448':p.suit}"/><path d="M152 446 h38 q8 4 6 14 h-44Z" fill="#111"/></g></g>`;
  const torso=`<path d="M100 206 Q150 190 202 206 L212 336 Q150 350 90 336Z" fill="${p.suit}"/>`+
    (p.camiseta?`<path d="M128 200 Q150 220 174 200" stroke="#000" stroke-opacity=".25" stroke-width="5" fill="none"/>`:
    `<path d="M132 198 L150 262 L170 198Z" fill="${p.shirt}"/>${p.tie?`<path d="M146 210 h10 l6 52 l-11 14 l-11-14Z" fill="${p.tie}"/>`:''}<path d="M132 198 L150 262 L122 250 L110 214Z" fill="${p.suit}" opacity=".9"/><path d="M170 198 L150 262 L178 250 L192 214Z" fill="${p.suit}" opacity=".9"/>`);
  const arm=(side)=>{const x=side==='l'?104:198,sg=side==='l'?-1:1;return `<g class="arm ${side}" style="transform-origin:${x}px 214px"><rect x="${x-12}" y="210" width="24" height="70" rx="11" fill="${p.suit}"/><g class="fore" style="transform-origin:${x}px 276px"><rect x="${x-11}" y="272" width="22" height="62" rx="10" fill="${p.suit}"/><circle cx="${x}" cy="342" r="13" fill="${S}"/></g></g>`};
  const head=`<g class="mhead" style="transform-origin:152px 190px">${monoHair(p,true)}
    <rect x="138" y="166" width="28" height="34" fill="${S}"/>
    <ellipse cx="99" cy="118" rx="10" ry="15" fill="${S}"/><ellipse cx="205" cy="118" rx="10" ry="15" fill="${S}"/>
    <path d="M100 96 Q100 46 152 44 Q204 46 204 96 L202 132 Q196 182 152 186 Q108 182 102 132Z" fill="${S}"/>
    ${p.barba?`<path d="M104 128 Q108 ${p.barbaCorta?178:190} 152 ${p.barbaCorta?186:198} Q196 ${p.barbaCorta?178:190} 200 128 Q192 150 176 150 Q152 140 128 150 Q112 150 104 128Z" fill="${p.barba}" opacity="${p.barbaCorta?.55:.95}"/>`:''}
    <g class="eyes"><g class="eye" style="transform-origin:130px 112px"><ellipse cx="130" cy="112" rx="9" ry="10" fill="#fff"/><circle class="pup" cx="131" cy="113" r="5" fill="#1b1b1b"/></g><g class="eye" style="transform-origin:174px 112px"><ellipse cx="174" cy="112" rx="9" ry="10" fill="#fff"/><circle class="pup" cx="175" cy="113" r="5" fill="#1b1b1b"/></g></g>
    <path class="brow l" d="M118 96 Q130 90 142 95" stroke="${p.style==='calvo'?'#3A2C22':p.hair}" stroke-width="6" stroke-linecap="round" fill="none" style="filter:brightness(.7)"/><path class="brow r" d="M162 95 Q174 90 186 96" stroke="${p.style==='calvo'?'#3A2C22':p.hair}" stroke-width="6" stroke-linecap="round" fill="none" style="filter:brightness(.7)"/>
    ${p.gafas?`<g fill="none" stroke="#222" stroke-width="4"><rect x="114" y="100" width="34" height="24" rx="6"/><rect x="156" y="100" width="34" height="24" rx="6"/><path d="M148 110 h8 M114 108 l-12 -4 M190 108 l12 -4"/></g>`:''}
    <path d="M150 118 Q146 138 152 144" stroke="#000" stroke-opacity=".25" stroke-width="4" fill="none"/>
    <g class="mouth" style="transform-origin:152px 160px"><path d="M134 156 Q152 ${p.smile?170:164} 170 156 Q152 ${p.smile?176:168} 134 156Z" fill="#7A2E2E"/><path class="teeth" d="M138 157 Q152 162 166 157" stroke="#fff" stroke-width="4" fill="none" opacity="${p.smile?1:0}"/></g>
    ${mujer?`<circle cx="99" cy="134" r="4" fill="#E8C35A"/><circle cx="205" cy="134" r="4" fill="#E8C35A"/>`:''}
    ${monoHair(p,false)}</g>`;
  return `<svg viewBox="40 20 224 450" class="mono" style="overflow:visible">${legs}<g class="mbody">${torso}${arm('l')}${arm('r')}</g>${head}</svg>`;
}
// anima el rig: talk (bool), a=tiempo desde que aparece, t=tiempo global, mode: 'walk'|'idle'
function MONO_ANIM(n, t, a, talk, e){
  const q=s=>n.querySelector(s), qa=s=>n.querySelectorAll(s);
  const walk=e.from&&a<0.7;
  // piernas
  const sw=walk?Math.sin(a*22)*24:0;
  const ll=q('.leg.l'),lr=q('.leg.r');if(ll){ll.style.transform=`rotate(${sw}deg)`;lr.style.transform=`rotate(${-sw}deg)`}
  // respiración y vaivén
  const br=Math.sin(t*2.2)*1.5;q('.mbody').style.transform=`translateY(${br}px)`;
  const hd=q('.mhead');
  const nod=talk?Math.sin(t*7.3)*4+Math.sin(t*3.1)*2:Math.sin(t*1.6)*2;
  hd.style.transform=`translateY(${br*0.8+(talk?-Math.abs(Math.sin(t*8))*3:0)}px) rotate(${nod}deg) scale(1.22)`;
  // boca
  const m=q('.mouth');const op=talk?0.35+0.65*Math.abs(Math.sin(t*15+Math.sin(t*4)*2)):0.12;m.style.transform=`scaleY(${0.6+op*1.9}) scaleX(${1-op*0.15})`;
  // parpadeo
  const bl=((t+e.x*0.07)%3.4)<0.12;qa('.eye').forEach(x=>x.style.transform=`scaleY(${bl?0.1:1})`);
  // cejas (énfasis al hablar)
  const bw=talk?Math.max(0,Math.sin(t*5.1))*-6:0;qa('.brow').forEach(x=>x.style.transform=`translateY(${bw}px)`);
  // brazos: gesto al hablar
  const al=q('.arm.l'),ar=q('.arm.r');
  if(walk){al.style.transform=`rotate(${-sw*0.8}deg)`;ar.style.transform=`rotate(${sw*0.8}deg)`;al.querySelector('.fore').style.transform='';ar.querySelector('.fore').style.transform='';}
  else if(talk){const g=Math.sin(t*4.2);ar.style.transform=`rotate(${-35-20*g}deg)`;ar.querySelector('.fore').style.transform=`rotate(${-60-25*Math.sin(t*6.3)}deg)`;al.style.transform=`rotate(${8+4*Math.sin(t*2)}deg)`;al.querySelector('.fore').style.transform=`rotate(${10}deg)`}
  else{al.style.transform=`rotate(${6+Math.sin(t*1.5)*2}deg)`;ar.style.transform=`rotate(${-6-Math.sin(t*1.5)*2}deg)`;al.querySelector('.fore').style.transform='';ar.querySelector('.fore').style.transform=''}
}
