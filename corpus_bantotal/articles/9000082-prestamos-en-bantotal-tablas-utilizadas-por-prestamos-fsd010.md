---
title: "Préstamos en Bantotal — Tablas utilizadas por préstamos — Fsd010: Operaciones"
source_id: 9000082
source_url: "local:extra_docs/bantotal/Prestamos_De_Larrobla_2001.md"
ingested_by: ingest_docs.py
---

## Tablas utilizadas por préstamos — Fsd010: Operaciones

Solo atributos que se usan en préstamos:

```
*Pgcod     N(3)      Cod.
*Aomod     N(3)      Modulo
*Aosuc     N(3)      Sucursal
*Aomda     N(4)      Moneda
*Aopap     N(4)      Aopap
*Aocta     N(9)      Cuenta
*Aooper    N(9)      Operación
*Aosbop    N(3)      Sub-operac.
*Aotope    N(3)      Tipo operac.
 Aofval    D(8)      F/valor
 Aofvto    D(8)      F/vto
 Aopzo     N(5)      Plazo
 Aottas    N(1)      Tipo de Tasa
 Aotasa    N(11.6)   Tasa
 Aotmor    N(11.6)   Tasa Mora
 Aotdia    N(1)      Tipo de días
 Aotano    N(1)      Tipo de ano
 Aodrev    N(5)      Días p/revisión de Tasa
 Aoimp     N(15.2)   Importe
 Aotvto    C(1)      Tipo de ajuste en vencto.
 Aoperiod  N(5)      Período (Itper)
```

En esta tabla se almacenan los siguientes datos: capital original (aoimp),
tasa y tipo de tasa (aottas, aotasa), tasa de mora (aotmor), tipo de año
(aotano), tipo de día (aotdia), periodo entre cuotas (aoperiod).
