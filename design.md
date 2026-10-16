# Brote de Fe — versión en español LATAM

Dirección aprobada por el usuario: conservar el diseño original de https://brotodefe.com.br/ y traducir todo, incluidas las cuatro imágenes promocionales.

## Alcance

Recrear la página de venta como HTML estático responsive, conservando secciones, espaciado, tipografía Poppins, azul marino, dorado, botones, testimonios y oferta del original. Traducir marca y título visibles como «Brote de Fe — El camino de las 73 raíces». Español latinoamericano neutro, tratamiento de tú y terminología católica: Padres y Doctores de la Iglesia, Tradición, Misa, libros deuterocanónicos.

Las cuatro artes se recrearán con generación de imágenes basada en los originales, reemplazando todos los textos portugueses por español y manteniendo composición, colores y estilo. Guardar originales de referencia y resultados en el proyecto.

Conservar testimonios y localidades de Brasil. Actualización aprobada: valor individual del ebook US$20 y bonos US$15, US$10, US$8 y US$7, todos tachados y con valor total US$60. Precio final «Hoy US$9,90». El propietario confirmó que enviará después el nuevo enlace Hotmart; conservar el enlace existente mientras tanto. La página no modifica el precio configurado en Hotmart ni traduce los archivos entregados por el checkout.

Debajo del precio, mostrar una estimación en la moneda del país detectado por IP (GeoJS), usando cotizaciones diarias de ExchangeRate-API y los códigos de moneda de Unicode CLDR. Mostrar código ISO y nombre de la moneda en español, como COP y pesos colombianos. No usar el idioma como sustituto de la ubicación. Consultas con timeout; caché del país por 30 minutos y cotizaciones por hasta 24 horas, sin guardar la IP. Ante fallos conservar el precio en USD y un aviso breve de indisponibilidad. Incluir atribución de cotizaciones y actualizar la política de privacidad.

## Implementación

Proyecto independiente en `brote-de-fe-latam/`, salida `dist/`, sin framework ni backend. Reutilizar estilos públicos y estructura visual del sitio del propietario. Implementar desplazamiento de CTA a oferta, enlace real al checkout, preguntas frecuentes accesibles y CTA móvil fijo. Traducir también textos alternativos y metadatos. Se obtuvo el contenido de las tres políticas públicas originales: traducirlas fielmente y servirlas localmente, manteniendo la legislación de Brasil y el correo real de soporte.

Registrar un nuevo Site privado y publicarlo con Sites para revisión, sin modificar el dominio original. Conservar archivos editables y documentación de prompts.

## Verificación

Actualización del carrusel: encabezado «Católicos de todo el mundo ya comenzaron», navegación manual por flechas, puntos, teclado y desplazamiento táctil. Ocho tarjetas de ejemplo con nombre latino y ciudad/país debajo. Mientras no se reciban relatos verificables, marcar cada tarjeta como «Ejemplo ilustrativo» y explicar que nombres y relatos son ficticios. No reasignar los testimonios brasileños a otras personas o países.

Revisar visualmente en escritorio y móvil, confirmar las cuatro artes, ausencia de textos portugueses en la página de venta, imágenes sin errores, navegación a oferta, FAQ y destino de compra. Comprobar que no haya desbordamiento horizontal. El checkout externo y el PDF del ebook quedan fuera de la traducción de esta página.
