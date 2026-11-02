import assert from 'node:assert/strict';
import { readFileSync, readdirSync } from 'node:fs';
import { join, relative } from 'node:path';
const root = new URL('..', import.meta.url).pathname;
const walk = dir => readdirSync(dir, {withFileTypes:true}).flatMap(e => e.isDirectory() && !['.git','node_modules'].includes(e.name) ? walk(join(dir,e.name)) : e.isFile() && e.name.endsWith('.html') ? [join(dir,e.name)] : []);
let anzahl = 0;
for (const path of walk(root)) {
 const html = readFileSync(path,'utf8');
 if (!html.includes('posthog-pilot.js')) continue;
 const tags = html.match(/<script[^>]+src="[^"]*seitenaufrufe\.js[^"]*"[^>]*>/g) || [];
 assert.equal(tags.length, 1, relative(root,path));
 const page = relative(root,path) === 'index.html' ? '/' : '/' + relative(root,path).replace(/\/index\.html$/, '');
 assert(tags[0].includes('data-seite="'+page+'"'), path);
 assert(tags[0].includes('data-website="laboraquise.de"'), path);
 anzahl++;
}
const js = readFileSync(join(root,'assets/marketing/seitenaufrufe.js'),'utf8');
assert(!/document\.cookie|localStorage|sessionStorage|document\.referrer|navigator\.|randomUUID/.test(js));
assert(js.includes("credentials: 'omit'"));
assert(js.includes("referrerPolicy: 'no-referrer'"));
console.log(`${anzahl} öffentliche Seiten: genau ein Zähler, feste Website/Seite, kein Browserspeicher.`);
