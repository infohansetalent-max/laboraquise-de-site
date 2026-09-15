/* Werkzeuge im Wissensbereich: Rechner, Kopierknopf, merkbare Prüflisten.
   Ohne Bibliothek, ohne externe Aufrufe. Faellt das Skript aus, bleiben
   Text, Links und Formular der Seite vollstaendig bedienbar. */
(function () {
  "use strict";

  var eur = new Intl.NumberFormat("de-DE", {
    style: "currency", currency: "EUR", maximumFractionDigits: 0 });
  var eur2 = new Intl.NumberFormat("de-DE", {
    style: "currency", currency: "EUR", minimumFractionDigits: 2, maximumFractionDigits: 2 });
  var num = new Intl.NumberFormat("de-DE", { maximumFractionDigits: 0 });

  function zahl(id) {
    var el = document.getElementById(id);
    if (!el) return 0;
    var w = parseFloat(String(el.value).replace(",", "."));
    return isFinite(w) && w >= 0 ? w : 0;
  }
  function setze(id, text) {
    var el = document.getElementById(id);
    if (el) el.textContent = text;
  }
  function binde(ids, fn) {
    var da = false;
    ids.forEach(function (id) {
      var el = document.getElementById(id);
      if (!el) return;
      da = true;
      el.addEventListener("input", fn);
      el.addEventListener("change", fn);
    });
    if (da) fn();
  }

  /* Bedarfsrechner: wie viele Praxen werden gebraucht */
  binde(["b-umsatz", "b-ziel", "b-abgang"], function () {
    var umsatz = zahl("b-umsatz"), ziel = zahl("b-ziel"), abgang = zahl("b-abgang");
    var jahr = umsatz * 12;
    var wachstum = jahr > 0 ? Math.ceil(ziel / jahr) : 0;
    setze("b-wachstum", num.format(wachstum));
    var gesamt = wachstum + Math.round(abgang);
    setze("b-gesamt", num.format(gesamt));
    /* Weg vom Ergebnis zur Anfrage: Zahl im Text, Zahl im Link */
    setze("b-anfrage-zahl", gesamt <= 0 ? "neue Praxen" : (gesamt === 1 ? "1 neue Praxis" : num.format(gesamt) + " neue Praxen"));
    setze("b-anfrage-label", gesamt <= 0 ? "Erstgespräch vereinbaren" : (gesamt === 1 ? "Erstgespräch zu 1 Praxis vereinbaren" : "Erstgespräch zu " + num.format(gesamt) + " Praxen vereinbaren"));
    var link = document.getElementById("b-anfrage-link");
    if (link) link.href = "/termin/?utm_source=laboraquise.de&utm_medium=rechner&utm_campaign=wissen-akquise&utm_content=" + Math.max(0, gesamt) + "-praxen";
  });

  /* Stundensatzrechner */
  binde(["s-kosten", "s-lohn", "s-koepfe", "s-stunden", "s-anteil"], function () {
    var kosten = zahl("s-kosten"), lohn = zahl("s-lohn");
    var koepfe = Math.max(1, Math.round(zahl("s-koepfe")));
    var stunden = zahl("s-stunden"), anteil = zahl("s-anteil");
    setze("s-anteil-wert", num.format(anteil));
    var verrechenbar = koepfe * stunden * (anteil / 100);
    setze("s-verrechenbar", num.format(Math.round(verrechenbar)));
    setze("s-satz", verrechenbar > 0 ? eur2.format((kosten + lohn) / verrechenbar) : "nicht berechenbar");
  });

  /* Kopierknopf in den Textblöcken zum Mitnehmen */
  document.querySelectorAll("[data-kopieren]").forEach(function (knopf) {
    knopf.addEventListener("click", function () {
      var block = knopf.parentNode.querySelector("pre");
      if (!block) return;
      var text = block.textContent;
      var fertig = function (ok) {
        var alt = knopf.textContent;
        knopf.textContent = ok ? "Kopiert" : "Bitte von Hand markieren";
        window.setTimeout(function () { knopf.textContent = alt; }, 2200);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () { fertig(true); },
                                                 function () { fertig(false); });
      } else {
        fertig(false);
      }
    });
  });

  /* Prüflisten merken sich den Stand im Browser des Lesers. */
  document.querySelectorAll("[data-liste]").forEach(function (liste) {
    var name = "laboraquise-liste-" + liste.getAttribute("data-liste");
    var kaesten = liste.querySelectorAll('input[type="checkbox"]');
    var stand = [];
    try {
      var roh = window.localStorage.getItem(name);
      if (roh) stand = JSON.parse(roh) || [];
    } catch (e) { stand = []; }
    kaesten.forEach(function (k, i) { if (stand[i]) k.checked = true; });
    liste.addEventListener("change", function () {
      try {
        var neu = [];
        kaesten.forEach(function (k) { neu.push(k.checked); });
        window.localStorage.setItem(name, JSON.stringify(neu));
      } catch (e) { /* privates Fenster oder gesperrter Speicher: Stand wird nicht gemerkt */ }
    });
  });
})();
