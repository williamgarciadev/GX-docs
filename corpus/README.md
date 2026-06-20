# Corpus GeneXus (grounding para agentes IA)

Corpus derivado de la documentación oficial **wiki.genexus.com** (GeneXus 18),
preparado para usarse como **fuente de verdad** y reducir alucinaciones de un
agente IA.

## Contenido

| Recurso | Descripción |
|---------|-------------|
| `articles/<id>-<slug>.md` | 5.433 artículos, uno por archivo. Cada uno con frontmatter de procedencia. |
| `genexus_corpus.jsonl` | Mismo contenido, un registro JSON por línea. Para pipelines de embeddings / RAG. |
| `INDEX.md` | Índice navegable con enlace a cada artículo y a su fuente en el wiki. |

Se generan con `python3 build_corpus.py` (en la raíz del repo) a partir de
`genexus_documentation.md`. El proceso es **idempotente**: re-ejecutarlo
reconstruye `corpus/` por completo.

## Frontmatter / esquema

Cada `.md` incluye:

```yaml
---
title: "<título del artículo>"
source_id: <id numérico del wiki>
source_url: https://wiki.genexus.com/commwiki/wiki?<id>
genexus_version: "18"
---
```

Cada registro del JSONL: `{id, title, source_url, genexus_version, path, content}`.

## Cómo usarlo para NO alucinar

- **Cita siempre `source_url`.** Toda afirmación sobre GeneXus debe respaldarse
  con el artículo del que proviene; si no hay artículo, decláralo como
  desconocido en lugar de inventarlo.
- **Recupera por artículo, no por trozos arbitrarios.** Cada archivo es una
  unidad completa: usa `INDEX.md` o búsqueda sobre `articles/` (o el JSONL en un
  índice vectorial) y entrega el artículo entero como contexto.
- **Alcance: GeneXus 18.** El corpus no cubre otras versiones; no extrapoles.

## Limitaciones conocidas

- **Sin imágenes.** Las figuras del wiki no se incluyeron; aparecen como
  `` `[imagen omitida: wiki id N]` `` para no dejar rutas rotas.
- **Enlaces internos** reescritos a URLs absolutas del wiki
  (`...wiki?<id>`); requieren conexión para abrirse.
- Es un volcado: puede contener restos menores de maquetación del wiki original
  (p. ej. tablas de *Backlinks*), ya con enlaces absolutos.
