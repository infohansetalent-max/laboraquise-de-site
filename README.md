# Laboraquise.de

## Freiwillige Statistik, 01.11.2026

Ben hat PostHog für die öffentlichen Seiten von lokalejobsuche.de und laboraquise.de freigegeben. Diese Erweiterung ist vorbereitet und noch nicht live bestätigt.

Alle 14 öffentlichen HTML-Seiten verwenden dieselbe kompakte Cookie-Auswahl. Ein Klick erlaubt oder verweigert die Statistik; die Wahl lässt sich über Cookie-Einstellungen ändern. Es werden keine Werbetags ergänzt. Die PostHog-Daten liegen im vorhandenen EU-Projekt 329103. Die Ereignisse sind durch `site=laboraquise.de` und `pilot=lba-website-v1` von lokalejobsuche.de getrennt.

- Seitenaufrufe, feste Linkkategorien und Formularbeginn bzw. Sendeversuch.
- Neue Anfrage nur nach erfolgreicher Serverantwort, gültiger Eingangs-UUID und ohne Duplikat.
- Eingebettete Portalbuchung nur nach Abschlussmeldung aus dem tatsächlich eingebundenen Portal-Fenster. Der Termin bleibt lokal und wird nicht als Ereigniseigenschaft exportiert.
- Keine Namen, Kontaktdaten, Formularwerte, vollständigen URLs, Werbe-IDs oder Qualifikationsbewertungen. Keine Aufzeichnungen, kein Autocapture und keine Profile.

Eigene `lba-ph-*`-Cookies verhindern, dass eine frühere lokalejobsuche-Zustimmung hier gilt. Die Auswahl gilt 180 Tage, die zufällige Kennung höchstens 90 Tage und die Einstiegszuordnung einen Tag. Das Portal nutzt für direkte Laboraquise-Buchungen eine getrennte Auswahl. Im eingebetteten Kalender wird kein zweiter Messclient geladen; die umgebende Website bleibt zuständig. Externe Calendly-Seiten gehören nicht zur eigenen Website-Statistik.

### Dateien und Prüfung

`assets/marketing/posthog-pilot.js` ist die für Laboraquise abgegrenzte Fassung des Messclients. Der öffentliche Projekttoken steht in `posthog-config.js`. `posthog-consent.js` und `.css` liefern die gemeinsame Auswahllogik und Gestaltung. Das unveränderte SDK und seine Lizenz liegen daneben. Die aktuelle Einbindung und Datenbegrenzung stehen in `datenschutz/index.html`.

`node scripts/pruefe-posthog.mjs` prüft Abdeckung, Einwilligung, Widerruf, Markentrennung, Erfolgsbedingungen und Feldbegrenzung ohne externe Aufrufe. `node scripts/pruefe-datenschutzauswahl.mjs` prüft die Ein-Klick-Auswahl, getrennte Entscheidungen und die Wiederaufnahme gespeicherter Entscheidungen. Die Darstellung wurde auf allen 14 Seiten bei 390 und 1280 Pixeln geprüft: 28 Fälle ohne Überlauf, gleich große Schaltflächen ab 44 Pixeln Höhe.

Auslieferung: GitHub Pages, Zweig `main`, eigene Domain `www.laboraquise.de`. Ein grüner lokaler Test oder PR ist noch kein Live-Nachweis. Nach Veröffentlichung Seitenstand und tatsächlichen Ereigniseingang prüfen.
