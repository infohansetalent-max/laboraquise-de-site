# Organische Anfragen: Befund, Umsetzung, Grenzen

Stand 15.09.2026. Baut auf `AUDIT.md` und `PLAN.md` vom 14.09.2026 auf.
Auftrag: möglichst viele organische Anfragen von Dentallaboren, die neue
Zahnarztpraxen als Kunden brauchen.

## 1. Der Befund, der alles bestimmt

Geprüft wurde die tatsächliche Suchnachfrage über die Google-Vorschlagsliste
(`suggestqueries.google.com`, hl=de, gl=de) am 15.09.2026. Die Vorschlagsliste
belegt, **dass** ein Begriff häufig genug gesucht wird, um überhaupt
vorgeschlagen zu werden. Sie liefert **kein** Suchvolumen. Für Volumenzahlen
fehlt in dieser Sitzung ein Zugang zu einem Keyword-Werkzeug.

**Ohne jeden Vorschlag, also praktisch ohne Nachfrage:**

    dentallabor marketing · dentallabor neukunden · zahntechnik marketing
    dentallabor zahnarzt akquise · dentallabor digitalisierung
    wie finde ich ein dentallabor · zahntechnisches labor gründen

Die Startseite ist auf genau dieses Wortfeld getextet. Sie ist die richtige
Seite für Besucher, die schon da sind, aber sie kann über die Suche kaum
Besucher holen. Daran ändert keine Textänderung etwas.

**Mit Vorschlägen, also mit belegbarer Nachfrage von Laborinhabern:**

| Suchfeld | Belegte Vorschläge | Bedient durch |
|---|---|---|
| Akquise | kundenakquise dentallabor, akquise dentallabor, dental akquise | `/wissen/kundenakquise-im-dentallabor/` |
| Kauf und Nachfolge | dentallabor kaufen (+ NRW, Bayern, Niedersachsen, Hessen, Berlin, Stuttgart, Hamburg, München, Schweiz), dentallabor verkaufen preis, dentallabor nachfolger, dentallabor übernahme, zahntechnik laborauflösung | `/wissen/dentallabor-kaufen-oder-uebernehmen/` |
| Gründung | dentallabor gründen kosten, dentallabor voraussetzungen, dentallabor eröffnen, dentallabor gewerbe, zahntechniker selbstständig ohne meisterbrief | `/wissen/dentallabor-gruenden/` |
| Preise und Abrechnung | dentallabor preisliste, dentallabor kosten, bel ii preisliste, bel 2 abrechnung, beb abrechnung zahntechnik, stundensatz zahntechnikermeister, zahntechnik stundenlohn | `/wissen/preise-und-stundensatz-im-dentallabor/` |
| Eigenlabor | eigenlabor zahnarzt (abrechnung, umsatzsteuer, preise, fremdlabor), praxislabor zahntechniker | `/wissen/eigenlabor-und-praxislabor/` |
| Marktzahlen | anzahl dentallabore in deutschland, umsatz dentallabore deutschland | `/wissen/zahntechnik-in-zahlen/` |

Der Schluss daraus: Organische Anfragen entstehen hier nicht über das eigene
Angebotswort, sondern über die Geld-, Rechts- und Betriebsfragen, die
Laborinhaber ohnehin googeln. Von dort führt jede Seite zum Erstgespräch.

## 2. Was gebaut wurde

Sechs neue Seiten unter `/wissen/`, dazu die neu aufgebaute Übersicht. Alle
nutzen die abgenommene Gestaltung der bestehenden Artikelseite, übernommen als
Schablone unter `werkzeuge/schablone/` (Endung `.part`, damit der Host sie
nicht als eigene Seite ausliefert).

Jede Seite hat: Sprungmarken, mindestens eine eigene SVG-Figur, Tabellen oder
Schrittfolgen, eine abhakbare Prüfliste, Häufige Fragen mit FAQPage-Auszeichnung
und einen Weg zum Erstgespräch. Vier Seiten haben zusätzlich einen Textbaustein
zum Kopieren, zwei haben einen Rechner.

Auf der Startseite neu: FAQPage-Auszeichnung der acht vorhandenen Fragen,
wortgleich aus dem sichtbaren Text erzeugt, und ein Abschnitt, der sechs
Wissensseiten verlinkt. **Am Text der Startseite wurde nichts geändert.**

## 3. Belegte Zahlen und ihre Quellen

| Zahl | Wert | Quelle |
|---|---|---|
| Zahntechnische Betriebe, H1 2025 | 6.845 | ZDH-Statistik, ausgewertet von Rebmann Research |
| Gewerbliche Dentallabore 2024 | 6.994 | ebenda |
| Rückgang 2023 auf 2024 | 3,4 Prozent | ebenda |
| Neugründungen H1 2025 | 105 | ebenda |
| Betriebsaufgaben H1 2025 | 254 | ebenda |
| Betriebe 2023 | rund 7.238 | **abgeleitet** aus 6.994 und 3,4 Prozent, als abgeleitet gekennzeichnet |
| Zahntechnikerhandwerk zulassungspflichtig | Anlage A Nr. 37 HwO | gesetze-im-internet.de |
| § 7b HwO gilt nicht für Gesundheitshandwerke | — | Auskunft mehrerer Handwerkskammern, im Text als Einordnung gekennzeichnet |
| Zahntechnische Leistungen | 7 Prozent USt | § 12 Abs. 2 Nr. 6 UStG |

Nicht genannt, weil keine geprüfte Primärquelle vorliegt: Anzahl der
Praxislabore, Branchenumsatz, Beschäftigtenzahl, Wechselquoten von Praxen.
Die Seite `/wissen/zahntechnik-in-zahlen/` benennt diese Lücken ausdrücklich.

## 4. Technische Änderungen

- Das je Seite eingebettete CSS (37,5 KB) liegt jetzt in
  `assets/css/wissen-basis.css`. Die bestehende Artikelseite schrumpfte dadurch
  von 96 KB auf 58 KB, alle weiteren Seiten laden dieselbe Datei aus dem Cache.
- Das Navigations-CSS für den Fall ohne JavaScript steht in
  `assets/css/wissen-ohne-js.css` und wird wie im Original nur über `<noscript>`
  geladen. **Achtung:** Diese Regeln dürfen nicht allgemein gelten, sonst
  verschwindet das Menü-Symbol auf schmalen Bildschirmen. Genau dieser Fehler
  ist beim Auslagern entstanden und wurde durch die Browsermessung gefunden.
- `assets/css/wissen-plus.css` und `assets/js/wissen-plus.js` sind neu:
  Kennzahlenband, Figurenrahmen, Rechner, Kopierknopf, gemerkte Prüflisten.
- Sitemap: 12 URLs statt 6. `scripts/serve.py` kennt alle Seiten.

## 5. Geprüft

| Prüfung | Ergebnis |
|---|---|
| SEO-Tests `python3 -m unittest discover -s tests` | 7 Gruppen grün, jetzt über 8 Wissensseiten statt 2 |
| Rechner gegen unabhängig berechnete Sollwerte | Bedarf 2/4 und 3/6 korrekt. Stundensatz 4.128 h und 96,90 €, nach Änderung 5.160 h und 102,71 €, beide korrekt |
| Waagerechter Überlauf bei 375 px | 0 Pixel auf allen acht Seiten |
| Bei 1440 px | 0 Pixel, Sprungleiste klebt, Karten je Zeile gleich hoch |
| Schrift | General Sans geladen, kein Rückfall auf Arial |
| Beschriftung in Figuren | keine unter 8 px |
| Sprungmarken | jedes Ziel vorhanden, auf allen Seiten |
| Bilder | keine defekten |
| JSON-LD | alle Blöcke parsen, Pflichtfelder erfüllt, Krümelpfade fortlaufend nummeriert |
| Gedankenstriche im sichtbaren Text | 0 auf allen neuen Seiten |

## 6. Was offen bleibt

- **Kein Suchvolumen gemessen.** Die Vorschlagsliste belegt Nachfrage, nicht
  ihre Größe. Wer Zahlen will, braucht Search Console oder ein Keyword-Werkzeug.
- **Keine Search Console eingerichtet.** Ohne sie lässt sich nach dem Livegang
  nicht messen, welche Seite tatsächlich Besucher bringt. Das ist der nächste
  sinnvolle Schritt.
- **Rankings brauchen Zeit.** Neue Seiten stehen nicht nach Tagen vorn.
  Belastbar beurteilen lässt sich das frühestens nach acht bis zwölf Wochen.
- **Der größte ungenutzte Hebel.** Die nachfragestärksten Suchen der Nische sind
  Ortssuchen wie `dentallabor hamburg`, `zahntechnik labor berlin`,
  `dentallabor in der nähe`. Diese Suchen kommen von **Praxen und Patienten**,
  nicht von Laboren. Wer dort sichtbar ist, erzeugt genau die Praxisanfragen,
  die Laboraquise.de verkauft. Das wäre ein eigenes Vorhaben mit Ortsseiten und
  einem Laborverzeichnis, nicht eine weitere Ratgeberseite.
