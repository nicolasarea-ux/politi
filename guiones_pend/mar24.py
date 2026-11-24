import sys,json;sys.path.insert(0,'engine')
from mk_cine import *
V={}
F='Libertad Digital, Infobae y Público (23-11-2026), debate a ocho de RTVE'
V['slp_192_braveheart_temu']=cine('slp_192_braveheart_temu',[
 ("«Cálmate, si ya sé que eres un Braveheart del Temu». Así le habló Ester Muñoz a Rufián anoche, en el debate a ocho de RTVE.",[mono('m0','munoz',30,72,300,say='«Braveheart del Temu»',cara='sonrie',label='Ester Muñoz · PP'),mono('r0','rufian',72,72,300,cara='sorpresa',label='Gabriel Rufián · ERC')],'rojo'),
 ("Rufián le respondió que hará todo lo posible para que ella no sea ministra.",[mono('r1','rufian',50,72,360,cara='enfado',label='Gabriel Rufián · ERC'),BIG('b1','¿MINISTRA?','',color='gold',y=36,fs=140)],'dia'),
 ("Muñoz, a los socios del Gobierno: hablan «como si no hubieran gobernado ocho años».",[mono('m2','munoz',50,72,360,cara='enfado',label='Ester Muñoz · PP'),BIG('b2','8 AÑOS','',color='red',y=36,fs=160)],'rojo'),
 ("Y Rufián, sobre los trenes: «Si fuera por la derecha, los trenes serían de plástico y las vías de madera».",[mono('r3','rufian',28,74,300,cara='risa',label='Gabriel Rufián · ERC'),BIG('b3','🚆','PLÁSTICO Y MADERA',y=38)],'dia'),
 ("Ocho portavoces, una noche. Y el jueves, los cuatro candidatos.",[mono('m4','munoz',28,72,280,cara='duda'),mono('r4','rufian',72,72,280,cara='duda'),BIG('b4','JUEVES','DEBATE A CUATRO',color='gold',y=36,fs=150)],'duelo')],
 '2026-11-24T20:00:00+01:00','¿Quién ganó el cruce: Muñoz o Rufián?','«Braveheart *del Temu*»','MUÑOZ VS RUFIÁN',F,'#debate #rtve #rufian',dias='cinco')

V['slp_193_nadie_176']=cine('slp_193_nadie_176',[
 ("¿Y si el domingo nadie llega a 176 escaños? No, no se repiten las elecciones. Todavía.",[HEMI('h0',[{'l':'NADIE','n':170,'c':'#9AA5B8'}],line='176',y=50)],'noche'),
 ("Primero, el Rey consulta a los partidos y propone un candidato.",[EDI('e1',y=56),BIG('b1','👑','CONSULTAS',y=84)],'dia'),
 ("Primera votación: necesita 176 síes. Mayoría absoluta.",[BIG('b2','176','SÍES EN LA 1.ª VOTACIÓN',color='gold',y=50)],'dia'),
 ("Si no los tiene, cuarenta y ocho horas después, otra. Ahí basta con más síes que noes.",[BIG('b3','48 H','MÁS SÍES QUE NOES',y=50)],None),
 ("Si tampoco sale, empieza a correr un reloj de dos meses.",[BIG('b4','⏳','2 MESES',color='gold',y=50)],'noche'),
 ("Y si en dos meses nadie es investido, el Rey disuelve las Cortes. Elecciones otra vez.",[XM('x5',y=46),BIG('b5','OTRA VEZ A VOTAR','',color='red',y=82,fs=110)],'rojo')],
 '2026-11-26T14:00:00+01:00','¿Habrá repetición electoral? Comenta sí o no.','¿Y si nadie llega a *176*?','LA INVESTIDURA','Constitución Española, art. 99 (BOE)','#investidura #congreso #constitucion',dias='tres')

V['slp_194_mesa_no_ir']=cine('slp_194_mesa_no_ir',[
 ("¿Te ha tocado mesa el domingo y piensas no ir? Cuidado: no es como una multa de tráfico.",[mono('t0','tu',50,72,340,cara='duda'),BIG('b0','🗳️','¿NO VAS?',y=36)],'rojo'),
 ("Si no vas sin una causa justificada, la ley electoral lo castiga como delito.",[SELLO('s1','DELITO',y=50)],'rojo'),
 ("Hasta un año de prisión. O una multa de seis a veinticuatro meses.",[BIG('b2','1 AÑO','DE PRISIÓN, COMO MÁXIMO',color='red',y=50)],'noche'),
 ("Tienes que estar a las ocho de la mañana. Presidente, dos vocales y sus suplentes.",[BIG('b3','8:00','EL DOMINGO 29',color='gold',y=40),mono('t3','tu',50,80,240,cara='neutral')],'dia'),
 ("A cambio, cobras setenta y cinco euros. Y si te surge una causa de fuerza mayor, avísalo y justifícalo ante la Junta Electoral de Zona.",[BIG('b4','75 €','POR EL DÍA',color='gold',y=50)],'dia')],
 '2026-11-26T20:00:00+01:00','¿Te ha tocado alguna vez? Comenta sí o no.','Te toca *mesa* y no vas','HASTA 1 AÑO','LOREG, arts. 27, 80 y 143 (BOE); dieta de 75 €: Ministerio del Interior','#mesaelectoral #29N #votar',dias='tres')

V['slp_195_reflexion_sabado']=cine('slp_195_reflexion_sabado',[
 ("Desde el viernes a medianoche, los partidos ya no pueden pedirte el voto. Ni uno.",[BIG('b0','00:00','VIERNES 27',color='red',y=50)],'noche'),
 ("Se acaba la campaña: ni mítines, ni actos, ni propaganda electoral.",[XM('x1',y=50)],'rojo'),
 ("El sábado es la jornada de reflexión. Un día entero sin campaña.",[BIG('b2','SÁBADO 28','REFLEXIÓN',color='gold',y=50,fs=150)],'dia'),
 ("Y las encuestas ya no se pueden publicar desde este martes. Hasta que cierren los colegios el domingo.",[BIG('b3','🤐','SIN ENCUESTAS HASTA LAS 20:00',y=50)],'noche'),
 ("La prohibición es para la campaña. Tú puedes seguir hablando de política con quien quieras.",[mono('t4','tu',50,72,340,cara='sonrie'),BIG('b4','💬','',y=34)],'dia')],
 '2026-11-26T23:00:00+01:00','¿Sirve de algo la jornada de reflexión? Comenta sí o no.','El sábado, *silencio*','REFLEXIÓN','LOREG, arts. 51, 53 y 69.7 (BOE)','#jornadadereflexion #29N #votar',dias='tres')

# slp_177: misma pieza, nueva fecha y nueva cuenta atrás
g=json.load(open('guiones/slp_177_coste_elecciones.json'))
for sc in g['scenes']:
  for s in sc['segments']: s['text']=s['text'].replace('quedan seis días','quedan tres días')
g['caption']=g['caption'].replace('Quedan seis días','Quedan tres días');g['fechaPub']='2026-11-26T09:00:00+01:00'
json.dump(g,open('guiones/slp_177_coste_elecciones.json','w'),ensure_ascii=False,indent=1)
V['slp_177_coste_elecciones']=' '.join(s['text'] for sc in g['scenes'] for s in sc['segments'])
for k,v in V.items(): print(k,len(v.split()),v)
json.dump(V,open('guiones_pend/voces_mar24.json','w'),ensure_ascii=False)
