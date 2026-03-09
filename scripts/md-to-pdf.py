#!/usr/bin/env python3
"""
Convierte archivos Markdown a PDF con estilo de libro.
Uso: python3 scripts/md-to-pdf.py es/01-capitulo.md [output.pdf]

Usa pandoc (md->html) + weasyprint (html->pdf).
"""

import subprocess
import sys
import os

def md_to_html(md_path):
    """Convierte Markdown a HTML usando pandoc."""
    result = subprocess.run(
        ["pandoc", "--from=markdown", "--to=html5", md_path],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"Error en pandoc: {result.stderr}")
        sys.exit(1)
    return result.stdout


CSS_STYLE = """
@import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;1,300;1,400&family=Open+Sans:wght@400;600;700&display=swap');

@page {
    size: A5;
    margin: 2cm 1.8cm;
    @bottom-center {
        content: counter(page);
        font-family: 'Open Sans', sans-serif;
        font-size: 9pt;
        color: #999;
    }
}

body {
    font-family: 'Merriweather', 'Georgia', serif;
    font-size: 10.5pt;
    line-height: 1.7;
    color: #2c2c2c;
    text-align: justify;
    hyphens: auto;
    -webkit-hyphens: auto;
}

h1 {
    font-family: 'Open Sans', sans-serif;
    font-size: 20pt;
    font-weight: 700;
    color: #1a1a2e;
    margin-top: 0;
    margin-bottom: 0.3em;
    text-align: left;
    border-bottom: 2px solid #16213e;
    padding-bottom: 0.3em;
    page-break-before: always;
}

/* El primer h1 del documento no necesita salto de página */
body > h1:first-child,
.cover + h1,
.cover ~ h1:first-of-type {
    page-break-before: avoid;
}

/* Carátula - sobreescribir TODOS los estilos heredados del body */
.cover {
    page-break-after: always;
    text-align: center !important;
    hyphens: none !important;
    -webkit-hyphens: none !important;
    word-break: normal !important;
    padding-top: 4cm;
    margin: 0;
}

.cover p {
    text-align: center !important;
    text-indent: 0 !important;
    hyphens: none !important;
    -webkit-hyphens: none !important;
    word-break: normal !important;
    margin-left: auto;
    margin-right: auto;
}

.cover .title {
    font-family: 'Open Sans', sans-serif;
    font-size: 28pt;
    font-weight: 700;
    color: #1a1a2e;
    margin-bottom: 0.2em;
    line-height: 1.2;
}

.cover .subtitle {
    font-family: 'Open Sans', sans-serif;
    font-size: 14pt;
    color: #555;
    font-style: italic;
    margin-bottom: 2.5em;
}

.cover .authors {
    font-family: 'Open Sans', sans-serif;
    font-size: 14pt;
    font-weight: 600;
    color: #1a1a2e;
    margin-bottom: 2.5em;
}

.cover .description {
    font-family: 'Open Sans', sans-serif;
    font-size: 10pt;
    color: #666;
    font-style: italic;
}

/* Ocultar número de página en la carátula */
@page :first {
    @bottom-center {
        content: none;
    }
}

h1 + p > em:first-child {
    display: block;
    font-family: 'Open Sans', sans-serif;
    font-size: 10pt;
    color: #555;
    margin-bottom: 1em;
}

h2 {
    font-family: 'Open Sans', sans-serif;
    font-size: 14pt;
    font-weight: 600;
    color: #16213e;
    margin-top: 2em;
    margin-bottom: 0.5em;
    text-align: left;
}

p {
    margin-bottom: 0.8em;
    text-indent: 1.5em;
}

/* Sin sangría en primer párrafo después de título o cita */
h1 + p, h2 + p, blockquote + p, hr + p {
    text-indent: 0;
}

blockquote {
    margin: 1.5em 0;
    padding: 0.8em 1.2em;
    border-left: 3px solid #16213e;
    background: #f8f8fc;
    font-style: italic;
    color: #333;
}

blockquote p {
    margin-bottom: 0.3em;
}

blockquote strong {
    font-style: normal;
    color: #1a1a2e;
}

hr {
    border: none;
    border-top: 1px solid #ddd;
    margin: 1.5em 0;
}

/* Los hr no deben forzar saltos de página */
hr + h1 {
    page-break-before: always;
}

em {
    color: #444;
}
"""


COVER_HTML = """
<div class="cover">
    <p class="title">Trabajar por Referidos</p>
    <p class="subtitle">¡Vive la Buena Vida!</p>
    <p class="authors">Brian Buffini &amp; Joe Niego</p>
    <p class="description">Estrategias Probadas para el Éxito y la Felicidad<br>en el Negocio Inmobiliario</p>
</div>
"""


def html_to_pdf(html_content, output_path, cover=False):
    """Convierte HTML con estilos a PDF usando WeasyPrint."""
    from weasyprint import HTML, CSS

    body_content = COVER_HTML + html_content if cover else html_content

    full_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Traducción</title>
</head>
<body>
{body_content}
</body>
</html>"""

    html_doc = HTML(string=full_html)
    css = CSS(string=CSS_STYLE)
    html_doc.write_pdf(output_path, stylesheets=[css])


def main():
    if len(sys.argv) < 2:
        print("Uso: python3 scripts/md-to-pdf.py <archivo.md> [output.pdf]")
        sys.exit(1)

    md_path = sys.argv[1]
    if not os.path.isabs(md_path):
        md_path = os.path.join(os.getcwd(), md_path)

    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        output_path = md_path.rsplit('.', 1)[0] + '.pdf'

    if not os.path.exists(md_path):
        print(f"Error: No se encontró '{md_path}'")
        sys.exit(1)

    print(f"Convirtiendo: {os.path.basename(md_path)}")
    print(f"  → Markdown a HTML (pandoc)...")
    html_content = md_to_html(md_path)

    # Detectar si es el libro completo para agregar carátula
    is_book = 'libro-completo' in os.path.basename(md_path)

    print(f"  → HTML a PDF (weasyprint)...")
    html_to_pdf(html_content, output_path, cover=is_book)

    size_kb = os.path.getsize(output_path) / 1024
    print(f"  ✅ PDF generado: {output_path} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
