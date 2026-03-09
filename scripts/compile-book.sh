#!/bin/bash
# Compila los capítulos del libro traducido en un solo libro-completo.md
# Uso: bash scripts/compile-book.sh

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$(dirname "$SCRIPT_DIR")"
ES_DIR="$BASE_DIR/es"
OUTPUT="$ES_DIR/libro-completo.md"

echo "Compilando libro completo..."

# Archivos del libro en orden correcto
BOOK_FILES=(
    "00-portada-y-preliminares.md"
    "00-tabla-de-contenidos.md"
    "00-los-cinco-circulos.md"
    "01-descubriendo-un-camino-mejor.md"
    "02-la-mentalidad-del-ambos-y.md"
    "03-trabajar-por-referidos.md"
    "04-estas-en-el-negocio-de-generar-leads.md"
    "05-descubriendo-las-riquezas-bajo-tus-pies.md"
    "06-clasificando-y-calificando-tu-base-de-datos.md"
    "07-activando-tu-base-de-datos.md"
    "08-las-tres-c-del-exito.md"
    "09-las-ventas-son-un-deporte-de-contacto.md"
    "10-cuidado-mas-alla-de-comprar-y-vender.md"
    "11-comunidad-creando-un-cliente-de-por-vida.md"
    "12-ocupandose-del-negocio.md"
    "13-ganando-el-dia.md"
    "14-manteniendo-el-rumbo.md"
    "15-el-proximo-paso-es-tuyo.md"
    "16-sobre-los-autores.md"
)

# Limpiar archivo de salida
> "$OUTPUT"

first=true
for basename in "${BOOK_FILES[@]}"; do
    f="$ES_DIR/$basename"
    if [ ! -f "$f" ]; then
        echo "  ⚠ No encontrado: $basename (saltando)"
        continue
    fi

    if [ "$first" = true ]; then
        first=false
    else
        echo "" >> "$OUTPUT"
    fi

    cat "$f" >> "$OUTPUT"
    echo "  ✓ $basename"
done

lines=$(wc -l < "$OUTPUT")
echo ""
echo "✅ Compilado: $OUTPUT ($lines líneas)"
