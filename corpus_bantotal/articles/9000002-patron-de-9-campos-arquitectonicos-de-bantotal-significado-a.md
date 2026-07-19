---
title: "Patrón de 9 Campos Arquitectónicos de Bantotal — Significado Arquitectónico"
source_id: 9000002
source_url: "local:extra_docs/bantotal/9-campos-clave.md"
ingested_by: ingest_docs.py
---

## Significado Arquitectónico

Este patrón de 9 campos permite:

- **Identificación única**: CODOPER + FECDESDE + CODSUCU + CORRGRAL
- **Versionado temporal**: Múltiples versiones del mismo registro según FECDESDE
- **Auditoría completa**: Quién (USUACTU), cuándo (FECACTU/HORACTU) modificó
- **Trazabilidad**: Seguimiento completo del ciclo de vida de operaciones
- **Particionamiento**: CODSUCU permite distribuir datos por sucursal
