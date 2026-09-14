# -*- coding: utf-8 -*-
"""Dentallabor kaufen oder uebernehmen. Zielsuchen (Google-Vorschlag belegt):
dentallabor kaufen (+ NRW, Bayern, Niedersachsen, Hessen, Berlin, Stuttgart,
Hamburg, Muenchen), dentallabor verkaufen preis, dentallabor nachfolge,
dentallabor uebernahme, zahntechnisches labor zu verkaufen."""
from wissen_bauen import (kennzahlen, figur, merksatz, mitnehmen, weiterlesen,
                          schritte, checkliste, tabelle)

FIG_UEBERGABE = '''<svg viewBox="0 0 640 240" role="img" aria-labelledby="t-uebergabe">
<title id="t-uebergabe">Nach einer Übernahme entscheidet jede Praxis neu, ob sie bleibt. Ein Teil des Kundenstamms geht erfahrungsgemäß verloren.</title>
<g font-size="13.5">
<text x="40" y="36" fill="#061421" font-size="15">Kundenstamm beim Kauf</text>
<g fill="#0068C9">
<rect x="40" y="52" width="34" height="34" rx="8"/><rect x="84" y="52" width="34" height="34" rx="8"/>
<rect x="128" y="52" width="34" height="34" rx="8"/><rect x="172" y="52" width="34" height="34" rx="8"/>
<rect x="216" y="52" width="34" height="34" rx="8"/><rect x="260" y="52" width="34" height="34" rx="8"/>
<rect x="304" y="52" width="34" height="34" rx="8"/><rect x="348" y="52" width="34" height="34" rx="8"/>
<rect x="392" y="52" width="34" height="34" rx="8"/><rect x="436" y="52" width="34" height="34" rx="8"/>
<rect x="480" y="52" width="34" height="34" rx="8"/><rect x="524" y="52" width="34" height="34" rx="8"/>
</g>
<text x="40" y="146" fill="#061421" font-size="15">Ein Jahr nach der Übergabe</text>
<g fill="#0068C9">
<rect x="40" y="162" width="34" height="34" rx="8"/><rect x="84" y="162" width="34" height="34" rx="8"/>
<rect x="128" y="162" width="34" height="34" rx="8"/><rect x="172" y="162" width="34" height="34" rx="8"/>
<rect x="216" y="162" width="34" height="34" rx="8"/><rect x="260" y="162" width="34" height="34" rx="8"/>
<rect x="304" y="162" width="34" height="34" rx="8"/><rect x="348" y="162" width="34" height="34" rx="8"/>
</g>
<g fill="none" stroke="#C2CAD4" stroke-width="1.6" stroke-dasharray="4 4">
<rect x="392" y="162" width="34" height="34" rx="8"/><rect x="436" y="162" width="34" height="34" rx="8"/>
<rect x="480" y="162" width="34" height="34" rx="8"/><rect x="524" y="162" width="34" height="34" rx="8"/>
</g>
<text x="40" y="224" fill="#4A5568" font-size="12.5">Gestrichelt: Praxen, die nach der Übergabe neu entscheiden. Die Anzahl ist ein Beispiel, kein Erfahrungswert.</text>
</g></svg>'''

VORLAGE_UEBERGABE = """Guten Tag Frau Dr. ...,

zum ... habe ich das Labor ... von Herrn/Frau ... übernommen.
Ich melde mich, bevor Sie es von jemand anderem hören.

Was sich für Sie ändert: nichts an den Personen, die Ihre Arbeiten
fertigen. ... arbeitet weiter im Haus. Ihre Lieferzeiten bleiben bei
... Arbeitstagen, Ihre Preise bleiben bis ... unverändert.

Was sich ändert: Ihr Ansprechpartner bin jetzt ich, erreichbar unter
... , werktags bis ... Uhr.

Ich würde in den nächsten zwei Wochen gern für zwanzig Minuten
vorbeikommen und mir anhören, was in der Zusammenarbeit bisher gut
lief und was nicht. Nennen Sie mir zwei Zeitfenster, ich richte
mich danach.

Freundliche Grüße
..."""

SEITE = {
 "slug": "dentallabor-kaufen-oder-uebernehmen",
 "titel": "Dentallabor kaufen oder übernehmen: worauf es beim Preis ankommt | Laboraquise.de",
 "beschreibung": "Was beim Kauf eines Dentallabors wirklich bezahlt wird, warum der Kundenstamm das Risiko ist und wie Sie die Praxen nach der Übernahme halten. Mit Prüfliste und Anschreiben.",
 "krume": "Dentallabor kaufen",
 "pille": "Wissen für Dentallabore",
 "h1": 'Ein Dentallabor <span class="text-color-primary">kaufen oder übernehmen</span>',
 "h1_klartext": "Dentallabor kaufen oder übernehmen: Preis, Kundenstamm und die ersten Monate",
 "lead": "Geräte lassen sich bewerten. Der Kundenstamm nicht, denn er kann gehen. Was den Preis bestimmt, welche Unterlagen Sie sehen müssen und wie Sie die Praxen nach der Übergabe halten.",
 "about": "Übernahme zahntechnischer Labore",
 "toc": [("lage","Der Markt für Übernahmen"),("wert","Was Sie tatsächlich kaufen"),
         ("pruefen","Unterlagen, die Sie sehen müssen"),("risiko","Das Risiko heißt Kundenstamm"),
         ("uebergabe","Die ersten hundert Tage"),("pruefung","Prüfliste zur Übernahme"),
         ("fragen","Häufige Fragen"),("weiterlesen","Weiterlesen")],
 "inhalt": f'''
<section id="lage">
{kennzahlen([
  ("254","Betriebsaufgaben im ersten Halbjahr 2025",
   'Quelle: ZDH-Statistik, ausgewertet von <a href="https://www.rebmann-research.de/zahntechnik-betriebszahlen-ruecklaeufig" rel="nofollow noopener" target="_blank">Rebmann Research</a>'),
  ("105","Neugründungen im selben Zeitraum",
   "Quelle: ebenda. Auf eine Gründung kommen rund 2,4 Aufgaben."),
  ("6.845","Zahntechnikbetriebe, Stand erstes Halbjahr 2025",
   "Quelle: ebenda. 2024 waren es 6.994."),
])}
<h2>Der Markt für Übernahmen ist größer als der für Gründungen</h2>
<p>Auf jede Neugründung kamen im ersten Halbjahr 2025 rund zweieinhalb Betriebsaufgaben. Ein Teil dieser Labore wird nicht übergeben, sondern geschlossen, weil sich kein Nachfolger findet. Für Käufer heißt das: Es gibt Angebot, und der Zeitdruck liegt häufiger beim Verkäufer.</p>
<p>Daraus folgt kein Schnäppchen. Es folgt daraus, dass Sie gründlich prüfen dürfen, ohne den Kauf zu verlieren.</p>
</section>

<section id="wert">
<h2>Was Sie tatsächlich kaufen</h2>
{tabelle(["Bestandteil","Wie bewertbar","Worauf zu achten ist"],[
 ["Geräte und Einrichtung","Gut. Zeitwert, Gutachten, Vergleichsangebote.","Alter der digitalen Kette. Ein Scanner ohne Wartungsvertrag ist ein Posten, keine Investition."],
 ["Material und Warenbestand","Gut. Inventur.","Verfallsdaten, Ladenhüter, gebundenes Kapital."],
 ["Räume und Mietvertrag","Gut.","Restlaufzeit, Übertragbarkeit, Zustand der Installationen."],
 ["Mitarbeitende","Eingeschränkt.","Betriebsübergang nach § 613a BGB. Wer bleibt, wer geht, wer ist Leistungsträger."],
 ["Kundenstamm","Schlecht. Er ist das Wertvollste und das Flüchtigste.","Siehe unten. Hier entscheidet sich der Erfolg der Übernahme."],
])}
{merksatz("Die Frage, die den Preis bestimmt",
 "Nicht: Was ist im Labor vorhanden? Sondern: Wie viel Umsatz kommt in zwölf Monaten noch, wenn der bisherige Inhaber nicht mehr da ist? Alles andere ist Inventar.")}
</section>

<section id="pruefen">
<h2>Unterlagen, die Sie vor einem Angebot sehen müssen</h2>
<ul>
<li><b>Umsatz je Auftraggeber über drei Jahre.</b> Nicht nur die Summe. Die Verteilung entscheidet über Ihr Risiko.</li>
<li><b>Anteil des größten Kunden.</b> Liegt er über einem Drittel, kaufen Sie im Wesentlichen eine Geschäftsbeziehung.</li>
<li><b>Altersstruktur der Auftraggeber.</b> Praxisinhaber kurz vor der Abgabe sind kein dauerhafter Umsatz.</li>
<li><b>Deckungsbeitrag je Arbeitsart.</b> Ein ausgelastetes Labor mit falscher Arbeitsverteilung verdient nichts.</li>
<li><b>Nacharbeitsquote und Reklamationen.</b> Fragen Sie nach der Regelung, nicht nach dem Gefühl.</li>
<li><b>Verträge:</b> Miete, Leasing, Wartung, Fremdfertigung, Arbeitsverträge.</li>
<li><b>Dokumentation nach Medizinprodukterecht.</b> Lücken übernehmen Sie mit.</li>
</ul>
{figur(FIG_UEBERGABE, "Schematische Darstellung: Nach einer Übergabe entscheidet jede Praxis neu über die Zusammenarbeit. Wie viele bleiben, hängt vom Übergabeprozess ab, nicht vom Kaufvertrag.", 520)}
</section>

<section id="risiko">
<h2>Das Risiko heißt Kundenstamm</h2>
<p>Eine Zahnarztpraxis arbeitet nicht mit einem Labor, sie arbeitet mit Menschen in einem Labor. Wenn der Inhaber geht, der jahrelang ans Telefon ging, ist die Geschäftsbeziehung offen. Nicht beendet, aber offen. Genau in diesem Moment ist jede Praxis für Ihre Wettbewerber ansprechbar.</p>
<p>Drei Vereinbarungen verringern das Risiko, und sie gehören in den Kaufvertrag, nicht in ein Gespräch:</p>
{schritte([
 ("1","Übergangszeit: Der bisherige Inhaber bleibt für mehrere Monate ansprechbar und stellt Sie persönlich vor. Schriftlich, mit Umfang."),
 ("2","Kaufpreisanteil an den Bestand koppeln: Ein Teil wird nach zwölf Monaten fällig, abhängig vom gehaltenen Umsatz."),
 ("3","Wettbewerbsverbot für den Verkäufer, zeitlich und räumlich begrenzt und damit wirksam."),
])}
<p style="margin-top:1.5rem">Und der Punkt, den Käufer regelmäßig unterschätzen: Sie brauchen ab Tag eins eigene Akquise. Nicht als Notfallplan, sondern als festen Bestandteil. Wer den Verlust einiger Praxen einkalkuliert, aber nichts dagegen tut, hat den Verlust nur benannt.</p>
</section>

<section id="uebergabe">
<h2>Die ersten hundert Tage</h2>
<p>Was in den ersten Wochen passiert, entscheidet, wie viele Praxen bleiben. Die Reihenfolge ist wichtiger als der Inhalt.</p>
{tabelle(["Zeitpunkt","Was zu tun ist"],[
 ["Vor der Übergabe","Mit dem Verkäufer festlegen, wer welche Praxis informiert und in welcher Reihenfolge. Die drei größten Auftraggeber erfahren es persönlich, nicht per Brief."],
 ["Woche 1","Schriftliche Information an alle Auftraggeber. Was bleibt, steht vor dem, was sich ändert."],
 ["Woche 2 bis 6","Persönlicher Besuch bei jedem nennenswerten Auftraggeber. Zuhören, nicht verkaufen."],
 ["Woche 1 bis 12","Keine Preisanpassung, keine Umstellung von Abläufen, keine neuen Materialien ohne Absprache."],
 ["Ab Woche 4","Eigene Ansprache neuer Praxen beginnen. Der Ersatz für Abgänge wird jetzt aufgebaut, nicht wenn die Abgänge da sind."],
])}
{mitnehmen("Anschreiben zur Übernahme, zum Anpassen und Kopieren", VORLAGE_UEBERGABE)}
</section>

<section id="pruefung">
<h2>Prüfliste zur Übernahme</h2>
{checkliste([
 "Ich kenne den Umsatz je Auftraggeber über drei Jahre, nicht nur die Gesamtsumme.",
 "Ich kenne den Umsatzanteil des größten Kunden.",
 "Ich weiß, welche Mitarbeitenden bleiben und wer Leistungsträger ist.",
 "Alle laufenden Verträge liegen mir vor, einschließlich Leasing und Wartung.",
 "Die Dokumentation nach Medizinprodukterecht ist gesichtet.",
 "Eine Übergangszeit mit dem Verkäufer ist schriftlich vereinbart.",
 "Ein Teil des Kaufpreises ist an den gehaltenen Umsatz gekoppelt.",
 "Ein wirksames Wettbewerbsverbot für den Verkäufer steht im Vertrag.",
 "Ich habe einen Plan, wie ich ab Woche vier selbst neue Praxen anspreche.",
], "uebernahme")}
</section>
''',
 "faq": [
  ("Was ist ein Dentallabor wert?",
   "Eine pauschale Formel führt in die Irre. Geräte, Material und Räume haben einen Zeitwert. Der größere Teil des Preises entfällt in der Regel auf den Kundenstamm, und der ist nur so viel wert, wie er nach der Übergabe bleibt. Deshalb gehört ein an den gehaltenen Umsatz gekoppelter Kaufpreisanteil in die Verhandlung."),
  ("Übernehme ich die Mitarbeitenden mit?",
   "Bei einem Betriebsübergang gehen bestehende Arbeitsverhältnisse nach § 613a BGB grundsätzlich auf den Erwerber über. Was das in Ihrem Fall bedeutet, insbesondere bei Kauf einzelner Wirtschaftsgüter statt des Betriebs, klärt eine Fachanwältin oder ein Fachanwalt für Arbeitsrecht. Dieser Text ist keine Rechtsberatung."),
  ("Wie viele Praxen bleiben nach einer Übernahme?",
   "Dazu liegen uns keine belastbaren Zahlen vor, und eine erfundene Quote hilft Ihnen nicht. Sicher ist die Richtung: Jede Praxis entscheidet nach dem Inhaberwechsel neu. Wie viele bleiben, hängt davon ab, wie persönlich und wie früh informiert wird und ob die vertrauten Personen im Labor bleiben."),
  ("Lohnt sich ein Kauf gegenüber einer Gründung?",
   "Ein Kauf bringt Umsatz ab dem ersten Tag und spart den Aufbau. Er bringt zugleich Altlasten mit: Verträge, Geräte, Abläufe und eine Kundenstruktur, die Sie nicht gewählt haben. Eine Gründung ist langsamer und frei von Altlasten. Die Entscheidung hängt an Ihrer Finanzierung und daran, wie schnell Sie Umsatz brauchen."),
 ],
 "nachspann": weiterlesen([
  ("/wissen/kundenakquise-im-dentallabor/","Kundenakquise im Dentallabor",
   "Der Ersatz für Abgänge, bevor die Abgänge da sind."),
  ("/wissen/dentallabor-gruenden/","Ein Dentallabor gründen",
   "Die Alternative zum Kauf, mit allen Voraussetzungen."),
  ("/wissen/preise-und-stundensatz-im-dentallabor/","Preise und Stundensatz im Dentallabor",
   "Ob das übernommene Labor kostendeckend kalkuliert."),
  ("/wissen/zahntechnik-in-zahlen/","Zahntechnik in Zahlen",
   "Wie viele Labore aufgeben und was das für Käufer bedeutet."),
 ]),
}
