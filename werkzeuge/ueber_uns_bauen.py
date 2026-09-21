#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut /ueber-uns/ aus derselben Schablone wie die Wissensseiten.

Warum es diese Seite gibt: Bisher steht das Unternehmen nur in einem
Ankerabschnitt der Startseite, unter /#about. Ein Anker ist keine Adresse.
Weder eine Suchmaschine noch eine Antwortmaschine kann darauf verweisen,
wenn jemand fragt, wer hinter Laboraquise.de steht. Genau diese Frage
stellen Laborinhaber vor einem Erstgespraech, und genau diese Frage
beantworten Antwortmaschinen aus dem, was sie an einer eigenen Adresse
finden.

Alle Angaben stammen aus dem Impressum, den AGB und der Startseite.
Zahlen, die nicht von dort stammen, sind im Text als das gekennzeichnet,
was sie sind, und der Bereich, aus dem sie kommen, wird genannt.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from wissen_bauen import (schreibe, tabelle, merksatz, schritte,  # noqa: E402
                          checkliste, abschluss, weiterlesen)

FIG_WEG = '''<svg viewBox="0 0 640 210" role="img" aria-labelledby="t-weg">
<title id="t-weg">Zwei Angebote für dieselbe Zielgruppe: Hansetalent besetzt Stellen im Dentallabor, Laboraquise.de gewinnt Zahnarztpraxen als Kunden. Beide gehören Ben Carstens.</title>
<g font-size="13.5">
<rect x="24" y="30" width="270" height="76" rx="16" fill="#EAF2FB"/>
<text x="46" y="60" fill="#061421" font-size="15">Hansetalent, seit 2022</text>
<text x="46" y="82" fill="#4A5568">Fachkräfte für Dentallabore</text>
<rect x="346" y="30" width="270" height="76" rx="16" fill="#0068C9"/>
<text x="368" y="60" fill="#FFFFFF" font-size="15">Laboraquise.de, seit 2026</text>
<text x="368" y="82" fill="#D6E7F8">Zahnarztpraxen für Dentallabore</text>
<path d="M300 68 H340" stroke="#C2CAD4" stroke-width="2" stroke-linecap="round"/>
<path d="M334 62 L342 68 L334 74" fill="none" stroke="#C2CAD4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<text x="24" y="150" fill="#061421" font-size="15">Dieselbe Branche, dieselbe Person, zwei Engpässe</text>
<text x="24" y="176" fill="#4A5568" font-size="12.5">Ein Labor, das keine Fachkräfte findet, kann nicht wachsen. Ein Labor, das keine neuen Praxen</text>
<text x="24" y="196" fill="#4A5568" font-size="12.5">gewinnt, hängt an denen, die es hat. Beides sind Engpässe, beide entstehen aus demselben Markt.</text>
</g></svg>'''

SEITE = {
    "slug": "ueber-uns",
    "pfad": "/ueber-uns/",
    "krume_html": '<a href="/">Startseite</a><span>/</span><span>Über uns</span>',
    "titel": "Über Laboraquise.de: wer dahintersteht | Laboraquise.de",
    "beschreibung": (
        "Wer hinter Laboraquise.de steht, woher die Erfahrung im Dentalmarkt kommt, "
        "was zugesagt wird und was nicht. Anbieter ist Hansetalent, Inhaber Ben Carstens, Hamburg."),
    "krume": "Über uns",
    "pille": "Über uns",
    "h1": 'Wer hinter <span class="text-color-primary">Laboraquise.de</span> steht',
    "h1_klartext": "Über Laboraquise.de",
    "lead": ("Ein Einzelunternehmen aus Hamburg, das ausschließlich mit Dentallaboren "
             "arbeitet. Hier steht, woher die Erfahrung kommt, wie gearbeitet wird und "
             "wo die Grenzen dessen liegen, was zugesagt wird."),
    "about": "Laboraquise.de",
    "toc": [("wer", "Wer arbeitet hier"), ("herkunft", "Woher die Erfahrung kommt"),
            ("arbeitsweise", "Wie gearbeitet wird"),
            ("grenzen", "Was zugesagt wird und was nicht"),
            ("daten", "Angaben zum Unternehmen"),
            ("ansprechen", "Erstgespräch"), ("weiterlesen", "Weiterlesen")],
    "inhalt": f'''
<section id="wer">
<h2>Wer arbeitet hier</h2>
<p>Laboraquise.de ist eine Geschäftsbezeichnung von Hansetalent, einem Einzelunternehmen mit Sitz in Hamburg. Inhaber ist Ben Carstens. Es gibt keine Agenturstruktur dahinter, keine Kundenbetreuung in zweiter Reihe und keine wechselnden Ansprechpartner. Wer das Erstgespräch führt, führt auch die Zusammenarbeit.</p>
<p>Das ist kein Werbeargument, sondern eine Einschränkung, die Sie kennen sollten: Die Anzahl der Labore, die gleichzeitig betreut werden können, ist dadurch begrenzt. Wir arbeiten außerdem nicht für zwei Labore, die sich im selben Einzugsgebiet um dieselben Praxen bewerben.</p>
{merksatz("Warum das für Sie zählt",
 "Ihr Kundenprofil, Ihre Preise und Ihre Fertigungsschwerpunkte sind Betriebswissen. Es bleibt bei der Person, der Sie es erzählt haben.")}
</section>

<section id="herkunft">
<h2>Woher die Erfahrung kommt</h2>
<p>Seit 2022 arbeitet Ben Carstens ausschließlich im Dentalmarkt, zunächst mit der Besetzung von Stellen in Dentallaboren unter der Marke Hansetalent. Dabei entsteht dieselbe Frage in jedem zweiten Gespräch: Woher kommen eigentlich die Aufträge, die die neuen Leute auslasten sollen. Aus dieser Frage ist 2026 Laboraquise.de entstanden.</p>
<figure class="fig"><div class="fig__rahmen" style="--fig-min:340px">{FIG_WEG}</div><figcaption>Zwei Engpässe im selben Markt. Die Personalseite bearbeitet Hansetalent seit 2022, die Kundenseite Laboraquise.de seit 2026.</figcaption></figure>
<p>Was daraus folgt, ist Kenntnis des Marktes, nicht ein Erfahrungswert für die Kundengewinnung. Laboraquise.de ist 2026 gestartet. Wer Ihnen an dieser Stelle jahrzehntelange Erfolge in der Praxisakquise verspricht, verwechselt Marktkenntnis mit Ergebnisnachweis.</p>
</section>

<section id="arbeitsweise">
<h2>Wie gearbeitet wird</h2>
{schritte([
 ("1", "Kundenprofil: welche Praxen passen zu Ihrer Fertigung, Ihren Preisen und Ihrem Einzugsgebiet. Schriftlich, vor dem Start."),
 ("2", "Angebot schärfen: was Ihr Labor besser kann als das, mit dem die Praxis gerade arbeitet."),
 ("3", "Kampagne im vereinbarten Gebiet. Das Werbebudget zahlen Sie direkt an die Plattform, nicht an uns."),
 ("4", "Vorqualifizierung: eingehende Anfragen werden anhand des Kundenprofils geprüft, bevor sie zu Ihnen gehen."),
 ("5", "Das Gespräch mit der Praxis führen Sie. Preise, Bedarf und Zusammenarbeit klären Sie selbst."),
])}
<p>Was Sie einbringen müssen: die Angaben zu Ihrem Labor, die Freigabe der Kampagneninhalte und eine zeitnahe Reaktion auf Anfragen. Eine Praxis, die drei Tage auf einen Rückruf wartet, ist keine Anfrage mehr.</p>
</section>

<section id="grenzen">
<h2>Was zugesagt wird und was nicht</h2>
<p>Dieser Abschnitt steht hier, weil er in Verkaufsgesprächen oft fehlt. Maßgeblich ist immer das konkrete Angebot, nicht diese Seite.</p>
{tabelle(["Frage", "Antwort"], [
 ["Wird eine Anzahl Anfragen zugesagt?",
  "Nur wenn sie im Angebot steht. Dann bezieht sie sich auf qualifizierte Praxisanfragen im vereinbarten Zeitraum und Gebiet."],
 ["Was heißt qualifiziert?",
  "Die Anfrage erfüllt die vor dem Start schriftlich festgelegten Muss-Kriterien und stammt aus dem von Ihnen gewählten Einzugsgebiet."],
 ["Werden neue Kunden zugesagt?",
  "Nein. Ob aus einer Anfrage eine Zusammenarbeit wird, entscheidet sich in Ihrem Gespräch."],
 ["Wird Umsatz zugesagt?",
  "Nein. Weder Höhe noch Zeitpunkt."],
 ["Ist das Werbebudget in einer Erstattung enthalten?",
  "Nein. Erstattet werden kann nur die Dienstleistungsgebühr, nicht das an die Plattform gezahlte Budget."],
 ["Wie schnell kommen die ersten Anfragen?",
  "Dafür gibt es keine Zusage. Gebiet, Angebot und Kampagne bestimmen das mit."],
])}
{merksatz("Der Satz, an dem Sie jeden Anbieter messen können",
 "Fragen Sie nach der schriftlichen Definition einer qualifizierten Anfrage. Wer sie nicht vor dem Start liefert, kann sie nachher beliebig auslegen.")}
</section>

<section id="daten">
<h2>Angaben zum Unternehmen</h2>
{tabelle(["", ""], [
 ["Anbieter", "Hansetalent, Inhaber Ben Carstens, Einzelunternehmen"],
 ["Geschäftsbezeichnung", "Laboraquise.de"],
 ["Anschrift", "Eppendorfer Weg 168, 20253 Hamburg, Deutschland"],
 ["Vertreten durch", "Ben Carstens"],
 ["E-Mail", '<a href="mailto:info@laboraquise.de">info@laboraquise.de</a>'],
 ["Tätig seit", "2022 im Dentalmarkt (Personalgewinnung), seit 2026 mit Laboraquise.de"],
 ["Markt", "Deutschland"],
 ["Rechtliches", '<a href="/impressum/">Impressum</a>, <a href="/datenschutz/">Datenschutzerklärung</a>, <a href="/agb/">AGB</a>'],
])}
<p>Prüfliste, wenn Sie einen Anbieter für die Praxisakquise vergleichen. Die Punkte gelten für uns genauso wie für jeden anderen.</p>
{checkliste([
 "Liegt eine schriftliche Definition der qualifizierten Anfrage vor dem Start vor?",
 "Ist das Einzugsgebiet benannt und begrenzt?",
 "Steht getrennt, was Dienstleistungsgebühr und was Werbebudget ist?",
 "Ist geregelt, wem die Kampagnendaten und das Werbekonto gehören?",
 "Gibt es eine Regelung, ob im selben Gebiet für Wettbewerber gearbeitet wird?",
 "Sind Laufzeit, Verlängerung und Kündigung eindeutig?",
], "anbieter-vergleich")}
</section>
''',
    "abschluss": abschluss(
        "Erstgespräch",
        "Dreißig Minuten, kostenlos und unverbindlich. Wir sehen uns Ihr Einzugsgebiet an, klären, welche Praxen überhaupt in Frage kommen, und Sie bekommen eine Einschätzung, ob sich der Aufwand für Ihr Labor lohnt. Wenn nicht, sagen wir das im Gespräch.",
        [("1", "Termin aussuchen"), ("2", "Situation und Einzugsgebiet besprechen"),
         ("3", "Einschätzung, ob es für Ihr Labor trägt")],
        "Nach dem Erstgespräch entscheiden Sie. Ein Angebot kommt nur, wenn es passt."),
    "nachspann": weiterlesen([
        ("/wissen/kundenakquise-im-dentallabor/", "Kundenakquise im Dentallabor",
         "Sieben Wege zu neuen Praxen im Vergleich, auch die ohne uns."),
        ("/wissen/", "Alle Arbeitshilfen",
         "Rechner, Prüflisten und Textvorlagen für das Laborgeschäft."),
        ("/agb/", "Allgemeine Geschäftsbedingungen",
         "Kontingente, Zählkriterien, Laufzeit und Kündigung im Wortlaut."),
    ]),
}

if __name__ == "__main__":
    ziel = schreibe(SEITE)
    print(f"{ziel.relative_to(ziel.parents[1])}  {ziel.stat().st_size / 1024:.0f} KB")
