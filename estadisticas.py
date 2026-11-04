"""Descarga las métricas de todos los Reels de @politizatehoy -> stats.json (views, alcance, tiempo medio visto, compartidos, guardados, seguidores)."""
import json, os, urllib.parse, urllib.request, urllib.error
API = "https://graph.instagram.com/v21.0"; TOKEN = os.environ["IG_TOKEN"]; USER = os.environ["IG_USER_ID"]
def get(path, **p):
    p["access_token"] = TOKEN
    try:
        with urllib.request.urlopen(f"{API}/{path}?{urllib.parse.urlencode(p)}", timeout=60) as r: return json.loads(r.read())
    except urllib.error.HTTPError as e: return {"error": e.read().decode(errors="replace")[:300]}
pub = {r.get("ig_media_id"): r["id"] for r in json.load(open("publicaciones.json"))["reels"] if r.get("ig_media_id")}
out = {"cuenta": get("me", fields="username,followers_count,media_count"), "reels": []}
media = get(f"{USER}/media", fields="id,caption,timestamp,media_product_type,like_count,comments_count,permalink", limit=100).get("data", [])
for m in media:
    ins = get(f"{m['id']}/insights", metric="views,reach,saved,shares,total_interactions,ig_reels_avg_watch_time,ig_reels_video_view_total_time")
    vals = {d["name"]: d["values"][0]["value"] for d in ins.get("data", [])} if "data" in ins else {"error": ins.get("error")}
    out["reels"].append({"id": pub.get(m["id"], "?"), "ig": m["id"], "fecha": m["timestamp"], "likes": m.get("like_count"), "comentarios": m.get("comments_count"),
                         "url": m.get("permalink"), "titulo": (m.get("caption") or "")[:60], **vals})
json.dump(out, open("stats.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps(out["cuenta"]), len(out["reels"]), "reels")
