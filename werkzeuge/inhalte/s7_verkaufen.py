# -*- coding: utf-8 -*-
"""Dentallabor verkaufen und bewerten.

Warum diese Seite: In der Search Console stehen am 18.09.2026 zwoelf
Suchanfragen. Fuenf davon fragen nach dem Verkauf und nach dem Wert:
'dentallabor verkauf', 'was ist ein dentallabor wert',
'kaufpreisfindung dentallabor', 'kaufvertrag pruefen dentallabor',
'dentallabor verkaufen preis'. Bisher landen sie auf der Kaufseite, die
aus Sicht des Kaeufers geschrieben ist. Wer verkauft, sucht etwas
anderes: den Wert, die Steuer und den Zeitplan.
"""
from wissen_bauen import (kennzahlen, figur, merksatz, mitnehmen, weiterlesen,
                          schritte, checkliste, tabelle, abschluss)

# Der Zusammenhang, um den es auf dieser Seite geht: derselbe Gewinn ist
# unterschiedlich viel wert, je nachdem, auf wie vielen Praxen er steht.
FIG_ABHAENGIGKEIT = '''<svg viewBox="0 0 640 260" role="img" aria-labelledby="t-abh">
<title id="t-abh">Zwei Labore mit gleichem Gewinn: das eine steht auf drei Praxen, das andere auf fünfzehn. Beim Verkauf wird das zweite höher bewertet, weil der Käufer weniger Risiko übernimmt.</title>
<g font-size="13.5">
<text x="24" y="30" fill="#061421" font-size="15">Labor A: drei Praxen tragen den Umsatz</text>
<g fill="#0068C9">
<rect x="24" y="44" width="150" height="30" rx="8"/>
<rect x="182" y="44" width="110" height="30" rx="8"/>
<rect x="300" y="44" width="78" height="30" rx="8"/>
</g>
<g fill="#C2CAD4">
<rect x="386" y="44" width="30" height="30" rx="8"/><rect x="424" y="44" width="24" height="30" rx="8"/>
</g>
<text x="24" y="98" fill="#4A5568" font-size="12.5">Größte Praxis: 41 Prozent des Umsatzes. Springt sie ab, fehlt fast die Hälfte.</text>

<text x="24" y="150" fill="#061421" font-size="15">Labor B: fünfzehn Praxen tragen denselben Umsatz</text>
<g fill="#0068C9">
<rect x="24" y="164" width="46" height="30" rx="8"/><rect x="78" y="164" width="42" height="30" rx="8"/>
<rect x="128" y="164" width="38" height="30" rx="8"/><rect x="174" y="164" width="36" height="30" rx="8"/>
<rect x="218" y="164" width="34" height="30" rx="8"/><rect x="260" y="164" width="32" height="30" rx="8"/>
<rect x="300" y="164" width="30" height="30" rx="8"/><rect x="338" y="164" width="28" height="30" rx="8"/>
<rect x="374" y="164" width="26" height="30" rx="8"/><rect x="408" y="164" width="24" height="30" rx="8"/>
<rect x="440" y="164" width="22" height="30" rx="8"/><rect x="470" y="164" width="20" height="30" rx="8"/>
<rect x="498" y="164" width="18" height="30" rx="8"/><rect x="524" y="164" width="16" height="30" rx="8"/>
<rect x="548" y="164" width="14" height="30" rx="8"/>
</g>
<text x="24" y="218" fill="#4A5568" font-size="12.5">Größte Praxis: 12 Prozent. Ihr Wegfall tut weh, trifft den Betrieb aber nicht.</text>
<text x="24" y="246" fill="#4A5568" font-size="12.5">Die Anteile sind ein Rechenbeispiel, kein erhobener Branchenwert.</text>
</g></svg>'''

VORLAGE_ANFRAGE = """Guten Tag Frau Dr. ...,

ich plane, mein Labor zum ... in andere Hände zu geben, und möchte,
dass Sie es von mir erfahren und nicht über Dritte.

Was ich vorhabe: Die Übergabe soll für Sie nichts verändern. Die
Personen, die Ihre Arbeiten fertigen, bleiben. Preise und Lieferzeiten
bleiben bis mindestens ... unverändert.

Was ich Sie bitte: Sagen Sie mir offen, was Ihnen bei einem Wechsel
der Inhaberschaft wichtig wäre. Ich nehme das in die Gespräche mit.

Ich rufe Sie in den nächsten Tagen an. Wenn Ihnen ein fester Termin
lieber ist, nennen Sie mir zwei Zeitfenster.

Freundliche Grüße
..."""

RECHNER = '''
<div class="rechner" data-rechner="laborwert">
  <h3>Was Ihr Labor überschlägig wert ist</h3>
  <p class="rechner__hinweis">Alle Werte setzen Sie selbst ein. Das Ergebnis ist eine Überschlagsrechnung nach der Logik des Ertragswertverfahrens, kein Gutachten, kein Angebot und keine Preisempfehlung. Eine belastbare Bewertung erstellt ein Wertermittler, im Handwerk meist nach dem AWH-Standard.</p>
  <div class="rechner__feld">
    <label for="w-gewinn">Gewinn vor Steuern im Jahr, bereinigt</label>
    <input type="number" id="w-gewinn" value="180000" min="0" step="5000" inputmode="numeric">
    <small>Bereinigt heißt: einmalige Sondereffekte heraus, private Posten heraus, ungewöhnlich hohe oder niedrige Mieten auf marktüblich gerechnet.</small>
  </div>
  <div class="rechner__feld">
    <label for="w-lohn">Kalkulatorischer Unternehmerlohn im Jahr</label>
    <input type="number" id="w-lohn" value="85000" min="0" step="5000" inputmode="numeric">
    <small>Was eine angestellte Leitung kosten würde, die Ihre Arbeit macht. Dieser Betrag gehört abgezogen, denn der Käufer muss ihn bezahlen.</small>
  </div>
  <div class="rechner__feld">
    <label for="w-anteil">Anteil der größten Praxis am Umsatz: <b><span id="w-anteil-wert">35</span> Prozent</b></label>
    <input type="range" id="w-anteil" value="35" min="5" max="70" step="5">
    <small>Je mehr Umsatz an einer einzigen Praxis hängt, desto höher das Risiko für den Käufer und desto niedriger der Preis, den er zahlt.</small>
  </div>
  <div class="rechner__feld">
    <label for="w-bindung">Wie stark hängen die Praxen an Ihnen persönlich?</label>
    <select id="w-bindung">
      <option value="0">Kaum. Feste Ansprechpartner im Team, Abläufe dokumentiert</option>
      <option value="2" selected>Teilweise. Wichtige Gespräche laufen über mich</option>
      <option value="4">Stark. Ohne mich kennt die Praxis niemanden im Haus</option>
    </select>
  </div>
  <div class="rechner__ausgabe">
    <div class="rechner__zelle"><span>Nachhaltiger Ertrag im Jahr, nach Unternehmerlohn</span><output id="w-ertrag">95.000 €</output></div>
    <div class="rechner__zelle"><span>Kapitalisierungszinssatz aus Basiszins und Risikozuschlag</span><output id="w-zins">15,0 %</output></div>
    <div class="rechner__zelle"><span>Überschlägiger Ertragswert, ohne Geräte und Warenbestand</span><output id="w-wert">633.333 €</output></div>
    <div class="rechner__zelle"><span>Unterschied zu demselben Labor mit breit verteiltem Kundenstamm</span><output id="w-luecke">316.667 €</output></div>
  </div>
  <p class="rechner__hinweis" style="margin:1.2rem 0 0">Zur Rechnung: Basiszins 8 Prozent, zuzüglich einem Punkt Risikozuschlag je 5 Prozentpunkte, die der größte Kunde über einem Zehntel des Umsatzes liegt, zuzüglich des Zuschlags für die Bindung an Ihre Person. Der Vergleichswert in der letzten Zelle rechnet dasselbe Labor mit einem Umsatzanteil des größten Kunden von 10 Prozent.</p>
</div>
'''

SEITE = {
 "slug": "dentallabor-verkaufen",
 "titel": "Dentallabor verkaufen: Wert ermitteln, Steuern, Ablauf | Laboraquise.de",
 "beschreibung": "Was ein Dentallabor wert ist, wie der Ertragswert nach AWH-Standard entsteht, welche Steuerregeln ab 55 gelten und in welcher Reihenfolge ein Verkauf abläuft. Mit Wertrechner und Prüfliste.",
 "krume": "Dentallabor verkaufen",
 "pille": "Wissen für Dentallabore",
 "h1": 'Ein Dentallabor <span class="text-color-primary">verkaufen</span>',
 "h1_klartext": "Dentallabor verkaufen: Wert ermitteln, Steuern, Ablauf",
 "lead": "Der Preis entsteht nicht aus dem, was Sie aufgebaut haben, sondern aus dem, was ohne Sie weiterläuft. Was den Wert bestimmt, welche Steuerregeln ab 55 greifen und in welcher Reihenfolge ein Verkauf abläuft.",
 "about": "Verkauf eines Dentallabors",
 "toc": [("wert","Woraus der Preis entsteht"),("rechner","Wertrechner"),
         ("abhaengigkeit","Was den Preis drückt"),("steuer","Steuern beim Verkauf"),
         ("ablauf","Der Ablauf in sieben Schritten"),("unterlagen","Prüfliste vor dem ersten Gespräch"),
         ("ansprechen","Den Wert vor dem Verkauf erhöhen"),("fragen","Häufige Fragen"),
         ("weiterlesen","Weiterlesen")],
 "inhalt": f'''
<section id="wert">
{kennzahlen([
  ("254","Betriebsaufgaben im ersten Halbjahr 2025",
   'Quelle: ZDH-Statistik, ausgewertet von <a href="https://www.rebmann-research.de/zahntechnik-betriebszahlen-ruecklaeufig" rel="nofollow noopener" target="_blank">Rebmann Research</a>'),
  ("105","Neugründungen im selben Zeitraum",
   "Quelle: ebenda. Auf eine Gründung kommen rund 2,4 Aufgaben."),
  ("2003","Seit diesem Jahr gibt es den AWH-Standard",
   'Bewertungsverfahren für Handwerksbetriebe, herausgegeben vom <a href="https://www.zdh.de/ueber-uns/fachbereich-gewerbefoerderung/betriebsnachfolge/das-awh-verfahren-zur-bewertung-von-handwerksbetrieben/" rel="nofollow noopener" target="_blank">ZDH</a>'),
])}
<h2>Woraus der Preis entsteht</h2>
<p>Viele Inhaber rechnen den Wert ihres Labors aus dem, was darin steht: Fräsmaschine, Scanner, Ofen, Einrichtung. Ein Käufer rechnet anders. Er kauft keine Geräte, er kauft einen Ertrag, der auch ohne den bisherigen Inhaber weiterläuft. Geräte sind für ihn ein Posten, den er notfalls neu beschafft.</p>
<p>Das übliche Verfahren im Handwerk ist der AWH-Standard, entwickelt von der Arbeitsgemeinschaft der wertermittelnden Betriebsberater im Handwerk zusammen mit dem Zentralverband des Deutschen Handwerks. Er rechnet nach dem Ertragswertverfahren und berücksichtigt dabei, was inhabergeführte Betriebe von Industrieunternehmen unterscheidet. Seit 2009 ist er auch für Zwecke der Erbschaft- und Schenkungsteuer als branchenspezifisches Verfahren anerkannt.</p>
{schritte([
 ("1","Den Gewinn der letzten drei Jahre bereinigen: Sondereffekte heraus, private Posten heraus, Mieten an nahestehende Personen auf marktüblich rechnen."),
 ("2","Den kalkulatorischen Unternehmerlohn abziehen. Was übrig bleibt, ist der nachhaltige Ertrag."),
 ("3","Diesen Ertrag durch einen Zinssatz teilen, der das Risiko abbildet. Je unsicherer der Ertrag, desto höher der Zins und desto niedriger der Wert."),
])}
{merksatz("Der Satz, der am meisten Geld kostet",
 "„Das Labor läuft doch, das sehen die Zahlen.“ Die Zahlen zeigen die Vergangenheit. Bezahlt wird die Zukunft ohne Sie. Jede Praxis, die nur wegen Ihrer Person bleibt, zählt für den Käufer nicht als Ertrag, sondern als Risiko.")}
</section>

<section id="rechner">
<h2>Wertrechner</h2>
<p>Die Rechnung darunter ist bewusst einfach gehalten: nachhaltiger Ertrag geteilt durch einen Kapitalisierungszinssatz. Der Zinssatz steigt mit dem Risiko, und das größte Risiko in einem Dentallabor ist die Frage, auf wie vielen Praxen der Umsatz steht.</p>
{RECHNER}
<p>Der Ertragswert enthält weder Geräte noch Warenbestand. Beides wird gesondert bewertet und kann den Preis heben oder senken, je nach Alter und Zustand.</p>
</section>

<section id="abhaengigkeit">
<h2>Was den Preis drückt</h2>
{figur(FIG_ABHAENGIGKEIT, "Zwei Labore, gleicher Gewinn, unterschiedlicher Preis. Der Unterschied liegt in der Verteilung des Umsatzes auf die Praxen.")}
{tabelle(["Was ein Käufer prüft","Warum es den Preis bewegt","Was Sie dagegen tun können"],[
 ["Anteil der größten Praxis am Umsatz","Fällt sie weg, fällt der Ertrag weg, auf dem der Kaufpreis steht.","Neue Praxen gewinnen, bevor Sie verkaufen. Jede zusätzliche Praxis senkt den Anteil der größten."],
 ["Bindung der Praxen an Ihre Person","Ein Kundenstamm, der an Ihnen hängt, geht mit Ihnen.","Ansprechpartner im Team aufbauen, Zuständigkeiten schriftlich regeln, sich aus Routinegesprächen herausnehmen."],
 ["Alter der Belegschaft und offene Stellen","Ein Labor ohne Fachkräfte kann den Ertrag nicht halten.","Offene Stellen vor dem Verkauf besetzen, nicht danach."],
 ["Zustand der digitalen Kette","Veraltete Technik heißt Investitionsstau, den der Käufer vom Preis abzieht.","Anschaffungen nicht aufschieben, solange sie sich noch amortisieren."],
 ["Dauer und Übertragbarkeit des Mietvertrags","Ein Labor ohne Räume ist schwer zu übernehmen.","Verlängerungsoption und Übertragbarkeit rechtzeitig mit dem Vermieter klären."],
 ["Dokumentation der Abläufe","Was nur in Ihrem Kopf steht, ist für den Käufer nicht vorhanden.","Arbeitsanweisungen, Preislisten und Kundenprofile schriftlich festhalten."],
])}
</section>

<section id="steuer">
<h2>Steuern beim Verkauf</h2>
<p>Der Gewinn aus dem Verkauf eines Betriebs wird nicht wie laufender Gewinn besteuert. Das Einkommensteuergesetz kennt dafür zwei Erleichterungen, die beide an das Alter geknüpft sind. Die Angaben ersetzen keine Steuerberatung, sie zeigen nur, worüber Sie mit Ihrer Beraterin sprechen sollten.</p>
{tabelle(["Regel","Was sie bedeutet","Bedingungen"],[
 ["Freibetrag nach § 16 Absatz 4 EStG",
  "Vom Veräußerungsgewinn bleiben 45.000 Euro steuerfrei.",
  "Das 55. Lebensjahr ist vollendet oder dauernde Berufsunfähigkeit im sozialversicherungsrechtlichen Sinne liegt vor. Auf Antrag. Nur einmal im Leben. Der Freibetrag verringert sich um den Betrag, um den der Veräußerungsgewinn 136.000 Euro übersteigt."],
 ["Ermäßigter Steuersatz nach § 34 Absatz 3 EStG",
  "Der Gewinn wird mit 56 Prozent des durchschnittlichen Steuersatzes versteuert, mindestens jedoch mit 14 Prozent.",
  "Ebenfalls ab dem vollendeten 55. Lebensjahr oder bei dauernder Berufsunfähigkeit. Auf Antrag, nur einmal im Leben, für Gewinne bis 5 Millionen Euro."],
 ["Fünftelregelung nach § 34 Absatz 1 EStG",
  "Die Steuer wird so berechnet, als verteile sich der Gewinn auf fünf Jahre.",
  "Kein Mindestalter. Wirkt vor allem dann, wenn das übrige Einkommen im Verkaufsjahr niedrig ist."],
])}
{merksatz("Was daraus für die Planung folgt",
 "Wer mit 53 verkauft, verschenkt unter Umständen beide Erleichterungen. Wer sie nutzen will, plant das Verkaufsjahr nach dem Geburtstag, nicht nach dem Angebot. Rechnen Sie das mit Ihrer Steuerberatung durch, bevor Sie einen Termin zusagen.")}
</section>

<section id="ablauf">
<h2>Der Ablauf in sieben Schritten</h2>
{schritte([
 ("1","Zahlen aufbereiten: drei Jahresabschlüsse, bereinigt, mit Erläuterung der Sondereffekte."),
 ("2","Wert ermitteln lassen. Die Handwerkskammern vermitteln Wertermittler, die nach dem AWH-Standard arbeiten."),
 ("3","Steuerliche Folgen durchrechnen, bevor ein Preis im Raum steht."),
 ("4","Unterlagen zusammenstellen: Kundenliste mit Umsatzanteilen, Personalübersicht, Geräteliste, Mietvertrag, offene Verbindlichkeiten."),
 ("5","Käufer ansprechen: eigene Mitarbeitende, Labore in der Region, Depots, die Handwerkskammer, Nachfolgebörsen."),
 ("6","Vertraulichkeit regeln, bevor Zahlen herausgehen. Erst Erklärung, dann Einblick."),
 ("7","Kaufvertrag anwaltlich prüfen lassen, insbesondere Haftung für Altverbindlichkeiten, Übergang der Arbeitsverhältnisse nach § 613a BGB und Wettbewerbsverbot."),
])}
{merksatz("Zeit ist der Preisfaktor, den niemand einrechnet",
 "Ein Labor, das verkauft werden muss, bringt weniger als eines, das verkauft werden kann. Wer zwei bis drei Jahre Vorlauf hat, kann Abhängigkeiten abbauen, Stellen besetzen und den Ertrag stabilisieren. Wer sechs Monate hat, verkauft den Ist-Zustand.")}
</section>

<section id="unterlagen">
<h2>Prüfliste vor dem ersten Gespräch</h2>
<p>Was ein ernsthafter Käufer sehen will, bevor er über einen Preis spricht. Fehlt etwas davon, verhandelt er den Abschlag dafür.</p>
{checkliste([
 "Drei Jahresabschlüsse, bereinigt, mit Erläuterung jedes Sondereffekts",
 "Betriebswirtschaftliche Auswertung des laufenden Jahres",
 "Kundenliste mit Umsatzanteil je Praxis über drei Jahre",
 "Personalübersicht mit Qualifikation, Alter, Betriebszugehörigkeit und Kündigungsfristen",
 "Geräteliste mit Anschaffungsjahr, Restbuchwert und Wartungsverträgen",
 "Mietvertrag mit Restlaufzeit, Verlängerungsoption und Übertragbarkeit",
 "Offene Verbindlichkeiten, Leasingverträge, Sicherheiten",
 "Nachweis der Eintragung in die Handwerksrolle und des Qualitätsmanagements",
 "Kalkulierte Preisliste, BEL II und BEB getrennt ausgewiesen",
], "verkaufen")}
{mitnehmen("Anschreiben an Ihre Praxen vor der Übergabe",
 VORLAGE_ANFRAGE)}
</section>
''',
 "faq": [
  ("Was ist mein Dentallabor wert?",
   "Der Wert entsteht aus dem nachhaltigen Ertrag nach Abzug eines kalkulatorischen Unternehmerlohns, geteilt durch einen Zinssatz, der das Risiko abbildet. Geräte und Warenbestand kommen gesondert hinzu. Ein Pauschalwert je Umsatz oder je Mitarbeiter führt in die Irre, weil er das Risiko nicht abbildet. Im Handwerk ist der AWH-Standard das übliche Verfahren; Wertermittler vermitteln die Handwerkskammern."),
  ("Wie lange dauert der Verkauf eines Dentallabors?",
   "Dafür gibt es keinen belegbaren Durchschnittswert, den wir nennen könnten. Planbar ist die Vorbereitung: Zahlen aufbereiten, Wert ermitteln, Steuerfolgen klären und Unterlagen zusammenstellen lässt sich in wenigen Monaten erledigen. Die Suche nach einem passenden Käufer und die Verhandlung liegen nicht in Ihrer Hand."),
  ("Muss der Käufer Zahntechnikermeister sein?",
   "Das Zahntechnikerhandwerk ist zulassungspflichtig nach Anlage A Nummer 37 der Handwerksordnung. Der Betrieb muss deshalb in der Handwerksrolle eingetragen sein. Dafür genügt es, dass die fachliche Leitung durch eine eingetragene Person sichergestellt ist; der Käufer selbst muss nicht zwingend Meister sein. Welche Gestaltung in Ihrem Fall trägt, klärt die zuständige Handwerkskammer verbindlich."),
  ("Was passiert mit meinen Mitarbeitenden?",
   "Bei einem Betriebsübergang gehen die Arbeitsverhältnisse nach § 613a BGB auf den Erwerber über, mit allen Rechten und Pflichten. Eine Kündigung wegen des Übergangs ist unwirksam. Die Beschäftigten sind vorher schriftlich zu unterrichten und können dem Übergang widersprechen."),
  ("Lohnt es sich, vor dem Verkauf noch neue Praxen zu gewinnen?",
   "Rechnerisch ja, sofern genug Zeit bleibt. Jede zusätzliche Praxis senkt den Umsatzanteil der größten und damit das Risiko, das ein Käufer einpreist. Der Wertrechner auf dieser Seite zeigt den Unterschied zwischen einem Labor, dessen Umsatz an wenigen Praxen hängt, und einem mit breit verteiltem Kundenstamm. Ob sich der Aufwand in Ihrem Fall rechnet, hängt vom Zeitpunkt des Verkaufs ab."),
 ],
 "abschluss": abschluss(
  "Den Wert vor dem Verkauf erhöhen",
  "Wer zwei Jahre vor der Übergabe anfängt, neue Praxen zu gewinnen, verkauft ein anderes Labor als jemand, der den Ist-Zustand anbietet. Der Gewinn muss dafür nicht steigen. Es reicht, dass er auf mehr Schultern steht. Genau das ist unsere Aufgabe: Wir richten Ihre Werbung auf passende Praxen in Ihrem Einzugsgebiet aus und prüfen die Anfragen anhand Ihres Kundenprofils. Die Gespräche führen Sie.",
  [("1","Kundenprofil festlegen: welche Praxen passen zu Ihrer Fertigung"),
   ("2","Kampagne im vereinbarten Einzugsgebiet"),
   ("3","Anfragen vorqualifiziert, Gespräche bei Ihnen"),
   ("4","Umsatz verteilt sich auf mehr Praxen, das Risiko für den Käufer sinkt")],
  "Der Weg von der einzelnen Anfrage zum breiteren Kundenstamm. Eine bestimmte Wertsteigerung ist damit nicht zugesagt."),
 "nachspann": weiterlesen([
  ("/wissen/dentallabor-kaufen-oder-uebernehmen/", "Dentallabor kaufen oder übernehmen",
   "Dieselbe Übergabe aus Sicht des Käufers, mit Prüfliste und Anschreiben."),
  ("/wissen/preise-und-stundensatz-im-dentallabor/", "Preise und Stundensatz",
   "Der Stundensatz bestimmt den Ertrag, und der Ertrag bestimmt den Preis."),
  ("/wissen/kundenakquise-im-dentallabor/", "Kundenakquise im Dentallabor",
   "Sieben Wege zu neuen Praxen, mit Bedarfsrechner."),
  ("/wissen/zahntechnik-in-zahlen/", "Zahntechnik in Zahlen",
   "Wie viele Labore es gibt und wie viele jedes Jahr aufgeben."),
 ]),
}
