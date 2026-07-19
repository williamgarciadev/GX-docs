---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 21. Formiik"
source_id: 9000029
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 21. Formiik

```sql
SELECT * FROM homologacion
SELECT * FROM MasterMind.BITACORA_CATALOGOS WHERE CODIGOPETICION=9 ORDER BY secuencial DESC  -- Cargos

-- Documentos cargados
SELECT TOP 10 * FROM dbo.XWF700  -- Registro de Solicitud (XWFCar3: estados)
SELECT TOP 10 * FROM dbo.XWFD06  -- Documentos clientes - Cédula
SELECT TOP 10 * FROM dbo.XWFD01  -- Estado, tipo documento
SELECT TOP 10 * FROM dbo.XWFD02  -- Usuario, SHA, extensión

-- Datos exclusivos de Formiik
SELECT TOP 10 * FROM dbo.JCCM70
SELECT TOP 10 * FROM WFATTBVALUES  -- Valores de solicitud
SELECT TOP 10 * FROM WFATTSVALUES  -- Más datos de solicitud

-- Consulta Bus
SELECT * FROM MESSAGE_LOG
WHERE operation_Name LIKE ('CargueTercerosRelacionados')
ORDER BY id DESC;
```

### Programas Formiik

| Programa | Función |
|----------|---------|
| `hjccn403` | Mantenimiento motivos de negación rechazo |
| `hjccn551` | Mantenimiento Equivalencias (Catálogos de Formiik) |
| `HJCCN501` | Mantenimiento Equivalencia Sucursales Oficina |

---
