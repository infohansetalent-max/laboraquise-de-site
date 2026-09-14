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
    '/impressum/': 'Impressum | Laboraquise.de',
    '/datenschutz/': 'Datenschutzerklärung | Laboraquise.de',
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
        self.assertFalse(tree.findall('.//{*}lastmod'), 'Kein unbelegtes Änderungsdatum')
        robots = (ROOT / 'robots.txt').read_text()
        self.assertIn('Sitemap: ' + ORIGIN + '/sitemap.xml', robots)
        self.assertNotRegex(robots, r'(?im)^Disallow:\s*/')
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
        self.assertEqual(len(blocks), 1)
        data = json.loads(blocks[0])
        self.assertEqual(data['@type'], 'Organization')
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
    def test_http_preview_and_production_simulation(self):
        for production in [False, True]:
            handler = type('TestHandler', (Handler,), {'production': production})
            server = ThreadingHTTPServer(('127.0.0.1', 0), handler)
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            base = 'http://127.0.0.1:' + str(server.server_port)
            try:
                for path in [*PAGES, '/sitemap.xml', '/robots.txt', '/assets/og-image-marke.jpg', '/assets/fonts/general-sans.css', '/assets/js/lenis.min.js']:
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
