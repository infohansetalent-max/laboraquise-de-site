// Vorhandenes Playwright verwenden. Keine Installation, keine echten Anfragen.
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
const moduleName = process.env.PLAYWRIGHT_MODULE;
const { chromium } = await import(moduleName ? pathToFileURL(moduleName).href : 'playwright-core');
const base = process.env.SEO_BASE_URL || 'http://127.0.0.1:4595';
assert(['127.0.0.1', 'localhost'].includes(new URL(base).hostname), 'Nur lokale Testziele erlaubt');
const out = process.env.SEO_ARTIFACT_DIR || fs.mkdtempSync(path.join(os.tmpdir(), 'laboraquise-seo-'));
fs.mkdirSync(out, { recursive: true });
const browser = await chromium.launch({ channel: 'chrome', headless: true });
const results = [];
const endpoint = 'https://portal.lokalejobsuche.de/api/eigenvertrieb/submit';
const calendar = 'https://calendly.com/hansetalent/laboraquise-erstgesprach';
async function context(width, options = {}) {
  const c = await browser.newContext({ viewport: { width, height: 900 }, ...options });
  await c.route('**/*', async route => {
    const u = new URL(route.request().url());
    if (u.origin === new URL(base).origin) return route.continue();
    if (u.origin === 'https://assets.calendly.com') return route.fulfill({ contentType: 'text/javascript', body: '' });
    if (u.hostname === 'calendly.com') return route.fulfill({ contentType: 'text/html; charset=utf-8', body: '<!doctype html><title>Kalender-Test</title><h1>Termin auswählen (Testantwort)</h1>' });
    return route.abort();
  });
  return c;
}
try {
  for (const width of [320, 390, 1440]) {
    const c = await context(width);
    const p = await c.newPage();
    const errors = [];
    const consoleMessages = [];
    p.on('console', m => { if (['error', 'warning'].includes(m.type())) consoleMessages.push({ type: m.type(), text: m.text() }); });
    p.on('pageerror', e => errors.push(e.message));
    for (const route of ['/', '/termin/', '/impressum/', '/datenschutz/', '/agb/', '/wissen/', '/wissen/warum-zahnaerzte-das-dentallabor-wechseln/']) {
      consoleMessages.length = 0;
      const response = await p.goto(base + route);
      assert.equal(response.status(), 200);
      assert.equal(response.headers()['x-robots-tag'], 'noindex, nofollow');
      await p.evaluate(() => document.fonts.ready);
      assert(await p.locator('h1').innerText());
      assert.equal(await p.locator('link[rel="canonical"]').getAttribute('href'), 'https://www.laboraquise.de' + route);
      assert.equal(await p.locator('nextjs-portal, vite-error-overlay').count(), 0);
      const before = await p.evaluate(() => performance.getEntriesByType('navigation')[0].domContentLoadedEventEnd);
      const overflow = [];
      let brokenImages = [];
      for (let y = 0; y < await p.evaluate(() => document.documentElement.scrollHeight); y += 700) {
        await p.evaluate(y => scrollTo({ top: y, behavior: 'instant' }), y);
        await p.waitForTimeout(45);
        overflow.push(await p.evaluate(() => document.documentElement.scrollWidth - innerWidth));
      }
      brokenImages = await p.locator('img').evaluateAll(images => images.filter(i => i.complete && !i.naturalWidth).map(i => i.getAttribute('src')));
      assert(Math.max(...overflow) <= 1, `Überlauf ${route} ${width}`);
      assert.deepEqual(brokenImages, [], `Bilder ${route}`);
      await p.evaluate(() => scrollTo(0, 0));
      await p.waitForTimeout(250);
      await p.screenshot({ path: path.join(out, `page-${route.replaceAll('/', '') || 'home'}-${width}.png`), fullPage: true });
      assert.deepEqual(consoleMessages.filter(m => m.type === 'error'), [], `Konsole ${route}`);
      results.push({ route, width, consoleMessages: [...consoleMessages], status: 'PASS', maxOverflow: Math.max(...overflow), brokenImages, initialAndDOMH1: true, domContentLoadedMs: Math.round(before) });
    }
    await p.goto(base + '/?utm_source=seo-test&email=private%40example.invalid&topic=implantat');
    await p.locator('[fs-cc="deny"]').first().click({ timeout: 4000 });
    // Redaktionelle Änderung: Beispielrechnung mit null, Standard und Obergrenze.
    const numberAt = async id => Number((await p.locator('#' + id).innerText()).replace(/[^0-9]/g, ''));
    for (const [amount, practices] of [[12000, 2], [0, 0], [30000, 5]]) {
      await p.locator('#salary').fill(String(amount));
      await p.locator('#impact').fill(String(practices));
      await p.waitForTimeout(800);
      assert.equal(await numberAt('totalAmount'), amount * practices * 12);
      assert.equal(await numberAt('perMonth'), amount * practices);
      assert.equal(await numberAt('perDay'), Math.round(amount * practices * 12 / 365));
      assert.equal(await numberAt('perWeek'), Math.round(amount * practices * 12 / 52));
    }
    await p.locator('#salary').fill('12000');
    await p.locator('#impact').fill('2');
    assert.match(await p.locator('.calc-explain').innerText(), /keine Prognose/);
    const caption = p.locator('.vorteile_image-wrapper.has-caption p');
    await caption.scrollIntoViewIfNeeded();
    assert(await caption.evaluate(el => {
      const a = el.getBoundingClientRect(), b = el.parentElement.getBoundingClientRect();
      return a.left >= b.left - 1 && a.right <= b.right + 1 && a.top >= b.top - 1 && a.bottom <= b.bottom + 1;
    }), 'Schemahinweis liegt vollständig in der Grafikbox');
    const faqs = p.locator('[data-accordion-toggle]');
    for (const faq of await faqs.all()) {
      await faq.click();
      const item = faq.locator('..');
      assert.equal(await item.getAttribute('data-accordion-status'), 'active');
      const answer = item.locator('.accordion-css__item-bottom-content');
      await answer.waitFor({ state: 'visible' });
      await p.waitForTimeout(400);
      const clipped = await answer.evaluate(el => {
        const rect = el.getBoundingClientRect();
        const parent = el.parentElement.getBoundingClientRect();
        return rect.bottom > parent.bottom + 2;
      });
      assert.equal(clipped, false, 'FAQ-Antwort vollständig sichtbar');
      await faq.click();
    }
    const popup = p.locator('[data-popup="popup"]');
    await p.locator('[data-popup="open"]').click();
    await popup.waitFor({ state: 'visible' });
    await p.waitForTimeout(500);
    assert.equal(await popup.locator('[data-timer], [data-day-container]').count(), 0);
    assert.match(await popup.innerText(), /30 Minuten/);
    const popupBox = await popup.boundingBox();
    assert(popupBox.x >= -1 && popupBox.x + popupBox.width <= width + 1);
    await p.screenshot({ path: path.join(out, `popup-${width}.png`) });
    await popup.locator('a[data-modal_1-trigger]').click();
    await p.locator('#wf-form-Erstgespraech').waitFor({ state: 'visible' });
    await p.keyboard.press('Escape');
    if (await popup.isVisible()) await popup.locator('[data-popup="close"]').click();
    results.push({ width, flow: 'Beispielrechner einschließlich null → alle FAQ → Terminfenster → Formular', status: 'PASS' });
    await p.evaluate(() => scrollTo({ top: 0, behavior: 'instant' }));
    const cta = p.locator('a[data-modal_1-trigger]:visible').first();
    await cta.click();
    const form = p.locator('#wf-form-Erstgespraech');
    await form.waitFor({ state: 'visible' });
    assert.match(await p.locator('.modal_1_content h2').innerText(), /30 Minuten/);
    // Sofortiges Schließen vor dem ersten Animationsbild muss ebenfalls funktionieren.
    await p.locator('.modal_1_dialog').evaluate(el => { el.tl?.pause(0); });
    await p.keyboard.press('Escape');
    await form.waitFor({ state: 'hidden' });
    await cta.focus();
    await p.keyboard.press('Enter');
    await form.waitFor({ state: 'visible' });
    assert.equal(new URL(p.url()).pathname, '/');
    assert.equal(await p.locator('a[href="/datenschutz/"]').first().getAttribute('href'), '/datenschutz/');
    const submit = form.locator('input[type="submit"]');
    await submit.click();
    assert.match(await form.locator('[role="alert"]').innerText(), /Namen/);
    await p.getByLabel('Vollständiger Name', { exact: true }).fill('SEO Test');
    await p.getByLabel('E-Mail', { exact: true }).fill('ungueltig');
    await p.getByLabel('Telefonnummer', { exact: true }).fill('0000000000');
    await p.getByLabel('Unternehmensname', { exact: true }).fill('Testlabor');
    await submit.click();
    assert.match(await form.locator('[role="alert"]').innerText(), /gültige E-Mail/);
    await p.getByLabel('E-Mail', { exact: true }).fill('seo@example.invalid');
    await submit.click();
    assert.match(await form.locator('[role="alert"]').innerText(), /Einwilligung/);
    await p.locator('#Einwilligung').check();
    let requests = 0;
    let key;
    const handler = async r => {
      requests++;
      const data = r.request().postDataJSON();
      assert.equal(data.angebot, 'laboraquise');
      assert.equal(data.consent, true);
      assert.deepEqual(data.utm, { source: 'seo-test' });
      assert(!JSON.stringify(data).includes('private@example.invalid'));
      if (key) assert.equal(data.idempotenz_schluessel, key);
      key = data.idempotenz_schluessel;
      if (requests === 1) return r.fulfill({ status: 500, contentType: 'application/json', body: JSON.stringify({ ok: true, calendly_url: calendar }) });
      if (requests === 2) return r.fulfill({ status: 200, contentType: 'application/json', body: '{ungueltig' });
      if (requests === 3) return r.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify({ ok: true, calendly_url: 'https://calendly.com.invalid/test' }) });
      if (requests === 4) return r.abort();
      return r.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify({ ok: true, calendly_url: calendar }) });
    };
    await c.route(endpoint, handler);
    for (let i = 0; i < 4; i++) {
      await submit.click();
      await form.locator('[role="alert"]').waitFor();
      assert.equal(new URL(p.url()).pathname, '/');
      assert.equal(await p.getByLabel('Vollständiger Name', { exact: true }).inputValue(), 'SEO Test');
      assert(await submit.isEnabled());
    }
    await p.screenshot({ path: path.join(out, `form-error-${width}.png`) });
    await submit.click();
    await p.waitForURL(calendar);
    assert.equal(await p.locator('h1').innerText(), 'Termin auswählen (Testantwort)');
    assert.equal(requests, 5);
    assert.deepEqual(errors, []);
    results.push({ width, flow: 'CTA → Formular → Validierung → HTTP/JSON/URL/Netzfehler → bestätigte Testantwort → Kalender-Testseite', status: 'PASS', requests, errors });
    await c.close();
  }
  const c = await context(390, { javaScriptEnabled: false });
  const p = await c.newPage();
  await p.goto(base + '/');
  assert.match(await p.locator('h1').innerText(), /Dentallabor/);
  await p.locator('a[data-modal_1-trigger]:visible').first().click();
  await p.waitForURL(base + '/termin/');
  await p.getByRole('link', { name: 'Termin in einem neuen Fenster aussuchen' }).waitFor();
  results.push({ flow: 'Ohne JavaScript: Startseite → CTA → Terminseite mit Calendly-Ersatzlink', status: 'PASS' });
  await c.close();
} finally {
  await browser.close();
  fs.writeFileSync(path.join(out, 'browser-results.json'), JSON.stringify(results, null, 2));
}
console.log(JSON.stringify(results, null, 2));
console.log('Artefakte: ' + out);
