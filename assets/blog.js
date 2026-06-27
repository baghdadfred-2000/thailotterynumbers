/* ------------------------------------------------------------------
   blog.js — tiny self-contained engine for the /guides (blog) section.
   Handles only: EN/TH language toggle, mobile menu, and the cookie
   banner. It deliberately does NOT load the SPA (app.js), Chart.js or
   the results dataset, so guide pages stay lightweight and adding an
   article never touches the main site engine.
   Language + consent state is shared with the main site via the same
   localStorage keys ("tln_lang", "tln_cookie").
------------------------------------------------------------------- */
(function () {
  "use strict";
  var LANG_KEY = "tln_lang", COOKIE_KEY = "tln_cookie";

  function applyLang(lang) {
    var th = lang === "th";
    document.body.classList.toggle("show-th", th);
    document.documentElement.lang = th ? "th" : "en";
    document.querySelectorAll(".lang-toggle button").forEach(function (b) {
      b.classList.toggle("on", b.dataset.lang === lang);
    });
  }

  function setLang(lang) {
    try { localStorage.setItem(LANG_KEY, lang); } catch (e) {}
    applyLang(lang);
  }

  function currentLang() {
    var l = "en";
    try { l = localStorage.getItem(LANG_KEY) || "en"; } catch (e) {}
    return l === "th" ? "th" : "en";
  }

  function cookieBanner() {
    var seen = null;
    try { seen = localStorage.getItem(COOKIE_KEY); } catch (e) {}
    if (seen) return;
    var el = document.getElementById("cookieBanner");
    if (!el) return;
    var en = "We use essential cookies to remember your language and consent. This site is also supported by ads served via Google AdSense, which uses cookies. See our Cookie and Privacy policies.";
    var th = "เราใช้คุกกี้ที่จำเป็นเพื่อจดจำภาษาและการยินยอมของคุณ เว็บไซต์นี้ยังมีโฆษณาผ่าน Google AdSense ซึ่งใช้คุกกี้ด้วย ดูรายละเอียดในนโยบายคุกกี้และความเป็นส่วนตัวของเรา";
    el.innerHTML =
      '<div class="cookie"><p><span class="lang-en">' + en + '</span><span class="lang-th">' + th + "</span></p>" +
      '<a class="btn btn-ghost" href="/cookie-settings"><span class="lang-en">Cookie Settings</span><span class="lang-th">ตั้งค่าคุกกี้</span></a>' +
      '<button class="btn btn-gold" id="ckOk"><span class="lang-en">Accept</span><span class="lang-th">ยอมรับ</span></button></div>';
    document.getElementById("ckOk").onclick = function () {
      try { localStorage.setItem(COOKIE_KEY, "1"); } catch (e) {}
      el.innerHTML = "";
    };
  }

  function init() {
    applyLang(currentLang());
    document.querySelectorAll(".lang-toggle button").forEach(function (b) {
      b.addEventListener("click", function () { setLang(b.dataset.lang); });
    });
    var burger = document.querySelector(".burger");
    if (burger) {
      burger.addEventListener("click", function () {
        var nav = document.querySelector(".nav-links");
        if (nav) nav.classList.toggle("open");
      });
    }
    cookieBanner();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
