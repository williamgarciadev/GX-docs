---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 4. Cuentas Cliente"
source_id: 9000012
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 4. Cuentas Cliente

```sql
SELECT TOP 10 * FROM dbo.FSD008   -- Maestro cuentas cliente
SELECT TOP 10 * FROM dbo.FSR008   -- Integración Cuenta/Personas (ctccli: 1=Nuevo, 2=Antiguo, 3=Preferencial)
SELECT TOP 10 * FROM dbo.FST049   -- Tipo cliente FSD008
```

### Clasificación de clientes (FSR008.ctccli)

| Valor | Significado |
|-------|-------------|
| `1` | Cliente Nuevo |
| `2` | Cliente Antiguo |
| `3` | Cliente Preferencial |

---
