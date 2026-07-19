---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 6. Plan de Pagos"
source_id: 9000014
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 6. Plan de Pagos

```sql
SELECT TOP 10 * FROM dbo.FSD601  -- Plan de pago: Capital / Interés
SELECT TOP 10 * FROM dbo.FSD602  -- Pago Capital / Interés
SELECT TOP 10 * FROM dbo.FSD611  -- Seguros / Intereses
SELECT TOP 10 * FROM dbo.FSD612  -- Pago Seguros/Intereses (SUM desde PP1IMP16 hasta PP1IMP20)
SELECT TOP 10 * FROM dbo.FPP002  -- Comisión / Otros conceptos
SELECT TOP 10 * FROM dbo.FPP003  -- Pago Comisión/Otros conceptos (PRESTCONC: 3=Mora / 6=Pago)
```

### Cambio de estado de cuota a pagada

```sql
UPDATE fsd602 SET pp1stat = 'T'
FROM fsd602
WHERE pgcod = 1 AND ppsuc = 65 AND ppcta = 318663 AND ppoper = 1637928
    AND d602co = 'S'
    AND ppfpag BETWEEN '2024-09-11' AND '2024-11-11'
    AND pptipo = 'F'
    AND pp1nump IN (10, 11, 12)
    AND pp1fech = '2024-06-19';
```

---
