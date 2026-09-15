# -*- coding: utf-8 -*-
"""Dentallabor gruenden. Zielsuchen (Google-Vorschlag belegt): dentallabor
gruenden kosten, dentallabor voraussetzungen, dentallabor eroeffnen,
dentallabor gewerbe, zahntechniker selbststaendig ohne meisterbrief."""
from wissen_bauen import (kennzahlen, figur, merksatz, mitnehmen, weiterlesen,
                          schritte, checkliste, tabelle, abschluss)

FIG_WEG = '''<svg viewBox="0 0 640 230" role="img" aria-labelledby="t-weg">
<title id="t-weg">Zwei Wege in die Selbstständigkeit: über die Meisterprüfung oder über eine Ausnahmebewilligung nach § 8 der Handwerksordnung.</title>
<defs><marker id="pf-gr" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">
<path d="M0 0 L9 4.5 L0 9 z" fill="#8A93A3"/></marker></defs>
<g font-size="13.5" fill="#061421">
<rect x="20" y="88" width="132" height="54" rx="12" fill="#0068C9" opacity=".12"/>
<text x="38" y="112">Zahntechniker,</text><text x="38" y="130">Geselle</text>
<rect x="228" y="24" width="180" height="54" rx="12" fill="#0068C9" opacity=".3"/>
<text x="248" y="48">Meisterprüfung</text><text x="248" y="66" font-size="12" fill="#4A5568">Regelweg</text>
<rect x="228" y="152" width="180" height="54" rx="12" fill="#0068C9" opacity=".18"/>
<text x="248" y="176">Ausnahmebewilligung</text><text x="248" y="194" font-size="12" fill="#4A5568">§ 8 HwO, Einzelfall</text>
<rect x="470" y="88" width="150" height="54" rx="12" fill="#0068C9"/>
<text x="488" y="112" fill="#ffffff">Eintragung in die</text><text x="488" y="130" fill="#ffffff">Handwerksrolle</text>
<path d="M152 106 L200 106 L200 51 L224 51" fill="none" stroke="#8A93A3" stroke-width="1.6" marker-end="url(#pf-gr)"/>
<path d="M152 124 L200 124 L200 179 L224 179" fill="none" stroke="#8A93A3" stroke-width="1.6" marker-end="url(#pf-gr)"/>
<path d="M408 51 L440 51 L440 106 L466 106" fill="none" stroke="#8A93A3" stroke-width="1.6" marker-end="url(#pf-gr)"/>
<path d="M408 179 L440 179 L440 118 L466 118" fill="none" stroke="#8A93A3" stroke-width="1.6" marker-end="url(#pf-gr)"/>
</g></svg>'''

VORLAGE_KAMMER = """Betreff: Eintragung Handwerksrolle, Zahntechnikerhandwerk

Guten Tag,

ich beabsichtige, im Zahntechnikerhandwerk ein eigenes Labor zu
eröffnen, Standort ... . Ich bitte um Auskunft zu folgenden Punkten:

1. Welche Nachweise benötigen Sie für die Eintragung in die
   Handwerksrolle in meinem Fall?
2. Welche Unterlagen und Fristen gelten bei Ihnen für einen Antrag
   auf Ausnahmebewilligung nach § 8 HwO im Zahntechnikerhandwerk?
3. Mit welchen Gebühren muss ich für Eintragung und Verfahren rechnen?
4. Welche Pflichtmitgliedschaften und Beiträge entstehen im ersten Jahr?

Meine Qualifikation: ... (Gesellenbrief vom ..., Berufsjahre ...,
Weiterbildungen ...).

Freundliche Grüße
..."""

SEITE = {
 "slug": "dentallabor-gruenden",
 "titel": "Dentallabor gründen: Voraussetzungen, Kosten, erste Praxen | Laboraquise.de",
 "beschreibung": "Was ein eigenes Dentallabor voraussetzt: Meisterpflicht nach Anlage A der Handwerksordnung, Ausnahmebewilligung, Medizinprodukterecht, 7 Prozent Umsatzsteuer und der Weg zu den ersten Zahnarztpraxen.",
 "krume": "Dentallabor gründen",
 "pille": "Wissen für Dentallabore",
 "h1": 'Ein <span class="text-color-primary">Dentallabor gründen</span>',
 "h1_klartext": "Dentallabor gründen: Voraussetzungen, Kosten und die ersten Praxen",
 "lead": "Meisterpflicht, Handwerksrolle, Medizinprodukterecht und Umsatzsteuer geordnet. Und die Frage, die in den meisten Gründungsratgebern fehlt: woher die ersten Zahnarztpraxen kommen.",
 "about": "Gründung eines zahntechnischen Labors",
 "toc": [("recht","Meisterpflicht und Handwerksrolle"),("ausnahme","Ohne Meisterbrief: § 8 HwO"),
         ("pflichten","Medizinprodukte und Steuern"),("kosten","Womit Sie rechnen müssen"),
         ("kunden","Die erste Praxis ist das eigentliche Problem"),
         ("plan","Ein Plan für die ersten sechs Monate"),("pruefung","Gründungs-Prüfliste"),
         ("ansprechen","Die ersten Praxen ansprechen"),("fragen","Häufige Fragen"),("weiterlesen","Weiterlesen")],
 "inhalt": f'''
<section id="recht">
{kennzahlen([
  ("Anlage A","Das Zahntechnikerhandwerk ist zulassungspflichtig, Nummer 37",
   'Quelle: <a href="https://www.gesetze-im-internet.de/hwo/anlage_a.html" rel="nofollow noopener" target="_blank">Anlage A HwO</a>'),
  ("§ 8 HwO","Einziger Weg ohne Meisterbrief, im Einzelfall",
   "Die Altgesellenregelung nach § 7b HwO gilt für Gesundheitshandwerke nicht."),
  ("7 %","Ermäßigter Umsatzsteuersatz für zahntechnische Leistungen",
   'Quelle: § 12 Abs. 2 Nr. 6 UStG'),
])}
<h2>Meisterpflicht und Eintragung in die Handwerksrolle</h2>
<p>Das Zahntechnikerhandwerk steht in Anlage A der Handwerksordnung, Nummer 37. Es ist damit zulassungspflichtig. Ein stehendes Gewerbe darf nur betreiben, wer in der Handwerksrolle eingetragen ist, und eingetragen wird in der Regel, wer die Meisterprüfung bestanden hat.</p>
<p>Gleichgestellt sind bestimmte Ingenieur-, Techniker- und vergleichbare Abschlüsse. Welcher Abschluss in Ihrem Fall anerkannt wird, entscheidet die zuständige Handwerkskammer, nicht der Ratgeber im Netz.</p>
{figur(FIG_WEG, "Zwei Wege führen in die Eintragung: die Meisterprüfung als Regelfall, die Ausnahmebewilligung nach § 8 HwO als Einzelfallentscheidung der Handwerkskammer.", 520)}
</section>

<section id="ausnahme">
<h2>Selbstständig ohne Meisterbrief: was wirklich gilt</h2>
<p>Für viele zulassungspflichtige Handwerke gibt es die Altgesellenregelung nach § 7b der Handwerksordnung: Wer als Geselle mehrere Jahre gearbeitet hat, darf sich unter Bedingungen selbstständig machen. <b>Für das Zahntechnikerhandwerk gilt diese Regelung nicht.</b> Gesundheitshandwerke sind davon ausgenommen.</p>
<p>Bleibt die Ausnahmebewilligung nach § 8 HwO. Sie wird im Einzelfall erteilt, wenn die notwendigen Kenntnisse und Fertigkeiten nachgewiesen sind und die Ablegung der Meisterprüfung eine unzumutbare Belastung darstellen würde. Das ist kein Formalakt und keine Alternative, mit der man planen sollte.</p>
{merksatz("Was das praktisch heißt",
 "Wer heute Geselle ist und ein eigenes Labor plant, plant zuerst die Meisterprüfung. Alles andere ist ein Antrag mit offenem Ausgang. Klären Sie die Frage schriftlich mit Ihrer Handwerkskammer, bevor Sie Geld in Räume oder Geräte stecken.")}
{mitnehmen("Anfrage an die Handwerkskammer zum Kopieren", VORLAGE_KAMMER)}
</section>

<section id="pflichten">
<h2>Medizinprodukterecht, Steuern, Pflichtmitgliedschaften</h2>
<p>Ein Dentallabor stellt Medizinprodukte her. Zahnersatz gilt als Sonderanfertigung. Daran hängen Pflichten zu Dokumentation, Konformitätserklärung und Rückverfolgbarkeit. Ihre Innung und die zuständige Behörde des Bundeslandes sagen Ihnen, welche Nachweise bei Ihnen konkret verlangt werden.</p>
<p>Steuerlich gilt für zahntechnische Leistungen und die Lieferung von Zahnersatz der ermäßigte Satz von 7 Prozent nach § 12 Abs. 2 Nr. 6 UStG. Das gilt unabhängig davon, ob Sie als Einzelunternehmen oder als GmbH arbeiten. Nicht jede Leistung eines Labors fällt darunter, deshalb gehört die Abgrenzung in die Hände Ihrer Steuerberatung.</p>
{tabelle(["Thema","Wer entscheidet","Was Sie vorher klären sollten"],[
 ["Eintragung Handwerksrolle","Handwerkskammer","Welche Nachweise gelten in Ihrem Fall, welche Gebühren fallen an."],
 ["Ausnahmebewilligung § 8 HwO","Handwerkskammer","Unterlagen, Fristen, Erfolgsaussicht im konkreten Fall."],
 ["Medizinprodukte, Sonderanfertigung","Zuständige Landesbehörde, Innung","Welche Dokumentation und welche Erklärungen verlangt werden."],
 ["Umsatzsteuer 7 Prozent","Finanzamt, Steuerberatung","Welche Ihrer Leistungen unter § 12 Abs. 2 Nr. 6 UStG fallen."],
 ["Innung, Kammerbeitrag","Kammer und Innung","Beitragshöhe im ersten Jahr, Pflicht und Freiwilligkeit."],
])}
<p class="text-size-small">Dieser Abschnitt ordnet die Zuständigkeiten. Er ist keine Rechts- oder Steuerberatung und ersetzt die Auskunft der genannten Stellen nicht.</p>
</section>

<section id="kosten">
<h2>Womit Sie rechnen müssen</h2>
<p>Belastbare Durchschnittskosten für eine Laborgründung liegen uns nicht vor, und geschätzte Zahlen wären hier wertlos. Was wir Ihnen geben können, ist die vollständige Liste der Posten, die in Angeboten regelmäßig vergessen werden:</p>
<ul>
<li><b>Räume:</b> Miete, Kaution, Umbau für Absaugung, Gips, Wasser, Starkstrom. Ein normales Büro ist kein Labor.</li>
<li><b>Geräte:</b> Neu, gebraucht oder geleast. Gebrauchte Geräte aus Laborauflösungen sind ein realer Markt.</li>
<li><b>Digitale Kette:</b> Scanner, Software, Fräse oder Fremdfertigung im Fräszentrum. Die Entscheidung dazu bestimmt Ihre laufenden Kosten.</li>
<li><b>Material und erster Warenbestand.</b></li>
<li><b>Versicherungen:</b> Betriebshaftpflicht, Inhaltsversicherung, Berufsgenossenschaft.</li>
<li><b>Laufende Kosten, bis Geld hereinkommt.</b> Zwischen der ersten Arbeit und der ersten Zahlung liegen Wochen.</li>
<li><b>Kundengewinnung.</b> Der Posten, der am häufigsten fehlt. Siehe nächster Abschnitt.</li>
</ul>
</section>

<section id="kunden">
<h2>Die erste Praxis ist das eigentliche Problem</h2>
<p>Technik, Räume und Genehmigungen lassen sich abarbeiten. Sie kosten Geld und Zeit, aber der Weg ist bekannt. Die Frage, an der Gründungen wirklich scheitern, lautet: Wer schickt Ihnen im dritten Monat Arbeit?</p>
<p>Viele Gründer starten mit Praxen, die sie aus dem alten Labor kennen. Das ist der schnellste Weg und zugleich der heikelste. Prüfen Sie vorher, welche Vereinbarungen aus Ihrem Arbeitsvertrag gelten, insbesondere ein nachvertragliches Wettbewerbsverbot. Ein Anwalt für Arbeitsrecht klärt das in einem Termin.</p>
{schritte([
 ("1","Zwei bis drei Praxen zusagen lassen, bevor der Mietvertrag unterschrieben wird. Mündlich reicht nicht, ein Probelauf schon."),
 ("2","Ein Einstiegsangebot festlegen: eine bestimmte Arbeit, fester Preis, feste Lieferzeit."),
 ("3","Ab dem ersten Monat laufend ansprechen, nicht erst, wenn die Auslastung fehlt."),
])}
<p style="margin-top:1.5rem">Ein neu gegründetes Labor hat gegenüber einem eingeführten Labor genau zwei Vorteile: freie Kapazität und einen Inhaber, der selbst ans Telefon geht. Beides sind gute Argumente. Nutzen Sie sie, solange sie stimmen.</p>
</section>

<section id="plan">
<h2>Ein Plan für die ersten sechs Monate</h2>
{tabelle(["Zeitraum","Was ansteht","Woran Sie merken, dass es läuft"],[
 ["Monat 1 bis 2","Kammer, Nachweise, Standort, Finanzierung klären. Wettbewerbsverbot anwaltlich prüfen.","Schriftliche Auskunft der Kammer liegt vor."],
 ["Monat 2 bis 3","Geräte und Räume festlegen. Parallel die ersten Praxen ansprechen.","Zwei Praxen haben einem Probelauf zugestimmt."],
 ["Monat 3 bis 4","Betrieb aufnehmen. Abläufe für Abholung, Rückfragen und Nacharbeit festlegen.","Die erste Arbeit ist termingerecht geliefert."],
 ["Monat 4 bis 6","Ansprache verstetigen. Jede gelieferte Arbeit nach Rückmeldung fragen.","Eine Praxis schickt regelmäßig, ohne dass Sie nachfassen."],
])}
</section>

<section id="pruefung">
<h2>Gründungs-Prüfliste</h2>
{checkliste([
 "Ich habe schriftlich von der Handwerkskammer, unter welchen Bedingungen ich eingetragen werde.",
 "Ein nachvertragliches Wettbewerbsverbot aus meinem Arbeitsvertrag ist anwaltlich geprüft.",
 "Die Pflichten aus dem Medizinprodukterecht für Sonderanfertigungen sind mir bekannt.",
 "Meine Steuerberatung hat die Umsatzsteuerfrage für meine Leistungen geklärt.",
 "Ich habe eine vollständige Kostenliste inklusive laufender Kosten für sechs Monate.",
 "Mindestens zwei Praxen haben einem Probelauf zugestimmt.",
 "Ich habe ein konkretes Einstiegsangebot mit Preis und Lieferzeit.",
 "Ich weiß, wie ich ab Monat eins laufend neue Praxen anspreche.",
], "gruendung")}
</section>
''',
 "faq": [
  ("Kann ich ohne Meisterbrief ein Dentallabor eröffnen?",
   "In aller Regel nicht. Das Zahntechnikerhandwerk steht in Anlage A der Handwerksordnung und ist zulassungspflichtig. Die Altgesellenregelung nach § 7b HwO, die in anderen Handwerken einen Weg ohne Meisterbrief eröffnet, gilt für Gesundheitshandwerke nicht. Bleibt die Ausnahmebewilligung nach § 8 HwO als Einzelfallentscheidung der Handwerkskammer."),
  ("Welche Umsatzsteuer gilt für ein Dentallabor?",
   "Für zahntechnische Leistungen und die Lieferung von Zahnersatz gilt der ermäßigte Satz von 7 Prozent nach § 12 Abs. 2 Nr. 6 UStG, unabhängig von der Rechtsform. Welche Ihrer Leistungen im Einzelnen darunter fallen, klärt Ihre Steuerberatung."),
  ("Darf ich Kunden aus meinem bisherigen Labor mitnehmen?",
   "Das hängt von Ihrem Arbeitsvertrag ab, insbesondere von einem nachvertraglichen Wettbewerbsverbot und seiner Wirksamkeit. Lassen Sie den Vertrag vor der Gründung von einer Fachanwältin oder einem Fachanwalt für Arbeitsrecht prüfen. Dieser Text ist keine Rechtsberatung."),
  ("Wie viele Praxen braucht ein neues Labor zum Start?",
   "Das hängt von Ihren Kosten und der Größe der Praxen ab. Rechnen Sie es mit Ihren eigenen Zahlen aus, statt mit einer Faustregel zu arbeiten. Der Bedarfsrechner auf unserer Seite zur Kundenakquise nimmt Ihre Werte auf."),
 ],
 "abschluss": abschluss(
   'Die ersten Praxen für Ihr neues Labor',
   'Räume, Geräte und Genehmigungen haben einen bekannten Weg. Die ersten Auftraggeber nicht. Wir richten Kampagnen auf das Gebiet und die Arbeiten aus, die Sie tatsächlich übernehmen können, und prüfen jede Anfrage gegen dieses Profil, bevor sie zu Ihnen kommt. Im Erstgespräch klären wir, ob das für Ihren Standort und Ihren Starttermin trägt. Einen Auftrag können wir Ihnen nicht zusagen, nur den Weg zum Gespräch.',
   [('01', 'Gebiet und Arbeiten festlegen'), ('02', 'Einstiegsangebot entwickeln'), ('03', 'Gespräche mit passenden Praxen')],
   'Kundengewinnung gehört in den Gründungsplan, nicht in den Notfallplan.'),
 "nachspann": weiterlesen([
  ("/wissen/kundenakquise-im-dentallabor/","Kundenakquise im Dentallabor",
   "Sieben Wege zu neuen Praxen, mit Rechner und Gesprächsvorlage."),
  ("/wissen/preise-und-stundensatz-im-dentallabor/","Preise und Stundensatz im Dentallabor",
   "Was Ihre Stunde kosten muss, damit am Ende etwas übrig bleibt."),
  ("/wissen/dentallabor-kaufen-oder-uebernehmen/","Dentallabor kaufen oder übernehmen",
   "Die Alternative zur Gründung und was dabei wirklich den Preis bestimmt."),
  ("/wissen/zahntechnik-in-zahlen/","Zahntechnik in Zahlen",
   "Wie viele Labore es gibt und wie viele jedes Jahr aufgeben."),
 ]),
}
