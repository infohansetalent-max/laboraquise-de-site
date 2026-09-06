import { chromium } from "playwright-core";
import fs from "node:fs";
const out = "scrollcraft/builds/praezision/initial";
fs.mkdirSync(out, { recursive: true });
const browser = await chromium.launch({ channel: "chrome", headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
});
await context.addInitScript(() => {
  Element.prototype.requestPointerLock = () => Promise.resolve();
  Element.prototype.setPointerCapture = () => {};
  Element.prototype.releasePointerCapture = () => {};
});
const page = await context.newPage();
page.on("pageerror", (e) => console.log("ERROR", e.message));
await page.goto("http://localhost:4587/");
await page.waitForTimeout(1400);
await page.screenshot({ path: out + "/desktop.png" });
console.log(
  await page.evaluate(() => ({
    font: getComputedStyle(document.querySelector("h1")).fontFamily,
    overflow: document.documentElement.scrollWidth - innerWidth,
    acts: [...document.querySelectorAll("[data-sc-act]")].map((x) => ({
      id: x.id,
      h: x.offsetHeight,
      top: x.offsetTop,
      device: x.dataset.scAct,
    })),
    h1: document.querySelector("h1").getBoundingClientRect().toJSON(),
  })),
);
await page.locator("#weg").scrollIntoViewIfNeeded();
await page.waitForTimeout(1000);
await page.screenshot({ path: out + "/peak.png" });
await page.setViewportSize({ width: 390, height: 844 });
await page.goto("http://localhost:4587/");
await page.waitForTimeout(1000);
await page.screenshot({ path: out + "/mobile.png" });
await page.locator("#weg").scrollIntoViewIfNeeded();
await page.waitForTimeout(700);
await page.screenshot({ path: out + "/mobile-peak.png" });
await page.goto("https://calendly.com/hansetalent/laboraquise-erstgesprach");
await page.waitForTimeout(4000);
console.log(
  "CALENDLY",
  (await page.locator("body").innerText()).slice(0, 4500),
);
await page.screenshot({ path: out + "/calendly.png" });
await browser.close();
