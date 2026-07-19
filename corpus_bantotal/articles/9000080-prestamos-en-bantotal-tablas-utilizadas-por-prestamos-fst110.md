---
title: "Préstamos en Bantotal — Tablas utilizadas por préstamos — FST110 y Fst111: Sistemas y relación sistema/módulo"
source_id: 9000080
source_url: "local:extra_docs/bantotal/Prestamos_De_Larrobla_2001.md"
ingested_by: ingest_docs.py
---

## Tablas utilizadas por préstamos — FST110 y Fst111: Sistemas y relación sistema/módulo

**FST110 : SISTEMAS**

```
*Dscod      N(3)    Código de sistema
 Dsnom      C(30)   Nombre de sistema
```

En esta tabla se define el sistema de préstamos, el código del sistema de
préstamos es el 50.

**Fst111 : Relación sistema / módulo**

```
*Dscod      N(3)    Código de sistema
*Modulo     N(3)    Modulo
```

En esta tabla se definen los módulos que integran el sistema.
