#!/usr/bin/env python3
"""
Extrae capítulos del PDF 'Work by Referral' y los guarda como .txt limpios en src/.
Uso: python3 scripts/extract-chapters.py [ruta_al_pdf]

Reutilizable: para adaptar a otro libro, solo hay que cambiar CHAPTERS.
"""

import subprocess
import re
import os
import sys

PDF_PATH = sys.argv[1] if len(sys.argv) > 1 else "WorkByReferral.pdf"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "src")

# Definición de capítulos: (nombre_archivo, pagina_inicio, pagina_fin)
# Las páginas son del PDF (1-indexed). Verificadas manualmente.
CHAPTERS = [
    ("00-front-matter",            2,  10),  # Endorsements, copyright, dedicatoria, agradecimientos
    ("00-table-of-contents",      12,  13),  # Tabla de contenidos
    ("00-five-circles-of-life",   14,  14),  # Prefacio: Five Circles of Life
    ("01-discovering-a-better-way",       20,  28),  # Chapter 1
    ("02-the-both-and-approach",          30,  38),  # Chapter 2
    ("03-working-by-referral",            40,  48),  # Chapter 3
    ("04-youre-in-the-lead-generation-business", 50, 56),  # Chapter 4
    ("05-discovering-the-riches-beneath-your-feet", 58, 66),  # Chapter 5
    ("06-sorting-and-qualifying-your-database",  68, 76),  # Chapter 6
    ("07-engaging-your-database",         78,  88),  # Chapter 7
    ("08-the-three-cs-to-success",        90,  96),  # Chapter 8
    ("09-sales-is-a-contact-sport",       98, 108),  # Chapter 9
    ("10-care-moving-beyond-buying-and-selling", 110, 114), # Chapter 10
    ("11-community-creating-a-client-for-life",  116, 121), # Chapter 11
    ("12-taking-care-of-business",        122, 128), # Chapter 12
    ("13-winning-the-day",                134, 144), # Chapter 13
    ("14-staying-the-course",             146, 154), # Chapter 14
    ("15-the-next-step-is-yours",         155, 156), # Chapter 15
    ("16-author-bios",                    158, 162), # Bios + back
]


def extract_pages(pdf_path, first_page, last_page):
    """Extrae texto de un rango de páginas del PDF."""
    result = subprocess.run(
        ["pdftotext", "-f", str(first_page), "-l", str(last_page), pdf_path, "-"],
        capture_output=True, text=True
    )
    return result.stdout


def clean_text(text):
    """Limpia artefactos comunes del OCR."""
    # Quitar form feeds (separadores de página)
    text = text.replace('\x0c', '\n')

    # Fix chapter headers con espacios del OCR
    chapter_fixes = {
        r'C\s+hapter\s+O\s*ne': 'Chapter One',
        r'C\s+hapter\s+Two': 'Chapter Two',
        r'C\s+hapter\s+T\s*hree': 'Chapter Three',
        r'C\s+hapter\s+F\s*our': 'Chapter Four',
        r'C\s+hapter\s+F\s*ive': 'Chapter Five',
        r'C\s+hapter\s+Six': 'Chapter Six',
        r'C\s+hapter\s+Seven': 'Chapter Seven',
        r'C\s+hapter\s+E\s*ight': 'Chapter Eight',
        r'C\s+hapter\s+N\s*ine': 'Chapter Nine',
        r'C\s+hapter\s+T\s*en': 'Chapter Ten',
        r'C\s+hapter\s+E\s*leven': 'Chapter Eleven',
        r'C\s+hapter\s+Twelve': 'Chapter Twelve',
        r'C\s+hapter\s+T\s*hirteen': 'Chapter Thirteen',
        r'C\s+hapter\s+Fourteen': 'Chapter Fourteen',
        r'C\s+hapter\s+Fifteen': 'Chapter Fifteen',
        r'C\s+hapter\s+(\d+)': r'Chapter \1',
    }
    for pattern, replacement in chapter_fixes.items():
        text = re.sub(pattern, replacement, text)

    # Fix "o f" -> "of" (artefacto OCR muy común en este PDF)
    text = re.sub(r'\bo f\b', 'of', text)

    # Fix "B rian B uffini" and similar spaced name patterns
    text = re.sub(r'B\s+rian\s+B\s+uffini', 'Brian Buffini', text)
    text = re.sub(r'J\s+oe\s+N\s+iego', 'Joe Niego', text)

    # Quitar líneas que son solo números de página aislados
    text = re.sub(r'\n\s*\d{1,3}\s*\n', '\n\n', text)

    # Quitar basura de OCR (secuencias sin sentido de imágenes escaneadas)
    # Patterns like "T K S& yZ X P K SK" or "S iS X £ X & )C 2..."
    text = re.sub(r'T\s*K\s*S\s*&\s*y\s*Z\s*X\s*P\s*K\s*S\s*K', '', text)
    text = re.sub(r'[A-Z]\s+[a-z][A-Z]\s+[A-Z]\s+[A-Z]\s+[A-Z]\s+[A-Z]\s+[A-Z]', '', text)
    text = re.sub(r'S\s*[iI]\s*S\s*X\s*£.*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'SS\s*X\s*S.*$', '', text, flags=re.MULTILINE)

    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        stripped = line.strip()
        # Quitar líneas que son pura basura OCR (solo símbolos sueltos)
        if stripped and len(stripped) < 8 and re.match(r'^[\^\(\)\[\]\{\}<>|/\\~`*_#@!$%&=+.,;:\'"?\-\s]+$', stripped):
            continue
        # Quitar el header repetido
        if stripped == "Work by Referral. Live the Good Life!":
            continue
        cleaned_lines.append(line)
    text = '\n'.join(cleaned_lines)

    # Reducir múltiples líneas en blanco a máximo 2
    text = re.sub(r'\n{4,}', '\n\n\n', text)

    # Quitar espacios trailing
    text = '\n'.join(line.rstrip() for line in text.split('\n'))

    return text.strip() + '\n'


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    pdf_path = PDF_PATH
    if not os.path.isabs(pdf_path):
        pdf_path = os.path.join(BASE_DIR, pdf_path)

    if not os.path.exists(pdf_path):
        print(f"Error: No se encontró el PDF en '{pdf_path}'")
        sys.exit(1)

    print(f"Extrayendo capítulos de: {pdf_path}")
    print(f"Destino: {OUTPUT_DIR}/")
    print()

    for filename, first_page, last_page in CHAPTERS:
        raw_text = extract_pages(pdf_path, first_page, last_page)
        clean = clean_text(raw_text)

        output_path = os.path.join(OUTPUT_DIR, f"{filename}.txt")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(clean)

        line_count = len(clean.split('\n'))
        print(f"  ✓ {filename}.txt ({last_page - first_page + 1} págs, {line_count} líneas)")

    print(f"\n✅ Extracción completa. {len(CHAPTERS)} archivos en {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
