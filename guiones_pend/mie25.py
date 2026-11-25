import sys,json;sys.path.insert(0,'engine')
from mk_cine import *
V={}
E=lambda id,t,x=50,y=50,w=220:P(id,'emo',x=x,y=y,w=w,text=t,fs=int(w*1.1))
V['slp_194_escanes']=cine('slp_194_escanes',[
 ("Una influencer dice a quién va a votar. Y después abre los mensajes.",[E('e0','📱',50,46,300),BIG('b0','«BUENOS DÍAS, SUPONGO»','',color='gold',y=74,fs=90)],'noche'),
 ("Laura Escanes anunció en TikTok que votará al PSOE. Con un baile y una canción hecha con IA.",[E('e1','🎵',30,40,240),BIG('b1','PSOE','SU VOTO',y=62,fs=170)],None),
 ("Sánchez lo comentó: «¡Vamos, chicos!».",[mono('s2','sanchez',50,72,360,say='«¡Vamos, chicos!»',cara='risa')],'dia'),
 ("Y luego llegaron los mensajes privados. Ella los ha publicado: deseos de muerte, y hasta uno contra su hija.",[E('e3','⚠️',50,40,280),SELLO('s3','AMENAZAS',y=70)],'rojo'),
 ("A quienes la criticaban ya les había dicho: «Se me lincha por decir que apoyo a un partido progresista».",[BIG('b4','«SE ME LINCHA»','',color='gold',y=46,fs=130)],'rojo'),
 ("Y no ha sido la única famosa en mojarse. María Pombo apoyó un post que llamaba a los votantes del PSOE «un par de escalones por debajo de la mayoría de edad intelectual y ética».",[E('e5','🔥',50,44,260),BIG('b5','INFLUENCERS','EN CAMPAÑA',y=70,fs=140)],'duelo'),
 ("Opinar, criticar, discrepar: vale. Pero amenazar a alguien por decir a quién vota…",[XM('x6',y=46),BIG('b6','¿HASTA AQUÍ?','',color='gold',y=76,fs=130)],'noche')],
 '2026-11-25T14:00:00+01:00','Mándaselo a alguien que diga que «la política no le afecta».','Le *amenazan* por su voto','AMENAZAS','Bilbao Hiria (25-11-2026)','#lauraescanes #29N #redes',dias='cuatro',
 fin_bg='noche',fin_txt='Mándaselo a quien diga que la política no va con él. Y síguenos: el jueves, debate a cuatro en directo.',fin_show=[E('eF','📤',50,40,300),BIG('bF','MÁNDASELO','A QUIEN LO NECESITE',color='gold',y=66,fs=140)])
V['slp_195_guerra_tiktok']=cine('slp_195_guerra_tiktok',[
 ("Sánchez tiene en TikTok cuatro veces más seguidores que su propio partido.",[BIG('b0','×4','SÁNCHEZ VS PSOE EN TIKTOK',color='gold',y=46,fs=220)],'noche'),
 ("Él: un millón trescientos mil. El PSOE: trescientos veinticinco mil.",[mono('s1','sanchez',30,72,280,cara='risa'),BIG('b1','1,3 M','',y=34,fs=150),BIG('b1b','325.000','PSOE',y=56,fs=110)],None),
 ("En Vox pasa al revés. La cuenta del partido suma casi cincuenta y cinco millones de visualizaciones. La de Abascal, la mitad.",[mono('a2','abascal',70,72,280,cara='neutral'),BIG('b2','54,8 M','VOX',color='gold',y=34,fs=140)],'rojo'),
 ("¿Y la reina de las visualizaciones? Irene Montero. Veinticuatro veces más que Podemos.",[BIG('b3','×24','MONTERO VS PODEMOS',color='gold',y=46,fs=220)],'dia'),
 ("Y el PP ha ido más lejos: un vídeo con IA que pone voces de Begoña Gómez, Ábalos y Zapatero diciendo cosas que nunca dijeron.",[E('e4','🤖',50,40,300),SELLO('s4','IA',y=68)],'rojo'),
 ("Begoña Gómez lo ha denunciado.",[SELLO('s5','DENUNCIA',y=50)],'rojo'),
 ("Esta campaña no se juega solo en los mítines. Se juega en tu móvil. Y eso que estás viendo ahora… también cuenta.",[E('e6','📱',50,46,320)],'noche')],
 '2026-11-25T17:00:00+01:00','¿Qué cuenta de político sigues tú?','La guerra de *TikTok*','×24','Euronews (25-11-2026)','#tiktok #sanchez #vox #montero',dias='cuatro',
 fin_bg='duelo',fin_txt='Si te ha sorprendido, compártelo. Y mañana, debate a cuatro en directo aquí.',fin_show=[E('eF','📤',50,40,300),BIG('bF','COMPÁRTELO','',color='gold',y=64,fs=150)])
json.dump(V,open('/tmp/claude-0/scr/v25.json','w'),ensure_ascii=False)
print(json.dumps(list(V.values()),ensure_ascii=False))
