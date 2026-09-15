# -*- coding: utf-8 -*-
"""Kundenakquise im Dentallabor. Zielsuchen: kundenakquise dentallabor,
akquise dentallabor, dental akquise (per Google-Vorschlag belegt)."""
from wissen_bauen import (kennzahlen, figur, merksatz, mitnehmen, weiterlesen,
                          schritte, checkliste, tabelle)

FIG_SCHWUND = '''<svg viewBox="0 0 640 260" role="img" aria-labelledby="t-schwund">
<title id="t-schwund">Ein Kundenstamm verliert jedes Jahr Praxen. Ohne Nachschub sinkt die Zahl der Auftraggeber.</title>
<g font-size="13" fill="#4A5568">
<line x1="60" y1="210" x2="610" y2="210" stroke="#DDE3EA" stroke-width="1"/>
<line x1="60" y1="30" x2="60" y2="210" stroke="#DDE3EA" stroke-width="1"/>
<text x="16" y="44">24</text><text x="16" y="129">12</text><text x="24" y="214">0</text>
<rect x="85" y="60" width="52" height="150" rx="6" fill="#0068C9"/>
<rect x="185" y="79" width="52" height="131" rx="6" fill="#0068C9" opacity=".82"/>
<rect x="285" y="98" width="52" height="112" rx="6" fill="#0068C9" opacity=".64"/>
<rect x="385" y="117" width="52" height="93" rx="6" fill="#0068C9" opacity=".46"/>
<rect x="485" y="136" width="52" height="74" rx="6" fill="#0068C9" opacity=".3"/>
<text x="92" y="232">heute</text><text x="190" y="232">Jahr 1</text><text x="290" y="232">Jahr 2</text>
<text x="390" y="232">Jahr 3</text><text x="490" y="232">Jahr 4</text>
<text x="98" y="52" fill="#061421" font-size="14">20</text>
<text x="198" y="71" fill="#061421" font-size="14">17</text>
<text x="298" y="90" fill="#061421" font-size="14">15</text>
<text x="398" y="109" fill="#061421" font-size="14">12</text>
<text x="498" y="128" fill="#061421" font-size="14">10</text>
</g></svg>'''

FIG_TRICHTER = '''<svg viewBox="0 0 640 300" role="img" aria-labelledby="t-trichter">
<title id="t-trichter">Vom angesprochenen Praxiskreis bleiben nach Vorqualifizierung und Gespräch einige wenige neue Auftraggeber übrig.</title>
<defs><marker id="pf-akq" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">
<path d="M0 0 L9 4.5 L0 9 z" fill="#8A93A3"/></marker></defs>
<g font-size="14">
<rect x="70" y="24" width="500" height="52" rx="10" fill="#0068C9" opacity=".12"/>
<text x="90" y="55" fill="#061421">Praxen im vereinbarten Gebiet</text>
<rect x="130" y="100" width="380" height="52" rx="10" fill="#0068C9" opacity=".26"/>
<text x="150" y="131" fill="#061421">Anfrage über das Formular</text>
<rect x="190" y="176" width="260" height="52" rx="10" fill="#0068C9" opacity=".5"/>
<text x="210" y="207" fill="#061421">Vorqualifiziert nach Profil</text>
<rect x="250" y="252" width="140" height="42" rx="10" fill="#0068C9"/>
<text x="268" y="278" fill="#ffffff">Ihr Gespräch</text>
<line x1="320" y1="78" x2="320" y2="96" stroke="#8A93A3" stroke-width="1.6" marker-end="url(#pf-akq)"/>
<line x1="320" y1="154" x2="320" y2="172" stroke="#8A93A3" stroke-width="1.6" marker-end="url(#pf-akq)"/>
<line x1="320" y1="230" x2="320" y2="248" stroke="#8A93A3" stroke-width="1.6" marker-end="url(#pf-akq)"/>
</g></svg>'''

VORLAGE_ERSTKONTAKT = """Betreff: Kapazität für Ihre Kronen- und Brückenarbeiten

Guten Tag Frau Dr. ...,

mein Name ist ..., ich führe ein zahntechnisches Labor in ... .
Wir haben derzeit Kapazität für zwei zusätzliche Praxen und arbeiten
im Umkreis von ... Kilometern.

Drei Punkte, die für Sie wichtig sein könnten:
1. Kronen und Brücken liefern wir in ... Arbeitstagen.
2. Rückfragen beantworte ich selbst, werktags bis ... Uhr.
3. Die erste Arbeit rechnen wir zum vereinbarten Preis ab. Passt sie
   nicht, tragen wir die Nacharbeit.

Wenn das interessant ist: Ich komme gern für zwanzig Minuten vorbei
und bringe zwei Arbeiten mit, die Sie in die Hand nehmen können.

Freundliche Grüße
..."""

SEITE = {
 "slug": "kundenakquise-im-dentallabor",
 "titel": "Kundenakquise im Dentallabor: neue Zahnarztpraxen gewinnen | Laboraquise.de",
 "beschreibung": "Sieben Wege zu neuen Zahnarztpraxen, ehrlich bewertet: Empfehlung, Besuch, Depot, Messe, Website, Werbung. Mit Rechner, Gesprächsvorlage und Prüfliste für Dentallabore.",
 "krume": "Kundenakquise im Dentallabor",
 "pille": "Wissen für Dentallabore",
 "h1": 'Kundenakquise im <span class="text-color-primary">Dentallabor</span>',
 "h1_klartext": "Kundenakquise im Dentallabor: neue Zahnarztpraxen gewinnen",
 "lead": "Sieben Wege zu neuen Praxen, mit Aufwand, Vorlauf und Steuerbarkeit nebeneinandergestellt. Dazu ein Rechner für Ihren eigenen Bedarf und ein Gesprächseinstieg zum Mitnehmen.",
 "about": "Kundengewinnung für zahntechnische Labore",
 "toc": [("lage","Warum der Bedarf steigt"),("anders","Was Laborakquise besonders macht"),
         ("wege","Die sieben Wege im Vergleich"),("bedarf","Wie viele Praxen brauchen Sie?"),
         ("profil","Das Kundenprofil zuerst"),("kontakt","Der erste Kontakt"),
         ("fehler","Woran Akquise scheitert"),("pruefung","Selbstprüfung"),
         ("fragen","Häufige Fragen"),("weiterlesen","Weiterlesen")],
 "inhalt": f'''
<section id="lage">
{kennzahlen([
  ("6.845","Zahntechnikbetriebe in Deutschland, Stand erstes Halbjahr 2025",
   'Quelle: ZDH-Statistik, ausgewertet von <a href="https://www.rebmann-research.de/zahntechnik-betriebszahlen-ruecklaeufig" rel="nofollow noopener" target="_blank">Rebmann Research</a>'),
  ("254","Betriebsaufgaben im ersten Halbjahr 2025",
   "Quelle: ebenda. Im selben Zeitraum 105 Neugründungen."),
  ("3,4 %","Rückgang der Betriebszahl von 2023 auf 2024",
   "Quelle: ebenda. Eine Betriebszahl ist keine Aussage über einzelne Labore."),
])}
<h2>Warum der Bedarf an neuen Praxen gerade steigt</h2>
<p>Die Zahl der zahntechnischen Betriebe in Deutschland sinkt seit Jahren. Im ersten Halbjahr 2025 standen 105 Neugründungen 254 Betriebsaufgaben gegenüber. Jedes aufgegebene Labor hatte Auftraggeber. Diese Praxen arbeiten weiter und brauchen ein Labor.</p>
<p>Für Ihr Labor heißt das zweierlei. Es gibt Praxen, die tatsächlich suchen. Und es gibt Wettbewerber, die dieselbe Lücke sehen. Wer wartet, bis eine Praxis von allein anruft, überlässt die Auswahl dem Zufall.</p>
{merksatz("Eine Zahl, die oft falsch gelesen wird",
 "Eine sinkende Betriebszahl bedeutet nicht, dass die Nachfrage nach Zahnersatz sinkt. Sie bedeutet, dass die vorhandene Arbeit auf weniger Labore verteilt wird. Wer die frei werdenden Praxen erreicht, wächst. Wer sie nicht erreicht, merkt davon nichts.")}
</section>

<section id="anders">
<h2>Was Laborakquise von normalem Verkauf unterscheidet</h2>
<p>Eine Zahnarztpraxis wechselt ihr Labor nicht wegen eines Sonderangebots. Sie wechselt, weil etwas nicht mehr passt: Liefertermine, Erreichbarkeit, Nacharbeit, ein Wechsel in der Praxisleitung. Diese Anlässe entstehen unregelmäßig und lassen sich nicht herbeireden.</p>
<p>Daraus folgen drei Dinge für Ihre Akquise:</p>
<ul>
<li><b>Sie verkaufen Verlässlichkeit, nicht Technik.</b> Fräszentrum, Scanner und Materialien hat der Wettbewerb auch. Was eine Praxis wirklich bewertet, ist der Termin und der Umgang mit Fehlern.</li>
<li><b>Sie brauchen Kontakt im richtigen Moment.</b> Wer nur einmal fragt, trifft den Anlass fast nie. Wer sichtbar und erreichbar bleibt, wird gefunden, wenn der Anlass eintritt.</li>
<li><b>Ein Kunde ist viel wert.</b> Eine Praxis, die bleibt, liefert über Jahre Umsatz. Deshalb lohnt sich Aufwand pro Kontakt, der in anderen Branchen unwirtschaftlich wäre.</li>
</ul>
{figur(FIG_SCHWUND, "Schematische Darstellung: Ein Kundenstamm verliert durch Praxisabgaben, Eigenlabore und Wettbewerb laufend Auftraggeber. Die Zahlen sind ein Beispiel, kein Branchenwert. Ohne eigene Ansprache sinkt die Zahl der Auftraggeber, auch wenn die Arbeit stimmt.", 500)}
</section>

<section id="wege">
<h2>Die sieben Wege zu neuen Praxen im Vergleich</h2>
<p>Alle sieben funktionieren. Sie unterscheiden sich in Vorlauf, Aufwand und darin, ob Sie den Zeitpunkt selbst bestimmen können. Die Einschätzungen sind unsere Erfahrungswerte aus Gesprächen mit Laboren, keine gemessenen Branchenzahlen.</p>
{tabelle(["Weg","Vorlauf","Ihr Aufwand","Steuerbar?"],[
 ["Empfehlung durch bestehende Praxen","Unbestimmt","Gering","Nein. Sie bestimmen den Zeitpunkt nicht."],
 ["Persönlicher Besuch in der Praxis","Kurz","Hoch. Ein Termin bindet eine halbe Stunde plus Fahrt.","Ja, aber begrenzt durch Ihre Zeit."],
 ["Telefonische Ansprache","Kurz","Mittel. Die Praxisleitung ist selten am Telefon.","Ja, mit hoher Absagequote."],
 ["Depot und Außendienst","Mittel","Gering","Nein. Der Vertreter entscheidet, wen er nennt."],
 ["Messe und Fortbildung","Mittel","Hoch an wenigen Tagen","Teilweise."],
 ["Eigene Website und Google","Lang. Sichtbarkeit wächst über Monate.","Einmalig hoch, danach gering","Teilweise. Sie bestimmen den Inhalt, nicht das Ranking."],
 ["Bezahlte Werbung mit Vorqualifizierung","Kurz. Anfragen entstehen ab Kampagnenstart.","Gering im laufenden Betrieb, Gespräche bleiben bei Ihnen","Ja. Gebiet, Arbeiten und Anzahl legen Sie vorher fest."],
])}
<p>Die ersten sechs Wege sollten Sie ohnehin nutzen. Der siebte ist der einzige, bei dem Sie Gebiet und Menge vorher festlegen. Genau das ist unsere Arbeit.</p>
</section>

<section id="bedarf">
<h2>Wie viele Praxen brauchen Sie wirklich?</h2>
<p>Bevor Sie über Werbung nachdenken, rechnen Sie den Bedarf aus. Nicht die Wunschzahl, sondern die Zahl, die zu Ihrer freien Kapazität passt.</p>
<div class="rechner" data-rechner="bedarf">
  <h3>Bedarfsrechner</h3>
  <p class="rechner__hinweis">Alle Werte setzen Sie selbst. Das Ergebnis ist eine Rechnung mit Ihren Annahmen, keine Prognose und keine Zusage.</p>
  <div class="rechner__feld">
    <label for="b-umsatz">Angenommener Laborumsatz je Praxis und Monat</label>
    <input type="number" id="b-umsatz" value="12000" min="0" step="500" inputmode="numeric">
    <small>Setzen Sie Ihren eigenen Erfahrungswert ein.</small>
  </div>
  <div class="rechner__feld">
    <label for="b-ziel">Zusätzlicher Jahresumsatz, den Sie anstreben</label>
    <input type="number" id="b-ziel" value="200000" min="0" step="10000" inputmode="numeric">
  </div>
  <div class="rechner__feld">
    <label for="b-abgang">Praxen, die Sie pro Jahr erfahrungsgemäß verlieren</label>
    <input type="number" id="b-abgang" value="2" min="0" max="20" step="1" inputmode="numeric">
    <small>Praxisabgabe, Eigenlabor, Wettbewerb. Wer das auf null setzt, rechnet ohne Abgang.</small>
  </div>
  <div class="rechner__ausgabe">
    <div class="rechner__zelle"><span>Neue Praxen für das Wachstumsziel</span><output id="b-wachstum">2</output></div>
    <div class="rechner__zelle"><span>Neue Praxen inklusive Ersatz für Abgänge</span><output id="b-gesamt">4</output></div>
  </div>
</div>
<p>Die zweite Zahl ist die wichtigere. Wer nur das Wachstumsziel rechnet und den Abgang vergisst, tritt auf der Stelle und wundert sich.</p>
</section>

<section id="profil">
<h2>Das Kundenprofil steht vor der ersten Ansprache</h2>
<p>Jede Ansprache ohne Profil erzeugt Gespräche mit Praxen, die nicht passen. Das kostet mehr Zeit als es bringt. Vier Festlegungen reichen:</p>
{schritte([
 ("1","Gebiet: In welchem Umkreis holen und liefern Sie zuverlässig? Nähe ist im Laborgeschäft ein echtes Verkaufsargument."),
 ("2","Arbeiten: Welche Arbeiten wollen Sie zusätzlich, welche nicht? Ein volles Haus mit den falschen Arbeiten ist kein Erfolg."),
 ("3","Ansprechpartner: Inhaber, Mitinhaber oder angestellte Leitung. Wer nicht entscheiden darf, kann auch nicht wechseln."),
]) }
<p style="margin-top:1.5rem">Die vierte Festlegung ist die unbequemste: Was bieten Sie beim Einstieg an, das eine Praxis zum Ausprobieren bewegt? Eine erste Arbeit zum festen Preis, eine zugesagte Liefertermin-Garantie für den Probelauf, ein fester Ansprechpartner. Ohne einen konkreten Einstieg bleibt es bei „Melden Sie sich gern".</p>
{figur(FIG_TRICHTER, "So entsteht ein Gespräch: Aus dem angesprochenen Praxiskreis wird eine Anfrage, aus der Anfrage nach Prüfung des Profils ein Gespräch. Die Zahlen je Stufe hängen von Gebiet, Angebot und Kampagne ab und werden vorher vereinbart.", 460)}
</section>

<section id="kontakt">
<h2>Der erste Kontakt: was eine Praxis hören will</h2>
<p>Eine Zahnarztpraxis hat wenig Zeit und hört Laborwerbung häufig. Drei Sätze entscheiden, ob weitergelesen wird: Wo sitzen Sie, welche Arbeit übernehmen Sie, und was passiert, wenn etwas nicht stimmt.</p>
<p>Was nicht funktioniert: Aufzählungen von Geräten, Zertifikaten und Materialien. Die kann eine Praxis nicht bewerten, und sie stehen in jedem zweiten Schreiben.</p>
{mitnehmen("Gesprächseinstieg zum Anpassen und Kopieren", VORLAGE_ERSTKONTAKT)}
<p>Passen Sie die Punkte an Ihr Labor an. Nennen Sie echte Zahlen: echte Arbeitstage, echte Uhrzeiten, eine echte Regelung für Nacharbeit. Eine Zusage, die Sie nicht halten, kostet Sie den Kunden beim ersten Fall.</p>
</section>

<section id="fehler">
<h2>Woran Akquise im Dentallabor meistens scheitert</h2>
<ul>
<li><b>Es wird erst gesucht, wenn es weh tut.</b> Wenn die Auslastung schon eingebrochen ist, fehlt Geld und Ruhe für eine ordentliche Ansprache.</li>
<li><b>Niemand ist zuständig.</b> Der Inhaber macht Akquise, wenn Zeit bleibt. Zeit bleibt nie.</li>
<li><b>Die Anfrage wird zu spät beantwortet.</b> Eine Praxis, die drei Tage auf Antwort wartet, hat den Anlass vergessen.</li>
<li><b>Es wird über Technik gesprochen statt über Zusammenarbeit.</b> Siehe oben.</li>
<li><b>Ein Versuch, dann Schluss.</b> Wer einmal zwanzig Praxen anschreibt und aufhört, hat den Zeitpunkt getroffen oder eben nicht.</li>
</ul>
</section>

<section id="pruefung">
<h2>Selbstprüfung für Ihr Labor</h2>
<p>Haken Sie ab, was heute schon feststeht. Was offen bleibt, ist Ihre Aufgabenliste.</p>
{checkliste([
 "Ich weiß, wie viele Praxen ich zusätzlich versorgen kann, ohne neu einzustellen.",
 "Ich weiß, welche Arbeiten ich zusätzlich übernehmen will und welche nicht.",
 "Mein Einzugsgebiet ist in Kilometern festgelegt, nicht als Gefühl.",
 "Ich habe ein konkretes Einstiegsangebot für eine neue Praxis.",
 "Anfragen beantwortet bei mir eine namentlich festgelegte Person, spätestens am nächsten Werktag.",
 "Ich weiß, wie viele Praxen ich im letzten Jahr verloren habe und warum.",
 "Ich habe eine Liste der Praxen in meinem Gebiet, die noch nicht mit mir arbeiten.",
], "akquise")}
</section>
''',
 "faq": [
  ("Was kostet Kundenakquise für ein Dentallabor?",
   "Das hängt vom Weg ab. Persönliche Besuche kosten vor allem Ihre Arbeitszeit. Bezahlte Werbung kostet Werbebudget an die Plattform plus die Dienstleistungsgebühr. Bei Laboraquise.de werden Leistungsumfang, Laufzeit und Bedingungen vor der Beauftragung im Angebot festgelegt. Eine pauschale Preisangabe ohne Ihr Gebiet und Ihre Arbeiten wäre eine Schätzung."),
  ("Wie lange dauert es, bis eine neue Praxis liefert?",
   "Zwischen dem ersten Kontakt und der ersten Arbeit liegt in der Regel ein persönliches Gespräch und ein Probelauf mit einer einzelnen Arbeit. Einen festen Zeitraum sagen wir nicht zu. Er hängt davon ab, wie schnell Sie Gespräche führen und ob die Praxis gerade einen Anlass zum Wechsel hat."),
  ("Ist Kaltakquise bei Zahnarztpraxen erlaubt?",
   "Telefonische Werbung gegenüber Unternehmen setzt nach § 7 UWG eine mutmaßliche Einwilligung voraus, Werbe-E-Mails ohne vorherige Einwilligung sind grundsätzlich unzulässig. Der persönliche Besuch und Werbung, auf die eine Praxis selbst reagiert, sind davon nicht betroffen. Prüfen Sie Ihren konkreten Fall anwaltlich, dieser Text ist keine Rechtsberatung."),
  ("Lohnt sich Akquise, wenn mein Labor gut ausgelastet ist?",
   "Zwei Gründe sprechen dafür. Erstens verlieren Sie regelmäßig Praxen, ohne es steuern zu können. Zweitens macht eine starke Abhängigkeit von wenigen großen Auftraggebern Preisgespräche schwer. Ob zusätzliche Arbeit wirtschaftlich möglich ist, prüfen Sie mit dem Rechner oben."),
 ],
 "nachspann": weiterlesen([
  ("/wissen/warum-zahnaerzte-das-dentallabor-wechseln/","Warum Zahnärzte ihr Dentallabor wechseln",
   "Die Anlässe für einen Wechsel und wie Sie sie im Gespräch erkennen."),
  ("/wissen/preise-und-stundensatz-im-dentallabor/","Preise und Stundensatz im Dentallabor",
   "BEL II, BEB und der Stundensatz, den Ihr Labor wirklich braucht. Mit Rechner."),
  ("/wissen/eigenlabor-und-praxislabor/","Eigenlabor und Praxislabor verstehen",
   "Warum Praxen eigene Labore aufbauen und wo das Fremdlabor im Vorteil bleibt."),
  ("/wissen/zahntechnik-in-zahlen/","Zahntechnik in Zahlen",
   "Betriebe, Aufgaben, Gründungen. Die belegten Zahlen zur Lage der Branche."),
 ]),
}
