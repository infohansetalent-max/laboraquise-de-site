/* Reine Tageszählung auf eigenen Seiten. Feste Herkunftskategorie, keine Besucherkennung. */
(function () {
  'use strict';
  var script = document.currentScript;
  if (!script) return;
  var website = script.getAttribute('data-website');
  var seite = script.getAttribute('data-seite');
  if (['lokalejobsuche.de', 'laboraquise.de'].indexOf(website) < 0 || !seite) return;
  if (website === 'lokalejobsuche.de' && /^\/stellen-marktcheck\/[^/]+$/.test(seite)) seite = '/stellen-marktcheck/[betrieb]';
  if ([website, 'www.' + website].indexOf(location.hostname) < 0) return;
  if (new URLSearchParams(location.search).has('ljs_tracking_test') || window.LjsBesuch?.ausgeschlossen()) return;
  // Nur feste Werte aus dem HTML. Keine URL, Parameter oder Geräteangaben versenden.
  try {
    fetch('https://portal.lokalejobsuche.de/api/funnels/seitenaufruf', {
      method: 'POST', headers: { 'Content-Type': 'text/plain' },
      body: JSON.stringify({ website: website, seite: seite, herkunft: window.LjsBesuch?.herkunft() || 'unbekannt' }),
      credentials: 'omit', referrerPolicy: 'no-referrer', cache: 'no-store', keepalive: true
    }).catch(function () {});
  } catch (_) { /* Ein Zählfehler darf die Seite nicht beeinträchtigen. */ }
})();
