"""Genera las 4 páginas del sitio C&E Contable con encabezado y pie compartidos."""
import pathlib, sys

OUT = pathlib.Path(sys.argv[1])
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@500;600;700'
         '&family=Bodoni+Moda:ital,opsz,wght@0,6..96,500..700;1,6..96,500..700&family=IBM+Plex+Mono:wght@400;500'
         '&family=IBM+Plex+Sans:wght@400;500;600&display=swap">\n'
         '<link rel="stylesheet" href="estilos.css">\n'
         '<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 64 64%27%3E%3Crect width=%2764%27 height=%2764%27 fill=%27%231F4E7E%27/%3E%3Ctext x=%2732%27 y=%2742%27 font-family=%27Georgia,serif%27 font-size=%2728%27 fill=%27white%27 text-anchor=%27middle%27%3EC%26amp;E%3C/text%3E%3C/svg%3E">\n')

PAGES = [("index.html", "Inicio"), ("servicios.html", "Servicios"), ("la-firma.html", "La firma"), ("contacto.html", "Contacto")]
# Páginas que solo se enlazan desde el pie de página
FOOTER_EXTRA = [("mision.html", "Misión, visión y valores")]

PEOPLE = [
    ("Jhonatan Estiben Correa Ángel", "Jhonatan E. Correa Ángel", "Contador Público y Financiero", "317 237 5824", "573172375824", "jcorrea@cyecontable.com"),
    ("Jaime Alonzo Usme Arbeláez", "Jaime A. Usme Arbeláez", "Contador Público", "310 498 0671", "573104980671", "jusme@cyecontable.com"),
]

AREAS = [
    ("c", "C", "Contables", "Servicios contables", "Asesoría · Outsourcing contable", [
        ("C-01", "Asesoría contable", "Somos su aliado para resolver cualquier inquietud sobre el proceso contable mensual de su empresa, garantizando el cumplimiento de normativas y mejores prácticas."),
        ("C-02", "Outsourcing contable", "Un equipo altamente capacitado y recursos tecnológicos de vanguardia para gestionar sus operaciones contables diarias, con un manejo eficiente y preciso de su información financiera."),
    ]),
    ("a", "A", "Administrativos", "Servicios administrativos", "Tesorería · Nómina · Seguridad social", [
        ("A-01", "Tesorería", "Gestionamos eficientemente los recursos financieros de su empresa, con un control óptimo de ingresos, egresos y disponibilidad de fondos."),
        ("A-02", "Nómina", "Manejo preciso y confiable del pago de salarios, garantizando el cumplimiento de normativas laborales y fiscales."),
        ("A-03", "Seguridad social", "Administramos y gestionamos las obligaciones de seguridad social, asegurando el bienestar y la tranquilidad de sus empleados."),
    ]),
    ("t", "T", "Tributarios", "Servicios tributarios", "Consultoría · Planeación · Outsourcing · Patrimonio", [
        ("T-01", "Consultoría tributaria", "Asesoramiento experto para cumplir sus obligaciones fiscales de manera eficiente y oportuna."),
        ("T-02", "Planeación tributaria", "Estrategias fiscales a la medida para optimizar su carga impositiva y mejorar la salud financiera de su empresa."),
        ("T-03", "Outsourcing tributario", "Gestión integral de sus procesos tributarios, para que usted pueda enfocarse en el crecimiento de su negocio."),
        ("T-04", "Planeación patrimonial", "Asesoramos a personas naturales en la estructuración societaria, financiera y fiscal de su patrimonio, asegurando su estabilidad y crecimiento."),
    ]),
    ("i", "I", "Auditorías internas", "Auditorías internas", "Estados financieros · Procedimientos · Verificación", [
        ("I-01", "Análisis de estados financieros", "Evaluamos la situación económica de su empresa con un estudio detallado de sus estados financieros, para facilitar decisiones estratégicas."),
        ("I-02", "Revisión de procedimientos", "Analizamos y optimizamos los procesos internos para lograr mayor eficiencia, cumplimiento normativo y mejores prácticas operativas."),
        ("I-03", "Verificación de información contable", "Validamos la exactitud y confiabilidad de la información contable, asegurando su cumplimiento con los principios y normativas vigentes."),
    ]),
]


def nav_items(current):
    out = []
    for href, label in PAGES:
        cur = ' aria-current="page"' if href == current else ""
        out.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    return "\n        ".join(out)


def header(current):
    items = nav_items(current)
    return f'''<div class="draft-banner" role="note"><span>Propuesta de diseño</span><span aria-hidden="true">·</span><span>JAC LAB</span><span aria-hidden="true">·</span><span>Borrador</span></div>
<a class="skip" href="#contenido">Saltar al contenido</a>
<header class="site-header wrap">
  <a class="logo" href="index.html" aria-label="C&amp;E Contable, inicio"><b>C&amp;E</b><span>CONTABLE</span></a>
  <nav class="menu" aria-label="Principal">
    <ul>
        {items}
    </ul>
  </nav>
  <div class="header-cta">
    <span class="phone">317 237 5824</span>
    <a class="btn btn-sm" href="contacto.html">Agenda una asesoría</a>
  </div>
  <details class="menu-mobile">
    <summary>Menú</summary>
    <ul>
        {items}
    </ul>
  </details>
</header>'''


def footer():
    people = "\n".join(
        f'<div><p class="who">{short}</p><p>{role}</p><p class="mono">{phone}</p><p class="mono">{mail}</p></div>'
        for _, short, role, phone, _, mail in PEOPLE)
    links = "\n".join(f'<li><a href="{h}">{l}</a></li>' for h, l in PAGES + FOOTER_EXTRA)
    return f'''<footer class="site-footer on-blue">
  <span class="lights" aria-hidden="true"></span>
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="logo" href="index.html" aria-label="C&amp;E Contable, inicio"><b>C&amp;E</b><span>CONTABLE</span></a>
        <p class="footer-motto">Para avanzar, rodéate siempre de los mejores.</p>
      </div>
      <div class="footer-col">
        <h2>Páginas</h2>
        <ul>
{links}
        </ul>
      </div>
      <div class="footer-col">
        <h2>Contacto</h2>
        <div class="footer-people">
{people}
        </div>
      </div>
    </div>
    <div class="footer-bottom"><span>© 2026 Cifras y Estrategias S.A.S. · C&amp;E Contable</span><span>Diseño y desarrollo: JAC LAB · Propuesta, todos los derechos reservados</span></div>
  </div>
</footer>'''


def page_hero(crumb, title, lead):
    return f'''<section class="page-hero on-blue">
  <span class="amp" aria-hidden="true">&amp;</span>
  <span class="lights" aria-hidden="true"></span>
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Inicio</a> / {crumb}</p>
    <h1 class="bodoni">{title}</h1>
    <p class="lead">{lead}</p>
  </div>
</section>'''


REASONS = '''<section class="section porque on-blue">
  <span class="lights" aria-hidden="true"></span>
  <div class="wrap">
    <p class="kicker">Por qué elegirnos</p>
    <h2 class="h2">Rigor en cada cifra, <em>cercanía</em> en cada decisión.</h2>
    <div class="reasons">
      <div class="reason"><span class="tag">Normativa</span><h3>Cumplimiento</h3><p>Trabajamos con las normativas contables, laborales y fiscales vigentes y con las mejores prácticas, para que su empresa esté siempre al día.</p></div>
      <div class="reason"><span class="tag">Herramientas</span><h3>Tecnología</h3><p>Recursos tecnológicos de vanguardia para gestionar sus operaciones con eficiencia y precisión.</p></div>
      <div class="reason"><span class="tag">Atención</span><h3>Integral y a la medida</h3><p>Soluciones personalizadas y secciones exclusivas para clientes, pensadas para las necesidades de su empresa.</p></div>
    </div>
  </div>
</section>'''

FACTS = '''<div class="facts">
          <div><b>4</b><span>Áreas</span></div>
          <div><b>12</b><span>Servicios</span></div>
          <div><b>2</b><span>Contadores públicos</span></div>
        </div>'''


def cta(title_html, text):
    return f'''<section class="section">
  <div class="wrap cta-strip">
    <div>
      <p class="kicker">Hablemos</p>
      <h2 class="h2">{title_html}</h2>
      <p class="lead">{text}</p>
    </div>
    <div class="actions">
      <a class="btn" href="contacto.html">Agenda una asesoría</a>
      <a class="btn btn-wa" href="https://wa.me/573172375824" target="_blank" rel="noopener">WhatsApp 317 237 5824</a>
    </div>
  </div>
</section>'''


# ---------------- Páginas ----------------
def inicio():
    rows = "\n".join(
        f'<a class="ledger-row" href="servicios.html#area-{k}"><span class="ref">{code}—</span><div><h3>{short}</h3><p>{summ}</p></div><span class="count">{len(items):02d}</span></a>'
        for k, code, short, _, summ, items in AREAS)
    partners = "\n".join(f'<div><p class="name">{short}</p><p class="role">{role}</p></div>' for _, short, role, *_ in PEOPLE)
    return "Inicio", f'''<header class="hero">
  <div class="hero-left">
    <div>
      <p class="eyebrow">Firma contable · Colombia</p>
      <h1 class="bodoni">Para avanzar, <em>rodéate siempre</em> de los mejores.</h1>
      <p class="lead">Contabilidad, finanzas, tributación y auditoría con soluciones a la medida de su empresa y de su patrimonio.</p>
      <div class="actions">
        <a class="btn" href="contacto.html">Agenda una asesoría</a>
        <a class="textlink" href="servicios.html">Ver los 12 servicios&nbsp;&nbsp;→</a>
      </div>
    </div>
    <div class="partners">
{partners}
    </div>
  </div>
  <aside class="band on-blue" aria-label="Áreas de servicio">
    <span class="amp" aria-hidden="true">&amp;</span>
    <span class="lights" aria-hidden="true"></span>
    <div class="ledger">
      <div class="ledger-head"><span>Ref.</span><span>Área</span><span>Servicios</span></div>
{rows}
      <div class="ledger-total"><span>Total</span><span>12</span></div>
    </div>
  </aside>
</header>

<section class="section white">
  <div class="wrap firma-grid">
    <div>
      <p class="kicker">La firma</p>
      <h2 class="h2">Un solo aliado para los <em>números</em> de su empresa.</h2>
      {FACTS}
    </div>
    <div class="firma-text">
      <p>Encontrará nuestra oferta completa en contabilidad, finanzas, tributación y auditoría, diseñada para brindarle soluciones efectivas y personalizadas.</p>
      <p>Además, hemos creado secciones exclusivas para nuestros clientes, con el objetivo de atender sus necesidades corporativas de manera integral.</p>
      <a class="textlink" href="la-firma.html">Conoce la firma y el equipo&nbsp;&nbsp;→</a>
    </div>
  </div>
</section>

{REASONS}

{cta('¿Listo para poner sus <em>números</em> en orden?', 'Cuéntenos qué necesita su empresa y le respondemos con una propuesta a la medida.')}'''


def servicios():
    index = "\n".join(
        f'<a href="#area-{k}"><span class="code">{code} —</span><b>{short}</b><span>{len(items):02d} servicios</span></a>'
        for k, code, short, _, _, items in AREAS)
    blocks = []
    for k, code, short, title, _, items in AREAS:
        lis = "\n".join(f'<li><span class="ref">{r}</span><div><h3>{n}</h3><p>{d}</p></div></li>' for r, n, d in items)
        blocks.append(f'''<article class="area" id="area-{k}">
        <div class="area-title"><span class="code">{code} — {short}</span><h2>{title}</h2><span class="n">{len(items):02d} servicios</span></div>
        <ul class="entries">
{lis}
        </ul>
      </article>''')
    blocks = "\n\n      ".join(blocks)
    return "Servicios", f'''{page_hero("Servicios", "Libro de <em>servicios</em>", "Cuatro áreas y doce servicios que cubren el ciclo completo de su información financiera: del registro diario a la auditoría.")}

<section class="section">
  <div class="wrap">
    <nav class="area-index" aria-label="Áreas de servicio">
{index}
    </nav>

      {blocks}

    <div class="servicios-total"><span>Total</span><span>12 servicios · 4 áreas</span></div>
  </div>
</section>

{cta('¿No sabe qué servicio <em>necesita</em>?', 'Escríbanos y le ayudamos a identificar qué área se ajusta mejor a su empresa.')}'''


def member_card(full, short, role, phone, wa, mail, idx):
    return f'''<article class="member">
        <div>
          <span class="mono-tag">Contador {idx:02d}</span>
          <h3>{full}</h3>
          <p class="role">{role}</p>
        </div>
        <dl>
          <dt>WhatsApp</dt><dd>{phone}</dd>
          <dt>Correo</dt><dd>{mail}</dd>
        </dl>
        <a class="btn btn-wa btn-sm" href="https://wa.me/{wa}" target="_blank" rel="noopener">Escribir por WhatsApp</a>
      </article>'''


def firma():
    cards = "\n      ".join(member_card(*p, i + 1) for i, p in enumerate(PEOPLE))
    return "La firma", f'''{page_hero("La firma", "Una firma para los <em>números</em> de su empresa", "Contabilidad, finanzas, tributación y auditoría con trato directo de contadores públicos.")}

<section class="section white">
  <div class="wrap firma-grid">
    <div>
      <p class="kicker">Quiénes somos</p>
      <h2 class="h2">Soluciones efectivas y <em>personalizadas</em>.</h2>
      {FACTS}
    </div>
    <div class="firma-text">
      <p>Bienvenido a nuestro portafolio de servicios. Aquí encontrará nuestra oferta completa en contabilidad, finanzas, tributación y auditoría, diseñada para brindarle soluciones efectivas y personalizadas.</p>
      <p>Además, hemos creado secciones exclusivas para nuestros clientes, con el objetivo de atender sus necesidades corporativas de manera integral.</p>
      <a class="textlink" href="mision.html">Nuestra misión, visión y valores&nbsp;&nbsp;→</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="kicker">Equipo</p>
    <h2 class="h2">Las personas detrás de sus <em>números</em>.</h2>
    <div class="team">
      {cards}
    </div>
  </div>
</section>

<section class="section white">
  <div class="wrap">
    <blockquote class="motto">“Para avanzar, rodéate siempre de los mejores.”<span class="motto-src">Lema de C&amp;E Contable</span></blockquote>
  </div>
</section>

{REASONS}'''


def contacto():
    cards = "\n        ".join(member_card(*p, i + 1) for i, p in enumerate(PEOPLE))
    options = "\n".join(f'<option>{title}</option>' for *_, title, _, _ in [(a[0], a[1], a[2], a[3], a[4], a[5]) for a in AREAS])
    return "Contacto", f'''{page_hero("Contacto", "Hablemos de su <em>empresa</em>", "Escríbanos por WhatsApp o déjenos sus datos y le contactamos.")}

<section class="section">
  <div class="wrap contact-grid">
    <div>
      <p class="kicker">Contacto directo</p>
      <div class="contact-cards">
        {cards}
      </div>
    </div>
    <form class="form" id="form-contacto" novalidate>
      <h2>Solicitar asesoría</h2>
      <div class="field"><label for="f-nombre">Nombre</label><input id="f-nombre" name="nombre" autocomplete="name" required></div>
      <div class="field"><label for="f-empresa">Empresa</label><input id="f-empresa" name="empresa" autocomplete="organization"></div>
      <div class="field"><label for="f-correo">Correo</label><input id="f-correo" name="correo" type="email" autocomplete="email" required></div>
      <div class="field"><label for="f-tel">Teléfono / WhatsApp</label><input id="f-tel" name="telefono" type="tel" autocomplete="tel"></div>
      <div class="field full"><label for="f-area">Servicio de interés</label>
        <select id="f-area" name="area">
          <option value="">Seleccione un área</option>
{options}
          <option>No estoy seguro</option>
        </select>
      </div>
      <div class="field full"><label for="f-msg">Mensaje</label><textarea id="f-msg" name="mensaje" placeholder="Cuéntenos brevemente qué necesita su empresa"></textarea></div>
      <button class="btn" type="submit">Enviar por WhatsApp</button>
      <p class="form-note">Al enviar, se abrirá WhatsApp con su solicitud lista para mandar.</p>
      <p class="form-status" id="form-status" role="status" hidden></p>
    </form>
  </div>
</section>
<script>
  (function () {{
    var form = document.getElementById('form-contacto');
    var status = document.getElementById('form-status');
    form.addEventListener('submit', function (e) {{
      e.preventDefault();
      var nombre = form.nombre.value.trim();
      var correo = form.correo.value.trim();
      if (!nombre || !correo || correo.indexOf('@') < 1) {{
        status.textContent = 'Escriba su nombre y un correo válido para continuar.';
        status.hidden = false;
        return;
      }}
      var lineas = ['Hola, C&E Contable. Quiero solicitar una asesoría.', 'Nombre: ' + nombre];
      if (form.empresa.value.trim()) lineas.push('Empresa: ' + form.empresa.value.trim());
      lineas.push('Correo: ' + correo);
      if (form.telefono.value.trim()) lineas.push('Teléfono: ' + form.telefono.value.trim());
      if (form.area.value) lineas.push('Servicio de interés: ' + form.area.value);
      if (form.mensaje.value.trim()) lineas.push('Mensaje: ' + form.mensaje.value.trim());
      var url = 'https://wa.me/573172375824?text=' + encodeURIComponent(lineas.join('\\n'));
      status.innerHTML = 'Abriendo WhatsApp… Si no se abre, <a href="' + url + '" target="_blank" rel="noopener">pulse aquí</a>.';
      window.open(url, '_blank', 'noopener');
      status.hidden = false;
    }});
  }})();
</script>'''


def doc(fname, title, body, full=True):
    page_title = "C&amp;E Contable" if title == "Inicio" else f"{title} · C&amp;E Contable"
    desc = "Firma contable C&amp;E Contable: contabilidad, finanzas, tributación y auditoría."
    main = f'{header(fname)}\n<main id="contenido">\n{body}\n</main>\n{footer()}\n'
    if full:
        return (f'<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
                f'<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
                f'<title>{page_title}</title>\n<meta name="description" content="{desc}">\n{FONTS}\n</head>\n<body>\n{main}</body>\n</html>\n')
    # Variante para la vista previa (el visor agrega el esqueleto html/head/body)
    return f'<title>{page_title}</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n{FONTS}\n{main}'



VALORES = [
    ("Respeto", "Reconocemos la dignidad, los derechos y las opiniones de cada persona en Cifras y Estrategias S.A.S., con un ambiente de tolerancia, comunicación asertiva y trato justo entre colaboradores, clientes y aliados estratégicos."),
    ("Verdad", "Actuamos con transparencia en cada uno de los procesos de la organización. Al actuar con veracidad fortalecemos la confianza de los clientes y garantizamos la integridad profesional."),
    ("Solidaridad", "Trabajamos de forma colaborativa, con empatía, sentido de pertenencia y apoyo mutuo entre los miembros del equipo, y promovemos la cooperación como base del crecimiento conjunto y de un entorno armonioso."),
    ("Compromiso", "Asumimos con responsabilidad los objetivos que nos planteamos, en coherencia con la identidad de la organización, para asegurar la excelencia en los servicios y cumplir las metas establecidas."),
    ("Confianza", "Consolidamos relaciones sólidas, creíbles y estables en el tiempo, dentro y fuera de la firma, con transparencia, cumplimiento de los compromisos y coherencia en el actuar diario."),
]

PROCESOS = [
    ("E", "Procesos estratégicos", "estrategicos", ["Planeación estratégica", "Gestión administrativa", "Gestión de calidad", "Direccionamiento organizacional"]),
    ("M", "Procesos misionales", "misionales", ["Asesoría contable", "Asesoría tributaria", "Gestión financiera", "Atención al cliente"]),
    ("A", "Procesos de apoyo", "apoyo", ["Gestión del talento humano", "Gestión documental", "Gestión tecnológica", "Gestión financiera interna", "Gestión legal y cumplimiento normativo"]),
    ("C", "Evaluación y control", "control", ["Control interno", "Auditoría administrativa", "Evaluación del desempeño", "Indicadores de gestión", "Productividad del personal"]),
]


def mision():
    valores = "\n".join(
        f'<li><span class="ref">V-{i + 1:02d}</span><h3>{n}</h3><p>{d}</p></li>' for i, (n, d) in enumerate(VALORES))
    filas = []
    for code, title, cls, items in PROCESOS:
        steps = "".join(f'<li>{it}</li>' for it in items)
        tag = ' <span class="tag">Clave del negocio</span>' if cls == "misionales" else ""
        filas.append(f'<div class="pm-row pm-{cls}"><p class="pm-title"><span class="code">{code}—</span>{title}{tag}</p><ol>{steps}</ol></div>')
    filas = "\n        ".join(filas)
    return "Misión, visión y valores", f'''{page_hero('<a href="la-firma.html">La firma</a> / Misión', 'Misión, visión <em>y valores</em>', 'Los principios que guían a Cifras y Estrategias S.A.S. en cada asesoría.')}

<section class="section white">
  <div class="wrap statement">
    <div class="statement-label"><p class="kicker">Misión</p><span class="mono-note">Lo que hacemos hoy</span></div>
    <p class="statement-text">Brindar servicios integrales de asesoría <em>contable, financiera y tributaria</em> a personas naturales y jurídicas, mediante procesos confiables, transparentes y orientados al cumplimiento normativo, enfocados en generar valor estratégico que contribuya a la sostenibilidad, competitividad y desarrollo empresarial de nuestros clientes, garantizando altos estándares de calidad y ética profesional.</p>
  </div>
</section>

<section class="section vision on-blue">
  <span class="amp" aria-hidden="true">&amp;</span>
  <span class="lights" aria-hidden="true"></span>
  <div class="wrap vision-grid">
    <div><p class="kicker">Visión</p><p class="year" aria-label="Año 2030">2030</p><span class="mono-note">Medellín</span></div>
    <p class="statement-text">Para el año 2030, Cifras y Estrategias S.A.S. será reconocida en Medellín como una firma contable <em>innovadora, confiable y altamente profesional</em>, destacada por sus procesos administrativos sólidos, su adopción de tecnologías digitales y su contribución al fortalecimiento empresarial de pequeñas y medianas organizaciones.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="servicios-head">
      <div><p class="kicker">Valores corporativos</p><h2 class="h2">Cinco principios en el <em>actuar diario</em>.</h2></div>
      <p>Son los principios éticos y morales de nuestra cultura: guían el trabajo del equipo y la forma en que nos relacionamos con clientes, proveedores y la comunidad.</p>
    </div>
    <ul class="values">
{valores}
    </ul>
  </div>
</section>

<section class="section white">
  <div class="wrap">
    <div class="servicios-head">
      <div><p class="kicker">Cómo trabajamos</p><h2 class="h2">Mapa de <em>procesos</em></h2></div>
      <p>Cuatro grupos de procesos conectan lo que cada cliente necesita con su satisfacción final.</p>
    </div>
    <div class="pm" role="group" aria-label="Mapa de procesos">
      <p class="pm-end pm-in"><span>Entrada</span>Necesidades del cliente</p>
      <div class="pm-body">
        {filas}
      </div>
      <p class="pm-end pm-out"><span>Resultado</span>Satisfacción del cliente</p>
    </div>
  </div>
</section>

{cta('Trabajemos juntos con <em>estos valores</em>.', 'Cuéntenos qué necesita su empresa y le respondemos con una propuesta a la medida.')}'''

builders = {"index.html": inicio, "servicios.html": servicios, "la-firma.html": firma, "contacto.html": contacto, "mision.html": mision}
OUT.mkdir(parents=True, exist_ok=True)
for fname, fn in builders.items():
    title, body = fn()
    (OUT / fname).write_text(doc(fname, title, body), encoding="utf-8")
    if fname == "index.html" and "--preview" in sys.argv:
        (OUT.parent / "preview-index.html").write_text(doc(fname, title, body, full=False), encoding="utf-8")
print("ok", sorted(p.name for p in OUT.iterdir()))
