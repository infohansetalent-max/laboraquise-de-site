/* Klick-Kennung von Google Ads an die Terminseite weiterreichen.
   Google haengt beim Anzeigenklick gclid, gbraid oder wbraid an die
   Ziel-URL. Wer danach auf "Erstgespraech vereinbaren" klickt, verliert
   die Kennung, weil die Links fest auf /termin/ zeigen. Dieses Skript
   haengt sie an.

   Auf der Terminseite gibt termin/index.html den Wert an Calendly
   weiter. Damit steht bei jeder Buchung, welcher Anzeigenklick sie
   ausgeloest hat, und die Buchung laesst sich als Conversion nach
   Google Ads laden.

   Wichtig: Die Kennung wandert nur durch die Adresszeile. Es wird
   nichts im Browser gespeichert, kein Cookie, kein Local Storage.
   Die Seite bleibt damit ohne Einwilligung nach Paragraf 25 TTDSG. */
(function () {
  if (!window.URLSearchParams) return;

  var SCHLUESSEL = ["gclid", "gbraid", "wbraid"];
  var rein = new URLSearchParams(window.location.search);
  var teile = [];

  SCHLUESSEL.forEach(function (name) {
    var wert = rein.get(name);
    if (wert) teile.push(name + "=" + encodeURIComponent(wert));
  });
  if (!teile.length) return;

  var anhang = teile.join("&");

  function ergaenzen(link) {
    var ziel = link.getAttribute("href");
    if (!ziel || ziel.indexOf("/termin/") !== 0) return;
    for (var i = 0; i < SCHLUESSEL.length; i++) {
      if (ziel.indexOf(SCHLUESSEL[i] + "=") !== -1) return;
    }
    link.setAttribute("href", ziel + (ziel.indexOf("?") === -1 ? "?" : "&") + anhang);
  }

  function alleLinks() {
    var links = document.querySelectorAll('a[href^="/termin/"]');
    Array.prototype.forEach.call(links, ergaenzen);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", alleLinks);
  } else {
    alleLinks();
  }

  /* Der Rechner schreibt den Link seines Knopfes bei jeder
     Reglerbewegung neu und wirft den Anhang dabei weg. Beim Klick
     deshalb noch einmal nachziehen. */
  document.addEventListener("click", function (e) {
    var ziel = e.target;
    if (!ziel || !ziel.closest) return;
    var link = ziel.closest('a[href^="/termin/"]');
    if (link) ergaenzen(link);
  }, true);
})();
