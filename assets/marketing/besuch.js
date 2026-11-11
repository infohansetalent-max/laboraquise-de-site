/* Gemeinsame Herkunft und eigener Testmodus. Es werden keine Besucherkennungen angelegt. */
(function () {
  'use strict';
  if (window.LjsBesuch) return;
  var host = location.hostname;
  var laboraquise = /(^|\.)laboraquise\.de$/.test(host);
  var domain = laboraquise ? 'laboraquise.de' : 'lokalejobsuche.de';
  var eigeneHosts = laboraquise
    ? ['laboraquise.de', 'www.laboraquise.de', 'portal.lokalejobsuche.de']
    : ['lokalejobsuche.de', 'www.lokalejobsuche.de', 'portal.lokalejobsuche.de'];
  if (eigeneHosts.indexOf(host) < 0) return;
  var cookieName = 'ljs-eigene-aufrufe-v1';
  var namen = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'utm_id'];

  function cookie() {
    try { return document.cookie.split(';').some(function (part) { return part.trim() === cookieName + '=1'; }); }
    catch (_) { return false; }
  }
  function eigene(aktiv) {
    try {
      document.cookie = cookieName + '=' + (aktiv ? '1' : '') + '; Path=/; Domain=' + domain +
        '; Max-Age=' + (aktiv ? 31536000 : 0) + '; SameSite=Lax; Secure';
    } catch (_) { /* Der URL-Testmarker funktioniert auch bei gesperrten Cookies. */ }
  }
  var start = new URLSearchParams(location.search);
  if (start.get('ljs_tracking_intern') === '1') eigene(true);
  if (start.get('ljs_tracking_intern') === '0') eigene(false);

  function ausgeschlossen() {
    var params = new URLSearchParams(location.search);
    return params.has('ljs_tracking_test') || params.get('ljs_tracking_intern') === '1' || cookie() ||
      (typeof navigator !== 'undefined' && navigator.webdriver === true);
  }
  function verweis() {
    try { return new URL(document.referrer).hostname.toLowerCase(); }
    catch (_) { return ''; }
  }
  function parameter() {
    var params = new URLSearchParams(location.search);
    var result = {};
    namen.forEach(function (name) {
      var value = params.get(name);
      if (value && value.trim() && !/[\r\n@]/.test(value)) result[name] = value.trim().slice(0, 160);
    });
    if (['gclid', 'gbraid', 'wbraid'].some(function (name) { return params.has(name); })) {
      result.utm_source = 'google'; result.utm_medium = 'cpc';
    } else if (!result.utm_source && !result.utm_medium) {
      var ref = verweis();
      if (params.has('fbclid')) {
        result.utm_source = 'facebook'; result.utm_medium = 'social';
      } else if (/(^|\.)google\.[a-z.]+$/.test(ref)) {
        result.utm_source = 'google'; result.utm_medium = 'organic';
      } else if (/(^|\.)(facebook\.com|fb\.com|fb\.me|instagram\.com|threads\.net|messenger\.com)$/.test(ref)) {
        result.utm_source = 'meta'; result.utm_medium = 'social';
      } else if (/(^|\.)(linkedin\.com|lnkd\.in)$/.test(ref)) {
        result.utm_source = 'linkedin'; result.utm_medium = 'social';
      } else if (ref && eigeneHosts.indexOf(ref) < 0) {
        result.utm_source = 'referral'; result.utm_medium = 'referral';
      }
    }
    if (ausgeschlossen()) result.ljs_tracking_test = '1';
    return result;
  }
  function herkunft() {
    var p = parameter();
    var source = (p.utm_source || '').toLowerCase();
    var medium = (p.utm_medium || '').toLowerCase();
    if (/^(google|googleads|adwords)$/.test(source) && /^(cpc|ppc|paid|paidsearch)$/.test(medium)) return 'google_ads';
    if (/^(instantly|email|e-mail|mail|newsletter|kaltmail)$/.test(source) || /^(email|e-mail|mail|newsletter)$/.test(medium)) return 'mail';
    if (/^(facebook|fb|instagram|ig|meta|threads|messenger|an|audience_network)$/.test(source)) return 'meta';
    if (/^(linkedin|lnkd)$/.test(source)) return 'linkedin';
    if (/^google/.test(source)) return 'google';
    if (source || medium) return 'andere';
    return eigeneHosts.indexOf(verweis()) >= 0 ? 'intern' : 'unbekannt';
  }
  function link(wert) {
    if (!wert || wert.charAt(0) === '#') return wert;
    try {
      var url = new URL(wert, location.href);
      if (url.protocol !== 'https:' || eigeneHosts.indexOf(url.hostname) < 0) return wert;
      if (/\.[a-z0-9]{2,5}$/i.test(url.pathname) || /^\/(admin|dashboard|api|email)(\/|$)/.test(url.pathname)) return wert;
      var p = parameter();
      var vorhandeneKampagne = namen.some(function (name) { return url.searchParams.has(name); });
      if (!vorhandeneKampagne) {
        namen.forEach(function (name) { if (p[name]) url.searchParams.set(name, p[name]); });
      } else if (!url.searchParams.has('utm_source') && !url.searchParams.has('utm_medium')) {
        ['utm_source', 'utm_medium'].forEach(function (name) { if (p[name]) url.searchParams.set(name, p[name]); });
      }
      if (p.ljs_tracking_test) url.searchParams.set('ljs_tracking_test', '1');
      return url.href;
    } catch (_) { return wert; }
  }
  window.LjsBesuch = { ausgeschlossen: ausgeschlossen, eigene: eigene, parameter: parameter, herkunft: herkunft, link: link };

  function aktualisiereLink(a) {
    var before = a.getAttribute('href');
    var after = link(before);
    if (before !== after) a.setAttribute('href', after);
  }
  function links(root) {
    root.querySelectorAll('a[href]').forEach(aktualisiereLink);
  }
  links(document);
  ['click', 'auxclick', 'contextmenu'].forEach(function (name) {
    document.addEventListener(name, function (event) {
      var a = event.target.closest && event.target.closest('a[href]');
      if (a) aktualisiereLink(a);
    }, { capture: true });
  });
  if (typeof MutationObserver !== 'undefined') {
    new MutationObserver(function (changes) {
      changes.forEach(function (change) {
        change.addedNodes.forEach(function (node) {
          if (node.nodeType !== 1) return;
          if (node.matches('a[href]')) aktualisiereLink(node);
          links(node);
        });
      });
    }).observe(document.documentElement, { childList: true, subtree: true });
  }
})();
