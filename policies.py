from pathlib import Path
from meta_pixel import META_PIXEL
from html import escape

ROOT = Path(__file__).resolve().parent
DATA = {
'privacidad': ('Política de privacidad', [
('', 'Tu privacidad es importante para nosotros. Esta política explica qué datos personales recopila Brote de Fe, cómo los utilizamos y cuáles son tus derechos, de conformidad con la Ley General de Protección de Datos de Brasil (LGPD, Ley n.º 13.709/2018).'),
('1. Quiénes somos', 'Brote de Fe es un proyecto de contenido católico que comercializa materiales digitales, como el ebook «El camino de las 73 raíces». Puedes contactarnos en cualquier momento escribiendo a suporte@brotodefe.com.br.'),
('2. Datos que recopilamos', 'Al realizar una compra o registrarte, podemos recopilar tu nombre, correo electrónico e información de la transacción (producto adquirido, importe y fecha). Los datos de pago, como el número de tarjeta y los datos bancarios, son tratados exclusivamente por la plataforma de pagos Hotmart; nosotros no tenemos acceso a ellos.\nTambién recopilamos automáticamente datos de navegación, como páginas visitadas, origen del acceso e interacciones con el sitio, mediante cookies y herramientas de análisis.'),
('3. Cómo utilizamos tus datos', 'Utilizamos los datos para procesar y entregar tu compra; enviar el material adquirido y las comunicaciones relacionadas con el pedido; ofrecer soporte; mejorar el contenido y la experiencia del sitio; y mostrar anuncios relevantes sobre nuestros materiales.'),
('4. Cookies y herramientas de terceros', 'Utilizamos herramientas de análisis y marketing que pueden recopilar datos de navegación anónimos o seudónimos, entre ellas Meta Pixel (Facebook), Google Analytics y Google Ads, Taboola y UTMify (seguimiento del origen de las ventas). Estas herramientas pueden utilizar cookies para personalizar anuncios y medir los resultados de las campañas.\nPara mostrar un equivalente aproximado del precio en tu moneda, el navegador consulta GeoJS para identificar el país a partir de la dirección IP y ExchangeRate-API para obtener los tipos de cambio. Al recibir estas conexiones, esos proveedores pueden tratar la dirección IP y los datos técnicos habituales de una solicitud web. No solicitamos acceso al GPS ni guardamos tu dirección IP en el almacenamiento del sitio. Conservamos temporalmente en tu navegador solo el código del país y las cotizaciones para reducir consultas repetidas.\nPuedes desactivar las cookies y el almacenamiento local en la configuración de tu navegador o gestionar la personalización de anuncios desde tu cuenta de Google o Facebook.'),
('5. Intercambio de datos', 'No vendemos ni cedemos tus datos personales a terceros para sus propios fines. Compartimos únicamente lo necesario con Hotmart, para procesar pagos y entregar el producto digital, y con los proveedores de análisis y marketing mencionados, siempre dentro de los límites de esta política y de la LGPD.'),
('6. Seguridad y conservación', 'Adoptamos medidas técnicas y organizativas para proteger tus datos contra accesos no autorizados. Conservamos los datos únicamente durante el tiempo necesario para cumplir las finalidades descritas en esta política o las obligaciones legales.'),
('7. Tus derechos', 'De acuerdo con la LGPD, puedes solicitar en cualquier momento la confirmación del tratamiento de tus datos; su acceso y corrección; la portabilidad; la anonimización, el bloqueo o la eliminación de datos innecesarios; y la revocación del consentimiento. Solo tienes que escribir a suporte@brotodefe.com.br.'),
('8. Actualizaciones de esta política', 'Esta política puede actualizarse periódicamente. Los cambios relevantes se reflejarán en esta página con una nueva fecha de actualización.'),
]),
'terminos': ('Términos de uso', [
('', 'Al utilizar este sitio y adquirir nuestros materiales digitales, aceptas los términos que se indican a continuación. Si no estás de acuerdo con alguna condición, te pedimos que no realices la compra.'),
('1. Sobre Brote de Fe', 'Brote de Fe es un proyecto de contenido católico dedicado a ayudar a los fieles a comprender la Biblia completa, sus 73 libros, de forma sencilla y accesible. Nuestro producto principal es el ebook «El camino de las 73 raíces».'),
('2. Compra y entrega del producto', 'Las compras se procesan a través de Hotmart. Después de confirmar el pago, recibirás por correo electrónico el acceso al material digital y las instrucciones para descargarlo o acceder a él.\nLos precios, condiciones y bonos son los que se muestran en la página de venta al momento de la compra y pueden modificarse sin previo aviso para compras futuras.'),
('3. Uso permitido del material', 'El material adquirido es de uso personal e intransferible. Puedes leerlo, imprimirlo para uso propio y consultarlo cuantas veces quieras.\nEstá prohibido reproducir, distribuir, revender, compartir el archivo o publicar el contenido, total o parcialmente, en cualquier medio físico o digital.'),
('4. Propiedad intelectual', 'Todo el contenido del sitio y de los materiales digitales, incluidos textos, diseño, nombre, marca e identidad visual, pertenece a Brote de Fe y está protegido por la legislación sobre derechos de autor. El uso no autorizado puede dar lugar a acciones judiciales.'),
('5. Naturaleza del contenido', 'El contenido tiene carácter educativo, devocional y pastoral. No sustituye la orientación espiritual personal, el asesoramiento profesional ni el Magisterio de la Iglesia. Las citas bíblicas utilizan versiones de dominio público o debidamente indicadas.'),
('6. Exención de responsabilidad', 'Nos esforzamos por mantener la información correcta y actualizada, pero no garantizamos que el sitio esté libre de errores o interrupciones temporales. No nos hacemos responsables de los perjuicios derivados del uso indebido del material o de decisiones tomadas con base en el contenido.'),
('7. Modificaciones de los términos', 'Estos términos pueden actualizarse en cualquier momento. El uso continuado del sitio después de la publicación de nuevas condiciones implica su aceptación.'),
('8. Contacto', 'Puedes enviar tus preguntas sobre estos términos a suporte@brotodefe.com.br.'),
]),
'reembolso': ('Política de reembolso', [
('', 'Queremos que quedes satisfecho con tu compra. Si el material no es lo que esperabas, el reembolso es sencillo y sin trámites complicados.'),
('1. Garantía de 7 días', 'Tienes 7 días naturales a partir de la fecha de compra para solicitar el reembolso íntegro sin necesidad de justificarlo. Este es el derecho de desistimiento previsto en el artículo 49 del Código de Defensa del Consumidor de Brasil y se respeta de forma incondicional.'),
('2. Cómo solicitarlo', 'Envía un correo a suporte@brotodefe.com.br con el asunto «Reembolso» e indica el correo electrónico utilizado para la compra.\nTambién puedes solicitarlo directamente en Hotmart, en la sección «Mis compras», dentro del plazo de garantía. Respondemos a las solicitudes en un plazo de hasta 24 horas, de lunes a viernes.'),
('3. Plazo y forma de devolución', 'Una vez confirmada la solicitud, Hotmart procesa el reembolso. El plazo para que el importe aparezca en tu estado de cuenta o cuenta bancaria depende de la entidad emisora de la tarjeta o del medio de pago; generalmente es de 5 a 15 días hábiles.'),
('4. Acceso al material después del reembolso', 'Con el reembolso, se desactiva el acceso al material digital adquirido. No hay reembolsos parciales: la compra se devuelve íntegramente dentro del plazo de garantía o se mantiene el acceso.'),
('5. Compras fuera del plazo de garantía', 'Si ya pasaron los 7 días, te pedimos que te comuniques con nosotros de todas formas. Evaluamos cada caso con cuidado y atención, especialmente las compras duplicadas o los problemas técnicos de acceso.'),
('6. Preguntas', 'Si tienes alguna pregunta sobre esta política, escribe a suporte@brotodefe.com.br.'),
]),
}

def build_policies():
    nav = '<nav aria-label="Políticas" class="flex flex-wrap justify-center gap-4">' + ''.join(f'<a href="../{key}/">{escape(title)}</a>' for key,(title,_) in DATA.items()) + '</nav>'
    for key,(title,sections) in DATA.items():
        content = ''.join((f'<h2>{escape(heading)}</h2>' if heading else '') + ''.join('<p>'+escape(p).replace('suporte@brotodefe.com.br','<a href="mailto:suporte@brotodefe.com.br">suporte@brotodefe.com.br</a>')+'</p>' for p in body.split('\n')) for heading,body in sections)
        page = f'''<!DOCTYPE html><html lang="es-419"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} — Brote de Fe</title><link rel="stylesheet" href="../../assets/styles.css"><link rel="stylesheet" href="../../assets/localization.css"><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">{META_PIXEL}</head><body><main class="policy"><a href="../../">← Brote de Fe</a><h1>{title}</h1><p class="updated">Última actualización: octubre de 2026</p>{content}<footer class="mt-10 border-t border-border py-8">{nav}<p class="text-center">© 2026 Brote de Fe</p></footer></main></body></html>'''
        dest = ROOT/'dist'/'politicas'/key
        dest.mkdir(parents=True,exist_ok=True)
        (dest/'index.html').write_text(page,encoding='utf-8')
    print('Built all 3 translated policy pages, preserving Brazilian legal references.')

if __name__ == '__main__':
    build_policies()
