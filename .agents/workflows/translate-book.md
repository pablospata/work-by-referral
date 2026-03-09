---
description: Cómo traducir un libro PDF de inglés a español usando el pipeline md
---

# Workflow: Traducir un Libro PDF

// turbo-all

## 1. Preparar el proyecto

```bash
mkdir -p {src,es,scripts}
```

## 2. Extraer capítulos del PDF

Editar `scripts/extract-chapters.py`:
- Actualizar `CHAPTERS` con los rangos de página correctos del nuevo PDF
- Verificar páginas clave con: `pdftotext -f N -l N archivo.pdf - | head -10`
- Ejecutar:

```bash
python3 scripts/extract-chapters.py nuevo-libro.pdf
```

## 3. Revisar texto extraído

Revisar los `.txt` en `src/` para verificar calidad del OCR y que los capítulos estén correctamente divididos.

## 4. Traducir capítulo por capítulo

Para cada archivo en `src/XX-nombre.txt`:
1. Leer el texto en inglés
2. Crear `es/XX-nombre.md` con la traducción
3. Seguir las convenciones de formato:
   - `# Capítulo X: Título` como header principal
   - `> "cita"` + `> — autor` para citas de apertura
   - `> **texto**` para recuadros/highlights del libro
   - `## Paso de Acción` para action steps al final
   - Omitir números de página

## 5. Compilar libro completo

```bash
bash scripts/compile-book.sh
```

Esto genera `es/libro-completo.md` con todos los capítulos unidos.

## 6. Verificar

- Revisar `es/libro-completo.md` para confirmar que todo está en orden
- Verificar que no falten capítulos
