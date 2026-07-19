---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 8. Ajuste de Tasas (Decreto 455)"
source_id: 9000016
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 8. Ajuste de Tasas (Decreto 455)

### EVTIPO — Tipos de evento en FSD012

| Código | Descripción |
|--------|-------------|
| `3` | Cambio de Tasa Normal (corriente) |
| `4` | Cambio de Tasa de Mora |
| `6` | Cambio de Tasa de Corte Normal |
| `11` | Reprogramación o diferimiento |
| `31` | Cambio en condiciones de negociación |
| `50` | Abono a capital |
| `88` | Nueva tasa de costo |

### Procedimiento MORA

```
1. Recibir información de Juan Carlos
2. Preparar datos para el query:
   SELECT * FROM fsd012 WHERE aooper IN (...) → EVCORR (el más alto) → bajar a Excel
   SELECT * FROM fsd010 WHERE aooper IN (...)  → bajar a Excel
3. Abrir nueva hoja: copiar títulos de FSD012 desde PGCOD hasta AOOPER de FSD010
4. Completar campos:
   - EVCORR:  el definido arriba
   - EVTIPO:  4 (mora)
   - EVFVAL:  fecha dada por Juan Carlos
   - EVFVTO:  campo Default de GeneXus
   - EVIMP:   0
   - EVTTAS:  1
   - EVTASA:  proporcionada por Juan Carlos
   - EVCAP→EVCD01: 0
   - EVCD02:  vacío
   - EVINV:   999999999 - EVCORR
   - EVPER→EVARB1: 0
   - EVMD / EVMD1: vacío
   - EVPRE→EV012RE: 0
   - D012FC:  fecha dada por Juan Carlos (fecha aplicación en Prod)
   - D012OR / D012SB: 0
   - D012CO:  'S'
5. Cuadrar cantidad de registros
6. Cuadrar que registros de una tasa sean la misma cantidad
```

### Procedimiento CORRIENTE

```
(Igual que MORA, excepto:)
   - EVTIPO:  3 (intereses corrientes)
   - D012FC:  fecha Default de GeneXus
   - Se sube como FSD012
```

### Ajuste tasas lineales x efectiva

```sql
SELECT * FROM fsd010  WHERE aofval >= '2025-02-03' AND aomod = 113 AND aottas = 2;
SELECT * FROM x054023 WHERE xllfvalor >= '2025-02-03' AND xllaomod = 113 AND xlltipotas = 2;
SELECT * FROM x054007 WHERE xllOAOfval >= '2025-02-03' AND xllOaomod = 113 AND xllOAOTTAS = 2;
```

### Abono a capital

```sql
SELECT * FROM fsd012
WHERE aomod = 113 AND evtipo = 50
    AND D012fc >= '2025-10-01 00:00:00.000'
    AND AOMOD <> 70 AND D012TR = 78;
```

---
