# SEO-Grundlage und Seitenarchitektur

Stand: 14.09.2026. Freigegebener Umfang: technische Korrekturen, bestehender Anfrageweg, Prüfungen, Planung für Phase 2. Keine Veröffentlichung.

## Spezifikation dieser Phase

Ziel: Qualifizierte Anfragen von Inhabern deutscher Dentallabore, die Zahnarztpraxen als Kunden gewinnen wollen. Die bestehende Startseite bleibt die zentrale Leistungsseite. Das statische HTML, lokale CSS/JavaScript und der Anfrageweg über das Kundenportal bleiben erhalten.

Grundlage: Produktionszweig `main`, Commit `273be1a780130b0a7f6a9d9f485c582b7ace81ff`. Eigener Arbeitsbaum und Zweig `codex/seo-grundlage-2026-09-14`. Andere Arbeitsbäume und Änderungen werden nicht übernommen oder überschrieben.

Struktur: vorhandene HTML-Dateien bleiben die Seitenquelle, `CNAME` ist die verbindliche Hostquelle. Kein CMS, keine Laufzeitbibliothek und keine SEO-Engine. Neue Prüfungen in `tests/`, lokaler Vorschau-Server in `scripts/`, Dokumentation hier. Keine bestehenden README-, Test-, Paketmanager- oder Build-Dateien auf `main` vorhanden. Die Teststruktur eines separaten Relaunchentwurfs gehört nicht zu diesem Produktionsstand.

Kleine Aufgaben mit Abnahme:
1. Metadaten, Sitemap und interne URL-Schreibweisen berichtigen. HTML-Parser prüft jede Seite, jede Canonical-URL und sämtliche Sitemap-Ziele.
2. Anfragebedienung gezielt absichern, Formular und Calendly erhalten. Browser prüft CTA, Validierung, Fehler und bestätigte Antwort ausschließlich mit abgefangenen Schnittstellen.
3. Lokale Vorschau standardmäßig gegen Indexierung schützen. HTTP-Prüfung unterscheidet Vorschau und explizite lokale Produktionssimulation; unbekannte Seiten bleiben 404.
4. Themenmatrix und konkrete Briefings erstellen. Keine Artikel, leeren Bereichsseiten oder öffentlichen Entwürfe anlegen.
5. Gesamte Änderung auf Korrektheit, Verständlichkeit, Architektur, Sicherheit und Performance prüfen. Kein Push, Merge, Deploy oder Schreiben in externe Systeme.

Prüfbefehle nach Umsetzung: `python3 -m unittest discover -s tests -v`; `python3 scripts/serve.py`; Browserprüfung mit vorhandenem Playwright und installiertem Chrome. Kein TypeScript, Linter oder Compiler im Produktionsrepository. Vorhandene JavaScript-Syntax zusätzlich mit Node prüfen. Artefakte außerhalb des Website-Verzeichnisses.

## Belege und Grenzen der Keyword-Zuordnung

Beobachtung: Die vollständig gelesene Startseite bietet Kundenprofil, Einstiegsangebot, Anzeigen über soziale Medien/Google, automatische Vorqualifizierung und Übergabe passender Praxisanfragen. AGB Ziffer 3 bestätigt diesen Leistungsumfang. Die Gespräche und Abschlüsse führt das Labor. Recruiting-Zahlen und die allgemeine Bewerbergarantie werden nicht übernommen. Das bestehende Angebot nennt 12 Praxisanfragen in 90 Tagen; dessen Erfüllung wurde hier nicht geprüft.

Suchprüfung am 14.09.2026: Abfragen „Neukundengewinnung Dentallabor Zahnarztkunden Akquise“ und „Dentallabor Marketing Zahnarztpraxen Kunden gewinnen“ über die verfügbare Websuche. Keine kontrollierte Google-DE-SERP, keine Volumendaten und keine Rankingmessung. Die zurückgegebenen Treffer enthalten sowohl direkte Akquisedienstleister als auch breitere Marketingangebote mit Patientenbezug. Primäre Angebotsseiten als Beispiele: [Dental Akquise](https://dental-akquise.com/), [Marketingpraxis](https://www.dentallabor-marketing.de/marketingpraxis-neue-kunden-f%C3%BCr-ihr-dentallabor/), [dentalmedia](https://www.dentalmedia.de/praxismarketingblog/marketing-dentallabore.html). Diese Seiten belegen lediglich unterschiedliche Angebotsausrichtungen, keine Marktgröße und keine Leistungsfähigkeit unseres Angebots.

Hypothese: Die vier kommerziellen Ausgangsbegriffe betreffen hier dieselbe Aufgabe des Laborinhabers. Die Startseite ist deshalb der stärkste vorhandene Kandidat für dieses gemeinsame Suchbedürfnis. Empfehlung: zuerst die vorhandene Zuständigkeit festigen und erst bei abweichenden Nutzungsaufgaben zusätzliche Inhalte veröffentlichen.

Search Console: Kein angebundener Search-Console-Zugriff und kein Export im bearbeiteten Repository festgestellt. Indexstatus, Suchnachfrage und bisherige organische Anfragen bleiben unbekannt. Keine site:-Suche als Indexierungsbeweis verwendet.

## URL- und Keyword-Matrix

Alle URLs beziehen sich auf `https://www.laboraquise.de`. Slugs mit Status „später“ sind reine Planung und existieren nicht als öffentliche Dateien oder Links.

| Prio | URL | Suchbedürfnis und Cluster | Rolle und Abgrenzung | Status | Begründung und Unsicherheit |
|---|---|---|---|---|---|
| P1 | `/` | Hilfe bei Neukundengewinnung für Dentallabore, Akquise für Dentallabore, neue Zahnarztkunden, Zahnarztpraxen als Kunden gewinnen | Zentrale kommerzielle Leistungsseite, tatsächliches Verfahren und Anfrage | verbessern | Angebot und Zielgruppe passen bereits. Keine Suchvolumen-/Conversiondaten. Keine parallele `/neukundengewinnung-dentallabor/`, `/akquise-dentallabor/` oder `/zahnarztkunden-gewinnen/`. |
| P1 | `/termin/` | Erstgespräch mit Laboraquise vereinbaren | Buchung für bereits interessierte Laborinhaber, kein zweiter Leistungsartikel | verbessern | Erreichbare Calendly-Buchung. Keine primäre generische Keyword-Seite. 30 Minuten live verifiziert. |
| P1 | `/#leistungen` | Marketing zur Gewinnung von Zahnarztpraxen | Abschnitt erklärt die tatsächlich angebotenen Kampagnen | erhalten | Breiteres Marken-, Patienten- oder Bestandskundenmarketing ist nicht als eigenständiges Angebot belegt. `/dentallabor-marketing/` vorerst nicht anlegen. |
| P1 | `/#about` | Anbieter und Erfahrung prüfen | Vorhandener Über-uns-Abschnitt | erhalten | Verantwortlicher ist sichtbar, kein Bedarf für leere Über-uns-Seite. Erfahrungsaussagen benötigen für spätere Ausweitung eigene Belege. |
| P1 | `/#referenzen` | Anbieter vertrauen | Vorhandene Stimmen, ausdrücklich aus Personalgewinnung | erhalten | Nicht als Akquise-Fallstudien verkaufen. Keine leere `/ergebnisse/` oder `/referenzen/` anlegen. |
| P1 | `/impressum/` | Anbieteridentität und Kontakt | Vertrauens-/Rechtsinformation | verbessern | Selbst-Canonical und Beschreibung ergänzt. Kein Akquise-Keywordziel. |
| P1 | `/datenschutz/` | Datenverarbeitung verstehen | Vertrauens-/Rechtsinformation | verbessern | Metadaten und Links korrigiert. Aktualität der genannten Auftragsverarbeiter separat prüfen. |
| P1 | `/agb/` | Vertragsbedingungen verstehen | Öffentlich lesbarer Vertragstext, bestehendes noindex bleibt | verbessern | Nicht als SEO-Zielseite behandeln; aus Sitemap entfernt. |
| P2, Inhalt 1 | `/wissen/warum-zahnaerzte-das-dentallabor-wechseln/` | Wechselgründe verstehen | Informational, Entscheidungssituationen der Praxis statt Dienstleistung erklären | später | Anschluss an sichtbare Lieferzeit-/Erreichbarkeitsthemen; echte Interview-/Fallbelege fehlen. |
| P2, Inhalt 2 | `/wissen/abhaengigkeit-von-zahnarztpraxen-reduzieren/` | Konzentrationsrisiko im Labor erkennen und bearbeiten | Betriebswirtschaftliche Selbstprüfung, keine pauschale Neukunden-Anleitung | später | Vorhandenes Problem auf Startseite; keine universellen Grenzwerte oder Umsatzzahlen erfinden. |
| P2, Inhalt 3 | `/wissen/dentallabor-positionierung/` | Passung zu einer Praxis konkret ausdrücken | Leistungsprofil und nachweisbare Zusagen erarbeiten | später | Eigener praktischer Nutzen, Beispielprofile und fachliche Prüfung fehlen. |
| P2, Inhalt 4 | `/wissen/aussendienst-oder-externe-akquise/` | Vertriebswege nach Aufwand und Eignung vergleichen | Neutrale Entscheidungshilfe mit realem eigenen Verfahren | später | Nicht suggerieren, dass Laboraquise Außendienst verkauft. Keine Rechtsratschläge. |
| P2, Inhalt 5 | `/wissen/social-media-zahnarztpraxen-erreichen/` | Eignung sozialer Medien für B2B-Anfragen einschätzen | Kanalgrenzen und Qualifizierung, keine Recruiting-/Patientenstrategie | später | Tatsächliche Kanal- und Qualitätsdaten fehlen. Erst nach Erkenntnissen aus Inhalt 1 veröffentlichen. |

Keine Stadtseiten, Branchenkopien, überlappenden Methodenleitfäden oder automatischen Zusammenlegungen. Bestehende URLs werden erhalten. Ein Wissensverzeichnis wird erst zusammen mit dem ersten fertigen Inhalt angelegt und erhält eine echte Übersicht; vorher gibt es keine Navigation dorthin.

## Priorisierte Briefings

### Zuerst die Startseite fachlich absichern

Title bereits umgesetzt: „Neukundengewinnung für Dentallabore | Laboraquise.de“.
H1 bleibt: „Neue Zahnarztpraxen für Ihr Dentallabor gewinnen.“

Abschnitte: Wer angesprochen wird; was als qualifizierte Anfrage zählt; Kundenprofil und Kampagnenverfahren; welche Aufgaben beim Labor bleiben; belastbare Anbietererfahrung; Garantie samt Bedingungen; Erstgespräch. Vorhandene Gliederung nutzen, kein Relaunch.

Benötigte Belege: freigegebenes Musterangebot für Garantievoraussetzungen; echte Definition und deduplizierte Auswertung von Praxisanfragen; Freigaben für Aussagen zur Anbietererfahrung; Herkunft und Einordnung der vorhandenen Referenzen. Die derzeitige Termin-Verknappung ist nicht mit realer Verfügbarkeit verknüpft und darf nicht als Messwert behandelt werden.

Interne Links: `/#leistungen`, `/#about`, `/#referenzen`, `/termin/`, `/agb/`, `/datenschutz/`. CTA: „Erstgespräch vereinbaren“. Bestehendes Formular mit anschließender Kalenderweiterleitung nutzen. Der aktuelle Kalender nennt 30 Minuten. Keine Potenzialanalyse, regionale Praxiszahlen oder sofortigen Ergebnisse ergänzen.

### Fachinhalt 1: Wechselgründe

Title-Entwurf: „Warum Zahnärzte ihr Dentallabor wechseln | Laboraquise.de“.
H1-Entwurf: „Warum Zahnärzte ihr Dentallabor wechseln“.
Abschnitte: konkreter Anlass; Lieferzuverlässigkeit und Abstimmung; fachliche Passung; Umgang mit Nacharbeit; Entscheidungsweg beim Wechsel; überprüfbare Selbstfragen für das Labor. Unterschiedliche Ursachen und einzelne Erfahrungsberichte nicht als allgemeine Häufigkeiten ausgeben.
Belege: anonymisierte, zur Nutzung freigegebene Aussagen aus echten Praxisgesprächen; konkrete Beispiele; Gegenprüfung durch fachkundige Labor-/Praxisperson. Keine erfundenen Autoren, Zitate oder Prozentwerte.
Links: zur Startseite mit „Neukundengewinnung für Dentallabore“ und zum tatsächlich veröffentlichten Wissensverzeichnis. Spätere Artikel erst verlinken, wenn sie existieren.
CTA: „Erstgespräch vereinbaren“, zunächst echter Link zur vorhandenen `/termin/`-Seite. Keine gemeinsame CTA-Komponente nötig, solange kein realer Wiederverwendungsbedarf besteht.

### Fachinhalt 2: Abhängigkeit reduzieren

Title-Entwurf: „Abhängigkeit von einzelnen Zahnarztpraxen reduzieren | Laboraquise.de“.
H1-Entwurf: „Wie abhängig ist Ihr Dentallabor von einzelnen Praxen?“.
Abschnitte: eigene Konzentration ermitteln; Kapazität und Spezialisierung berücksichtigen; Bestandskunden betreuen; zusätzliche passende Praxen erschließen; Maßnahmen nach Aufwand priorisieren.
Belege: freigegebenes anonymes Rechenbeispiel mit Zeitraum und nachvollziehbaren Ausgangswerten; fachliche Prüfung der Interpretation. Keine universelle Risikoschwelle.
Links: Startseite, fertiger Wechselgründe-Artikel, Wissensübersicht.
CTA: „Erstgespräch vereinbaren“ über `/termin/`.

### Fachinhalt 3: Positionierung

Title-Entwurf: „Dentallabor gegenüber Zahnarztpraxen positionieren | Laboraquise.de“.
H1-Entwurf: „Wofür soll eine Zahnarztpraxis Ihr Dentallabor wählen?“.
Abschnitte: passende Arbeiten und Praxistypen; belegbare Leistungsmerkmale; Zusammenarbeit und Grenzen; ein ausgefülltes Leistungsprofil; Anschluss an Erstkontakt und Kundenprofil.
Belege: authentisches, freigegebenes Profil eines Labors, tatsächliche Liefer-/Abstimmungsprozesse und überprüfbare Fachkompetenz. Keinen erfundenen Qualitätsvorsprung formulieren.
Links: Startseite, Wechselgründe, Wissensübersicht. CTA: „Erstgespräch vereinbaren“.

## Minimale Grundlage für spätere Inhalte

Die bestehenden handgeschriebenen HTML-Seiten reichen für diese Phase aus. Kein zusätzliches Datenmodell implementieren. Den ersten Entwurf außerhalb des öffentlich ausgelieferten Repository-Wurzelverzeichnisses erstellen. GitHub Pages veröffentlicht aktuell direkt die Wurzel mit `.nojekyll`; deshalb sind bloße Ordnernamen wie `drafts` kein sicherer Ausschluss.

Redaktionelle Vorlage für Phase 2: Slug; Seitentyp `Fachartikel`; Status `Entwurf` oder `zur Veröffentlichung freigegeben`; Title; Description; vollständiger Inhalt; belegte Quellen; vorgesehene interne Links. Autor nur bei tatsächlicher Verantwortlichkeit. Datum erst bei echter Veröffentlichung bzw. relevanter Änderung. Nach Freigabe HTML mit einer H1, Selbst-Canonical, vorhandenem Seitenstil und Terminlink erstellen. Sitemap erst danach ergänzen und Tests aktualisieren. Article/BreadcrumbList nur bei tatsächlich eingeführter redaktioneller Struktur.

## Messplan und Consent-Grenze

Beobachtung: Die Website bindet derzeit keinen Analyseanbieter ein und sagt dies auch in Banner und Datenschutzerklärung. GTM-/Pixel-Blöcke sind leer. Der bestehende Formularcode übergibt UTM-Parameter an das eigene Portal. Er sendet kein organisches Einstiegsseiten- oder Referrer-Feld. Ein allgemeiner URL-Kopierer wurde entfernt, weil er beliebige Parameter an alle Links einschließlich Kontakt-/Rechtslinks anhängte. Das Formular liest seine UTM weiterhin aus der aktuellen URL; funktionale Calendly-Parameter bleiben erhalten.

Daher jetzt keine neuen Analytics-Ereignisse und keine bloße Datensammlung ohne Empfänger einbauen. Auswertung bleibt ein konkreter Folgeauftrag mit verifiziertem Portal-Datenmodell und freigegebenem Consent-Konzept:

1. Search Console lesend anbinden oder Export für mindestens einen benannten vollständigen Zeitraum bereitstellen. Seiten/Queries getrennt aggregiert nach Impressionen, Klicks und Position prüfen. Vorher keine Nullwerte behaupten.
2. Im Portal zuerst existierende Felder und Deduplizierung prüfen. „Anfrage bestätigt“ entspricht einer serverseitig gespeicherten Anfrage, nicht einem Absendeversuch. „Termin gebucht“ und „qualifizierter Lead“ sind getrennte Folgezustände.
3. Nur nach verifizierter Datenannahme und Datenschutzabgleich eine bereinigte Einstiegsroute und aggregierte Herkunft vorsehen. Keine Namen, E-Mails, Telefonnummern oder vollständigen URLs in Analytics. Keine ungeprüfte Erweiterung des Formularschemas in dieser Phase.
4. Falls ein bestehender consentfähiger Analysekanal freigegeben wird: Ereignis für primären CTA-Klick und erfolgreiche serverbestätigte Anfrage; Idempotenzschlüssel bzw. bestätigte Vorgangs-ID zur Vermeidung von Doppelzählung verwenden. Bestehende Ereignisnamen zuerst prüfen.
5. Organische Einstiegsseite → bestätigte Anfragen → qualifizierte CRM-Vorgänge monatlich aggregiert vergleichen. Search-Console-Suchanfragen lassen sich nicht individuell einem Lead zuordnen. Ausbleibende oder abgelehnte Einwilligung und direkte Kalenderbuchungen als Messlücken ausweisen.

## Einsatzfertiger Auftrag für Phase 2

> Bearbeite zuerst die bestehende Startseite von Laboraquise.de anhand des freigegebenen Angebots und echter Belege zur Praxisakquise. Prüfe Garantiebedingungen, Anbietererfahrung und die unbelegte Termin-Verknappung. Erstelle danach genau einen nicht öffentlichen Entwurf für `/wissen/warum-zahnaerzte-das-dentallabor-wechseln/`. Nutze freigegebene Aussagen aus Praxisgesprächen und eine fachliche Gegenprüfung. Erhalte das Design und den bestehenden Anfrageweg. Ergänze den Wissensbereich, öffentliche Links und Sitemap erst mit einem vollständigen, freigegebenen Inhalt. Erstelle keine zweite kommerzielle Akquise-Seite. Führe die vorhandenen SEO- und Browserprüfungen erneut aus. Veröffentliche erst nach separater Freigabe.

Ungeklärt bleiben die tatsächliche organische Nachfrage, der Google-Indexstatus, die serverseitige Leadzuordnung und die noch fehlenden fachlichen Veröffentlichungsbelege.
