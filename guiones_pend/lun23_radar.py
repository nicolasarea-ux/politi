import sys,json;sys.path.insert(0,'engine')
from mk_cine import *
V={}
V['slp_184_gane_de_largo']=cine('slp_184_gane_de_largo',[
 ("Sánchez, anoche en Salvados: «Yo creo que gané el debate de largo».",[mono('s0','sanchez',50,72,360,say='«Gané el debate de largo»',cara='risa')],'dia'),
 ("Y lo explica así: «Hay una figura en la retórica que es la elipsis».",[mono('s1','sanchez',26,74,300,cara='sonrie'),BIG('b1','ELIPSIS','SÁNCHEZ · SALVADOS',color='gold',y=40,fs=150)],'dia'),
 ("Feijóo, esta mañana en Espejo Público: «Es como si cuando el domingo pierda las elecciones dice que está contento».",[mono('f2','feijoo',50,72,360,say='«…dice que está contento»',cara='neutral')],'rojo'),
 ("Y pide no confiarse: «Que un día de relajación no nos condene a cuatro años más de lamentos».",[mono('f3','feijoo',74,74,300,cara='neutral'),BIG('b3','4 AÑOS','FEIJÓO · MURCIA',color='red',y=40,fs=160)],'rojo'),
 ("Los dos dicen que ganan. El jueves, otro debate. Y el domingo, decides tú.",[mono('s4','sanchez',28,72,300,cara='duda'),mono('f4','feijoo',72,72,300,cara='duda'),BIG('b4','29-N','',color='gold',y=36,fs=170)],'duelo')],
 '2026-11-23T20:00:00+01:00','¿Quién ganó el cara a cara: Sánchez o Feijóo?','«Gané *de largo*»','¿Y FEIJÓO?','elDiario.es (22-11), 20minutos (22-11), El Español (23-11)','#sanchez #feijoo #debate',dias='seis')
for k,v in V.items(): print(k,len(v.split()),v)
json.dump(V,open('/tmp/claude-0/scr/voz184.json','w'),ensure_ascii=False)
