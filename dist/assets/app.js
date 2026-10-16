document.querySelectorAll('[aria-controls^="faq-answer-"]').forEach(button => {
  button.addEventListener('click', () => {
    const expanded = button.getAttribute('aria-expanded') === 'true';
    button.setAttribute('aria-expanded', String(!expanded));
    document.getElementById(button.getAttribute('aria-controls')).hidden = expanded;
  });
});

document.querySelectorAll('[data-carousel]').forEach(carousel => {
  const track = carousel.querySelector('.testimonial-track');
  const cards = [...track.querySelectorAll('.testimonial-card')];
  const dots = [...carousel.querySelectorAll('[data-slide]')];
  const previous = carousel.querySelector('[data-carousel-prev]');
  const next = carousel.querySelector('[data-carousel-next]');
  const status = carousel.querySelector('[data-carousel-status]');
  if (!cards.length) return;
  let frame;
  let active = 0;
  let stops = [];

  const position = card => card.offsetLeft - cards[0].offsetLeft;
  const maxScroll = () => Math.max(0, track.scrollWidth - track.clientWidth);
  function update() {
    frame = null;
    const edge = track.scrollLeft;
    const max = maxScroll();
    stops = [...new Set(cards.map(card => Math.round(Math.min(position(card), max))))];
    active = stops.reduce((best, stop, i) => Math.abs(stop - edge) < Math.abs(stops[best] - edge) ? i : best, 0);
    dots.forEach((dot, i) => {
      dot.hidden = i >= stops.length;
      dot.setAttribute('aria-label', `Ver grupo ${i + 1} de tarjetas`);
      dot.setAttribute('aria-current', String(i === active));
    });
    previous.disabled = edge <= 3;
    next.disabled = edge >= max - 3;
    const visible = cards.map((card, i) => ({ i, start: position(card), end: position(card) + card.offsetWidth }))
      .filter(card => card.start < edge + track.clientWidth - 6 && card.end > edge + 6);
    if (!visible.length) return;
    const first = visible[0].i + 1;
    const last = visible[visible.length - 1].i + 1;
    status.textContent = first === last ? `Tarjeta ${first} de ${cards.length}` : `Tarjetas ${first}–${last} de ${cards.length}`;
  }
  function scheduleUpdate() {
    if (!frame) frame = requestAnimationFrame(update);
  }
  function goTo(index) {
    const target = Math.min(stops.length - 1, Math.max(0, index));
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    track.scrollTo({ left: stops[target], behavior: reducedMotion ? 'instant' : 'smooth' });
  }
  previous.addEventListener('click', () => goTo(active - 1));
  next.addEventListener('click', () => goTo(active + 1));
  dots.forEach((dot, i) => dot.addEventListener('click', () => goTo(i)));
  track.addEventListener('keydown', event => {
    if (event.target !== track) return;
    const keys = { ArrowLeft: active - 1, ArrowRight: active + 1, Home: 0, End: stops.length - 1 };
    if (event.key in keys) { event.preventDefault(); goTo(keys[event.key]); }
  });
  track.addEventListener('scroll', scheduleUpdate, { passive: true });
  if (typeof ResizeObserver !== 'undefined') new ResizeObserver(scheduleUpdate).observe(track);
  else window.addEventListener('resize', scheduleUpdate);
  update();
});
