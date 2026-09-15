"""Lokale statische Vorschau. Keine Veröffentlichung und kein Produktionsserver."""
import argparse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = ('/', '/termin/', '/impressum/', '/datenschutz/', '/agb/', '/wissen/',
         '/wissen/warum-zahnaerzte-das-dentallabor-wechseln/',
         '/wissen/kundenakquise-im-dentallabor/',
         '/wissen/preise-und-stundensatz-im-dentallabor/',
         '/wissen/dentallabor-gruenden/',
         '/wissen/dentallabor-kaufen-oder-uebernehmen/',
         '/wissen/eigenlabor-und-praxislabor/',
         '/wissen/zahntechnik-in-zahlen/')

class Handler(SimpleHTTPRequestHandler):
    production = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def end_headers(self):
        if not self.production:
            self.send_header('X-Robots-Tag', 'noindex, nofollow')
        super().end_headers()

    def send_head(self):
        path = unquote(urlsplit(self.path).path)
        file = (ROOT / path.lstrip('/')).resolve()
        public_page = path in PAGES or path in [p + 'index.html' for p in PAGES]
        slash_redirect = path + '/' in PAGES
        resource = path in ('/robots.txt', '/sitemap.xml') or (
            path.startswith('/assets/') and file.is_relative_to(ROOT / 'assets')
        )
        if not file.is_relative_to(ROOT) or not (public_page or slash_redirect or resource):
            self.send_error(404, 'Seite nicht gefunden')
            return None
        # Keine Verzeichnislisten, auch nicht für Ressourcen.
        if file.is_dir() and resource:
            self.send_error(404, 'Seite nicht gefunden')
            return None
        return super().send_head()

    def log_message(self, *args):
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=4595)
    parser.add_argument('--production-simulation', action='store_true',
                        help='Nur lokale Prüfung der Produktions-HTML-Dateien ohne Preview-Header.')
    args = parser.parse_args()
    Handler.production = args.production_simulation
    print(f'Lokale {"Produktionssimulation" if Handler.production else "noindex-Vorschau"}: http://127.0.0.1:{args.port}', flush=True)
    ThreadingHTTPServer(('127.0.0.1', args.port), Handler).serve_forever()
