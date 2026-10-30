# Rutina diaria de Politízate Hoy (@politizatehoy)

Canal de TikTok (y después Reels y Shorts) de actualidad política explicada, centrado en las elecciones generales del 29-N.
Nicks quiere que todo sea automático: esta rutina investiga, escribe, pone voz, renderiza y programa los vídeos sin que él toque nada.
Plan editorial completo: https://claude.ai/artifact/EpGu7vKZV4ok4vE6ARonrp

Datos fijos
- Repo público `nicolasarea-ux/politi`, rama `main`. Zona horaria `Europe/Madrid`.
- URL pública de un vídeo: `https://raw.githubusercontent.com/nicolasarea-ux/politi/main/videos/<id>.mp4`
- La rutina necesita el ordenador de Nicks (Windows, "nicolaptop") encendido con la app de Claude abierta: la voz se saca de Clipchamp y la subida se hace en TikTok Studio. **Usa su Chrome (extensión Claude in Chrome, `mcp__claude-in-chrome__*`), no el navegador integrado: Nicks no se fía del integrado.** Si Clipchamp o TikTok piden iniciar sesión, para y avisa. Carpeta compartida: `C:\Users\nicol\Downloads`.
- Si el ordenador no responde: deja los guiones escritos, anótalo en `registro.md` y avisa a Nicks. TikTok Studio permite programar hasta 10 días, así que la rutina siempre deja **hoy, mañana y pasado** cubiertos: un día caído no deja huecos.

## Ritmo (no subir sin datos)
| Fechas | Vídeos/día | Horas (Madrid) |
| --- | --- | --- |
| 30-O → 5-N | 3 | 13:30, 19:30, 22:00 |
| 6-N → 12-N | 5 | 8:30, 13:30, 19:30, 21:00, 22:30 |
| 13-N → 29-N | 6 | 8:30, 12:30, 14:30, 19:30, 21:00, 22:30 |
| Picos: 11-N, 13-N, días de debate, 19-N, 25-N, 29-N | 10 | 8:30, 10:30, 12:30, 14:00, 16:00, 18:00, 19:30, 20:45, 21:45, 23:00 |

Mínimo 1 h entre vídeos. Lección de @fichalo.app: pasar a 12/día hundió el alcance y Meta bloqueó la API. Si las visitas medias por vídeo caen más de un 30 % al subir volumen, baja al ritmo anterior y anótalo.

## Pasada diaria: 10:31 (hora a la que Nicks garantiza el ordenador encendido)
Hay **una sola pasada al día**, a las 10:31. Tiene que dejar hechos y programados TODOS los vídeos de hoy (franjas después de las 10:31), mañana y pasado, incluidas las franjas de mañana antes de las 10:31. Lo que pase después de la pasada se cubre al día siguiente: prioriza lo de las últimas 24 h.

**Regla de frescura (Nicks, 30-O): la actualidad caduca.**
- Vídeos de **actualidad** (noticias, frases, entrevistas, encuestas): SOLO para las franjas de hoy y, como mucho, la de primera hora de mañana. Nunca programes una noticia para dentro de 2 días.
- Franjas de **mañana y pasado**: solo vídeos **atemporales** (cómo votar, explicadores como D'Hondt o la investidura, quién es quién, qué propone cada partido sobre un tema). Márcalos en `cola.json` con `"tipo": "atemporal"`.
- En cada pasada, las franjas de hoy que tengan un atemporal programado se **sustituyen por actualidad** si el radar da temas con gancho ≥ 4. El atemporal sustituido vuelve a `cola.json` como `reserva` (se reutiliza otro día) y se quita de `publicaciones.json`.
- Un vídeo de actualidad que no llegó a publicarse y tiene más de 24 h se marca `caducado` y no se publica.

**Reparto diario (Nicks, 30-O): 2/3 actualidad, 1/3 atemporal.** Con 3/día: 13:30 actualidad · 19:30 atemporal · 22:00 actualidad (la más fuerte del día). Con 5–6/día se mantiene la proporción (las franjas de mañana y tarde-noche para actualidad, una o dos intermedias para atemporales). Si hay un evento muy grande (p. ej. entrevistas de Jordi Wild, un debate), todas las franjas del día pueden ser de actualidad.

**Qué prepara cada pasada de las 10:31:**
1. Actualidad de HOY para sus franjas de actualidad (sustituyendo los atemporales de relleno que hubiera).
2. El atemporal de HOY ya debería estar hecho de antes; si no, se hace.
3. MAÑANA y PASADO: todas sus franjas con atemporales (los de las franjas de actualidad son relleno de seguridad por si el ordenador está apagado; la pasada de ese día los cambia por noticias y vuelven a `reserva`).
4. Mantén siempre al menos 6 atemporales en `reserva` listos para reutilizar.

## Peticiones de Nicks
Antes del radar, lee `peticiones.md`. Lo que Nicks pida para un día concreto manda sobre el reparto base y sobre el radar.

## Radar de actualidad (lo primero en CADA pasada)
Nicks quiere que el canal vaya **en tiempo real**: el plan es la base, pero manda lo que esté pasando y tenga gancho en internet.
1. Busca (WebSearch, modo `extended` para lo de las últimas horas) qué ha pasado desde la última pasada (mira la hora en `registro.md`): "elecciones 29N última hora", "campaña 29N hoy", cada candidato por su nombre (Sánchez, Feijóo, Abascal, Colau, Montero y los territoriales), "encuesta CIS 29N", "debate electoral", "Jordi Wild entrevista", "polémica", "bulo elecciones" (Maldita, Newtral). Abre las noticias.
2. Puntúa cada tema de 1 a 5 en **gancho** (cuánto se va a buscar o comentar hoy: candidatos en podcasts o streams como The Wild Project, frases virales, choques en debates, encuestas, medidas que afectan al bolsillo, bulos que circulan) y en **verificable** (se puede contar con fuentes abiertas hoy mismo). Solo valen los temas con verificable ≥ 4.
3. Un tema con gancho ≥ 4 **pasa por delante del plan**: haz su vídeo para la próxima franja libre. Si no hay hueco en las próximas 6 h, sustituye el vídeo `pendiente` más atemporal (marca el sustituido como `reserva` en `cola.json`, no lo borres).
4. Ángulos que más funcionan: "¿Qué ha dicho X en…?" (frase literal + qué dicen los datos), "Lo que no se dijo en…", "3 claves de la entrevista de…", "¿Es verdad que…?" (bulo o frase comprobada), "Qué cambia para ti si…". Un evento grande da para 2–4 vídeos con ángulos distintos, repartidos entre partidos.
5. Citas solo de una fuente que puedas enlazar (la transcripción, el vídeo original o medios que la recojan literal). Si un medio solo lo resume, dilo así ("según X"), nunca entre comillas.
6. Anota en `registro.md` los temas valorados y qué se hizo con cada uno.

Momentos ya conocidos: **13-N**, Jordi Wild publica en The Wild Project sus entrevistas a Sánchez, Feijóo, Colau y Abascal (60–90 min cada una, con dos verificadores). Como la pasada es a las 10:31, normalmente saldrán el 14: un vídeo por entrevista ("¿Qué ha dicho X en The Wild Project?") más uno comparando lo que dijo cada uno sobre el mismo tema.

## Pasos
1. `git pull`. Lee `cola.json` y `registro.md`. Calcula qué franjas de hoy (las que aún no han pasado), mañana y pasado están vacías.
2. **Haz el radar de actualidad** (arriba). Para el resto de franjas, usa el calendario del plan. Abre las páginas de las que sacas datos: un fragmento de búsqueda no es una fuente.
3. **Escribe un guion por franja** en `guiones/<id>.json` (id = `slp_NNN_slug`, NNN correlativo). Mismo formato que `guiones/slp_002_voto_correo.json`. Reglas de contenido abajo.
4. **Voz de Andrew** (Clipchamp, en Chrome). Un audio por vídeo:
   1. Abre `https://app.clipchamp.com/` en una pestaña nueva. Abre el proyecto "Video Project 20" de "Tus vídeos" (o "Texto a voz → Pruébalo" si no está). Panel "Texto a voz": Idioma "Español (España)", Voz **"Andrew Multilingual"**.
   2. Clic en el cuadro de texto, `ctrl+a`, escribe el texto hablado completo: los `text` de todos los segmentos unidos con espacios, usando la parte después de `|` cuando la hay (números en letra). Pulsa "Guardar" y espera unos 10 s.
   3. `read_network_requests` con `urlPattern: "local-cache"`: el audio nuevo es el GET a `/local-cache/<id>` que no estaba antes. Con `javascript_tool`: `fetch` de esa URL → blob `audio/mpeg` → enlace con `download` y `click()`.
   4. En `C:\Users\nicol\Downloads` aparece un `.tmp` con el mismo tamaño que el blob (el listado es enorme: búscalo por `mtimeMs` en el fichero guardado). `device_stage_files` y cópialo a `audio/<id>.mp3`.
5. `./crear.sh <id>` → `videos/<id>.mp4` + portada `videos/<id>.jpg` (~2 min por vídeo). Mira `work/<id>/check.png`: textos legibles, nada se sale ni se solapa, cortes de frase bien sincronizados.
6. `git add -A && git commit && git push`. Comprueba que la URL pública de cada vídeo da 200.
7. **Programa en TikTok Studio** (Chrome, `https://www.tiktok.com/tiktokstudio/upload`). *Pasos por validar en la primera subida de prueba.* Para cada vídeo: el archivo se sube con `mcp__claude-in-chrome__file_upload` sobre el `input[type=file]` (copia antes el mp4 a `/mnt/user-data/outputs/`); descripción (`copy` de la cola); **activar "Contenido generado por IA"**; programar a la franja; "Programar". Comprueba que aparece en la lista de programados.
8. **Instagram Reels (cuenta nueva @politizatehoy, NO @fichalo.app):** por cada vídeo añade a `publicaciones.json` `{"id", "fecha": <misma franja + 15 min>, "estado": "pendiente", "copy"}`. Lo publica GitHub Actions (`publicar.py`, cada 15 min) con la API oficial; solo funciona cuando la variable `PUBLICADOR_ACTIVO` = `si` (ver `CONFIGURAR_INSTAGRAM.md`). Revisa errores o retrasos de más de 1 h y anótalos.
9. Actualiza `cola.json` (`estado: programado`, `fecha`, `copy`) y añade una línea a `registro.md` con lo programado y cualquier fallo. No inventes: si algo falla, anótalo y avisa a Nicks.

## Marca (no cambiar)
- Colores: azul marino `#14213D`, fosforito `#C8F53C`, papel `#F3EEE3`, rojo sello `#D7263D`, verde sello `#1F9D55`. Tipos: Fraunces 900 (titulares y logo), Courier Prime (cabecera, notas, sellos), Inter Tight (subtítulos).
- Logo = el de la foto de perfil (`marca/perfil_v3.png`): círculo azul marino con "Politízate" en blanco y "hoy" en caja fosforito. Cierre de cada vídeo: elemento `logo` + sello "+ SEGUIR" (ver `guiones/slp_002_voto_correo.json`).
- Cabecera con @politizatehoy, barra de cláusulas y sección final "La letra pequeña" en todos los vídeos.

## Tragedias y sucesos graves
Con víctimas (accidentes, atentados, catástrofes): `"tono": "serio"` en el guion (sin música, sin sellos de broma), etiquetas de la barra con `"clauseLabels"` (p. ej. LO QUE SE SABE / LOS AUDIOS / LO QUE NO SE SABE) en vez de cláusulas y letra pequeña, cifras atribuidas y con hora, nada de culpables mientras haya investigación, y nunca imágenes o detalles morbosos.

## Reglas de contenido (obligatorias)
- **Neutral:** sin opinión, sin pedir el voto. Mismo número de vídeos por partido y serie cada semana (cuenta en `cola.json` → `partidos`). Orden alfabético cuando salen varios.
- **Cada dato con fuente oficial o dos medios.** La fuente va en `header.source` y en el primer comentario. Plazos y cómo votar: siempre contra la fuente oficial (Junta Electoral, BOE, INE, Correos).
- **Citas literales** en "¿Qué ha dicho?", con enlace. Nunca voces clonadas, imágenes falsas, clips de TV ni fotos de agencia.
- **Veda de encuestas del 24-N al 29-N a las 20:00:** ningún vídeo con encuestas. **28-N y 29-N hasta las 20:00:** solo contenido práctico sobre cómo votar.
- Si no hay temas verificables para todas las franjas, publica menos. Nunca relleno.
- Formato: 30–40 s. Gancho en la primera frase (pregunta que te señala, promesa de lo oculto, dato que choca o urgencia real), 2 cláusulas y "la letra pequeña" al final, y un cierre que deje la historia abierta. Portada legible sin sonido.
- Descripción: título distinto al texto del vídeo + una pregunta para comentarios + 4–6 hashtags (`#elecciones #29N #eleccionesgenerales` + 2–3 del tema). Nunca hashtags de partidos.
- Series y calendario: ver el plan (enlace arriba).
