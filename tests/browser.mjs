import { chromium } from "playwright-core";
import AxeBuilder from "@axe-core/playwright";
import fs from "node:fs";
import assert from "node:assert/strict";
const base = "http://localhost:4587";
const out = "scrollcraft/builds/praezision/qa";
fs.mkdirSync(out, { recursive: true });
const browser = await chromium.launch({ channel: "chrome", headless: true });
const report = [];
let failures = 0;
async function context(options = {}) {
  const c = await browser.newContext(options);
  await c.addInitScript(() => {
    Element.prototype.requestPointerLock = () => Promise.resolve();
    Element.prototype.setPointerCapture = () => {};
    Element.prototype.releasePointerCapture = () => {};
  });
  return c;
}
for (const [width, height] of [
  [1440, 900],
  [1100, 800],
  [768, 1024],
  [390, 844],
  [320, 740],
  [360, 640],
]) {
  const c = await context({ viewport: { width, height } });
  const p = await c.newPage();
  const errors = [];
  p.on("pageerror", (e) => errors.push(e.message));
  await p.goto(base);
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(350);
  const row = { width, height, states: [], errors };
  const hero = await p.locator(".hero .button").boundingBox();
  row.ctaVisible = hero.y + hero.height < height;
  await p.screenshot({ path: `${out}/${width}-hero.png` });
  const sections = await p
    .locator("main>section")
    .evaluateAll((els) =>
      els.map((el) => ({
        id: el.id,
        top: el.offsetTop,
        height: el.offsetHeight,
        pin: el.dataset.scAct === "pin",
      })),
    );
  for (let i = 0; i < sections.length; i++) {
    const section = sections[i];
    const positions = section.pin ? [0, 0.2, 0.4, 0.6, 0.8, 1] : [0, 0.5];
    for (const progress of positions) {
      await p.evaluate(
        (y) => scrollTo({ top: y, behavior: "instant" }),
        section.top +
          (section.pin
            ? section.height - height
            : Math.max(0, section.height - height)) *
            progress,
      );
      await p.waitForTimeout(220);
      const state = await p.evaluate(() => ({
        overflow: document.documentElement.scrollWidth - innerWidth,
        broken: [...document.images]
          .filter((x) => x.complete && x.naturalWidth === 0)
          .map((x) => x.src),
        phase: document.querySelector(".workbench").dataset.scVerifyState,
        stage: (() => {
          const x = document
            .querySelector(".process-caption")
            .getBoundingClientRect();
          return { top: x.top, bottom: x.bottom };
        })(),
      }));
      row.states.push({ section: i, progress, ...state });
      await p.screenshot({
        path: `${out}/${width}-s${i}-${Math.round(progress * 100)}.png`,
      });
    }
  }
  await p.goto(base);
  await p.waitForTimeout(250);
  const a11y = await new AxeBuilder({ page: p })
    .withTags(["wcag2a", "wcag2aa", "wcag21aa"])
    .analyze();
  row.accessibility = a11y.violations.map((v) => ({
    id: v.id,
    impact: v.impact,
    nodes: v.nodes.map((n) => ({
      target: n.target,
      summary: n.failureSummary,
    })),
  }));
  row.failed =
    !row.ctaVisible ||
    errors.length > 0 ||
    row.states.some((s) => s.overflow > 1 || s.broken.length) ||
    row.accessibility.length > 0;
  if (row.failed) failures++;
  report.push(row);
  console.log(
    width,
    row.failed ? "FAIL" : "OK",
    JSON.stringify({
      cta: row.ctaVisible,
      errors,
      overflow: Math.max(...row.states.map((s) => s.overflow)),
      a11y: row.accessibility,
    }),
  );
  await c.close();
}
// Alle echten Bedienelemente mit ihren Folgen prüfen.
{
  const c = await context({
    viewport: { width: 1440, height: 900 },
    permissions: ["clipboard-read", "clipboard-write"],
  });
  const p = await c.newPage();
  await p.goto(base);
  await p.waitForTimeout(400);
  await p.locator("#weg").scrollIntoViewIfNeeded();
  await p.locator('[data-phase="3"]').click();
  await p.waitForTimeout(180);
  const before = await p
    .locator(".workbench")
    .getAttribute("data-sc-verify-state");
  await p.selectOption("#region", "fern");
  await p.selectOption("#focus", "implantat");
  await p.waitForTimeout(180);
  const matched = await p
    .locator(".practice.is-match")
    .evaluateAll((els) =>
      els.map((el) => ({ region: el.dataset.region, focus: el.dataset.focus })),
    );
  assert.deepEqual(matched, [{ region: "fern", focus: "implantat" }]);
  await p.locator(".fit-check input").nth(0).check();
  await p.locator(".fit-check input").nth(2).check();
  await p.locator(".conversation-note summary").click();
  const note = await p.locator("#note").inputValue();
  assert(
    note.includes("Überregional") &&
      note.includes("Implantatprothetik") &&
      note.includes("Freie Kapazität"),
  );
  await p.locator("#copy-note").click();
  assert.equal(await p.evaluate(() => navigator.clipboard.readText()), note);
  await p.locator(".faqs details").first().locator("summary").click();
  assert.equal(
    await p.locator(".faqs details").first().getAttribute("open"),
    "",
  );
  await p.locator(".closing .button").click();
  await p.waitForURL("**/termin/");
  const localLinks = await p
    .locator("a")
    .evaluateAll((a) => a.map((x) => x.href));
  assert(
    localLinks.some((l) =>
      l.includes("calendly.com/hansetalent/laboraquise-erstgesprach"),
    ),
  );
  report.push({
    interactions: "OK",
    matching: matched,
    note,
    phaseState: before,
  });
  await c.close();
}
for (const mode of ["reduced", "no-js", "failed-media"]) {
  const c = await context({
    viewport: { width: 390, height: 844 },
    reducedMotion: mode === "reduced" ? "reduce" : "no-preference",
    javaScriptEnabled: mode !== "no-js",
  });
  const p = await c.newPage();
  if (mode === "failed-media")
    await p.route("**/*.{avif,png,jpg,webp}", (r) => r.abort());
  await p.goto(base);
  await p.waitForTimeout(450);
  await p.screenshot({ path: `${out}/${mode}-hero.png` });
  await p.locator("#weg").scrollIntoViewIfNeeded();
  await p.screenshot({ path: `${out}/${mode}-peak.png` });
  const steps = await p.locator(".process-steps li").count();
  assert.equal(steps, 4);
  if (mode !== "failed-media")
    assert.equal(await p.locator(".process-steps li:visible").count(), 4);
  assert(
    (await p.locator(".hero .button").getAttribute("href")) === "/termin/",
  );
  report.push({ mode, status: "OK" });
  await c.close();
}
{
  const c = await context({ viewport: { width: 390, height: 844 } });
  const p = await c.newPage();
  await p.goto(base);
  await p.locator(".menu-toggle").click();
  assert(await p.locator("#mobile-nav").isVisible());
  await p.keyboard.press("Escape");
  assert(!(await p.locator("#mobile-nav").isVisible()));
  await p.locator(".menu-toggle").click();
  await p.locator("#mobile-nav a").first().click();
  assert(!(await p.locator("#mobile-nav").isVisible()));
  await p.goto(base);
  const focus = [];
  for (let i = 0; i < 14; i++) {
    await p.keyboard.press("Tab");
    focus.push(
      await p.evaluate(() => ({
        text: document.activeElement.textContent.trim().slice(0, 70),
        tag: document.activeElement.tagName,
        outline: getComputedStyle(document.activeElement).outlineStyle,
      })),
    );
  }
  report.push({ keyboard: focus });
  await c.close();
}
fs.writeFileSync(`${out}/results.json`, JSON.stringify(report, null, 2));
await browser.close();
if (failures) process.exitCode = 1;
