"""Build the faithful, framework-free Spanish localization from the owner's page."""
from pathlib import Path
from bs4 import BeautifulSoup, Comment
import json
import shutil

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent
OUT = ROOT / 'dist'
T = {
'Oferta de lançamento:':'Oferta de lanzamiento:',
'Ebook completo com':'Ebook completo con',
'50% de desconto':'50% de descuento',
'Para católicos que querem entender a Bíblia':'Para católicos que quieren comprender la Biblia',
'Um guia devocional claro, breve e fiel à Tradição — para que você pare de se sentir perdido e comece a ler a Palavra com confiança, incluindo os':'Una guía devocional clara, breve y fiel a la Tradición para que dejes de sentirte perdido y comiences a leer la Palabra con confianza, incluidos los',
'7 livros que só a Bíblia católica preserva':'7 libros que conserva la Biblia Católica',
'Os 73 livros explicados em linguagem simples':'Los 73 libros explicados en un lenguaje sencillo',
'Voz dos Padres e Doutores da Igreja':'La voz de los Padres y Doctores de la Iglesia',
'Como cada livro aponta para Cristo e para a Liturgia':'Cómo cada libro apunta a Cristo y a la Liturgia',
'Uma oração final para cada um':'Una oración final para cada libro',
'QUERO MEU EBOOK AGORA':'QUIERO MI EBOOK AHORA',
'Acesso imediato · Garantia de 7 dias':'Acceso inmediato · Garantía de 7 días',
'4.9/5':'4,9/5',
'+2.000 leitores em todo o Brasil':'+2.000 lectores en todo Brasil',
'Recomendado por catequistas':'Recomendado por catequistas',
'Soa familiar?':'¿Te resulta familiar?',
'Você quer ler a Bíblia… mas não sabe por onde começar':'Quieres leer la Biblia… pero no sabes por dónde empezar',
'Você abre o Antigo Testamento e tudo parece confuso, distante, sem conexão com você.':'Abres el Antiguo Testamento y todo parece confuso, lejano y sin conexión con tu vida.',
"Disseram que é 'o livro mais importante da sua vida', mas ninguém te ensinou como lê-lo.":'Te dijeron que es «el libro más importante de tu vida», pero nadie te enseñó a leerlo.',
'Você sente santa inveja de quem cita versículos com naturalidade — queria o mesmo.':'Sientes una sana envidia de quienes citan versículos con naturalidad. Te gustaría poder hacerlo también.',
'"A culpa não é sua. Ninguém te deu um mapa — só um livro de 1.500 páginas e a esperança de que você adivinhasse o caminho."':'«No es tu culpa. Nadie te dio un mapa: solo un libro de 1.500 páginas y la esperanza de que encontraras el camino por tu cuenta».',
'A solução':'La solución',
'Broto de Fé é o mapa que nunca te deram':'Brote de Fe es el mapa que nunca te dieron',
'Um ebook devocional com':'Un ebook devocional con',
'uma raiz por livro':'una raíz por libro',
': cada capítulo se lê em 5–10 minutos, com autor, contexto, temas centrais, voz da Tradição e uma oração final.':': cada capítulo se lee en 5 a 10 minutos e incluye autor, contexto, temas centrales, la voz de la Tradición y una oración final.',
'Quando terminar, você vai conhecer os':'Al terminar, conocerás los',
'73 livros':'73 libros',
'da Bíblia Católica — incluindo os 7 deuterocanônicos que muitas Bíblias modernas tiraram.':'de la Biblia Católica, incluidos los 7 deuterocanónicos que no aparecen en muchas ediciones modernas.',
'Sem tecnicismos':'Sin tecnicismos',
'Fiel à Tradição':'Fiel a la Tradición',
'Leitura diária':'Lectura diaria',
'Para toda a família':'Para toda la familia',
'O que você vai encontrar dentro':'Lo que encontrarás en el ebook',
'Cada livro, uma raiz que floresce':'Cada libro, una raíz que florece',
'Autor e época':'Autor y época',
'Quem escreveu e quando — sem academicismos.':'Quién lo escribió y cuándo, sin complicaciones académicas.',
'Contexto histórico':'Contexto histórico',
'Por que foi escrito e para quem.':'Por qué se escribió y para quién.',
'Temas centrais':'Temas centrales',
'O essencial que você precisa saber.':'Lo esencial que necesitas saber.',
'Como aponta para Cristo':'Cómo apunta a Cristo',
'A chave católica de leitura.':'La clave católica para su lectura.',
'Voz da Tradição':'La voz de la Tradición',
'Citações de Padres e Doutores.':'Citas de los Padres y Doctores de la Iglesia.',
'Na Liturgia':'En la Liturgia',
'Onde você o ouve na Missa.':'Cuándo lo escuchas en la Misa.',
'Oração final':'Oración final',
'Para encerrar o dia com a Palavra.':'Para terminar el día con la Palabra.',
'A transformação':'La transformación',
'Antes do Broto de Fé vs. depois':'Antes y después de Brote de Fe',
'Antes':'Antes',
'Você abre a Bíblia e fecha sem ler':'Abres la Biblia y la cierras sin leer',
'Não sabe diferenciar Antigo e Novo Testamento':'No distingues entre el Antiguo y el Nuevo Testamento',
'Se perde com os profetas e os livros sapienciais':'Te pierdes entre los profetas y los libros sapienciales',
'Sente a fé distante, sem alimento diário':'Sientes tu fe lejana, sin alimento diario',
'Depois':'Después',
'Você sabe o que ler e por quê, todo dia':'Sabes qué leer y por qué, cada día',
'Conhece os 73 livros e seu lugar na história da salvação':'Conoces los 73 libros y su lugar en la historia de la salvación',
'Lê com o olhar da Igreja, sem dúvidas':'Lees con la mirada de la Iglesia y con confianza',
'Sua oração diária tem raiz e fruto':'Tu oración diaria tiene raíces y da fruto',
'É para você?':'¿Es para ti?',
'Broto de Fé foi feito pensando em você se…':'Brote de Fe está pensado para ti si…',
'Você é católico (ou quer se aproximar) e quer conhecer a Bíblia completa.':'Eres católico (o quieres acercarte a la fe) y deseas conocer la Biblia completa.',
'Está cansado de explicações longas e acadêmicas.':'Estás cansado de explicaciones largas y académicas.',
'Busca um material breve para a sua oração diária.':'Buscas un material breve para tu oración diaria.',
'Quer formar a sua família com a fé de sempre.':'Quieres formar a tu familia en la fe de siempre.',
'É catequista, padrinho, líder de grupo ou catecúmeno.':'Eres catequista, padrino, madrina, líder de grupo o catecúmeno.',
'Precisa de um guia simples — sem perder profundidade.':'Necesitas una guía sencilla que conserve la profundidad.',
'O que dizem os leitores':'Lo que dicen los lectores',
'Católicos de todo o Brasil já começaram':'Católicos de todo Brasil ya comenzaron',
'Eu lia a Bíblia sem entender. Com o Broto de Fé finalmente tenho uma ordem e um guia católico que respeita a Tradição.':'Leía la Biblia sin entenderla. Con Brote de Fe por fin tengo un orden y una guía católica que respeta la Tradición.',
'Leio no celular antes de dormir. Dez minutos por dia e minha fé mudou. Vale muito mais do que custa.':'Lo leo en el celular antes de dormir. Diez minutos al día y mi fe cambió. Vale mucho más de lo que cuesta.',
'Dei de presente para minha mãe e agora oramos juntas pelo WhatsApp. É claro, breve e profundamente católico.':'Se lo regalé a mi mamá y ahora rezamos juntas por WhatsApp. Es claro, breve y profundamente católico.',
'Por trás do livro':'Detrás del libro',
'Escrito com amor à Igreja e respeito à Tradição':'Escrito con amor a la Iglesia y respeto por la Tradición',
'Broto de Fé nasceu da necessidade real de tantos católicos que amam a Cristo mas não encontram um material claro e fiel. Cada raiz foi revisada com o':'Brote de Fe nació de la necesidad real de tantos católicos que aman a Cristo, pero no encuentran un material claro y fiel. Cada raíz se revisó con el',
'Catecismo da Igreja Católica':'Catecismo de la Iglesia Católica',
'e a tradição dos Padres à mão.':'y la tradición de los Padres a la mano.',
'Inclui os 7 livros deuterocanônicos':'Incluye los 7 libros deuterocanónicos',
'Linguagem reverente, não protestantizada':'Lenguaje reverente y fiel a la tradición católica',
'Citações de Santos e Doutores em cada livro':'Citas de santos y Doctores de la Iglesia en cada libro',
'Seu investimento hoje':'Tu inversión hoy',
'Tudo o que você recebe ao comprar o Broto de Fé':'Todo lo que recibes al comprar Brote de Fe',
'Ebook Broto de Fé - A Jornada das 73 Raízes':'Ebook Brote de Fe — El camino de las 73 raíces',
'BÔNUS #1 · Plano de leitura de 90 dias':'BONO #1 · Plan de lectura de 90 días',
'BÔNUS #2 · Mini-guia para orar com a Palavra':'BONO #2 · Miniguía para orar con la Palabra',
'BÔNUS #3 · Calendário litúrgico para imprimir':'BONO #3 · Calendario litúrgico para imprimir',
'BÔNUS #4 · Guia da missa passo a passo':'BONO #4 · Guía de la Misa paso a paso',
'Valor total':'Valor total',
'Hoje você paga apenas':'Hoy pagas solo',
'Pagamento único · acesso vitalício':'Pago único · acceso de por vida',
'Pagamento seguro':'Pago seguro',
'Acesso imediato':'Acceso inmediato',
'Qualquer dispositivo':'Cualquier dispositivo',
'Garantia incondicional':'Garantía incondicional',
'7 dias para ler com tranquilidade':'7 días para leer con tranquilidad',
'Se nos primeiros 7 dias o ebook não for o que você esperava, basta escrever para a Hotmart e você recebe':'Si durante los primeros 7 días el ebook no es lo que esperabas, solo tienes que contactar a Hotmart y recibirás',
'100% do seu dinheiro de volta':'el 100% de tu dinero de vuelta',
'. Sem perguntas, sem burocracia. O risco é nosso.':'. Sin preguntas ni trámites complicados. Nosotros asumimos el riesgo.',
'Perguntas frequentes':'Preguntas frecuentes',
'Vamos esclarecer suas dúvidas antes da compra':'Resolvemos tus dudas antes de comprar',
'Como recebo o ebook?':'¿Cómo recibo el ebook?',
'Em quais dispositivos posso ler?':'¿En qué dispositivos puedo leerlo?',
'Como funciona o pagamento?':'¿Cómo funciona el pago?',
'É católico de verdade?':'¿Es realmente católico?',
'E se eu não gostar?':'¿Y si no me gusta?',
'Preciso ser teólogo para entender?':'¿Necesito ser teólogo para entenderlo?',
'Comece hoje':'Comienza hoy',
'A Palavra que nutriu 2.000 anos de santos — agora no seu celular':'La Palabra que alimentó a los santos durante 2.000 años, ahora en tu celular',
'Por menos do preço de uma pizza, leve com você os 73 livros da Bíblia Católica com a sabedoria da Tradição.':'Por menos de lo que cuesta una pizza, lleva contigo los 73 libros de la Biblia Católica y la sabiduría de la Tradición.',
'R$47,90 · pagamento único · acesso vitalício':'R$47,90 · pago único · acceso de por vida',
'P.S.:':'P. D.:',
'Lembre-se que você tem 7 dias de garantia total. Se não for para você, devolvemos cada centavo. A única coisa que você pode perder é a oportunidade de finalmente entender a Bíblia.':'Recuerda que tienes 7 días de garantía total. Si no es para ti, te devolvemos cada centavo. Lo único que puedes perder es la oportunidad de comprender por fin la Biblia.',
'Política de Privacidade':'Política de privacidad',
'Termos de Uso':'Términos de uso',
'Política de Reembolso':'Política de reembolso',
'Broto de Fé':'Brote de Fe',
'Pagamentos processados pela Hotmart':'Pagos procesados por Hotmart',
}

FAQ = [
'Después de confirmar el pago, recibirás un correo de Hotmart con el enlace para descargar el PDF. El acceso es inmediato y de por vida.',
'En cualquier celular, tablet, computadora o lector de libros electrónicos compatible con PDF. También puedes imprimirlo en formato A5.',
'Hotmart procesa el pago y muestra los medios disponibles según tu país. En Brasil, la oferta original admite tarjeta de crédito, Pix y boleto bancario. El acceso se habilita automáticamente cuando se confirma el pago.',
'Sí. Incluye los 73 libros, con los 7 deuterocanónicos, respeta el Magisterio, cita a los Padres y Doctores de la Iglesia y conecta cada libro con la Liturgia.',
'Tienes 7 días de garantía total. Solicita el reembolso a Hotmart y recibirás el 100% de tu dinero de vuelta, sin preguntas.',
'No. Está escrito en un lenguaje claro y reverente para que cualquier persona pueda comprenderlo dedicando unos minutos al día.',
]

def build():
    soup = BeautifulSoup((ROOT / 'source.html').read_text(encoding='utf-8'), 'html.parser')
    main = soup.main.extract()
    untouched = []
    for t in list(main.find_all(string=True)):
        if isinstance(t, Comment):
            t.extract()
            continue
        k = str(t).strip()
        if k in T:
            raw = str(t)
            t.replace_with(raw[:len(raw)-len(raw.lstrip())] + T[k] + raw[len(raw.rstrip()):])
        elif k and not all(c.isdigit() or c in 'R$.,→•©" ' for c in k) and k not in ['Maria Fernanda','São Paulo, SP','Carlos A.','Belo Horizonte, MG','Lúcia R.','Curitiba, PR']:
            untouched.append(k)
    if untouched:
        raise ValueError(f'Untranslated text: {untouched}')
    alt = ['Ebook Brote de Fe: portada digital en español','Los 73 libros de la Biblia: beneficios de Brote de Fe','Ejemplo de lectura: Génesis en español','Lectora con el ebook Brote de Fe en español']
    files = ['01-portada.webp','02-beneficios.webp','04-genesis.webp','03-lectura.webp']
    for i, img in enumerate(main.find_all('img')):
        img['src'] = '/assets/' + files[i]
        img['alt'] = alt[i]
        img.attrs.pop('srcset', None)
        img['width'] = '1024'
        img['height'] = '1024'
    for button in main.select('button.cta-pulse'):
        button.name = 'a'
        button.attrs.pop('type',None)
        button['href'] = '#comprar'
    for i, button in enumerate(main.select('[data-section="faq"] button')):
        button['type'] = 'button'
        button['aria-expanded'] = 'false'
        button['aria-controls'] = f'faq-answer-{i}'
        button['id'] = f'faq-question-{i}'
        panel = soup.new_tag('p', id=f'faq-answer-{i}', attrs={'class':'mt-3 text-muted-foreground','hidden':'','role':'region','aria-labelledby':f'faq-question-{i}'})
        panel.string = FAQ[i]
        button.insert_after(panel)
    for a in main.select('footer a'):
        a['href'] = {'/politicas/privacidade':'/politicas/privacidad/','/politicas/termos':'/politicas/terminos/','/politicas/reembolso':'/politicas/reembolso/'}[a['href']]
    main.select_one('nav')['aria-label'] = 'Políticas'
    h1 = soup.new_tag('h1',attrs={'class':'sr-only'})
    h1.string = 'Brote de Fe — El camino de las 73 raíces'
    main.select_one('[data-section="hero"]').insert(0,h1)
    sticky = soup.new_tag('div',attrs={'class':'mobile-buy','aria-label':'Comprar Brote de Fe'})
    sticky.append(BeautifulSoup('<div><strong>R$47,90</strong><small>Pago único · 7 días de garantía</small></div><a href="#comprar">QUIERO MI EBOOK <span aria-hidden="true">→</span></a>', 'html.parser'))
    main.append(sticky)
    description = 'Comprende los 73 libros de la Biblia Católica con una guía devocional clara, breve y fiel a la Tradición.'
    head = f'''<!DOCTYPE html><html lang="es-419"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Brote de Fe — El camino de las 73 raíces</title><meta name="description" content="{description}"><meta name="theme-color" content="#0e2654"><link rel="preload" as="image" href="/assets/01-portada.webp"><link rel="stylesheet" href="/assets/styles.css"><link rel="stylesheet" href="/assets/localization.css"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"><link rel="canonical" href="https://brote-de-fe-latam.chalkybox3.chatgpt.site/"><meta property="og:title" content="Brote de Fe — El camino de las 73 raíces"><meta property="og:description" content="{description}"><meta property="og:type" content="website"><meta property="og:locale" content="es_LA"><meta property="og:image" content="https://brote-de-fe-latam.chalkybox3.chatgpt.site/assets/01-portada.webp"><meta name="twitter:card" content="summary_large_image"></head><body>'''
    (OUT/'index.html').write_text(head+str(main)+'<script src="/assets/app.js" defer></script></body></html>',encoding='utf-8')
    print('Built Spanish page: all original text nodes translated, 4 localized images, 6 FAQ answers.')

if __name__ == '__main__':
    build()
