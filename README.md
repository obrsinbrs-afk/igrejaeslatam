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

Oferta aprobada: ebook US$20,00 + bonos US$15,00, US$10,00, US$8,00 y US$7,00 = valor total US$60,00 (todos tachados). Precio de lanzamiento: US$9,90, pago único. La aclaración más reciente del propietario reemplaza la mención inicial de US$200.

El propietario enviará posteriormente el enlace de la oferta de US$9,90. Hasta recibirlo se conserva el checkout original: https://pay.hotmart.com/U106054486T?checkoutMode=10. Cambiar el precio visible de la página no modifica el precio configurado en Hotmart.

La estimación local consulta el país de la IP con GeoJS y los tipos de cambio diarios de ExchangeRate-API. No usa GPS ni el idioma del navegador como sustituto del país. Los códigos de moneda por país provienen de Unicode CLDR. Solo se guarda el código del país durante 30 minutos y la tabla de cotizaciones por un máximo de 24 horas (o hasta la próxima actualización del proveedor). No se almacena la IP. Ante errores de red, datos inválidos o moneda no compatible se conserva US$9,90 sin inventar una conversión.

Fuentes: https://www.geojs.io/docs/v1/endpoints/country/ ; https://www.exchangerate-api.com/docs/free ; https://github.com/unicode-org/cldr-json/blob/main/cldr-json/cldr-core/supplemental/currencyData.json . La página incluye la atribución requerida al proveedor de cotizaciones. La conversión es orientativa; no fija un precio de cobro local.

Los nombres y las ciudades de los testimonios se conservan; son testimonios de Brasil traducidos al español.

La página y sus imágenes están en español. El PDF del ebook y los bonos entregados por Hotmart no se proporcionaron en este encargo y no fueron traducidos. El propietario debe preparar esos archivos y configurar la oferta/checkout en español antes de usar esta versión para vender el producto en español. La página original y su dominio no se modificaron.

Las políticas son traducciones de las políticas públicas del propietario; conservan las referencias a la legislación de Brasil y el correo real de soporte. La configuración regional del checkout externo se gestiona en Hotmart.

Los scripts de marketing del HTML original no se ejecutan en esta copia privada de revisión. La política de privacidad conserva la descripción de los servicios del sitio comercial original. La activación de campañas y su seguimiento requiere configurar la versión comercial correspondiente.
