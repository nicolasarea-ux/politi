import sys,json;sys.path.insert(0,'engine')
from mk_cine import *
V={}
E=lambda id,t,x=50,y=50,w=220:P(id,'emo',x=x,y=y,w=w,text=t,fs=int(w*1.1))
SH=lambda txt:[E('eF','📤',50,40,300),BIG('bF',txt,'',color='gold',y=64,fs=130)]
V['slp_202_plex_247']=cine('slp_202_plex_247',[
 ("Doscientos cuarenta y siete kilómetros por hora. Y de copiloto, el candidato del PP.",[BIG('b0','247','KM/H',color='gold',y=42,fs=240),E('e0','🏎️',50,72,240)],'rojo'),
 ("Plex conduce su Porsche por el Jarama. Feijóo va al lado. Hay trompos. Y Feijóo suelta: «Esta es la prueba más difícil de la campaña».",[mono('f1','feijoo',50,72,360,say='«La prueba más difícil»',cara='sorpresa')],'noche'),
 ("Al ver el marcador: «Ya no lo seguí mirando».",[BIG('b2','👀','',y=40,fs=200),BIG('b2b','«YA NO LO SEGUÍ MIRANDO»','',color='gold',y=70,fs=80)],None),
 ("Y luego, medio en broma: «Bueno, yo no sabía que ibas a ir a 247».",[mono('f3','feijoo',30,74,300,cara='duda'),BIG('b3','¿247?','',y=36,fs=170)],'rojo'),
 ("Plex le pincha: a ti también te van las emociones fuertes, «si no, no estarías aquí».",[E('e4','😏',50,44,280)],'dia'),
 ("¿Su veredicto? «No he pasado miedo, pero cuidado». Y dice que ha sido el momento más intenso de toda la campaña. Más que el cara a cara con Sánchez.",[mono('f5','feijoo',50,72,360,say='«No he pasado miedo»',cara='risa'),BIG('b5','💓','',y=30,fs=160)],'duelo')],
 '2026-11-26T08:30:00+01:00','','Feijóo a *247 km/h*','FEIJÓO x PLEX','Libertad Digital y Público (25-11-2026), canal de Plex','#plex #feijoo #porsche',dias='cuatro',
 fin_bg='noche',fin_txt='Mándaselo a quien conduzca como Plex. Y esta noche, debate a cuatro en directo.',fin_show=SH('MÁNDASELO'))
V['slp_203_plex_feijoo_vox']=cine('slp_203_plex_feijoo_vox',[
 ("Plex le pregunta a Feijóo lo que todo el mundo quiere saber: ¿y Vox?",[mono('f0','feijoo',30,72,280,cara='duda'),mono('a0','abascal',70,72,280,cara='neutral'),BIG('b0','¿Y VOX?','',color='gold',y=34,fs=170)],'noche'),
 ("Su respuesta: «Más del treinta por ciento de la población tiene un presidente del Partido Popular con algún miembro del Gobierno de Vox».",[BIG('b1','+30%','PP CON VOX EN GOBIERNOS',color='gold',y=46,fs=200)],None),
 ("Y añade: «Creo que no ha pasado nada grave».",[mono('f2','feijoo',50,72,360,say='«No ha pasado nada grave»',cara='neutral')],'rojo'),
 ("Sobre los votantes de Vox: «Yo no creo que los tres millones de ciudadanos que voten a Vox sean gente extrañísima».",[BIG('b3','3 M','VOTANTES DE VOX',y=40,fs=190),E('e3','🗳️',50,72,200)],'dia'),
 ("¿Pactará con ellos? «El domingo vamos a votar. ¿Qué va a decidir la gente? Bueno, no lo sabemos».",[mono('f4','feijoo',50,72,360,say='«No lo sabemos»',cara='duda')],None),
 ("Ni sí, ni no. Y esta noche, en el debate, Abascal estará a un metro. ¿Saldrá el tema?",[mono('f5','feijoo',26,72,280,cara='duda'),mono('a5','abascal',74,72,280,cara='risa'),BIG('b5','22:00','',color='gold',y=34,fs=150)],'duelo')],
 '2026-11-26T10:00:00+01:00','','Feijóo y *Vox*','FEIJÓO x PLEX','Público (25-11-2026), canal de Plex','#plex #feijoo #vox',dias='cuatro',
 fin_bg='noche',fin_txt='¿Crees que pactarán? Dímelo abajo y compártelo. Esta noche, debate a cuatro en directo.',fin_show=[BIG('bF','¿PACTARÁN?','',color='gold',y=40,fs=135),E('eF','🤝',50,68,240)])
json.dump(V,open('/tmp/claude-0/scr/vplex2.json','w'),ensure_ascii=False)
print(json.dumps(list(V.values()),ensure_ascii=False))
