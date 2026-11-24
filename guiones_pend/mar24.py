import sys,json;sys.path.insert(0,'engine')
from mk_cine import *
V={}
V['slp_192_intxaurrondo']=cine('slp_192_intxaurrondo',[
 ("«No voy a renunciar a mis preguntas». Lo dice una presentadora de la tele pública. Y tiene un expediente encima.",[BIG('b0','«NO VOY A RENUNCIAR A MIS PREGUNTAS»','',color='gold',y=44,fs=92),SELLO('s0','EXPEDIENTE',y=70)],'rojo'),
 ("Se llama Silvia Intxaurrondo. La de La hora de la 1, en TVE.",[mono('m1','ministra',50,72,360,cara='neutral'),BIG('b1','TVE','LA HORA DE LA 1',y=32,fs=150)],'noche'),
 ("¿Y qué hizo? Preguntó en directo si la extrema derecha debe tener espacio en la televisión pública.",[mono('m2','ministra',28,74,300,cara='duda'),BIG('b2','❓','',y=36)],None),
 ("Vox la denunció. Y la Junta Electoral le ha abierto expediente por falta de neutralidad.",[EDI('e3',y=46,w=600),SELLO('s3','JUNTA ELECTORAL',y=78)],'rojo'),
 ("Le puede caer una multa de entre cien y mil euros.",[BIG('b4','100–1.000 €','POSIBLE MULTA',color='red',y=50,fs=150)],'rojo'),
 ("¿Su respuesta? Con ironía: «La libertad de prensa también tiene descuento por pronto pago».",[mono('m5','ministra',50,72,360,say='«Descuento por pronto pago»',cara='risa')],'dia'),
 ("Va a recurrir hasta el final. Y la pregunta ahora es otra: preguntar eso, ¿es opinar… o es hacer periodismo?",[mono('m6','ministra',30,72,280,cara='neutral'),BIG('b6','⚖️','',y=36)],'duelo')],
 '2026-11-24T17:00:00+01:00','¿Opinar o periodismo?','Expediente por *preguntar*','EXPEDIENTE','La Nación (24-11-2026)','#intxaurrondo #tve #juntaelectoral',dias='cinco',
 fin_bg='noche',fin_txt='Tú qué crees: ¿opinión o periodismo? Te leo en comentarios.',fin_show=[BIG('bF','¿OPINIÓN','',color='gold',y=34,fs=150),BIG('bG','O PERIODISMO?','',y=50,fs=150),P('eF','emo',x=50,y=74,w=200,text='🎙️')])
V['slp_193_no_aceptaran']=cine('slp_193_no_aceptaran',[
 ("Faltan cinco días para votar. Y ya se está hablando de lo que pasará… después.",[BIG('b0','DESPUÉS DEL 29-N','',color='gold',y=46,fs=120),P('e0','emo',x=50,y=70,w=220,text='🗳️')],'noche'),
 ("Sánchez, hoy en RNE: «No van a aceptar el resultado electoral y eso es muy grave».",[mono('s1','sanchez',50,72,360,say='«No van a aceptar el resultado»',cara='duda')],'rojo'),
 ("Se refiere al PP y a Vox. Por eso pide una victoria «contundente y amplia».",[mono('s2','sanchez',28,74,300,cara='neutral'),BIG('b2','CONTUNDENTE','Y AMPLIA',y=38,fs=130)],None),
 ("Y Abascal, en Palencia: «Necesitamos vigilar, estar atentos para que no haya ninguna trampa».",[mono('a3','abascal',50,72,360,say='«Que no haya ninguna trampa»',cara='enfado')],'rojo'),
 ("Vox está en alerta con el voto desde el extranjero.",[mono('a4','abascal',72,74,300,cara='neutral'),P('e4','emo',x=30,y=40,w=220,text='✈️')],'dia'),
 ("O sea: uno avisa de que el otro no aceptará el resultado. El otro pide vigilar el voto. Y todavía no ha votado nadie.",[mono('s5','sanchez',26,72,280,cara='duda'),mono('a5','abascal',74,72,280,cara='duda'),BIG('b5','0 VOTOS','AÚN',color='gold',y=36,fs=150)],'duelo')],
 '2026-11-24T20:00:00+01:00','¿Te fías del recuento?','¿Y si *no aceptan*?','SÁNCHEZ VS ABASCAL','Moncloa.com (24-11, entrevista RNE), Estrella Digital (24-11)','#sanchez #abascal #29N',dias='cinco',
 fin_bg='noche',fin_txt='¿Tú te fías del recuento? Dímelo abajo. Y el jueves, debate a cuatro aquí.',fin_show=[BIG('bF','¿TE FÍAS?','',color='gold',y=40,fs=190),P('eF','emo',x=50,y=70,w=220,text='🤔')])
json.dump(V,open('/tmp/claude-0/scr/v24.json','w'),ensure_ascii=False)
print(json.dumps(list(V.values()),ensure_ascii=False))
