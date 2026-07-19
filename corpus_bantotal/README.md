# Corpus Bantotal (grounding para agentes IA)

Corpus de apoyo para que un agente IA **no invente** nombres de tabla, campos
o convenciones al trabajar sobre el Core Bancario **Bantotal** (construido
sobre GeneXus). A diferencia de `corpus/` (GeneXus), aquí NO hay un wiki
público equivalente: las fuentes son un manual propietario y, opcionalmente,
tus propios exports `.xpz` de KB.

## Contenido

| Recurso | Descripción | Confianza |
|---------|-------------|-----------|
| `tables.tsv` | Catálogo de tablas Bantotal: `code\tname\tfamily\tnote\tsource` (70 tablas). | **Derivada** — ver limitaciones. |
| `families.tsv` | Prefijos de tabla (FST, FSD, FSR, FSH, FSN...) y su categoría: `prefix\tcategory\tpurpose`. | Derivada. |
| `nine_fields.md` | El patrón arquitectónico de 9 campos base (PGCOD + 8 campos con prefijo de 2 letras) que identifican unívocamente una operación. | Derivada. |
| `xpz_objects.tsv` | Catálogo de objetos GeneXus REALES (Transaction/Procedure/SDT/...) escaneados de tus `.xpz`: `name\ttype\tmodule\tattributes_or_vars\tsource_xpz`. Vacío hasta que agregues `.xpz`. | **Alta** (viene de tu propia KB, no de prosa). |
| `bantotal_xpz/` | Carpeta donde vos agregás tus exports `.xpz` para que `scan_bantotal_xpz.py` los catalogue. | — |
| `index.tsv` + `articles/` | Artículos ingeridos desde `extra_docs/bantotal/*.{md,html}` vía `python3 ingest_docs.py bantotal` (manuales adicionales, notas funcionales, etc. que vos aportes). `id\ttitle\tpath\turl`, mismo esquema que `corpus/index.tsv`. Vacío hasta que ingieras algo. Documentos tipo "chuleta" con varias secciones `## ` se parten en un artículo por sección para que el ranking por título los encuentre. | Tan confiable como el documento que ingeriste — `source_url` queda como `local:...`, no como fuente oficial. |

Se generan con `python3 build_bantotal_corpus.py` (tables/families/nine_fields,
a partir de `bantotal_sources/`) y `python3 scan_bantotal_xpz.py`
(xpz_objects.tsv, a partir de `corpus_bantotal/bantotal_xpz/*.xpz`). Ambos son
idempotentes.

## Fuentes (`bantotal_sources/`)

- `MDU-99000-GL-V3R1.11.pdf` — manual oficial del modelo de datos Bantotal
  (**FUENTE PRIMARIA**; licencia internal-use). Úsalo para verificar la
  estructura EXACTA de campos de una tabla puntual antes de escribir código
  que dependa de ella.
- `Analisis_Modelo_Datos_Bantotal.md` — análisis técnico derivado del manual
  (118 páginas, 80 tablas). Fuente de `tables.tsv`.
- `Patron_9_Campos_Bantotal.md` — fuente de `nine_fields.md`.
- `MDU-10304-CO-V3R1.2-Certificado-Deposito-a-Termino.pdf` — manual oficial
  del módulo de Certificados de Depósito a Término (CDT) (**FUENTE
  PRIMARIA**; mismo aviso de licencia que el MDU-99000). Su texto extraído
  y limpiado (`pdftotext -layout` + remoción de encabezados/pies repetidos,
  sin parafrasear) se ingirió como artículos vía `ingest_docs.py` — ver
  `extra_docs/bantotal/MDU-10304-CO_Certificado_Deposito_a_Termino.md`.

## Cómo usarlo para NO alucinar

- **REGLA DURA**: un nombre de tabla Bantotal (`FST###`, `FSD###`, `FSR###`,
  `FSH###`, `FSN###`, ...) que uses debe figurar en `tables.tsv`; si no está,
  no lo inventes — dilo explícitamente o verifica contra el PDF/manual.
- **`tables.tsv` es un catálogo DERIVADO**, no una extracción literal del PDF
  página por página: te dice qué tablas EXISTEN y su propósito, pero NO la
  lista exacta de columnas. Para la estructura completa de una tabla,
  consulta `bantotal_sources/MDU-99000-GL-V3R1.11.pdf` directamente (o la
  skill `bantotal-table-extractor` si está disponible).
- **`xpz_objects.tsv` es la fuente de mayor confianza**: si un nombre de
  atributo/variable aparece ahí, existe de verdad en la KB del usuario
  (viene de parsear XML real, no de prosa). Priorízalo sobre `tables.tsv`
  cuando ambos apliquen.
- **El patrón de 9 campos (`nine_fields.md`) es una heurística observada**,
  no una regla universal documentada campo por campo en el manual — presenta
  el patrón como tal (probable, no garantizado) salvo que lo confirmes contra
  una tabla puntual.
- **⚠️ Conflicto conocido sobre "los 9 campos"**: `nine_fields.md` documenta
  una versión (`PGCOD, XXMOD, XXSUC, XXMDA, XXPAP, XXCTA, XXOPER, XXSBOP,
  XXTOPE`). Un artículo ingerido con `ingest_docs.py` (originado en la skill
  `bantotal-table-extractor`) documenta OTRA versión distinta (`CODOPER,
  FECDESDE, CODSUCU, CORRGRAL, FECACTU, HORACTU, USUACTU, FECDACTU, VERCFG`).
  Son dos análisis secundarios independientes que no coinciden — ninguno sale
  de una extracción literal del PDF. Si vas a responder sobre esto, decilo
  explícitamente en vez de elegir una versión al azar; verificá contra
  `bantotal_sources/MDU-99000-GL-V3R1.11.pdf` para la tabla puntual que te
  importe.
- **Cita la fuente.** Cada fila de `tables.tsv` trae su `source` (archivo y
  línea del análisis); cada fila de `xpz_objects.tsv` trae el `.xpz` de
  origen; cada fila de `index.tsv` trae un `local:...` que apunta al
  documento que vos ingeriste (no es fuente oficial: aclaralo si lo citás).

## Limitaciones conocidas

- Cobertura parcial: 70 de las ~80 tablas mencionadas en el manual quedaron
  capturadas por el patrón de extracción (tablas citadas solo como ejemplo
  suelto, sin fila propia en el análisis, no entran). Si buscás una tabla y
  no aparece en `tables.tsv`, no asumas que no existe: puede estar en el PDF
  y no en el análisis derivado.
- Sin `.xpz` agregados, `xpz_objects.tsv` está vacío — la parte de mayor
  confianza del corpus depende de que subas exports reales de tu KB.
- No hay `source_url` público (a diferencia de GeneXus): las fuentes son
  archivos locales en `bantotal_sources/`.
