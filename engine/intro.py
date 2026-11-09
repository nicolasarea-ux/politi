"""Antepone clips reales (frase del político con su voz) o la cara de Nicks al vídeo animado.

Uso: python3 engine/intro.py <guion.json> <work_dir>
Lee "intro" del guion: lista de tramos que van ANTES del vídeo animado, en orden:
  {"file": "clips/abascal_revuelta.mp4",  # ruta dentro del repo
   "ss": 12.3, "to": 18.0,                 # segundos del original (máx. ~8 s)
   "tipo": "clip" | "cara",                # clip = vídeo de terceros encajado; cara = selfie a pantalla completa
   "label": "ABASCAL, ANOCHE EN LA REVUELTA",
   "sub": "«No vengo a hacer amigos»",      # frase literal, opcional
   "fuente": "Imagen: RTVE"}               # obligatorio en tipo clip
Sustituye <work_dir>/final.mp4 por la versión con intro.
"""
import json, os, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
INK, MARK, PAPER = (20, 33, 61), (200, 240, 60), (243, 238, 227)
FONT = os.path.join(os.path.dirname(__file__), "fonts_ttf", "InterTight-900.ttf")


def font(sz):
    return ImageFont.truetype(FONT, sz)


def wrap(d, txt, f, maxw):
    words, lines, cur = txt.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines


def overlay(seg, path):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    # marca arriba a la derecha
    f = font(34); t = "@politizatehoy"
    d.rounded_rectangle((W - 60 - d.textlength(t, font=f) - 36, 120, W - 60, 182), 18, fill=PAPER + (235,))
    d.text((W - 60 - 18, 151), t, font=f, fill=INK, anchor="rm")
    if seg.get("label"):
        f = font(52); lines = wrap(d, seg["label"].upper(), f, W - 220)
        y = 300
        for ln in lines:
            tw = d.textlength(ln, font=f)
            d.rounded_rectangle(((W - tw) / 2 - 26, y - 8, (W + tw) / 2 + 26, y + 70), 16, fill=INK + (255,))
            d.text((W / 2, y + 31), ln, font=f, fill=PAPER, anchor="mm"); y += 86
        # subrayado lima
        d.rectangle((W / 2 - 90, y + 4, W / 2 + 90, y + 16), fill=MARK + (255,))
    if seg.get("sub"):
        f = font(58); lines = wrap(d, seg["sub"], f, W - 160); y = 1290
        for ln in lines:
            tw = d.textlength(ln, font=f)
            d.rounded_rectangle(((W - tw) / 2 - 18, y - 6, (W + tw) / 2 + 18, y + 72), 12, fill=MARK + (255,))
            d.text((W / 2, y + 33), ln, font=f, fill=INK, anchor="mm"); y += 84
    if seg.get("fuente"):
        f = font(30)
        d.text((W / 2, 1560), seg["fuente"], font=f, fill=(255, 255, 255, 230), anchor="mm",
               stroke_width=3, stroke_fill=(0, 0, 0, 160))
    im.save(path)


def render_seg(seg, root, out, ovl):
    src = os.path.join(root, seg["file"])
    ss, to = float(seg.get("ss", 0)), seg.get("to")
    dur = ["-t", str(float(to) - ss)] if to is not None else []
    if seg.get("tipo", "clip") == "cara":
        vf = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,fps=30[v];"
              "[v][1:v]overlay=0:0,format=yuv420p[o]")
    else:
        vf = (f"[0:v]split[a][b];"
              f"[a]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=30:2,eq=brightness=-0.18[bg];"
              f"[b]scale={W - 60}:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2-40,setsar=1,fps=30[v];"
              "[v][1:v]overlay=0:0,format=yuv420p[o]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(ss), *dur, "-i", src, "-i", ovl,
                    "-filter_complex", vf, "-map", "[o]", "-map", "0:a:0?",
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
                    "-c:a", "aac", "-ar", "48000", "-ac", "2", "-b:a", "160k", out], check=True)
    # si el clip no tiene audio, añadir silencio para que el concat no falle
    has_a = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=index",
                            "-of", "csv=p=0", out], capture_output=True, text=True).stdout.strip()
    if not has_a:
        tmp = out + ".s.mp4"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", out, "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
                        "-shortest", "-c:v", "copy", "-c:a", "aac", tmp], check=True)
        os.replace(tmp, out)


def main(guion, work):
    g = json.load(open(guion)); segs = g.get("intro") or []
    if not segs:
        return
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    final = os.path.join(work, "final.mp4"); tmpd = tempfile.mkdtemp(dir=work)
    parts = []
    for i, s in enumerate(segs):
        if s.get("tipo", "clip") == "clip" and not s.get("fuente"):
            sys.exit(f"intro[{i}]: un clip de terceros necesita 'fuente'")
        o, p = os.path.join(tmpd, f"ovl{i}.png"), os.path.join(tmpd, f"seg{i}.mp4")
        overlay(s, o); render_seg(s, root, p, o); parts.append(p)
    parts.append(final)
    ins = sum([["-i", p] for p in parts], [])
    fc = "".join(f"[{i}:v]fps=30,format=yuv420p,setsar=1[v{i}];[{i}:a]aresample=48000,aformat=channel_layouts=stereo[a{i}];"
                 for i in range(len(parts)))
    fc += "".join(f"[v{i}][a{i}]" for i in range(len(parts))) + f"concat=n={len(parts)}:v=1:a=1[v][a]"
    out = os.path.join(work, "final_intro.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", fc, "-map", "[v]", "-map", "[a]",
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-c:a", "aac", "-b:a", "160k",
                    "-movflags", "+faststart", out], check=True)
    os.replace(out, final)
    print("intro ok:", len(segs), "tramo(s)")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
