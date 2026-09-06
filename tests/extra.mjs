import { chromium } from "playwright-core";
import AxeBuilder from "@axe-core/playwright";
import assert from "node:assert/strict";
import fs from "node:fs";
const out = "scrollcraft/builds/praezision/qa";
fs.mkdirSync(out, { recursive: true });
const browser = await chromium.launch({ channel: "chrome", headless: true });
const c = await browser.newContext({ viewport: { width: 1440, height: 900 } });
await c.addInitScript(() => {
  Element.prototype.requestPointerLock = () => Promise.resolve();
  Element.prototype.setPointerCapture = () => {};
  Element.prototype.releasePointerCapture = () => {};
});
const p = await c.newPage();
const result = {};
await p.goto("http://localhost:4587/");
await p.waitForTimeout(300);
await p.mouse.move(780, 250);
await p.waitForTimeout(250);
await p.screenshot({ path: out + "/pointer-left.png" });
await p.mouse.move(1270, 600);
await p.waitForTimeout(250);
await p.screenshot({ path: out + "/pointer-right.png" });
const heroMove = [];
for (const y of [0, 200, 400]) {
  await p.evaluate((y) => scrollTo({ top: y, behavior: "instant" }), y);
  await p.waitForTimeout(180);
  heroMove.push(
    await p
      .locator(".hero-scene [data-sc-parallax]")
      .evaluateAll((els) =>
        els.map((el) => ({
          rate: el.dataset.scParallax,
          transform: getComputedStyle(el).transform,
        })),
      ),
  );
  await p.screenshot({ path: `${out}/hero-depth-${y}.png` });
}
result.heroDepth = heroMove;
await p.locator("#weg").scrollIntoViewIfNeeded();
result.phases = [];
for (let i = 0; i < 4; i++) {
  await p.locator(`[data-phase="${i}"]`).click();
  await p.waitForTimeout(180);
  assert.equal(
    await p.locator(".process-steps .is-active").innerText(),
    await p.locator(".process-steps li").nth(i).innerText(),
  );
  result.phases.push(
    await p.locator(".workbench").getAttribute("data-sc-verify-state"),
  );
}
result.combinations = [];
for (const region of ["nah", "fern"])
  for (const focus of ["kronen", "implantat", "schienen"]) {
    await p.selectOption("#region", region);
    await p.selectOption("#focus", focus);
    await p.waitForTimeout(100);
    const matches = await p.locator(".practice.is-match").count();
    assert.equal(matches, 1);
    result.combinations.push({ region, focus, matches });
  }
for (const [width, height] of [
  [1440, 900],
  [390, 844],
  [320, 740],
]) {
  await p.setViewportSize({ width, height });
  await p.goto("http://localhost:4587/termin/");
  await p.waitForTimeout(2800);
  const overflow = await p.evaluate(
    () => document.documentElement.scrollWidth - innerWidth,
  );
  assert.equal(overflow, 0);
  const frame = p
    .frames()
    .find((f) => f.url().startsWith("https://calendly.com/hansetalent/"));
  assert(frame);
  await frame.getByText("September 2026", {exact:true}).first().waitFor({timeout:15000});
  const calendarText = await frame.locator("body").innerText();
  assert(calendarText.includes("September 2026"));
  console.log("Kalender",width,calendarText.slice(0,250));
  const a11y = await new AxeBuilder({ page: p })
    .exclude("iframe")
    .withTags(["wcag2a", "wcag2aa"])
    .analyze();
  result["booking-" + width] = {
    overflow,
    calendar: true,
    violations: a11y.violations.map((v) => ({
      id: v.id,
      nodes: v.nodes.map((n) => n.target),
    })),
  };
  await p.screenshot({ path: `${out}/termin-${width}.png`, fullPage: true });
}
// Produktive Terminverfügbarkeit lesen, keine Reservierung oder Buchung absenden.
await p.goto("https://calendly.com/hansetalent/laboraquise-erstgesprach");
await p.waitForTimeout(1800);
if (await p.getByRole("button", { name: "Alle ablehnen", exact: true }).count())
  await p.getByRole("button", { name: "Alle ablehnen", exact: true }).click();
const buttons = await p.getByRole("button").all();
result.calendarButtons = [];
for (const b of buttons) {
  const name = await b.getAttribute("aria-label");
  if (name && /September|September/i.test(name))
    result.calendarButtons.push(name);
}
const day = p
  .getByRole("button", { name: /7\. September|Montag, 7|Monday, September 7/i })
  .first();
if (await day.count()) {
  await day.click();
  await p.waitForTimeout(800);
  result.times = (await p.locator("body").innerText()).match(
    /\b\d{2}:\d{2}\b/g,
  );
  await p.screenshot({ path: out + "/calendly-times.png" });
}
await p.setViewportSize({ width: 1440, height: 900 });
await p.goto("https://www.zeiss.com/meditec/en/home.html", {
  waitUntil: "domcontentloaded",
});
await p.waitForTimeout(700);
if (await p.getByRole("button", { name: "Reject All", exact: true }).count())
  await p.getByRole("button", { name: "Reject All", exact: true }).click();
await p.screenshot({ path: out + "/referenz-zeiss.png" });
await p.evaluate(() => scrollTo({ top: 800, behavior: "instant" }));
await p.waitForTimeout(500);
await p.screenshot({ path: out + "/referenz-zeiss-scroll.png" });
await p.route("**/assets/vendor/scrollcraft.js", (r) => r.abort());
await p.goto("http://localhost:4587/");
await p.waitForTimeout(250);
assert.equal(await p.locator(".process-steps li:visible").count(), 4);
result.noEngine = "OK";
await p.screenshot({ path: out + "/no-engine.png", fullPage: true });
fs.writeFileSync(out + "/extra-results.json", JSON.stringify(result, null, 2));
console.log(JSON.stringify(result));
await browser.close();
