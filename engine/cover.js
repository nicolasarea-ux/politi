// guion -> portada 1080x1920 (lo importante dentro del recorte 3:4 de la cuadrícula de Instagram)
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const [guion, out] = process.argv.slice(2);
  const g = JSON.parse(fs.readFileSync(guion));
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.join(__dirname, 'slp.html'));
  await p.evaluate(async g => { await document.fonts.ready; await renderCover(g); }, g);
  await p.waitForTimeout(150);
  await p.screenshot({ path: out, type: 'jpeg', quality: 92 });
  await b.close();
})();
