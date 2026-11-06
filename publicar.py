"""Publica en Instagram (API oficial con Instagram Login) los Reels de publicaciones.json cuya hora ya ha llegado.
Lo ejecuta GitHub Actions cada 15 minutos. Variables de entorno: IG_TOKEN, IG_USER_ID.
publicaciones.json = {"reels": [{"id": "...", "fecha": "YYYY-MM-DDTHH:MM" (Madrid), "estado": "pendiente|publicado|error", ...}]}
"""
import json, time, os, sys, urllib.error, urllib.parse, urllib.request
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

API = "https://graph.instagram.com/v21.0"
REPO_RAW = "https://raw.githubusercontent.com/nicolasarea-ux/politi/main/videos/"
CAPTION = "Lo que no te cuentan, en 30 segundos.\n\n#elecciones #29N #eleccionesgenerales #politica"
TZ = ZoneInfo("Europe/Madrid")
TOKEN = os.environ["IG_TOKEN"]
USER = os.environ["IG_USER_ID"]


def call(method, path, **params):
    params["access_token"] = TOKEN
    data = urllib.parse.urlencode(params).encode()
    if method == "GET":
        req = urllib.request.Request(f"{API}/{path}?{data.decode()}")
    else:
        req = urllib.request.Request(f"{API}/{path}", data=data, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:  # que el error de Instagram quede legible en publicaciones.json
        raise RuntimeError(f"HTTP {e.code}: {e.read().decode(errors='replace')[:250]}") from None


def ya_publicado(reel):
    """Evita duplicados: si un Reel con el mismo texto ya está en la cuenta (p. ej. se publicó pero falló el guardado), no se repite."""
    try:
        txt = (reel.get("copy") or "")[:80]
        for m in call("GET", f"{USER}/media", fields="id,caption", limit=15).get("data", []):
            if txt and (m.get("caption") or "")[:80] == txt:
                return m["id"]
    except Exception:
        pass
    return None


def publicar(reel):
    dup = ya_publicado(reel)
    if dup:
        print("Ya estaba publicado:", reel["id"], dup)
        return dup
    extra = {}
    portada = REPO_RAW + reel["id"] + ".jpg"
    try:  # portada de marca si existe (videos/<id>.jpg); si no, el segundo 1 del vídeo
        urllib.request.urlopen(urllib.request.Request(portada, method="HEAD"), timeout=20)
        extra["cover_url"] = portada
    except Exception:
        extra["thumb_offset"] = 1000
    c = call("POST", f"{USER}/media", media_type="REELS", video_url=REPO_RAW + reel["id"] + ".mp4",
             caption=reel.get("copy") or CAPTION, share_to_feed="true", **extra)
    cid = c["id"]
    for _ in range(40):  # hasta ~10 min procesando
        st = call("GET", cid, fields="status_code")["status_code"]
        if st == "FINISHED":
            break
        if st in ("ERROR", "EXPIRED"):
            raise RuntimeError(f"contenedor {st}")
        time.sleep(15)
    else:
        raise RuntimeError("timeout procesando el vídeo")
    return call("POST", f"{USER}/media_publish", creation_id=cid)["id"]


def main():
    # comprueba el token en cada pasada: si caduca, el workflow falla y GitHub avisa por email
    try:
        yo = call("GET", "me", fields="user_id,username")
    except Exception as e:  # p. ej. "API access blocked": se avisa en el log pero sin fallar (evita un email cada pasada)
        print("::warning::Instagram rechaza el token/app:", e)
        return
    print("Cuenta:", yo.get("username"), yo.get("user_id"))
    path = "publicaciones.json"
    data = json.load(open(path, encoding="utf-8"))
    ahora = datetime.now(TZ)
    # GitHub lanza el cron cuando quiere (~1 vez por hora): si el siguiente Reel toca en menos de 70 min, espera aquí hasta su hora exacta
    pend = sorted(datetime.fromisoformat(r["fecha"]).replace(tzinfo=TZ) for r in data["reels"] if r.get("estado") == "pendiente")
    prox = next((t for t in pend if t > ahora), None)
    if prox and not any(t <= ahora for t in pend) and prox - ahora < timedelta(minutes=70):
        espera = (prox - ahora).total_seconds()
        print(f"Esperando {espera/60:.0f} min hasta {prox:%H:%M}")
        time.sleep(espera)
        ahora = datetime.now(TZ)
    cambios = 0
    for r in sorted(data["reels"], key=lambda x: x["fecha"]):
        if r.get("estado") != "pendiente":
            continue
        t = datetime.fromisoformat(r["fecha"]).replace(tzinfo=TZ)
        if t > ahora + timedelta(minutes=2):  # la espera de arriba ya ajusta la hora
            continue
        if any(x.get("publicado_en") and ahora - datetime.fromisoformat(x["publicado_en"]).replace(tzinfo=TZ) < timedelta(minutes=45) for x in data["reels"]) or cambios >= 1:  # como mucho 1 Reel por pasada: si hubo un parón, no salen todos de golpe
            break
        if ahora - t > timedelta(hours=3):  # muy atrasado (p. ej. tras un bloqueo): no se publica a deshora
            r["estado"] = "saltado"
            r["nota"] = "más de 3 h de retraso; la rutina lo reprograma"
            cambios += 1
            continue
        try:
            r["ig_media_id"] = publicar(r)
            r["estado"] = "publicado"
            r["publicado_en"] = datetime.now(TZ).strftime("%Y-%m-%dT%H:%M")
            print("OK", r["id"])
        except Exception as e:  # noqa
            r["intentos"] = r.get("intentos", 0) + 1
            r["ultimo_error"] = str(e)[:300]
            if r["intentos"] >= 3:
                r["estado"] = "error"
            print("ERROR", r["id"], e, file=sys.stderr)
        cambios += 1
    if cambios:
        json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
