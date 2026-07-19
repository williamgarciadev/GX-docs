---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 23. Impuestos y GMF"
source_id: 9000031
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 23. Impuestos y GMF

```sql
SELECT * FROM FSI001 WHERE cicpo='UVT'
SELECT * FROM FSI002 WHERE cicpo='UVT' AND cifech='2025-01-01 00:00:00.000'
SELECT * FROM FAIt01 WHERE FAImpCod=9
SELECT * FROM FAIt02 WHERE FAImpCod=9
SELECT * FROM FAIt03 WHERE faimpcod=9
```

### Programas

| Programa | Función |
|----------|---------|
| `HFAIR01` | Relación Transacción/Impuesto |
| `HFAIT01` | Mantenimiento de Impuesto |
| `hfaid01` | Condición por Impuesto/Persona |
| `HFAIT01` | Parametrización de Impuestos |

### GMF — Nueva reforma tributaria (Ley 2277 de 2022)

```sql
SELECT * FROM fst200 WHERE opgcod=20368     -- Habilita Notificaciones
SELECT * FROM fSI001 WHERE CICpo='RUB_GMF'  -- Opciones Generales
SELECT * FROM fSI006 WHERE CICpo='RUB_GMF'  -- Rubro
SELECT * FROM fste03                         -- Alta Notificaciones
SELECT * FROM fste01                         -- Mantenimiento Eventos
SELECT * FROM fst998 WHERE ngtipo=940        -- Tipo de Numerador
SELECT * FROM fst198 WHERE tp1cod1=645       -- Guía principal GMF
```

---
