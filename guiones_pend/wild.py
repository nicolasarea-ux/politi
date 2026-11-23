import sys,json;sys.path.insert(0,'engine')
from mk_cine import *
V={}
F='elDiario.es/Vertele (17-11-2026), entrevista en Horizonte (Cuatro)'
V['slp_185_wild_planton']=cine('slp_185_wild_planton',[
 ("Iba a sentar a los cuatro candidatos. Y horas antes, uno se le cayó.",[mono('w0','wild',50,72,360,cara='sorpresa'),BIG('b0','4 → 3','CANDIDATOS',color='gold',y=34,fs=160)],'noche'),
 ("Abascal no fue a la entrevista con Jordi Wild. La noche antes de la de Feijóo.",[mono('a1','abascal',50,72,340,cara='neutral'),XM('x1',y=36)],'rojo'),
 ("Wild lo contó así: «Para mí fue un choque anímico importante. Me sentía un poco hundido».",[mono('w2','wild',50,72,360,say='«Me sentía un poco hundido»',cara='duda')],'noche'),
 ("Y añadió: «La presión de la prensa ese día fue el más bestia que he tenido en mi vida».",[mono('w3','wild',28,74,300,cara='sorpresa'),BIG('b3','PRESIÓN','«EL MÁS BESTIA»',color='red',y=38,fs=150)],'rojo'),
 ("Pero no se culpa: «Con el tema de Abascal yo sé que no me tengo que culpar a mí mismo».",[mono('w4','wild',72,74,300,cara='neutral'),BIG('b4','🙅','',y=38)],'dia'),
 ("Y esta noche, se ha sentado con Pablo Motos en El Hormiguero.",[mono('w5','wild',30,72,280,cara='risa'),mono('m5','motos',70,72,280,cara='risa')],'duelo')],
 '2026-11-24T00:15:00+01:00','¿Hizo bien Abascal en no ir? Comenta sí o no.','El plantón de *Abascal*','«HUNDIDO»',F,'#jordiwild #abascal #elhormiguero',dias='cinco')
V['slp_186_wild_ranking']=cine('slp_186_wild_ranking',[
 ("Jordi Wild ha entrevistado a Sánchez, Feijóo y Colau. Y ya ha dicho quién le gustó más.",[mono('s0','sanchez',20,72,240),mono('f0','feijoo',50,72,240),mono('c0','colau',80,72,240)],'noche'),
 ("Feijóo, según él, fue «el más desubicado de los tres en cuanto al sitio en el que estaba».",[mono('f1','feijoo',50,72,360,say='«El más desubicado»',cara='duda')],'dia'),
 ("Pero matiza: «fue muy agradable». Y le sorprendió «lo campechano que es».",[mono('f2','feijoo',28,74,300,cara='risa'),BIG('b2','CAMPECHANO','',color='gold',y=38,fs=130)],'dia'),
 ("Sánchez fue el que más le impuso. Lo vio «muy tranquilo» y «cordial».",[mono('s3','sanchez',50,72,360,say='«Muy tranquilo»',cara='neutral')],None),
 ("¿Y la ganadora? Colau. «La mejor de las tres a nivel de trato».",[mono('c4','colau',50,72,360,cara='risa'),BIG('b4','🥇','',y=34)],'duelo'),
 ("«Tenía muchas ganas de dar juego». Y fue con su hijo, que es fan de Wild.",[mono('c5','colau',30,74,300,cara='risa'),mono('w5','wild',70,74,300,cara='risa')],'dia')],
 '2026-11-24T00:50:00+01:00','¿Cuál de las tres entrevistas te gustó más? Comenta.','El ranking de *Wild*','¿QUIÉN GANÓ?',F,'#jordiwild #colau #feijoo #sanchez',dias='cinco')
V['slp_187_wild_mil_fallos']=cine('slp_187_wild_mil_fallos',[
 ("Quería entrevistar a los cuatro candidatos en cuatro días seguidos. Y Jordi Wild admite que se equivocó.",[BIG('b0','4 EN 4','CANDIDATOS · DÍAS',color='gold',y=50)],'noche'),
 ("Lo dice él: «Lo he dado todo pero he hecho mil fallos».",[mono('w1','wild',50,72,360,say='«He hecho mil fallos»',cara='duda')],'rojo'),
 ("Hacerlas tan seguidas, según Wild, fue «un error de cálculo por mi parte total».",[mono('w2','wild',28,74,300,cara='sorpresa'),BIG('b2','ERROR','DE CÁLCULO',color='red',y=38,fs=160)],'rojo'),
 ("¿Por qué? «Nunca había hecho este tipo de entrevistas». «Mi formato es otro».",[mono('w3','wild',72,74,300,cara='neutral'),BIG('b3','🎙️','',y=36)],None),
 ("Dice que él no suele repreguntar ni crear tensión.",[mono('w4','wild',50,72,340,cara='duda')],'dia'),
 ("¿Y si alguien le dictaba las preguntas desde detrás de cámara? Respuesta: «No, no, no».",[XM('x5',y=40),mono('w5','wild',50,76,300,cara='risa')],'duelo')],
 '2026-11-24T01:30:00+01:00','¿Le pondrías nota a sus entrevistas? Del 1 al 10.','«Mil *fallos*»','AUTOCRÍTICA',F,'#jordiwild #thewildproject #29N',dias='cinco')
json.dump(V,open('/tmp/claude-0/scr/vw.json','w'),ensure_ascii=False)
for k,v in V.items(): print(k,len(v))
