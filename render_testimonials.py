"""Accessible, build-time carousel markup. Example cards stay explicitly labeled."""
import json
from pathlib import Path
from html import escape
from bs4 import BeautifulSoup


def render_testimonials(section, root):
    data = json.loads((Path(root) / 'testimonials.json').read_text(encoding='utf-8'))
    examples = data['mode'] == 'illustrative'
    cards = data['cards']
    section['id'] = 'testimonios'
    section['aria-labelledby'] = 'testimonials-heading'
    section['aria-roledescription'] = 'carrusel'
    section.h2['id'] = 'testimonials-heading'
    section.h2.string = 'Católicos de todo el mundo ya comenzaron'
    label = section.select_one('p')
    label.contents[-1].replace_with('Historias para inspirar tu lectura' if examples else 'Lo que dicen los lectores')
    if examples:
        note = BeautifulSoup('<p class="testimonial-example-note" id="testimonial-example-note">Vista previa con ejemplos ilustrativos: los nombres, ciudades y relatos de estas tarjetas son ficticios y no representan testimonios verificados.</p>', 'html.parser')
        section.h2.insert_after(note)
        section['aria-describedby'] = 'testimonial-example-note'
    grid = section.select_one('div.grid')
    fragments = []
    count = len(cards)
    for i, card in enumerate(cards):
        initials = ''.join(part[0] for part in card['name'].split()[:2]).upper()
        badge = '<span class="testimonial-example-badge">Ejemplo ilustrativo</span>' if examples else ''
        fragments.append(f'''<article class="testimonial-card" role="group" aria-roledescription="diapositiva" aria-label="{i+1} de {count}">
          <div class="testimonial-card-top"><span class="testimonial-country">{escape(card['country'])}</span>{badge}</div>
          <span class="testimonial-quote-mark" aria-hidden="true">“</span>
          <blockquote>{escape(card['quote'])}</blockquote>
          <div class="testimonial-person"><span class="testimonial-initials" aria-hidden="true">{escape(initials)}</span><div><p class="testimonial-name">{escape(card['name'])}</p><p class="testimonial-location">{escape(card['city'])}, {escape(card['country'])}</p></div></div>
        </article>''')
    dots = ''.join(f'<button type="button" class="carousel-dot" data-slide="{i}" aria-label="Ver tarjeta {i+1}" aria-controls="testimonial-track" aria-current="{"true" if i==0 else "false"}"></button>' for i in range(count))
    carousel = BeautifulSoup(f'''<div class="testimonial-carousel" data-carousel>
      <div class="testimonial-track" id="testimonial-track" tabindex="0" aria-label="Relatos de América Latina">{''.join(fragments)}</div>
      <div class="carousel-controls"><button type="button" class="carousel-arrow" data-carousel-prev aria-label="Ver tarjetas anteriores" aria-controls="testimonial-track"><span aria-hidden="true">←</span></button><div class="carousel-dots" aria-label="Elegir tarjeta">{dots}</div><button type="button" class="carousel-arrow" data-carousel-next aria-label="Ver tarjetas siguientes" aria-controls="testimonial-track"><span aria-hidden="true">→</span></button></div>
      <p class="carousel-status" data-carousel-status aria-live="polite" aria-atomic="true">Tarjeta 1 de {count}</p>
    </div>''', 'html.parser')
    grid.replace_with(carousel)
