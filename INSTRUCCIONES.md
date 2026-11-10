# Rutina diaria de Politízate Hoy (@politizatehoy)

Canal de TikTok (y después Reels y Shorts) de actualidad política explicada, centrado en las elecciones generales del 29-N.
Nicks quiere que todo sea automático: esta rutina investiga, escribe, pone voz, renderiza y programa los vídeos sin que él toque nada.
Plan editorial completo: https://claude.ai/artifact/EpGu7vKZV4ok4vE6ARonrp

Datos fijos
- Repo público `nicolasarea-ux/politi`, rama `main`. Zona horaria `Europe/Madrid`.
- URL pública de un vídeo: `https://raw.githubusercontent.com/nicolasarea-ux/politi/main/videos/<id>.mp4`
- La rutina necesita el ordenador de Nicks (Windows, "nicolaptop") encendido con la app de Claude abierta: la voz se saca de Clipchamp y la subida se hace en TikTok Studio. **Usa el navegador integrado de la app de Claude (`mcp__remote-devices__Claude_Browser__*`), NO su Chrome: desde el 30-O Chrome se congela con Clipchamp y Nicks pidió cambiar al integrado.** Ahí Clipchamp ya tiene la sesión iniciada. Si Clipchamp o TikTok piden iniciar sesión, para y avisa. Carpeta compartida: `C:\Users\nicol\Downloads`.
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
4. **Voz de Andrew** (Clipchamp en el navegador integrado). Un audio por vídeo:
   1. `preview_start` con `https://app.clipchamp.com/` → "Texto a voz → Pruébalo". Idioma "Español (España)"; en el campo Voz (combobox) escribe "Andrew" y elige **"Andrew Multilingual"** (compruébalo: el panel a veces se reajusta y un clic por coordenadas cae en otro campo; usa `find`/refs, no coordenadas).
   2. Cuadro "Escribe lo que te gustaría decir": clic, `ctrl+a`, escribe el texto hablado completo (los `text` de los segmentos unidos con espacios, parte después de `|`, `_` → espacio). Espera 1 s, `find "Guardar"`, `scroll_to` + clic en el botón, y espera ~14 s.
   3. `read_network_requests` con `urlPattern: "local-cache"`: el audio nuevo es el último GET `/local-cache/<id>` (sin `_filmstrip`). Clipchamp borra el anterior al guardar uno nuevo: sácalo antes de generar el siguiente.
   (Desde la versión de Clipchamp del 3-N, `fetch` y `read_network_requests` de `/local-cache/` devuelven HTML: si pasa, saca el audio de IndexedDB `local-cache`, almacén `assets`; cada fila tiene `blob`, `fileName` y `permanentUrl`. Búscalo por el inicio del texto en `fileName`, y antes `pip install soundfile numpy --break-system-packages` si falta.)
   4. `javascript_tool`: `fetch` de esa URL → bytes → base64 y devuélvelo como resultado. El resultado es demasiado grande y se guarda en un fichero de `tool-results`; de ahí extrae el base64 y escribe `audio/<id>.mp3` (no hace falta la carpeta Downloads).
5. `./crear.sh <id>` → `videos/<id>.mp4` + portada `videos/<id>.jpg` (~2 min por vídeo). Mira `work/<id>/check.png`: textos legibles, nada se sale ni se solapa, cortes de frase bien sincronizados.
6. `git add -A && git commit && git push`. Comprueba que la URL pública de cada vídeo da 200.
7. **Programa en TikTok Studio** (Chrome, `https://www.tiktok.com/tiktokstudio/upload`). *Pasos por validar en la primera subida de prueba.* Para cada vídeo: el archivo se sube con `mcp__claude-in-chrome__file_upload` sobre el `input[type=file]` (copia antes el mp4 a `/mnt/user-data/outputs/`); descripción (`copy` de la cola); **activar "Contenido generado por IA"**; programar a la franja; "Programar". Comprueba que aparece en la lista de programados.
8. **Instagram Reels (cuenta nueva @politizatehoy, NO @fichalo.app):** por cada vídeo añade a `publicaciones.json` `{"id", "fecha": <misma franja + 15 min>, "estado": "pendiente", "copy"}`. Lo publica GitHub Actions (`publicar.py`, cada 15 min) con la API oficial; solo funciona cuando la variable `PUBLICADOR_ACTIVO` = `si` (ver `CONFIGURAR_INSTAGRAM.md`). Revisa errores o retrasos de más de 1 h y anótalos.
9. Actualiza `cola.json` (`estado: programado`, `fecha`, `copy`) y añade una línea a `registro.md` con lo programado y cualquier fallo. No inventes: si algo falla, anótalo y avisa a Nicks.

## Marca (no cambiar)
- Colores: azul marino `#14213D`, fosforito `#C8F53C`, papel `#F3EEE3`, rojo sello `#D7263D`, verde sello `#1F9D55`. Tipos: Fraunces 900 (titulares y logo), Courier Prime (cabecera, notas, sellos), Inter Tight (subtítulos).
- Logo = el de la foto de perfil (`marca/perfil_v3.png`): círculo azul marino con "Politízate" en blanco y "hoy" en caja fosforito. Cierre de cada vídeo: elemento `logo` + sello "+ SEGUIR" (ver `guiones/slp_002_voto_correo.json`).
- Cabecera con @politizatehoy, barra de cláusulas y sección final "La letra pequeña" en todos los vídeos.

## Portadas (Nicks, 30-O: las de antes eran feas)
`crear.sh` genera `videos/<id>.jpg` con `engine/cover.js` (diseño fijo: serie arriba, título grande con fosforito, mancha con icono, píldora de marca; todo dentro del recorte 3:4 de la cuadrícula de Instagram). Cada guion lleva `"portada": {"serie", "titulo" (con *marca*), "icono" o "grande" (un número/texto corto en vez de icono), "sub" (5–7 palabras)}`; si falta algo, se saca de la cabecera y del primer titular. Revisa la portada antes de programar: el icono tiene que tener sentido (nada de `doc` tachado o `person` tachado para cosas neutras). Iconos: rings, kids, house, doc, envelope, calendar, laptop, train, clock, phone, plane, question, urna, user.


**Portadas (desde 3-N):** el círculo lleva un DATO, no un icono genérico. Pon siempre `portada.grande` con la cifra, fecha o palabra clave del vídeo (p. ej. "203", "69", "28-N", "4 h", "×3", "DNI"; máx. ~6 caracteres). En "Quién es quién" (icono user) salen solas las iniciales del título (PS, AF…). Icono solo si de verdad no hay dato. `sub` corto (≤ 32 caracteres): ahora se ve a 76 px. Nada de fotos de políticos (derechos de imagen).
Series "Quién es quién": prioriza candidatos principales (Sánchez, Feijóo, Abascal, Díaz); los secundarios rinden mucho menos (Colau 41 views vs Feijóo 307).

## Formato animado (Nicks, 3-N: "subida de calidad")
Desde el 3-N, **al menos la mitad de los vídeos** se hacen en formato animado (`"formato": "animado"` en guion y cola), y todos los que tengan algo que se pueda dibujar:
- `via`: esquema de vía con dos trenes, señal, reloj y choque; `keys` con `{"s": escena relativa, "g": segmento, "f": fracción}` y estado (`a`, `b` = posición 0–1, `sig` off/red/green, `clk`, `speed`, `boom`, `lab`). Ejemplo: `guiones/slp_033_urda_minuto.json`.
- `hemi`: hemiciclo de 350 puntos que se llena (`fill` [{n, c}], `line` 176, contador). `grid`: tabla que aparece celda a celda y marca ganadores (`win`), p. ej. cocientes D'Hondt (ejemplo: `guiones/slp_014_dhondt.json`).
- En `show`, `at` es el índice de la palabra del segmento (entero), no segundos.
- Cifras que cuentan: en `card` escribe `{69}`. `card` sin `icon` = tarjeta centrada solo con texto.
- Algo nuevo en pantalla cada 2–3 s; la cámara ya hace zoom lento sola. Duración objetivo 35–45 s.
- **Portada animada:** `portada.escena` = el mismo elemento (`via` con `estado`, `hemi`…) en lugar del círculo; `portada.tam` fija el tamaño del título si se parte mal. Revisa siempre la portada recortada 3:4.
- Tono serio en tragedias: sin `boom` en portada, sin sellos.
Mide: compara views y tiempo de visionado animado vs. normal en `registro.md` cada 3 días.

## 4 formatos en prueba (Nicks, 3-N noche: "más dopamina", 0 seguidores → retención y seguir)
Cada día, **un vídeo de cada formato** (los otros huecos, formato normal animado). Anota en `cola.json` `"formato"` con el nombre y compara cada 3 días views, tiempo medio y seguidores ganados por formato en `registro.md`; el que gane gana franjas.
1. **`minuto`** — reconstrucción o explicador con esquema animado (`via`, `hemi`, `grid`, mapas). Ej.: slp_033, slp_036.
2. **`bulo`** — "¿Verdad o bulo?": frase viral en pantalla (cita literal + quién la dijo), `urni` con `mood` "duda", `poll` VERDAD/BULO con `hide: true` (muestra "?") y "¿Tú qué crees? Comenta antes de que te lo diga", 2 s de espera, `reveal` + `flash` "VERDAD"/"BULO"/"ENGAÑOSO" y los datos con fuente oficial. Solo afirmaciones verificables y de cualquier partido (rota partidos).
3. **`top3`** — "3 cosas que…": `flash` gigante "3", "2", "1" (bg mark/ink/red), cada punto con `card`+`sticker` y una cifra que cuenta `{n}`; el mejor al final ("el 1 casi nadie lo sabe"). Cierre: "¿Cuál pondrías tú en el 1?".
4. **`urni`** — la mascota Urni (urna con ojos, `type: "urni"`, `moods` [{at, m: neutral/sorpresa/duda/serio/feliz}], `say` = bocadillo corto) explica un tema como si tuvieras 14 años, con `sticker` emoji (🤯 🧐 ⚠️ ✅ 🗳️) y cambios de cara cada frase. Nunca para tragedias.

**Reglas de retención (todos los formatos):**
- Fotograma 0 = gancho: titular + un `flash` o pregunta grande en el primer segundo. Nada de logo al principio.
- Algo nuevo en pantalla cada ≤ 2 s (tarjeta, flash, sticker, cambio de cara, contador). La cámara ya da un golpe en cada elemento.
- Bucle abierto en la primera frase ("y lo último es lo que más cuesta creer").
- 30–40 s máximo. Si el guion pasa de 95 palabras, recorta.
- **Seguidores:** termina con una razón concreta para seguir ("Mañana: lo que propone cada partido sobre el alquiler. Síguenos para no perdértelo") y numera series ("Parte 1/3"). En el copy, una pregunta que se responda en una palabra.

**Portadas v2 (3-N):** fondo azul marino por defecto (no parecen un fotograma), título en papel con fosforito, círculo con dato o `portada.escena` en tarjeta, y `portada.badge` (sello rojo: "MINUTO A MINUTO", "¿BULO?", "TOP 3", "EN 30 S"). `portada.estilo: "clasico"` vuelve al papel.

## PLAN DE CRECIMIENTO (Nicks, 6-N — manda sobre lo anterior si choca)
Datos 9 días (35 Reels): mediana 127 views, alcance ~111, 8 s vistos, 0 comentarios. Solo salen del grupo de prueba los vídeos de PERSONAS y CHOQUES (Sánchez vs Milei 352, Feijóo 307, Jesús de Miguel 208). Explicativos sin cara (top 3, Urni explicando, D'Hondt, Senado): 96–120 y 6 s.
1. **Mezcla diaria:** 2 de cada 3 Reels sobre una PERSONA o un CHOQUE: "X vs Y" (dos caras, mismo espacio, frases literales de ambos), "Lo que ha dicho X", "Quién es X", "X responde a Y". Siempre `cara` en el vídeo desde `at: 0` y en la portada.
2. **Explicativos: máximo 1 al día** y colgados de una persona ("Lo que propone Feijóo sobre vivienda", no "Qué es la vivienda"). Atemporales sin cara → `reserva`.
3. **En pausa 1 semana:** formatos `top3` y `urni` explicando. Se mantienen `bulo` (en serie), `minuto` y `vs`. Urni solo como reacción pequeña.
4. **Segundo 0:** cara + la frase literal más fuerte en pantalla (`flash` o `card` con comillas) antes de cualquier contexto. 20–30 s.
5. **Comentarios:** cierra SIEMPRE con una pregunta de sí/no o de elegir entre dos ("¿Dimisión justa? Sí o no", "¿Quién gana: Sánchez o Milei?"), en voz, en pantalla y como primera línea del copy. Nada de preguntas abiertas.
6. **Neutralidad intacta:** rota personas de todos los partidos; en los VS, mismo tiempo y mismo trato para los dos; 2 fuentes; frases literales.
7. **Objetivo semanal:** tiempo medio visto ≥ 12 s y 1 de cada 3 Reels > 250 views. Revísalo en `stats.json` cada pasada y anota en `registro.md` qué Reel superó 250.
8. Al replanificar: si en la cola hay más de 1 explicativo sin cara en un día, pasa los demás a `reserva` y llena el hueco con persona/choque del radar.

## Datos del 4-N (stats.json) y cambios obligatorios
`stats.json` se actualiza solo en cada pasada del publicador (views, alcance, `ig_reels_avg_watch_time` en ms, compartidos, guardados). Léelo en cada pasada y anota en `registro.md` los 3 mejores y peores por tiempo medio visto.
Diagnóstico 4-N: todos los Reels se quedan en ~100–130 de alcance (grupo de prueba) y el tiempo medio visto es 5–10 s en vídeos de 35–50 s. Lo que más retiene: caras conocidas y noticia caliente. Lo que peor: arranques lentos (Urda minuto a minuto: 4 s).
- **Duración 20–30 s, máximo 70 palabras.** La voz va un 10 % más rápida (TEMPO=1.1 en `tts_andrew.py`, ya por defecto).
- **Segundo 0:** el primer elemento aparece con `at: 0` y es lo más fuerte (cara, `flash`, cifra). La primera frase es el conflicto o la pregunta, nunca contexto.
- **Caras:** `fotos/<nombre>_rec.png` (recortadas, licencia libre; créditos en `fotos/creditos.json`). Elemento `{"type":"cara","foto":"sanchez","h":600,"label":"Pedro Sánchez"}`. Si usas una cara, añade al copy la línea `Fotos: <autor> (<licencia>, Wikimedia Commons)`. Para añadir caras nuevas: Commons (CC0, CC BY, CC BY-SA, dominio público o La Moncloa con atribución) vía el navegador integrado, recorte con `rembg` (modelo u2net_human_seg). Nunca fotos de agencia (EFE, Europa Press…).
- **Portadas (Nicks, 4-N: le gustan las miniatura):** `portada.mini` es el estilo POR DEFECTO en todos los vídeos (si falta, `cover.js` lo genera del título, pero mejor escríbelo tú: `texto` corto, `rojo` 1–3 palabras, `cara` si sale una persona con foto en `fotos/`, si no Urni con `mood`). La v2 azul solo con `estilo: "v2"`. Antes la regla era: alterna `portada.mini` (estilo miniatura: `texto` 2 líneas, `rojo` = palabra gancho en caja roja, `cara` o Urni con `mood`, `emoji`, flecha) con la v2 azul. Anota en `cola.json` `"portada_estilo": "mini"|"v2"` y compara cada 3 días.
- TikTok multiplicaría el alcance: si Nicks crea la cuenta, prioridad máxima automatizarla.

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


## CIERRE "SÍGUENOS" (8-N, petición de Nicks)
- Todos los vídeos llevan en los últimos ~3 s un banner "Síguenos: las 4 entrevistas de Wild 13-N" (engine/slp.html, FOLLOW_DEF) y publicar.py añade al copy, antes de los hashtags, la línea CTA.
- Excepciones: noticias graves (atentados, muertes) → `"follow": false` en el guion.
- Texto propio por vídeo: `"follow": "texto"`.
- El 14-N, cambiar FOLLOW_DEF y CTA (publicar.py) por el siguiente gancho con fecha (p. ej. debates o el 29-N). Siempre un motivo concreto y con fecha, nunca un "síguenos" genérico.

## SEMANA DE PRUEBA (9-N → 15-N) — sustituye al plan del 6-N donde choque
Motivo: estancados en ~130 views de mediana y 2 seguidores con 5 Reels/día.
1. **2–3 Reels al día, máximo.** Solo actualidad con caras y choque, publicada en las primeras horas tras la noticia. Huecos: 13:45, 19:45 y 22:45 (8:45 solo si hay algo muy fuerte de la mañana).
2. **Cero explicativos/"cómo votar"**: están en `reserva` y vuelven del 22-N al 28-N, cuando la gente los busca.
3. **Clip real en el primer segundo** siempre que exista: 4–8 s de la frase del político con su voz, campo `intro` del guion (ver engine/intro.py). Fuente obligatoria en pantalla y en el copy ("Imagen: RTVE"). Fragmento corto y con comentario nuestro, nunca piezas largas de terceros.
   - De dónde salen: Nicks deja clips o grabaciones de pantalla en `Descargas\politizate\clips` del portátil (carpeta conectada) → stage → `clips/<nombre>.mp4` en el repo.
4. **Nicks NO sale en cámara ni pone su voz** (dicho el 9-N). No proponerlo más. El gancho humano lo dan los clips reales de los políticos.
5. **Doble publicación en TikTok** cuando la cuenta esté conectada en Metricool (marca Politízate Hoy). Hasta entonces, solo Instagram.
6. Medir el domingo 15-N: mediana de views, segundos vistos, seguidores ganados. Comparar con la semana anterior (mediana 130, 2 seguidores).

## REGLA DE ORO (10-N): "TANDA EN CALIENTE"
- Lo que funcionó: Abascal en La Revuelta → 3 Reels de madrugada con 2.100–2.800 views cada uno (mediana del canal: 139), 17–18 s vistos, 23 comentarios, de 2 a 8 seguidores.
- Cuando haya un MOMENTO del que todo el mundo habla (entrevista, debate, zasca viral): esa misma noche, un Reel por momento (3 en las primeras 2 h y el resto al día siguiente). Frase literal en grande en el segundo 0, las dos caras, pregunta para comentar al final. Formato "top 5" incluido.
- Próximos momentos a preparar con antelación (guiones base y caras listas): entrevistas de Jordi Wild (13-N), debates a 4 y a 2, mítines de cierre, noche electoral 29-N.
- Días sin momento: 2–3 Reels de actualidad con caras. Nunca relleno.
