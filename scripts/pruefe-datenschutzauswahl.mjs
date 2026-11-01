import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import vm from 'node:vm';

const code = readFileSync(new URL('../assets/marketing/posthog-consent.js', import.meta.url), 'utf8');
function surface({ consent = '', advertising = '', withAds = true } = {}) {
  const events = {}, actions = [];
  const el = () => ({ hidden: true, checked: false, open: false, addEventListener(_type, fn) { this.click = fn; }, focus() {} });
  const panel = el(), open = el(), statistic = el(), marketing = withAds ? el() : null, allow = el(), decline = el(), save = el(), details = el(), footer = el();
  panel.querySelector = () => decline;
  const nodes = {'[data-privacy-panel]': panel, '[data-privacy-open]': open, '[data-privacy-statistik]': statistic, '[data-privacy-werbung]': marketing, '[data-posthog-allow]': allow, '[data-posthog-decline]': decline, '[data-privacy-save]': save, '[data-privacy-details]': details};
  const box = { hidden: true, querySelector: s => nodes[s] };
  const window = { addEventListener: (event, fn) => events[event] = fn, LjsPostHog: {
    available: () => true, consent: () => consent,
    allow() { consent = 'yes'; actions.push('statistic:yes'); events['ljs:posthog-consent'](); },
    decline() { consent = 'no'; actions.push('statistic:no'); events['ljs:posthog-consent'](); },
  }, ...(withAds ? {LjsWerbung: {consent: () => advertising, choose(value) {advertising = value; actions.push('advertising:' + value);}}} : {}) };
  vm.runInNewContext(code, {window,document:{querySelector:()=>box,querySelectorAll:()=>[footer]}});
  return {panel,statistic,marketing,allow,decline,save,footer,actions,events};
}

const first = surface();
assert.equal(first.panel.hidden,false);
assert.deepEqual(first.actions,[],'Keine Zustimmung beim Anzeigen');
assert.equal(first.statistic.checked,false);
assert.equal(first.marketing.checked,false);
first.allow.click();
assert.deepEqual(first.actions,['statistic:yes','advertising:ja'],'Ein Klick erlaubt beide klar benannten Zwecke');
assert.equal(first.panel.hidden,true);
first.events['ljs:posthog-consent']();
assert.equal(first.panel.hidden,true,'Kein zweites Popup nach Bestätigung');
first.footer.click();
assert.equal(first.panel.hidden,false);
first.decline.click();
assert.deepEqual(first.actions.slice(-2),['statistic:no','advertising:nein'],'Widerruf beider Zwecke in einem Klick');

const individual = surface();
individual.statistic.checked=true;
individual.save.click();
assert.deepEqual(individual.actions,['statistic:yes','advertising:nein'],'Statistik ist unabhängig von Werbung');
const onlyAdvertising = surface();
onlyAdvertising.marketing.checked=true;
onlyAdvertising.save.click();
assert.deepEqual(onlyAdvertising.actions,['statistic:no','advertising:ja'],'Werbung ist unabhängig von Statistik');

const oldAdvertising = surface({advertising:'ja'});
assert.equal(oldAdvertising.statistic.checked,false,'Alte Werbezustimmung erlaubt keine Statistik');
assert.equal(oldAdvertising.panel.hidden,false);
assert.deepEqual(oldAdvertising.actions,[]);
const existing = surface({consent:'no', advertising:'nein'});
assert.equal(existing.panel.hidden,true,'Keine Wiederholung bei bekannter Entscheidung');
const statisticsFirst = surface({consent:'yes', advertising:''});
assert.equal(statisticsFirst.panel.hidden,true,'Kein zweiter Dialog nach einer Statistikentscheidung auf einer Seite ohne Werbetags');
assert.deepEqual(statisticsFirst.actions,[],'Keine automatische Freigabe der bislang unentschiedenen Werbung');
const statisticsOnly = surface({withAds:false});
statisticsOnly.allow.click();
assert.deepEqual(statisticsOnly.actions,['statistic:yes'],'Keine erfundene Werbeoption auf Seiten ohne Werbetags');
console.log('Datenschutzauswahl geprüft: ein Klick, getrennte Zwecke, keine Vorauswahl oder automatische Einwilligung, keine wiederholte Abfrage, Widerruf erreichbar. Keine Netzaufrufe.');
