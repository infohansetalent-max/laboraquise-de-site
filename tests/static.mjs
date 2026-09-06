import fs from "node:fs";
import { createHash } from "node:crypto";
import assert from "node:assert/strict";
const html = fs.readFileSync("index.html", "utf8");
const visible = html
  .replace(/<style[\s\S]*?<\/style>/g, "")
  .replace(/<script[\s\S]*?<\/script>/g, "");
assert(
  !/[—–]/.test(visible),
  "Keine Gedankenstriche in neuen sichtbaren Inhalten",
);
assert.equal((html.match(/<h1\b/g) || []).length, 1);
assert(
  !/12 Praxisanfragen|76 Verträge|garantierte Termine|Wir rufen an/.test(
    visible,
  ),
);
for (const match of html.matchAll(/(?:href|src)="([^"]+)"/g)) {
  const url = match[1];
  if (/^(https?:|data:|tel:|mailto:)/.test(url)) continue;
  if (url.startsWith("#")) {
    assert(html.includes(`id="${url.slice(1)}"`), url);
    continue;
  }
  const file = "." + url + (url.endsWith("/") ? "index.html" : "");
  assert(fs.existsSync(file), "Fehlendes Ziel " + url);
}
for (const ext of ["js", "css"])
  assert.equal(
    fs.readFileSync(`assets/vendor/scrollcraft.${ext}`, "utf8"),
    fs.readFileSync(
      `.agents/skills/scroll-craft/engine/scrollcraft.${ext}`,
      "utf8",
    ),
    "Engine unverändert",
  );
const legal = JSON.parse(fs.readFileSync("tests/legal-sha256.json", "utf8"));
for (const [name, hash] of Object.entries(legal))
  assert.equal(
    createHash("sha256")
      .update(fs.readFileSync(`${name}/index.html`))
      .digest("hex"),
    hash,
    "Rechtstext unverändert " + name,
  );
console.log(
  "OK: Semantik, lokale Verweise, Aussagen, unveränderte Engine und Rechtstexte.",
);
