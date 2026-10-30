"""Música original sintetizada + efectos (pop por elemento, whoosh por escena) + voz -> final.mp4"""
import json, sys, os, subprocess
import numpy as np, soundfile as sf

SR = 24000
rng = np.random.default_rng(7)


def env(n, a=0.005, r=0.2):
    t = np.arange(n) / SR
    return np.minimum(t / a, 1) * np.exp(-t / r)


def tone(f, dur, r=0.2, kind="sine"):
    n = int(dur * SR); t = np.arange(n) / SR
    w = np.sin(2 * np.pi * f * t) if kind == "sine" else 2 * ((f * t) % 1) - 1
    return w * env(n, r=r)


def music(dur, bpm=112):
    n = int(dur * SR); out = np.zeros(n + SR * 2)
    beat = 60 / bpm
    prog = [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]]  # Am F C G
    hz = lambda m: 440 * 2 ** ((m - 69) / 12)
    b = 0
    while b * beat < dur:
        i = int(b * beat * SR)
        # bombo
        kn = int(0.25 * SR); kt = np.arange(kn) / SR
        if b % 1 == 0:
            out[i:i + kn] += 0.9 * np.sin(2 * np.pi * (50 + 90 * np.exp(-kt * 30)) * kt) * np.exp(-kt * 14)
        # charles a contratiempo
        hi = int((b + 0.5) * beat * SR); hn = int(0.05 * SR)
        out[hi:hi + hn] += 0.12 * rng.standard_normal(hn) * np.exp(-np.arange(hn) / SR * 80)
        # caja en 2 y 4
        if b % 2 == 1:
            sn = int(0.15 * SR)
            out[i:i + sn] += 0.25 * rng.standard_normal(sn) * np.exp(-np.arange(sn) / SR * 25)
        # acordes pluck en corcheas
        ch = prog[(b // 4) % 4]
        for half in (0, 0.5):
            j = int((b + half) * beat * SR)
            for m in ch:
                s = tone(hz(m + 12), 0.35, r=0.12)
                out[j:j + len(s)] += 0.10 * s
        # bajo
        if b % 2 == 0:
            s = tone(hz(ch[0] - 12), beat * 1.8, r=0.4)
            out[i:i + len(s)] += 0.35 * s
        b += 1
    out = out[:n]
    fade = int(1.0 * SR); out[-fade:] *= np.linspace(1, 0, fade)
    return out / np.abs(out).max()


def pop():
    n = int(0.09 * SR); t = np.arange(n) / SR
    return np.sin(2 * np.pi * (500 + 900 * t / t[-1]) * t) * env(n, a=0.002, r=0.03)


def thump():
    n = int(0.22 * SR); t = np.arange(n) / SR
    body = np.sin(2 * np.pi * (70 + 120 * np.exp(-t * 40)) * t) * np.exp(-t * 18)
    return body + 0.5 * rng.standard_normal(n) * np.exp(-t * 60)


def ticks(dur=0.9):
    n = int(dur * SR); x = np.zeros(n)
    for k in range(int(dur * 16)):
        i = int(k / 16 * SR); m = int(0.012 * SR)
        x[i:i + m] += rng.standard_normal(m) * np.exp(-np.arange(m) / SR * 400) * 0.6
    return x


def whoosh():
    n = int(0.35 * SR); x = rng.standard_normal(n)
    x = np.convolve(x, np.ones(12) / 12, "same")
    return x * np.sin(np.pi * np.arange(n) / n) ** 2


def db(x, d):
    return x * 10 ** (d / 20)


def main(vdir):
    tl = json.load(open(os.path.join(vdir, "timeline.json")))
    voice, _ = sf.read(os.path.join(vdir, "voz.wav"))
    n = len(voice)
    mix = voice / np.abs(voice).max() * 0.85
    if tl.get("tono") != "serio":
        mix = mix + db(music(n / SR + 0.1)[:n], -23)
    fx = np.zeros(n + SR)
    for s in tl["scenes"]:
        i = max(int((s["t0"] - 0.1) * SR), 0); w = whoosh(); fx[i:i + len(w)] += 0.5 * w
        for g in s["segments"]:
            for e in g["show"]:
                i = int(e["t"] * SR)
                p = {"stamp": thump, "note": ticks}.get(e["type"], pop)()
                gain = {"stamp": 0.9, "note": 0.35}.get(e["type"], 0.45)
                fx[i:i + len(p)] += gain * p[:len(fx) - i]
    mix = mix + db(fx[:n], -9)
    mix = mix / np.abs(mix).max() * 0.95
    wav = os.path.join(vdir, "mezcla.wav")
    sf.write(wav, mix, SR)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", os.path.join(vdir, "mudo.mp4"), "-i", wav,
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-af", "loudnorm=I=-14:TP=-1.5",
                    "-shortest", "-movflags", "+faststart", os.path.join(vdir, "final.mp4")], check=True)
    print("ok")


if __name__ == "__main__":
    main(sys.argv[1])
