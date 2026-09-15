# -*- coding: utf-8 -*-
"""Eigenlabor und Praxislabor. Zielsuchen (Google-Vorschlag belegt): eigenlabor
zahnarzt, eigenlabor zahnarzt abrechnung, zahnarzt eigenlabor fremdlabor,
praxislabor zahnarzt, praxislabor zahntechniker."""
from wissen_bauen import (kennzahlen, figur, merksatz, mitnehmen, weiterlesen,
                          schritte, checkliste, tabelle, abschluss)

FIG_WAAGE = '''<svg viewBox="0 0 640 280" role="img" aria-labelledby="t-waage">
<title id="t-waage">Gegenüberstellung: Was für ein Praxislabor spricht und was für das Fremdlabor.</title>
<g font-size="13.5">
<rect x="20" y="20" width="290" height="240" rx="16" fill="#0068C9" opacity=".09"/>
<rect x="330" y="20" width="290" height="240" rx="16" fill="#0068C9" opacity=".18"/>
<text x="44" y="52" fill="#061421" font-size="15">Praxislabor</text>
<text x="354" y="52" fill="#061421" font-size="15">Ihr Labor</text>
<g fill="#4A5568">
<text x="44" y="84">Kurze Wege im Haus</text>
<text x="44" y="110">Marge bleibt in der Praxis</text>
<text x="44" y="136">Termine selbst steuerbar</text>
<text x="44" y="170" fill="#8A93A3">Gebunden: Personal</text>
<text x="44" y="194" fill="#8A93A3">Gebunden: Geräte</text>
<text x="44" y="218" fill="#8A93A3">Begrenzt: Arbeitsumfang</text>
<text x="354" y="84">Volle Fertigungstiefe</text>
<text x="354" y="110">Kein Personalrisiko der Praxis</text>
<text x="354" y="136">Spitzen abfangen</text>
<text x="354" y="162">Aufwendige Arbeiten</text>
<text x="354" y="188">Vertretung bei Ausfall</text>
<text x="354" y="222" fill="#8A93A3">Gebunden: Abstimmung nötig</text>
</g></svg>'''

VORLAGE_EIGENLABOR = """Guten Tag Frau Dr. ...,

Sie fertigen einen Teil Ihrer Arbeiten selbst. Das ist für die
Standardfälle oft der schnellste Weg.

Ich frage deshalb nur nach dem, was daneben liegt:
- Arbeiten, für die im Praxislabor Technik oder Zeit fehlt
- Wochen, in denen Ihre Zahntechnikerin ausfällt oder Urlaub hat
- Aufwendige Fälle, die Sie ungern zwischenschieben

Für genau diese Fälle halte ich Kapazität frei. Liefertermin
... Arbeitstage, Rückfragen beantworte ich selbst.

Wollen wir das an einem Fall ausprobieren? Ich hole ab und bringe
zurück.

Freundliche Grüße
..."""

SEITE = {
 "slug": "eigenlabor-und-praxislabor",
 "titel": "Eigenlabor und Praxislabor: was das für Ihr Dentallabor bedeutet | Laboraquise.de",
 "beschreibung": "Warum Zahnarztpraxen eigene Labore aufbauen, wo die Grenzen eines Praxislabors liegen und mit welchen Argumenten ein gewerbliches Dentallabor daneben bestehen kann.",
 "krume": "Eigenlabor und Praxislabor",
 "pille": "Wissen für Dentallabore",
 "h1": 'Eigenlabor und <span class="text-color-primary">Praxislabor</span> verstehen',
 "h1_klartext": "Eigenlabor und Praxislabor: was das für gewerbliche Dentallabore bedeutet",
 "lead": "Praxen, die selbst fertigen, sind kein verlorener Kunde. Sie sind ein Kunde mit anderem Bedarf. Wo die Grenzen des Praxislabors liegen und wie Sie daneben Arbeit gewinnen.",
 "about": "Praxislabore und gewerbliche Dentallabore",
 "toc": [("warum","Warum Praxen selbst fertigen"),("grenzen","Wo ein Praxislabor an Grenzen stößt"),
         ("gegenueber","Gegenüberstellung"),("ansprache","Wie Sie eine Praxis mit Eigenlabor ansprechen"),
         ("signale","Woran Sie den richtigen Zeitpunkt erkennen"),("pruefung","Prüfliste"),
         ("ansprechen","Praxen mit Eigenlabor erreichen"),("fragen","Häufige Fragen"),("weiterlesen","Weiterlesen")],
 "inhalt": f'''
<section id="warum">
<h2>Warum Zahnarztpraxen eigene Labore aufbauen</h2>
<p>Ein Praxislabor ist für eine Praxis zuerst eine betriebswirtschaftliche Entscheidung. Drei Gründe hört man immer wieder:</p>
<ul>
<li><b>Wertschöpfung bleibt im Haus.</b> Die Marge auf zahntechnische Leistungen wandert nicht zum Lieferanten.</li>
<li><b>Kurze Wege.</b> Anprobe, Korrektur und Nacharbeit im selben Gebäude sparen Tage.</li>
<li><b>Unabhängigkeit.</b> Wer selbst fertigt, hängt nicht am Terminplan eines externen Labors.</li>
</ul>
<p>Diese Gründe sind ernst zu nehmen. Wer sie im Gespräch kleinredet, verliert die Praxis endgültig. Interessant wird es an der Stelle, an der das Praxislabor an seine Grenzen kommt, und diese Stelle gibt es in jeder Praxis.</p>
</section>

<section id="grenzen">
<h2>Wo ein Praxislabor an Grenzen stößt</h2>
{schritte([
 ("1","Fertigungstiefe. Ein Praxislabor deckt die häufigen Arbeiten ab. Aufwendige Prothetik, Kombitechnik oder Kieferorthopädie stehen oft nicht im Haus."),
 ("2","Ausfall. Eine Zahntechnikerin im Praxislabor ist eine Person. Urlaub, Krankheit und Kündigung legen die Fertigung still."),
 ("3","Spitzen. Wenn drei große Fälle gleichzeitig kommen, verschiebt sich alles. Ein externes Labor fängt genau das ab."),
])}
<p style="margin-top:1.5rem">Dazu kommen Investitionen. Jeder Schritt in der digitalen Kette, vom Scanner über Software bis zur Fräse, bindet Geld, das die Praxis nicht in Behandlungsstühle steckt. Für Standardarbeiten rechnet sich das. Für seltene Arbeiten selten.</p>
{figur(FIG_WAAGE, "Gegenüberstellung der Stärken. Ein Praxislabor und ein gewerbliches Labor schließen sich nicht aus. Die meisten Praxen mit Eigenlabor vergeben weiterhin Arbeiten nach außen.", 520)}
</section>

<section id="gegenueber">
<h2>Die Gegenüberstellung, die im Gespräch hilft</h2>
{tabelle(["Frage der Praxis","Praxislabor","Gewerbliches Labor"],[
 ["Wer trägt das Personalrisiko?","Die Praxis. Ausfall trifft direkt die Fertigung.","Das Labor. Vertretung ist dort organisiert."],
 ["Was passiert bei Auftragsspitzen?","Verschiebung oder Fremdvergabe","Zusätzliche Kapazität im Rahmen der Vereinbarung"],
 ["Wer investiert in neue Technik?","Die Praxis, aus eigenem Kapital","Das Labor, verteilt auf viele Praxen"],
 ["Wie breit ist das Arbeitsspektrum?","Auf die häufigen Arbeiten ausgerichtet","Volle Breite, je nach Labor"],
 ["Wie schnell ist eine Korrektur?","Sehr schnell, im Haus","Abhängig von Weg und Absprache"],
])}
<p>Die letzte Zeile ist der Punkt, an dem Sie als externes Labor liefern müssen. Nähe, feste Abholzeiten und ein Ansprechpartner, der ans Telefon geht, sind genau die Antwort auf den stärksten Vorteil des Praxislabors.</p>
</section>

<section id="ansprache">
<h2>Wie Sie eine Praxis mit Eigenlabor ansprechen</h2>
<p>Der Fehler ist, die Praxis vom Praxislabor abbringen zu wollen. Das gelingt nicht und wirkt übergriffig. Der Weg, der funktioniert, ist schmaler und ehrlicher: Sie bieten sich für das an, was das Praxislabor nicht abdeckt.</p>
{mitnehmen("Ansprache für Praxen mit Eigenlabor, zum Anpassen und Kopieren", VORLAGE_EIGENLABOR)}
{merksatz("Warum dieser Weg besser funktioniert",
 "Eine Praxis, die einmal eine Vertretungsarbeit bei Ihnen fertigen lässt, hat Sie erlebt. Wenn die eigene Zahntechnikerin kündigt, und das kommt vor, sind Sie der Erste, an den gedacht wird. Das ist kein Trick, sondern die einzige Reihenfolge, die funktioniert.")}
</section>

<section id="signale">
<h2>Woran Sie den richtigen Zeitpunkt erkennen</h2>
<ul>
<li>Die Praxis sucht offen eine Zahntechnikerin oder einen Zahntechniker.</li>
<li>Die Praxis wächst, ein zusätzlicher Behandler kommt dazu.</li>
<li>Die Praxisleitung wechselt, etwa bei einer Übergabe.</li>
<li>Die Praxis bietet neu eine Leistung an, die im eigenen Labor nicht gefertigt werden kann.</li>
</ul>
<p>Diese Anlässe sind öffentlich sichtbar, in Stellenanzeigen, auf der Praxiswebsite und in lokalen Meldungen. Wer sie systematisch beobachtet, spricht zum richtigen Zeitpunkt an statt auf Verdacht.</p>
</section>

<section id="pruefung">
<h2>Prüfliste für Ihr Labor</h2>
{checkliste([
 "Ich weiß, welche Praxen in meinem Gebiet ein eigenes Labor betreiben.",
 "Ich habe ein Angebot für Vertretungs- und Spitzenlast formuliert, nicht nur für Vollversorgung.",
 "Ich kann benennen, welche Arbeiten ich fertige, die ein Praxislabor typischerweise nicht abdeckt.",
 "Meine Abholung und Lieferung ist so geregelt, dass die Nähe des Praxislabors kein entscheidender Vorteil bleibt.",
 "Ich beobachte Stellenanzeigen von Praxen in meinem Gebiet.",
], "eigenlabor")}
</section>
''',
 "faq": [
  ("Ist ein Praxislabor ein Konkurrent für mein Dentallabor?",
   "Teilweise. Es übernimmt die häufigen Arbeiten und bindet damit Umsatz, der früher nach außen ging. Es ersetzt ein gewerbliches Labor aber selten vollständig, weil Fertigungstiefe, Vertretung bei Ausfall und Auftragsspitzen im Haus schwer abzudecken sind."),
  ("Lohnt es sich, Praxen mit Eigenlabor überhaupt anzusprechen?",
   "Ja, mit einem anderen Angebot. Nicht die Vollversorgung, sondern die Arbeiten außerhalb des eigenen Spektrums, Vertretung bei Ausfall und Spitzenlast. Wer so einsteigt, ist der naheliegende Ansprechpartner, wenn sich im Praxislabor etwas ändert."),
  ("Wie viele Praxen betreiben ein eigenes Labor?",
   "Eine belastbare aktuelle Zahl liegt uns nicht vor, deshalb nennen wir hier keine. Für Ihr Gebiet lässt sich das praktisch klären: Praxiswebsites und Stellenanzeigen geben darüber in der Regel Auskunft."),
 ],
 "abschluss": abschluss(
   'Auch Praxen mit Eigenlabor gezielt erreichen',
   'Vertretung, Spitzenlast und Arbeiten außerhalb des eigenen Spektrums sind ein eigenes Angebot. Wer damit ansprechen will, braucht ein Kundenprofil, das genau diesen Bedarf beschreibt. Wir legen das mit Ihnen fest, richten die Kampagne darauf aus und prüfen jede Anfrage dagegen. Ob Bedarf und Zusammenarbeit wirklich passen, klärt sich in Ihrem Gespräch mit der Praxis.',
   [('01', 'Angebot für Vertretung und Spitzen'), ('02', 'Passende Praxen ansprechen'), ('03', 'Am einzelnen Fall anfangen')],
   'Der Einstieg über einen Fall ist wahrscheinlicher als der Wechsel der ganzen Praxis.'),
 "nachspann": weiterlesen([
  ("/wissen/kundenakquise-im-dentallabor/","Kundenakquise im Dentallabor",
   "Die sieben Wege zu neuen Praxen im Vergleich."),
  ("/wissen/preise-und-stundensatz-im-dentallabor/","Preise und Stundensatz im Dentallabor",
   "Was Ihre Stunde kosten muss und wie Sie das begründen."),
  ("/wissen/warum-zahnaerzte-das-dentallabor-wechseln/","Warum Zahnärzte ihr Dentallabor wechseln",
   "Die Anlässe, an denen eine Praxis neu entscheidet."),
  ("/wissen/zahntechnik-in-zahlen/","Zahntechnik in Zahlen",
   "Betriebe, Gründungen und Aufgaben, mit Quelle."),
 ]),
}
