"""Voz externa (Andrew/Clipchamp, mp3 con el guion completo) -> voz.wav + timeline.json.
Uso: python3 tts_andrew.py <video_dir> <audio.mp3>
Corta el audio en segmentos buscando los silencios más cercanos a donde deberían caer."""
import json, sys, os, subprocess
import numpy as np, soundfile as sf
import re


def syllables(w):
    w = w.lower()
    n = len(re.findall(r"[aeiouáéíóúü]+", w)) or 1
    if re.search(r"[,.:;!?]$", w):
        n += 1.2  # pausa de puntuación
    return n

SR, LEAD, TAIL = 24000, 0.15, 0.6


def load(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).copy()


def silences(a, hop=0.01, min_len=0.12):
    h = int(hop * SR)
    e = np.array([np.sqrt(np.mean(a[i:i + h] ** 2) + 1e-12) for i in range(0, len(a) - h, h)])
    db = 20 * np.log10(e / e.max())
    quiet = db < -38
    out, i = [], 0
    while i < len(quiet):
        if quiet[i]:
            j = i
            while j < len(quiet) and quiet[j]:
                j += 1
            if (j - i) * hop >= min_len:
                out.append((i * hop, j * hop))
            i = j
        else:
            i += 1
    speech = np.where(~quiet)[0]
    return out, speech[0] * hop, speech[-1] * hop


def main(vdir, mp3):
    sc = json.load(open(os.path.join(vdir, "script.json")))
    a = load(mp3)
    sil, s0, s1 = silences(a)
    sil = [x for x in sil if x[0] > s0 and x[1] < s1]
    segs = [(si, g) for si, scene in enumerate(sc["scenes"]) for g in scene["segments"]]
    spok = [[t.split("|")[-1] for t in g["text"].split()] for _, g in segs]
    w = np.array([sum(syllables(x) for x in s) for s in spok], float)
    expect = s0 + np.cumsum(w)[:-1] / w.sum() * (s1 - s0)
    # elegir N-1 silencios monótonos: programación dinámica (cerca de lo esperado y largos)
    N, M = len(expect), len(sil)
    mids = np.array([(x[0] + x[1]) / 2 for x in sil]); lens = np.array([x[1] - x[0] for x in sil])
    INF = 1e9
    cost = np.full((N, M), INF); back = np.zeros((N, M), int)
    loc = lambda k, j: abs(mids[j] - expect[k]) - 2.0 * lens[j]
    for j in range(M):
        cost[0, j] = loc(0, j)
    for k in range(1, N):
        best, bj = INF, -1
        for j in range(M):
            if j > 0 and cost[k - 1, j - 1] < best:
                best, bj = cost[k - 1, j - 1], j - 1
            if bj >= 0:
                cost[k, j] = best + loc(k, j); back[k, j] = bj
    j = int(np.argmin(cost[N - 1])); picks = [j]
    for k in range(N - 1, 0, -1):
        j = back[k, j]; picks.append(j)
    picks = picks[::-1]
    bounds = [(s0, None)] + [sil[p] for p in picks] + [(None, s1)]
    tl = {"brand": sc["brand"], "header": sc.get("header", {}), "clauses": sc.get("clauses", 0), "scenes": []}
    scenes = {}
    for idx, (si, g) in enumerate(segs):
        t0 = (bounds[idx][1] if idx else s0) + LEAD
        t1 = (bounds[idx + 1][0] if idx < N else s1) + LEAD
        toks = g["text"].split(); disp = [x.split("|")[0] for x in toks]
        ww = np.array([syllables(x) for x in spok[idx]])
        edges = t0 + np.concatenate([[0], np.cumsum(ww) / ww.sum()]) * (t1 - t0)
        words = [{"w": d, "t0": edges[i], "t1": edges[i + 1]} for i, d in enumerate(disp)]
        els = []
        for e in g.get("show", []):
            e = dict(e); at = min(e.pop("at", 0), len(words) - 1)
            e["t"] = words[at]["t0"] if at else t0; els.append(e)
        S = scenes.setdefault(si, {**{k: v for k, v in sc["scenes"][si].items() if k != "segments"}, "t0": t0, "segments": []})
        S["segments"].append({"t0": t0, "t1": t1, "words": words, "show": els, "hide": g.get("hide", []), "hideAt": t0})
    order = sorted(scenes)
    for n, si in enumerate(order):
        S = scenes[si]
        S["t1"] = scenes[order[n + 1]]["t0"] if n + 1 < len(order) else s1 + LEAD + TAIL
        if n + 1 < len(order):
            S["t0n"] = S["t1"]
        tl["scenes"].append(S)
    # que cada escena empiece justo después de terminar la anterior (sin huecos visuales)
    for n in range(1, len(tl["scenes"])):
        tl["scenes"][n]["t0"] = min(tl["scenes"][n]["t0"], tl["scenes"][n - 1]["t1"])
    tl["duration"] = s1 + LEAD + TAIL
    voice = np.concatenate([np.zeros(int(LEAD * SR), np.float32), a, np.zeros(int(TAIL * SR), np.float32)])
    voice = voice[: int(tl["duration"] * SR) + 1]
    sf.write(os.path.join(vdir, "voz.wav"), voice, SR)
    json.dump(tl, open(os.path.join(vdir, "timeline.json"), "w"), ensure_ascii=False, indent=1)
    print(f"duración {tl['duration']:.1f}s, {len(sil)} silencios, cortes en:",
          " ".join(f"{sil[p][0]:.2f}" for p in picks))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
