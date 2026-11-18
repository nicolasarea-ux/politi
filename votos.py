"""Cuenta votos en comentarios («Sánchez» / «Feijóo») de los reels marcados con "votos": true en publicaciones.json.
Escribe votos.json. Lo ejecuta el workflow después de estadisticas.py."""
import json, os, re, unicodedata, urllib.parse, urllib.request
TOKEN = os.environ["IG_TOKEN"]
def get(path, **p):
    p["access_token"] = TOKEN
    return json.load(urllib.request.urlopen("https://graph.instagram.com/v21.0/" + path + "?" + urllib.parse.urlencode(p), timeout=30))
def norm(s): return unicodedata.normalize("NFD", s.lower()).encode("ascii", "ignore").decode()
pubs = json.load(open("publicaciones.json")); L = pubs if isinstance(pubs, list) else list(pubs.values())[0]
out = {}
for r in L:
    mid = r.get("ig_media_id")
    if not (r.get("votos") and mid): continue
    c = {"sanchez": 0, "feijoo": 0}; quien = {}
    url = f"{mid}/comments"; params = dict(fields="id,text,username", limit=50)
    while True:
        d = get(url, **params)
        for m in d.get("data", []):
            t = norm(m.get("text", "")); s = bool(re.search(r"\bsanchez|pedro\b", t)); f = bool(re.search(r"\bfeijoo|feijo|feij", t))
            if s != f: quien[m.get("username") or m["id"]] = "sanchez" if s else "feijoo"  # 1 voto por usuario, el último
        nxt = d.get("paging", {}).get("cursors", {}).get("after")
        if not nxt or not d.get("paging", {}).get("next"): break
        params["after"] = nxt
    for v in quien.values(): c[v] += 1
    out[r["id"]] = c
json.dump(out, open("votos.json", "w"), indent=1)
print(out)
