# Spezifikation: Laboraquise Neufassung

Ziel: Inhaber von Dentallaboren verstehen die Gewinnung passender Praxisanfragen und erreichen den vorhandenen Terminweg. Hochwertige fotografische Website mit einer individuellen Auswahlsequenz.

Technik: bestehendes statisches HTML, CSS, JavaScript. Unveränderte Scroll Craft Engine. Keine neue Laufzeitarchitektur. Native Links, Details und Formularelemente statt Komponentenframework.
Struktur: index.html als tatsächliche Startseite; assets/praezision für eigenes CSS und JS; assets/vendor für unveränderte Engine; tests für Browserprüfung; scrollcraft/builds/praezision für Briefing und Belege.
Befehle: npm run dev startet lokale Vorschau. npm test prüft Verhalten im installierten Chrome. npm run check prüft Syntax und lokale Verweise. Keine Buildstufe notwendig.
Stil: semantisches HTML, zentrale Designvariablen, klar benannte Funktionen. Beispiel: `const selectedRegion = regionSelect.value;`. Keine sichtbaren Gedankenstriche, keine erfundenen Zahlen.
Prüfung: Desktop 1440, Laptop 1100, Tablet 768, Telefon 390 und 320 Pixel, reduzierte Bewegung, Medienausfall, kein JavaScript, Tastatur, Links, Calendly ohne Buchung. Screenshots an Zwischenständen und Kontaktbögen öffnen. Gemessene Überläufe, Konsolenfehler, Bilder und Kontrast prüfen.
Grenzen: Immer ursprüngliche Änderungen sichern und separaten Zweig nutzen. Produktivveröffentlichung nur nach Freigabe. Keine echten Buchungen, Formularnachrichten oder bezahlten Bildaufrufe. Rechtstexte unverändert.
Erfolg: klare Heroaussage und CTA sofort sichtbar, erklärende Auswahlsequenz mit vollständiger statischer Alternative, keine leeren Scrollstrecken, keine horizontalen Überläufe, geprüfte Vorschau geöffnet.
