# SEO-Audit und Übergabe, Phase 1 und 2

Stand: 14.09.2026. Phase 2 im isolierten Arbeitsbaum umgesetzt und lokal geprüft. Nicht gepusht, nicht gemergt, nicht deployt. Die lesende Live-Prüfung betrifft ausschließlich den Ausgangsstand aus Phase 1. Die folgende Ergänzung hat bei Zustandsangaben Vorrang vor dem darunter dokumentierten Phase-1-Verlauf.

## Phase 2: Ergebnis und Beleggrenze

Die Startseite bleibt die einzige kommerzielle Akquise-Seite. Sie beschreibt das Verfahren und die Aufgaben des Labors. Ein vollständiger Fachartikel liegt als private Markdown-Datei außerhalb des Website-Roots vor. Er ist weder als Route noch als Navigations- oder Sitemap-Eintrag angelegt. Die fachliche Gegenprüfung, eine freigegebene echte Praxisstimme und die Veröffentlichungsfreigabe stehen aus. Phase 2 ist damit technisch und redaktionell vorbereitet, aber nicht fachlich zur Veröffentlichung abgenommen.

### Umgesetzte Änderungen

| Befund | Änderung | Nachweis und Grenze |
|---|---|---|
| Für die pauschale Zusage von zwölf Praxisanfragen in 90 Tagen liegt kein freigegebenes Praxisakquise-Angebot vor. Die gezielt gefundene Angebotsvorlage betrifft Recruiting. | Numerische Garantie aus allen Startseitenabschnitten entfernt. Bedingte Erklärung zu Anfragen, Angebot und Erstattungsumfang mit Links zu AGB-Ziffern 5, 6 und 16. Keine neue Garantie eingesetzt. | AGB vollständig gelesen, selbst als Entwurf gekennzeichnet. Rechtstext unverändert. Keine rechtliche Freigabe oder tatsächliche Garantieleistung behauptet. |
| Countdown und erzeugte Tagesauswahl zeigten keine Kalenderverfügbarkeit. | Knappheitstext, Countdown, Tagesauswahl, Online-Punkt und dazugehörige Datumsskripte entfernt. Terminfenster nennt 30 Minuten und verweist auf die anschließende Kalenderauswahl. | Terminfenster auf drei Breiten geöffnet und bis zum Formular bedient. Echte Kalenderbuchung nicht ausgeführt. |
| Pauschale Umsätze, Erfahrungsmengen, ein fixes Anrufverhältnis und Ergebnisse nach 30 Tagen waren nicht belegt. | Entsprechende Behauptungen entfernt oder als mögliche Situationen formuliert. Ablauf erklärt Aufgaben ohne zugesagten ersten Auftrag. | Vollständiger sichtbarer Startseitentext nach Änderung gelesen. Keine Übernahme allgemeiner Recruiting-Kennzahlen. |
| Rechner stellte frei gesetzte Eingaben als entgangenen Umsatz dar. | Deutliches Rechenbeispiel, eigene Eingaben, null möglich. Monatsumsatz je Praxis × Anzahl × 12; Jahreswert ÷ 365 beziehungsweise ÷ 52. Kosten/Gewinn nicht berechnet. | Standard 12.000 × 2 × 12 = 288.000 Euro; Monat 24.000, Tag gerundet 789, Woche gerundet 5.538 Euro. Auch null und obere Reglerwerte geprüft. Das sind Annahmen, keine Marktwerte. |
| Drei bestehende Zahlenanimationen schrieben auf denselben Rechnerwert. Der Browser zeigte 134.134 statt 288.000. | Zwei konkurrierende Animatoren entfernt; ein Animator bricht den vorherigen Frame bei neuer Eingabe ab. | Rechneranzeige gegen unabhängig berechnete Sollwerte geprüft. |
| „Fünf Labore“ war mit der sichtbaren Referenzliste unvereinbar. | Stimmen ausdrücklich als Personalgewinnung bei Hansetalent eingeordnet, Hausarztpraxis und doppelte Laborzugehörigkeit benannt. Bestehende Zitate/Zuordnungen nicht verändert. | Fünf Personen, drei verschiedene Dentallabore und eine Hausarztpraxis. Bestehende Ergebniszitate und Nutzungsfreigaben nicht unabhängig bestätigt. Keine Akquise-Fallstudie daraus gemacht. |
| Social-Bild enthält die nun zurückgestellte numerische Garantie. | OG/Twitter verwenden das vorhandene 512-Pixel-Markenzeichen. Bildtyp, Maße, Beschreibung und Kartenformat angepasst. | Bestehendes Bild visuell geprüft, keine Bildproduktion. Alte Bilddatei bleibt Bestandsasset; externe Caches nicht geändert. |
| Prozessillustration enthält eine fiktive Ergebnisanzeige. | Sichtbarer Hinweis „Schematische Darstellung, keine echten Suchergebnisse.“ ergänzt; auf Mobil unter der Grafik angeordnet. | Hinweis auf drei Breiten innerhalb seiner Grafikbox gemessen. Bestehendes Bild nicht verändert. |
| Datenschutzseite lief bei 320 Pixeln um 70 Pixel über, im Ausgangsstand reproduziert. | Wortumbruch im Haupttext ergänzt. | Nach Korrektur 0 Pixel Überlauf. Sichtbarer Rechtstext unverändert. |

### Artikel und Quellen

Geplant: `/wissen/warum-zahnaerzte-das-dentallabor-wechseln/`. Der vollständige private Entwurf enthält Metadaten, sechs fachliche Abschnitte, Selbstprüfung, Gesprächseinstieg und den vorhandenen Terminlink. Er enthält keine Platzhalter im Artikeltext, erfundenen Autoren, privaten Zitate oder vermeintlichen Kundenfälle. Ein konstruiertes Beispiel ist ausdrücklich so bezeichnet.

Die externe Primärquelle wurde am Original überprüft: [Ismail und Al-Moghrabi, BMC Oral Health 2023](https://link.springer.com/article/10.1186/s12903-023-03395-z). Zehn zahnärztliche und zehn zahntechnische Fachpersonen in Saudi-Arabien; Gegenstand ist Zusammenarbeit. Keine repräsentative deutsche Wechselstatistik. Praktische Selbstfragen werden als redaktionelle Vorschläge bezeichnet. Ein vollständig gelesenes internes Laborgespräch ersetzt keine direkte Praxisbefragung. Die darin angesprochene Referenzzusage gilt nicht automatisch für diesen Artikel. Eine gesonderte interne Quellen- und Freigabenübersicht bleibt außerhalb des Website-Roots.

### Prüfung Phase 2

| Prüfung | Status | Beleg |
|---|---|---|
| SEO und HTTP | PASS | Sechs bestehende Python-Testgruppen: alle fünf Seiten, Canonicals, Sitemap, Links/Anker, Schema, Preview-Header, Pfadbegrenzung und lokale 404. |
| Browser | PASS | 22 Fälle in Chrome: fünf Seiten bei 320, 390 und 1440 Pixel Breite; je Breite Rechner/FAQ/Terminfenster und gemockter Anfragepfad; zusätzlich JavaScript-freier CTA. |
| Darstellung | PASS im geprüften Umfang | Vollständiger Scroll-Durchlauf, 0 Pixel horizontaler Überlauf, keine defekten geladenen Bilder. Sämtliche FAQ geöffnet und Antworten auf Abschneiden gemessen. Zusätzliche Abschnittsaufnahmen geprüft. Eine zunächst abgeschnittene neue Bildunterschrift mobil korrigiert. |
| Anfrageweg | PASS, gemockt | Validierung, vier Fehlerarten, erhaltener Formularinhalt, stabiler Idempotenzschlüssel und bestätigte Testantwort bis Kalender-Testseite. Keine echte Anfrage versendet. |
| JavaScript | PASS | 22 ausführbare Inline-Blöcke über alle Seiten mit Node auf Syntax geprüft. Zwei bereits in Phase 1 belegte GSAP-Warnungen bleiben; keine neuen ungefangenen Skriptfehler. |
| Rechtstexte | PASS | Sichtbarer Inhalt von AGB, Impressum und Datenschutz gegen `cf6ff47` identisch. Nur Datenschutz-Umbruch neu. |
| Entwurfsgrenze | PASS lokal | Weiterhin genau fünf öffentliche HTML-Dateien. Kein Wissensverzeichnis, kein Artikel in Sitemap oder Navigation. Privater Text und Quellenübersicht liegen außerhalb des Repository-Roots. |
| Review | PASS für Technik und redaktionelle Abgrenzung | Unabhängiger Review über fünf Achsen. Veraltete Zustandsformulierungen im Plan korrigiert und wirkungslosen Datumstimer entfernt. Kein Ersatz für fachkundige Gegenprüfung. |
| Build, Typecheck, Lint | NICHT VORHANDEN | Unverändert statischer Export ohne solche Projektbefehle. |
| Echte Leads, Versand, Buchung | NICHT GEPRÜFT | Nur gemockte externe Antworten; keine echten Vorgänge. |
| Deploy, neue Live-Fassung, Google-Index | NICHT ERFOLGT / NICHT GEPRÜFT | Kein Push, Merge oder Deploy. Keine Search-Console-Daten. |
| Fachliche Inhaltsfreigabe | OFFEN | Benannte Fachperson, freigegebene Praxisstimme und Veröffentlichungsfreigabe fehlen. |

Geänderte Dateien gegenüber Phase 1: `index.html`, `datenschutz/index.html`, `tests/browser-smoke.mjs`, `docs/seo/AUDIT.md`, `docs/seo/PLAN.md`. Keine neue öffentliche URL. Kein neuer Dienst, keine Bibliothek und keine Hostingänderung. Browser- und Syntaxbelege liegen außerhalb des Website-Roots unter `work/phase2/`. Private Übergabedateien sind nicht Teil des Website-Patches.

## Dokumentierter Verlauf aus Phase 1

## 1. Verifizierte Anwendung und Arbeitsgrundlage

Repository: `infohansetalent-max/laboraquise-de-site`, Remote `https://github.com/infohansetalent-max/laboraquise-de-site.git`.

Ursprünglicher Arbeitsbaum: `/Users/bencarstens/Desktop/Laboraquise.de/laboraquise-website`. Dort ist `hormozi-fassung-2-2026-08-26` ausgecheckt und es gibt eine geänderte `index.html` sowie unversionierte Scroll-/Asset-Dateien. Diese Dateien wurden nicht verändert, entfernt oder übernommen. Weitere separate Relaunch-Arbeitsbäume existieren und wurden nicht zusammengeführt.

Bearbeiteter Arbeitsbaum: `/Users/bencarstens/Documents/Codex/2026-09-14/files-pasted-by-the-user-auftrag/work/laboraquise`, Zweig `codex/seo-grundlage-2026-09-14`, Ausgangscommit `273be1a780130b0a7f6a9d9f485c582b7ace81ff`.

Verifizierter Produktionshost: **https://www.laboraquise.de/**. Belege: `CNAME:1`, Canonical der ursprünglichen Startseite, robots.txt, Sitemap und lesende GitHub-API `repos/infohansetalent-max/laboraquise-de-site/pages`. Antwort: `cname=www.laboraquise.de`, `source.branch=main`, `source.path=/`, `build_type=legacy`, `https_enforced=true`. Neuester gelisteter GitHub-Pages-Deploy verweist auf denselben Ausgangscommit.

HTTP-Prüfung am 14.09.2026 gegen 13:21 UTC: HTTP-Apex, HTTPS-Apex und HTTP-www antworten jeweils mit 301 auf `https://www.laboraquise.de/`. `/termin` antwortet mit 301 auf `/termin/`. `/index.html` und `/termin/index.html` liefern dagegen 200. Die bisherige bevorzugte Variante ist HTTPS, www und abschließender Slash für Verzeichnisse. Auch `https://infohansetalent-max.github.io/laboraquise-de-site/` führt per 301 zum Produktionshost. Für `labor-aquise.de` und `www.labor-aquise.de` scheiterte die DNS-Auflösung in dieser Prüfung. Daraus wird keine Aussage über Eigentum oder zukünftige Erreichbarkeit abgeleitet.

Stack: statischer Webflow-Export, HTML/CSS und Browser-JavaScript. Keine React-/Next-/SPA-Anwendung, keine Framework-Migration. Öffentliche Seiten liegen als fünf `index.html`-Dateien vor. Auslieferung des fertigen HTML über GitHub Pages, Verzeichnisrouting des Hosts. Die Exportdateien identifizieren Webflow per Site-/Bundle-IDs, aber keine belastbare Produktversion. Vorhandene lokale Bibliotheksbelege: jQuery 3.5.1 im Dateinamen, GSAP 3.15.0 im Versionsverzeichnis. Kein `package.json`, Lockfile, README, Build-, Typecheck-, Lint- oder Testbefehl im Produktionszweig vorhanden. Die zusätzliche Paket-/Teststruktur in einem Relaunchentwurf gehört nicht zu diesem Stand.

Geladene Regeln: Nutzerauftrag, geltende übergeordnete AGENTS.md, die gefundenen Repository-Dateien sowie Skills für Spezifikation, Browserprüfung und Review über fünf Achsen. Keine projektspezifische zusätzliche AGENTS.md auf dem Produktionszweig gefunden. Es gibt keine bestehende geeignete Dokumentationsstruktur, daher `docs/seo/`.

## 2. Angebot und Rolle der Startseite

Beobachtung: Laboraquise spricht Laborinhaber an, die neue Zahnarztpraxen als Kunden gewinnen wollen. Angeboten werden Kundenprofil, Einstiegsangebot, Kampagnen über soziale Medien/Google, automatisierte Vorqualifizierung und Übergabe der Praxisanfragen. Das Labor führt die Gespräche und Abschlüsse selbst. Quelle: vollständig gelesene Startseite und AGB Ziffer 3 und 5.

Die bestehende Startseite ist bereits die zentrale kommerzielle Leistungsseite. Ihre H1 bleibt „Neue Zahnarztpraxen für Ihr Dentallabor gewinnen.“ Die verschiedenen Akquise-Keywords werden einer URL zugeordnet. Es wurden weder neue Leistungen noch Seitenkopien angelegt.

Der vorhandene Anfrageweg: Startseite → Formularfenster → POST an `https://portal.lokalejobsuche.de/api/eigenvertrieb/submit` → vom Server bestätigte Calendly-URL. Der HTML-Ausgangstext nennt noch `/api/funnels/submit`, der vorhandene Skriptblock `eigenvertrieb-absenden` überschreibt ihn zur Laufzeit. Es gibt außerdem `/termin/` mit direkter Calendly-Einbettung und Ersatzlink. Kein zusätzliches Formular oder Buchungssystem eingerichtet.

Der Website-Ausgangsstand nannte eine Garantie für 12 qualifizierte Praxisanfragen in 90 Tagen, keinen garantierten Neukundenabschluss. Diese Aussage war eine Websitebehauptung, kein geprüftes Musterangebot. In Phase 2 wurde sie aus der lokalen Startseite entfernt. Die allgemeinen Recruiting-Regeln anderer Projekte wurden nicht übertragen.

## 3. Vollständiges URL-Inventar des Ausgangsstands

Geprüft wurden sämtliche fünf öffentlichen HTML-Dateien, die gesamte Sitemap, robots.txt, alle im HTML auffindbaren internen href/src-Ziele sowie die HTTP-Varianten oben und eine unbekannte URL. Keine dynamischen Inhaltsrouten vorhanden. Vergleich der fünf heruntergeladenen HTML-Antworten mit dem Git-Ausgangsstand per SHA-256: **5 von 5 bytegleich**. Das ist ein Beleg für diesen Abrufzeitpunkt, kein fortlaufender Abgleich.

Alle folgenden Pfade liegen unter `https://www.laboraquise.de`:

| URL | Zweck / Zielgruppe | HTTP | Title vorher | H1 | Canonical vorher | Robots vorher | Sitemap vorher | Rendering / intern erreichbar | Anfrageziel |
|---|---|---|---|---|---|---|---|---|---|
| `/` | Neukundengewinnung für Laborinhaber | 200 | Laboraquise.de \| Neue Praxen für Dentallabore gewinnen | Neue Zahnarztpraxen für Ihr Dentallabor gewinnen. | auf sich selbst | kein Meta-Robots, kein X-Robots-Tag; erlaubt | ja | Inhalt vollständig im initialen HTML; Navigation und Footer | Formularfenster, Portal-API, bestätigte Calendly-URL |
| `/termin/` | Interessierte Laborinhaber buchen Gespräch | 200 | Termin aussuchen \| Laboraquise.de | Termin aussuchen | fehlt | kein Meta-Robots, kein X-Robots-Tag; erlaubt | ja | redaktioneller Inhalt im HTML; Kalender per JavaScript; vorher Link aus Datenschutz, Haupt-CTA nur Formularbutton | eingebettetes Calendly und direkter Ersatzlink |
| `/impressum/` | Anbieteridentität / Kontakt | 200 | Impressum \| Laboraquise.de | Impressum | fehlt | kein Meta-Robots, kein X-Robots-Tag; erlaubt | ja | statisches HTML; Footerlinks auf index.html-Alias | E-Mail / Telefon |
| `/datenschutz/` | Information zur Datenverarbeitung | 200 | Datenschutzerklärung \| Laboraquise.de | Datenschutzerklärung | fehlt | kein Meta-Robots, kein X-Robots-Tag; erlaubt | ja | statisches HTML; Formular und Footer | Kontakt / Link zur Terminseite |
| `/agb/` | Bedingungen für Unternehmer | 200 | Allgemeine Geschäftsbedingungen \| Laboraquise.de | Allgemeine Geschäftsbedingungen | fehlt | `noindex, follow`, kein X-Robots-Tag; Crawl erlaubt | ja, widersprüchlich | statisches HTML; Footer / Inhaltsanker | Rückweg zur Startseite |
| `/seo-pruefung-nicht-vorhanden-20260914/` | nicht vorhanden | 404 | GitHub-Fehlerantwort | keine Inhaltsseite | nicht zutreffend | Status schließt Erfolg aus | nein | tatsächlicher Live-404 | kein Anfrageweg erforderlich |

Keine Redirectschleife beobachtet. Keine widersprüchlichen X-Robots-Header gefunden. robots.txt erlaubt öffentliche Inhalte sowie CSS/JavaScript. Die allgemeine Rewrite-Regel `_redirects` wird von GitHub Pages nicht angewendet: die unbekannte Live-URL war schon vorher 404.

## 4. Befunde, Änderungen und kleinste Korrekturen

| Prio | Beleg | Auswirkung | Umsetzung / Prüfverfahren |
|---|---|---|---|
| P1 | Vier Unterseiten hatten keinen Canonical und keine Description; Originaldateien / HTTP-Inventar, neu jeweils HTML-Kopf | Doppelte index.html-Adressen ohne eindeutige bevorzugte URL, fehlende redaktionelle Beschreibung | Selbst-Canonicals, eindeutige Beschreibungen und explizite Robots-Direktiven. `CNAME` als geprüfte Hostquelle; Smoke-Test vergleicht sämtliche Metadaten damit. |
| P1 | Original `sitemap.xml` enthält `/agb/`, AGB hat `noindex, follow` | Sitemap empfiehlt eine ausgeschlossene Seite | Nur AGB aus Sitemap entfernt. noindex bleibt crawlbar, kein robots.txt-Verbot. Vier gültige Sitemap-URLs getestet. |
| P1 | Original Sitemap-lastmod stammt vom 16./25.08., obwohl HTML am 27.08. geändert wurde | Unzuverlässiges Änderungssignal | lastmod weggelassen. Kein Builddatum eingesetzt. |
| P1 | Ursprüngliche Links zu `*/index.html`, `index.html`-Skript „Append query parameters to all links“ | Verlinkung von Dubletten; beliebige Parameter gelangen an Rechts-/Kontaktlinks | Root-relative Slash-Links, allgemeinen Parameterkopierer entfernt. UTM-Auslesen am Formular und erlaubte funktionale Calendly-Parameter bleiben erhalten. Interne Link-/Anchor-Prüfung und Browserfall mit UTM plus zusätzlichem Parameter. Keine pauschalen URL-Redirects. |
| P1 | Haupt-CTAs waren Buttons mit `aria-label="text"`; Formulartexte waren div statt label | Keine crawlbare Terminverbindung aus dem Haupt-CTA; unverständliche Screenreader-Namen | Sieben CTA-Abdeckungen als echte `/termin/`-Links, beschreibende Namen, bestehendes Modal bei normalem Klick erhalten. Vier verbundene Labels. Tastatur, Escape, Formular und JavaScript-Ausfall geprüft. |
| P1 | `index.html`, Formularhandler: nur leere E-Mail geprüft, Response-Status ignoriert | Ungültige Eingaben bzw. fehlerhafte HTTP-Antwort könnten zur Weiterleitung führen | Native E-Mail-Gültigkeit prüfen; HTTP-Fehler nicht als Erfolg behandeln. Mockprüfungen für ungültige E-Mail, fehlende Einwilligung, HTTP 500 mit irreführendem ok, ungültiges JSON, unzulässige Kalenderdomain und Netzwerkfehler. |
| P1 | Live-Calendly zeigt „30 min“ und „30 Minuten. Online. Kostenlos.“, Website vorher viermal 15 Minuten | Falsche Erwartung vor Buchung | Drei Angaben auf Startseite einschließlich Modal und eine auf `/termin/` auf 30 Minuten korrigiert. Kein externer Termin geändert. Quelle: lesender Browserabruf vom 14.09.2026. |
| P1 | Keine konfigurierte externe Preview-Umgebung im geprüften Repository; keine Preview-Regeln | Eine spätere Kopie des Roots auf einem Testhost wäre indexierbar | Lokaler Server bindet ausschließlich an 127.0.0.1 und liefert standardmäßig `X-Robots-Tag: noindex, nofollow`. Explizite lokale Produktionssimulation prüft HTML ohne diesen Header. Das verändert keine Produktionsheader. Externe Preview-Veröffentlichung bleibt bis zur Prüfung ihrer echten Hostregeln gesperrt. |
| P2 | Startseite JSON-LD `Organization.url` war `/`; zusätzlich leerer preconnect | Relative Organisationsadresse, nutzloser Verbindungs-Hinweis | Absolute verifizierte Organisations-URL; sachliche Beschreibung ohne verstärkte Garantie; leerer preconnect entfernt. Ein JSON-LD-Block, parsbar und zum sichtbaren Anbieter passend. Kein Dentist, keine Bewertungen, kein unnötiges Article/Breadcrumb-Schema. |
| P2 | `_redirects:1` enthielt `/* /index.html 200` | Bei späterem Hostingwechsel möglicher Soft-404 | Nicht benötigten SPA-Fallback durch Kommentar ersetzt. GitHub-Pages-404 erhalten, keine neue Weiterleitung. |
| P2 offen | Statischer Popup-Text „Diese Woche kaum noch Plätze verfügbar“, generierte Wochentage, kein Verfügbarkeitsabruf in diesem Popup | Unbelegte Dringlichkeit kann Vertrauen kosten | In Phase 2 mit tatsächlichem Angebot abgleichen bzw. sachlich ersetzen. Nicht als realer Kalenderbefund ausgeben. |
| P2 offen | Referenzabschnitt erklärt Personalgewinnung, enthält u. a. eine Hausarztpraxis | Kein Ergebnisbeleg für Praxisakquise; Überschrift „Fünf Labore“ passt nicht vollständig zur Liste | Keine Akquise-Fallstudie erfunden. Redaktionelle Prüfung und freigegebene Belege in Phase 2. |
| P2 offen | Datenschutzerklärung nennt Cloudflare/Supabase/Resend; tatsächlicher Browserendpoint ist portal.lokalejobsuche.de | Backend-Anbieter und Datenschutztext könnten auseinanderliegen | Kein Beweis für einen Verstoß oder veraltete Verträge. Technischen Portalbetreiber und Datenweg separat verifizieren, dann fachlich abgleichen. Keine ungefragte Rechtstextänderung. |

Es wurde kein gemessener P0-Ausfall festgestellt. Die echte Speicherung und Zustellung einer Anfrage wurde bewusst nicht getestet. Der vorhandene Live-Frontendweg und der lokal gemockte Erfolgsfall sind unterschiedliche Belege.

## 5. Umgebungen und Veröffentlichungsgrenze

**Produktion:** GitHub Pages aus `main:/`. `.nojekyll` ist vorhanden. HTML liegt fertig vor, es gibt keinen Anwendungsbuild. `_headers` ist keine belegte wirksame GitHub-Pages-Headerkonfiguration. Die Änderungen greifen dort erst nach einer gesondert autorisierten Veröffentlichung.

**Lokal:** `scripts/serve.py` liefert ausschließlich bekannte öffentliche Seiten und Ressourcen, keine Verzeichnislisten. Default ist noindex. `--production-simulation` bedeutet ausschließlich lokale Prüfung ohne Preview-Header. Es ist keine vollständige Simulation der GitHub-Infrastruktur. Ein codierter Asset-Pfad kann nach Review keine internen Dokumente mehr erreichen; Regressionstest enthalten.

**Wichtige Grenze:** Die lokale Auslieferungssperre für `docs/`, `tests/` und `scripts/` gilt nicht für GitHub Pages. Bei einem späteren unveränderten Root-Publish sind diese nicht vertraulichen Quelldateien öffentlich abrufbar. Deshalb enthalten sie keine Geheimnisse, Kundendaten oder Artikelentwürfe. Entwürfe und Testartefakte liegen außerhalb des Repository-Roots. Vor einer Änderung dieses Veröffentlichungsmodells wäre eine explizite Auswahl des Deploy-Artefakts erforderlich; diese Phase verändert keine Hostingkonfiguration.

**Externe Previews:** Keine automatische PR-Preview im geprüften Produktionsrepository eingerichtet; die gelisteten Deployments verwenden `github-pages/main`. Das beweist nicht die Abwesenheit jeder extern angelegten Kopie. Eine nicht vorgelegte Preview-URL wurde nicht geprüft. Vor einem späteren öffentlichen Preview-Deploy muss der echte Host noindex ausliefern oder Zugriffsschutz verwenden. `NODE_ENV` wird hier nicht benutzt. noindex ist keine Zugriffssperre.

## 6. Durchgeführte Prüfungen

Umgebung: macOS, Python 3.9.6, Node 26.7.0, vorhandenes Playwright Core 1.63.0 und installiertes Chrome, headless. Der Browser-Skill des Browser-Plugins ist in dieser Sitzung nicht verfügbar; reguläres Playwright gemäß frontend-testing-debugging verwendet. Es wurden keine Browserabhängigkeiten installiert. Das Modul wurde aus dem vorhandenen separaten Arbeitsbaum geladen, ohne dessen Dateien zu ändern.

| Prüfung | Status | Beleg / Grenze |
|---|---|---|
| Produktionshost / GitHub-Pages-Zweig | PASS | API-Ausgabe, 301-Antworten und 5/5 HTML-Hashes |
| Ausgangsstand erreichbar | PASS | fünf reale 200-Antworten; echte unbekannte URL 404 |
| SEO-Smoke-Test | PASS | `python3 -m unittest discover -s tests -v`: sechs Testgruppen, einschließlich aller Seiten, Canonicals, Sitemap, Ressourcen, Anker, Schema und beider lokalen Modi |
| Vorher-/Nachher-Test | PASS | Neue Tests schlagen gegen den Ausgangsstand bei den erwarteten SEO-Lücken fehl; nach Korrektur grün. Testdatei `seo-before.log` dokumentiert das ursprüngliche Rot. |
| JavaScript-Syntax | PASS | 25 vorhandene Inline-Skriptblöcke mit `node --check` geprüft; Testskript separat geprüft |
| Desktop und Mobile | PASS | 1440×900 und 390×900, alle fünf Seiten; vollständiger Scroll-Durchlauf, jeweils 0 Pixel horizontaler Überlauf, keine defekten geladenen Bilder, keine ungefangenen Skriptfehler oder Fehleroverlays |
| Console bei Seitenaufruf | PASS | Keine console.error-Meldungen in den geprüften lokalen Seitendurchläufen. Zwei GSAP-Warnungen über fehlende Animationsziele je Startseitenaufruf sind im bytegleichen Ausgangs-HTML identisch reproduziert und keine neue Regression. Absichtlich simulierte Netzwerk-/HTTP-Fehler im Formular sind getrennte Testfälle. |
| Formularpfad | PASS, gemockt | CTA → sichtbares Formular → Tastatur/Escape → Validierung → vier Fehlerantworten → bestätigte Antwort → Kalender-Testseite; auf beiden Breiten. Eingaben bleiben bei Fehlern erhalten, Idempotenzschlüssel bleibt stabil. |
| Ohne JavaScript | PASS | Startseiten-H1 vorhanden, primärer Link führt zu `/termin/`, direkter Calendly-Ersatzlink vorhanden |
| Live-Browser, Ausgangsstand | PASS, lesend | Startseite und `/termin/` bei 390×844, kein Überlauf/ungefangener Skriptfehler. Kalenderframe lädt, direkte Calendly-Seite zeigt Auswahl und 30 Minuten. Keine Buchung ausgewählt oder abgeschickt. Fremde schreibende HTTP-Methoden blockiert. |
| Compiler-Build / Typecheck / Lint | NICHT VORHANDEN | Statischer Export ohne entsprechende Projektbefehle. Kein Build-Erfolg erfunden. Git-Diff und JavaScript-Syntax geprüft. |
| Echter API-Erfolg, CRM-Lead, Mailzustellung, Terminbuchung | NICHT GEPRÜFT | Kein freigegebenes Testbackend. Alle Formularübermittlungen lokal abgefangen; keine echten Vorgänge erzeugt. |
| Neue Änderungen live | NICHT GEPRÜFT | Nicht deployt |
| Search Console / Google-Indexierung | NICHT GEPRÜFT | Keine autorisierten Search-Console-Daten für diese Untersuchung vorliegend |
| Reale Core Web Vitals, Safari, physisches Smartphone | NICHT GEPRÜFT | Lokale Chrome-Labortests sind kein Feld- oder iPhone-Nachweis |

Performance: Ausgangs-HTML der Startseite 255.997 Bytes; Assetverzeichnis 16.681.667 Bytes, davon größte Datei ein MP4 mit 5.829.607 Bytes. Verzeichnisgröße ist ausdrücklich keine gemessene Seitenübertragung. Sichtprüfung und lokale ungedrosselte DOMContentLoaded-Zeiten sind in Browserartefakten enthalten. Keine belastbare reale LCP-/INP-/CLS-Verschlechterung oder ein eindeutig zuzuordnender Engpass gemessen. Deshalb keine Bildneuproduktion, Komprimierungsserie oder Script-Entfernung auf Verdacht.

Die initialen Browser-Testfehler waren ein unpassender Selektor für einen mobilen unsichtbaren Navigationsbutton und fehlendes UTF-8 in einer Testantwort. Beides im Prüfskript korrigiert. Ein früher Test las HTTP-Antwortkörper nicht vollständig und erzeugte BrokenPipe-Logs im lokalen Server; Testclient korrigiert. Keine Fehler durch Deaktivieren von Prüfungen kaschiert.

## 7. Review und geänderte Dateien

Unabhängige Prüfung über Korrektheit, Verständlichkeit, Architektur, Sicherheit und Performance durchgeführt. Zwei konkrete Review-Befunde: Produktionsgrenze der lokalen Sperre dokumentieren und Assetpfad nach Auflösung begrenzen. Beide korrigiert und durch den Reviewer nachgeprüft. Keine übrigen offenen konkreten Reviewbefunde gemeldet. Kein Merge erfolgt.

Geändert:
- `index.html`: Metadaten, JSON-LD, interne Links, CTA-Semantik, Labels, Formularvalidierung/HTTP-Status, Dauertexte.
- `termin/index.html`: Metadaten, interne Links, 30-Minuten-Angabe.
- `impressum/index.html`, `datenschutz/index.html`, `agb/index.html`: Metadaten und interne Links. Bestehende Rechtstexte erhalten; sichtbarer Text aller drei Rechtsseiten gegen den Ausgangsstand automatisch abgeglichen.
- `sitemap.xml`: AGB und unbelegte lastmod-Angaben entfernt.
- `_redirects`: unpassenden SPA-Fallback entfernt; GitHub-Pages-Verhalten unverändert.

Neu:
- `scripts/serve.py`: lokale Vorschau mit noindex und expliziter lokaler Produktionssimulation.
- `tests/test_seo.py`: reproduzierbare SEO-/HTTP-Prüfung ohne Abhängigkeiten.
- `tests/browser-smoke.mjs`: lokale Browserprüfung mit vollständig abgefangenen externen Formularantworten.
- `.gitignore`: Python-Zwischendateien ausschließen.
- `docs/seo/AUDIT.md`, `docs/seo/PLAN.md`: kanonische Dokumentation dieser Phase.

Betroffene Inhalts-URLs: `/`, `/termin/`, `/impressum/`, `/datenschutz/`, `/agb/`. Keine neue öffentliche Inhalts-URL und keine URL gelöscht. Sitemap jetzt mit vier statt fünf Einträgen. Titel-/Keywordzuständigkeit siehe PLAN.

Testartefakte: im benachbarten `work/evidence/`, ausdrücklich außerhalb des Website-Roots. Darin Rohantworten/Hashes, Redirectinventar, Browserprotokolle, Screenshots und Syntaxprüfung. Bereitgestellte Ausgaben sind datierte Exporte, keine zweite zu pflegende Dokumentationsstruktur.

## 8. Offene Entscheidungen und Auftrag für Phase 2

Kein Blocker für die hier lokal umgesetzten Korrekturen. Offen vor tatsächlicher Veröffentlichung: separate Deploy-Freigabe, finale Prüfung des zu veröffentlichenden Diff und anschließende Live-HTTP-/Browserprüfung. Für einen echten Anfrage-Erfolg ist ein freigegebenes Testbackend oder ein autorisierter kontrollierter Testvorgang erforderlich. Für Indexstatus und Nachfrage sind autorisierte Search-Console-Daten erforderlich. Keine Zwischenfreigabe für erledigbare lokale Arbeiten abgewartet.

Phase 2 beginnt mit fachlicher Absicherung der Startseite, danach mit genau einem belegten Artikel über Wechselgründe von Zahnarztpraxen. Vollständige Matrix, drei ausgearbeitete Briefings und Messplan stehen in PLAN.md. Keine zusätzliche kommerzielle Akquise-Seite.

## 9. Technische Primärquellen

- [Google: Canonicals und bevorzugte URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls): einheitliche Canonical- und interne Linkziele.
- [Google: noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing): noindex muss crawlbar sein; robots.txt ist kein Ersatz.
- [Google: Sitemap erstellen](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap): kanonische URLs und nachvollziehbare Änderungsdaten.
- [Google: JavaScript-SEO](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics): HTML und gerenderten Inhalt getrennt beurteilen.
- [Google: Richtlinien für strukturierte Daten](https://developers.google.com/search/docs/appearance/structured-data/sd-policies): Bezug zu sichtbaren, belegbaren Inhalten.
- [GitHub Pages: Fehlerseiten](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-custom-404-page-for-your-github-pages-site): statisches Hosting und 404-Verhalten.

## Einsatzfertige Übergabe nach Phase 2

> Gleiche die Startseite vor erneuter Bewerbung einer numerischen Garantie mit dem freigegebenen Praxisakquise-Angebot ab. Lasse den vorhandenen privaten Artikel vollständig fachlich prüfen und dokumentiere die Nutzungsfreigabe einer echten Praxisstimme. Halte die Startseite als einzige kommerzielle Akquise-Seite. Setze den Artikel erst nach Inhaltsfreigabe ins vorhandene Seitendesign um und erweitere dann Wissensübersicht und Sitemap. Übernimm den lokal geprüften Zweig erst nach ausdrücklicher Veröffentlichungsfreigabe. Prüfe anschließend die fünf bestehenden URLs, etwaige freigegebene neue URLs, die Sitemap und eine unbekannte URL am echten Produktionshost. Erzeuge keine reale Anfrage oder Buchung ohne autorisierten Testweg.

Ungeklärt bleiben Indexierung, organische Nachfrage, serverseitige Anfragespeicherung und die noch fehlenden Veröffentlichungsbelege. **IM CODE UMGESETZT ≠ LOKAL GETESTET ≠ DEPLOYT ≠ LIVE VERIFIZIERT ≠ BEI GOOGLE INDEXIERT.**
