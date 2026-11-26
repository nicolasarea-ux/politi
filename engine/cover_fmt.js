const { chromium } = require('playwright');const fs=require('fs'),path=require('path');
(async()=>{const [guion,out]=process.argv.slice(2);const g=JSON.parse(fs.readFileSync(guion));
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
 await p.goto('file://'+path.join(__dirname,'fmt.html'));await p.evaluate(async g=>{renderCover(g);await document.fonts.ready},g);await p.waitForTimeout(200);
 await p.screenshot({path:out,type:'jpeg',quality:95});await b.close()})();
