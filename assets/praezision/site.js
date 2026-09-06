/* Individuelle Inszenierung. Die Scroll Craft Engine bleibt unverändert. */
(() => {
  "use strict";
  const root = document.documentElement;
  const reduce = matchMedia("(prefers-reduced-motion: reduce)");
  const compact = matchMedia("(max-width: 640px)");
  const connection = document.querySelector(".connection");
  const bench = document.querySelector(".workbench");
  const field = document.querySelector(".selection-field");
  const profiles = [...document.querySelectorAll(".practice")];
  const steps = [...document.querySelectorAll(".process-steps li")];
  const phaseButtons = [...document.querySelectorAll("[data-phase]")];
  const region = document.querySelector("#region");
  const focus = document.querySelector("#focus");
  const checks = [...document.querySelectorAll(".fit-check input")];
  const note = document.querySelector("#note");
  const stage = document.querySelector(".connection-stage");
  const clamp = (value) => Math.max(0, Math.min(1, value));
  const ease = (value) => {
    const p = clamp(value);
    return p * p * (3 - 2 * p);
  };
  let manualProgress = null;
  let lastScroll = scrollY;
  let frame = 0;
  let activePhase = -1;
  let metrics = [];

  profiles.forEach((profile, index) => {
    profile.style.setProperty("--mobile-col", index % 2);
    profile.style.setProperty("--mobile-row", Math.floor(index / 2));
  });

  function measure() {
    metrics = profiles.map((profile) => ({
      x: profile.offsetLeft,
      y: profile.offsetTop,
      width: profile.offsetWidth,
      height: profile.offsetHeight,
    }));
    schedule();
  }

  function updateNote() {
    const selected = checks
      .filter((input) => input.checked)
      .map((input) => input.value);
    const profile = `Beispielprofil: ${region.selectedOptions[0].text}, ${focus.selectedOptions[0].text}.`;
    note.value = `Gespräch mit Laboraquise\n${profile}\nVoraussetzungen: ${selected.length ? selected.join("; ") : "Gemeinsam klären"}.\nZu klären: Kundenprofil, Gebiet, Kapazität, Leistungsumfang und Budget.`;
    document.querySelector("#fit-result").textContent =
      selected.length === 3
        ? "Gute Voraussetzungen für ein konkretes Gespräch. Gebiet, Angebot und Budget klären wir gemeinsam."
        : selected.length
          ? "Ihre Auswahl ist in der Gesprächsnotiz vorgemerkt. Die offenen Voraussetzungen klären wir gemeinsam."
          : "Im Erstgespräch klären wir gemeinsam die Voraussetzungen.";
  }

  function paint() {
    frame = 0;
    if (document.hidden || reduce.matches) return;
    const rect = connection.getBoundingClientRect();
    if (rect.bottom < 0 || rect.top > innerHeight) return;
    // Enginefortschritt ist die einzige Scrollzeitlinie. Bedienung darf sie lokal vorgeben.
    const progress =
      manualProgress ??
      (parseFloat(getComputedStyle(connection).getPropertyValue("--sc-p")) ||
        0);
    const filterRegion = ease((progress - 0.08) / 0.24);
    const filterFocus = ease((progress - 0.3) / 0.27);
    const gather = ease((progress - 0.51) / 0.32);
    const line = ease((progress - 0.68) / 0.27);
    const phase =
      progress < 0.24 ? 0 : progress < 0.48 ? 1 : progress < 0.75 ? 2 : 3;
    if (phase !== activePhase) {
      steps.forEach((step, i) =>
        step.classList.toggle("is-active", i === phase),
      );
      phaseButtons.forEach((button, i) =>
        button.setAttribute("aria-pressed", String(i === phase)),
      );
      activePhase = phase;
    }
    const states = [];
    profiles.forEach((profile, i) => {
      const item = metrics[i];
      if (!item) return;
      const regionFits = profile.dataset.region === region.value;
      const focusFits = profile.dataset.focus === focus.value;
      const match = regionFits && focusFits;
      let opacity = regionFits ? 1 : 1 - filterRegion * 0.82;
      if (!focusFits) opacity *= 1 - filterFocus * 0.82;
      if (!match) opacity *= 1 - gather;
      const targetX =
        field.clientWidth * (compact.matches ? 0.28 : 0.41) - item.width / 2;
      const targetY = field.clientHeight / 2 - item.height / 2;
      const x = match
        ? (targetX - item.x) * gather
        : (i % 2 ? 28 : -28) * gather;
      const y = match
        ? (targetY - item.y) * gather
        : (i < 3 ? -18 : 18) * gather;
      const scale = match
        ? 1 + gather * (compact.matches ? 0.14 : 0.22)
        : 1 - 0.05 * gather;
      profile.style.setProperty("--x", `${x.toFixed(1)}px`);
      profile.style.setProperty("--y", `${y.toFixed(1)}px`);
      profile.style.setProperty("--scale", scale.toFixed(3));
      profile.style.setProperty("--opacity", opacity.toFixed(3));
      profile.style.zIndex = match ? "2" : "1";
      profile.classList.toggle("is-match", match && filterFocus > 0.5);
      profile.querySelector(".match-label").style.opacity = match
        ? filterFocus.toFixed(3)
        : "0";
      states.push([x.toFixed(0), y.toFixed(0), opacity.toFixed(2)].join(","));
    });
    bench.style.setProperty("--line-progress", line.toFixed(3));
    bench.dataset.scVerifyState = `${phase}|${states.join(";")}|line:${line.toFixed(2)}`;
    bench.dataset.scVerifyHold = String(progress >= 0.95);
    if (!root.classList.contains("motion-on"))
      bench.dataset.scVerifyHold = "true";
  }

  function schedule() {
    if (!frame)
      frame = requestAnimationFrame(() => requestAnimationFrame(paint));
  }

  function setPhase(index) {
    manualProgress = [0.06, 0.36, 0.62, 0.94][index];
    schedule();
  }

  function configureMotion() {
    const mobile = compact.matches;
    // Kein langer Pin, wenn der gesamte Inhalt nicht ins Fenster passt.
    const canPin =
      Boolean(window.ScrollCraft) &&
      !reduce.matches &&
      innerHeight >= (mobile ? 750 : 720);
    root.classList.toggle("motion-on", canPin);
    connection.dataset.scAct = canPin ? "pin" : "flow";
    connection.dataset.scSpan = mobile ? "2.15" : "2.7";
    if (!canPin) {
      connection.classList.remove("sc-act--pinned");
      stage.classList.remove("sc-stage");
      connection.style.height = "";
      connection.style.minHeight = "";
      stage.style.height = "";
      manualProgress = 0.94;
    }
    return canPin;
  }

  root.classList.add("js-ready");
  const animated = configureMotion();
  if (window.ScrollCraft) window.ScrollCraft.mount(document);
  region.disabled = false;
  focus.disabled = false;
  if (!animated) manualProgress = 0.94;
  phaseButtons.forEach((button, index) =>
    button.addEventListener("click", () => setPhase(index)),
  );
  [region, focus].forEach((select) =>
    select.addEventListener("change", () => {
      updateNote();
      manualProgress = 0.94;
      measure();
    }),
  );
  checks.forEach((input) => input.addEventListener("change", updateNote));
  updateNote();
  measure();

  addEventListener(
    "scroll",
    () => {
      if (
        Math.abs(scrollY - lastScroll) > 3 &&
        root.classList.contains("motion-on")
      )
        manualProgress = null;
      lastScroll = scrollY;
      schedule();
    },
    { passive: true },
  );
  addEventListener("resize", measure, { passive: true });
  new ResizeObserver(measure).observe(field);
  document.fonts.ready.then(measure);
  document.addEventListener("visibilitychange", schedule);
  // Die Engine bindet Motionpräferenzen beim Mount. Neu laden erhält einen vollständigen Zustand.
  reduce.addEventListener("change", () => location.reload());

  const menu = document.querySelector("#mobile-nav");
  const toggle = document.querySelector(".menu-toggle");
  function closeMenu(restoreFocus = false) {
    menu.hidden = true;
    toggle.setAttribute("aria-expanded", "false");
    toggle.setAttribute("aria-label", "Menü öffnen");
    if (restoreFocus) toggle.focus();
  }
  toggle.addEventListener("click", () => {
    menu.hidden = !menu.hidden;
    toggle.setAttribute("aria-expanded", String(!menu.hidden));
    toggle.setAttribute(
      "aria-label",
      menu.hidden ? "Menü öffnen" : "Menü schließen",
    );
  });
  menu
    .querySelectorAll("a")
    .forEach((link) => link.addEventListener("click", () => closeMenu()));
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && !menu.hidden) closeMenu(true);
  });

  document.querySelector("#copy-note").addEventListener("click", async () => {
    const status = document.querySelector("#copy-status");
    try {
      await navigator.clipboard.writeText(note.value);
      status.textContent = "Gesprächsnotiz kopiert.";
    } catch {
      note.focus();
      note.select();
      status.textContent =
        "Automatisches Kopieren ist hier nicht verfügbar. Die Notiz ist zum Kopieren markiert.";
    }
  });
  const heroScene = document.querySelector(".hero-scene");
  if (
    matchMedia("(hover: hover) and (pointer: fine)").matches &&
    !reduce.matches
  ) {
    heroScene.addEventListener("pointermove", (event) => {
      const box = heroScene.getBoundingClientRect();
      heroScene.style.setProperty(
        "--pointer-x",
        ((event.clientX - box.left) / box.width - 0.5).toFixed(3),
      );
      heroScene.style.setProperty(
        "--pointer-y",
        ((event.clientY - box.top) / box.height - 0.5).toFixed(3),
      );
    });
    heroScene.addEventListener("pointerleave", () => {
      heroScene.style.setProperty("--pointer-x", "0");
      heroScene.style.setProperty("--pointer-y", "0");
    });
  }
  document
    .querySelectorAll(".hero-scene img,.image-frame img")
    .forEach((img) => {
      const failed = () => img.parentElement.classList.add("media-failed");
      img.addEventListener("error", failed);
      if (img.complete && img.naturalWidth === 0) failed();
    });
  // Statische Inhalte bleiben lesbar, auch wenn Einblendung oder Engine ausfallen.
  setTimeout(() => {
    document
      .querySelectorAll("[data-sc-in]")
      .forEach((el) => el.classList.add("sc-in"));
  }, 3500);
})();
