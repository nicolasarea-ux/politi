import sys;sys.path.insert(0,'engine')
from mk_fmt import fmt,E
V={}
POD=lambda hl=None:E('podios',x=50,y=80,hl=hl)
def CAND(who,lab,party,stat,sub,fs=80,emo=None):
    els=[E('por',who=who,x=50,y=40,w=620,h=760,label=lab),E('big',tx=party,x=50,y=90,fs=200 if len(party)<6 else 120,color='#fff'),E('stat',tx=stat,sub=sub,x=70,y=50,w=500,h=230,fs=fs,at=2)]
    if emo: els.append(E('emo',e=emo,x=20,y=55,fs=170,at=2))
    return els
V['slp_204_f1_vivienda']=fmt('slp_204_f1_vivienda','f1',[
 ("El domingo no eliges presidente. Eliges trescientos cincuenta diputados.",[E('hemi',x=50,y=45)]),
 ("Hay más partidos, pero estos cuatro debaten esta noche a las diez.",[E('big',tx='DEBATE A CUATRO',sub='JUEVES 26 · 22:00',x=50,y=36,fs=120,subfs=64,subc='#F7D23E'),POD()]),
 ("Y en lo que más te preocupa, la vivienda, esto es lo que promete cada uno.",[POD(),E('emo',e='🏠',x=50,y=38,fs=300)]),
 ("Feijóo, PP: construir un millón de viviendas.",CAND('feijoo','FEIJÓO','PP','1.000.000','DE VIVIENDAS',emo='🏗️')),
 ("Y un IVA del cuatro por ciento en la primera vivienda para menores de cuarenta.",CAND('feijoo','FEIJÓO','PP','IVA 4 %','PRIMERA VIVIENDA · MENORES DE 40',fs=100,emo='🏠')),
 ("Sánchez, PSOE: el uno por ciento del PIB cada año para vivienda.",CAND('sanchez','SÁNCHEZ','PSOE','1 % DEL PIB','CADA AÑO PARA VIVIENDA',fs=90,emo='💶')),
 ("Abascal, Vox: IVA cero para familias españolas y prioridad nacional en vivienda y ayudas.",CAND('abascal','ABASCAL','VOX','PRIORIDAD NACIONAL','IVA 0 % · VIVIENDA Y AYUDAS',fs=62,emo='🇪🇸')),
 ("Colau, Frente Amplio: un millón y medio de viviendas públicas en doce años.",CAND('colau','COLAU','FRENTE AMPLIO','1.500.000','VIVIENDAS PÚBLICAS EN 12 AÑOS',emo='🏘️')),
 ("¿Y tu nómina? El PP propone que, si tienes entre dieciocho y treinta y cinco años, no pagues IRPF.",[E('card',title='NÓMINA',lines=[{'a':'Salario bruto','b':'· · · ·'},{'a':'Seguridad Social','b':'· · · ·'},{'a':'IRPF 18-35 años','b':'0 €','hl':1}],x=50,y=45,w=820,h=420,at=2),POD('pp')]),
 ("¿Letra pequeña? Solo es el cien por cien el primer año. Luego, setenta y cinco, cincuenta y veinticinco.",[E('card',title='REBAJA IRPF JÓVENES',lines=[{'a':'Año 1','b':'100 %','hl':1},{'a':'Año 2','b':'75 %'},{'a':'Año 3','b':'50 %'},{'a':'Año 4','b':'25 %'}],x=50,y=45,w=820,h=480),E('emo',e='🔍',x=80,y=58,fs=200,at=1)]),
 ("Esta noche, los cuatro, cara a cara. ¿Con quién te quedas? Te leo en comentarios.",[E('big',tx='¿CON QUIÉN TE QUEDAS?',x=50,y=36,fs=110),POD()])],
 '2026-11-26T11:30:00+01:00','El domingo no eliges presidente','Programas electorales PP, PSOE, Vox y Frente Amplio (El Cronista, Rankia, nov. 2026). Fotos: Wikimedia Commons','#vivienda #debate #29N',
 portada={'titulo':'No eliges *presidente*','who':['feijoo','sanchez','abascal','colau'],'sello':'VIVIENDA'})
V['slp_205_f2_puigdemont']=fmt('slp_205_f2_puigdemont','f2',[
 ("Puigdemont vuelve a España después de nueve años. ¿Por qué se fue, por qué ahora y cuándo vuelve?",[E('step',n=0),E('por',who='puigdemont',x=50,y=34,w=760,h=760)]),
 ("Uno: por qué se fue. En octubre de 2017, tras la declaración de independencia en el Parlament,",[E('step',n=1),E('por',who='parlament',x=50,y=30,w=900,h=560,at=4)]),
 ("se marchó a Bélgica para evitar que lo detuvieran. Y allí ha vivido estos años, en Waterloo.",[E('step',n=1),E('emo',e='🇧🇪',x=30,y=32,fs=260),E('emo',e='🧳',x=70,y=34,fs=240,at=5)]),
 ("Dos: por qué ahora. Con la ley de amnistía, el juez Llarena levantó en octubre la orden de detención en España.",[E('step',n=2),E('emo',e='📜',x=28,y=32,fs=260),E('stat',tx='ORDEN DE DETENCIÓN',sub='LEVANTADA · OCTUBRE 2026',x=66,y=34,w=560,h=230,fs=66,at=8)]),
 ("Tres: cuándo vuelve. No hay fecha confirmada. Él ha dicho que no será en campaña, y se habla del doce de diciembre.",[E('step',n=3),E('card',title='DICIEMBRE',lines=[{'a':'Fecha confirmada','b':'NO'},{'a':'¿Durante la campaña?','b':'NO'},{'a':'Fecha que se maneja','b':'12','hl':1}],x=50,y=34,w=800,h=420)]),
 ("Cuatro: qué pasará. El presidente del Parlament, Josep Rull, quiere darle una bienvenida oficial.",[E('step',n=4),E('por',who='parlament',x=50,y=30,w=900,h=560),E('emo',e='🚪',x=78,y=40,fs=220,at=6)]),
 ("¿Y tú? ¿Crees que su vuelta cambiará algo después del 29N? Te leo en comentarios.",[E('step',n=5),E('por',who='puigdemont',x=50,y=34,w=620,h=640),E('big',tx='¿Y TÚ?',x=50,y=58,fs=130)])],
 '2026-11-26T13:00:00+01:00','Puigdemont vuelve tras nueve años','Al Jazeera (6-10-2026), Demócrata (12-11-2026). Fotos: Wikimedia Commons (Parlament de Catalunya; Kent Wang, CC BY-SA 4.0)','#puigdemont #amnistia #29N',
 portada={'titulo':'Puigdemont *vuelve*','who':['puigdemont']})
V['slp_206_f3_cartel']=fmt('slp_206_f3_cartel','f3',[
 ("Arrancar este cartel electoral puede costarte muy caro.",[E('cartel',x=50,y=50,w=860,h=1000)]),
 ("Porque no es un cartel cualquiera.",[E('cartel',x=50,y=50,w=860,h=1000,glow=1)]),
 ("Durante las elecciones, cada ayuntamiento reserva espacios gratuitos para los carteles de los partidos.",[E('cartel',x=50,y=48,w=820,h=940,glow=1,ley='ley electoral',plate='AYUNTAMIENTO')]),
 ("Y la ley electoral los protege. Artículo ciento cuarenta y cuatro.",[E('card',title='LOREG · Artículo 144',lines=[{'a':'1. Serán castigados…'},{'a':'b) Infringir las normas legales'},{'a':'en materia de carteles','hl':1},{'a':'electorales y espacios reservados'}],x=50,y=48,w=860,h=560)]),
 ("Quien infrinja las normas sobre carteles y espacios reservados puede cometer un delito electoral.",[E('card',title='LOREG · Artículo 144',lines=[{'a':'b) Carteles electorales','hl':1}],x=50,y=44,w=820,h=260),E('stat',tx='DELITO ELECTORAL',x=50,y=60,w=640,h=140,fs=70,at=4,c='#E30613')]),
 ("La pena: de tres meses a un año de cárcel. O una multa de seis a veinticuatro meses.",[E('stat',tx='3 meses – 1 año',sub='de cárcel',x=50,y=40,w=760,h=220,fs=86),E('stat',tx='6 – 24 meses',sub='de multa',x=50,y=60,w=760,h=220,fs=86,at=9),E('emo',e='⛓️',x=86,y=30,fs=150)]),
 ("¿Y si no llega a delito? La Junta Electoral puede multarte igual.",[E('emo',e='⚖️',x=50,y=48,fs=420)]),
 ("Entre cien y mil euros si eres un particular. Lo dice el artículo ciento cincuenta y tres.",[E('emo',e='⚖️',x=50,y=40,fs=300),E('stat',tx='100 – 1.000 €',sub='LOREG, art. 153 · particulares',x=50,y=64,w=760,h=230,fs=96,at=2)]),
 ("Y da igual de qué partido sea el cartel. La ley es la misma para todos.",[E('cartel',x=50,y=50,w=820,h=940)]),
 ("Así que ese papel que no te gusta… mejor déjalo donde está. Sígueme para más leyes que nadie te cuenta.",[E('cartel',x=50,y=50,w=820,h=940,glow=1)])],
 '2026-11-26T14:30:00+01:00','Arrancar un cartel electoral puede costarte cárcel','Ley Orgánica 5/1985 del Régimen Electoral General (LOREG), arts. 144 y 153','#leyelectoral #29N #carteles',
 portada={'titulo':'Arrancar este cartel = *delito*','emo':'🪧','sello':'LOREG ART. 144'})
V['slp_207_f6_vox_alvise']=fmt('slp_207_f6_vox_alvise','f6',[
 ("¿Vox o Alvise? Te lo explico en un minuto. Se parecen mucho… pero no en todo.",[E('tape',tx='¿VOX O ALVISE?',x=50,y=17,fs=86),E('por',who='abascal',x=30,y=38,w=400,h=460,label='ABASCAL',rot=-5),E('por',who='alvise',x=70,y=38,w=400,h=460,label='ALVISE',rot=4),E('emo',e='🥊',x=50,y=27,fs=180)]),
 ("Según el comparador de Tu Papeleta, coinciden en veintisiete de treinta y dos temas.",[E('big',tx='COINCIDEN EN',x=50,y=17,fs=70),E('tape',tx='27 DE 32',x=50,y=24,fs=110),E('emo',e='🤝',x=50,y=45,fs=320)]),
 ("Los dos quieren expulsar a quien entró de forma irregular.",[E('big',tx='LOS DOS:',x=50,y=16,fs=70),E('tape',tx='INMIGRACIÓN',x=50,y=23,fs=100),E('emo',e='🚧',x=50,y=45,fs=320)]),
 ("Los dos: desalojar okupas en veinticuatro o cuarenta y ocho horas.",[E('big',tx='LOS DOS:',x=50,y=16,fs=70),E('tape',tx='VIVIENDA',x=50,y=23,fs=100),E('emo',e='🏠',x=40,y=44,fs=280),E('emo',e='🔒',x=66,y=50,fs=160,at=2),E('tape',tx='OKUPAS: FUERA EN 24-48 H',x=50,y=63,fs=56,rot=2)]),
 ("Los dos: bajar el IRPF y eliminar el impuesto de sucesiones.",[E('big',tx='LOS DOS:',x=50,y=16,fs=70),E('tape',tx='IMPUESTOS',x=50,y=23,fs=100),E('emo',e='🐷',x=38,y=44,fs=260),E('emo',e='💶',x=66,y=46,fs=200,at=3)]),
 ("Y los dos, contra la amnistía.",[E('big',tx='LOS DOS:',x=50,y=16,fs=70),E('tape',tx='AMNISTÍA',x=50,y=23,fs=100),E('emo',e='❌',x=50,y=45,fs=320)]),
 ("¿Diferencias? Pisos turísticos: Vox quiere restringirlos con fuerza. Alvise, no.",[E('tape',tx='DIFERENCIAS',x=50,y=16,fs=96),E('emo',e='🧳',x=50,y=36,fs=240),E('tape',tx='VOX: RESTRINGIR',x=50,y=52,fs=64,rot=-2,at=4),E('tape',tx='ALVISE: NO',x=50,y=60,fs=64,rot=2,at=8)]),
 ("Pensiones ligadas al IPC: según ese comparador, Alvise muy a favor y Vox en contra.",[E('tape',tx='PENSIONES',x=50,y=16,fs=96),E('emo',e='👵',x=50,y=36,fs=240),E('tape',tx='ALVISE: SÍ',x=50,y=52,fs=64,rot=-2,at=6),E('tape',tx='VOX: NO',x=50,y=60,fs=64,rot=2,at=9)]),
 ("Muy parecidos. Pero no iguales. ¿Y tú, con cuál te quedas? Te leo.",[E('tape',tx='¿Y A TI?',x=50,y=17,fs=100),E('por',who='abascal',x=30,y=40,w=380,h=440,label='ABASCAL',rot=-5),E('por',who='alvise',x=70,y=40,w=380,h=440,label='ALVISE',rot=4)])],
 '2026-11-26T16:00:00+01:00','¿Vox o Alvise? En qué se parecen y en qué no','Comparador Tu Papeleta (tupapeleta.es). Fotos: Wikimedia Commons (Gage Skidmore, CC BY-SA 2.0; Parlamento Europeo)','#vox #alvise #salf #29N',
 portada={'titulo':'¿Vox o *Alvise*?','who':['abascal','alvise']})
import json;json.dump(V,open('/tmp/claude-0/scr/vf.json','w'),ensure_ascii=False)
for k,v in V.items(): print(k,len(v))
