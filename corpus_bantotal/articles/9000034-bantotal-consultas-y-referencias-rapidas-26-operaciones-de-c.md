---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 26. Operaciones de Caja"
source_id: 9000034
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 26. Operaciones de Caja

### Caja saldo cero

```sql
SELECT Scsdo, * FROM FSD011
WHERE SCRUB=1105050001 AND SCSBOP=0 AND Scsdo <> 0;

SELECT Itafgt, * FROM fsd016
WHERE Itsuc=56 AND itmod=50 AND ittran=110 AND Itnrel=40
ORDER BY Itnrel, itord;

SELECT itcont, * FROM fsd015
WHERE Itsuc=56 AND itmod=50 AND ittran=110 AND Itnrel=40;
```

### Descruce de caja / Operaciones no contabilizadas

```sql
SELECT * FROM fsd015 a WITH (NOLOCK)
WHERE a.pgcod=1 AND a.itcont='E'
AND EXISTS (
    SELECT * FROM fsd016 b WITH (NOLOCK)
    WHERE b.pgcod=a.pgcod AND b.itsuc=a.itsuc
        AND b.itmod=a.itmod AND b.ittran=a.ittran
        AND b.itnrel=a.itnrel AND b.itafgt='E'
);

SELECT * FROM fsd015 WHERE ItconT <> 'S' AND Itsuc=93;  -- No contabilizadas
```

### Cierre de cajas

```sql
SELECT COUNT(mbccest) FROM MBC004 WHERE MBCCFch='2024-03-30' AND MBCCEst='A' AND MBCCCaj<>0  -- Abiertas
SELECT COUNT(mbccest) FROM MBC004 WHERE MBCCFch='2024-03-30' AND MBCCEst='C' AND MBCCCaj<>0  -- Cerradas
SELECT * FROM MBC004 WHERE MBCCFch='2024-03-30' AND MBCCEst='A' AND MBCCCaj<>0 ORDER BY MBCCSuc
```

---
