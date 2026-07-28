/* ===================================================================
   VERCEL / APPLE-STYLE CLEAN & MINIMALIST LIGHT PORTFOLIO SCRIPT
   Developer: Sameer Chakravedi — AI & ML Developer
   =================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  // Mobile Navigation Hamburger
  const hamburger = document.getElementById('hamburger');
  const navMenu = document.getElementById('nav-menu');
  if (hamburger && navMenu) {
    hamburger.addEventListener('click', () => {
      navMenu.classList.toggle('open');
    });
    document.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => navMenu.classList.remove('open'));
    });
  }

  // Hero Typewriter Headline Effect
  const typewriterElement = document.getElementById('typewriter');
  if (typewriterElement) {
    const roles = [
      'AI & ML Developer',
      'Computer Vision Engineer',
      'NLP & Deep Learning Specialist',
      'Full-Stack AI Solutions Builder'
    ];
    let roleIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let typingSpeed = 90;

    function typeEffect() {
      const currentRole = roles[roleIndex];

      if (isDeleting) {
        typewriterElement.textContent = currentRole.substring(0, charIndex - 1);
        charIndex--;
        typingSpeed = 40;
      } else {
        typewriterElement.textContent = currentRole.substring(0, charIndex + 1);
        charIndex++;
        typingSpeed = 90;
      }

      if (!isDeleting && charIndex === currentRole.length) {
        isDeleting = true;
        typingSpeed = 1600;
      } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        roleIndex = (roleIndex + 1) % roles.length;
        typingSpeed = 400;
      }

      setTimeout(typeEffect, typingSpeed);
    }
    typeEffect();
  }

  // Interactive Project Filter Pills & Search Input
  const filterPills = document.querySelectorAll('.filter-pill');
  const projectCards = document.querySelectorAll('.project-card');
  const searchInput = document.getElementById('project-search');

  let activeFilter = 'all';
  let searchQuery = '';

  function filterProjects() {
    projectCards.forEach(card => {
      const cardCategory = card.getAttribute('data-category');
      const isLive = card.getAttribute('data-is-live') === 'true';
      const keywords = (card.getAttribute('data-keywords') || '').toLowerCase();

      let matchesFilter = false;
      if (activeFilter === 'all') {
        matchesFilter = true;
      } else if (activeFilter === 'live') {
        matchesFilter = isLive;
      } else if (cardCategory === activeFilter) {
        matchesFilter = true;
      }

      let matchesSearch = true;
      if (searchQuery.trim() !== '') {
        matchesSearch = keywords.includes(searchQuery.toLowerCase().trim());
      }

      if (matchesFilter && matchesSearch) {
        card.style.display = 'flex';
        setTimeout(() => {
          card.style.opacity = '1';
          card.style.transform = 'translateY(0)';
        }, 50);
      } else {
        card.style.opacity = '0';
        card.style.transform = 'translateY(10px)';
        setTimeout(() => {
          card.style.display = 'none';
        }, 200);
      }
    });
  }

  filterPills.forEach(pill => {
    pill.addEventListener('click', () => {
      filterPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      activeFilter = pill.getAttribute('data-filter');
      filterProjects();
    });
  });

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value;
      filterProjects();
    });
  }

  // Copy Email Toast Notification
  const copyBtn = document.getElementById('copy-email-btn');
  const toast = document.getElementById('toast');
  if (copyBtn && toast) {
    copyBtn.addEventListener('click', () => {
      const email = copyBtn.getAttribute('data-email');
      navigator.clipboard.writeText(email).then(() => {
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 2800);
      });
    });
  }

  // Active Navbar Scroll Highlight
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');
  window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(sec => {
      if (window.scrollY >= sec.offsetTop - 120) {
        current = sec.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === '#' + current) {
        link.classList.add('active');
      }
    });
  });
});
