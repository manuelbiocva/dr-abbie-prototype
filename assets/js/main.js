/* ==========================================================================
   Dr. Abbie Clinics — Prototype behaviour
   Vanilla JS, no dependencies. Every interaction is keyboard-operable and
   respects prefers-reduced-motion. Animate transform/opacity only.
   ========================================================================== */

(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ------------------------------------------------------------------------
     Services dropdown (desktop)
     Opens on hover and on click/Enter. Closes on Escape, outside click, blur.
     ------------------------------------------------------------------------ */
  function initDropdowns() {
    var items = document.querySelectorAll('.nav__item--has-dropdown');

    items.forEach(function (item) {
      var trigger = item.querySelector('.nav__link');
      var panel = item.querySelector('.dropdown');
      if (!trigger || !panel) return;

      var closeTimer;

      function open() {
        clearTimeout(closeTimer);
        // one menu at a time: the mega panels open in the same place, so the
        // other must close straight away rather than after its hover delay
        items.forEach(function (other) {
          if (other !== item && other.classList.contains('is-open')) {
            other.classList.remove('is-open');
            var t = other.querySelector('.nav__link');
            if (t) t.setAttribute('aria-expanded', 'false');
          }
        });
        item.classList.add('is-open');
        trigger.setAttribute('aria-expanded', 'true');
      }
      function close() {
        item.classList.remove('is-open');
        trigger.setAttribute('aria-expanded', 'false');
      }
      function closeSoon() {
        closeTimer = setTimeout(close, 140);
      }

      item.addEventListener('mouseenter', open);
      item.addEventListener('mouseleave', closeSoon);

      trigger.addEventListener('click', function (e) {
        e.preventDefault();
        item.classList.contains('is-open') ? close() : open();
      });

      // Close when focus leaves the whole item (tabbing past the last link)
      item.addEventListener('focusout', function (e) {
        if (!item.contains(e.relatedTarget)) close();
      });

      item.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && item.classList.contains('is-open')) {
          close();
          trigger.focus();
        }
      });
    });

    document.addEventListener('click', function (e) {
      document.querySelectorAll('.nav__item--has-dropdown.is-open').forEach(function (item) {
        if (!item.contains(e.target)) {
          item.classList.remove('is-open');
          var t = item.querySelector('.nav__link');
          if (t) t.setAttribute('aria-expanded', 'false');
        }
      });
    });
  }

  /* ------------------------------------------------------------------------
     Mobile drawer — focus trapped, body locked, Escape closes
     ------------------------------------------------------------------------ */
  function initDrawer() {
    var drawer = document.getElementById('mobile-drawer');
    var openBtn = document.querySelector('.nav-toggle');
    var closeBtn = drawer && drawer.querySelector('.drawer__close');
    if (!drawer || !openBtn) return;

    var lastFocused = null;

    function open() {
      lastFocused = document.activeElement;
      drawer.classList.add('is-open');
      drawer.removeAttribute('inert');
      openBtn.setAttribute('aria-expanded', 'true');
      document.body.classList.add('is-locked');
      var first = drawer.querySelector('.drawer__close');
      if (first) first.focus();
    }

    function close() {
      drawer.classList.remove('is-open');
      openBtn.setAttribute('aria-expanded', 'false');
      document.body.classList.remove('is-locked');
      // Wait for the transition before removing from the a11y tree
      setTimeout(function () {
        if (!drawer.classList.contains('is-open')) drawer.setAttribute('inert', '');
      }, reduceMotion ? 0 : 400);
      if (lastFocused) lastFocused.focus();
    }

    openBtn.addEventListener('click', open);
    if (closeBtn) closeBtn.addEventListener('click', close);

    drawer.addEventListener('click', function (e) {
      if (e.target.closest('a')) close();
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && drawer.classList.contains('is-open')) close();
    });

    // Focus trap
    drawer.addEventListener('keydown', function (e) {
      if (e.key !== 'Tab' || !drawer.classList.contains('is-open')) return;
      var focusables = drawer.querySelectorAll('a[href], button:not([disabled])');
      if (!focusables.length) return;
      var first = focusables[0];
      var last = focusables[focusables.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });

    // Expandable groups inside the drawer (Services, Locations)
    drawer.querySelectorAll('.drawer__group > button').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var group = btn.parentElement;
        var isOpen = group.classList.toggle('is-open');
        btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      });
    });

    // Close if the viewport grows back to desktop
    window.matchMedia('(min-width: 1081px)').addEventListener('change', function (e) {
      if (e.matches && drawer.classList.contains('is-open')) close();
    });
  }

  /* ------------------------------------------------------------------------
     Accordions — treatments and FAQs
     Height via grid-template-rows, not max-height guessing.
     ------------------------------------------------------------------------ */
  function initAccordions() {
    document.querySelectorAll('.accordion').forEach(function (acc) {
      var single = acc.hasAttribute('data-single');

      acc.querySelectorAll('.acc-trigger').forEach(function (trigger) {
        trigger.addEventListener('click', function () {
          var item = trigger.closest('.acc-item');
          var isOpen = item.classList.contains('is-open');

          if (single && !isOpen) {
            acc.querySelectorAll('.acc-item.is-open').forEach(function (other) {
              other.classList.remove('is-open');
              other.querySelector('.acc-trigger').setAttribute('aria-expanded', 'false');
            });
          }

          item.classList.toggle('is-open', !isOpen);
          trigger.setAttribute('aria-expanded', String(!isOpen));
        });
      });
    });
  }

  /* ------------------------------------------------------------------------
     Carousel — native scroll-snap, buttons scroll by one card
     ------------------------------------------------------------------------ */
  function initCarousels() {
    document.querySelectorAll('.carousel').forEach(function (carousel) {
      var track = carousel.querySelector('.carousel__track');
      var prev = carousel.querySelector('[data-carousel="prev"]');
      var next = carousel.querySelector('[data-carousel="next"]');
      if (!track) return;

      function step() {
        var card = track.firstElementChild;
        if (!card) return 320;
        var gap = parseFloat(getComputedStyle(track).columnGap) || 24;
        return card.getBoundingClientRect().width + gap;
      }

      function sync() {
        if (!prev || !next) return;
        var max = track.scrollWidth - track.clientWidth - 2;
        prev.disabled = track.scrollLeft <= 2;
        next.disabled = track.scrollLeft >= max;
      }

      if (prev) prev.addEventListener('click', function () {
        track.scrollBy({ left: -step(), behavior: reduceMotion ? 'auto' : 'smooth' });
      });
      if (next) next.addEventListener('click', function () {
        track.scrollBy({ left: step(), behavior: reduceMotion ? 'auto' : 'smooth' });
      });

      track.addEventListener('scroll', sync, { passive: true });
      window.addEventListener('resize', sync);
      sync();
    });
  }

  /* ------------------------------------------------------------------------
     Scroll reveal — one-shot, never re-triggers on scroll up
     ------------------------------------------------------------------------ */
  /* ------------------------------------------------------------------------
     Scroll reveal
     Bidirectional: elements animate in on the way down and re-arm once they
     are fully out of view, so scrolling back up plays them again. The previous
     version unobserved on first sight, which made it a one-shot.

     Two thresholds rather than one. Adding at 8% and removing at 0% leaves a
     dead band between them, so an element parked exactly on the trigger line
     cannot flicker between states.
     ------------------------------------------------------------------------ */
  function initReveal() {
    var targets = document.querySelectorAll('.reveal');
    if (!targets.length) return;

    if (reduceMotion || !('IntersectionObserver' in window)) {
      Array.prototype.forEach.call(targets, function (el) { el.classList.add('is-visible'); });
      return;
    }

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var el = entry.target;
        if (entry.isIntersecting && entry.intersectionRatio >= 0.08) {
          // transition-delay rather than setTimeout: re-arming cancels it
          // cleanly, where a pending timer would fire against a stale state
          el.style.transitionDelay = (parseInt(el.dataset.revealDelay || '0', 10)) + 'ms';
          el.classList.add('is-visible');
        } else if (entry.intersectionRatio === 0) {
          el.style.transitionDelay = '0ms';
          el.classList.remove('is-visible');
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: [0, 0.08] });

    Array.prototype.forEach.call(targets, function (el) { observer.observe(el); });
  }

  /* ------------------------------------------------------------------------
     Hero entrance
     The hidden state is applied by JS, never by the stylesheet. If this script
     fails to run the hero copy is simply visible, rather than permanently
     invisible behind an animation that never starts.
     ------------------------------------------------------------------------ */
  function initHeroEnter() {
    var hero = document.querySelector('.hero--bleed');
    if (!hero || reduceMotion) return;
    hero.classList.add('is-armed');
    window.requestAnimationFrame(function () {
      window.requestAnimationFrame(function () { hero.classList.add('is-loaded'); });
    });
  }


  /* Stagger cards inside a grid — 60ms cascade, set as data attributes */
  function initStagger() {
    document.querySelectorAll('[data-stagger]').forEach(function (group) {
      Array.prototype.forEach.call(group.children, function (child, i) {
        if (child.classList.contains('reveal')) {
          child.dataset.revealDelay = String(Math.min(i, 6) * 60);
        }
      });
    });
  }

  /* ------------------------------------------------------------------------
     Today's opening hours — highlights the current row on location pages
     Reads rendered data only; invents nothing.
     ------------------------------------------------------------------------ */
  function initHours() {
    var days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'];
    var today = days[new Date().getDay()];
    document.querySelectorAll('.hours-table tr[data-day="' + today + '"]').forEach(function (row) {
      row.classList.add('is-today');
      var label = row.querySelector('th');
      if (label && !label.querySelector('.sr-only')) {
        var tag = document.createElement('span');
        tag.className = 'sr-only';
        tag.textContent = ' (today)';
        label.appendChild(tag);
      }
    });
  }


  /* ------------------------------------------------------------------------
     Hero zoom — pause when off-screen
     The hero image loops continuously. Once it scrolls away there is no
     reason to keep a full-screen composited layer animating, so it is paused
     until it comes back.
     ------------------------------------------------------------------------ */
  function initHeroZoom() {
    var img = document.querySelector('.hero--bleed .hero__bg img');
    if (!img || reduceMotion || !('IntersectionObserver' in window)) return;

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        img.classList.toggle('is-paused', !entry.isIntersecting);
      });
    }, { threshold: 0 });

    observer.observe(img.closest('.hero'));
  }


  /* ------------------------------------------------------------------------
     Hero treatment slider
     Three cards visible, stepping one at a time through seven treatments.
     The first three slides are cloned at the end of the track, so reaching
     the end can be swapped back to the start with the transition switched
     off — the loop has no visible jump.

     Same guards as the hero zoom: pauses off-screen, pauses on hover and on
     keyboard focus, and never auto-advances under prefers-reduced-motion,
     where it stays a working manual carousel.
     ------------------------------------------------------------------------ */
  /* ------------------------------------------------------------------------
     Stepped slider
     One implementation for every stepped carousel on the page. Each root
     declares its own per-view count; the clones that make the wrap seamless
     sit at the end of the track, so `real` is the slide count minus them.

     Generalised from the hero treatment slider when the practitioners rail
     was switched from a continuous marquee to the same stepped behaviour --
     two copies of this logic was the alternative.
     ------------------------------------------------------------------------ */
  function initSlider(root) {
    var track = root.querySelector('[data-slider-track]');
    if (!track) return;
    var slides = track.querySelectorAll('[data-slide]');
    var prev = root.querySelector('[data-slider="prev"]');
    var next = root.querySelector('[data-slider="next"]');
    var PER_VIEW = parseInt(root.getAttribute('data-per-view'), 10) || 3;
    var real = slides.length - PER_VIEW;   // clones sit at the end
    if (real < 1) return;

    var index = 0;
    var timer = null;
    var visible = true;
    var hovered = false;
    var delay = parseInt(root.getAttribute('data-interval'), 10) || 3600;

    function offset() {
      var slide = slides[0];
      var gap = parseFloat(getComputedStyle(track).columnGap) || 0;
      return slide.getBoundingClientRect().width + gap;
    }

    function apply(animate) {
      track.style.transition = animate ? '' : 'none';
      track.style.transform = 'translateX(' + (-index * offset()) + 'px)';
      if (!animate) {
        // force a reflow so the next change animates again
        void track.offsetWidth;
        track.style.transition = '';
      }
    }

    function go(step) {
      index += step;
      if (index < 0) {
        // jump to the cloned tail, then step back into the real slides
        index = real;
        apply(false);
        index = real - 1;
      }
      apply(true);
    }

    track.addEventListener('transitionend', function (e) {
      if (e.propertyName !== 'transform') return;
      if (index >= real) {
        index -= real;
        apply(false);
      }
    });

    function start() {
      if (reduceMotion || timer) return;
      timer = setInterval(function () {
        if (visible && !hovered) go(1);
      }, delay);
    }

    if (prev) prev.addEventListener('click', function () { go(-1); });
    if (next) next.addEventListener('click', function () { go(1); });

    root.addEventListener('mouseenter', function () { hovered = true; });
    root.addEventListener('mouseleave', function () { hovered = false; });
    root.addEventListener('focusin', function () { hovered = true; });
    root.addEventListener('focusout', function (e) {
      if (!root.contains(e.relatedTarget)) hovered = false;
    });

    window.addEventListener('resize', function () { apply(false); });

    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) { visible = entry.isIntersecting; });
      }, { threshold: 0 }).observe(root);
    }

    start();
  }

  function initSliders() {
    Array.prototype.forEach.call(
      document.querySelectorAll('[data-slider-root]'), initSlider);
  }


  /* ------------------------------------------------------------------------
     Logo marquee — pause when off-screen
     Hover, focus and reduced-motion are handled in CSS; this only stops the
     animation compositing once the strip has scrolled away.
     ------------------------------------------------------------------------ */
  function initLogoMarquee() {
    if (reduceMotion || !('IntersectionObserver' in window)) return;
    // querySelectorAll, not querySelector: the strip now appears on more than
    // one template, and a page could carry two.
    Array.prototype.forEach.call(
      document.querySelectorAll('[data-logo-marquee]'), function (track) {
        var host = track.closest('.logo-strip');
        if (!host) return;
        new IntersectionObserver(function (entries) {
          entries.forEach(function (entry) {
            track.classList.toggle('is-paused', !entry.isIntersecting);
          });
        }, { threshold: 0 }).observe(host);
      });
  }

  /* ------------------------------------------------------------------------
     Parallax backgrounds
     Scroll-linked, not perpetual: nothing moves unless the user is scrolling,
     so this sits outside the DESIGN.md motion budget that governs the looping
     animations. transform only, rAF-throttled, and updated only for sections
     currently on screen. Held to 13% of the section height -- the layer has
     15% of overhang top and bottom, so the image edge can never come into view.
     ------------------------------------------------------------------------ */
  function initParallax() {
    var items = [];
    Array.prototype.forEach.call(document.querySelectorAll('[data-parallax]'), function (el) {
      var host = el.closest ? el.closest('section') : null;
      items.push({ el: el, host: host || el.parentNode, on: false });
    });
    if (!items.length || reduceMotion) return;

    var ticking = false;

    function update() {
      var vh = window.innerHeight;
      items.forEach(function (it) {
        if (!it.on) return;
        var r = it.host.getBoundingClientRect();
        // 0 as the section enters from the bottom, 1 as it leaves at the top
        var p = (vh - r.top) / (vh + r.height);
        p = p < 0 ? 0 : (p > 1 ? 1 : p);
        var travel = r.height * 0.13;
        it.el.style.transform =
          'translate3d(0,' + ((p - 0.5) * 2 * travel).toFixed(1) + 'px,0)';
      });
      ticking = false;
    }

    function onScroll() {
      if (!ticking) { window.requestAnimationFrame(update); ticking = true; }
    }

    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          items.forEach(function (it) { if (it.host === e.target) it.on = e.isIntersecting; });
        });
        onScroll();
      }, { threshold: 0 });
      items.forEach(function (it) { io.observe(it.host); });
    } else {
      items.forEach(function (it) { it.on = true; });
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    update();
  }

  /* ------------------------------------------------------------------------
     Conversion tracking hooks
     Fires dataLayer events for GTM/GA4. No IDs are invented — the container
     is added at build time; these events simply queue until it loads.
     ------------------------------------------------------------------------ */
  function initTracking() {
    window.dataLayer = window.dataLayer || [];

    document.addEventListener('click', function (e) {
      var book = e.target.closest('[data-track="book"]');
      if (book) {
        // method: online (a clinic's Nookal diary), phone ("Call to book"), or
        // chooser (a generic button on its way to the choose-your-clinic page)
        window.dataLayer.push({
          event: 'booking_click',
          location: book.dataset.location || 'sitewide',
          source: book.dataset.source || 'unknown',
          method: book.dataset.bookMethod || 'chooser'
        });
        return;
      }

      var call = e.target.closest('a[href^="tel:"]');
      if (call) {
        window.dataLayer.push({
          event: 'phone_click',
          location: call.dataset.location || 'sitewide',
          number: call.getAttribute('href').replace('tel:', '')
        });
      }
    });
  }

  /* ------------------------------------------------------------------------
     Header shadow on scroll
     ------------------------------------------------------------------------ */
  function initHeader() {
    var header = document.querySelector('.site-header');
    if (!header) return;
    var ticking = false;

    function update() {
      // Past roughly the header's own height, so a transparent header has a
      // visible transparent state before it turns solid.
      header.classList.toggle('is-scrolled', window.scrollY > 72);
      ticking = false;
    }
    window.addEventListener('scroll', function () {
      if (!ticking) { window.requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    update();
  }

  /* ------------------------------------------------------------------------
     Blog post contents: marks the section currently being read. A scroll
     listener rather than IntersectionObserver, because a heading that has
     already scrolled past still counts as the current section.
     ------------------------------------------------------------------------ */
  function initToc() {
    var toc = document.querySelector('[data-toc]');
    if (!toc) return;
    var heads = [];
    Array.prototype.forEach.call(toc.querySelectorAll('a[href^="#"]'), function (a) {
      var h = document.getElementById(a.getAttribute('href').slice(1));
      if (h) heads.push({ el: h, link: a });
    });
    if (!heads.length) return;
    var ticking = false;

    function update() {
      var line = window.innerHeight * 0.3;
      var current = null;
      heads.forEach(function (h) {
        if (h.el.getBoundingClientRect().top <= line) current = h;
      });
      heads.forEach(function (h) {
        if (h === current) h.link.setAttribute('aria-current', 'true');
        else h.link.removeAttribute('aria-current');
      });
      ticking = false;
    }
    window.addEventListener('scroll', function () {
      if (!ticking) { window.requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    update();
  }

  /* ------------------------------------------------------------------------
     Enquiry form (contact page). Prototype only: validates in the browser,
     records the event and shows the success state, but sends nothing. The
     WordPress form plugin replaces the submit handling.
     ------------------------------------------------------------------------ */
  function initEnquiryForm() {
    var form = document.querySelector('[data-enquiry-form]');
    if (!form) return;
    var done = document.querySelector('[data-enquiry-done]');

    function check(field) {
      var ok;
      var value = (field.value || '').trim();
      if (field.type === 'checkbox') ok = field.checked;
      else if (field.type === 'email') ok = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(value);
      else if (field.type === 'tel') ok = value.replace(/\D/g, '').length >= 8;
      else ok = value.length > 0;
      var err = document.getElementById(field.id + '-err');
      field.setAttribute('aria-invalid', ok ? 'false' : 'true');
      if (err) err.hidden = ok;
      return ok;
    }

    var required = form.querySelectorAll('[required]');
    Array.prototype.forEach.call(required, function (field) {
      // re-check as the person corrects a field, but do not nag before submit
      field.addEventListener(field.type === 'checkbox' ? 'change' : 'input', function () {
        if (field.getAttribute('aria-invalid') === 'true') check(field);
      });
      field.addEventListener('blur', function () {
        if (field.value || field.getAttribute('aria-invalid')) check(field);
      });
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var firstBad = null;
      Array.prototype.forEach.call(required, function (field) {
        if (!check(field) && !firstBad) firstBad = field;
      });
      if (firstBad) { firstBad.focus(); return; }
      if (form.elements.website && form.elements.website.value) return;   // bot

      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({
        event: 'enquiry_submit',
        topic: form.elements.topic ? form.elements.topic.value : '',
        location: form.elements.clinic ? (form.elements.clinic.value || 'none') : 'none'
      });
      form.hidden = true;
      if (done) { done.hidden = false; done.focus(); }
    });
  }

  /* ------------------------------------------------------------------------
     Swipe rows: arrows and an "n / total" counter under every .swipe row,
     shown only while the row actually overflows (mobile, or always for
     .swipe--always). Native scroll-snap does the swiping; this only adds the
     buttons for people who do not think to swipe.
     ------------------------------------------------------------------------ */
  function initSwipe() {
    var L = '<svg width="16" height="16" viewBox="0 0 18 18" fill="none" aria-hidden="true"><path d="M11 4 6 9l5 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    var R = '<svg width="16" height="16" viewBox="0 0 18 18" fill="none" aria-hidden="true"><path d="m7 4 5 5-5 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>';

    document.querySelectorAll('.swipe').forEach(function (row) {
      var items = row.children;
      if (items.length < 2) return;
      var nav = document.createElement('div');
      nav.className = 'swipe-nav' +
        (row.classList.contains('swipe--always') ? ' swipe-nav--always' : '') +
        (row.classList.contains('swipe--dark') ? ' swipe-nav--dark' : '');
      nav.innerHTML = '<span class="swipe-nav__count" aria-live="polite"></span>' +
        '<button type="button" class="swipe-nav__btn" data-dir="-1" aria-label="Previous">' + L + '</button>' +
        '<button type="button" class="swipe-nav__btn" data-dir="1" aria-label="Next">' + R + '</button>';
      row.parentNode.insertBefore(nav, row.nextSibling);
      var count = nav.querySelector('.swipe-nav__count');
      var prev = nav.querySelector('[data-dir="-1"]');
      var next = nav.querySelector('[data-dir="1"]');

      function step() {
        var a = items[0].getBoundingClientRect(), b = items[1].getBoundingClientRect();
        return Math.max(1, b.left - a.left);
      }
      function update() {
        var overflow = row.scrollWidth > row.clientWidth + 2;
        nav.hidden = !overflow;
        if (!overflow) return;
        var perView = Math.max(1, Math.round(row.clientWidth / step()));
        var first = Math.round(row.scrollLeft / step()) + 1;
        var last = Math.min(items.length, first + perView - 1);
        count.textContent = (perView > 1 ? first + '–' + last : first) + ' / ' + items.length;
        prev.disabled = row.scrollLeft <= 2;
        next.disabled = row.scrollLeft + row.clientWidth >= row.scrollWidth - 2;
      }
      nav.addEventListener('click', function (e) {
        var btn = e.target.closest('.swipe-nav__btn');
        if (!btn) return;
        row.scrollBy({ left: step() * parseInt(btn.getAttribute('data-dir'), 10),
                       behavior: reduceMotion ? 'auto' : 'smooth' });
      });
      var ticking = false;
      row.addEventListener('scroll', function () {
        if (!ticking) { window.requestAnimationFrame(function () { update(); ticking = false; }); ticking = true; }
      }, { passive: true });
      window.addEventListener('resize', update);

      // Auto-advance (client request): one card every 4.5s, back to the start
      // after the last. Only while the row overflows and is on screen; paused
      // while the visitor touches, hovers or focuses it, and for 8s after they
      // swipe themselves. Off entirely under prefers-reduced-motion.
      if (!reduceMotion) {
        var visible = false, held = false, resumeAt = 0;
        function hold() { held = true; }
        function release() { held = false; resumeAt = Date.now() + 8000; }
        row.addEventListener('pointerenter', hold);
        row.addEventListener('pointerleave', release);
        row.addEventListener('touchstart', hold, { passive: true });
        row.addEventListener('touchend', release, { passive: true });
        row.addEventListener('focusin', hold);
        row.addEventListener('focusout', release);
        nav.addEventListener('click', function () { resumeAt = Date.now() + 8000; });
        if ('IntersectionObserver' in window) {
          new IntersectionObserver(function (entries) {
            visible = entries[0].isIntersecting;
          }, { threshold: 0.5 }).observe(row);
        }
        setInterval(function () {
          if (!visible || held || Date.now() < resumeAt || document.hidden) return;
          if (row.scrollWidth <= row.clientWidth + 2) return;
          var atEnd = row.scrollLeft + row.clientWidth >= row.scrollWidth - 2;
          if (atEnd) row.scrollTo({ left: 0, behavior: 'smooth' });
          else row.scrollBy({ left: step(), behavior: 'smooth' });
        }, 4500);
      }
      update();
    });
  }

  /* ---------------------------------------------------------------------- */

  function init() {
    initHeader();
    initHeroZoom();
    initHeroEnter();
    initSliders();
    initLogoMarquee();
    initParallax();
    initDropdowns();
    initDrawer();
    initAccordions();
    initCarousels();
    initStagger();
    initReveal();
    initHours();
    initTracking();
    initToc();
    initEnquiryForm();
    initSwipe();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
