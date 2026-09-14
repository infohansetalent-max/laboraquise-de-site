import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
const {chromium}=await import(process.env.PLAYWRIGHT_MODULE?pathToFileURL(process.env.PLAYWRIGHT_MODULE).href:'playwright-core');
const base=process.env.SEO_BASE_URL||'http://127.0.0.1:4598';
assert(['localhost','127.0.0.1'].includes(new URL(base).hostname),'Nur lokale Testziele');
const out=pathToFileURL((process.env.SEO_ARTIFACT_DIR||fs.mkdtempSync(path.join(os.tmpdir(),'wissen-browser-')))+path.sep);
fs.mkdirSync(out,{recursive:true});
const article='/wissen/warum-zahnaerzte-das-dentallabor-wechseln/';
const browser=await chromium.launch({channel:'chrome',headless:true});
const results=[];
try {
  for(const width of [320,390,1440]) {
    const context=await browser.newContext({viewport:{width,height:900},permissions:['clipboard-read','clipboard-write']});
    await context.route('**/*', r=>new URL(r.request().url()).origin===base?r.continue():r.abort());
    const page=await context.newPage();
    const errors=[]; page.on('pageerror', e=>errors.push(e.message));
    page.on('console',m=>{if(m.type()==='error')errors.push(m.text());});
    for(const route of ['/wissen/',article]) {
      const response=await page.goto(base+route);
      assert.equal(response.status(),200);
      assert.equal(response.headers()['x-robots-tag'],'noindex, nofollow');
      assert.equal(await page.locator('meta[name="robots"]').getAttribute('content'),'index, follow');
      assert.equal(await page.locator('h1').count(),1);
      await page.evaluate(()=>document.fonts.ready);
      assert.equal(await page.evaluate(()=>document.fonts.check('17px "General Sans"')),true);
      const overflow=await page.evaluate(()=>document.documentElement.scrollWidth-innerWidth);
      assert(overflow<=1,`Überlauf ${route} ${width}: ${overflow}`);
      const links=await page.locator('a[href]').evaluateAll(as=>as.map(a=>a.getAttribute('href')));
      for(const href of links) {
        if(href.startsWith('#')) assert.equal(await page.locator(href).count(),1);
        else if(href.startsWith('/')) assert.equal((await context.request.get(base+href)).status(),200,href);
      }
      const clipped=await page.locator('p,h1,h2,li,td,th,summary,button').evaluateAll(nodes=>nodes.filter(el=>el.getClientRects().length && el.scrollWidth>el.clientWidth+2).map(el=>el.textContent.slice(0,80)));
      assert.deepEqual(clipped,[]);
      await page.screenshot({path:new URL(`${route===article?'article':'wissen'}-${width}.png`,out).pathname,fullPage:true});
      results.push({route,width,status:'PASS',overflow,links:links.length,clipped});
    }
    assert.equal(await page.locator('article section').count(),9);
    const checks=page.locator('.checklist input');
    assert.equal(await checks.count(),8);
    for(const box of await checks.all()) await box.check();
    assert.match(await page.locator('.checkcount').innerText(),/^8 von 8/);
    await checks.first().uncheck();
    assert.match(await page.locator('.checkcount').innerText(),/^7 von 8/);
    await page.locator('summary').click();
    await page.locator('#copy-button').click();
    await page.waitForFunction(()=>document.getElementById('copy-status').textContent.length>0);
    assert.equal(await page.locator('#copy-status').innerText(),'Gesprächseinstieg kopiert.');
    assert.equal(await page.evaluate(()=>navigator.clipboard.readText()),await page.locator('#copy-text').innerText());
    await page.evaluate(()=>Object.defineProperty(navigator,'clipboard',{value:{writeText:async()=>{throw new Error('Testfehler');}}}));
    await page.locator('#copy-button').click();
    await page.waitForFunction(()=>document.getElementById('copy-status').textContent.includes('manuell kopiert'));
    assert.match(await page.locator('#copy-status').innerText(),/manuell kopiert/);
    assert.equal(await page.evaluate(()=>getSelection().toString()),await page.locator('#copy-text').innerText());
    await page.locator('.toc a').first().click();
    assert.equal(new URL(page.url()).hash,'#abschnitt-1');
    await page.locator('article a.button').click();
    await page.waitForURL(base+'/termin/');
    assert(await page.getByRole('link',{name:'Termin in einem neuen Fenster aussuchen'}).count());
    // Kalenderressourcen sind absichtlich blockiert. Keine reale Terminbuchung.
    assert.deepEqual(errors.filter(e=>!e.includes('net::ERR_FAILED')),[]);
    results.push({width,status:'PASS',flow:'Prüfliste, Kopieren und Fehlerfall, Sprungmarke, Artikel → Termin'});
    await context.close();
  }
  const context=await browser.newContext({viewport:{width:390,height:900},javaScriptEnabled:false});
  await context.route('**/*',r=>new URL(r.request().url()).origin===new URL(base).origin?r.continue():r.abort());
  const page=await context.newPage();await page.goto(base+article);
  await page.locator('summary').click();assert(await page.locator('#copy-text').isVisible());
  assert.equal(await page.locator('#copy-button').isVisible(),false);
  await page.locator('.checklist input').first().check();
  await page.locator('article a.button').click();await page.waitForURL(base+'/termin/');
  results.push({status:'PASS',flow:'Ohne JavaScript: ganzer Artikel, Text aufklappen, Prüfliste, Terminlink'});
  for(const path of ['/docs/seo/PLAN.md','/assets/','/Wechselgruende-Entwurf.md','/unbekannt/']) assert.equal((await context.request.get(base+path)).status(),404);
  assert.equal((await context.request.get(base+'/wissen',{maxRedirects:0})).status(),301);
  assert((await (await context.request.get(base+'/sitemap.xml')).text()).includes('/wissen/'));
  results.push({status:'PASS',flow:'Private Dateien und unbekannte URL 404; Slash-Redirect; Sitemap mit freigegebenen Wissensseiten'});
} finally {await browser.close();fs.writeFileSync(new URL('results.json',out),JSON.stringify(results,null,2));}
console.log(JSON.stringify(results,null,2));
