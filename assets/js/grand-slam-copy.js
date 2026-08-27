(function () {
  'use strict';

  if (window.__grandSlamRecruitingCopy) return;
  window.__grandSlamRecruitingCopy = true;

  var MONEY = new Intl.NumberFormat('de-DE', {
    style: 'currency',
    currency: 'EUR',
    maximumFractionDigits: 0
  });

  function one(selector, root) {
    return (root || document).querySelector(selector);
  }

  function all(selector, root) {
    return Array.prototype.slice.call((root || document).querySelectorAll(selector));
  }

  function text(el, value) {
    if (el) el.textContent = value;
  }

  function html(el, value) {
    if (el) el.innerHTML = value;
  }

  function meta(selector, value) {
    var el = one(selector);
    if (el) el.setAttribute('content', value);
  }

  function replaceButtonCopy() {
    all('.pointer-events-none.text-wrap-nowrap').forEach(function (el) {
      var current = (el.textContent || '').trim();
      if (/Erstgespräch|Termin buchen|kontaktieren/i.test(current)) {
        el.textContent = '15-Minuten-Kapazitäts-Audit buchen';
      }
    });
    all('.button_subtext').forEach(function (el) {
      el.textContent = 'Kostenlos, 15 Minuten, ohne Verpflichtung.';
    });
  }

  function applyHead() {
    document.title = 'Zahntechniker finden | 12 qualifizierte Bewerbungen in 60 Tagen | Laboraquise.de';
    var description = 'Dental-Recruiting für Dentallabore: 12 qualifizierte Zahntechniker-Bewerbungen in 60 Tagen garantiert oder 100 % der Dienstleistungsgebühr zurück. 8.000 € netto, Werbebudget separat.';
    meta('meta[name="description"]', description);
    meta('meta[property="og:title"]', '12 qualifizierte Zahntechniker-Bewerbungen in 60 Tagen | Laboraquise.de');
    meta('meta[property="og:description"]', description);
    meta('meta[name="twitter:title"]', '12 qualifizierte Zahntechniker-Bewerbungen in 60 Tagen | Laboraquise.de');
    meta('meta[name="twitter:description"]', description);
  }

  function applyNavigation() {
    all('.mega-nav__bar-link span').forEach(function (el) {
      var current = (el.textContent || '').trim();
      if (current === 'Leistungen') el.textContent = 'Das System';
      if (current === 'Referenzen') el.textContent = 'Ergebnisse';
      if (current === 'Über uns') el.textContent = 'Über uns';
    });
  }

  function applyHero() {
    text(one('.hero-pille__text'), 'Exklusiv für Dentallabore');
    html(one('.header3_h1'), '12 qualifizierte Zahntechniker-Bewerbungen <span class="text-color-primary">in 60 Tagen.</span>');

    var heroLead = one('.header3_content-left .text-color-secondary.text-size-medium');
    text(heroLead, 'Garantiert. Oder Sie erhalten 100 % unserer Dienstleistungsgebühr zurück. Das Dental-Recruiting-System für inhabergeführte Labore, die keine Zeit mehr für Quereinsteiger, Stellenbörsen und leere Werbeversprechen haben.');

    var profile = one('.marquee_1_profile-wrapper .text-color-secondary');
    text(profile, 'Ein System. Ein Garantieprofil. Ein messbares Ergebnis.');

    var chips = [
      'Über 1.600 Branchenkontakte im Talent-Pool',
      '12 qualifizierte Bewerbungen in 60 Tagen',
      '100 % Spezialisierung auf Zahntechnik',
      'Keine Quereinsteiger im Garantieprofil',
      '4 harte Muss-Kriterien',
      '8.000 € netto Festpreis',
      '100 % Geld-zurück-Garantie',
      '15-Minuten-Kapazitäts-Audit'
    ];
    all('.zusage-chip').forEach(function (el, index) {
      var svg = el.querySelector('svg');
      el.textContent = chips[index % chips.length];
      if (svg) el.insertBefore(svg, el.firstChild);
    });
  }

  function applyCalculator() {
    var wrapper = one('.header3_image-wrapper .calc-wrapper');
    if (!wrapper) return;

    text(one('.result-status', wrapper), 'Vakanzkosten-Rechner');
    text(one('#resultUnit', wrapper), 'Produktionsausfall bei 2 Monaten Vakanz');
    text(one('.calc-explain', wrapper), '60 Tage Leerstand kosten bei 14.500 € Produktionsausfall pro Monat bereits 29.000 €. Jeder weitere Monat erhöht den Verlust.');

    var labels = all('.control-label', wrapper);
    var hints = all('.control-hint', wrapper);
    if (labels[0]) labels[0].textContent = 'Produktionsausfall pro unbesetztem Techniker / Monat';
    if (hints[0]) hints[0].textContent = 'Orientierungswert: 14.500 € monatlich';
    if (labels[1]) labels[1].textContent = 'Wie lange ist der Tisch bereits unbesetzt?';
    if (hints[1]) hints[1].textContent = 'Jeder weitere Monat vervielfacht den Kapazitätsverlust';

    var salary = one('#salary', wrapper);
    var impact = one('#impact', wrapper);
    if (!salary || !impact) return;

    salary.min = '10000';
    salary.max = '20000';
    salary.step = '500';
    salary.value = '14500';
    impact.min = '1';
    impact.max = '6';
    impact.step = '1';
    impact.value = '2';

    var scale = all('.impact-scale span', wrapper);
    if (scale[0]) scale[0].textContent = '1 Monat';
    if (scale[1]) scale[1].textContent = '3 Monate';
    if (scale[2]) scale[2].textContent = '6 Monate';

    function setProgress(el) {
      var value = parseFloat(el.value);
      var min = parseFloat(el.min);
      var max = parseFloat(el.max);
      var progress = ((value - min) / (max - min)) * 100;
      el.style.setProperty('--progress', progress + '%');
    }

    function render() {
      var monthly = parseFloat(salary.value) || 14500;
      var months = parseFloat(impact.value) || 2;
      var total = monthly * months;
      var perDay = monthly / 21.7;
      var perWeek = monthly / 4.33;

      text(one('#salaryVal', wrapper), MONEY.format(monthly));
      text(one('#impactVal', wrapper), months + (months === 1 ? ' Monat' : ' Monate'));
      text(one('#totalAmount', wrapper), MONEY.format(total));
      text(one('#resultUnit', wrapper), 'Produktionsausfall bei ' + months + (months === 1 ? ' Monat Vakanz' : ' Monaten Vakanz'));
      text(one('#perDay', wrapper), MONEY.format(perDay));
      text(one('#perWeek', wrapper), MONEY.format(perWeek));
      text(one('#perMonth', wrapper), MONEY.format(monthly));
      setProgress(salary);
      setProgress(impact);
    }

    if (!wrapper.dataset.grandSlamCalc) {
      wrapper.dataset.grandSlamCalc = '1';
      salary.addEventListener('input', function () { setTimeout(render, 0); });
      impact.addEventListener('input', function () { setTimeout(render, 0); });
      salary.addEventListener('change', function () { setTimeout(render, 0); });
      impact.addEventListener('change', function () { setTimeout(render, 0); });
    }
    render();
  }

  function applyProblems() {
    var section = one('.section_problems');
    if (!section) return;

    html(one('h2', section), 'Eine offene Zahntechnikerstelle kostet Sie <span class="text-color-primary">jeden einzelnen Tag.</span>');

    var bigCards = all('.recruiting-erfahrung_card', section);
    if (bigCards[0]) {
      text(one('h5', bigCards[0]), 'Sie stehen abends wieder selbst an der Fräse');
      text(one('.text-color-secondary', bigCards[0]), 'Eigentlich müssten Sie das Labor führen. Stattdessen springen Sie nach Feierabend in CAD/CAM, Keramik oder Arbeitsvorbereitung ein, weil der Tisch seit Monaten unbesetzt ist.');
    }
    if (bigCards[1]) {
      text(one('h5', bigCards[1]), 'Aufträge sind da. Die Kapazität fehlt.');
      text(one('.text-color-secondary', bigCards[1]), 'Neue Fälle anzunehmen klingt gut, bis niemand mehr weiß, wer sie fertigen soll. Dann werden Lieferzeiten länger, das Team arbeitet am Anschlag und Wachstum wird zum Risiko.');
    }

    text(one('.schmerz-frage', section), 'Kommt Ihnen das <span>aus Ihrem Labor bekannt vor?</span>');

    var pain = [
      ['Der Inhaber kompensiert die offene Stelle', 'Sie führen nicht mehr. Sie produzieren. Und jede Stunde am Werktisch fehlt bei Kunden, Mitarbeitern und Unternehmensentwicklung.'],
      ['Stellenbörsen erreichen vor allem aktiv Suchende', 'Die guten Zahntechniker sitzen meistens bereits in einem Labor. Eine Anzeige allein wartet darauf, dass genau diese Menschen zufällig suchen.'],
      ['Quereinsteiger kosten Zeit statt sie zu sparen', 'Allgemeine Kampagnen erzeugen Formulareinträge. Wir definieren vorher, welche Ausbildung, Erfahrung und Spezialisierung überhaupt zählen.'],
      ['Ihr Team trägt die Vakanz mit', 'Überstunden funktionieren eine Zeit lang. Danach steigen Fehler, Ausschuss, Frust und das Risiko der nächsten Kündigung.'],
      ['60 Tage Leerstand kosten über 29.000 €', 'Bei 14.500 € monatlichem Produktionsausfall wird Abwarten schnell teurer als eine konsequente Besetzungskampagne.'],
      ['Großlabore nehmen den Markt, während Kapazität fehlt', 'Wer nicht liefern kann, kann nicht wachsen. Die freie Nachfrage wandert zu Laboren, die personell schneller skalieren können.']
    ];
    all('.schmerz-karte', section).forEach(function (card, index) {
      if (!pain[index]) return;
      text(one('h3', card), pain[index][0]);
      text(one('p', card), pain[index][1]);
    });
  }

  function applyMechanismIntro() {
    var section = one('.section_shop');
    if (!section) return;
    text(one('.inline-text', section), 'DAS DENTAL-RECRUITING-SYSTEM');
    html(one('h2', section), 'Hören Sie auf, auf Bewerber zu warten. <span class="text-color-primary">Bauen Sie ein Besetzungssystem.</span>');
    text(one('.scorecard_content-left > .margin-top .text-color-secondary', section), 'Wir behandeln Ihre offene Zahntechnikerstelle wie ein messbares Akquiseproblem: Zielprofil definieren, vorhandenen Talent-Pool prüfen, regionale Nachfrage erzeugen, hart qualifizieren und jeden Schritt transparent im Portal abbilden.');
    var checks = all('.scorecard_check-item .text-weight-medium', section);
    var copy = [
      'Day-1-Scan gegen über 1.600 bestehende Branchenkontakte',
      '4-Punkte-Filter: Ausbildung, Erfahrung, Spezialisierung, Region',
      '12 qualifizierte Bewerbungen in 60 Tagen oder 100 % Geld zurück'
    ];
    checks.forEach(function (el, i) { if (copy[i]) el.textContent = copy[i]; });
  }

  function applyOfferStack() {
    var section = one('.section_leistung-slider');
    if (!section) return;
    text(one('.inline-text', section), 'DAS 60-TAGE-BESETZUNGSSYSTEM');
    html(one('h2', section), 'Sie führen die Gespräche. <span class="text-color-primary">Wir bauen den gesamten Weg dorthin.</span>');

    var items = [
      ['Day-1-Scan', 'Kein Kaltstart: Wir gleichen Ihr Einzugsgebiet direkt mit unserem Pool aus über 1.600 vorqualifizierten Zahntechnikern aus vergangenen Branchen-Kampagnen ab. Ziel: erste passende Profile innerhalb von 48–72 Stunden.'],
      ['Garantieprofil festlegen', 'Vor Kampagnenstart definieren wir objektiv, welche Ausbildung, Berufserfahrung, Spezialisierung und regionale Entfernung eine Bewerbung erfüllen muss, damit sie zählt.'],
      ['Regionale Omnipräsenz', 'Wir bringen Ihre Position im exakt vereinbarten Radius vor die festangestellten Zahntechniker, die nicht täglich auf Jobbörsen suchen, aber für die richtige Gelegenheit wechselbereit sind.'],
      ['4-Punkte Dental-Talent-Filter', 'Nur reale Interessenten mit gültigen Kontaktdaten, abgeschlossener Zahntechnik-Ausbildung, passender Erfahrung und realistischem Arbeitsweg fließen in das Garantieergebnis ein.'],
      ['Kunden- und Bewerberportal', 'Sie sehen gefilterte Kandidaten, Qualifizierungsstatus und nächsten Schritt in Echtzeit. Kein Excel-Chaos, kein Nachfragen, kein Blackbox-Recruiting.'],
      ['Zahntechniker-Gesprächssystem', 'Sie erhalten einen 30-Minuten-Leitfaden, Kandidaten-Scorecard sowie Follow-up- und Rückmeldevorlagen, damit aus guten Bewerbern schnelle, strukturierte Entscheidungen werden.'],
      ['60 Tage Steuerung + Garantie', 'Wir testen, optimieren und steuern die Kampagne über 60 Tage. Kommen weniger als 12 qualifizierte Bewerbungen gemäß Garantieprofil, erstatten wir 100 % der Dienstleistungsgebühr.']
    ];
    all('.leistung-slider_item', section).forEach(function (item, index) {
      if (!items[index]) return;
      var content = one('.text-color-secondary.text-size-medium', item);
      if (content) content.innerHTML = '<span class="text-color-text text-weight-medium">' + items[index][0] + '</span> — ' + items[index][1];
      var img = one('img', item);
      if (img) img.alt = items[index][0] + ' im Dental-Recruiting-System';
    });
  }

  function applyMidCTA() {
    var section = one('.section_cta-1');
    if (!section) return;
    html(one('h2', section), 'Prüfen Sie in 15 Minuten, <span class="text-color-primary">ob Ihr Labor in das 60-Tage-System passt.</span>');
    text(one('.text-color-secondary', section), 'Im Kapazitäts-Audit klären wir offene Position, regionalen Radius, Muss-Kriterien und ob ein Start wirtschaftlich sinnvoll ist. Keine allgemeine Agenturberatung.');
  }

  function applyFilterSection() {
    var section = one('.section_video');
    if (!section) return;
    html(one('h2', section), 'Eine Bewerbung zählt erst, wenn <span class="text-color-primary">vier harte Kriterien erfüllt sind.</span>');
    text(one('.text-color-secondary', section), '1. Reale Person mit gültigen Kontaktdaten und echtem Interesse. 2. Abgeschlossene Ausbildung als Zahntechniker/in. 3. Berufserfahrung im gesuchten Schwerpunkt wie CAD/CAM, Keramik oder Teleskop. 4. Wohnort im vereinbarten Einzugsgebiet mit realistischem Arbeitsweg. Keine Quereinsteiger im Garantieprofil.');
  }

  function applyTimeline() {
    var section = one('.section_timeline');
    if (!section) return;
    html(one('h2', section), 'Vom Kapazitäts-Audit bis zum <span class="text-color-primary">garantierten 60-Tage-Ergebnis.</span>');

    var labels = all('.timeline_label .inline-text', section);
    ['Heute', '48–72 Std.', 'Tag 60'].forEach(function (v, i) { if (labels[i]) labels[i].textContent = v; });

    var cards = all('.timeline_card', section).filter(function (el) { return !el.closest('.hide'); });
    var content = [
      ['15-Minuten-Kapazitäts-Audit', ['Offene Position und Engpass prüfen', 'Einzugsgebiet und Muss-Kriterien festlegen', 'Passung für das 8.000-€-Festpreis-System klären']],
      ['Day-1-Scan + Kampagnenstart', ['1.600+ Branchenkontakte gegen Ihr Gebiet prüfen', 'Garantieprofil und Ansprache aufsetzen', 'Erste Matches nach Möglichkeit innerhalb von 48–72 Stunden']],
      ['12 qualifizierte Bewerbungen oder Geld zurück', ['60 Tage aktive Steuerung und Optimierung', 'Jede Bewerbung wird am Garantieprofil gemessen', 'Bei Zielverfehlung 100 % Dienstleistungsgebühr zurück']]
    ];
    cards.forEach(function (card, index) {
      if (!content[index]) return;
      text(one('.text-size-medium.text-weight-medium', card), content[index][0]);
      var bullets = all('.timeline_check-item > div:last-child', card);
      content[index][1].forEach(function (v, i) { if (bullets[i]) bullets[i].textContent = v; });
    });
  }

  function applyValueAndGuarantee() {
    var section = one('.section_vorteile');
    if (!section) return;
    html(one('h2', section), 'Ein Festpreis. Ein Garantieprofil. <span class="text-color-primary">Das Risiko liegt bei uns.</span>');

    var boxes = all('.vorteile_box-wrapper', section);
    if (boxes[0]) {
      text(one('h3', boxes[0]), 'Die eiserne 100-%-Geld-zurück-Garantie');
      text(one('.text-size-medium.text-color-secondary', boxes[0]), 'Gehen innerhalb von 60 Tagen weniger als 12 nachweislich qualifizierte Bewerbungen gemäß dem vorab definierten Garantieprofil bei Ihnen ein, überweisen wir Ihnen 100 % unserer Dienstleistungsgebühr zurück. Keine Gutschrift. Keine Pflichtverlängerung. Echte Rücküberweisung. Das gesamte Risiko liegt bei uns.');
    }
    var last = boxes[boxes.length - 1];
    if (last) {
      text(one('h3', last), '8.000 € netto für das vollständige 60-Tage-System');
      text(one('.text-size-medium.text-color-secondary', last), 'Festpreis für Kampagnenaufbau, regionale Bewerbergewinnung, Qualifizierung, Portal, laufende Optimierung und Ergebnisgarantie. Das Meta-Werbebudget wird separat und direkt an Meta gezahlt.');
    }

    var reasons = [
      'Abgeschlossene Zahntechnik-Ausbildung',
      'Passende Berufserfahrung',
      'Gesuchter Fachbereich',
      'Realistischer Arbeitsweg',
      'Echtes Gesprächsinteresse'
    ];
    all('.grund-text', section).forEach(function (el, i) { el.textContent = reasons[i % reasons.length]; });
  }

  function applyProof() {
    var section = one('#about');
    if (section) {
      text(one('h2', section), 'Kein Generalisten-Recruiting. Zahntechnik. Punkt.');
      text(one('.text-color-secondary', section), 'Das System ist auf inhabergeführte Dentallabore mit offenen Fachpositionen ausgelegt. Der Fokus liegt nicht auf Reichweite, sondern auf einem vorher objektiv definierten Bewerberprofil und einem messbaren 60-Tage-Ergebnis.');
      var stats = all('.about-2_box-item', section);
      var values = [
        ['1.600+', 'Branchenkontakte im Talent-Pool'],
        ['Ø 12', 'qualifizierte Bewerbungen in 60 Tagen'],
        ['100 %', 'Spezialisierung auf Zahntechnik']
      ];
      stats.forEach(function (box, i) {
        if (!values[i]) return;
        text(one('.heading-style-h3', box), values[i][0]);
        text(one('.text-color-secondary', box), values[i][1]);
      });
    }

    var testimonial = one('.section_testimonial-slider');
    if (!testimonial) return;
    html(one('.ts-kopf h2', testimonial), 'Keine Fantasie-Logos. <span class="text-color-primary">Nur die Kennzahlen, an denen wir uns messen lassen.</span>');
    text(one('.ts-hinweis', testimonial), 'Wir entfernen branchenfremde oder nicht belastbare Referenzflächen aus dieser Seite. Entscheidend für dieses Angebot sind das vorab definierte Garantieprofil, der Dental-Talent-Pool, die 60-Tage-Laufzeit und die schriftliche Risikoumkehr.');
    all('.testimonial-slider_stars', testimonial).forEach(function (el) { el.style.display = 'none'; });

    var quoteCopy = [
      '„Über 1.600 Branchenkontakte bilden den Ausgangspunkt für den Day-1-Scan im vereinbarten Einzugsgebiet.“',
      '„12 qualifizierte Zahntechniker-Bewerbungen in 60 Tagen sind das klare Ziel des Systems.“',
      '„Vier objektive Muss-Kriterien entscheiden, ob eine Bewerbung überhaupt zum Garantieergebnis zählt.“',
      '„8.000 € netto Festpreis. Werbebudget separat. Kein unklarer Agentur-Retainer.“',
      '„Bei Zielverfehlung: 100 % der Dienstleistungsgebühr zurück. Keine Gutschrift. Keine Pflichtverlängerung.“'
    ];
    var authorCopy = [
      ['Day-1-Scan', 'Bestehender Dental-Talent-Pool'],
      ['60-Tage-Ziel', 'Messbares Ergebnis'],
      ['4-Punkte-Filter', 'Objektive Qualifizierung'],
      ['Festpreis', 'Klare Investition'],
      ['Risikoumkehr', 'Schriftliche Ergebnisgarantie']
    ];
    all('.testimonial-slider_quote .heading-style-h6', testimonial).forEach(function (el, i) {
      if (quoteCopy[i]) el.textContent = quoteCopy[i];
    });
    all('.testimonial-slider_author', testimonial).forEach(function (el, i) {
      if (!authorCopy[i]) return;
      var name = one('.text-size-medium', el);
      var sub = one('.text-size-small.text-color-secondary', el);
      text(name, authorCopy[i][0]);
      text(sub, authorCopy[i][1]);
    });
  }

  function applySpecialties() {
    var section = one('.section_branchen');
    if (!section) return;
    text(one('h2', section), 'Für diese Zahntechniker-Schwerpunkte bauen wir Kampagnen');
    var titles = ['CAD/CAM & digitale Fertigung', 'Keramik & Ästhetik', 'Kombitechnik & Teleskop', 'Kunststoff & Prothetik', 'Arbeitsvorbereitung & Allrounder'];
    all('.branchen_item .heading-style-h6', section).forEach(function (el, i) { if (titles[i]) el.textContent = titles[i]; });
    all('.branchen_item img', section).forEach(function (img, i) { if (titles[i]) img.alt = 'Zahntechnik Schwerpunkt: ' + titles[i]; });

    var gallery = one('.section_references-gallery');
    if (gallery) {
      html(one('h2', gallery), '<span class="text-color-primary">Keine allgemeine Recruiting-Agentur.</span> Ein System für Zahntechnik.');
      text(one('.references-gallery_content .text-color-secondary', gallery), 'CAD/CAM, Keramik, Kombitechnik, Prothetik: Wir bauen die Ansprache um den tatsächlichen Arbeitsplatz und die Wechselgründe Ihrer gesuchten Fachkraft.');
    }
  }

  function applyFAQ() {
    var section = one('.section_startseite_faq-sektion');
    if (!section) return;
    text(one('h2', section), 'Häufige Fragen vor dem Kapazitäts-Audit');
    var qa = [
      ['Was garantieren Sie konkret?', '12 qualifizierte Zahntechniker-Bewerbungen innerhalb von 60 Tagen gemäß dem vor Kampagnenstart gemeinsam definierten Garantieprofil. Erreichen wir dieses Ziel nicht, erhalten Sie 100 % unserer Dienstleistungsgebühr zurück. Garantiert werden Bewerbungen, nicht die konkrete Einstellung.'],
      ['Was gilt als qualifizierte Bewerbung?', 'Eine reale Person mit gültigen Kontaktdaten und echtem Gesprächsinteresse, abgeschlossener Zahntechnik-Ausbildung, passender Berufserfahrung im gesuchten Schwerpunkt und einem Wohnort beziehungsweise Arbeitsweg innerhalb des vereinbarten regionalen Profils.'],
      ['Bekommen wir wieder Quereinsteiger?', 'Quereinsteiger ohne die vereinbarte abgeschlossene Zahntechnik-Ausbildung zählen nicht zum Garantieergebnis. Genau deshalb wird das Garantieprofil vor dem Start schriftlich und objektiv definiert.'],
      ['Warum Social Media statt nur Indeed oder StepStone?', 'Weil ein großer Teil der interessanten Zahntechniker bereits beschäftigt ist und nicht täglich auf Jobbörsen sucht. Die regionale Kampagne bringt Ihre Position im vereinbarten Radius aktiv vor diese Zielgruppe.'],
      ['Was passiert in den ersten 48–72 Stunden?', 'Wir starten mit dem Day-1-Scan und gleichen Ihr Einzugsgebiet mit unserem bestehenden Pool aus über 1.600 Branchenkontakten ab. Wenn passende Profile vorhanden sind, können daraus bereits erste Matches entstehen. Parallel wird die regionale Kampagne aufgebaut.'],
      ['Was kostet das Dental-Recruiting-System?', '8.000 € netto als Festpreis für das vollständige 60-Tage-System. Das Werbebudget wird separat und direkt an Meta gezahlt.'],
      ['Wie viel Zeit müssen wir selbst investieren?', 'Sie liefern im Onboarding die Informationen zur Position, geben Kampagne und Garantieprofil frei, reagieren zeitnah auf passende Kandidaten und führen die finalen Gespräche. Strategie, Creatives, Kampagne, Bewerbungsprozess, Qualifizierung, Portal und Optimierung übernehmen wir.'],
      ['Was passiert, wenn Sie die 12 Bewerbungen nicht erreichen?', 'Dann greift die Risikoumkehr: 100 % der gezahlten Dienstleistungsgebühr werden zurücküberwiesen. Keine Gutschrift. Keine Pflichtverlängerung. Echte Rücküberweisung gemäß den vereinbarten Garantiebedingungen.']
    ];
    all('.accordion-css__item', section).forEach(function (item, i) {
      if (!qa[i]) return;
      text(one('.accordion-css__item-top .text-size-medium', item), qa[i][0]);
      text(one('.accordion-css__item-bottom-content p', item), qa[i][1]);
    });
  }

  function applyFooter() {
    var cta = one('.section_cta-footer');
    if (cta) {
      html(one('h2', cta), 'Besetzen Sie den Tisch, bevor die nächste Vakanz <span class="text-color-primary">weitere 29.000 € kostet.</span>');
      text(one('.text-color-secondary', cta), 'Buchen Sie das 15-minütige Kapazitäts-Audit. Wir prüfen Position, Einzugsgebiet und Garantieprofil und sagen Ihnen direkt, ob das 60-Tage-System für Ihr Labor passt.');
    }
    var footer = one('.section_footer');
    if (footer) {
      html(one('.footer_slogan-wrapper h2', footer), '12 qualifizierte Zahntechniker-Bewerbungen <span class="text-color-primary">in 60 Tagen.</span>');
      all('.footer_link div').forEach(function (el) {
        var current = (el.textContent || '').trim();
        if (current === 'Leistungen') el.textContent = 'Das System';
        if (current === 'Referenzen') el.textContent = 'Ergebnisse';
      });
    }
  }

  function applyPopupAndForm() {
    var modalTitle = one('.modal_1_content-wrap h2');
    if (modalTitle) modalTitle.innerHTML = '<span class="text-color-primary">15 Minuten</span> Kapazitäts-Audit buchen';
    var submit = one('#wf-form-Erstgespraech input[type="submit"]');
    if (submit) submit.value = 'Kapazitäts-Audit anfragen';

    var popup = one('.message-popup');
    if (popup) {
      text(one('.message_text .text-weight-medium', popup), '15-Minuten-Kapazitäts-Audit');
      text(one('.message_text .text-color-secondary', popup), 'Wir prüfen Ihre offene Zahntechnikerstelle, den regionalen Radius und ob das 60-Tage-System zu Ihrem Labor passt.');
      var timer = one('.message_timer-wrapper-copy', popup);
      if (timer) timer.style.display = 'none';
      var booking = one('.pointer-events-none.text-wrap-nowrap', popup);
      if (booking) booking.textContent = 'Kapazitäts-Audit buchen';
    }
  }

  function applyDirectResponseLanguage() {
    var comparisonSection = one('.section_references-gallery');
    if (comparisonSection) {
      var overlay = one('.references-gallery_content', comparisonSection);
      if (overlay) overlay.setAttribute('data-comparison-copy', 'stellenboerse-vs-headhunter-vs-dental-system');
    }
  }

  function applyAll() {
    applyHead();
    applyNavigation();
    replaceButtonCopy();
    applyHero();
    applyCalculator();
    applyProblems();
    applyMechanismIntro();
    applyOfferStack();
    applyMidCTA();
    applyFilterSection();
    applyTimeline();
    applyValueAndGuarantee();
    applyProof();
    applySpecialties();
    applyFAQ();
    applyFooter();
    applyPopupAndForm();
    applyDirectResponseLanguage();
  }

  applyAll();
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      setTimeout(applyAll, 0);
      setTimeout(applyAll, 500);
    });
  } else {
    setTimeout(applyAll, 0);
  }
  window.addEventListener('load', function () { setTimeout(applyAll, 100); });
})();
