import sys,json;sys.path.insert(0,'engine')
from mk_cine import *
V={}
V['slp_200_sueldo_diputado']=cine('slp_200_sueldo_diputado',[
 ("¿Cuánto va a cobrar cada uno de los 350 diputados que elijas el domingo?",[BIG('b0','350','DIPUTADOS',color='gold',y=34,fs=190),EDI('e0',y=64,w=640)],'noche'),
 ("Sueldo base: 3.366 euros brutos al mes. Lo llaman asignación constitucional.",[BIG('b1','3.366 €','AL MES, BRUTO',color='gold',y=44,fs=160),mono('m1','tu',24,80,220,cara='sorpresa')],'dia'),
 ("Pero hay más. Si no es de Madrid, suma 2.162 euros al mes para gastos. Y sin pagar impuestos por ellos.",[BIG('b2','+2.162 €','GASTOS',y=40,fs=150),SELLO('s2','SIN IRPF',y=66)],None),
 ("Los elegidos por Madrid, 1.032.",[BIG('b3','+1.032 €','SI ES DE MADRID',y=46,fs=150)],None),
 ("¿Portavoz de grupo? Unos 3.200 euros más. ¿Presidente del Congreso? Casi 11.000 extra.",[BARRAS('br4',[{"l":"BASE","v":3.4,"c":"#C8F53C"},{"l":"PORTAVOZ","v":6.6,"c":"#1D84CE"},{"l":"PRESID.","v":14.3,"c":"#D7263D"}],0,0,'',y=52)],'rojo'),
 ("Y al irse pueden pedir una paga: un mes por año de mandato, hasta veinticuatro.",[BIG('b5','24','MESES MÁXIMO',color='red',y=44,fs=190)],'duelo')],
 '2026-11-27T09:00:00+01:00','¿Cobran demasiado? Comenta sí o no.','¿Cuánto *cobra*?','SUELDO','Congreso de los Diputados (régimen económico 2026) y ESdiario (5-10-2026)','#congreso #diputados #sueldos',dias='dos',
 fin_bg='noche',fin_show=[BIG('bF','¿DEMASIADO?','',color='gold',y=40,fs=120),P('eF','emo',x=50,y=70,w=220,text='💰')])
V['slp_201_dhondt']=cine('slp_201_dhondt',[
 ("Tu partido saca el diez por ciento de los votos en tu provincia. ¿Cuántos escaños gana? Puede que ninguno.",[BIG('b0','10 % = 0','ESCAÑOS',color='red',y=40,fs=170),XM('x0',y=66,w=300)],'rojo'),
 ("Es la ley D'Hondt. Imagina una provincia que reparte cinco escaños.",[BIG('b1','5','ESCAÑOS',color='gold',y=40,fs=200),P('u1','urna',y=72,w=300)],'noche'),
 ("Cuatro partidos: cuarenta, treinta, veinte y diez mil votos.",[BARRAS('br2',[{"l":"A","v":40,"c":"#1D84CE"},{"l":"B","v":30,"c":"#E1251B"},{"l":"C","v":20,"c":"#5DAA2B"},{"l":"D","v":10,"c":"#9B59B6"}],0,0,'',y=50)],None),
 ("Se dividen entre uno, entre dos, entre tres… Y los cinco números más altos se llevan escaño.",[BIG('b3','÷1 ÷2 ÷3','',y=40,fs=150),MED('md3','LOS 5 MÁS ALTOS','GANAN ESCAÑO',y=68)],'dia'),
 ("Resultado: dos, dos, uno… y cero para el que sacó el diez por ciento.",[BIG('b4','2 · 2 · 1 · 0','A · B · C · D',color='gold',y=44,fs=150)],'rojo'),
 ("Y por debajo del tres por ciento en tu provincia, ni entras en el reparto.",[BIG('b5','3 %','BARRERA',color='red',y=42,fs=200),SELLO('s5','FUERA',y=68)],'duelo')],
 '2026-11-27T14:00:00+01:00','¿Cambiarías la ley D\'Hondt? Comenta sí o no.','Tu voto *vale 0*','D\'HONDT','LOREG (arts. 162 y 163) y La Moncloa, guía del 29-N','#dhondt #leyelectoral #escaños',dias='dos',
 fin_bg='noche',fin_show=[BIG('bF','¿LA CAMBIARÍAS?','',color='gold',y=40,fs=130),P('eF','emo',x=50,y=70,w=220,text='🗳️')])
V['slp_202_recuento']=cine('slp_202_recuento',[
 ("¿Se puede hacer trampa al contar los votos el domingo? Mira cómo se cuentan.",[BIG('b0','¿TRAMPA?','',color='red',y=36,fs=155),P('u0','urna',y=66,w=380)],'rojo'),
 ("A las ocho se cierra la votación. Y se cuenta allí mismo, en la mesa.",[BIG('b1','20:00','FIN DE LA VOTACIÓN',color='gold',y=42,fs=190)],'noche'),
 ("El presidente saca los sobres uno a uno y lee cada papeleta en voz alta.",[P('u2','urna',y=60,w=420),mono('m2','tu',22,80,220,cara='sorpresa')],None),
 ("Y la enseña a vocales, interventores y apoderados de los partidos.",[BIG('b3','👀','TODOS MIRAN',y=44,fs=200)],'dia'),
 ("Si alguien protesta, la mesa decide por mayoría. Y todo va a un acta, con copia para los partidos.",[P('d4','doc',y=52,w=520),SELLO('s4','ACTA',y=72)],None),
 ("Lo de esa noche es provisional. El oficial lo hacen las Juntas Electorales Provinciales, del cuatro al siete de diciembre.",[BIG('b5','4–7 DIC','RECUENTO OFICIAL',color='gold',y=44,fs=160)],'duelo')],
 '2026-11-27T20:00:00+01:00','¿Has visto alguna vez un recuento? Comenta sí o no.','¿Se puede *hacer trampa*?','RECUENTO','La Moncloa, guía básica del 29-N (6-11-2026) y LOREG (arts. 95-97 y 103)','#recuento #mesaelectoral #votar',dias='dos',
 fin_bg='noche',fin_show=[BIG('bF','¿LO HAS VISTO?','',color='gold',y=40,fs=100),P('eF','emo',x=50,y=70,w=220,text='🗳️')])
V['slp_203_cuando_gobierno']=cine('slp_203_cuando_gobierno',[
 ("Votas el domingo. ¿Cuándo hay nuevo presidente? Spoiler: el lunes no.",[BIG('b0','¿CUÁNDO?','',color='gold',y=38,fs=150),XM('x0',y=66,w=260)],'noche'),
 ("Domingo: se vota de nueve de la mañana a ocho de la tarde. Esa noche, recuento provisional.",[BIG('b1','9:00–20:00','DOMINGO 29',y=42,fs=120),P('u1','urna',y=70,w=280)],'dia'),
 ("Del cuatro al siete de diciembre, las Juntas Electorales hacen el recuento oficial.",[BIG('b2','4–7 DIC','RECUENTO OFICIAL',color='gold',y=44,fs=160)],None),
 ("El veintitrés de diciembre, a las diez, se constituyen el Congreso y el Senado.",[BIG('b3','23 DIC','10:00',color='gold',y=32,fs=150),EDI('e3',y=62,w=600)],'noche'),
 ("Después, el Rey consulta a los partidos y propone un candidato. Y solo entonces, la investidura.",[BIG('b4','👑','RONDA DE CONSULTAS',y=40,fs=200)],None),
 ("Y mientras tanto, desde el lunes, el Gobierno de Sánchez sigue, pero en funciones.",[mono('m5','sanchez',50,72,340,cara='neutral'),SELLO('s5','EN FUNCIONES',y=34)],'duelo')],
 '2026-11-27T23:00:00+01:00','¿Habrá Gobierno antes de Reyes? Comenta sí o no.','¿Cuándo hay *Gobierno*?','CALENDARIO','La Moncloa, guía básica del 29-N (6-11-2026) y Constitución (arts. 99 y 101)','#investidura #gobierno #calendario',dias='dos',
 fin_bg='noche',fin_show=[BIG('bF','¿ANTES','DE REYES?',color='gold',y=40,fs=170),P('eF','emo',x=50,y=70,w=220,text='👑')])
json.dump(V,open('guiones_pend/voces_mie25_pasada.json','w'),ensure_ascii=False,indent=1)
for k,v in V.items(): print(k,len(v.split()),'|',v)
