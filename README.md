# Brote de Fe — español LATAM

Recreación fiel de la página del propietario https://brotodefe.com.br/. Diseño aprobado: conservar el visual original y traducir todo. HTML estático responsive, sin instalación de dependencias web.

## Contenido

- `dist/index.html`: página de venta en español latinoamericano.
- `dist/assets/`: CSS, interacción de preguntas frecuentes y las cuatro artes localizadas.
- `dist/politicas/`: privacidad, términos y reembolso en español.
- `build.py` y `policies.py`: fuentes editables de la localización; utilizan BeautifulSoup disponible en el entorno de trabajo.
- `image-prompts.json`: prompts completos de las cuatro artes, generadas con la herramienta integrada ImageGen a partir de los originales.

Para servir localmente: `python -m http.server 4173 --directory dist --bind 127.0.0.1`.

## Condiciones comerciales conservadas

Precio: R$47,90 (BRL). Checkout original: https://pay.hotmart.com/U106054486T?checkoutMode=10. Los nombres y las ciudades de los testimonios se conservan; son testimonios de Brasil traducidos al español. No se inventaron testimonios ni precios para otros países.

La página y sus imágenes están en español. El PDF del ebook y los bonos entregados por Hotmart no se proporcionaron en este encargo y no fueron traducidos. El propietario debe preparar esos archivos y configurar la oferta/checkout en español antes de usar esta versión para vender el producto en español. La página original y su dominio no se modificaron.

Las políticas son traducciones de las políticas públicas del propietario; conservan las referencias a la legislación de Brasil y el correo real de soporte. La configuración regional del checkout externo se gestiona en Hotmart.

Los scripts de marketing del HTML original no se ejecutan en esta copia privada de revisión. La política de privacidad conserva la descripción de los servicios del sitio comercial original. La activación de campañas y su seguimiento requiere configurar la versión comercial correspondiente.
