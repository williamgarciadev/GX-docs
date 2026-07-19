---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 7. Tasas e Índices"
source_id: 9000015
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 7. Tasas e Índices

### IBR

```sql
SELECT * FROM FSD024
WHERE CLTCOD IN ('20','21','22','23','24','25','63','65','61','62','64')
AND TGFDES = '2023-01-27';
```

| Código | Descripción |
|--------|-------------|
| `20` | IBR Mes Nominal |
| `23` | IBR Mes Efectiva |
| `21` | IBR Trimestre Nominal |
| `24` | IBR Trimestre Efectiva |
| `22` | IBR Semestre Nominal |
| `25` | IBR Semestre Efectiva |
| `65` | IBR Diaria Nominal |
| `63` | IBR Diaria Efectiva |
| `61` | DTF Nominal |
| `62` | DTF Efectiva |
| `64` | DTF Trimestre |

### TRM

```sql
SELECT * FROM FSH005 WHERE MONEDA = 101 AND cofdes = '2022-10-19';
```

### UVR

```sql
SELECT * FROM FST098 WHERE TPCOD = 2823;
SELECT * FROM Fsh205 WHERE PAPEL = 111 AND PRFDES = '2021-06-01 00:00:00.000';
SELECT * FROM FST144 WHERE COECOD IN (111, 112);
```

### IPC

```sql
SELECT * FROM FSI002
WHERE pgcod = 1 AND cicpo = 'INFLACIO'
ORDER BY cifech;
```

### Orden de carga de tasas

```sql
SELECT * FROM FST205   -- Índices y Especies
SELECT * FROM FSE205
SELECT * FROM FSFIAJ
SELECT * FROM FBC201
SELECT * FROM FBC202
SELECT * FROM FBC203
SELECT * FROM FBC204
SELECT * FROM FSFICN
```

---
