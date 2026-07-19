---
title: "Patrón de 9 Campos Arquitectónicos de Bantotal — Ejemplo de Uso"
source_id: 9000004
source_url: "local:extra_docs/bantotal/9-campos-clave.md"
ingested_by: ingest_docs.py
---

## Ejemplo de Uso

```sql
-- Tabla típica con el patrón completo
CREATE TABLE FST001 (
    CODOPER   NUMERIC(7,0)  NOT NULL,  -- [1]
    FECDESDE  DATE          NOT NULL,  -- [2]
    CODSUCU   NUMERIC(3,0)  NOT NULL,  -- [3]
    CORRGRAL  NUMERIC(5,0)  NOT NULL,  -- [4]
    -- ... otros campos específicos de negocio ...
    FECACTU   DATE          NULL,      -- [5]
    HORACTU   NUMERIC(6,0)  NULL,      -- [6]
    USUACTU   VARCHAR(10)   NULL,      -- [7]
    FECDACTU  NUMERIC(8,0)  NULL,      -- [8]
    VERCFG    NUMERIC(3,0)  NULL,      -- [9]
    CONSTRAINT PK_FST001 PRIMARY KEY (CODOPER, FECDESDE, CODSUCU, CORRGRAL)
);
```
