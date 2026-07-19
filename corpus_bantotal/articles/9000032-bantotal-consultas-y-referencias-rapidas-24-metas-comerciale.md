---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 24. Metas Comerciales"
source_id: 9000032
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 24. Metas Comerciales

```sql
SELECT * FROM FST098 WHERE tpcod=81004   -- Las regiones
SELECT * FROM fbc205 WHERE bc205cod IN (811,812,813,814,815,816)
SELECT * FROM fbc206 WHERE bc205cod IN (811,812,813,814,815)
SELECT * FROM JCCY12 WHERE jccy12anio=2023 AND JCCY12DOfi LIKE '%Barbosa%'  -- Generales
SELECT * FROM JCCY13 WHERE jccy13anio=2024 AND JCCY13DOfi LIKE '%Barbosa%'  -- Detalladas
```

### Programas de Metas

| Programa | Función |
|----------|---------|
| `hjccy008` | Cargue de Metas |
| `hjccy009` | Asignación Metas |
| `hjccy010` | Metas comerciales asesor |
| `hjccy011` | Metas comerciales zona |
| `hjccy014` | Ajuste Metas oficina |
| `hjccy018` | Visualización Metas Comerciales |

### Jerarquía comercial

```sql
SELECT
    A.BC205Cod AS CODIGO_REGION, A.BC205Dsc AS NOMBRE_REGION,
    B.BC206Id1 AS CODIGO_ZONA,   B.BC206Chr1 AS NOMBRE_ZONA,
    C.OFICOD AS CODIGO_OFICINA,  D.SCNOM AS NOMBRE_SUCURSAL
FROM fbc205 AS A
INNER JOIN fBc206 AS B ON A.BC205EMP=B.BC205EMP AND A.BC205Cod=B.BC205Cod
INNER JOIN FST811 AS C ON A.BC205EMP=C.Pgcod AND B.BC206ID1=C.REGCOD
INNER JOIN FST001 AS D ON A.BC205EMP=c.PGCOD AND C.OFICOD=D.Sucurs
WHERE A.bc205cod IN (811,812,813,814,815,816)
ORDER BY CODIGO_REGION;
```

---
