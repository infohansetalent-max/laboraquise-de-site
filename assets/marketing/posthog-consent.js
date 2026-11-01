(function () {
  'use strict';
  var box = document.querySelector('[data-posthog-consent]');
  if (!box || !window.LjsPostHog) return;
  var panel = box.querySelector('[data-privacy-panel]');
  var launcher = box.querySelector('[data-privacy-open]');
  var statistic = box.querySelector('[data-privacy-statistik]');
  var advertising = box.querySelector('[data-privacy-werbung]');
  var externalOpeners = document.querySelectorAll('[data-hinweis-oeffnen]');
  var decidedHere = false;
  function ads() { return advertising && window.LjsWerbung; }
  function update() {
    var available = window.LjsPostHog.available();
    box.hidden = !available;
    launcher.hidden = externalOpeners.length > 0;
    statistic.checked = window.LjsPostHog.consent() === 'yes';
    if (ads()) advertising.checked = ads().consent() === 'ja';
    if (!decidedHere && available) {
      var unanswered = !window.LjsPostHog.consent() || (ads() && !ads().consent());
      panel.hidden = !unanswered;
    }
  }
  function choose(statistics, marketing) {
    decidedHere = true;
    if (statistics) window.LjsPostHog.allow(); else window.LjsPostHog.decline();
    if (ads()) ads().choose(marketing ? 'ja' : 'nein');
    panel.hidden = true;
    box.querySelector('[data-privacy-details]').open = false;
    update();
  }
  function open() {
    update();
    panel.hidden = false;
    panel.querySelector('[data-posthog-decline]').focus();
  }
  launcher.addEventListener('click', open);
  externalOpeners.forEach(function (button) { button.addEventListener('click', open); });
  box.querySelector('[data-posthog-allow]').addEventListener('click', function () { choose(true, true); });
  box.querySelector('[data-posthog-decline]').addEventListener('click', function () { choose(false, false); });
  box.querySelector('[data-privacy-save]').addEventListener('click', function () { choose(statistic.checked, advertising ? advertising.checked : false); });
  window.addEventListener('ljs:posthog-consent', update);
  window.addEventListener('ljs:werbung-bereit', update);
  update();
})();
