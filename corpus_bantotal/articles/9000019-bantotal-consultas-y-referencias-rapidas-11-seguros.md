---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 11. Seguros"
source_id: 9000019
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 11. Seguros

```sql
SELECT TOP 10 * FROM dbo.FSD611  -- Seguros / Intereses (plan de pago)
SELECT TOP 10 * FROM dbo.FSD612  -- Pago Seguros/Intereses
SELECT * FROM dbo.FST300         -- Tipos de Seguros
SELECT * FROM JCCA52             -- Uno a uno de las pólizas
SELECT * FROM X054011 WHERE sgcod IN (123,...,139)  -- Seguros nuevos / Seteo Producto
SELECT * FROM FST098 WHERE tpcod = 13429            -- Seguro Voluntario y Obligatorio
SELECT * FROM FPP065 WHERE PP065sgcod IN (...)      -- Pizarras
SELECT * FROM FST301                                -- Tipo de Seguros
```

### Consulta seguros por operación

```sql
SELECT Aomod, Aosuc, Aocta, Aooper, Aotope, Aofval, Aofvto, Aopzo, Aoimp, Aoperiod,
       Aofinc, Ppfpag, Ppimp11, Ppimp12, Ppimp13
FROM FSD010
LEFT JOIN FSD611
    ON FSD010.Pgcod = FSD611.Pgcod AND FSD010.Aomod = FSD611.Ppmod
    AND FSD010.Aomda = FSD611.Ppmda AND FSD010.Aosuc = FSD611.Ppsuc
    AND FSD010.Aosbop = FSD611.Ppsbop AND FSD010.Aooper = FSD611.Ppoper
    AND FSD010.Aopap = FSD611.Pppap AND FSD010.Aocta = FSD611.Ppcta
    AND FSD010.Aotope = FSD611.Pptope
WHERE Aofval >= '2024-06-20' AND Aomod IN (111, 103, 113)
    AND aostat <> 99 AND Pptipo <> 'K'
ORDER BY AOCTA, AOOPER, PPFPAG;
```

---
