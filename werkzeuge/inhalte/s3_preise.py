# -*- coding: utf-8 -*-
"""Preise und Stundensatz. Zielsuchen (Google-Vorschlag belegt): dentallabor
preise, dentallabor preisliste, dentallabor kosten, stundensatz
zahntechnikermeister, zahntechnik stundenlohn, bel ii preisliste, beb."""
from wissen_bauen import (kennzahlen, figur, merksatz, mitnehmen, weiterlesen,
                          schritte, checkliste, tabelle)

FIG_STUNDE = '''<svg viewBox="0 0 640 250" role="img" aria-labelledby="t-stunde">
<title id="t-stunde">Von der Anwesenheitszeit bleibt nach Abzug von Urlaub, Krankheit, Rüstzeit und Verwaltung nur ein Teil als verrechenbare Stunde übrig.</title>
<g font-size="13.5">
<rect x="40" y="30" width="560" height="42" rx="8" fill="#0068C9" opacity=".14"/>
<text x="54" y="57" fill="#061421">Bezahlte Anwesenheit</text><text x="556" y="57" fill="#061421" text-anchor="end">100 %</text>
<rect x="40" y="86" width="452" height="42" rx="8" fill="#0068C9" opacity=".26"/>
<text x="54" y="113" fill="#061421">abzüglich Urlaub, Krankheit, Fortbildung</text><text x="478" y="113" fill="#061421" text-anchor="end">81 %</text>
<rect x="40" y="142" width="352" height="42" rx="8" fill="#0068C9" opacity=".45"/>
<text x="54" y="169" fill="#061421">abzüglich Rüsten, Reinigen, Warten</text><text x="378" y="169" fill="#061421" text-anchor="end">63 %</text>
<rect x="40" y="198" width="268" height="42" rx="8" fill="#0068C9"/>
<text x="54" y="225" fill="#ffffff">verrechenbare Stunden</text><text x="294" y="225" fill="#ffffff" text-anchor="end">48 %</text>
</g></svg>'''

VORLAGE_PREIS = """Guten Tag Frau Dr. ...,

zum 1. ... passen wir unsere Preise an. Betroffen sind die
Positionen ... . Die Anpassung beträgt im Mittel ... Prozent.

Der Grund ist kein allgemeiner Hinweis auf gestiegene Kosten,
sondern konkret: ... (Material, Energie, Tarif, Fremdleistung).
Die letzte Anpassung war am ... .

Was gleich bleibt:
- Ihre Lieferzeiten: ... Arbeitstage
- Ihr Ansprechpartner: ...
- Unsere Regelung bei Nacharbeit: ...

Die neue Preisliste liegt bei. Wenn Sie einzelne Positionen
durchsprechen möchten, rufe ich gern an. Nennen Sie mir einfach
zwei Zeitfenster.

Freundliche Grüße
..."""

SEITE = {
 "slug": "preise-und-stundensatz-im-dentallabor",
 "titel": "Preise und Stundensatz im Dentallabor: BEL II, BEB, Kalkulation | Laboraquise.de",
 "beschreibung": "Wie sich der Stundensatz eines Dentallabors berechnet, was BEL II und BEB unterscheidet und wie eine Preisanpassung gegenüber Zahnarztpraxen begründet wird. Mit Rechner und Textvorlage.",
 "krume": "Preise und Stundensatz",
 "pille": "Wissen für Dentallabore",
 "h1": 'Preise und <span class="text-color-primary">Stundensatz</span> im Dentallabor',
 "h1_klartext": "Preise und Stundensatz im Dentallabor: BEL II, BEB und die eigene Kalkulation",
 "lead": "Der Unterschied zwischen BEL II und BEB, die Rechnung hinter Ihrem Stundensatz und ein Weg, eine Preisanpassung so zu begründen, dass die Praxis sie akzeptiert.",
 "about": "Preiskalkulation in zahntechnischen Laboren",
 "toc": [("grundlagen","BEL II und BEB im Unterschied"),("rechnung","Die Rechnung hinter Ihrem Stundensatz"),
         ("rechner","Stundensatz-Rechner"),("verrechenbar","Die Stunde, die niemand zählt"),
         ("anpassung","Preise anpassen, ohne Kunden zu verlieren"),
         ("abhaengig","Wenn ein Kunde den Preis diktiert"),("pruefung","Prüfliste zur Kalkulation"),
         ("fragen","Häufige Fragen"),("weiterlesen","Weiterlesen")],
 "inhalt": f'''
<section id="grundlagen">
<h2>BEL II und BEB: was der Unterschied praktisch bedeutet</h2>
<p>Zwei Verzeichnisse bestimmen, wie zahntechnische Leistungen abgerechnet werden. Wer sie durcheinanderbringt, verschenkt Geld oder bekommt Rechnungen zurück.</p>
{tabelle(["","BEL II","BEB"],[
 ["Wofür","Leistungen im Rahmen der gesetzlichen Krankenversicherung","Privat abgerechnete Leistungen und Leistungen außerhalb des BEL"],
 ["Preise","Bundeseinheitliches Leistungsverzeichnis, Höchstpreise werden verhandelt","Frei kalkulierbar, das Verzeichnis liefert die Leistungsbeschreibung"],
 ["Spielraum","Kein eigener Preisspielraum nach oben","Ihre Kalkulation bestimmt den Preis"],
 ["Folge fürs Labor","Die Menge entscheidet über den Deckungsbeitrag","Hier entscheidet sich, ob Ihr Labor verdient"],
])}
{merksatz("Der Punkt, an dem viele Labore Geld verlieren",
 "Wer seine BEB-Positionen jahrelang unverändert lässt und gleichzeitig steigende Material- und Lohnkosten trägt, arbeitet sich langsam in die Verlustzone. Der Effekt fällt nicht auf, weil die Auslastung stimmt. Er fällt am Jahresende auf.")}
</section>

<section id="rechnung">
<h2>Die Rechnung hinter Ihrem Stundensatz</h2>
<p>Ein Stundensatz ist kein Verhandlungswert, sondern ein Rechenergebnis. Er entsteht aus drei Größen: den Kosten Ihres Labors, dem Gewinn, den Sie brauchen, und den Stunden, die Sie tatsächlich verrechnen können.</p>
{schritte([
 ("1","Alle Kosten eines Jahres zusammenzählen: Löhne inklusive Nebenkosten, Miete, Energie, Geräte, Material, Versicherungen, Fremdleistungen, Verwaltung."),
 ("2","Den Unternehmerlohn und den nötigen Gewinn addieren. Wer sich selbst nicht einrechnet, arbeitet für die Bank."),
 ("3","Durch die verrechenbaren Stunden teilen, nicht durch die Anwesenheitsstunden."),
])}
</section>

<section id="rechner">
<h2>Stundensatz-Rechner</h2>
<div class="rechner" data-rechner="stundensatz">
  <h3>Was Ihre Stunde kosten muss</h3>
  <p class="rechner__hinweis">Alle Werte setzen Sie selbst ein. Das Ergebnis ist Ihre eigene Rechnung, kein Branchenwert und keine Preisempfehlung.</p>
  <div class="rechner__feld">
    <label for="s-kosten">Jahreskosten des Labors insgesamt, ohne Unternehmerlohn</label>
    <input type="number" id="s-kosten" value="320000" min="0" step="5000" inputmode="numeric">
    <small>Löhne, Miete, Energie, Material, Geräte, Versicherungen, Fremdleistungen.</small>
  </div>
  <div class="rechner__feld">
    <label for="s-lohn">Unternehmerlohn und angestrebter Gewinn im Jahr</label>
    <input type="number" id="s-lohn" value="80000" min="0" step="5000" inputmode="numeric">
  </div>
  <div class="rechner__feld">
    <label for="s-koepfe">Produktive Personen im Labor</label>
    <input type="number" id="s-koepfe" value="5" min="1" max="99" step="1" inputmode="numeric">
    <small>Alle, die zahntechnisch arbeiten. Reine Verwaltung zählt hier nicht mit.</small>
  </div>
  <div class="rechner__feld">
    <label for="s-stunden">Bezahlte Anwesenheitsstunden je Person und Jahr</label>
    <input type="number" id="s-stunden" value="1720" min="1" step="20" inputmode="numeric">
    <small>Wochenstunden mal Wochen. Bei 40 Stunden und 43 Wochen sind das 1.720.</small>
  </div>
  <div class="rechner__feld">
    <label for="s-anteil">Anteil davon, der wirklich verrechenbar ist: <b><span id="s-anteil-wert">48</span> Prozent</b></label>
    <input type="range" id="s-anteil" value="48" min="20" max="90" step="1">
    <small>Rüsten, Reinigen, Rückfragen, Nacharbeit und Verwaltung gehen ab. Siehe nächster Abschnitt.</small>
  </div>
  <div class="rechner__ausgabe">
    <div class="rechner__zelle"><span>Verrechenbare Stunden im Jahr</span><output id="s-verrechenbar">4.128</output></div>
    <div class="rechner__zelle"><span>Nötiger Stundensatz</span><output id="s-satz">96,90 €</output></div>
  </div>
</div>
</section>

<section id="verrechenbar">
<h2>Die Stunde, die niemand zählt</h2>
<p>Der häufigste Kalkulationsfehler steckt nicht in den Kosten, sondern im Nenner. Wer die Jahreskosten durch die bezahlten Anwesenheitsstunden teilt, rechnet mit Stunden, die er nie in Rechnung stellt.</p>
{figur(FIG_STUNDE, "Schematische Darstellung des Wegs von der bezahlten Anwesenheit zur verrechenbaren Stunde. Die Prozentwerte sind ein Beispiel. Messen Sie Ihren eigenen Anteil, statt ihn zu schätzen.", 480)}
<p>Messen Sie den Anteil einmal über vier Wochen an einem einzelnen Arbeitsplatz. Das ist unbequem und bringt mehr als jede Preisverhandlung.</p>
</section>

<section id="anpassung">
<h2>Preise anpassen, ohne Kunden zu verlieren</h2>
<p>Preisanpassungen scheitern selten am Betrag und fast immer an der Begründung. „Gestiegene Kosten" ist keine Begründung, das hört die Praxis von jedem Lieferanten. Was funktioniert: konkret werden, früh informieren, und im selben Schreiben sagen, was gleich bleibt.</p>
{mitnehmen("Schreiben zur Preisanpassung, zum Anpassen und Kopieren", VORLAGE_PREIS)}
<p>Schicken Sie das Schreiben mindestens vier Wochen vorher und rufen Sie bei Ihren drei größten Praxen zusätzlich an. Ein Anruf vor der Rechnung ist billiger als ein Kunde nach der Rechnung.</p>
</section>

<section id="abhaengig">
<h2>Wenn ein Kunde den Preis diktiert</h2>
<p>Je größer der Anteil eines einzelnen Auftraggebers an Ihrem Umsatz, desto schwächer Ihre Position bei Preis, Termin und Nacharbeit. Das ist keine Frage der Sympathie, sondern der Rechnung: Wer bei einem Nein vierzig Prozent seines Umsatzes verliert, sagt nicht Nein.</p>
<p>Der Ausweg ist unbequem und dauert. Zusätzliche passende Praxen senken den Anteil des größten Kunden. Danach lassen sich Preisgespräche anders führen, ohne dass jemand droht.</p>
{merksatz("Eine Zahl, die Sie kennen sollten",
 "Rechnen Sie aus, welchen Anteil Ihr größter Auftraggeber am Jahresumsatz hat. Liegt er über einem Drittel, ist Ihre Preisgestaltung faktisch fremdbestimmt.")}
</section>

<section id="pruefung">
<h2>Prüfliste zur Kalkulation</h2>
{checkliste([
 "Meine Jahreskosten sind vollständig erfasst, einschließlich Fremdleistungen und Verwaltung.",
 "Unternehmerlohn und Gewinn sind in der Kalkulation enthalten.",
 "Ich kenne meinen tatsächlichen Anteil verrechenbarer Stunden, gemessen statt geschätzt.",
 "Meine BEB-Positionen wurden in den letzten zwölf Monaten überprüft.",
 "Ich weiß, welche Arbeiten bei mir Deckungsbeitrag bringen und welche nicht.",
 "Ich kenne den Umsatzanteil meines größten Auftraggebers.",
 "Meine letzte Preisanpassung ist weniger als achtzehn Monate her oder bewusst aufgeschoben.",
], "kalkulation")}
</section>
''',
 "faq": [
  ("Was ist der Unterschied zwischen BEL II und BEB?",
   "BEL II ist das bundeseinheitliche Leistungsverzeichnis für zahntechnische Leistungen im Rahmen der gesetzlichen Krankenversicherung, mit verhandelten Höchstpreisen. BEB beschreibt Leistungen für die private Abrechnung, die Preise kalkuliert das Labor selbst. Der eigene Preisspielraum liegt praktisch vollständig im BEB-Bereich."),
  ("Wie berechnet man den Stundensatz im Dentallabor?",
   "Jahreskosten plus Unternehmerlohn und Gewinn, geteilt durch die tatsächlich verrechenbaren Stunden aller produktiven Personen. Entscheidend ist der Nenner: Wer mit Anwesenheitsstunden statt mit verrechenbaren Stunden rechnet, setzt den Stundensatz systematisch zu niedrig an."),
  ("Wie oft sollte ein Labor seine Preise anpassen?",
   "Es gibt keine allgemeingültige Frist. Sinnvoll ist eine jährliche Überprüfung der Kalkulation, auch wenn daraus keine Anpassung folgt. Wer mehrere Jahre nicht anpasst, muss später in einem Schritt so viel nachholen, dass die Praxis es als Preissprung erlebt."),
  ("Wie begründe ich eine Preiserhöhung gegenüber der Praxis?",
   "Konkret statt allgemein: Nennen Sie die betroffenen Positionen, den Zeitpunkt der letzten Anpassung und den tatsächlichen Kostentreiber. Sagen Sie im selben Schreiben, was unverändert bleibt, also Lieferzeiten, Ansprechpartner und Ihre Regelung bei Nacharbeit. Eine Vorlage dafür steht oben auf dieser Seite."),
 ],
 "nachspann": weiterlesen([
  ("/wissen/kundenakquise-im-dentallabor/","Kundenakquise im Dentallabor",
   "Wie Sie die Abhängigkeit von einem großen Auftraggeber verringern."),
  ("/wissen/eigenlabor-und-praxislabor/","Eigenlabor und Praxislabor verstehen",
   "Warum Praxen selbst fertigen und wo Ihr Preis dagegen besteht."),
  ("/wissen/dentallabor-gruenden/","Ein Dentallabor gründen",
   "Voraussetzungen, Pflichten und die ersten Praxen."),
  ("/wissen/warum-zahnaerzte-das-dentallabor-wechseln/","Warum Zahnärzte ihr Dentallabor wechseln",
   "Die Anlässe hinter einem Wechsel, jenseits des Preises."),
 ]),
}
