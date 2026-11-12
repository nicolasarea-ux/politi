"""Recorta la cabeza de cada fotos/<n>_rec.png -> fotos/<n>_head.png (para el elemento 'cabezon').
Busca el cuello (fila más estrecha del recorte entre cabeza y hombros). La boca queda ~al 76 % de la altura."""
import glob, sys, numpy as np
from PIL import Image
names = sys.argv[1:] or sorted(f.split('/')[-1][:-8] for f in glob.glob('fotos/*_rec.png') if '_px_' not in f)
for n in names:
    im = Image.open(f'fotos/{n}_rec.png').convert('RGBA'); a = np.array(im)[:, :, 3] > 128
    rows = np.where(a.any(1))[0]; top, bot = rows[0], rows[-1]; H = bot - top
    wid = np.array([a[r].sum() for r in range(im.height)])
    lo, hi = top + int(0.42 * H), top + int(0.85 * H)
    # cuello: mínimo de anchura suavizada antes de que se ensanchen los hombros
    sm = np.convolve(wid, np.ones(9) / 9, 'same')
    neck = lo + int(np.argmin(sm[lo:hi]))
    cols = np.where(a[top:neck].any(0))[0]
    # anchura de la cabeza = percentil de anchuras en la parte alta (evita orejas/pelo raro)
    hw = int(np.percentile(wid[top:neck], 90)); cx = int(np.mean([np.where(a[r])[0].mean() for r in range(top + (neck - top) // 3, neck) if a[r].any()]))
    W = int(hw * 1.15); Hh = int((neck - top) * 1.07)
    crop = im.crop((cx - W // 2, top - int(0.02 * Hh), cx + W // 2, top + Hh))
    crop = crop.resize((600, int(600 * crop.height / crop.width)))
    crop.save(f'fotos/{n}_head.png'); print(n, crop.size, 'cuello', round((neck - top) / H, 2))
