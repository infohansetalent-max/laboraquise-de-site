#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut die Wissensseiten aus der abgenommenen Seitenschablone.

Die Schablone stammt aus der bereits freigegebenen Seite
wissen/warum-zahnaerzte-das-dentallabor-wechseln/. Dadurch erben alle
neuen Seiten Navigation, Fussbereich, Schrift und Farben unveraendert.
Neu ist allein der Artikelteil je Seite.
"""
from __future__ import annotations
import json, pathlib, re, sys, html

WURZEL = pathlib.Path(__file__).resolve().parent.parent
SCHAB = WURZEL / "werkzeuge" / "schablone"
HOST = "https://www.laboraquise.de"

def teil(name: str) -> str:
    """Schablonenteile tragen die Endung .part, damit sie auf dem Host
    nicht als eigene HTML-Seite ausgeliefert und indexiert werden."""
    return (SCHAB / name).read_text(encoding="utf-8")

KOPF, BODYSTART, NAV, FUSS, SKRIPTE = (
    teil("kopf.part"), teil("bodystart.part"), teil("nav.part"),
    teil("fuss.part"), teil("skripte.part"))

# Zusatz-CSS in den Kopf haengen, direkt hinter das Webflow-Stylesheet.
ZUSATZ_LINK = ('<link href="/assets/css/wissen-basis.css" rel="stylesheet">'
               '<link href="/assets/css/wissen-plus.css" rel="stylesheet">'
               # zuletzt, damit seine Regeln die davor stehenden ueberschreiben
               '<noscript><link href="/assets/css/wissen-ohne-js.css" rel="stylesheet"></noscript>')
if "wissen-basis.css" not in KOPF:
    anker = '<link rel="icon"'
    assert anker in KOPF, "Anker fuer die Stylesheets fehlt in der Kopfschablone"
    KOPF = KOPF.replace(anker, ZUSATZ_LINK + anker, 1)
assert "wissen-basis.css" in KOPF and "wissen-plus.css" in KOPF


def kennzahlen(felder) -> str:
    """felder: Liste von (zahl, text, quelle)"""
    z = "".join(
        f'<div class="kz-feld"><span class="kz-zahl">{z_}</span>'
        f'<span class="kz-text">{t}</span>'
        f'<span class="kz-quelle">{q}</span></div>'
        for z_, t, q in felder)
    return f'<div class="kz-band">{z}</div>'


def figur(svg: str, unterschrift: str, minbreite: int = 340) -> str:
    return (f'<figure class="fig"><div class="fig__rahmen" style="--fig-min:{minbreite}px">'
            f'{svg}</div><figcaption>{unterschrift}</figcaption></figure>')


def merksatz(titel: str, text: str) -> str:
    return f'<div class="merk"><b>{titel}</b><p>{text}</p></div>'


def mitnehmen(titel: str, text: str) -> str:
    sicher = html.escape(text)
    return (f'<details class="mitnehmen"><summary>{titel}</summary>'
            f'<div class="mitnehmen__inhalt"><pre>{sicher}</pre>'
            f'<button type="button" data-kopieren>Text kopieren</button></div></details>')


def weiterlesen(eintraege) -> str:
    li = "".join(f'<li><a href="{u}"><b>{t}</b><span>{b}</span></a></li>' for u, t, b in eintraege)
    return f'<h2 id="weiterlesen">Weiterlesen</h2><ul class="weiter">{li}</ul>'


def schritte(paare) -> str:
    s = "".join(f'<div class="step"><b>{n}</b><span>{t}</span></div>' for n, t in paare)
    return f'<div class="flow">{s}</div>'


def checkliste(punkte, name: str) -> str:
    li = "".join(
        f'<li><label><input type="checkbox"><span>{p}</span></label></li>'
        for p in punkte)
    return f'<ul class="checklist" data-liste="{name}">{li}</ul>'



def abschluss(titel: str, text: str, schritte_paare, unterschrift: str) -> str:
    """Abschluss jeder Wissensseite: Bezug zum Angebot und ein Weg zum
    Erstgespraech. Uebernimmt Aufbau und Klassen der abgenommenen Artikelseite."""
    s = "".join(f'<div class="step"><b>{n}</b><span>{t}</span></div>' for n, t in schritte_paare)
    return (f'<section id="ansprechen"><h2>{titel}</h2><p>{text}</p>'
            f'<figure><div class="flow">{s}</div>'
            f'<figcaption>{unterschrift}</figcaption></figure></section>'
            '<a class="button wissen-button cta" href="/termin/">'
            '<span>Erstgespräch vereinbaren</span>'
            '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
            '<path d="M4 12H20M20 12L14 6M20 12L14 18" stroke="currentColor" stroke-width="2" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg></a>')

def tabelle(kopf, zeilen) -> str:
    th = "".join(f"<th>{k}</th>" for k in kopf)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in z) + "</tr>" for z in zeilen)
    return f"<table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>"


def render(seite: dict) -> str:
    slug = seite["slug"]
    url = f"{HOST}/wissen/{slug}/"
    toc = "".join(f'<li><a href="#{a}">{t}</a></li>' for a, t in seite["toc"])

    ld = [{
        "@context": "https://schema.org", "@type": "Article",
        "headline": seite["h1_klartext"],
        "description": seite["beschreibung"],
        "inLanguage": "de-DE",
        "url": url,
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "isPartOf": {"@type": "CollectionPage", "@id": f"{HOST}/wissen/"},
        "publisher": {"@type": "Organization", "name": "Laboraquise.de", "url": HOST + "/"},
        "about": seite.get("about", "Zahntechnik"),
    }, {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Startseite", "item": HOST + "/"},
            {"@type": "ListItem", "position": 2, "name": "Wissen", "item": HOST + "/wissen/"},
            {"@type": "ListItem", "position": 3, "name": seite["krume"], "item": url},
        ]}]
    if seite.get("faq"):
        ld.append({
            "@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": f,
                 "acceptedAnswer": {"@type": "Answer", "text": a}}
                for f, a in seite["faq"]]})
    ld_html = ('<script type="application/ld+json">'
               + json.dumps({"@context": "https://schema.org", "@graph":
                             [{k: v for k, v in d.items() if k != "@context"} for d in ld]},
                            ensure_ascii=False) + "</script>")

    faq_html = ""
    if seite.get("faq"):
        blocks = "".join(
            f'<h3>{f}</h3><p>{a}</p>' for f, a in seite["faq"])
        faq_html = (f'<section id="fragen"><h2>Häufige Fragen</h2>{blocks}</section>')

    kopf_meta = (
        f'<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        f'<meta name="robots" content="index, follow">'
        f'<title>{seite["titel"]}</title>'
        f'<meta name="description" content="{seite["beschreibung"]}">'
        f'<link rel="canonical" href="{url}">'
        f'<meta property="og:type" content="article">'
        f'<meta property="og:locale" content="de_DE">'
        f'<meta property="og:site_name" content="Laboraquise.de">'
        f'<meta property="og:url" content="{url}">'
        f'<meta property="og:title" content="{seite["titel"]}">'
        f'<meta property="og:description" content="{seite["beschreibung"]}">'
        f'<meta property="og:image" content="{HOST}/assets/69ce12160e49568ac435ef6a/laboraquise-icon-512-v2.png">'
        f'<meta property="og:image:width" content="512"><meta property="og:image:height" content="512">'
        f'<meta property="og:image:type" content="image/png">'
        f'<meta property="og:image:alt" content="Laboraquise.de: Markenzeichen mit zwei verbundenen Personen">'
        f'<meta name="twitter:card" content="summary">'
        f'<meta name="twitter:title" content="{seite["titel"]}">'
        f'<meta name="twitter:description" content="{seite["beschreibung"]}">'
        f'<meta name="twitter:image" content="{HOST}/assets/69ce12160e49568ac435ef6a/laboraquise-icon-512-v2.png">'
        f'<meta name="twitter:image:alt" content="Laboraquise.de: Markenzeichen mit zwei verbundenen Personen">')

    kopfbereich = f'''<header class="section_header"><div class="padding-global"><div class="container-large"><div class="padding-section-nav"><div class="wissen-crumb"><a href="/">Startseite</a><span>/</span><a href="/wissen/">Wissen</a></div><div class="header3_component"><div class="w-layout-grid header3_content"><div class="header3_content-left"><div class="hero-pille"><span class="hero-pille__punkt" aria-hidden="true"></span><span class="hero-pille__text">{seite["pille"]}</span><span class="hero-pille__glanz" aria-hidden="true"></span></div><h1 class="header3_h1 wissen-title">{seite["h1"]}</h1><p class="text-color-secondary text-size-medium wissen-lead">{seite["lead"]}</p><a class="wissen-textlink" href="#{seite["toc"][0][0]}">Direkt zum Inhalt<svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 5v14M5 12l7 7 7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></a></div></div></div></div></div></div></header>'''

    artikel = f'''<div class="padding-global"><div class="container-large"><div class="wissen-layout"><nav class="wissen-toc" aria-label="Inhalt dieser Seite"><div class="text-size-small text-color-secondary">Auf dieser Seite</div><ol>{toc}</ol></nav><article class="wissen-article">{seite["inhalt"]}{faq_html}{seite.get("abschluss","")}{seite.get("nachspann","")}</article></div></div></div>'''

    return ("<!doctype html><html lang=\"de\"><head>" + kopf_meta + KOPF + ld_html + "</head>"
            + BODYSTART + NAV
            + '<main class="main-wrapper" id="inhalt">' + kopfbereich + artikel
            + FUSS + SKRIPTE
            + '<script src="/assets/js/wissen-plus.js" defer></script>'
            + "</body></html>")


def schreibe(seite: dict):
    ziel = WURZEL / "wissen" / seite["slug"] / "index.html"
    ziel.parent.mkdir(parents=True, exist_ok=True)
    ziel.write_text(render(seite), encoding="utf-8")
    return ziel


if __name__ == "__main__":
    sys.path.insert(0, str(WURZEL / "werkzeuge"))
    import inhalte
    for s in inhalte.SEITEN:
        z = schreibe(s)
        print(f"{z.relative_to(WURZEL)}  {z.stat().st_size/1024:.0f} KB")
