#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ergaenzt die Startseite um zwei Dinge, ohne bestehenden Text zu aendern:
1. FAQPage-Auszeichnung, wortgleich aus den sichtbaren Fragen und Antworten.
2. Einen Abschnitt, der die Wissensseiten verlinkt.
Das Skript ist wiederholbar: es entfernt seine eigene frueheren Einfuegungen."""
import html as H, json, pathlib, re, sys

WURZEL = pathlib.Path(__file__).resolve().parent.parent
HOST = "https://www.laboraquise.de"
MARKE_LD = "<!-- faq-ld -->"
MARKE_WISSEN_A, MARKE_WISSEN_E = "<!-- wissen-block -->", "<!-- /wissen-block -->"

KARTEN = [
 ("kundenakquise-im-dentallabor", "Kundenakquise im Dentallabor",
  "Sieben Wege zu neuen Praxen im Vergleich, mit Bedarfsrechner."),
 ("preise-und-stundensatz-im-dentallabor", "Preise und Stundensatz",
  "BEL II, BEB und die Rechnung hinter Ihrem Stundensatz."),
 ("zahntechnik-in-zahlen", "Zahntechnik in Zahlen",
  "Wie viele Labore es gibt und wie viele jedes Jahr aufgeben."),
 ("warum-zahnaerzte-das-dentallabor-wechseln", "Warum Praxen das Labor wechseln",
  "Die Anlässe hinter einem Wechsel und was Sie daraus ableiten."),
 ("dentallabor-kaufen-oder-uebernehmen", "Labor kaufen oder übernehmen",
  "Was den Preis bestimmt und wie Sie die Praxen danach halten."),
 ("eigenlabor-und-praxislabor", "Eigenlabor und Praxislabor",
  "Wo ein Praxislabor an Grenzen stößt und wo Sie gewinnen."),
]

def text_von(fragment: str) -> str:
    t = re.sub(r"<[^>]+>", "", fragment)
    return H.unescape(re.sub(r"\s+", " ", t)).strip()

def faq_paare(quelle: str):
    paare = []
    for m in re.finditer(
        r'class="accordion-css__item-top".*?class="text-size-medium">(.*?)</div>'
        r'.*?class="accordion-css__item-bottom-content">(.*?)</div>', quelle, re.S):
        f, a = text_von(m.group(1)), text_von(m.group(2))
        if f and a:
            paare.append((f, a))
    return paare

def wissen_block() -> str:
    karten = "".join(
        f'<li><a class="wissen-karte" href="/wissen/{s}/">'
        f'<h2>{t}</h2><p>{b}</p><span>Lesen</span></a></li>' for s, t, b in KARTEN)
    return (MARKE_WISSEN_A +
      '<section class="section_wissen-teaser" id="wissen"><div class="padding-global">'
      '<div class="container-large"><div class="padding-section-large">'
      '<div class="margin-bottom margin-xlarge"><div class="text-align-center">'
      '<div class="max-width-large align-center">'
      '<h2 class="heading-style-h2">Wissen für Dentallabore</h2>'
      '<p class="text-color-secondary text-size-medium" style="margin-top:1rem">'
      'Arbeitshilfen zu den Fragen, die im Laboralltag anstehen. Mit Rechnern, Prüflisten '
      'und Textvorlagen zum Mitnehmen. Kostenlos und ohne Anmeldung.</p></div></div></div>'
      f'<ul class="wissen-karten">{karten}</ul>'
      '<div class="text-align-center" style="margin-top:2.5rem">'
      '<a class="wissen-textlink" href="/wissen/">Alle Arbeitshilfen ansehen'
      '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
      '<path d="M5 12h14M12 5l7 7-7 7" stroke="currentColor" stroke-width="2" '
      'stroke-linecap="round" stroke-linejoin="round"/></svg></a></div>'
      '</div></div></div></section>' + MARKE_WISSEN_E)

def main():
    p = WURZEL / "index.html"
    s = p.read_text(encoding="utf-8")
    vorher = len(s)

    # frühere Einfügungen dieses Skripts entfernen, damit es wiederholbar bleibt
    s = re.sub(re.escape(MARKE_WISSEN_A) + r".*?" + re.escape(MARKE_WISSEN_E), "", s, flags=re.S)
    s = re.sub(re.escape(MARKE_LD) + r'<script type="application/ld\+json">.*?</script>', "", s, flags=re.S)

    paare = faq_paare(s)
    if len(paare) < 4:
        sys.exit(f"Abbruch: nur {len(paare)} FAQ-Paare gefunden, das passt nicht zur Seite.")

    ld = {"@context": "https://schema.org", "@type": "FAQPage",
          "mainEntity": [{"@type": "Question", "name": f,
                          "acceptedAnswer": {"@type": "Answer", "text": a}} for f, a in paare]}
    ld_html = MARKE_LD + f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
    s = s.replace("</head>", ld_html + "</head>", 1)

    # CSS der Wissensseiten auch auf der Startseite verfuegbar machen
    css = '<link href="/assets/css/wissen-plus.css" rel="stylesheet">'
    if css not in s:
        s = s.replace('<link rel="canonical"', css + '<link rel="canonical"', 1)

    s = s.replace("<footer", wissen_block() + "<footer", 1)
    p.write_text(s, encoding="utf-8")
    print(f"FAQ-Paare ausgezeichnet: {len(paare)}")
    for f, _ in paare:
        print("   -", f[:80])
    print(f"Wissensblock eingefuegt. Startseite {vorher} -> {len(s)} Zeichen")

if __name__ == "__main__":
    main()
