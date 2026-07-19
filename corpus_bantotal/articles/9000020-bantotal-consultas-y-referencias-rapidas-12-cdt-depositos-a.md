---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 12. CDT — Depósitos a Plazo"
source_id: 9000020
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 12. CDT — Depósitos a Plazo

### Estados del CDT (FST500 / FSD850)

| Código | Descripción |
|--------|-------------|
| `2` | Activado |
| `3` | Pendiente |
| `4` | Entregado |
| `7` | Custodia |
| `17` | Pendiente de Activar |
| `98` | Repuesto |
| `99` | Anulado |

### Pizarras CDT

```sql
SELECT * FROM FST053                                               -- Tipos de pizarra
SELECT * FROM FSD025 WHERE Pgcod=1 AND Tamod=22 AND Tpizar IN (1,3,8,9)  -- CDT monto
SELECT * FROM FSR025 WHERE Pgcod=1 AND Tamod=22 AND Tpizar IN (1,3,8,9)  -- CDT rango
```

### Guías CDT

```sql
SELECT * FROM FST198 WHERE Tp1cod1 = 70100  -- Calendario
SELECT * FROM FST198 WHERE Tp1cod1 = 57     -- Plazos y montos
```

### Tablas simulador CDT (actualización)

```sql
SELECT * FROM FPP015 WHERE pp010prd=22 AND pp015cod=12   -- Lista códigos numéricos
SELECT * FROM FPP026 WHERE pp010prd=22 AND pp026top=12   -- Lista códigos numéricos x Producto
SELECT * FROM FPP028 WHERE pp010prd=22 AND pp028top=12   -- Valores parámetro simple nivel Producto
SELECT * FROM FPP040 WHERE Pp028Mod=22 AND pp028top=12   -- Visibilidad parámetro
SELECT * FROM X054010 WHERE xpremod=22 AND xpretope=12   -- Productos (Módulos / Tipo op)
SELECT * FROM DP0501 WHERE DP0501MOD=22 AND DP0501TOP=12
SELECT * FROM DP0502 WHERE DP0502MOD=22 AND DP0502TOP=12
SELECT * FROM fst053 WHERE tpizar=12
SELECT * FROM DP00500 WHERE DP00500MOD=22 AND DP00500TOP=12
```

> **Último paso:** Ejecutar desde el llamador de programas el proceso `PDP09100`

---
