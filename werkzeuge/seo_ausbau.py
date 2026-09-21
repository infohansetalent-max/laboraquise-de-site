#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Spielt die Entitaet auf alle Seiten und schreibt robots, sitemap, llms.txt.

Wiederholbar: das Skript entfernt zuerst jede Auszeichnung, die es selbst
erzeugt hat, und setzt sie neu. Zweimal laufen lassen aendert nichts.

Gelesen wird ausschliesslich aus dem sichtbaren Seitentext. Damit kann die
Auszeichnung nicht behaupten, was auf der Seite nicht steht. Die
Datumsangaben kommen aus der Versionsgeschichte, nicht aus der Fantasie.

Aufruf:  python3 werkzeuge/seo_ausbau.py
"""
from __future__ import annotations

import html as H
import json
import pathlib
import re
import subprocess
import sys

WURZEL = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WURZEL / "werkzeuge"))
sys.path.insert(0, str(WURZEL / "scripts"))

import entitaet as E  # noqa: E402
from serve import PAGES  # noqa: E402

HOST = E.HOST
LD_MUSTER = re.compile(r'<script type="application/ld\+json">.*?</script>', re.S)


# ---------------------------------------------------------------- Hilfen

def nur_text(bruchstueck: str) -> str:
    t = re.sub(r"<[^>]+>", " ", bruchstueck)
    return H.unescape(re.sub(r"\s+", " ", t)).strip()


def git_datum(pfad: str, erst: bool) -> str:
    """Belegtes Datum aus der Versionsgeschichte. Kein Commit, kein Datum.

    Liegt die Datei im Arbeitsbaum geaendert vor, gilt heute: die Aenderung
    ist real, sie ist nur noch nicht festgeschrieben. Nach dem Commit nennt
    git dasselbe Datum, die Angabe bleibt also stimmig."""
    befehl = ["git", "log", "--format=%ad", "--date=short", "-1"]
    if erst:
        befehl.insert(2, "--diff-filter=A")
    ergebnis = subprocess.run(befehl + ["--", pfad], cwd=WURZEL,
                              capture_output=True, text=True)
    datum = ergebnis.stdout.strip()
    if not datum:
        # Noch kein Commit: die Seite ist neu und geht heute raus.
        return _heute() if seiten_datei_existiert(pfad) else ""
    if not erst:
        offen = subprocess.run(["git", "status", "--porcelain", "--", pfad],
                               cwd=WURZEL, capture_output=True, text=True).stdout.strip()
        if offen:
            return _heute()
    return datum


def seiten_datei_existiert(pfad: str) -> bool:
    return (WURZEL / pfad).is_file()


def _heute() -> str:
    from datetime import date
    return date.today().isoformat()


def seiten_datei(pfad: str) -> pathlib.Path:
    return WURZEL / pfad.lstrip("/") / "index.html"


def lies(pfad: str) -> str:
    return seiten_datei(pfad).read_text(encoding="utf-8")


def titel_von(quelle: str) -> str:
    return H.unescape(re.search(r"<title>(.*?)</title>", quelle, re.S).group(1)).strip()


def beschreibung_von(quelle: str) -> str:
    m = re.search(r'<meta name="description" content="(.*?)"', quelle, re.S)
    return H.unescape(m.group(1)).strip() if m else ""


def h1_von(quelle: str) -> str:
    m = re.search(r"<h1[^>]*>(.*?)</h1>", quelle, re.S)
    return nur_text(m.group(1)) if m else ""


def faq_von(pfad: str, quelle: str):
    """Fragen und Antworten aus dem sichtbaren Text. Zwei Bauweisen:
    die Aufklappliste der Startseite und die h3/p-Folge der Wissensseiten."""
    paare = []
    if pfad == "/":
        for m in re.finditer(
                r'class="accordion-css__item-top".*?class="text-size-medium">(.*?)</div>'
                r'.*?class="accordion-css__item-bottom-content">(.*?)</div>', quelle, re.S):
            f, a = nur_text(m.group(1)), nur_text(m.group(2))
            if f and a:
                paare.append((f, a))
        return paare
    m = re.search(r'<section id="fragen">(.*?)</section>', quelle, re.S)
    if not m:
        return paare
    for f, a in re.findall(r"<h3[^>]*>(.*?)</h3>\s*<p[^>]*>(.*?)</p>", m.group(1), re.S):
        paare.append((nur_text(f), nur_text(a)))
    return paare


def erste_absaetze(quelle: str, anzahl: int = 2) -> str:
    """Anfang des Artikeltextes, fuer die Kurzfassung in llms-full.txt."""
    m = re.search(r"<article[^>]*>(.*?)</article>", quelle, re.S)
    raum = m.group(1) if m else quelle
    stuecke = [nur_text(p) for p in re.findall(r"<p[^>]*>(.*?)</p>", raum, re.S)]
    stuecke = [s for s in stuecke if len(s) > 80]
    return " ".join(stuecke[:anzahl])


# ---------------------------------------------------------- Seitenkunde

# Krümelpfad und Art je Seite. Die Wissensseiten erben ihren Namen aus der H1.
KRUME = {
    "/": [("Startseite", HOST + "/")],
    "/termin/": [("Startseite", HOST + "/"), ("Erstgespräch", HOST + "/termin/")],
    "/impressum/": [("Startseite", HOST + "/"), ("Impressum", HOST + "/impressum/")],
    "/datenschutz/": [("Startseite", HOST + "/"), ("Datenschutz", HOST + "/datenschutz/")],
    "/agb/": [("Startseite", HOST + "/"), ("AGB", HOST + "/agb/")],
    "/wissen/": [("Startseite", HOST + "/"), ("Wissen", HOST + "/wissen/")],
}

ARTIKEL_THEMA = {
    "/wissen/kundenakquise-im-dentallabor/": "Kundenakquise im Dentallabor",
    "/wissen/warum-zahnaerzte-das-dentallabor-wechseln/": "Laborwechsel von Zahnarztpraxen",
    "/wissen/preise-und-stundensatz-im-dentallabor/": "Kalkulation zahntechnischer Leistungen",
    "/wissen/dentallabor-gruenden/": "Gründung eines zahntechnischen Betriebs",
    "/wissen/dentallabor-kaufen-oder-uebernehmen/": "Übernahme eines Dentallabors",
    "/wissen/dentallabor-verkaufen/": "Verkauf eines Dentallabors",
    "/wissen/eigenlabor-und-praxislabor/": "Praxiseigene Dentallabore",
    "/wissen/zahntechnik-in-zahlen/": "Marktzahlen der Zahntechnik in Deutschland",
    "/wissen/glossar/": "Fachbegriffe der Zahntechnik",
}


def liste_der_artikel(quelle: str) -> dict:
    """ItemList der Uebersicht, gelesen aus ihren eigenen Karten."""
    treffer, gesehen = [], set()
    for slug, titel in re.findall(
            r'<a class="wissen-karte" href="/wissen/([^/"]+)/">.*?<h2>(.*?)</h2>',
            quelle, re.S):
        if slug in gesehen:
            continue
        gesehen.add(slug)
        treffer.append((slug, nur_text(titel)))
    return {
        "@type": "ItemList",
        "numberOfItems": len(treffer),
        "itemListElement": [
            {"@type": "ListItem", "position": i, "name": t,
             "url": f"{HOST}/wissen/{s}/"}
            for i, (s, t) in enumerate(treffer, start=1)],
    }


def ist_artikel(pfad: str) -> bool:
    return pfad.startswith("/wissen/") and pfad != "/wissen/"


def graph_fuer(pfad: str, quelle: str) -> list:
    url = HOST + pfad
    titel, beschr = titel_von(quelle), beschreibung_von(quelle)
    krumen = KRUME.get(pfad)
    if krumen is None:                       # Wissensseite
        krumen = [("Startseite", HOST + "/"), ("Wissen", HOST + "/wissen/"),
                  (h1_von(quelle), url)]

    stuecke = E.grundgraph()
    stuecke.append(E.krume(krumen))

    erstellt, geaendert = git_datum(pfad.lstrip("/") + "index.html", True), \
        git_datum(pfad.lstrip("/") + "index.html", False)

    if ist_artikel(pfad):
        artikel = {
            "@type": "Article",
            "@id": url + "#artikel",
            "headline": h1_von(quelle) or titel.split("|")[0].strip(),
            "name": titel.split("|")[0].strip(),
            "description": beschr,
            "inLanguage": "de-DE",
            "url": url,
            "mainEntityOfPage": {"@id": url + "#seite"},
            "isPartOf": {"@id": HOST + "/wissen/#sammlung"},
            "author": {"@id": E.ID_PERSON},
            "publisher": {"@id": E.ID_ORG},
            "copyrightHolder": {"@id": E.ID_ORG},
            "about": ARTIKEL_THEMA.get(pfad, "Zahntechnik"),
            "audience": {"@type": "BusinessAudience",
                         "name": "Inhaber und Leitung zahntechnischer Labore"},
            "image": E.MARKE_BILD,
        }
        # Datumsangaben nur, wenn die Versionsgeschichte sie hergibt.
        if erstellt:
            artikel["datePublished"] = erstellt
        if geaendert:
            artikel["dateModified"] = geaendert
        stuecke.append(artikel)
        seite_typ, haupt = "WebPage", {"@id": url + "#artikel"}
    elif pfad == "/wissen/":
        seite_typ, haupt = "CollectionPage", None
        stuecke.append({
            "@type": "CollectionPage",
            "@id": HOST + "/wissen/#sammlung",
            "url": HOST + "/wissen/",
            "name": titel.split("|")[0].strip(),
            "description": beschr,
            "inLanguage": "de-DE",
            "isPartOf": {"@id": E.ID_SITE},
            "publisher": {"@id": E.ID_ORG},
            "about": "Betriebswirtschaftliche und fachliche Fragen im Dentallabor",
            # Die Liste kommt aus den Karten der Seite selbst. Damit kann sie
            # nicht auf Artikel zeigen, die dort nicht verlinkt sind.
            "mainEntity": liste_der_artikel(quelle),
        })
    else:
        seite_typ, haupt = "WebPage", None
        if pfad == "/":
            seite_typ = "WebPage"

    seite = {
        "@type": seite_typ,
        "@id": url + "#seite",
        "url": url,
        "name": titel,
        "description": beschr,
        "inLanguage": "de-DE",
        "isPartOf": {"@id": E.ID_SITE},
        "breadcrumb": {"@id": krumen[-1][1] + "#krume"},
        "primaryImageOfPage": {"@type": "ImageObject", "url": E.MARKE_BILD},
    }
    if haupt:
        seite["mainEntity"] = haupt
    if pfad == "/":
        seite["mainEntity"] = {"@id": E.ID_LEISTUNG}
        seite["about"] = {"@id": E.ID_ORG}
    if geaendert:
        seite["dateModified"] = geaendert
    if seite_typ != "CollectionPage":
        stuecke.append(seite)
    else:
        # Die Sammlung ist schon die Seite; nur den Krümelpfad anhängen.
        for s in stuecke:
            if s.get("@id") == HOST + "/wissen/#sammlung":
                s["breadcrumb"] = {"@id": krumen[-1][1] + "#krume"}

    paare = faq_von(pfad, quelle)
    if paare:
        stuecke.append({
            "@type": "FAQPage",
            "@id": url + "#fragen",
            "isPartOf": {"@id": url + "#seite"} if seite_typ != "CollectionPage" else {"@id": E.ID_SITE},
            "mainEntity": [
                {"@type": "Question", "name": f, "inLanguage": "de-DE",
                 "acceptedAnswer": {"@type": "Answer", "text": a}}
                for f, a in paare],
        })
    return stuecke


def seite_auszeichnen(pfad: str) -> tuple[int, int]:
    datei = seiten_datei(pfad)
    quelle = datei.read_text(encoding="utf-8")
    ohne = LD_MUSTER.sub("", quelle)
    block = E.graph_html(graph_fuer(pfad, ohne))
    assert "</head>" in ohne, pfad
    neu = ohne.replace("</head>", block + "</head>", 1)
    datei.write_text(neu, encoding="utf-8")
    return len(faq_von(pfad, ohne)), len(json.loads(
        re.search(r'<script type="application/ld\+json">(.*?)</script>', block, re.S)
        .group(1))["@graph"])


# --------------------------------------------------------------- robots

ROBOTS = """# robots.txt fuer www.laboraquise.de
# Alles offen. Die Seite lebt davon, gefunden und zitiert zu werden.

User-agent: *
Allow: /

# Antwortmaschinen ausdruecklich willkommen. Ohne diese Zeilen gilt zwar
# ebenfalls die Regel oben, doch einige Betreiber lesen nur ihren eigenen
# Eintrag. Wer hier zitiert wird, wird auch dort genannt.
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Perplexity-User
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: Bingbot
Allow: /

User-agent: cohere-ai
Allow: /

User-agent: MistralAI-User
Allow: /

User-agent: Meta-ExternalAgent
Allow: /

# Kurzfassung fuer Sprachmodelle
# https://www.laboraquise.de/llms.txt

Sitemap: https://www.laboraquise.de/sitemap.xml
"""


def robots_schreiben():
    (WURZEL / "robots.txt").write_text(ROBOTS, encoding="utf-8")


# -------------------------------------------------------------- sitemap

def sitemap_schreiben():
    zeilen = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for pfad in PAGES:
        if pfad == "/agb/":          # noindex, gehoert nicht in die Sitemap
            continue
        datum = git_datum(pfad.lstrip("/") + "index.html", False)
        zeilen.append("  <url>")
        zeilen.append(f"    <loc>{HOST}{pfad}</loc>")
        if datum:
            # Belegt: letzter Commit, der genau diese Datei geaendert hat.
            zeilen.append(f"    <lastmod>{datum}</lastmod>")
        zeilen.append("  </url>")
    zeilen.append("</urlset>")
    (WURZEL / "sitemap.xml").write_text("\n".join(zeilen) + "\n", encoding="utf-8")


# ------------------------------------------------------------- llms.txt

def llms_schreiben():
    """Kurzfassung der Seite fuer Sprachmodelle.

    Der Sinn: ein Modell, das die Marke einordnen soll, muss sonst 240 KB
    Webflow-HTML durchsuchen. Hier steht dasselbe in 4 KB, in derselben
    Reihenfolge, mit denselben Zahlen und denselben Grenzen.
    """
    seiten = []
    for pfad in PAGES:
        if pfad in ("/agb/", "/impressum/", "/datenschutz/"):
            continue
        quelle = lies(pfad)
        seiten.append((pfad, titel_von(quelle).split("|")[0].strip(),
                       beschreibung_von(quelle)))

    kurz = ["# Laboraquise.de",
            "",
            "> Laboraquise.de richtet Werbekampagnen von Dentallaboren auf "
            "Zahnarztpraxen im selbst gewählten Einzugsgebiet aus und prüft "
            "eingehende Anfragen anhand des vorher festgelegten Kundenprofils. "
            "Die Gespräche mit der Praxis führt das Labor selbst. Anbieter ist "
            "Hansetalent, Inhaber Ben Carstens, Hamburg.",
            "",
            "Betreiber: Hansetalent, Inhaber Ben Carstens, Eppendorfer Weg 168, "
            "20253 Hamburg, Deutschland. Kontakt: info@laboraquise.de.",
            "Sprache: Deutsch. Markt: Deutschland. Zielgruppe: Inhaber und "
            "Leitung zahntechnischer Labore.",
            "",
            "## Was zutrifft und was nicht",
            "",
            "- Zugesagt wird eine Anzahl qualifizierter Praxisanfragen, sofern "
            "sie im Angebot vereinbart ist. Neue Kunden oder Umsatz sind nicht "
            "zugesagt.",
            "- Qualifiziert heißt: die Anfrage erfüllt die vor dem Start "
            "schriftlich festgelegten Muss-Kriterien und stammt aus dem "
            "vereinbarten Einzugsgebiet.",
            "- Das an die Werbeplattform gezahlte Budget ist von einer "
            "Erstattung der Dienstleistungsgebühr nicht umfasst.",
            "- Die Gespräche mit der Praxis und die Entscheidung über eine "
            "Zusammenarbeit liegen beim Labor.",
            "",
            "## Seiten",
            ""]
    for pfad, name, beschr in seiten:
        kurz.append(f"- [{name}]({HOST}{pfad}): {beschr}")
    kurz += ["",
             "## Belegte Zahlen aus dem Wissensbereich",
             "",
             "- 6.845 zahntechnische Betriebe in Deutschland im ersten Halbjahr "
             "2025. Quelle: ZDH-Statistik, ausgewertet von Rebmann Research.",
             "- 6.994 gewerbliche Dentallabore 2024, ein Rückgang von 3,4 Prozent "
             "gegenüber 2023. Quelle: ebenda.",
             "- 105 Neugründungen und 254 Betriebsaufgaben im ersten Halbjahr "
             "2025. Quelle: ebenda.",
             "- Das Zahntechnikerhandwerk ist zulassungspflichtig nach Anlage A "
             "Nummer 37 der Handwerksordnung.",
             "- Zahntechnische Leistungen unterliegen dem ermäßigten Steuersatz "
             "von 7 Prozent nach § 12 Absatz 2 Nummer 6 UStG.",
             "",
             "Nicht belegt und deshalb auf der Seite nicht behauptet: Anzahl der "
             "Praxislabore, Branchenumsatz, Beschäftigtenzahl, Wechselquoten von "
             "Praxen.",
             "",
             "## Zitieren",
             "",
             "Inhalte dürfen mit Quellenangabe und Link auf die jeweilige Seite "
             "zitiert werden. Die vollständigen Texte stehen in "
             f"[llms-full.txt]({HOST}/llms-full.txt).",
             ""]
    (WURZEL / "llms.txt").write_text("\n".join(kurz), encoding="utf-8")

    # Langfassung: je Seite die Kernaussagen und alle Fragen mit Antwort.
    lang = ["# Laboraquise.de, vollständige Fassung für Sprachmodelle",
            "",
            "Stand: " + (git_datum("index.html", False) or "unbekannt") + ". "
            "Quelle aller Angaben: die verlinkten Seiten selbst.",
            ""]
    for pfad in PAGES:
        if pfad in ("/agb/", "/impressum/", "/datenschutz/"):
            continue
        quelle = lies(pfad)
        lang.append(f"## {titel_von(quelle).split('|')[0].strip()}")
        lang.append("")
        lang.append(f"URL: {HOST}{pfad}")
        lang.append("")
        lang.append(beschreibung_von(quelle))
        anfang = erste_absaetze(quelle)
        if anfang:
            lang += ["", anfang]
        paare = faq_von(pfad, quelle)
        if paare:
            lang += ["", "### Fragen und Antworten", ""]
            for f, a in paare:
                lang += [f"**{f}**", "", a, ""]
        lang.append("")
    (WURZEL / "llms-full.txt").write_text("\n".join(lang), encoding="utf-8")
    return len(seiten)


# ------------------------------------------------------------------ Lauf

if __name__ == "__main__":
    print("Auszeichnung je Seite")
    for pfad in PAGES:
        fragen, stuecke = seite_auszeichnen(pfad)
        print(f"  {pfad:58s} {stuecke:2d} Bausteine, {fragen:2d} Fragen")
    robots_schreiben()
    sitemap_schreiben()
    anzahl = llms_schreiben()
    print(f"robots.txt, sitemap.xml, llms.txt und llms-full.txt geschrieben "
          f"({anzahl} Seiten in der Kurzfassung)")
