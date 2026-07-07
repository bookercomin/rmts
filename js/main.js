// Roccia Marketing — shared site behavior
(function(){
  // Footer year
  var y = document.getElementById('year');
  if(y){ y.textContent = new Date().getFullYear(); }

 // Mobile nav toggle
  var toggle = document.getElementById('navToggle');
  var links = document.getElementById('navLinks');
  function closeMenu(){
    if(!links || !toggle) return;
    links.classList.remove('open');
    toggle.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }
  function openMenu(){
    if(!links || !toggle) return;
    links.classList.add('open');
    toggle.classList.add('open');
    toggle.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  }
  if(toggle && links){
    toggle.addEventListener('click', function(e){
      e.stopPropagation();
      if(links.classList.contains('open')){ closeMenu(); } else { openMenu(); }
    });
    links.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click', closeMenu);
    });
    document.addEventListener('click', function(e){
      if(links.classList.contains('open') && !links.contains(e.target) && e.target !== toggle && !toggle.contains(e.target)){
        closeMenu();
      }
    });
    document.addEventListener('keydown', function(e){
      if(e.key === 'Escape'){ closeMenu(); }
    });
    window.addEventListener('resize', function(){
      if(window.innerWidth > 880){ closeMenu(); }
    });
  }

  // Active nav link based on current page
  var current = (window.location.pathname.split('/').pop() || 'index.html').replace('.html','') || 'index';
  var navKey = current.indexOf('blog') === 0 ? 'blog' : current;
  document.querySelectorAll('.nav-links a').forEach(function(a){
    if(a.dataset.nav === navKey){ a.classList.add('active'); }
  });

  // Reveal on scroll
  var revealEls = document.querySelectorAll('.reveal');
  if('IntersectionObserver' in window && revealEls.length){
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if(entry.isIntersecting){
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.14, rootMargin: '0px 0px -40px 0px' });
    revealEls.forEach(function(el){ io.observe(el); });
  } else {
    revealEls.forEach(function(el){ el.classList.add('in'); });
  }

  // Simple accordion (used on Services FAQ / pricing details)
  document.querySelectorAll('[data-accordion-trigger]').forEach(function(btn){
    btn.addEventListener('click', function(){
      var panel = document.getElementById(btn.getAttribute('aria-controls'));
      var open = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', open ? 'false' : 'true');
      if(panel){ panel.style.maxHeight = open ? null : panel.scrollHeight + 'px'; }
    });
  });

  // Contact form (static demo — replace action with real endpoint / Formspree / etc.)
  var form = document.getElementById('contactForm');
  if(form){
    form.addEventListener('submit', function(e){
      e.preventDefault();
      var status = document.getElementById('formStatus');
      if(status){
        status.textContent = "Thanks — that's in. We'll reply within one business day, or grab a slot on our calendar below for the fastest response.";
        status.style.display = 'block';
      }
      form.reset();
    });
  }
})();
