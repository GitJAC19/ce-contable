# C&E Contable · Sitio web

Sitio estático de la firma C&E Contable: contabilidad, finanzas, tributación y auditoría.

**Propuesta de diseño · JAC LAB · Borrador.** Todos los derechos reservados; ver `LICENSE`.

## Páginas
- `index.html`: Inicio
- `servicios.html`: Libro de servicios (12 servicios en 4 áreas)
- `la-firma.html`: La firma y el equipo
- `contacto.html`: Contacto (el formulario abre WhatsApp con la solicitud lista)

Todas comparten `estilos.css`.

## Cómo editar
Las páginas se generan con `build_site.py`, que arma el menú y el pie de página compartidos:

```bash
python3 build_site.py .
```

## Publicación
Publicado con GitHub Pages desde la rama `main` (carpeta raíz).

## Franja de propuesta
Mientras el diseño sea una propuesta, todas las páginas muestran la franja "Propuesta de diseño · JAC LAB · Borrador". Para quitarla, borre el bloque `draft-banner` en `build_site.py` y vuelva a generar las páginas.
