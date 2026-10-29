# Rutina diaria de Politízate Hoy (@politizatehoy)

Canal de TikTok (y después Reels y Shorts) de actualidad política explicada, centrado en las elecciones generales del 29-N.
Nicks quiere que todo sea automático: esta rutina investiga, escribe, pone voz, renderiza y programa los vídeos sin que él toque nada.
Plan editorial completo: https://claude.ai/artifact/EpGu7vKZV4ok4vE6ARonrp

Datos fijos
- Repo público `nicolasarea-ux/politi`, rama `main`. Zona horaria `Europe/Madrid`.
- URL pública de un vídeo: `https://raw.githubusercontent.com/nicolasarea-ux/politi/main/videos/<id>.mp4`
- La rutina necesita el ordenador de Nicks (Windows, "nicolaptop") encendido con la app de Claude abierta: la voz se saca de Clipchamp y la subida se hace en TikTok Studio, los dos en el **navegador integrado** (herramientas `mcp__remote-devices__Claude_Browser__*`), donde Nicks ya tiene la sesión iniciada. Carpeta compartida: `C:\Users\nicol\Downloads`.
- Si el ordenador no responde: deja los guiones escritos, anótalo en `registro.md` y avisa a Nicks. TikTok Studio permite programar hasta 10 días, así que la rutina siempre deja **hoy, mañana y pasado** cubiertos: un día caído no deja huecos.

## Ritmo (no subir sin datos)
| Fechas | Vídeos/día | Horas (Madrid) |
| --- | --- | --- |
| 30-O → 5-N | 3 | 13:30, 19:30, 22:00 |
| 6-N → 12-N | 5 | 8:30, 13:30, 19:30, 21:00, 22:30 |
| 13-N → 29-N | 6 | 8:30, 12:30, 14:30, 19:30, 21:00, 22:30 |
| Picos: 11-N, 13-N, días de debate, 19-N, 26-N, 29-N | 10 | 8:30, 10:30, 12:30, 14:00, 16:00, 18:00, 19:30, 20:45, 21:45, 23:00 |

Mínimo 1 h entre vídeos. Lección de @fichalo.app: pasar a 12/día hundió el alcance y Meta bloqueó la API. Si las visitas medias por vídeo caen más de un 30 % al subir volumen, baja al ritmo anterior y anótalo.

## Pasos
1. `git pull`. Lee `cola.json` y `registro.md`. Calcula qué franjas de hoy (las que aún no han pasado), mañana y pasado están vacías.
2. **Investiga** (WebSearch / WebFetch) la actualidad política del día y lo que toca según el calendario del plan. Abre las páginas de las que sacas datos: un fragmento de búsqueda no es una fuente.
3. **Escribe un guion por franja** en `guiones/<id>.json` (id = `slp_NNN_slug`, NNN correlativo). Mismo formato que `guiones/slp_002_voto_correo.json`. Reglas de contenido abajo.
4. **Voz de Andrew** (Clipchamp, navegador integrado). Un audio por vídeo:
   1. Abre `https://app.clipchamp.com/` y pon el viewport a 1440×900 (`resize_window`). Abre el proyecto "Video Project 20" de "Tus vídeos" (o "Texto a voz → Pruébalo" si no está). Panel "Texto a voz": Idioma "Español (España)", Voz **"Andrew Multilingual"**.
   2. Clic en el cuadro de texto, `ctrl+a`, escribe el texto hablado completo: los `text` de todos los segmentos unidos con espacios, usando la parte después de `|` cuando la hay (números en letra). Pulsa "Guardar" y espera unos 10 s.
   3. `read_network_requests` con `urlPattern: "local-cache"`: el audio nuevo es el GET a `/local-cache/<id>` que no estaba antes. Con `javascript_tool`: `fetch` de esa URL → blob `audio/mpeg` → enlace con `download` y `click()`.
   4. En `C:\Users\nicol\Downloads` aparece un `.tmp` con el mismo tamaño que el blob (el listado es enorme: búscalo por `mtimeMs` en el fichero guardado). `device_stage_files` y cópialo a `audio/<id>.mp3`.
5. `./crear.sh <id>` → `videos/<id>.mp4` + portada `videos/<id>.jpg` (~2 min por vídeo). Mira `work/<id>/check.png`: textos legibles, nada se sale ni se solapa, cortes de frase bien sincronizados.
6. `git add -A && git commit && git push`. Comprueba que la URL pública de cada vídeo da 200.
7. **Programa en TikTok Studio** (navegador integrado, `https://www.tiktok.com/tiktokstudio/upload`). *Pasos por validar en la primera subida de prueba.* Para cada vídeo: el archivo se mete con `javascript_tool` (fetch de la URL pública → `File` → `DataTransfer` → `input[type=file]` + evento `change`); descripción (`copy` de la cola); **activar "Contenido generado por IA"**; programar a la franja; "Programar". Comprueba que aparece en la lista de programados.
8. **Instagram Reels (cuenta nueva @politizatehoy, NO @fichalo.app):** por cada vídeo añade a `publicaciones.json` `{"id", "fecha": <misma franja + 15 min>, "estado": "pendiente", "copy"}`. Lo publica GitHub Actions (`publicar.py`, cada 15 min) con la API oficial; solo funciona cuando la variable `PUBLICADOR_ACTIVO` = `si` (ver `CONFIGURAR_INSTAGRAM.md`). Revisa errores o retrasos de más de 1 h y anótalos.
9. Actualiza `cola.json` (`estado: programado`, `fecha`, `copy`) y añade una línea a `registro.md` con lo programado y cualquier fallo. No inventes: si algo falla, anótalo y avisa a Nicks.

## Marca (no cambiar)
- Colores: azul marino `#14213D`, fosforito `#C8F53C`, papel `#F3EEE3`, rojo sello `#D7263D`, verde sello `#1F9D55`. Tipos: Fraunces 900 (titulares y logo), Courier Prime (cabecera, notas, sellos), Inter Tight (subtítulos).
- Logo = el de la foto de perfil (`marca/perfil_v3.png`): círculo azul marino con "Politízate" en blanco y "hoy" en caja fosforito. Cierre de cada vídeo: elemento `logo` + sello "+ SEGUIR" (ver `guiones/slp_002_voto_correo.json`).
- Cabecera con @politizatehoy, barra de cláusulas y sección final "La letra pequeña" en todos los vídeos.

## Reglas de contenido (obligatorias)
- **Neutral:** sin opinión, sin pedir el voto. Mismo número de vídeos por partido y serie cada semana (cuenta en `cola.json` → `partidos`). Orden alfabético cuando salen varios.
- **Cada dato con fuente oficial o dos medios.** La fuente va en `header.source` y en el primer comentario. Plazos y cómo votar: siempre contra la fuente oficial (Junta Electoral, BOE, INE, Correos).
- **Citas literales** en "¿Qué ha dicho?", con enlace. Nunca voces clonadas, imágenes falsas, clips de TV ni fotos de agencia.
- **Veda de encuestas del 24-N al 29-N a las 20:00:** ningún vídeo con encuestas. **28-N y 29-N hasta las 20:00:** solo contenido práctico sobre cómo votar.
- Si no hay temas verificables para todas las franjas, publica menos. Nunca relleno.
- Formato: 30–40 s. Gancho en la primera frase (pregunta que te señala, promesa de lo oculto, dato que choca o urgencia real), 2 cláusulas y "la letra pequeña" al final, y un cierre que deje la historia abierta. Portada legible sin sonido.
- Descripción: título distinto al texto del vídeo + una pregunta para comentarios + 4–6 hashtags (`#elecciones #29N #eleccionesgenerales` + 2–3 del tema). Nunca hashtags de partidos.
- Series y calendario: ver el plan (enlace arriba).
