# Laboraquise.de

## Freiwillige Statistik, 01.11.2026

Ben hat PostHog für die öffentlichen Seiten von lokalejobsuche.de und laboraquise.de freigegeben. Die 14 öffentlichen Seiten sind mit PR 19 und Commit `292907f79e7c81d2e9a191b4f8e0b44dfa32cf23` auf GitHub Pages veröffentlicht und live geprüft. Die aktuelle Cookie-Auswahl ist mit PR 20 und Commit `fc295a8f9bd499694268009d948ef267f8983781` veröffentlicht. Direkte Portal-Buchungen sind mit Portal-PR 336, Commit `14b7833b3a81dc417629c039daf3cad9d65542d5`, aktiv.

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

### Live-Nachweis, 01.11.2026

GitHub Pages meldet den aktuellen Seitencommit als gebaut; der ausgelieferte Messclient stimmt per SHA-256 mit dem Quellstand überein. Alle 14 Seiten laden ohne erneute Auswahl nach gültiger Zustimmung. Vor Zustimmung und nach Ablehnung beziehungsweise Widerruf wird kein Analyse-SDK geladen. Der Widerruf wurde mit erneutem Seitenaufruf geprüft.

Im EU-Projekt wurden 29 technische Prüfeinträge gelesen: Seitenaufrufe aller 14 Pfade, Einstiegsereignisse und ein Formularbeginn ohne Absenden. Die Testkennung `2f546916-5e91-434d-9adb-a7e3a580f3e8` gehört nicht zum Besucherverkehr. Sie ist im gespeicherten Dashboard-Standardfilter und ausdrücklich in der SQL-Seitenübersicht ausgeschlossen. Keine echten Anfragen oder Buchungen wurden als Test erzeugt. Die kontrollierten Ereignisfelder enthielten ausschließlich die vorgesehenen Kategorien und technischen Kennungen.

[Laboraquise-Dashboard](https://eu.posthog.com/project/329103/dashboard/1074311): Seiten `Rr0Iy6IP`, bestätigte Anfragen/Buchungen `PI42pmbk`, Anfragefunnel `m1QN6s6c`. Die PostHog-Oberfläche zählt zustimmende Browser, keine eindeutigen Menschen und keinen gesamten Websiteverkehr.

Die direkten Laboraquise-Buchungsseiten wurden nach dem Portal-Deploy aufgerufen. Sie zeigen die separate kompakte Zustimmung; eine lokalejobsuche-Zustimmung aktiviert Laboraquise nicht. Ablehnung und Neuladen laden kein SDK. Eingebettete Buchungen verwenden weiterhin die Entscheidung der umgebenden Laboraquise-Seite.
