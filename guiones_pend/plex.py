import sys,json;sys.path.insert(0,'engine')
from mk_cine import *
V={}
E=lambda id,t,x=50,y=50,w=220:P(id,'emo',x=x,y=y,w=w,text=t,fs=int(w*1.1))
FS='elDiario.es, The Objective, Infobae, El Independiente (25-11-2026), canal de Plex'
SH=lambda txt:[E('eF','📤',50,40,300),BIG('bF',txt,'',color='gold',y=64,fs=130)]
V['slp_196_plex_lambo']=cine('slp_196_plex_lambo',[
 ("Sánchez entra en casa de Plex. Ve el coche aparcado. Y suelta esto: «Coño, pero si aquí hay un Lamborghini».",[E('e0','🏎️',50,40,340),BIG('b0','«PERO SI AQUÍ HAY UN LAMBORGHINI»','',color='gold',y=70,fs=72)],'noche'),
 ("Plex, con retranca: «Los que te gustan».",[mono('s1','sanchez',30,74,280,cara='risa'),BIG('b1','«LOS QUE TE GUSTAN»','PLEX',y=36,fs=100)],'dia'),
 ("Porque Sánchez había dicho que hacían falta «más transporte público y menos Lamborghinis». Y a Plex eso le sentó mal.",[E('e2','🚌',30,40,220),E('e2b','🏎️',70,40,220),XM('x2',y=40)],'rojo'),
 ("«¿Qué tiene que ver una cosa con la otra?», le pregunta.",[BIG('b3','¿QUÉ TIENE QUE VER?','',color='gold',y=46,fs=120)],'rojo'),
 ("Y Sánchez recula: «No, y tienes razón».",[mono('s4','sanchez',50,72,360,say='«Tienes razón»',cara='duda')],'dia'),
 ("«Lo que quise decir fue que estupendo que la gente tenga su Lambo si quiere».",[mono('s5','sanchez',72,74,300,cara='risa'),E('e5','✅',28,40,240)],None)],
 '2026-11-25T23:40:00+01:00','','«Pero si aquí hay un *Lamborghini*»','SÁNCHEZ x PLEX',FS,'#plex #sanchez #lamborghini',dias='cuatro',
 fin_bg='noche',fin_txt='Mándaselo a alguien que tenga un Lambo… o que lo sueñe. Y síguenos: mañana, debate a cuatro en directo.',fin_show=SH('MÁNDASELO'))
V['slp_197_plex_farsante']=cine('slp_197_plex_farsante',[
 ("¿Te acuerdas de cuando a Feijóo le cortaron el micro en pleno Congreso? Ahora, por fin, ha explicado qué quería decir.",[mono('f0','feijoo',50,72,340,cara='sorpresa'),E('e0','🎙️',50,32,240),XM('x0',y=32)],'noche'),
 ("Fue en noviembre del año pasado. Quiso soltar una frase preparada contra Sánchez, se trabó… y se quedó sin tiempo.",[BIG('b1','⏱️ 0:00','',color='red',y=44,fs=150)],'rojo'),
 ("Ahora, con Plex, lo cuenta: «No me fijé en el contador y yo quería decir Anatomía de un farsante».",[mono('f2','feijoo',50,72,360,say='«Anatomía de un farsante»',cara='risa')],'dia'),
 ("Sánchez aprovechó aquel día para decir que, entre sus virtudes, «no está el de ser un buen parlamentario».",[mono('s3','sanchez',50,72,340,cara='risa'),BIG('b3','ZASCA','',color='gold',y=34,fs=150)],None),
 ("La entrevista la grabaron en el circuito del Jarama. Con Feijóo subido al Porsche de Plex.",[E('e4','🏁',30,40,240),E('e4b','🏎️',70,44,260),BIG('b4','JARAMA','',y=70,fs=150)],'dia'),
 ("Un año después, el lapsus sigue persiguiéndole. Pero esta vez lo ha contado él.",[mono('f5','feijoo',50,72,360,cara='risa')],'duelo')],
 '2026-11-26T00:20:00+01:00','','«Anatomía de un *farsante*»','FEIJÓO x PLEX','El Independiente (25-11-2026), Infobae (26-11-2025), canal de Plex','#plex #feijoo #farsante',dias='cuatro',
 fin_bg='noche',fin_txt='Si te acordabas del micro cortado, compártelo. Y mañana, debate a cuatro en directo aquí.',fin_show=SH('COMPÁRTELO'))
V['slp_198_plex_andorra']=cine('slp_198_plex_andorra',[
 ("Plex tiene quince millones de suscriptores. Podría irse a Andorra. Y no lo ha hecho.",[BIG('b0','15 M','SUSCRIPTORES',color='gold',y=40,fs=180),E('e0','🇦🇩',50,70,200),XM('x0',y=70)],'noche'),
 ("Y Sánchez se lo agradece: «Soy muy fan de Andorra, pero de vacaciones, no para vivir».",[mono('s1','sanchez',50,72,360,say='«De vacaciones, no para vivir»',cara='risa')],'dia'),
 ("Su argumento: «Si el triunfo y el éxito lo logran en España principalmente, pues es bueno quedarse aquí y pagar impuestos».",[mono('s2','sanchez',28,74,300,cara='neutral'),BIG('b2','QUEDARSE','Y PAGAR AQUÍ',y=38,fs=140)],None),
 ("Y le echa un piropo: «Dice mucho de ti el que digas: no solamente pago impuestos, sino que los quiero pagar aquí en España».",[E('e3','💶',50,40,260),BIG('b3','«DICE MUCHO DE TI»','',color='gold',y=68,fs=100)],'dia'),
 ("Pero Plex no se lo compra del todo: cree que «los impuestos a veces no están bien utilizados».",[BIG('b4','«NO ESTÁN BIEN UTILIZADOS»','PLEX',color='red',y=46,fs=86)],'rojo'),
 ("O sea: los dos de acuerdo en pagar aquí. En qué se hace con ese dinero… ya no tanto.",[mono('s5','sanchez',50,72,340,cara='duda'),E('e5','🤷',50,32,220)],'duelo')],
 '2026-11-26T01:00:00+01:00','','«Andorra, de *vacaciones*»','SÁNCHEZ x PLEX',FS,'#plex #sanchez #andorra #impuestos',dias='cuatro',
 fin_bg='noche',fin_txt='Mándaselo al colega que siempre dice que se va a Andorra. Y síguenos.',fin_show=SH('MÁNDASELO'))
V['slp_199_plex_lambo_porsche']=cine('slp_199_plex_lambo_porsche',[
 ("Un Lamborghini. Un Porsche. Y los dos candidatos a presidente, en casa del mismo youtuber.",[E('e0','🏎️',30,40,260),E('e0b','🏁',70,40,260),BIG('b0','LAMBO','VS PORSCHE',color='gold',y=70,fs=150)],'noche'),
 ("Plex: veinticuatro años, quince millones de suscriptores. Y la noche antes del debate, sus dos entrevistas, una detrás de otra.",[BIG('b1','20:00','SÁNCHEZ',y=36,fs=150),BIG('b1b','21:00','FEIJÓO',color='gold',y=60,fs=150)],None),
 ("Sánchez fue a su casa de la sierra. Y empezó con el Lamborghini aparcado en la puerta.",[mono('s2','sanchez',50,72,360,say='«Si aquí hay un Lamborghini»',cara='risa')],'dia'),
 ("Feijóo fue al circuito del Jarama. Casco puesto, y vueltas en el Porsche de Plex.",[mono('f3','feijoo',50,72,360,cara='risa'),E('e3','🪖',50,32,220)],'dia'),
 ("Ni mitin, ni atril, ni debate. Lo que buscan los dos es lo mismo: tu voto, si tienes menos de treinta.",[E('e4','📱',50,44,300),BIG('b4','VOTO JOVEN','',color='gold',y=72,fs=130)],'rojo'),
 ("Y Plex dice que no quiere decirte a quién votar. Solo enseñarte cómo son cuando se apagan las cámaras de la tele.",[mono('s5','sanchez',26,72,280,cara='neutral'),mono('f5','feijoo',74,72,280,cara='neutral')],'duelo')],
 '2026-11-26T07:00:00+01:00','','*Lambo* vs Porsche','PLEX','El Independiente, Demócrata, Hola (24/25-11-2026)','#plex #sanchez #feijoo',dias='cuatro',
 fin_bg='noche',fin_txt='¿Quién salió mejor con Plex? Dímelo abajo. Y esta noche, debate a cuatro en directo.',fin_show=[BIG('bF','¿QUIÉN SALIÓ','',color='gold',y=34,fs=130),BIG('bG','MEJOR?','',y=48,fs=150),E('eF','🤔',50,72,220)])
V['slp_200_plex_sanchez_personal']=cine('slp_200_plex_sanchez_personal',[
 ("En 2011 Pedro Sánchez se quedó fuera del Congreso. Y con Plex ha contado quién sostuvo a su familia.",[BIG('b0','2011','FUERA DEL CONGRESO',color='gold',y=44,fs=190)],'noche'),
 ("«Ella fue la que sostuvo la familia entonces». Habla de Begoña Gómez.",[mono('s1','sanchez',50,72,360,say='«Ella sostuvo la familia»',cara='neutral')],'dia'),
 ("Más cosas que no sabías: hace ciclismo de enduro. Y con el casco puesto, dice, nadie le reconoce.",[E('e2','🚵',50,44,320)],'dia'),
 ("Plex le explica el GTA seis. Y Sánchez pregunta: «¿No da un poco de miedo que no haya reglas, que puedas ser lo que quieras y hacer lo que quieras?».",[E('e3','🎮',50,40,280),BIG('b3','¿SIN REGLAS?','',color='red',y=70,fs=130)],'rojo'),
 ("Y sobre la política, una confesión: le da pena que los jóvenes piensen que sus políticos «lo único que hacen es discutir».",[mono('s4','sanchez',50,72,340,cara='duda'),BIG('b4','DISCUTIR','',y=34,fs=150)],None),
 ("Curioso, dicho por alguien que esta noche se sube a un debate a cuatro.",[mono('s5','sanchez',50,72,340,cara='risa'),E('e5','🥊',50,32,220)],'duelo')],
 '2026-11-26T07:45:00+01:00','','Sánchez, sin *corbata*','SÁNCHEZ x PLEX',FS,'#plex #sanchez #gta',dias='cuatro',
 fin_bg='noche',fin_txt='¿Te ha sorprendido algo? Compártelo. Y esta noche, debate a cuatro en directo.',fin_show=SH('COMPÁRTELO'))
V['slp_201_plex_desafeccion']=cine('slp_201_plex_desafeccion',[
 ("Un youtuber de veinticuatro años le dice al presidente lo que muchos jóvenes piensan. Y no se corta.",[E('e0','🎙️',50,42,300),BIG('b0','SIN FILTRO','',color='gold',y=72,fs=140)],'noche'),
 ("Sobre la DANA, Plex le reprocha que los partidos «se echaran las culpas unos a otros».",[BIG('b1','DANA','',color='red',y=40,fs=180),E('e1','👉👈',50,66,220)],'rojo'),
 ("Sánchez, sobre las broncas políticas, dice que la democracia «también es el contraste de posiciones». «Es sano que haya unos que defiendan una cosa, otros que defiendan otra».",[mono('s2','sanchez',50,72,360,say='«Es sano»',cara='neutral')],'dia'),
 ("Pero admite: «Lo malo es que después de esa discusión no se pueda llegar a un acuerdo».",[mono('s3','sanchez',28,74,300,cara='duda'),BIG('b3','SIN ACUERDO','',y=38,fs=130)],None),
 ("Y Plex lo remata: hay que contribuir, sí, pero «los impuestos a veces no están bien utilizados».",[BIG('b4','«NO ESTÁN BIEN UTILIZADOS»','',color='gold',y=46,fs=86)],'rojo'),
 ("Quince millones de suscriptores escuchando a uno de los suyos decirle eso al presidente. Eso también es campaña.",[BIG('b5','15 M','',color='gold',y=40,fs=180),mono('s5','sanchez',50,76,300,cara='duda')],'duelo')],
 '2026-11-26T09:15:00+01:00','','Plex, *sin filtro*','SÁNCHEZ x PLEX',FS,'#plex #sanchez #dana',dias='cuatro',
 fin_bg='noche',fin_txt='Mándaselo a quien diga que los políticos solo discuten. Y esta noche, debate a cuatro en directo.',fin_show=SH('MÁNDASELO'))
json.dump(V,open('/tmp/claude-0/scr/vplex.json','w'),ensure_ascii=False)
for k,v in V.items(): print(k,len(v))
