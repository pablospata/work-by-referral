# Prompt para continuar traducción por capítulos

Usa este prompt en una nueva conversación para pedir la traducción de capítulos específicos del libro "Work by Referral".

---

## Prompt (copiar y pegar):

```
Estoy traduciendo el libro "Work by Referral" de inglés a español.

El proyecto está en: /home/pablo/Documentos/WorkByReferral/

La estructura es:
- src/ → texto extraído del PDF en inglés, un .txt por capítulo
- es/ → traducciones en Markdown, un .md por capítulo
- scripts/md-to-pdf.py → convierte .md a PDF con estilo de libro

Mirá el capítulo ya traducido es/01-descubriendo-un-camino-mejor.md para seguir exactamente el mismo estilo, tono y formato de traducción.

Ahora necesito que traduzcas los capítulos [X, Y, Z]. Para cada uno:
1. Leé el .txt correspondiente en src/
2. Traducilo al español siguiendo el mismo estilo del capítulo 1
3. Guardalo como .md en es/
4. Generá el PDF con: python3 scripts/md-to-pdf.py es/[archivo].md

Convenciones de formato:
- # Capítulo X: Título → header principal
- > "cita" + > — autor → citas de apertura
- > **texto** → recuadros/highlights del libro
- ## Paso de Acción → action steps al final
- Omitir números de página
```

---

### Ejemplo de uso:

> Traducí los capítulos 2, 3 y 4 (archivos src/02-*.txt, src/03-*.txt, src/04-*.txt)

> Traducí el capítulo 13 (src/13-winning-the-day.txt)
