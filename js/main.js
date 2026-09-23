/* Twin Cities Pawn & Gun — main.js
   Vanilla JS: mobile menu toggle, smooth scroll, active nav, footer year. */
(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    /* ---- Mobile hamburger menu ---- */
    var toggle = document.getElementById('menu-toggle');
    var menu = document.getElementById('mobile-menu');
    if (toggle && menu) {
      toggle.addEventListener('click', function () {
        var open = menu.classList.toggle('open');
        toggle.classList.toggle('open', open);
        toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
      /* Close menu when a link is clicked */
      menu.querySelectorAll('a').forEach(function (link) {
        link.addEventListener('click', function () {
          menu.classList.remove('open');
          toggle.classList.remove('open');
          toggle.setAttribute('aria-expanded', 'false');
        });
      });
    }

    /* ---- Smooth scroll for same-page anchors ---- */
    document.querySelectorAll('a[href^="#"]').forEach(function (a) {
      a.addEventListener('click', function (e) {
        var id = a.getAttribute('href');
        if (id.length > 1) {
          var target = document.querySelector(id);
          if (target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
          }
        }
      });
    });

    /* ---- Active nav link based on current page ---- */
    var path = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('[data-nav]').forEach(function (link) {
      if (link.getAttribute('data-nav') === path) {
        link.classList.add('active');
      }
    });

    /* ---- Footer copyright year ---- */
    var yr = document.getElementById('year');
    if (yr) { yr.textContent = new Date().getFullYear(); }
  });
})();
