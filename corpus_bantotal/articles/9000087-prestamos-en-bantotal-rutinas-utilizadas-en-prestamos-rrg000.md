---
title: "Préstamos en Bantotal — Rutinas utilizadas en préstamos — RRg0004"
source_id: 9000087
source_url: "local:extra_docs/bantotal/Prestamos_De_Larrobla_2001.md"
ingested_by: ingest_docs.py
---

## Rutinas utilizadas en préstamos — RRg0004

```
RRg0004(&Ttas, &Tasa, &Tano, &Plazo, &Tint, &Coef)
```

Esta rutina se utiliza para calcular intereses.

Parámetros que recibe:

- **&ttas**: Tipo de tasa.
- **&tasa**: Tasa.
- **&tano**: Tipo de año (1 = comercial, 2 = calendario).
- **&plazo**: cantidad de días.
- **&tint**: Enviar "C".

Parámetros que devuelve: `&coef`.
