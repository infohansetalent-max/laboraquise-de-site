# Google Search Console

Eingerichtet am 15.09.2026.

## Zugang

| | |
|---|---|
| Konto | info.hansetalent@gmail.com |
| Property | URL-Präfix `https://www.laboraquise.de/` |
| Bestätigt per | Meta-Tag auf der Startseite |
| Direktlink | https://search.google.com/search-console?resource_id=https%3A%2F%2Fwww.laboraquise.de%2F |

## Der Nachweis darf nicht verschwinden

Auf der Startseite steht im Kopf:

    <meta name="google-site-verification" content="kFe-99axlwPy2d9ltDw9lAeiQEMwrpuGfuP1C0hd2HA">

Wird er entfernt, verliert die Property den Nachweis und alle Daten sind
gesperrt, bis neu bestätigt wird. Der Tag steht deshalb auch in
`werkzeuge/startseite_ergaenzen.py`, damit ein erneuter Lauf ihn wieder setzt.

**Warum Meta-Tag statt der von Google empfohlenen HTML-Datei:** Der Test in
`tests/test_seo.py` verbietet zusätzliche HTML-Dateien im Wurzelverzeichnis,
damit nichts versehentlich als eigene Seite indexiert wird. Eine
`google4715d20de194e500.html` hätte ihn gebrochen.

**Warum nicht per DNS:** Die Zone liegt bei IONOS und trägt die MX-Einträge des
Postfachs. Für eine Bestätigung wird dort nichts angefasst.

## Was am 15.09.2026 gemacht wurde

1. Property angelegt und bestätigt.
2. `sitemap.xml` eingereicht. Status erfolgreich, 12 erkannte Seiten.
3. Indexierung für alle neun öffentlichen Seiten einzeln beantragt:
   Startseite, `/wissen/` und die sieben Artikelseiten.

## Ausgangsbefund

Vor der Einrichtung war **keine einzige Seite der Domain bei Google indexiert**,
auch die Startseite nicht. Die URL-Prüfung meldete durchgängig
„URL ist nicht auf Google". Das erklärt, warum es bisher keine organischen
Anfragen gab: Die Seite stand nicht in den Ergebnissen, nicht auf Seite zwei,
sondern gar nicht.

## Was als Nächstes zu beobachten ist

| Wann | Was |
|---|---|
| Nach 3 bis 7 Tagen | Unter *Indexierung → Seiten* prüfen, wie viele der zwölf URLs indexiert sind. |
| Nach 4 Wochen | Unter *Leistung* stehen die ersten echten Suchanfragen. Sie ersetzen die Annahmen aus `ORGANISCH-2026-09-15.md`. |
| Nach 8 bis 12 Wochen | Belastbar beurteilen, welche Seite trägt und wo ausgebaut wird. |

Wichtig: Eine beantragte Indexierung ist keine Zusage. Google entscheidet
weiterhin selbst, ob und wann eine Seite aufgenommen wird.
