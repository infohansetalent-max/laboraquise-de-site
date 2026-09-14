# -*- coding: utf-8 -*-
"""Zahntechnik in Zahlen. Zielsuchen (Google-Vorschlag belegt): anzahl
dentallabore in deutschland, wie viele dentallabore gibt es in deutschland,
umsatz dentallabore deutschland."""
from wissen_bauen import (kennzahlen, figur, merksatz, weiterlesen,
                          checkliste, tabelle)

FIG_VERLAUF = '''<svg viewBox="0 0 640 260" role="img" aria-labelledby="t-verlauf">
<title id="t-verlauf">Entwicklung der Zahl zahntechnischer Betriebe in Deutschland von 2023 bis zur Jahresmitte 2025.</title>
<g font-size="13.5" fill="#4A5568">
<line x1="76" y1="200" x2="600" y2="200" stroke="#DDE3EA"/>
<line x1="76" y1="30" x2="76" y2="200" stroke="#DDE3EA"/>
<text x="14" y="48">7.300</text><text x="14" y="124">7.000</text><text x="14" y="200">6.700</text>
<rect x="130" y="41" width="88" height="159" rx="8" fill="#0068C9" opacity=".45"/>
<rect x="290" y="61" width="88" height="139" rx="8" fill="#0068C9" opacity=".7"/>
<rect x="450" y="99" width="88" height="101" rx="8" fill="#0068C9"/>
<text x="140" y="222">2023</text><text x="300" y="222">2024</text><text x="450" y="222">Mitte 2025</text>
<text x="136" y="33" fill="#061421" font-size="14">7.238</text>
<text x="296" y="53" fill="#061421" font-size="14">6.994</text>
<text x="456" y="91" fill="#061421" font-size="14">6.845</text>
<text x="76" y="250" font-size="12">2023 abgeleitet aus 6.994 und dem angegebenen Rückgang von 3,4 Prozent.</text>
</g></svg>'''

FIG_SALDO = '''<svg viewBox="0 0 640 210" role="img" aria-labelledby="t-saldo">
<title id="t-saldo">Im ersten Halbjahr 2025 kamen auf 105 Neugründungen 254 Betriebsaufgaben.</title>
<g font-size="14">
<text x="40" y="52" fill="#061421">Neugründungen</text>
<rect x="210" y="32" width="145" height="34" rx="8" fill="#0068C9" opacity=".4"/>
<text x="366" y="55" fill="#061421">105</text>
<text x="40" y="122" fill="#061421">Betriebsaufgaben</text>
<rect x="210" y="102" width="351" height="34" rx="8" fill="#0068C9"/>
<text x="572" y="125" fill="#061421">254</text>
<text x="40" y="180" fill="#4A5568" font-size="12.5">Erstes Halbjahr 2025. Auf eine Gründung kommen rund 2,4 Aufgaben.</text>
</g></svg>'''

QUELLE = ('Quelle: ZDH-Statistik, ausgewertet von <a href="https://www.rebmann-research.de/'
          'zahntechnik-betriebszahlen-ruecklaeufig" rel="nofollow noopener" target="_blank">Rebmann Research</a>')

SEITE = {
 "slug": "zahntechnik-in-zahlen",
 "titel": "Wie viele Dentallabore gibt es in Deutschland? Zahlen mit Quelle | Laboraquise.de",
 "beschreibung": "Zahl der zahntechnischen Betriebe in Deutschland, Neugründungen und Betriebsaufgaben mit Quellenangabe. Und was die Entwicklung für einzelne Labore praktisch bedeutet.",
 "krume": "Zahntechnik in Zahlen",
 "pille": "Wissen für Dentallabore",
 "h1": 'Zahntechnik <span class="text-color-primary">in Zahlen</span>',
 "h1_klartext": "Zahntechnik in Zahlen: Betriebe, Gründungen und Aufgaben in Deutschland",
 "lead": "Wie viele zahntechnische Betriebe es in Deutschland gibt, wie sich die Zahl entwickelt und was daraus für ein einzelnes Labor folgt. Jede Zahl mit Quelle, Abgeleitetes ist als abgeleitet gekennzeichnet.",
 "about": "Marktzahlen des Zahntechnikerhandwerks",
 "toc": [("bestand","Wie viele Labore es gibt"),("entwicklung","Die Entwicklung seit 2023"),
         ("saldo","Gründungen und Aufgaben"),("bedeutung","Was das für Ihr Labor bedeutet"),
         ("unbelegt","Was wir nicht belegen können"),("fragen","Häufige Fragen"),("weiterlesen","Weiterlesen")],
 "inhalt": f'''
<section id="bestand">
{kennzahlen([
  ("6.845","Zahntechnikbetriebe in Deutschland, Stand erstes Halbjahr 2025", QUELLE),
  ("6.994","Gewerbliche Dentallabore im Jahr 2024", QUELLE),
  ("3,4 %","Rückgang der Betriebszahl von 2023 auf 2024", QUELLE),
])}
<h2>Wie viele Dentallabore gibt es in Deutschland?</h2>
<p>Zum Ende des ersten Halbjahres 2025 gab es in Deutschland <b>6.845 zahntechnische Betriebe</b>. Im Jahr 2024 waren es 6.994 gewerbliche Dentallabore. Die Zahlen stammen aus der Statistik des Zentralverbands des Deutschen Handwerks und wurden von Rebmann Research ausgewertet.</p>
<p>Gemeint sind gewerbliche Labore, also eingetragene Betriebe des Zahntechnikerhandwerks. Praxislabore innerhalb von Zahnarztpraxen sind darin nicht enthalten. Wer beide Zahlen vergleicht, vergleicht zwei verschiedene Dinge.</p>
</section>

<section id="entwicklung">
<h2>Die Entwicklung seit 2023</h2>
{figur(FIG_VERLAUF, "Entwicklung der Betriebszahl. Die Werte für 2024 und Mitte 2025 sind belegt. Der Wert für 2023 ist aus der Angabe von 6.994 Betrieben und dem genannten Rückgang von 3,4 Prozent abgeleitet und deshalb gerundet.", 520)}
<p>Der Rückgang ist kein einmaliger Ausschlag. Er setzt eine längere Entwicklung fort und hat sich im ersten Halbjahr 2025 beschleunigt.</p>
</section>

<section id="saldo">
<h2>Gründungen und Aufgaben im ersten Halbjahr 2025</h2>
<p>Im ersten Halbjahr 2025 wurden <b>105 Neugründungen</b> gezählt, dem standen <b>254 Betriebsaufgaben</b> gegenüber. Auf eine Gründung kommen damit rund 2,4 Aufgaben.</p>
{figur(FIG_SALDO, "Neugründungen und Betriebsaufgaben im ersten Halbjahr 2025. Quelle: ZDH-Statistik, ausgewertet von Rebmann Research.", 480)}
{tabelle(["Größe","Wert","Zeitraum","Art der Angabe"],[
 ["Zahntechnische Betriebe","6.845","Erstes Halbjahr 2025","Belegt"],
 ["Gewerbliche Dentallabore","6.994","2024","Belegt"],
 ["Rückgang der Betriebszahl","3,4 Prozent","2023 auf 2024","Belegt"],
 ["Neugründungen","105","Erstes Halbjahr 2025","Belegt"],
 ["Betriebsaufgaben","254","Erstes Halbjahr 2025","Belegt"],
 ["Verhältnis Aufgaben zu Gründungen","rund 2,4 zu 1","Erstes Halbjahr 2025","Abgeleitet aus 254 geteilt durch 105"],
 ["Betriebe 2023","rund 7.238","2023","Abgeleitet aus 6.994 und 3,4 Prozent"],
])}
</section>

<section id="bedeutung">
<h2>Was das für Ihr Labor praktisch bedeutet</h2>
<p>Eine sinkende Betriebszahl sagt nichts darüber, ob weniger Zahnersatz gebraucht wird. Sie sagt, dass die vorhandene Arbeit auf weniger Labore verteilt wird. Für ein einzelnes Labor folgt daraus dreierlei:</p>
<ul>
<li><b>Es gibt suchende Praxen.</b> Jedes aufgegebene Labor hatte Auftraggeber. Diese Praxen behandeln weiter und brauchen ein Labor.</li>
<li><b>Sie werden nicht automatisch gefunden.</b> Eine Praxis, deren Labor schließt, fragt zuerst im Kollegenkreis und beim Depot. Wer dort nicht genannt wird, kommt nicht vor.</li>
<li><b>Der Zeitpunkt lässt sich nicht abwarten.</b> Die Praxis entscheidet innerhalb weniger Wochen. Wer erst dann anfängt, sichtbar zu werden, kommt zu spät.</li>
</ul>
{merksatz("Die eine Rechnung, die Sie selbst machen sollten",
 "Wie viele Labore in Ihrem Einzugsgebiet haben in den letzten drei Jahren aufgegeben? Die Handwerksrolle Ihrer Kammer und die Innung wissen das. Diese Zahl sagt Ihnen mehr über Ihre Marktlage als jede Bundesstatistik.")}
{checkliste([
 "Ich weiß, wie viele Labore in meinem Einzugsgebiet in den letzten drei Jahren aufgegeben haben.",
 "Ich weiß, wie viele Zahnarztpraxen es in meinem Einzugsgebiet gibt.",
 "Ich weiß, mit wie vielen davon ich heute arbeite.",
 "Ich kenne die Differenz aus den beiden vorigen Zahlen. Das ist mein Markt.",
], "zahlen")}
</section>

<section id="unbelegt">
<h2>Was wir nicht belegen können</h2>
<p>Zu mehreren Größen kursieren Zahlen, für die wir keine belastbare Primärquelle geprüft haben. Wir nennen sie deshalb nicht als Fakt:</p>
<ul>
<li>Die Anzahl der Praxislabore in Deutschland.</li>
<li>Der Gesamtumsatz des Zahntechnikerhandwerks und die Verteilung nach Betriebsgrößen.</li>
<li>Die Zahl der Beschäftigten im Zahntechnikerhandwerk.</li>
<li>Durchschnittliche Wechselquoten von Zahnarztpraxen zwischen Laboren.</li>
</ul>
<p>Wer diese Zahlen sucht, findet Basisdaten und Umfrageergebnisse beim <a href="https://www.vdzi.de/Basisdaten-und-Umfrageergebnisse" rel="nofollow noopener" target="_blank">Verband Deutscher Zahntechniker-Innungen</a> sowie bei der <a href="https://www.zdh-statistik.de/application/index.php" rel="nofollow noopener" target="_blank">Statistik des ZDH</a>.</p>
</section>
''',
 "faq": [
  ("Wie viele Dentallabore gibt es in Deutschland?",
   "Zum Ende des ersten Halbjahres 2025 waren es 6.845 zahntechnische Betriebe. Für 2024 werden 6.994 gewerbliche Dentallabore genannt. Quelle ist die Statistik des Zentralverbands des Deutschen Handwerks, ausgewertet von Rebmann Research. Praxislabore in Zahnarztpraxen sind in diesen Zahlen nicht enthalten."),
  ("Wird die Zahl der Dentallabore weiter sinken?",
   "Eine Prognose geben wir nicht ab. Belegt ist die bisherige Richtung: von 2023 auf 2024 ein Rückgang um 3,4 Prozent, im ersten Halbjahr 2025 standen 105 Neugründungen 254 Betriebsaufgaben gegenüber."),
  ("Bedeutet weniger Labore automatisch mehr Arbeit für die übrigen?",
   "Nicht automatisch. Die Arbeit der aufgegebenen Labore verteilt sich auf die verbleibenden Labore, auf Praxislabore und auf Fertigung im Ausland. Welcher Anteil wohin geht, ist uns nicht belegt bekannt. Sicher ist nur, dass die Praxen dieser Labore neu entscheiden."),
 ],
 "nachspann": weiterlesen([
  ("/wissen/kundenakquise-im-dentallabor/","Kundenakquise im Dentallabor",
   "Wie Sie die suchenden Praxen tatsächlich erreichen."),
  ("/wissen/dentallabor-kaufen-oder-uebernehmen/","Dentallabor kaufen oder übernehmen",
   "Was der Rückgang für Käufer und Nachfolger bedeutet."),
  ("/wissen/dentallabor-gruenden/","Ein Dentallabor gründen",
   "Voraussetzungen, Pflichten und die ersten Praxen."),
  ("/wissen/eigenlabor-und-praxislabor/","Eigenlabor und Praxislabor verstehen",
   "Wohin ein Teil der Arbeit wandert und wo Sie gewinnen."),
 ]),
}
