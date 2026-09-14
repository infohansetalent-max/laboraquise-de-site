#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut die Uebersichtsseite /wissen/ aus derselben Schablone wie die Artikel."""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from wissen_bauen import KOPF, BODYSTART, NAV, FUSS, SKRIPTE, WURZEL, HOST

ARTIKEL = [
 ("kundenakquise-im-dentallabor", "Akquise",
  "Kundenakquise im Dentallabor",
  "Sieben Wege zu neuen Zahnarztpraxen, mit Aufwand und Vorlauf nebeneinandergestellt. Dazu ein Bedarfsrechner und ein Gesprächseinstieg zum Kopieren."),
 ("warum-zahnaerzte-das-dentallabor-wechseln", "Zusammenarbeit",
  "Warum Zahnärzte ihr Dentallabor wechseln",
  "Die Anlässe hinter einem Wechsel und wie Sie Erwartungen an Termin, Erreichbarkeit und Nacharbeit konkret klären."),
 ("preise-und-stundensatz-im-dentallabor", "Kalkulation",
  "Preise und Stundensatz im Dentallabor",
  "BEL II und BEB im Unterschied, die Rechnung hinter Ihrem Stundensatz und eine Vorlage für die Preisanpassung. Mit Rechner."),
 ("dentallabor-gruenden", "Gründung",
  "Ein Dentallabor gründen",
  "Meisterpflicht, Handwerksrolle, Medizinprodukterecht und Umsatzsteuer geordnet. Und die Frage, woher die ersten Praxen kommen."),
 ("dentallabor-kaufen-oder-uebernehmen", "Übernahme",
  "Ein Dentallabor kaufen oder übernehmen",
  "Was beim Kauf wirklich bezahlt wird, welche Unterlagen Sie sehen müssen und wie Sie die Praxen nach der Übergabe halten."),
 ("eigenlabor-und-praxislabor", "Wettbewerb",
  "Eigenlabor und Praxislabor verstehen",
  "Warum Praxen selbst fertigen, wo ein Praxislabor an Grenzen stößt und mit welchem Angebot Sie daneben Arbeit gewinnen."),
 ("zahntechnik-in-zahlen", "Marktzahlen",
  "Zahntechnik in Zahlen",
  "Wie viele zahntechnische Betriebe es gibt, wie viele jedes Jahr aufgeben und was daraus für Ihr Labor folgt. Jede Zahl mit Quelle."),
]

TITEL = "Wissen für Dentallabore: Akquise, Kalkulation, Gründung | Laboraquise.de"
BESCHR = ("Arbeitshilfen für Dentallabore: neue Zahnarztpraxen gewinnen, Stundensatz kalkulieren, "
          "Labor gründen oder übernehmen. Mit Rechnern, Prüflisten und Textvorlagen zum Mitnehmen.")

def bauen():
    karten = "".join(
        f'<li><a class="wissen-karte" href="/wissen/{slug}/">'
        f'<span class="wissen-karte__marke">{marke}</span>'
        f'<h2>{titel}</h2><p>{text}</p><span>Lesen</span></a></li>'
        for slug, marke, titel, text in ARTIKEL)

    ld = [{
      "@context":"https://schema.org","@type":"CollectionPage",
      "name":"Wissen für Dentallabore","description":BESCHR,
      "url":f"{HOST}/wissen/","inLanguage":"de-DE",
      "isPartOf":{"@type":"WebSite","name":"Laboraquise.de","url":HOST+"/"},
      "mainEntity":{"@type":"ItemList","numberOfItems":len(ARTIKEL),"itemListElement":[
        {"@type":"ListItem","position":i+1,"name":t,"url":f"{HOST}/wissen/{s}/"}
        for i,(s,_,t,_x) in enumerate(ARTIKEL)]}},
     {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
       {"@type":"ListItem","position":1,"name":"Startseite","item":HOST+"/"},
       {"@type":"ListItem","position":2,"name":"Wissen","item":f"{HOST}/wissen/"}]}]
    ld_html = ('<script type="application/ld+json">'
               + json.dumps({"@context": "https://schema.org", "@graph":
                             [{k: v for k, v in d.items() if k != "@context"} for d in ld]},
                            ensure_ascii=False) + "</script>")

    meta = (f'<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="robots" content="index, follow"><title>{TITEL}</title>'
            f'<meta name="description" content="{BESCHR}">'
            f'<link rel="canonical" href="{HOST}/wissen/">'
            f'<meta property="og:type" content="website"><meta property="og:locale" content="de_DE">'
            f'<meta property="og:site_name" content="Laboraquise.de">'
            f'<meta property="og:url" content="{HOST}/wissen/">'
            f'<meta property="og:title" content="{TITEL}">'
            f'<meta property="og:description" content="{BESCHR}">'
            f'<meta property="og:image" content="{HOST}/assets/69ce12160e49568ac435ef6a/laboraquise-icon-512-v2.png">'
            f'<meta property="og:image:width" content="512"><meta property="og:image:height" content="512">'
            f'<meta property="og:image:type" content="image/png">'
            f'<meta property="og:image:alt" content="Laboraquise.de: Markenzeichen mit zwei verbundenen Personen">'
            f'<meta name="twitter:card" content="summary"><meta name="twitter:title" content="{TITEL}">'
            f'<meta name="twitter:description" content="{BESCHR}">'
            f'<meta name="twitter:image" content="{HOST}/assets/69ce12160e49568ac435ef6a/laboraquise-icon-512-v2.png">'
            f'<meta name="twitter:image:alt" content="Laboraquise.de: Markenzeichen mit zwei verbundenen Personen">')

    kopfbereich = ('<header class="section_header"><div class="padding-global"><div class="container-large">'
      '<div class="padding-section-nav"><div class="wissen-crumb"><a href="/">Startseite</a><span>/</span>'
      '<span>Wissen</span></div><div class="header3_component"><div class="w-layout-grid header3_content">'
      '<div class="header3_content-left"><div class="hero-pille">'
      '<span class="hero-pille__punkt" aria-hidden="true"></span>'
      '<span class="hero-pille__text">Wissen für Dentallabore</span>'
      '<span class="hero-pille__glanz" aria-hidden="true"></span></div>'
      '<h1 class="header3_h1 wissen-title">Arbeitshilfen für Ihr <span class="text-color-primary">Dentallabor</span></h1>'
      '<p class="text-color-secondary text-size-medium wissen-lead">Sieben Seiten zu den Fragen, die im Laboralltag '
      'tatsächlich anstehen: neue Praxen gewinnen, richtig kalkulieren, gründen oder übernehmen. '
      'Mit Rechnern, Prüflisten und Textvorlagen zum Mitnehmen.</p>'
      '</div></div></div></div></div></div></header>')

    inhalt = ('<div class="padding-global"><div class="container-large">'
      '<div style="padding:1rem 0 6rem">'
      f'<ul class="wissen-karten">{karten}</ul>'
      '<div class="merk" style="margin-top:3rem"><b>Wie diese Seiten gemeint sind</b>'
      '<p>Alle Texte sind für Inhaberinnen und Inhaber zahntechnischer Labore geschrieben. '
      'Zahlen stehen mit Quelle dabei, Abgeleitetes ist als abgeleitet gekennzeichnet, und was wir nicht '
      'belegen können, nennen wir nicht als Fakt. Rechts- und Steuerfragen ordnen wir ein, ersetzen aber '
      'keine Beratung.</p></div>'
      '</div></div></div>')

    html = ("<!doctype html><html lang=\"de\"><head>" + meta + KOPF + ld_html + "</head>"
            + BODYSTART + NAV + '<main class="main-wrapper" id="inhalt">' + kopfbereich + inhalt
            + FUSS + SKRIPTE + '<script src="/assets/js/wissen-plus.js" defer></script>'
            + "</body></html>")
    ziel = WURZEL / "wissen" / "index.html"
    ziel.write_text(html, encoding="utf-8")
    return ziel

if __name__ == "__main__":
    z = bauen()
    print(f"{z.relative_to(WURZEL)}  {z.stat().st_size/1024:.0f} KB  ({len(ARTIKEL)} Artikel)")
