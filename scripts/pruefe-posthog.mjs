import assert from 'node:assert/strict';
import { readFileSync, readdirSync, existsSync } from 'node:fs';
import vm from 'node:vm';
import { createHash, randomUUID } from 'node:crypto';

const code = readFileSync(new URL('../assets/marketing/posthog-pilot.js', import.meta.url), 'utf8');
const key = 'phc_test_key_without_real_project';
let tests = 0;
function check(label, fn) { fn(); tests++; console.log('OK ' + label); }
check('Offizielles SDK-Bundle ist unveraendert', () => {
  const sdk = readFileSync(new URL('../assets/marketing/posthog-1.444.0.no-external.js', import.meta.url));
  assert.equal(createHash('sha256').update(sdk).digest('hex'), 'e3552c24c94a8b6df68401bb64d592d454a97942f33e828fef9e8c5a9d04d5b0');
});
function browser(address, jar = new Map(), options = {}) {
  const listeners = {}, scripts = [], captured = [];
  let config, optedOut = options.sdkOptOut === true;
  const location = new URL(address);
  const document = {
    referrer: options.referrer || '',
    get cookie() { return [...jar].map(([k, v]) => k + '=' + v).join('; '); },
    set cookie(value) {
      const [pair, ...attrs] = value.split(';');
      const i = pair.indexOf('=');
      if (attrs.some(a => a.trim() === 'Max-Age=0')) jar.delete(pair.slice(0, i));
      else jar.set(pair.slice(0, i), pair.slice(i + 1));
    },
    addEventListener(name, fn) { listeners['doc:' + name] = fn; },
    createElement() { return {}; },
    head: { appendChild(script) { scripts.push(script); } },
  };
  const client = {
    capture(event, properties) {
      if (options.captureError) throw new Error("SDK-Testfehler");
      if (optedOut) return;
      const value = config.before_send({ event, properties: { ...properties, $current_url: address, $initial_referrer: 'https://private.example/person?email=secret@example.de', email: 'secret@example.de', $set: { name: 'Privat' } } });
      if (value) captured.push(JSON.parse(JSON.stringify(value)));
    },
    opt_out_capturing() { optedOut = true; },
    opt_in_capturing() { optedOut = false; },
    stopSessionRecording() {},
  };
  const window = {
    location, crypto: { randomUUID }, navigator: { doNotTrack: options.dnt || '' },
    matchMedia() { return { matches: options.mobile || false }; },
    addEventListener(name, fn) { listeners[name] = fn; },
    dispatchEvent(event) { listeners[event.type]?.(event); },
    posthog: { init(_key, next) { config = next; config.loaded(client); } },
  };
  vm.runInNewContext(code, { window, document, URL, URLSearchParams, Date, Set, CustomEvent: class { constructor(type) { this.type = type; } } });
  const api = window.LjsPostHog;
  api.configure({ enabled: options.enabled !== false, projectKey: options.key ?? key, audience: options.audience, contentId: options.contentId });
  function load() { scripts.at(-1)?.onload(); }
  function click(preview = false) {
    listeners['doc:click']({ target: { closest: () => ({ hasAttribute: () => preview, getAttribute: () => 'https://portal.lokalejobsuche.de/start?quelle=vsl' }) } });
  }
  return { api, jar, scripts, captured, load, click, client, config: () => config };
}


const pages=JSON.parse(code.match(/var pages = (\[[^;]+\]);/)[1]);
check('14 Seiten: keine Messung vor Zustimmung, gültige Ereignisse danach, Widerruf stoppt',()=>{
 assert.equal(pages.length,14);
 for(const path of pages){
  const html=readFileSync(new URL('../'+(path==='/'?'index.html':path.slice(1)+'/index.html'),import.meta.url),'utf8');
  assert.equal((html.match(/data-posthog-consent/g)||[]).length,1);
  const b=browser('https://www.laboraquise.de'+path);assert.equal(b.scripts.length,0);
  b.api.allow();b.load();assert.equal(b.captured[0].properties.site,'laboraquise.de');assert.equal(b.captured[0].properties.page_path,path);
  b.api.decline();assert.equal(b.jar.get('lba-ph-consent-v2'),'no');assert.equal(b.jar.has('lba-ph-visitor-v2'),false);
  const before=b.captured.length;b.api.lead({ok:true,eingang_id:randomUUID()},true);assert.equal(b.captured.length,before);
 }
});
check('Fremde Marke, Vorschau, Testparameter, DNT und fremde Einwilligung aktivieren nichts',()=>{
 for(const url of ['https://lokalejobsuche.de/','https://preview.vercel.app/','https://www.laboraquise.de/?ljs_tracking_test=0']){
  const b=browser(url);b.api.allow();assert.equal(b.scripts.length,0);
 }
 assert.equal(browser('https://www.laboraquise.de/',new Map([['ljs-ph-consent-v2','yes']])).scripts.length,0);
 const dnt=browser('https://www.laboraquise.de/',new Map(),{dnt:'1'});dnt.api.allow();assert.equal(dnt.scripts.length,0);
});
check('Eingang nur mit HTTP-Erfolg und UUID, ohne Duplikat oder Formularwerte',()=>{
 const b=browser('https://www.laboraquise.de/rueckruf/');b.api.allow();b.load();const valid={ok:true,eingang_id:randomUUID()};
 for(const value of [{ok:true},{...valid,doppelt:true},{...valid,ok:false}])b.api.lead(value,true);
 b.api.lead(valid,false);assert.equal(b.captured.length,2);b.api.lead(valid,true);b.api.lead(valid,true);assert.equal(b.captured.length,3);
 assert.equal(b.captured.at(-1).event,'lead_submitted');assert.doesNotMatch(JSON.stringify(b.captured),/secret|Privat|current_url|referrer|email|\$set/);
});
check('Eingebettete Buchung: genau einmal, Terminangabe bleibt lokal, Quelle wird geprüft',()=>{
 const b=browser('https://www.laboraquise.de/termin/');b.api.allow();b.load();b.api.embeddedBooked('bad');assert.equal(b.captured.length,1);
 b.api.embeddedBooked('2026-11-02T12:00:00Z');b.api.embeddedBooked('2026-11-02T12:00:00Z');assert.equal(b.captured.length,2);assert.equal(b.captured[1].event,'appointment_booked');assert.ok(!JSON.stringify(b.captured).includes('2026-11-02'));
 const html=readFileSync(new URL('../termin/index.html',import.meta.url),'utf8');assert.ok(html.includes('e.origin !== PORTAL'));assert.ok(html.includes('e.source === fenster.contentWindow'));
});
console.log(tests+' Prüfgruppen bestanden. Keine echten Daten oder Netzaufrufe.');
