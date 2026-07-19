---
title: "Préstamos en Bantotal — Tablas utilizadas por préstamos — Fsd012: Cambios de tasa"
source_id: 9000083
source_url: "local:extra_docs/bantotal/Prestamos_De_Larrobla_2001.md"
ingested_by: ingest_docs.py
---

## Tablas utilizadas por préstamos — Fsd012: Cambios de tasa

Solo datos importantes:

```
*Pgcod      N(3)      Cod.
*Aomod      N(3)      Modulo
*Aosuc      N(3)      Sucursal
*Aomda      N(4)      Moneda
*Aopap      N(4)      Aopap
*Aocta      N(9)      Cuenta
*Aooper     N(9)      Operación
*Aosbop     N(3)      Sub-operac.
*Aotope     N(3)      Tipo operac.
*Evcorr     N(9)      Correlativo evento
 Evfval     D(8)      Fecha valor
 Evtasa     N(11.6)   Tasa
 Evcd01     N(2)      Evcd01
 D012co     C(1)      ¿Contabilizado?
 D012cd     N(3)      pgcod
 D012mo     N(3)      hcmod
 D012su     N(3)      hsucor
 D012tr     N(3)      htran
 D012re     N(4)      hnrel
 D012fc     D(8)      hfcon
 D012or     N(2)      hcord
 D012sb     N(3)      hcsubo
 Evtipo     N(2)      Evtipo
 Evttas     N(1)      Tipo de tasa
```

Las tasas de una operación pueden ser cambiadas, en ese caso los cambios de
tasa se almacenan en esta tabla.

- `Evtipo = 3` => Cambio de tasa de la operación
- `Evtipo = 4` => Cambio de tasa de mora
