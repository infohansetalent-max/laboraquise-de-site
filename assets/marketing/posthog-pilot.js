/* Freiwillige Statistik für laboraquise.de. Abgeleitet aus dem Messclient
   für lokalejobsuche.de, mit eigener Einwilligung und Browserkennung. Keine Formularwerte, URLs, Replays oder Werbe-IDs. */
(function () {
  'use strict';
  if (window.LjsPostHog && window.LjsPostHog.version === 2) return;
  if (window.LjsPostHog) { try { window.LjsPostHog.decline(); } catch (_) { /* Alte Einwilligung gilt nicht für den neuen Umfang. */ } }
  var CONSENT = 'lba-ph-consent-v2';
  var VISITOR = 'lba-ph-visitor-v2';
  var ENTRY = 'lba-ph-entry-v2';
  var CHANNEL = 'lba-ph-channel-v1';
  var UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
  var config = { enabled: false, projectKey: '', audience: '', contentId: '' };
  var sdk = null, loading = false, pending = [], seen = new Set();
  var channels = ['google', 'meta', 'email', 'organic', 'referral', 'unknown'];
  var events = ['landing_viewed', 'cta_clicked', 'check_started', 'check_step_completed', 'lead_submitted', 'appointment_booked', 'funnel_error', 'page_viewed', 'link_clicked', 'form_started', 'form_submit_attempted', 'application_started', 'application_step_completed', 'application_submitted'];

  function cookie(name) {
    try {
      var found = document.cookie.split(';').map(function (v) { return v.trim(); }).find(function (v) { return v.indexOf(name + '=') === 0; });
      return found ? found.slice(name.length + 1) : '';
    } catch (_) { return ''; }
  }
  function write(name, value, seconds) {
    try { document.cookie = name + '=' + value + '; Path=/; Domain=laboraquise.de; Max-Age=' + seconds + '; SameSite=Lax; Secure'; } catch (_) { /* Keine Ersatzspeicherung. */ }
  }
  var pages = ["/agb", "/datenschutz", "/impressum", "/", "/rueckruf", "/termin", "/wissen/dentallabor-gruenden", "/wissen/dentallabor-kaufen-oder-uebernehmen", "/wissen/eigenlabor-und-praxislabor", "/wissen", "/wissen/kundenakquise-im-dentallabor", "/wissen/preise-und-stundensatz-im-dentallabor", "/wissen/warum-zahnaerzte-das-dentallabor-wechseln", "/wissen/zahntechnik-in-zahlen"];
  function page() {
    var host = window.location.hostname;
    var path = window.location.pathname.replace(/\/$/, '') || '/';
    if (new URLSearchParams(window.location.search).has('ljs_tracking_test') || !/^(www\.)?laboraquise\.de$/.test(host) || pages.indexOf(path) < 0) return null;
    return { path: path, surface: path === '/termin' ? 'booking' : 'landing', audience: /^(\/agb|\/impressum|\/datenschutz)/.test(path) ? 'general' : 'employer' };
  }
  function context() { var value = page(); return value ? value.surface : ''; }
  function enabled() { return config.enabled === true && /^phc_[a-zA-Z0-9_-]{10,}$/.test(config.projectKey) && !!context(); }
  function permitted() { return enabled() && window.navigator.doNotTrack !== '1' && cookie(CONSENT) === 'yes'; }
  function channel() {
    var stored = cookie(CHANNEL);
    if (channels.indexOf(stored) >= 0) return stored;
    var params = new URLSearchParams(window.location.search);
    var source = (params.get('utm_source') || '').toLowerCase();
    var medium = (params.get('utm_medium') || '').toLowerCase();
    if (/^(google|googleads|adwords)$/.test(source)) return 'google';
    if (/^(facebook|instagram|fb|ig|meta)$/.test(source)) return 'meta';
    if (/^(instantly|email|newsletter)$/.test(source) || medium === 'email') return 'email';
    try {
      var ref = new URL(document.referrer).hostname;
      if (/(^|\.)(google\.[a-z.]+|bing\.com|duckduckgo\.com)$/.test(ref)) return 'organic';
      if (ref && !/(^|\.)laboraquise\.de$/.test(ref)) return 'referral';
    } catch (_) { /* Fehlender Verweis ist keine belegte Direktquelle. */ }
    return 'unknown';
  }
  function properties(name, raw) {
    raw = raw || {};
    var current = page();
    if (!current) return null;
    var entry = cookie(ENTRY);
    var props = { pilot: 'lba-website-v1', site: 'laboraquise.de', audience: current.audience, page_path: current.path, surface: context(), entry_page: pages.indexOf(entry) >= 0 ? entry : current.path, source_channel: channel(), device_type: window.matchMedia('(max-width: 767px)').matches ? 'mobile' : 'desktop' };
    if (UUID.test(config.contentId) && current.audience === 'applicant') props.content_id = config.contentId;
    if (name === 'check_step_completed' || name === 'application_step_completed') {
      if (!Number.isInteger(raw.step) || raw.step < 1 || raw.step > (name === 'application_step_completed' ? 50 : 6)) return null;
      props.step = raw.step;
    }
    if (name === 'cta_clicked') props.cta = ['preview', 'start', 'booking', 'apply', 'phone', 'email'].indexOf(raw.cta) >= 0 ? raw.cta : 'start';
    if (name === 'link_clicked') props.target_type = ['internal', 'external', 'phone', 'email'].indexOf(raw.target_type) >= 0 ? raw.target_type : 'internal';
    if (name === 'funnel_error') {
      if (['validation', 'network', 'server', 'invalid_response'].indexOf(raw.code) < 0) return null;
      props.code = raw.code;
      if (Number.isInteger(raw.step) && raw.step >= 1 && raw.step <= 6) props.step = raw.step;
    }
    return props;
  }
  function beforeSend(event) {
    if (!permitted() || !event || events.indexOf(event.event) < 0) return null;
    var clean = properties(event.event, event.properties);
    var id = cookie(VISITOR);
    if (!clean || !UUID.test(id)) return null;
    // Positive Liste statt nachträglicher Entfernung einzelner PII-Felder.
    // Auch automatisch vom SDK ergänzte URL-, Referrer- und Profilwerte entfallen.
    event.properties = Object.assign(clean, { token: config.projectKey, distinct_id: id, $process_person_profile: false, $ip: null, $geoip_disable: true });
    return event;
  }
  function once(name, raw, key) {
    var current = page();
    key = current ? current.path + ':' + config.contentId + ':' + key : key;
    if (!permitted() || seen.has(key)) return;
    var props = properties(name, raw);
    if (!props || events.indexOf(name) < 0) return;
    seen.add(key);
    if (sdk) send(name, props);
    else if (pending.length < 32) pending.push([name, props]);
  }
  function send(name, props) {
    try { sdk.capture(name, props); } catch (_) { /* Messfehler dürfen keine Anfrage unterbrechen. */ }
  }
  function changed() { window.dispatchEvent(new CustomEvent('ljs:posthog-consent')); }
  function start() {
    if (!permitted()) return;
    var id = cookie(VISITOR);
    if (!UUID.test(id)) {
      try { id = window.crypto.randomUUID(); } catch (_) { return; }
      write(VISITOR, id, 7776000);
    }
    if (!UUID.test(cookie(VISITOR))) return; // Gesperrte Cookies: keine Ersatzkennung.
    if (!cookie(ENTRY)) write(ENTRY, page().path, 86400);
    write(CHANNEL, channel(), 86400);
    once('page_viewed', {}, 'page');
    if (context() === 'landing' && page().audience === 'employer') once('landing_viewed', {}, 'landing');
    if (sdk || loading) return;
    loading = true;
    var script = document.createElement('script');
    script.src = '/marketing/posthog-1.444.0.no-external.js';
    if (window.location.hostname !== 'portal.laboraquise.de') script.src = '/assets/marketing/posthog-1.444.0.no-external.js';
    script.async = true;
    script.onerror = function () { loading = false; pending = []; seen.clear(); };
    script.onload = function () {
      loading = false;
      if (!permitted() || !window.posthog) { pending = []; return; }
      try { window.posthog.init(config.projectKey, {
        api_host: 'https://eu.i.posthog.com', ui_host: 'https://eu.posthog.com',
        bootstrap: { distinctID: cookie(VISITOR), isIdentifiedID: false },
        persistence: 'memory', disable_persistence: true, person_profiles: 'never',
        autocapture: false, capture_pageview: false, capture_pageleave: false,
        capture_dead_clicks: false, capture_heatmaps: false, rageclick: false,
        capture_performance: false, capture_exceptions: false,
        disable_session_recording: true, enable_recording_console_log: false,
        session_recording: { maskAllInputs: true, maskTextSelector: '*', blockSelector: 'form, [data-ph-private]' },
        disable_surveys: true, disable_conversations: true, disable_product_tours: true,
        disable_web_experiments: true, disable_external_dependency_loading: true,
        advanced_disable_flags: true, save_campaign_params: false, save_referrer: false,
        advanced_disable_feature_flags: true, advanced_disable_toolbar_metrics: true,
        request_batching: false, ip: false, respect_dnt: true,
        before_send: beforeSend,
        loaded: function (client) {
          sdk = client;
          // Eine frühere Ablehnung im SDK darf die neue, ausdrückliche
          // Zustimmung nach einem Seitenwechsel nicht dauerhaft sperren.
          client.opt_in_capturing({ captureEventName: false });
          var batch = pending; pending = [];
          batch.forEach(function (item) { if (permitted()) send(item[0], item[1]); });
        }
      }, 'lbaWebsite'); } catch (_) { sdk = null; pending = []; seen.clear(); }
    };
    document.head.appendChild(script);
  }
  function decline() {
    // Auch auf der Landingpage widerrufen, wenn der Pilot später abgeschaltet ist.
    if (!/^(www\.)?laboraquise\.de$/.test(window.location.hostname)) return;
    write(CONSENT, 'no', 15552000);
    write('lba-ph-consent-v1', 'no', 15552000);
    [VISITOR, ENTRY, CHANNEL, 'lba-ph-visitor-v1', 'lba-ph-entry-v1'].forEach(function (name) { write(name, '', 0); });
    pending = []; seen.clear();
    if (sdk) { try { sdk.stopSessionRecording(); sdk.opt_out_capturing(); } catch (_) { /* Die eigene Zustimmungssperre gilt trotzdem. */ } }
    changed();
  }
  window.LjsPostHog = {
    version: 2,
    configure: function (next) { config = { enabled: next.enabled === true, projectKey: next.projectKey || '', audience: next.audience || '', contentId: next.contentId || '' }; start(); changed(); },
    available: enabled,
    consent: function () { return cookie(CONSENT); },
    allow: function () {
      if (!enabled() || window.navigator.doNotTrack === '1') return;
      write(CONSENT, 'yes', 15552000);
      write('lba-ph-consent-v1', 'no', 15552000);
      if (sdk) { try { sdk.opt_in_capturing({ captureEventName: false }); } catch (_) { /* SDK-Ausfall blockiert keinen Kontakt. */ } }
      start(); changed();
    },
    decline: decline,
    started: function () { if (context() === 'check') once('check_started', {}, 'started'); },
    step: function (step) { if (context() === 'check') once('check_step_completed', { step: step }, 'step:' + step); },
    lead: function (response, httpOk) {
      if (!page() || page().audience !== 'employer' || !httpOk || !response || response.ok !== true || response.doppelt || !UUID.test(response.eingang_id || '')) return;
      if (context() === 'check') once('check_step_completed', { step: 6 }, 'step:6');
      once('lead_submitted', {}, 'lead:' + response.eingang_id);
    },
    booked: function (response, httpOk) {
      if (context() !== 'booking' || !httpOk || !response || response.ok !== true || typeof response.token !== 'string' || !/^[a-zA-Z0-9_-]{16,512}$/.test(response.token) || !response.beginn || !Number.isFinite(Date.parse(response.beginn))) return;
      once('appointment_booked', {}, 'booking:' + response.token);
    },
    embeddedBooked: function (begin) {
      if (context() !== 'booking' || typeof begin !== 'string' || !Number.isFinite(Date.parse(begin))) return;
      once('appointment_booked', {}, 'embedded-booking:' + begin);
    },
    applicationStarted: function () { if (page() && page().audience === 'applicant') once('application_started', {}, 'application-started'); },
    applicationStep: function (step) { if (page() && page().audience === 'applicant') once('application_step_completed', { step: step }, 'application-step:' + step); },
    applicationSubmitted: function (response, httpOk) {
      if (!page() || page().audience !== 'applicant' || !httpOk || !response || response.ok !== true || response.doppelt || !UUID.test(response.eingang_id || '')) return;
      once('application_submitted', {}, 'application:' + response.eingang_id);
    },
    error: function (code, step) { once('funnel_error', { code: code, step: step }, 'error:' + code + ':' + step); }
  };
  document.addEventListener('click', function (event) {
    if (!page()) return;
    var link = event.target.closest ? event.target.closest('a[href]') : null;
    if (!link) return;
    var href = link.getAttribute('href') || '';
    var type = /^tel:/.test(href) ? 'phone' : /^mailto:/.test(href) ? 'email' : 'internal';
    try { if (type === 'internal' && new URL(href, window.location.href).hostname !== window.location.hostname) type = 'external'; } catch (_) { return; }
    once('link_clicked', { target_type: type }, 'link:' + type);
    // Nur feste Zielkategorien, niemals Linktext oder freie Zieladressen.
    var cta = link.hasAttribute('data-weiter') ? 'preview' : /\/start(?:[?#]|$)/.test(href) ? 'start' : /\/buchen\/laboraquise/.test(href) || /\/termin\/?(?:[?#]|$)/.test(href) ? 'booking' : link.hasAttribute('data-startlink') ? 'start' : '';
    if (cta) once('cta_clicked', { cta: cta }, 'cta:' + cta);
  }, { capture: true });
  document.addEventListener('focusin', function (event) {
    if (!page() || !event.target.closest || !event.target.closest('form')) return;
    once('form_started', {}, 'form-started');
    if (page().audience === 'applicant') window.LjsPostHog.applicationStarted();
  });
  document.addEventListener('submit', function () { if (page()) once('form_submit_attempted', {}, 'form-submit-attempted'); }, { capture: true });
  // Cookie-Entscheidungen gelten in beiden Ursprüngen. Jeder Versand prüft sie
  // erneut, auch nach einem Widerruf im anderen Tab oder in der Einbettung.
  window.addEventListener('focus', function () { if (permitted()) start(); changed(); });
  if (window.LjsPostHogConfig) window.LjsPostHog.configure(window.LjsPostHogConfig);
})();
