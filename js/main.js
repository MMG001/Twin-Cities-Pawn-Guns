/* Twin Cities Pawn & Gun — main.js (Stitch redesign)
   Hamburger menu, mobile inventory accordion, active nav, footer year,
   smooth scroll, inventory filter chips. Vanilla JS. */
(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    /* ---- Footer copyright year ---- */
    document.querySelectorAll('#year').forEach(function (el) {
      el.textContent = new Date().getFullYear();
    });

    /* ---- Mobile hamburger ---- */
    var hamburger = document.getElementById('hamburger');
    var mobileMenu = document.getElementById('mobile-menu');
    if (hamburger && mobileMenu) {
      hamburger.addEventListener('click', function () {
        mobileMenu.classList.toggle('open');
        var icon = hamburger.querySelector('.material-symbols-outlined');
        if (icon) { icon.textContent = mobileMenu.classList.contains('open') ? 'close' : 'menu'; }
      });
    }

    /* ---- Mobile accordion toggles (inventory / online store) ---- */
    document.querySelectorAll('[data-accordion-toggle]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var target = document.getElementById(btn.getAttribute('data-accordion-toggle'));
        if (target) { target.classList.toggle('hidden'); }
        var chevron = btn.querySelector('.acc-chevron');
        if (chevron) { chevron.textContent = target && !target.classList.contains('hidden') ? 'expand_less' : 'expand_more'; }
      });
    });

    /* ---- Active nav link (desktop + mobile) by current page ---- */
    var path = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('[data-nav]').forEach(function (link) {
      if (link.getAttribute('data-nav') === path) {
        link.classList.add('active');
      }
    });

    /* ---- Smooth scroll for same-page anchors ---- */
    document.querySelectorAll('a[href^="#"]').forEach(function (a) {
      a.addEventListener('click', function (e) {
        var id = a.getAttribute('href');
        if (id.length > 1) {
          var target = document.querySelector(id);
          if (target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            if (mobileMenu) { mobileMenu.classList.remove('open'); }
          }
        }
      });
    });

    /* ---- Inventory filter chips (guns-rifles page) ---- */
    var chips = document.querySelectorAll('[data-filter]');
    if (chips.length) {
      chips.forEach(function (chip) {
        chip.addEventListener('click', function () {
          var filter = chip.getAttribute('data-filter');
          chips.forEach(function (c) { c.classList.remove('active'); });
          chip.classList.add('active');
          document.querySelectorAll('[data-section]').forEach(function (sec) {
            if (filter === 'all' || sec.getAttribute('data-section') === filter) {
              sec.style.display = '';
            } else {
              sec.style.display = 'none';
            }
          });
        });
      });
    }

    /* ---- FAQ accordion ---- */
    document.querySelectorAll('.faq-item .faq-head').forEach(function (head) {
      head.addEventListener('click', function () {
        head.closest('.faq-item').classList.toggle('open');
      });
    });
  });
})();
