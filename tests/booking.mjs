import { chromium } from "playwright-core";
import fs from "node:fs";
const browser = await chromium.launch({ channel: "chrome", headless: true });
const context = await browser.newContext({
  viewport: { width: 1100, height: 800 },
});
await context.addInitScript(() => {
  Element.prototype.requestPointerLock = () => Promise.resolve();
  Element.prototype.setPointerCapture = () => {};
  Element.prototype.releasePointerCapture = () => {};
});
const page = await context.newPage();
await page.goto("http://localhost:4587/termin/");
await page.waitForTimeout(5000);
console.log(
  "frames",
  page.frames().map((f) => f.url()),
);
for (const frame of page.frames())
  if (frame.url().includes("calendly.com"))
    console.log(
      "Kalender",
      (await frame.locator("body").innerText()).slice(0, 1300),
    );
await page.screenshot({
  path: "scrollcraft/builds/praezision/qa/termin.png",
  fullPage: true,
});
await page.goto("https://www.laboraquise.de/");
await page.waitForTimeout(1500);
await page.screenshot({
  path: "scrollcraft/builds/praezision/qa/bestand-live.png",
});
console.log("LIVE", await page.title());
await page.goto("https://www.zeiss.com/meditec/en/home.html", {
  waitUntil: "domcontentloaded",
});
await page.waitForTimeout(1500);
await page.screenshot({
  path: "scrollcraft/builds/praezision/qa/referenz-zeiss.png",
});
await page.evaluate(() => scrollTo(0, 700));
await page.waitForTimeout(500);
await page.screenshot({
  path: "scrollcraft/builds/praezision/qa/referenz-zeiss-scroll.png",
});
await browser.close();
