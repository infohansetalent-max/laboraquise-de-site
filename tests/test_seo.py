"""SEO-Smoke-Test mit Python-Standardbibliothek. Alle öffentlichen Seiten."""
import json
import re
import threading
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urljoin, urlsplit, unquote
from urllib.request import urlopen
from xml.etree import ElementTree
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from serve import Handler, ThreadingHTTPServer, PAGES
ORIGIN = 'https://' + (ROOT / 'CNAME').read_text().strip().rstrip('/')
TITLES = {
    '/': 'Neukundengewinnung für Dentallabore | Laboraquise.de',
    '/termin/': 'Erstgespräch für Dentallabore vereinbaren | Laboraquise.de',
    '/ueber-uns/': 'Über Laboraquise.de: wer dahintersteht | Laboraquise.de',
    '/impressum/': 'Impressum | Laboraquise.de',
    '/datenschutz/': 'Datenschutzerklärung | Laboraquise.de',
    '/wissen/': 'Wissen für Dentallabore: Akquise, Kalkulation, Gründung | Laboraquise.de',
    '/wissen/warum-zahnaerzte-das-dentallabor-wechseln/': 'Warum Zahnärzte ihr Dentallabor wechseln | Laboraquise.de',
    '/wissen/kundenakquise-im-dentallabor/': 'Kundenakquise im Dentallabor: neue Zahnarztpraxen gewinnen | Laboraquise.de',
    '/wissen/preise-und-stundensatz-im-dentallabor/': 'Preise und Stundensatz im Dentallabor: BEL II, BEB, Kalkulation | Laboraquise.de',
    '/wissen/dentallabor-gruenden/': 'Dentallabor gründen: Voraussetzungen, Kosten, erste Praxen | Laboraquise.de',
    '/wissen/dentallabor-kaufen-oder-uebernehmen/': 'Dentallabor kaufen oder übernehmen: worauf es beim Preis ankommt | Laboraquise.de',
    '/wissen/dentallabor-verkaufen/': 'Dentallabor verkaufen: Wert ermitteln, Steuern, Ablauf | Laboraquise.de',
    '/wissen/eigenlabor-und-praxislabor/': 'Eigenlabor und Praxislabor: was das für Ihr Dentallabor bedeutet | Laboraquise.de',
    '/wissen/zahntechnik-in-zahlen/': 'Wie viele Dentallabore gibt es in Deutschland? Zahlen mit Quelle | Laboraquise.de',
    '/agb/': 'Allgemeine Geschäftsbedingungen | Laboraquise.de',
}

class Page(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.feed(html)
        self.html = html
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))
    def attrs(self, tag, **attrs):
        return [a for t, a in self.tags if t == tag and all(a.get(k) == v for k, v in attrs.items())]

def read(path):
    return (ROOT / path.lstrip('/') / 'index.html').read_text()

class SEO(unittest.TestCase):
    def test_metadata_matrix(self):
        for path, title in TITLES.items():
            with self.subTest(path=path):
                p = Page(read(path))
                from html import unescape
                self.assertEqual([unescape(x) for x in re.findall(r'<title>(.*?)</title>', p.html)], [title])
                self.assertEqual(len(p.attrs('h1')), 1)
                self.assertEqual([a['href'] for a in p.attrs('link', rel='canonical')], [ORIGIN + path])
                desc = p.attrs('meta', name='description')
                self.assertEqual(len(desc), 1)
                self.assertTrue(desc[0]['content'].strip())
                self.assertEqual([a['content'] for a in p.attrs('meta', name='robots')],
                                 ['noindex, follow' if path == '/agb/' else 'index, follow'])
                self.assertFalse(p.attrs('meta', name='googlebot'))
    def test_sitemap_and_robots(self):
        tree = ElementTree.parse(ROOT / 'sitemap.xml')
        urls = [e.text for e in tree.findall('.//{*}loc')]
        self.assertCountEqual(urls, [ORIGIN + p for p in PAGES if p != '/agb/'])
        # Seit 21.09.2026 steht ein lastmod je URL. Es ist belegt: das Datum
        # des letzten Commits, der genau diese Datei geändert hat. Google wertet
        # lastmod aus, priority dagegen nicht.
        from datetime import date
        for url in tree.findall('.//{*}url'):
            loc = url.find('{*}loc').text
            stand = url.find('{*}lastmod')
            self.assertIsNotNone(stand, loc + ': lastmod fehlt')
            self.assertRegex(stand.text, r'^\d{4}-\d{2}-\d{2}$', loc)
            self.assertLessEqual(date.fromisoformat(stand.text), date.today(),
                                 loc + ': lastmod liegt in der Zukunft')
        self.assertFalse(tree.findall('.//{*}priority'), 'priority wertet Google nicht aus')
        robots = (ROOT / 'robots.txt').read_text()
        self.assertIn('Sitemap: ' + ORIGIN + '/sitemap.xml', robots)
        self.assertNotRegex(robots, r'(?im)^Disallow:\s*/')
        # Antwortmaschinen sind ausdrücklich zugelassen. Wer hier sperrt,
        # verschwindet aus den Antworten von ChatGPT, Claude und Perplexity.
        for bot in ['GPTBot', 'OAI-SearchBot', 'ClaudeBot', 'PerplexityBot',
                    'Google-Extended', 'Applebot-Extended']:
            self.assertIn('User-agent: ' + bot, robots)
    def test_internal_links_resources_and_drafts(self):
        reached = set()
        for path in PAGES:
            p = Page(read(path))
            for tag, attrs in p.tags:
                value = attrs.get('href') if tag in ('a', 'link') else attrs.get('src') if tag in ('script', 'img', 'source') else None
                if not value or value.startswith(('data:', 'mailto:', 'tel:')):
                    continue
                url = urlsplit(urljoin(ORIGIN + path, value))
                if url.netloc != urlsplit(ORIGIN).netloc:
                    continue
                target = ROOT / unquote(url.path.lstrip('/'))
                if target.is_dir():
                    target = target / 'index.html'
                self.assertTrue(target.is_file(), (path, value))
                if tag == 'a':
                    self.assertNotIn('index.html', value)
                    self.assertNotRegex(value, r'drafts|entwurf|docs/|tests/')
                    reached.add(url.path)
                    if url.fragment:
                        self.assertTrue(Page(target.read_text()).attrs('div', id=url.fragment) or
                                        any(a.get('id') == url.fragment for t, a in Page(target.read_text()).tags), value)
        self.assertTrue(set(PAGES) <= reached)
        self.assertCountEqual([p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*.html')],
                              [p.lstrip('/') + 'index.html' for p in PAGES])
    def test_jsonld_and_social(self):
        p = Page(read('/'))
        blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', p.html, re.S)
        # Seit 21.09.2026 ein einziger Graph je Seite. Lose Blöcke nebeneinander
        # werden zwar gelesen, zeigen aber keine Verbindung zwischen Marke,
        # Person und Leistung.
        self.assertEqual(len(blocks), 1)
        graph = json.loads(blocks[0])['@graph']
        stuecke = {s['@type']: s for s in graph}
        data = stuecke['Organization']
        faq = stuecke['FAQPage']
        for art in ['Organization', 'Person', 'WebSite', 'Service', 'BreadcrumbList', 'WebPage']:
            self.assertIn(art, stuecke, art + ' fehlt im Graph der Startseite')
        self.assertEqual(stuecke['Person']['name'], 'Ben Carstens')
        self.assertEqual(stuecke['Service']['provider']['@id'], data['@id'])
        # FAQ-Auszeichnung muss wortgleich zu den sichtbaren Antworten sein.
        self.assertEqual(faq['@type'], 'FAQPage')
        self.assertEqual(len(faq['mainEntity']), 8)
        from html import unescape as _u
        sichtbar = re.sub(r'<[^>]+>', '', p.html)
        sichtbar = re.sub(r'\s+', ' ', _u(sichtbar))
        for eintrag in faq['mainEntity']:
            self.assertIn(eintrag['name'], sichtbar)
            self.assertIn(eintrag['acceptedAnswer']['text'][:60], sichtbar)
        self.assertEqual(data['url'], ORIGIN + '/')
        self.assertEqual(data['name'], 'Laboraquise.de')
        self.assertIn('Ben Carstens', read('/impressum/'))
        self.assertNotRegex(blocks[0], r'AggregateRating|Dentist|MedicalOrganization')
        for key in ['og:title', 'og:description', 'og:url', 'og:image']:
            self.assertEqual(len(p.attrs('meta', property=key)), 1)
        self.assertEqual(p.attrs('meta', property='og:url')[0]['content'], ORIGIN + '/')
        self.assertEqual(p.attrs('meta', property='og:title')[0]['content'], TITLES['/'])
        self.assertEqual(p.attrs('meta', property='og:description')[0]['content'], p.attrs('meta', name='description')[0]['content'])
    def test_cta_is_crawlable(self):
        p = Page(read('/'))
        links = p.attrs('a', **{'data-modal_1-trigger': 'item-1'})
        self.assertGreater(len(links), 0)
        self.assertTrue(all(a.get('href') == '/termin/' and a.get('aria-label') == 'Erstgespräch vereinbaren' for a in links))
        for name in ['Name', 'E-Mail', 'Telefonnummer', 'Unternehmen']:
            self.assertEqual(len(p.attrs('label', **{'for': name})), 1)
    def test_published_knowledge(self):
        seiten = [('/wissen/', 'CollectionPage')]
        seiten += [(p, 'Article') for p in PAGES if p.startswith('/wissen/') and p != '/wissen/']
        self.assertEqual(len(seiten), 9, 'Alle Wissensseiten werden geprüft')
        for path, kind in seiten:
            p = Page(read(path))
            self.assertNotIn('Lokale Vorschau', p.html)
            blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', p.html, re.S)
            self.assertEqual(len(blocks), 1)
            graph = json.loads(blocks[0])['@graph']
            stuecke = {s['@type']: s for s in graph}
            self.assertIn(kind, stuecke)
            self.assertEqual(stuecke[kind]['url'], ORIGIN + path)
            crumbs = stuecke['BreadcrumbList']['itemListElement']
            self.assertEqual(crumbs[-1]['item'], ORIGIN + path)
            self.assertEqual([c['position'] for c in crumbs], list(range(1, len(crumbs) + 1)))
            self.assertNotRegex(blocks[0], r'AggregateRating')
            if kind == 'Article':
                # Autor und Datum sind belegt: Ben Carstens steht im Impressum,
                # die Daten erzeugt werkzeuge/seo_ausbau.py aus der
                # Versionsgeschichte der Datei, nicht aus einer Annahme.
                from datetime import date
                artikel = stuecke['Article']
                self.assertEqual(artikel['author']['@id'], ORIGIN + '/#ben-carstens')
                self.assertEqual(artikel['publisher']['@id'], ORIGIN + '/#organisation')
                for feld in ['datePublished', 'dateModified']:
                    self.assertRegex(artikel.get(feld, ''), r'^\d{4}-\d{2}-\d{2}$', path + ': ' + feld)
                    self.assertLessEqual(date.fromisoformat(artikel[feld]), date.today(), path)
                self.assertLessEqual(artikel['datePublished'], artikel['dateModified'], path)
            for crumb in crumbs:
                self.assertTrue(p.attrs('a', href=urlsplit(crumb['item']).path) or crumb == crumbs[-1])
            for key in ['og:title', 'og:description', 'og:url', 'og:image']:
                self.assertEqual(len(p.attrs('meta', property=key)), 1)
            self.assertEqual(p.attrs('meta', property='og:url')[0]['content'], ORIGIN + path)
            brand_image = ORIGIN + '/assets/69ce12160e49568ac435ef6a/laboraquise-icon-512-v2.png'
            self.assertEqual(p.attrs('meta', property='og:image')[0]['content'], brand_image)
            self.assertEqual(p.attrs('meta', name='twitter:image')[0]['content'], brand_image)
        # Jede Artikelseite braucht eine abhakbare Liste und einen Weg zum Erstgespräch
        # im Artikeltext selbst. Ein Link allein in der Navigation zählt nicht: Seiten
        # ohne Handlungsaufruf im Text holen Besucher, ohne dass daraus etwas wird.
        for path, _ in seiten[1:]:
            html = read(path)
            seite = Page(html)
            self.assertGreaterEqual(len(seite.attrs('input', type='checkbox')), 4, path)
            artikel = html[html.index('<article'):html.index('</article>')]
            self.assertIn('href="/termin/"', artikel, path + ': kein Weg zum Erstgespräch im Artikel')
            self.assertIn('Erstgespräch vereinbaren', artikel, path)
        article = read('/wissen/warum-zahnaerzte-das-dentallabor-wechseln/')
        self.assertEqual(len(Page(article).attrs('input', type='checkbox')), 8)
        self.assertIn('10.1186/s12903-023-03395-z', article)
        self.assertTrue(Page(read('/')).attrs('a', href='/wissen/'))
    def test_keine_cookies_kein_hinweis(self):
        # Seit 15.09.2026: kein Cookie-Hinweis, keine Einwilligungsbibliothek, kein eigener
        # Cookie. Die Datenschutzerklaerung sagt genau das, also muss es so bleiben.
        for path in PAGES:
            with self.subTest(path=path):
                html = read(path)
                self.assertNotIn('fs-cc=', html)
                self.assertNotIn('fs-cc.js', html)
                self.assertNotIn('cookie-consent', html)
                self.assertNotIn('document.cookie', html)
        self.assertIn('Diese Website setzt keine Cookies', read('/datenschutz/'))
        self.assertFalse(list((ROOT / 'assets').rglob('fs-cc*')))
    def test_klick_kennung_erreicht_calendly(self):
        # Seit 16.09.2026: Die Klick-Kennung von Google Ads (gclid, gbraid,
        # wbraid) wandert von der Zielseite ueber /termin/ bis in die
        # Calendly-Buchung. Ohne sie laeuft die Anzeigenkampagne blind, weil
        # keine Buchung ihrem Klick zugeordnet werden kann. Sie faehrt nur in
        # der Adresse mit, deshalb bleibt die Seite ohne Cookie.
        skript = (ROOT / 'assets' / 'js' / 'klick-id.js').read_text(encoding='utf-8')
        for name in ['gclid', 'gbraid', 'wbraid']:
            self.assertIn(name, skript)
        self.assertNotIn('document.cookie', skript)
        self.assertNotIn('localStorage', skript)
        for path in [p for p in PAGES if p not in ('/termin/', '/impressum/', '/datenschutz/', '/agb/')]:
            with self.subTest(path=path):
                self.assertIn('/assets/js/klick-id.js', read(path).replace('"assets/js/', '"/assets/js/'))
        termin = read('/termin/')
        self.assertIn('gclid', termin)
        self.assertIn('utm_term', termin)
    def test_entitaet_ist_ueberall_gleich(self):
        # Eine Antwortmaschine baut sich aus vielen Seiten ein Bild davon, wer
        # hier schreibt. Steht es auf jeder Seite anders, entsteht kein Bild.
        # Deshalb: dieselben Kennungen, dieselben Werte, auf jeder Seite.
        from urllib.parse import urlsplit
        referenz = None
        for path in PAGES:
            with self.subTest(path=path):
                blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>',
                                    read(path), re.S)
                self.assertEqual(len(blocks), 1, path + ': genau ein Graph je Seite')
                graph = json.loads(blocks[0])['@graph']
                stuecke = {s['@type']: s for s in graph}
                for art in ['Organization', 'Person', 'WebSite', 'Service', 'BreadcrumbList']:
                    self.assertIn(art, stuecke, path + ': ' + art + ' fehlt')
                kern = {a: stuecke[a] for a in ['Organization', 'Person', 'WebSite', 'Service']}
                if referenz is None:
                    referenz = kern
                else:
                    self.assertEqual(kern, referenz, path + ': Entität weicht ab')
                # Jeder Verweis muss im Graph aufgehen. Ein @id ins Leere ist
                # schlimmer als gar keiner: er behauptet eine Verbindung.
                kennungen = {s.get('@id') for s in graph}
                verweise = set(re.findall(r'"@id":"([^"]+)"', json.dumps(graph)))
                self.assertFalse(verweise - kennungen, path + ': Verweis ins Leere')
        self.assertEqual(referenz['Organization']['address']['streetAddress'],
                         'Eppendorfer Weg 168')
        self.assertIn('Eppendorfer Weg 168', read('/impressum/'))

    def test_llms_txt(self):
        kurz = (ROOT / 'llms.txt').read_text()
        lang = (ROOT / 'llms-full.txt').read_text()
        self.assertTrue(kurz.startswith('# Laboraquise.de'))
        # Jede oeffentliche Seite ausser den Rechtstexten steht drin.
        for path in PAGES:
            if path in ('/agb/', '/impressum/', '/datenschutz/'):
                continue
            self.assertIn(ORIGIN + path, kurz, path + ' fehlt in llms.txt')
            self.assertIn(ORIGIN + path, lang, path + ' fehlt in llms-full.txt')
        # Die Grenzen des Versprechens stehen dort, wo ein Modell sie liest.
        self.assertIn('Neue Kunden oder Umsatz sind nicht zugesagt', kurz)
        self.assertIn('ZDH-Statistik', kurz)
        # Keine Gedankenstriche, wie im gesamten sichtbaren Text.
        for name, inhalt in [('llms.txt', kurz), ('llms-full.txt', lang)]:
            self.assertNotIn('\u2014', inhalt, name)
            self.assertNotIn(' \u2013 ', inhalt, name)

    def test_http_preview_and_production_simulation(self):
        for production in [False, True]:
            handler = type('TestHandler', (Handler,), {'production': production})
            server = ThreadingHTTPServer(('127.0.0.1', 0), handler)
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            base = 'http://127.0.0.1:' + str(server.server_port)
            try:
                for path in [*PAGES, '/sitemap.xml', '/robots.txt', '/llms.txt', '/llms-full.txt', '/assets/og-image-marke.jpg', '/assets/fonts/general-sans.css', '/assets/js/lenis.min.js']:
                    with urlopen(base + path) as response:
                        response.read()
                        self.assertEqual(response.status, 200)
                        self.assertEqual(response.headers.get('X-Robots-Tag'), None if production else 'noindex, nofollow')
                # Ausschluss gilt nur für diesen lokalen Server, nicht für GitHub Pages.
                for path in ['/unbekannt-seo/', '/docs/seo/PLAN.md', '/tests/test_seo.py', '/entwurf/', '/assets/', '/assets/../../.git', '/assets/%2e%2e/docs/seo/PLAN.md', '/assets/%2e%2e/tests/test_seo.py']:
                    with self.assertRaises(HTTPError) as error:
                        urlopen(base + path)
                    self.assertEqual(error.exception.code, 404)
                with urlopen(base + '/termin?utm_source=test') as response:
                    response.read()
                    self.assertEqual(response.url, base + '/termin/?utm_source=test')
            finally:
                server.shutdown()
                server.server_close()
                thread.join()

if __name__ == '__main__':
    unittest.main()
