import sys,json;sys.path.insert(0,'engine')
from mk_cine import *
V={}
F='elDiario.es/Vertele y OKdiario (23-11-2026), El Hormiguero (Antena 3)'
V['slp_188_wild_vox_derechos']=cine('slp_188_wild_vox_derechos',[
 ("Jordi Wild ha contado en El Hormiguero por qué Abascal no fue a su entrevista. Y no es lo que pensabas.",[mono('w0','wild',30,72,280,cara='sorpresa'),mono('m0','motos',70,72,280,cara='neutral')],'noche'),
 ("Según Wild, Vox quería grabarla ellos. Con los derechos de emisión.",[mono('a1','abascal',50,72,340,cara='neutral'),BIG('b1','🎥','DERECHOS DE EMISIÓN',y=34)],'rojo'),
 ("Su respuesta: «Eso no es serio». «Esto no es serio, estás en mi casa».",[mono('w2','wild',50,72,360,say='«Estás en mi casa»',cara='enfado')],'rojo'),
 ("Y deja claro: «¿Qué interés tengo yo de manipularlo?».",[mono('w3','wild',28,74,300,cara='duda'),BIG('b3','¿MANIPULAR?','',color='gold',y=38,fs=130)],None),
 ("Dice que, al ver que era imposible, «me pidieron perdón».",[mono('w4','wild',72,74,300,cara='neutral'),BIG('b4','🙏','',y=36)],'dia'),
 ("¿Su teoría? «Creo que salieron tan reforzados de La Revuelta, que pensaron que era bueno minimizar un riesgo más».",[mono('w5','wild',30,72,280,cara='duda'),mono('a5','abascal',70,72,280,cara='neutral')],'duelo')],
 '2026-11-24T00:15:00+01:00','¿Hizo bien Vox en no ir? Comenta sí o no.','Por qué *Abascal* no fue','«NO ES SERIO»',F,'#jordiwild #abascal #elhormiguero #vox',dias='cinco')
V['slp_189_wild_psoe_pp']=cine('slp_189_wild_psoe_pp',[
 ("Ha entrevistado a Sánchez, Feijóo y Colau. Y en El Hormiguero ha soltado esto.",[mono('w0','wild',50,72,360,cara='neutral')],'noche'),
 ("Sobre PSOE y PP: «Son partidos asolados por la corrupción».",[mono('w1','wild',50,72,360,say='«Asolados por la corrupción»',cara='enfado')],'rojo'),
 ("Y va más allá: «Yo te diría de desbandarlos y crear una alternativa».",[mono('w2','wild',28,74,300,cara='enfado'),BIG('b2','ALTERNATIVA','',color='gold',y=38,fs=130)],'rojo'),
 ("¿Y los candidatos? «Casi ninguno de ellos me convence, no es un tema ideológico, es un tema de palabra».",[mono('w3','wild',72,74,300,cara='duda'),BIG('b3','PALABRA','NO IDEOLOGÍA',y=38,fs=150)],None),
 ("Aunque matiza: «Al humanizarlos no son monstruos, el trato fue muy bueno».",[mono('w4','wild',50,72,340,cara='risa')],'dia'),
 ("Y suelta la frase de la noche: «Para ascender en la política de hoy en día tienes que tener un punto medio psicopático».",[mono('w5','wild',50,72,360,say='«Un punto medio psicopático»',cara='sorpresa')],'duelo')],
 '2026-11-24T02:15:00+01:00','¿Estás de acuerdo con Wild? Comenta sí o no.','«Asolados por la *corrupción*»','JORDI WILD',F,'#jordiwild #psoe #pp #elhormiguero',dias='cinco')
V['slp_190_wild_sanchez']=cine('slp_190_wild_sanchez',[
 ("Antes de entrevistar a Sánchez, su equipo revisó el estudio. Y según Jordi Wild, «pasaron hasta los perros».",[mono('w0','wild',50,72,360,say='«Pasaron hasta los perros»',cara='sorpresa')],'noche'),
 ("«Vinieron días antes a comprobar las calles, el estudio, horas antes a revisarlo».",[mono('s1','sanchez',50,72,340,cara='neutral'),BIG('b1','🐕','',y=34)],'dia'),
 ("Su veredicto: «Un crack, una bestia política, impone pero fue muy amable».",[mono('s2','sanchez',50,72,360,say='«Una bestia política»',cara='risa')],'dia'),
 ("Y reconoce: «Él sabía que era la entrevista más dura».",[mono('s3','sanchez',28,74,300,cara='neutral'),BIG('b3','LA MÁS DURA','',color='red',y=38,fs=130)],'rojo'),
 ("Pero sus cambios de opinión le parecieron «bastante escandalosos». Y su discurso no le convenció.",[mono('w4','wild',72,74,300,cara='enfado'),XM('x4',y=36)],'rojo'),
 ("Amable sí. Convincente, según Wild, no.",[mono('w5','wild',30,72,280,cara='duda'),mono('s5','sanchez',70,72,280,cara='risa')],'duelo')],
 '2026-11-24T07:00:00+01:00','¿Qué opinas de Sánchez en el podcast? Comenta.','«Hasta los *perros*»','SÁNCHEZ',F,'#jordiwild #sanchez #elhormiguero',dias='cinco')
V['slp_191_wild_feijoo']=cine('slp_191_wild_feijoo',[
 ("Jordi Wild dice que, si hubiera entrevistado a Feijóo el primer día, la entrevista habría sido otra.",[mono('w0','wild',30,72,280,cara='duda'),mono('f0','feijoo',70,72,280,cara='neutral')],'noche'),
 ("Su gran error: «Querer hacer cuatro entrevistas en cuatro días consecutivos».",[mono('w1','wild',50,72,340,cara='duda'),BIG('b1','4 EN 4','',color='gold',y=34,fs=160)],'rojo'),
 ("«Llegué agotado mentalmente a Feijóo». Y «se me quedaron temas como el de la DANA, Mazón».",[mono('w2','wild',50,72,360,say='«Llegué agotado»',cara='sorpresa')],'rojo'),
 ("Aun así, cuando le preguntó por el piso de Ayuso y el caso Marcial, lo vio «apurado».",[mono('f3','feijoo',50,72,360,say='…',cara='duda'),BIG('b3','APURADO','',color='red',y=34,fs=150)],None),
 ("«Si esa parte hubiera durado más hubiera estado más apurado».",[mono('f4','feijoo',28,74,300,cara='duda'),BIG('b4','⏱️','',y=36)],'dia'),
 ("Su definición: «Un político de la vieja escuela».",[mono('f5','feijoo',50,72,360,say='«Vieja escuela»',cara='neutral')],'duelo')],
 '2026-11-24T08:30:00+01:00','¿Le hizo bien la entrevista a Feijóo? Comenta.','«Llegué *agotado*»','FEIJÓO',F,'#jordiwild #feijoo #elhormiguero',dias='cinco')
json.dump(V,open('/tmp/claude-0/scr/vw2.json','w'),ensure_ascii=False)
for k,v in V.items(): print(k,len(v))
