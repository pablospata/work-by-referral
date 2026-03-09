# Prompt general para traducir cualquier libro PDF

Usa este prompt en un proyecto nuevo para reutilizar el pipeline de traducción ya creado en WorkByReferral.

---

## Prompt (copiar y pegar):

```
Quiero traducir un libro PDF de inglés a español.

Ya tengo un pipeline probado en /home/pablo/Documentos/WorkByReferral/ que quiero reutilizar. Mirá ese proyecto como referencia:

- scripts/extract-chapters.py → extrae capítulos del PDF y limpia OCR
- scripts/md-to-pdf.py → convierte Markdown a PDF con estilo de libro
- scripts/compile-book.sh → une todos los .md en un libro-completo.md
- es/01-descubriendo-un-camino-mejor.md → ejemplo del estilo de traducción
- .agents/workflows/translate-book.md → workflow paso a paso

Para este nuevo proyecto:
1. Copiá los scripts de WorkByReferral a este proyecto
2. Adaptá extract-chapters.py con los rangos de página del nuevo PDF
3. Extraé los capítulos y empezá a traducir siguiendo el mismo estilo

El PDF a traducir es: [NOMBRE_DEL_PDF]

El libro se llama: [TÍTULO] de [AUTOR]

Empezá por la extracción y traducción del primer capítulo para que apruebe el estilo.
```

---

### Notas:
- El script `extract-chapters.py` necesita que adaptes la lista `CHAPTERS` con los rangos de página del nuevo PDF
- El script `md-to-pdf.py` funciona tal cual para cualquier Markdown
- Si el nuevo PDF no es OCR, la extracción será más limpia y necesitará menos limpieza
