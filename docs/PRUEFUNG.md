# Prüfung der Neufassung

Stand: 06.09.2026. Lokale Vorschau: http://localhost:4587/

## Ergebnis
Die Website ist im tatsächlichen Git Projekt umgesetzt. Eigenständiger Arbeitsbaum auf codex/laboraquise-praezision-2026-09-06. Bestehende fremde Änderungen liegen weiterhin unverändert im ursprünglichen Arbeitsverzeichnis. Zusätzlich wurden sie vor Beginn als Archiv gesichert.

## Gestaltung
Heller Auftakt mit General Sans und Signalblau. Zwei getrennte fotografische Bildebenen und ein davor liegender Maßrahmen bewegen sich unabhängig. Die Motive bleiben in eigenen fotografischen Rahmen: keine behaupteten Freisteller oder echten Kundenaufnahmen. Vorhandene Beispiele wurden wiederverwendet, es gab keine neue Generierung.

Ein dunkler Auswahlbereich bildet den einzigen gehaltenen Höhepunkt. Beispielprofile werden nach Region und Schwerpunkt geordnet, ein passendes Profil rückt zum Labor. Die anschließenden Schritte unterscheiden Interesse, Prüfung, Anfrage und geschäftliches Gespräch. Die Darstellungsdaten sind ausdrücklich schematisch.

Der Passungscheck und die Auswahl ergeben eine kopierbare Gesprächsnotiz. Sie wird lokal erzeugt und nicht an einen Empfänger gesendet. Alle primären Aktionen heißen „Erstgespräch vereinbaren“ und führen zum bestehenden Kalender.

## Tatsächlich ausgeführt
- npm run check: Syntax, lokale Pfade, ein H1, problematische Aussagen, unveränderte Engine und SHA256 Vergleich der drei Rechtstexte.
- npm test: installiertes Chrome im Headlessbetrieb mit 1440×900, 1100×800, 768×1024, 390×844, 320×740 und 360×640. Auf jedem Bildschirm heroische CTA innerhalb der ersten Ansicht, keine horizontalen Überläufe, keine Seitenfehler, keine defekten geladenen Bilder. Abschnittsaufnahmen und Zwischenstände des Auswahlbereichs.
- Axe Prüfung der Startseite in allen sechs Größen: keine gefundenen Verstöße der geprüften WCAG A/AA Regeln. Keine vollständige Zertifizierung.
- Alle sechs Kombinationen der beiden Regionen und drei Schwerpunkte geprüft: genau das passende schematische Profil wird gewählt. Alle vier Phasen per Knopf getestet.
- Passungswahl, Textübernahme, tatsächlicher Inhalt der Zwischenablage, FAQ, Mobilmenü, Escape und Tastaturfokus geprüft.
- Reduzierte Bewegung, deaktiviertes JavaScript, Ausfall der Bilddateien und separat Ausfall der Engine geprüft. Alle vier Prozessschritte bleiben lesbar. Ohne JavaScript sind die nicht ausführbaren Auswahlfelder deaktiviert.
- Scroll Craft shoot.mjs für Desktop, Telefon und reduzierte Bewegung: keine gemeldeten leeren Scrollstrecken. Die erfassten animierten Textzeilen erreichen im Kontrasttest mindestens 4,5:1. Statische Inhalte zusätzlich über Axe geprüft. Kontaktbögen und Detailaufnahmen geöffnet und beurteilt.
- Die Pointeränderung verändert tatsächlich Bildpixel; die Messung steht in qa/pointer-diff.json. Kein Pointer Lock oder Capture in automatisierten Browserkontexten.
- Terminseite auf 1440, 390 und 320 Pixeln: Kalenderinhalt lädt, keine horizontalen Überläufe, keine gefundenen Axe Verstöße im eigenen Seitenbereich. Die fremde Calendly Oberfläche wurde von dieser Axe Prüfung ausgenommen und gesondert funktional gelesen.
- Calendly zeigt freie Tage und nach Auswahl eines Tages Uhrzeiten. Keine Buchung erzeugt. Telefon und E-Mail verweisen auf die vorhandenen Angaben im Impressum.

## Gefundene und behobene Probleme
1. Eingebettete Grundvorlage gab der Auswahlfläche zusätzlichen Innenabstand. Eigene Layoutrollen setzen diese Dokumentabstände zurück. Vollständige Bedienung bleibt sichtbar.
2. Nicht passende Profile blieben im Endzustand als blasse Textreste stehen. Sie verschwinden nun vollständig und geben der passenden Verbindung Raum.
3. Der Zeilenumbruch der animierten Überschrift verschluckte ein Leerzeichen. HTML korrigiert und Bildfolge erneut geprüft.
4. Mobile Rasterpositionen waren zunächst nur im JavaScript gesetzt. Sie stehen jetzt zusätzlich im HTML und gelten auch ohne JavaScript.
5. Der bestehende Termintext vermischte Personalgewinnung und Praxisgewinnung. Die Terminseite folgt jetzt dem beschriebenen Angebot, bei unverändertem Terminziel.
6. Die externe Kalenderoberfläche verwendet auf Mobilgeräten „Wählen Sie einen Tag aus“ statt des Desktoptexts. Der Funktionstest wurde auf den tatsächlich geladenen Kalender und angebotene Zeiten ausgerichtet.

## Gestalterische Nachprüfung
Briefingkurve: Interesse, Wiedererkennung, Klarheit, Vertrauen, Entschlossenheit.
Wirkung der ersten Bildfolge: Sorgfalt, Nachdenken, Auswahl zunächst zu blass, Nachvollziehbarkeit, Ruhe. Hauptabweichung war der schwache Endzustand des Höhepunkts. Das vollständige Entfernen unpassender Profile macht die Verbindung zur stärksten Veränderung. Der Abschluss bleibt bewusst ruhig mit sichtbarem Button.

Abgleich mit der ersten Arbeitskomposition: Typografie, fotografischer Doppelrahmen und Farbwelt bleiben erhalten. Im Auswahlbereich wurden zusätzliche Abstände entfernt, die mobilen Profile vergrößert und die Endszene klarer gemacht. Keine nachträgliche Behauptung einer Designfreigabe.

## Fünf Achsen der Codeprüfung
Korrektheit: Alle Auswahlkombinationen, Kontaktwege und Rückfallzustände geprüft. Kein Erfolgstext ohne echten Kopiervorgang, kein Formular mit fingierter Übermittlung.
Lesbarkeit: Semantische HTML Abschnitte, formatierte eigene CSS/JS Dateien, getrennte Belege und Quellen. Inline Markenbasis bleibt wegen der vorgegebenen Schrifteinbettung im HTML.
Architektur: Statische Website, unveränderte gemeinsame Engine. Individuelle Logik in einer eigenen Datei. Alte Webflow und Sequenzskripte sind in der neuen Startseite nicht eingebunden.
Sicherheit: Keine neuen Datenspeicher, Schlüssel oder externen Übermittlungen auf der Startseite. Calendly Nachrichtenursprung auf exakte Domain begrenzt. Keine Testanfragen abgesendet.
Leistung: Bereits komprimierte AVIF Dateien, nachgelagerte Bilder lazy, kein Video und keine externe Schrift. Prüfungspakete sind nur Entwicklungsabhängigkeiten. npm audit meldet keine bekannten Schwachstellen.

## Grenzen und Freigaben
Browseremulation ist kein Test auf einem physischen Smartphone. Safari, iOS und reale Mobilfunkleistung wurden nicht gemessen. Keine Lighthouse Werte behauptet.
Die vorhandenen AGB sind als Entwurf bezeichnet. Juristische Freigabe und endgültige Angebote mit möglichen Garantien bleiben offen. Echte Kundenreferenzen und echte Laborfotos fehlen weiterhin.
GitHub Pages veröffentlicht laut gelesener Konfiguration nur main. Produktive Veröffentlichung und DNS Änderungen wurden nicht vorgenommen und brauchen eine gesonderte Entscheidung.

## Belege
Ausführbare Prüfungen: tests/static.mjs, tests/browser.mjs und tests/extra.mjs.
Maschinenberichte, Screenshots und Kontaktbögen: scrollcraft/builds/praezision/qa und harness-desktop, harness-mobile, harness-reduced. Frühere Bildstände liegen unter evidence-before-final. Diese großen lokalen Prüfdateien sind nicht Bestandteil der produktiven Website.
