// timeline.json -> frames (Playwright) -> mudo.mp4 (ffmpeg)
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const fs = require('fs'), path = require('path');
const vdir = path.resolve(process.argv[2]);
const only = process.argv[3]; // opcional: lista de segundos para previsualizar "1,5,9"
const FPS = 30;
(async () => {
  const tl = JSON.parse(fs.readFileSync(path.join(vdir, 'timeline.json')));
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.join(__dirname, process.env.TPL || 'slp.html'));
  await p.evaluate(d => init(d), tl);
  if (only) {
    for (const s of only.split(',')) {
      await p.evaluate(t => render(t), +s);
      await p.screenshot({ path: path.join(vdir, `prev_${s}.png`) });
    }
    await b.close(); return;
  }
  const ff = spawn('ffmpeg', ['-y', '-v', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-',
    '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', path.join(vdir, 'mudo.mp4')]);
  const N = Math.ceil(tl.duration * FPS);
  for (let i = 0; i < N; i++) {
    await p.evaluate(t => render(t), i / FPS);
    const buf = await p.screenshot({ type: 'jpeg', quality: 92 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (i % 300 === 0) console.log(`frame ${i}/${N}`);
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
  await b.close();
})();
