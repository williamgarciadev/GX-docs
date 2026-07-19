---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 16. Cadena de Cierre"
source_id: 9000024
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 16. Cadena de Cierre

```sql
SELECT * FROM dbo.FST101   -- Tareas cadena de cierre
SELECT * FROM dbo.FSR101   -- Threads tareas cadena de cierre
SELECT * FROM dbo.CAP003   -- SQL tareas cadena de cierre
SELECT * FROM dbo.FST998   -- Tipos de numerador
SELECT * FROM dbo.FSN999   -- Numeradores
```

### Programas de Cadena

| Programa | Función |
|----------|---------|
| `hfst101` | Cadena de Cierre |
| `hcap003` | Mantenimiento de Paralelización |
| `HFRPRCCONSOLE` | Consola de Procesos |
| `HCONSOL` | Consola de Procesos |
| `hrgap001` | Trabajar con Procesos |

### Análisis por hilos (FRTASKS)

```sql
SELECT TOP 100
    DATEDIFF(MINUTE, CONVERT(DATETIME, FRTskTimSt), CONVERT(DATETIME, FRTskTimEn)) AS diff, *
FROM dbo.FRTASKS WHERE FRPrcId = 2200 ORDER BY diff DESC;

SELECT TOP 100 * FROM dbo.FRTASKS
WHERE FRTskDsc LIKE '%Cartera%' ORDER BY FRTskTimCr DESC;
```

---
