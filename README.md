# 📚 Trabajar por Referidos — Traducción y Adaptación

Traducción al español del libro **"Work by Referral: Live the Good Life!"** de Brian Buffini y Joe Niego, junto con materiales complementarios originales.

---

## 📖 Sobre el libro

*Work by Referral* es un clásico del mundo inmobiliario que presenta un sistema probado para construir un negocio basado en referidos en lugar del desgastante enfoque transaccional (llamadas en frío, publicidad masiva, perseguir extraños). Los principios son universales y aplicables a cualquier profesional que trabaje con clientes: asesores financieros, contadores, abogados, seguros, y más.

Los autores — Brian Buffini, un inmigrante irlandés que construyó una fortuna en bienes raíces en San Diego, y Joe Niego, un ex drafteado de la NBA que se convirtió en uno de los agentes más exitosos de Chicago — comparten sus historias personales y un sistema paso a paso basado en relaciones, confianza y servicio genuino.

📥 **Libro original en inglés (PDF gratuito compartido por los autores):** [Descargar Work by Referral](https://downloads.buffiniandcompany.com/documents/resources/WorkByReferral_2015_Color.pdf)

---

## 📁 Estructura del repositorio

```
WorkByReferral/
├── es/                              # Todos los documentos en español
│   ├── 00-portada-y-preliminares.md # Elogios, dedicatoria, agradecimientos
│   ├── 00-tabla-de-contenidos.md    # Índice del libro
│   ├── 00-los-cinco-circulos.md     # Prefacio: Los Cinco Círculos de la Vida
│   ├── 01 a 16 — Capítulos          # Los 16 capítulos traducidos (MD + PDF)
│   ├── Trabajar-por-Referidos-*.md/.pdf  # Libro compilado con carátula
│   ├── 00-resumen.md                # Resumen integral del libro
│   ├── 00-plan-de-accion.md         # Plan paso a paso (inmobiliarios)
│   ├── 00-checklist.md              # Checklist de progreso (inmobiliarios)
│   ├── 00-resumen-bursatil.md       # Resumen adaptado para asesores financieros
│   ├── 00-plan-bursatil.md          # Plan paso a paso para asesores financieros
│   ├── 00-checklist-bursatil.md     # Checklist para asesores financieros
│   └── 00-plantillas-bursatil.md    # Mensajes y scripts listos para usar
├── scripts/
│   ├── extract-chapters.py          # Extrae capítulos del PDF y limpia OCR
│   ├── md-to-pdf.py                 # Convierte Markdown a PDF con estilo de libro
│   └── compile-book.sh              # Compila todos los .md en libro-completo
├── src/                             # Textos fuente extraídos del PDF original
└── WorkByReferral.pdf               # PDF original del libro en inglés
```

---

## 📋 Contenido

### Libro traducido

| Sección | Contenido |
|---------|----------|
| Preliminares | Elogios, dedicatoria, agradecimientos |
| Índice | Tabla de contenidos |
| Prefacio | Los Cinco Círculos de la Vida |
| **Capítulo 1** | Descubriendo un Camino Mejor |
| **Capítulo 2** | La Mentalidad del "Ambos/Y" |
| **Capítulo 3** | Trabajar por Referidos |
| **Capítulo 4** | Estás en el Negocio de Generar Leads |
| **Capítulo 5** | Descubriendo las Riquezas Bajo tus Pies |
| **Capítulo 6** | Clasificando y Calificando tu Base de Datos |
| **Capítulo 7** | Activando tu Base de Datos |
| **Capítulo 8** | Las Tres C del Éxito |
| **Capítulo 9** | Las Ventas son un Deporte de Contacto |
| **Capítulo 10** | Cuidado: Más Allá de Comprar y Vender |
| **Capítulo 11** | Comunidad: Creando un Cliente de por Vida |
| **Capítulo 12** | Ocupándose del Negocio |
| **Capítulo 13** | Ganando el Día |
| **Capítulo 14** | Manteniendo el Rumbo |
| **Capítulo 15** | El Próximo Paso es Tuyo |
| **Capítulo 16** | Sobre los Autores |
| **📖 Libro completo** | Todo compilado con carátula — [⬇️ Descargar PDF](https://github.com/pablospata/work-by-referral/raw/main/es/Trabajar-por-Referidos-Buffini-Niego-ES.pdf) |

### Materiales complementarios

| Documento | Descripción |
|-----------|-------------|
| **Resumen** | Síntesis del libro completo en un solo documento fluido |
| **Plan de Acción** | Guía paso a paso en 6 fases y 17 pasos para implementar el sistema |
| **Checklist** | Lista de verificación para trackear progreso |
| **Resumen Bursátil** | Los mismos principios adaptados para asesores financieros |
| **Plan Bursátil** | Plan de acción específico para captación de inversores |
| **Checklist Bursátil** | Checklist con tracking de AUM y referidos |
| **Plantillas Bursátil** | Mensajes, scripts y 12 Elementos de Valor listos para usar |

Todos los documentos están disponibles en formato Markdown (.md) y PDF.

---

## 💼 Adaptación para Asesores Financieros

Los documentos con sufijo `bursatil` son una adaptación que hice de los principios del libro para mi trabajo como **asesor financiero independiente** (agente productor en el mercado de capitales argentino).

La adaptación traduce conceptos inmobiliarios al mundo bursátil:

- "Comprar/vender una casa" → "Poner la plata a trabajar"
- Notas escritas a mano → Mensajes personales genuinos
- Pop-Bys → Cafés uno a uno
- Fiestas de clientes → Desayunos de mercado
- Transacciones cerradas → AUM captado
- Red de proveedores → Red de aliados profesionales (contadores, abogados, escribanos)

Si sos asesor financiero, agente de bolsa, o trabajás en la industria de servicios financieros, estos materiales te van a servir tal cual o con mínimas modificaciones.

---

## 🔧 Pipeline de Traducción

Este proyecto incluye un pipeline completo y reutilizable para traducir libros PDF de inglés a español. Las herramientas están en `scripts/` y los prompts de IA en la raíz del repo.

### Paso 1: Extraer capítulos del PDF

`scripts/extract-chapters.py` extrae el texto de cada capítulo del PDF original usando `pdftotext` y limpia artefactos comunes de OCR (espacios rotos, headers repetidos, basura de escaneo).

```bash
python3 scripts/extract-chapters.py WorkByReferral.pdf
```

Para adaptar a otro libro, solo hay que editar la lista `CHAPTERS` al inicio del script con los rangos de página correspondientes. Podés verificar páginas con:

```bash
pdftotext -f 20 -l 28 nuevo-libro.pdf - | head -20
```

**Genera:** un `.txt` limpio por capítulo en `src/`.

### Paso 2: Traducir capítulo por capítulo

Cada `.txt` en `src/` se traduce manualmente (o con asistencia de IA) a un `.md` en `es/`, siguiendo estas convenciones de formato:

- `# Capítulo X: Título` → header principal
- `> "cita"` + `> — autor` → citas de apertura
- `> **texto**` → recuadros/highlights del libro
- `## Paso de Acción` → action steps al final
- Omitir números de página

### Paso 3: Generar PDFs

`scripts/md-to-pdf.py` convierte cada Markdown a PDF con estilo de libro (tipografía Merriweather + Open Sans, tamaño A5, márgenes de libro).

```bash
python3 scripts/md-to-pdf.py es/01-descubriendo-un-camino-mejor.md
```

**Requiere:** `pandoc` y `weasyprint` (`pip install weasyprint`).

### Paso 4: Compilar el libro completo

`scripts/compile-book.sh` une todos los `.md` de `es/` en un solo `libro-completo.md`:

```bash
bash scripts/compile-book.sh
```

### Reutilizar el pipeline para otro libro

El repo incluye dos prompts listos para reutilizar este pipeline:

| Archivo | Uso |
|---------|-----|
| `PROMPT-CAPITULOS.md` | Prompt para pedirle a una IA que traduzca capítulos específicos siguiendo el estilo ya establecido |
| `PROMPT-NUEVO-PROYECTO.md` | Prompt para arrancar la traducción de un libro completamente nuevo copiando este pipeline |

También hay un workflow automatizado en `.agents/workflows/translate-book.md` con el paso a paso completo.

---

## 🤝 Contacto

**Pablo Spata** — Asesor Financiero Independiente | AP CNV 2165

Si te interesa invertir tu dinero de forma inteligente en el mercado de capitales argentino, o si sos colega y querés intercambiar ideas, escribime:

- 📱 **WhatsApp:** [+54 9 2345 40-0586](https://wa.me/5492345400586)
- 📧 **Email:** [pablospata@gmail.com](mailto:pablospata@gmail.com)

---

## ⚖️ Disclaimer

Este repositorio contiene una traducción no oficial del libro *Work by Referral* de Brian Buffini y Joe Niego, realizada con fines educativos y de uso personal. Todos los derechos del contenido original pertenecen a sus autores y a Buffini & Company. Si sos el titular de los derechos y querés que modifique o elimine algo, contactame.

Los materiales complementarios (resúmenes, planes de acción, plantillas) son elaboración propia basada en los conceptos del libro.
