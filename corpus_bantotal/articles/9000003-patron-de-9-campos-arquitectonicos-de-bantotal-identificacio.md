---
title: "Patrón de 9 Campos Arquitectónicos de Bantotal — Identificación en Tablas"
source_id: 9000003
source_url: "local:extra_docs/bantotal/9-campos-clave.md"
ingested_by: ingest_docs.py
---

## Identificación en Tablas

Para identificar si una tabla sigue este patrón:

1. Buscar la presencia de CODOPER (casi siempre presente en tablas transaccionales)
2. Verificar FECDESDE (indica versionado temporal)
3. Contar cuántos de los 9 campos están presentes
4. Tablas con 7+ de estos campos son consideradas "tablas arquitectónicas core"
