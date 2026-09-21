#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Die Entitaet Laboraquise.de, einmal definiert, ueberall gleich.

Warum das eine eigene Datei ist: Suchmaschinen und Antwortmaschinen bauen
sich aus vielen Einzelsignalen ein Bild davon, *wer* hier schreibt. Steht
das auf jeder Seite anders, entsteht kein Bild, sondern Rauschen. Hier
steht es einmal, mit festen Kennungen (@id), auf die jede Seite verweist.

Nichts in dieser Datei ist erfunden. Anschrift, Rechtsform und Person
stammen aus dem Impressum, die Datumsangaben aus der Versionsgeschichte.
Ein Feld ohne Beleg bleibt leer, statt geraten zu werden.
"""
from __future__ import annotations

HOST = "https://www.laboraquise.de"

# Feste Kennungen. Sie sind der Kitt: jede Seite verweist auf dieselbe
# Organisation, dieselbe Person, dieselbe Leistung.
ID_ORG = f"{HOST}/#organisation"
ID_SITE = f"{HOST}/#website"
ID_PERSON = f"{HOST}/#ben-carstens"
ID_LEISTUNG = f"{HOST}/#leistung"

MARKE_BILD = f"{HOST}/assets/69ce12160e49568ac435ef6a/laboraquise-icon-512-v2.png"

# Aus dem Impressum, Stand 14.09.2026.
ANSCHRIFT = {
    "@type": "PostalAddress",
    "streetAddress": "Eppendorfer Weg 168",
    "postalCode": "20253",
    "addressLocality": "Hamburg",
    "addressRegion": "Hamburg",
    "addressCountry": "DE",
}


def organisation() -> dict:
    return {
        "@type": "Organization",
        "@id": ID_ORG,
        "name": "Laboraquise.de",
        "legalName": "Hansetalent, Inhaber Ben Carstens",
        "description": (
            "Laboraquise.de richtet Werbekampagnen von Dentallaboren auf "
            "Zahnarztpraxen im selbst gewählten Einzugsgebiet aus und prüft "
            "eingehende Anfragen anhand des vorher festgelegten Kundenprofils."
        ),
        "url": HOST + "/",
        "logo": {
            "@type": "ImageObject",
            "url": MARKE_BILD,
            "width": 512,
            "height": 512,
            "caption": "Laboraquise.de: Markenzeichen mit zwei verbundenen Personen",
        },
        "image": MARKE_BILD,
        "email": "info@laboraquise.de",
        "address": ANSCHRIFT,
        "foundingDate": "2026",
        "founder": {"@id": ID_PERSON},
        "employee": {"@id": ID_PERSON},
        "parentOrganization": {
            "@type": "Organization",
            "name": "Hansetalent",
            "url": "https://hansetalent.de/",
        },
        "areaServed": {"@type": "Country", "name": "Deutschland"},
        "knowsLanguage": "de",
        # Worueber diese Organisation belegbar etwas sagen kann. Diese Felder
        # ordnen die Marke einem Sachgebiet zu, statt nur einen Namen zu nennen.
        "knowsAbout": [
            "Kundenakquise für Dentallabore",
            "Zahntechnik",
            "Zusammenarbeit von Dentallabor und Zahnarztpraxis",
            "Kalkulation zahntechnischer Leistungen nach BEL II und BEB",
            "Gründung und Übernahme zahntechnischer Betriebe",
        ],
        "slogan": "Sie fertigen an. Wir sprechen Praxen an.",
        "contactPoint": {
            "@type": "ContactPoint",
            "contactType": "Vertrieb",
            "email": "info@laboraquise.de",
            "availableLanguage": "de",
            "areaServed": "DE",
        },
    }


def person() -> dict:
    return {
        "@type": "Person",
        "@id": ID_PERSON,
        "name": "Ben Carstens",
        "givenName": "Ben",
        "familyName": "Carstens",
        "jobTitle": "Inhaber",
        "worksFor": {"@id": ID_ORG},
        "address": ANSCHRIFT,
        "knowsAbout": [
            "Kundenakquise für Dentallabore",
            "Personalgewinnung für Dentallabore",
            "Werbekampagnen im Dentalmarkt",
        ],
        "description": (
            "Ben Carstens arbeitet seit 2022 ausschließlich mit Dentallaboren, "
            "zuerst bei der Besetzung von Stellen, seit 2026 bei der Gewinnung "
            "neuer Zahnarztpraxen."
        ),
    }


def website() -> dict:
    return {
        "@type": "WebSite",
        "@id": ID_SITE,
        "url": HOST + "/",
        "name": "Laboraquise.de",
        "inLanguage": "de-DE",
        "publisher": {"@id": ID_ORG},
        "copyrightHolder": {"@id": ID_ORG},
    }


def leistung() -> dict:
    """Was genau verkauft wird. Ohne dieses Stueck bleibt fuer eine
    Antwortmaschine offen, wofuer die Marke steht."""
    return {
        "@type": "Service",
        "@id": ID_LEISTUNG,
        "name": "Neukundengewinnung für Dentallabore",
        "serviceType": "Gewinnung von Zahnarztpraxen als Laborkunden",
        "provider": {"@id": ID_ORG},
        "areaServed": {"@type": "Country", "name": "Deutschland"},
        "audience": {
            "@type": "BusinessAudience",
            "name": "Zahntechnische Labore und Praxislabore in Deutschland",
        },
        "description": (
            "Kundenprofil festlegen, Angebot schärfen, Werbung im vereinbarten "
            "Einzugsgebiet schalten, eingehende Praxisanfragen anhand des "
            "Kundenprofils vorqualifizieren. Die Gespräche mit der Praxis führt "
            "das Labor selbst."
        ),
        "termsOfService": HOST + "/agb/",
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Ablauf der Zusammenarbeit",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {
                    "@type": "Service", "name": "Kundenprofil und Zählkriterien festlegen"}},
                {"@type": "Offer", "itemOffered": {
                    "@type": "Service", "name": "Kampagne im gewählten Einzugsgebiet"}},
                {"@type": "Offer", "itemOffered": {
                    "@type": "Service", "name": "Vorqualifizierung eingehender Praxisanfragen"}},
            ],
        },
    }


def grundgraph() -> list:
    """Die vier Stuecke, die auf jede Seite gehoeren."""
    return [organisation(), person(), website(), leistung()]


def krume(paare) -> dict:
    """paare: Liste von (name, url)"""
    return {
        "@type": "BreadcrumbList",
        "@id": paare[-1][1] + "#krume",
        "itemListElement": [
            {"@type": "ListItem", "position": i, "name": n, "item": u}
            for i, (n, u) in enumerate(paare, start=1)
        ],
    }


def graph_html(stuecke: list) -> str:
    """Ein einziger Block je Seite. Mehrere Blöcke nebeneinander lesen
    Maschinen zwar auch, aber nur ein Graph zeigt die Verbindungen."""
    import json
    return ('<script type="application/ld+json">'
            + json.dumps({"@context": "https://schema.org", "@graph": stuecke},
                         ensure_ascii=False, separators=(",", ":"))
            + "</script>")
