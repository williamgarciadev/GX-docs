---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 30. Debug y Diagnóstico"
source_id: 9000038
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 30. Debug y Diagnóstico

```sql
-- Activar Debug (Opción General 2850)
SELECT * FROM fst098 WHERE TPCOD=2006 AND TPCORR=999
SELECT * FROM FST200 WHERE Pgcod=1 AND OpgCod=2850  -- Estado debug
SELECT * FROM FSADBG WHERE SADbgPrg='PJCCY023'      -- Registros debug
SELECT * FROM FSADBG WHERE SADbgUsu=' '             -- Debug por usuario

-- Foto del día anterior
SELECT TOP 10 * FROM dbo.RRCO03  -- Foto del día anterior de la FSD010

-- Facturas electrónicas
SELECT TOP 10 * FROM dbo.JCCI02  -- Consultar facturas electrónicas
```

### Análisis de hilos (FRTASKS)

```sql
SELECT TOP 100
    DATEDIFF(MINUTE, CONVERT(DATETIME, FRTskTimSt), CONVERT(DATETIME, FRTskTimEn)) AS diff, *
FROM dbo.FRTASKS
WHERE FRPrcId=2200 ORDER BY diff DESC;

SELECT TOP 100 * FROM dbo.FRTASKS
WHERE FRTskDsc LIKE '%Cartera%' ORDER BY FRTskTimCr DESC;
```

### Diagnóstico: Listas negras

```sql
-- Si tiene registros vacíos, las consultas de listas negras fallan para todos
SELECT TOP 10 * FROM dbo.FSD201 WHERE LnApeA='' AND LnNomA='';
```

### Consola de procesos

```
HFRPRCCONSOLE → Ver procesos en ejecución
HTRT200       → Debug  
hchkenv001    → Validación de ambiente
HFRSERVICES   → Reiniciar para tomar cambios
```

---

*Documento generado a partir de `Rapidas_2.txt` — Bantotal Core Bancario*
