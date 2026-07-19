---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 20. Control Dual"
source_id: 9000028
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 20. Control Dual

```sql
-- Guía especial 38: Correlativo 1 = 0 (sin Control Dual)
SELECT * FROM fst198 WHERE tp1cod1=38 AND tp1corr1=457;
-- 0 = Inhabilitado (directo a producción)
-- 1 = Sin control dual pero genera log
-- 2 = Control dual activo
```

### Tablas de Control Dual

```sql
SELECT * FROM CTD000  -- Configuración Tablas
SELECT * FROM CTD001  -- Configuración Campos Tablas
SELECT * FROM CTD006  -- Tablas Relacionadas
SELECT * FROM CTD007  -- Agrupador Tablas
SELECT * FROM fst200 WHERE OpgCod = 3054  -- Aprueba Masivo
SELECT * FROM fst098 WHERE tpcod = 3422   -- Orden aparición en pantalla
```

### Programas Control Dual

| Programa | Función |
|----------|---------|
| `HMDA401` | Cotizaciones de Cierre |
| `HMDA401C` | Confirmación Cotizaciones de Cierre |
| `HMDA402` | Mantenimiento de Pizarras |
| `HMDA402C` | Confirmación Mantenimiento de Pizarras |
| `HCTD001` | Mantenimiento de Tablas Control Dual |

---
