import sys,json;sys.path.insert(0,'engine')
from mk_cine import *
V={}
CUA=lambda p,y=70,w=200:[mono(p+'s','sanchez',14,y,w,cara='neutral'),mono(p+'f','feijoo',38,y,w,cara='neutral'),mono(p+'a','abascal',62,y,w,cara='neutral'),mono(p+'c','colau',86,y,w,cara='neutral')]
# LUN 23:00
V['slp_178_tres_frases']=cine('slp_178_tres_frases',[
 ("Faltan seis días. Y en los mítines ya casi no se habla de propuestas. Se habla de esto.",[BIG('b0','3 FRASES','3 MÍTINES',color='gold',y=50)],'noche'),
 ("Abascal, este domingo en Alicante. Llamó al Gobierno «mafia».",[mono('a1','abascal',50,72,360,say='«Mafia»',cara='enfado')],'rojo'),
 ("Y dijo que los números del Gobierno «son mentira» porque nunca llegan a las familias.",[mono('a2','abascal',30,74,300,cara='enfado'),BIG('b2','«MENTIRA»','ABASCAL · ALICANTE',y=36,fs=150)],'rojo'),
 ("Feijóo, en Galicia, lo resumió así: «De Ábalos a Puente y siempre Sánchez».",[mono('f3','feijoo',50,72,360,say='«Y siempre Sánchez»',cara='neutral')],'dia'),
 ("Y Sánchez, en Tarragona: «Si el 29N votamos en masa, mandamos a casa a Feijóo y a Abascal».",[mono('s4','sanchez',50,72,360,say='«Mandamos a casa a Feijóo y a Abascal»',cara='risa')],None),
 ("¿Te has fijado? Dos apuntan a Sánchez. Y Sánchez apunta a los dos.",[mono('a5','abascal',18,72,250,cara='enfado'),mono('s5','sanchez',50,72,250,cara='duda'),mono('f5','feijoo',82,72,250,cara='neutral'),BIG('b5','2 VS 1','',color='gold',y=36,fs=170)],'duelo'),
 ("El jueves, por primera vez en esta campaña, se lo dirán a la cara. Con Colau en medio.",CUA('c6'),'noche')],
 '2026-11-23T23:00:00+01:00','¿Qué frase te convence más? Comenta 1, 2 o 3.','3 frases, 3 *mítines*','2 VS 1','Moncloa.com (22-11), Demócrata (14-11), Diari de Tarragona (7-11)','#abascal #feijoo #sanchez',dias='seis')
# MAR 23:00
V['slp_179_voto_soria']=cine('slp_179_voto_soria',[
 ("Tu voto no vale lo mismo en Soria que en Madrid. Y es legal.",[MED('m0','SORIA','MADRID',f=1,y=58)],'noche'),
 ("En el Congreso hay 350 escaños. Y se reparten por provincias.",[HEMI('h1',[{'l':'ESCAÑOS','n':350,'c':'#F5B700'}],y=50)],'noche'),
 ("Pero la ley da a cada provincia un mínimo de dos diputados, tenga la gente que tenga.",[BIG('b2','2','MÍNIMO POR PROVINCIA',color='gold',y=50)],None),
 ("Madrid elige 38 este año. Uno más que en 2023.",[BIG('b3','38','ESCAÑOS EN MADRID',y=50)],'dia'),
 ("Soria, con unas noventa mil personas, elige dos.",[BIG('b4','2','ESCAÑOS EN SORIA',color='gold',y=50)],'dia'),
 ("Resultado: en Madrid hay casi cuatro veces más votantes por cada escaño que en Soria.",[BIG('b5','×4','VOTANTES POR ESCAÑO',color='gold',y=50)],'rojo'),
 ("Por eso los partidos pelean las provincias pequeñas voto a voto. Allí, un puñado decide un escaño.",[BIG('b6','💺','UN PUÑADO DE VOTOS',y=50)],None)],
 '2026-11-24T23:00:00+01:00','¿Te parece justo? Comenta sí o no.','Tu voto no vale *igual*','SORIA ≠ MADRID','LOREG art. 162; Demócrata (escaños 2026); INE, censo electoral','#escaños #soria #madrid',dias='cinco')
# MIE 09:00
V['slp_180_correo_hoy']=cine('slp_180_correo_hoy',[
 ("Si pediste el voto por correo y todavía no lo has mandado: es hoy.",[BIG('b0','HOY','ÚLTIMO DÍA',color='gold',y=50)],'rojo'),
 ("Hoy, miércoles 25, es el último día para entregarlo en Correos.",[BIG('b1','25-N','ÚLTIMO DÍA EN CORREOS',y=50)],'noche'),
 ("Lo llevas tú en persona a una oficina, con tu DNI.",[mono('m2','tu',50,72,320,cara='risa')],None),
 ("Y ojo: si lo pediste, el domingo ya no puedes votar en tu colegio.",[XM('x3',y=52),BIG('b3','🚫','',y=80)],'rojo'),
 ("Si no lo mandas hoy, tu voto se pierde.",[BIG('b4','VOTO PERDIDO','',y=50,fs=105)],'noche')],
 '2026-11-25T09:00:00+01:00','¿Ya lo has mandado? Comenta sí o no.','Voto por correo: es *hoy*','ÚLTIMO DÍA','LOREG art. 73; Correos','#votoporcorreo #29N',dias='cuatro')
# MIE 14:00
V['slp_181_quien_colau']=cine('slp_181_quien_colau',[
 ("Mañana hay cuatro en el debate. Y la cuarta no es quien muchos esperaban.",CUA('c0'),'noche'),
 ("Ada Colau. Exalcaldesa de Barcelona. La primera mujer en serlo.",[mono('c1','colau',50,72,360,cara='risa'),BIG('b1','2015','PRIMERA ALCALDESA',color='gold',y=34,fs=150)],None),
 ("Antes fue portavoz de la Plataforma de Afectados por la Hipoteca. La de los desahucios.",[mono('c2','colau',28,78,280),EDI('e2',y=40,w=520)],'dia'),
 ("Gobernó Barcelona ocho años, hasta 2023.",[BIG('b3','8 AÑOS','ALCALDESA 2015-2023',y=50)],None),
 ("En octubre la eligieron candidata de Frente Amplio: Sumar, Izquierda Unida, Más Madrid y los Comuns.",[BIG('b4','FRENTE AMPLIO','SUMAR · IU · MÁS MADRID · COMUNS',color='gold',y=50,fs=140)],'noche'),
 ("Podemos no está dentro. Va por su cuenta.",[XM('x5',y=50)],'rojo'),
 ("Y mañana, por primera vez, estará en un debate frente a Sánchez, Feijóo y Abascal a la vez.",CUA('c6'),'duelo')],
 '2026-11-25T14:00:00+01:00','¿La conocías? Comenta sí o no.','¿Quién es la *cuarta*?','COLAU','Euronews (13-11-2026)','#colau #frenteamplio #debate',dias='cuatro')
# MIE 20:00
V['slp_182_abascal_sanchez']=cine('slp_182_abascal_sanchez',[
 ("Mañana Abascal y Sánchez estarán a unos metros. Esto es lo que se han dicho esta campaña.",[mono('a0','abascal',28,72,300,cara='neutral'),mono('s0','sanchez',72,72,300,cara='neutral')],'duelo'),
 ("Abascal, sobre el Gobierno: «mafia».",[mono('a1','abascal',50,72,360,say='«Mafia»',cara='enfado')],'rojo'),
 ("Y sobre la vivienda: «totalmente inaccesible para la juventud».",[mono('a2','abascal',26,74,300,cara='enfado'),EDI('e2',y=52,w=520)],'rojo'),
 ("Sánchez, en Tarragona: «Si el 29N votamos en masa, mandamos a casa a Feijóo y a Abascal».",[mono('s3','sanchez',50,72,360,say='«Mandamos a casa a Feijóo y a Abascal»',cara='risa')],'dia'),
 ("Y: «La mejor receta contra la involución se llama movilización».",[mono('s4','sanchez',74,74,300,cara='risa'),BIG('b4','MOVILIZACIÓN','',color='gold',y=40,fs=130)],'dia'),
 ("Uno habla de mafia. El otro de mandarle a casa. Y mañana, cara a cara, con Feijóo y Colau en medio.",CUA('c5'),'duelo')],
 '2026-11-25T20:00:00+01:00','¿Quién crees que saldrá más fuerte? Comenta.','Abascal vs *Sánchez*','MAÑANA 22:00','Moncloa.com (22-11), Diari de Tarragona (7-11)','#abascal #sanchez #debate',dias='cuatro')
# MIE 23:00
V['slp_183_guia_debate4']=cine('slp_183_guia_debate4',[
 ("Mañana a las diez de la noche, los cuatro, en el mismo plató. Por primera vez en esta campaña.",CUA('c0'),'noche'),
 ("Lo organiza la Academia de la Televisión. Lo dan Telecinco y Cuatro, y cualquier cadena que quiera.",[BIG('b1','22:00','JUEVES 26 · TELECINCO · CUATRO',color='gold',y=50)],None),
 ("Cinco bloques: vivienda, economía, servicios públicos, corrupción, e inmigración y política exterior.",[BIG('b2','5','BLOQUES',y=50)],'dia'),
 ("Y el orden de palabra se sortea allí mismo, con los cuatro delante.",[BIG('b3','🎲','SORTEO EN DIRECTO',y=50)],None),
 ("¿Podemos? Fuera. La Junta Electoral dijo que no tiene derecho a estar.",[XM('x4',y=50),BIG('b4','JUNTA ELECTORAL','',y=82,fs=110)],'rojo'),
 ("Y aquí lo tendrás en directo: los mejores momentos, mientras pasan.",[BIG('b5','EN DIRECTO','@POLITIZATEHOY',color='gold',y=50,fs=140)],'noche')],
 '2026-11-25T23:00:00+01:00','¿Lo vas a ver? Comenta sí o no.','Debate a *cuatro*: guía','JUEVES 22:00','Periódico de Ibiza (20-11), Doble Lectura (21-11), El Español (17-11)','#debate #29N',dias='cuatro')
json.dump(V,open('/tmp/claude-0/scr/voces_lunmie.json','w'),ensure_ascii=False)
for k,v in V.items(): print(k, len(json.dumps(v)))
