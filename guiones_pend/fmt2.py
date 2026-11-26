import sys;sys.path.insert(0,'engine')
from mk_fmt import fmt,E
V={}
FULL=lambda img,**k:E('pan',img='img/'+img,x=50,y=50,w=1080,h=1920,nob=1,**k)
V['slp_208_f4_pp_vox']=fmt('slp_208_f4_pp_vox','f4',[
 ("PP y Vox. Muchos los meten en el mismo saco.",[E('pan',img='img/feijoo.jpg',pos='40% 10%',x=25,y=50,w=540,h=1920,nob=1),E('pan',img='img/abascal.jpg',pos='50% 10%',x=75,y=50,w=540,h=1920,nob=1),E('big',tx='PP',x=25,y=72,fs=170),E('big',tx='VOX',x=75,y=72,fs=170)]),
 ("Pero sus programas no dicen lo mismo.",[FULL('a_congreso.jpg')]),
 ("Impuestos. El PP quiere ajustar los tramos del IRPF a la inflación cada año.",[FULL('a_tax.jpg')]),
 ("Y para jóvenes de dieciocho a treinta y cinco, una rebaja que empieza en el cien por cien y va bajando.",[FULL('a_young.jpg'),E('stat',tx='18-35',sub='100 % → 75 → 50 → 25',x=50,y=30,w=640,h=240,fs=110,at=3)]),
 ("Vox propuso en el Congreso dejar exentos los primeros veintidós mil euros, y solo dos tipos: quince y veinticinco por ciento.",[FULL('a_tax.jpg'),E('stat',tx='22.000 €',sub='EXENTOS · 15 % · 25 %',x=50,y=30,w=640,h=240,fs=110,at=5)]),
 ("Vivienda. PP: IVA del cuatro por ciento en la primera casa para menores de cuarenta. Vox: IVA cero, para familias españolas.",[FULL('a_keys.jpg'),E('stat',tx='PP: 4 %',sub='VOX: 0 %',x=50,y=28,w=560,h=240,fs=110,subfs=70,at=3)]),
 ("Okupas. PP: recuperar la casa en cuarenta y ocho horas. Vox: desalojo en menos de veinticuatro.",[FULL('a_door.jpg'),E('stat',tx='PP: 48 H',sub='VOX: 24 H',x=50,y=28,w=560,h=240,fs=110,subfs=70,at=1)]),
 ("Y Vox pide prioridad nacional en vivienda protegida y ayudas.",[FULL('a_queue.jpg')]),
 ("En lo que coinciden: los dos quieren derogar la Ley de Vivienda.",[FULL('a_law.jpg')]),
 ("Parecidos, sí. Iguales, no. ¿Con cuál te quedas? Te leo en comentarios.",[E('pan',img='img/feijoo.jpg',pos='40% 10%',x=25,y=50,w=540,h=1920,nob=1),E('pan',img='img/abascal.jpg',pos='50% 10%',x=75,y=50,w=540,h=1920,nob=1)])],
 '2026-11-26T17:30:00+01:00','PP vs Vox: las diferencias que debes conocer','Programas electorales PP y Vox 29N (El Cronista; Rankia), proposición de ley de Vox sobre IRPF (2024). Fotos: Wikimedia Commons. Ilustraciones: IA','#pp #vox #29N',
 portada={'titulo':'PP vs *Vox*','who':['feijoo','abascal'],'sello':'DIFERENCIAS'})
L=lambda img,**k:E('pan',img='img/'+img,x=25,y=50,w=540,h=1920,nob=1,**k)
R=lambda img,**k:E('pan',img='img/'+img,x=75,y=50,w=540,h=1920,nob=1,**k)
HEAD=[L('b_man.jpg',keep=1),R('b_woman.jpg',keep=1),E('vs',x=50,y=56,keep=1),E('pill',tx='1975',x=25,y=24,keep=1),E('pill',tx='2026',x=75,y=24,bg='#5b5fe0',keep=1)]
CARD=lambda img,x,y,at=0:E('pan',img='img/'+img,x=x,y=y,w=360,h=360,round=40,at=at)
V['slp_209_f5_franco']=fmt('slp_209_f5_franco','f5',[
 ("¿Con Franco se vivía mejor? Solo datos, sin opiniones.",[E('pan',img='img/franco.jpg',pos='50% 15%',x=50,y=50,w=1080,h=1920,nob=1)]),
 ("Mil novecientos setenta y cinco contra dos mil veintiséis.",HEAD),
 ("El salario mínimo en 1975: ocho mil cuatrocientas pesetas al mes.",[CARD('b_pesetas.jpg',25,40),E('stat',tx='8.400 pts',sub='AL MES · 1975',x=25,y=62,w=440,h=200,fs=76)]),
 ("Hoy: mil doscientos veintiún euros al mes, en catorce pagas.",[E('stat',tx='1.221 €',sub='AL MES · 14 PAGAS',x=75,y=62,w=440,h=200,fs=84)]),
 ("Esperanza de vida: en 1975, unos setenta y tres años. Hoy, casi ochenta y cuatro.",[E('stat',tx='73 años',x=25,y=40,w=420,h=170,fs=84),E('stat',tx='84 años',x=75,y=40,w=420,h=170,fs=84,at=8)]),
 ("Hasta mayo de 1975, una mujer casada necesitaba el permiso de su marido para trabajar o abrir una cuenta.",[CARD('b_ring.jpg',25,40),E('emo',e='❌',x=25,y=62,fs=170,at=6)]),
 ("Votar: en 1975 no había elecciones libres. Las primeras llegaron en 1977.",[CARD('b_ballot.jpg',75,40),E('pill',tx='1977',x=75,y=62,bg='#2a9d8f',at=8)]),
 ("¿Y algo que fuera mejor entonces? Mucha gente señala la vivienda. Hoy es el gran problema de los jóvenes.",[CARD('b_building.jpg',75,40),E('emo',e='😟',x=75,y=62,fs=170,at=8)]),
 ("Datos sobre la mesa. ¿Tú qué opinas? Te leo en comentarios.",[E('big',tx='¿TÚ QUÉ OPINAS?',x=50,y=38,fs=110,clear=1)])],
 '2026-11-26T19:00:00+01:00','¿Con Franco se vivía mejor? Solo datos','BOE 24-3-1975 (SMI 1975); Real Decreto 126/2026 (SMI 2026); INE; Ley 14/1975 (licencia marital). Foto: Wikimedia Commons (CC0). Ilustraciones: IA','#franco #datos #29N',
 portada={'titulo':'¿Con Franco se vivía *mejor*?','who':['franco'],'sello':'SOLO DATOS'})
import json;json.dump(V,open('/tmp/claude-0/scr/vf2.json','w'),ensure_ascii=False)
print(json.dumps(list(V.values()),ensure_ascii=False))
