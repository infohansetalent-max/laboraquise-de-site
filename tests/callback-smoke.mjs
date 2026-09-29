import assert from 'node:assert/strict';
import { pathToFileURL } from 'node:url';

const moduleName = process.env.PLAYWRIGHT_MODULE;
const { chromium } = await import(moduleName ? pathToFileURL(moduleName).href : 'playwright-core');
const base = process.env.SEO_BASE_URL || 'http://127.0.0.1:4595';
assert(['127.0.0.1', 'localhost'].includes(new URL(base).hostname));
const browser = await chromium.launch({ channel: 'chrome', headless: true });

try {
  for (const width of [390, 1280]) {
    const page = await browser.newPage({ viewport: { width, height: 844 } });
    let payload;
    await page.route('https://portal.lokalejobsuche.de/api/eigenvertrieb/submit', async route => {
      payload = route.request().postDataJSON();
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({ ok: true, eingang_id: '00000000-0000-4000-8000-000000000001' }),
      });
    });
    await page.goto(base + '/?gclid=probe123');
    await page.locator('a[href^="/rueckruf/"]').first().click();
    assert.match(page.url(), /rueckruf\/\?gclid=probe123/);
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true);
    await page.getByRole('button', { name: 'Rückruf anfordern' }).click();
    assert.equal(await page.getByRole('alert').innerText(), 'Bitte geben Sie Ihren Namen an.');
    await page.getByRole('textbox', { name: 'Ihr Name' }).fill('Test Person');
    await page.getByRole('textbox', { name: 'Ihr Dentallabor' }).fill('Testlabor');
    await page.getByRole('textbox', { name: 'Telefonnummer für den Rückruf' }).fill('030 123456');
    await page.getByRole('textbox', { name: 'E-Mail-Adresse' }).fill('test@example.invalid');
    await page.getByRole('checkbox').check();
    await page.getByRole('button', { name: 'Rückruf anfordern' }).click();
    assert.equal(payload.angebot, 'laboraquise');
    assert.equal(payload.utm.anfrageart, 'rueckruf');
    assert.equal(payload.utm.term, 'gclid:probe123');
    await page.locator('#erfolg').waitFor({ state: 'visible' });
    assert.equal(await page.locator('#rueckruf-formular').isVisible(), false);
    console.log(width + ': Rückrufweg ohne echte Anfrage bestanden');
    await page.close();
  }
} finally {
  await browser.close();
}
