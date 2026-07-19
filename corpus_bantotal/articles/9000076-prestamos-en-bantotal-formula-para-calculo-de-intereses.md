---
title: "Préstamos en Bantotal — Fórmula para cálculo de intereses"
source_id: 9000076
source_url: "local:extra_docs/bantotal/Prestamos_De_Larrobla_2001.md"
ingested_by: ingest_docs.py
---

## Fórmula para cálculo de intereses

El interés se calcula en función de la tasa, el capital, el plazo y el tipo
de año.

```
Capital(C) = 10000
Plazo (P) = 360 días

Si tasa 15% lineal anual (T)
  Año comercial:
      Interés = C*T*P/36000 = 10000*15*360/36000 = 1500
  Año calendario:
      Interés = C*T*P/36000 = 10000*15*360/36500 = 1479.45

Si tasa 15% efectiva anual (T)
  Año comercial:
      Interés = C*(1+(T/100))^(360/360)-1 = 1500
  Año calendario:
      Interés = C*(1+(T/100))^(360/365)-1 = 1478
```
