---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 9. Contabilidad"
source_id: 9000017
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 9. Contabilidad

```sql
SELECT TOP 10 * FROM dbo.FSH012  -- Contabilidad histórica por día
SELECT TOP 10 * FROM dbo.FSH014  -- Contabilidad histórica por año (capturado mensual)
SELECT TOP 10 * FROM dbo.FSD016  -- Contabilidad diaria
SELECT TOP 10 * FROM dbo.FSH016  -- Contabilidad histórica
SELECT TOP 10 * FROM dbo.FSH015  -- Asientos (cabezal)
```

### Join cabezal + detalle contable

```sql
SELECT TOP 100 *
FROM dbo.FSD015 FD15
    INNER JOIN dbo.FSD016 FD16
        ON FD16.Pgcod = FD15.Pgcod AND FD15.Itmod = FD16.Itmod
        AND FD15.Itsuc = FD16.Itsuc AND FD15.Ittran = FD16.Ittran
        AND FD15.Itnrel = FD16.Itnrel
WHERE FD16.Itoper = 1310837;
```

### Asientos anulados

```sql
-- Htpoas='A' | Hccorr='A' | 1=Debe | 2=Haber

-- Diarios (FSH015 / FSH016)
SELECT Htpoas,Hccorr,hsucor,hcmod,htran,hnrel,hfcon,Hccaja
FROM fsh015
WHERE hsucor=58 AND hcmod=22 AND htran=60 AND hfcon='2024-03-21' AND Hccorr=99
UNION
SELECT Htpoas,Hccorr,hsucor,hcmod,htran,hnrel,hfcon,Hccaja
FROM fsh015
WHERE hsucor=58 AND hcmod=22 AND htran=60 AND hfcon='2024-03-21' AND Htpoas='A';

-- Históricos (FSD015 / FSD016)
SELECT ittpoas,itcorr,itsuc,itmod,ittran,Itnrel,itfcon,Itcaja
FROM fsd015
WHERE itsuc=73 AND itmod=50 AND ittran=750 AND itfcon='2025-07-18' AND ittpoas='A' OR itcorr=99;
```

### Errores contables

```sql
-- Registro queda en E: fsd016.itafgt <> 'C' y fsd015.itcont = 'E'
SELECT TOP 10 * FROM dbo.FSH104   -- Errores contables
SELECT TOP 10 * FROM dbo.FSD515   -- Relación asientos anulados
SELECT TOP 10 * FROM dbo.FSX015   -- Detalle anulación (Txcod=9: Hora / 709: Permanencia anterior / 749: Observaciones)
SELECT TOP 10 * FROM dbo.FSA030   -- Asientos desiguales
```

### Programas de contabilización

| Programa | Función |
|----------|---------|
| `PW103` | Contabiliza con preformato |
| `PP006` | Contabiliza |
| `PRG0010B` | Graba preformato / Crea cabezal FSD015 |

---
