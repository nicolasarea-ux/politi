import sys,json;sys.path.insert(0,'engine')
from mk_cine import *
# Pasada del 26-N (disparada a las 17:18): franjas del 28-N, jornada de reflexión -> solo contenido práctico sobre cómo votar.
FIN28="Síguenos: mañana se vota."
def fix(id):
    g=json.load(open(f'guiones/{id}.json'))
    g['caption']=g['caption'].replace('⏳ Quedan uno días para el 29-N. Síguenos: cada día, la campaña explicada.','🗳️ Mañana, 29-N, se vota de 9:00 a 20:00. Síguenos: te lo contamos todo.')
    json.dump(g,open(f'guiones/{id}.json','w'),ensure_ascii=False,indent=1)
V={}
V['slp_220_reflexion_hoy']=cine('slp_220_reflexion_hoy',[
 ("Hoy ningún partido puede pedirte el voto. Ni uno. ¿Por qué?",[BIG('b0','0','MÍTINES HOY',color='red',y=38,fs=220),XM('x0',y=68,w=280)],'rojo'),
 ("Es la jornada de reflexión. La campaña acabó anoche a las doce.",[BIG('b1','00:00','FIN DE LA CAMPAÑA',color='gold',y=40,fs=180),P('u1','urna',y=70,w=280)],'noche'),
 ("Desde entonces, ni mítines, ni actos, ni propaganda electoral hasta que se vote.",[SELLO('s2','PROHIBIDO',y=40),mono('m2','tu',50,76,240,cara='sorpresa')],None),
 ("Y encuestas, tampoco: no se pueden publicar hasta que cierren los colegios mañana a las ocho.",[BIG('b3','20:00','SIN ENCUESTAS HASTA',color='red',y=42,fs=180)],'dia'),
 ("Pero la prohibición es para la campaña. Tú puedes seguir hablando de política con quien quieras.",[MED('md4','TÚ SÍ PUEDES','HABLAR DE POLÍTICA',y=46),P('e4','emo',x=50,y=72,w=200,text='🗣️')],'duelo')],
 '2026-11-28T09:00:00+01:00','¿Sirve de algo la jornada de reflexión? Comenta sí o no.','Hoy *nadie* pide el voto','REFLEXIÓN','LOREG (arts. 51, 53 y 69.7)','#jornadadereflexion #votar',dias='uno',fin_txt="¿Sirve de algo la jornada de reflexión? Comenta sí o no. "+FIN28,
 fin_bg='noche',fin_show=[BIG('bF','¿SIRVE','DE ALGO?',color='gold',y=40,fs=150),P('eF','emo',x=50,y=70,w=220,text='🤔')])
V['slp_221_dni_movil']=cine('slp_221_dni_movil',[
 ("¿Puedes ir a votar mañana solo con el móvil? Sí. Pero ojo.",[BIG('b0','📱','¿SOLO CON EL MÓVIL?',y=40,fs=230)],'rojo'),
 ("La Junta Electoral Central aceptó el DNI digital de la app MiDNI el cinco de noviembre.",[BIG('b1','5-N','LA JUNTA ELECTORAL LO ACEPTA',color='gold',y=42,fs=190),SELLO('s1','MiDNI',y=70)],'noche'),
 ("Hubo un recurso. Y el Tribunal Supremo lo avaló el veinticuatro de noviembre.",[BIG('b2','24-N','EL SUPREMO LO AVALA',color='gold',y=42,fs=190)],None),
 ("En la mesa enseñas un código QR temporal y lo comprueban con un lector.",[BIG('b3','QR','LO ESCANEA LA MESA',y=40,fs=230),P('u3','urna',y=72,w=260)],'dia'),
 ("También valen el DNI físico, el pasaporte o el carné de conducir, con tu foto.",[MED('md4','DNI · PASAPORTE','CARNÉ DE CONDUCIR',y=44),mono('m4','tu',50,78,220,cara='sonrie')],None),
 ("Fotocopias, no. ¿Y si el móvil se queda sin batería? Llévate también el físico.",[XM('x5',y=40,w=260),BIG('b5','🔋','',y=70,fs=160)],'duelo')],
 '2026-11-28T14:00:00+01:00','¿Votarás con el móvil? Comenta sí o no.','¿Votar con el *móvil*?','MiDNI','Ministerio del Interior; Maldita.es (11-11-2026); Público y elEconomista (24-11-2026, Supremo); LOREG art. 85','#dnidigital #midni #votar',dias='uno',fin_txt="¿Votarás con el móvil? Comenta sí o no. "+FIN28,
 fin_bg='noche',fin_show=[BIG('bF','¿MÓVIL','O FÍSICO?',color='gold',y=40,fs=150),P('eF','emo',x=50,y=70,w=220,text='📱')])
V['slp_222_mesa_manana']=cine('slp_222_mesa_manana',[
 ("¿Te ha tocado mesa mañana y piensas no ir? Cuidado: no es como una multa de tráfico.",[BIG('b0','¿NO VAS?','',color='red',y=38,fs=160),XM('x0',y=66,w=280)],'rojo'),
 ("Si no vas sin una causa justificada, la ley electoral lo castiga como delito.",[SELLO('s1','DELITO',y=38),BIG('b1','⚖️','',y=66,fs=180)],'noche'),
 ("De tres meses a un año de prisión. O una multa de seis a veinticuatro meses.",[BIG('b2','1 AÑO','DE PRISIÓN, COMO MÁXIMO',color='red',y=42,fs=180)],None),
 ("Tienes que estar a las ocho de la mañana. Presidente, dos vocales y sus suplentes.",[BIG('b3','8:00','DOMINGO 29',color='gold',y=40,fs=200),mono('m3','tu',50,78,220,cara='sorpresa')],'dia'),
 ("A cambio, cobras setenta y cinco euros. Y si te surge una causa de fuerza mayor, avisa y justifícalo ante la Junta Electoral de Zona.",[BIG('b4','75 €','POR EL DÍA',color='gold',y=42,fs=200)],'duelo')],
 '2026-11-28T20:00:00+01:00','¿Te ha tocado alguna vez? Comenta sí o no.','Mesa *mañana*','MESA','LOREG (arts. 27, 80 y 143) y BOE-A-2026-13948 (dieta de 75 €)','#mesaelectoral #votar',dias='uno',fin_txt="¿Te ha tocado alguna vez? Comenta sí o no. "+FIN28,
 fin_bg='noche',fin_show=[BIG('bF','¿TE HA','TOCADO?',color='gold',y=40,fs=150),P('eF','emo',x=50,y=70,w=220,text='🗳️')])
V['slp_223_blanco_nulo']=cine('slp_223_blanco_nulo',[
 ("Blanco, nulo o quedarte en casa. Mañana no es lo mismo. Y casi nadie sabe por qué.",[BIG('b0','⬜ 🚫 🏠','',y=40,fs=170)],'rojo'),
 ("Voto en blanco: el sobre del Congreso, vacío. Cuenta como voto válido.",[BIG('b1','BLANCO','= VOTO VÁLIDO',color='gold',y=40,fs=170),P('u1','urna',y=72,w=260)],'noche'),
 ("Y por eso sube el listón del tres por ciento que necesita cada partido en tu provincia.",[BIG('b2','3 %','EL LISTÓN SUBE',color='red',y=42,fs=200)],None),
 ("Voto nulo: papeleta tachada o con algo escrito, o dos de partidos distintos en el sobre. No cuenta para nada.",[BIG('b3','NULO','NO CUENTA',color='red',y=40,fs=180),XM('x3',y=70,w=240)],'dia'),
 ("¿Y la abstención? Ni entra en el recuento. Mañana se vota de nueve de la mañana a ocho de la tarde.",[BIG('b4','9:00–20:00','DOMINGO 29',color='gold',y=42,fs=120),mono('m4','tu',50,78,220,cara='duda')],'duelo')],
 '2026-11-28T23:00:00+01:00','¿Has votado alguna vez en blanco? Comenta sí o no.','¿Blanco o *nulo*?','BLANCO','LOREG (arts. 84, 96 y 163)','#votoenblanco #votonulo #votar',dias='uno',fin_txt="¿Has votado alguna vez en blanco? Comenta sí o no. "+FIN28,
 fin_bg='noche',fin_show=[BIG('bF','¿BLANCO','O NULO?',color='gold',y=40,fs=150),P('eF','emo',x=50,y=70,w=220,text='🗳️')])
for k in V: fix(k)
json.dump(V,open('guiones_pend/voces_jue26_pasada.json','w'),ensure_ascii=False,indent=1)
for k,v in V.items(): print(k,len(v.split()),'|',v)
