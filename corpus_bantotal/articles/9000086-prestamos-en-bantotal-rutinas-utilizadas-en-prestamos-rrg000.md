---
title: "Préstamos en Bantotal — Rutinas utilizadas en préstamos — RRg0003"
source_id: 9000086
source_url: "local:extra_docs/bantotal/Prestamos_De_Larrobla_2001.md"
ingested_by: ingest_docs.py
---

## Rutinas utilizadas en préstamos — RRg0003

```
RRg0003(&Ppgcod, &Psucurs, &Fval, &Fvto, &Plazo, &Tplzo, &Tvto)
```

Esta rutina se utiliza para obtener la fecha de vto dada la fecha valor y
el plazo, o el plazo dada la fecha valor y la fecha de vencimiento.

Parámetros que recibe:

- **&Ppgcod**: empresa en la que se trabaja.
- **&Psucurs**: Sucursal en la que está el préstamo.
- **&fval**: fecha inicial.
- **&fvto**: fecha final (si se envía en blanco, la devuelve, sino
  devuelve el plazo).
- **&plazo**: cantidad de días.
- **&tplzo**: tipo de año (1 = comercial, 2 = calendario).
- **&Tvto**:
  - `'P'` si la fecha final calculada es un día feriado, ajusta al
    siguiente hábil.
  - `'A'` si la fecha final calculada es un día feriado, ajusta al hábil
    anterior.
  - `'N'` si la fecha final calculada es un día feriado, no realiza
    ajuste.

Parámetros que devuelve: `&fvto`, `&plazo`.
