---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 10. Garantías"
source_id: 9000018
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 10. Garantías

```sql
SELECT * FROM FRI101             -- Garantía Real
SELECT * FROM jcca12             -- Tabla Garantías
SELECT * FROM ppg000             -- Atributo con texto
SELECT * FROM ppg001             -- Atributo con texto
SELECT * FROM ppg002             -- Atributo con relación / fecha
SELECT * FROM ppg010             -- Atributo
SELECT * FROM ppg011             -- Atributo x tipo de dato
SELECT * FROM ppg012             -- Atributo x Obligatorio y Habilitado
SELECT * FROM ppg008 WHERE ppg008cta = 5058  -- Tabla x Garantías
```

### WII112 — Valorización de Garantías

```sql
SELECT * FROM fst198 WHERE tp1cod1 = 56663  -- Define los atributos
SELECT * FROM fst101 WHERE pbproc IN ('PJCCA124','PJCCA125')
```

| Programa | Función |
|----------|---------|
| `PJCCA123` | Control del carga de archivo |
| `PJCCA124` | Valorización anual |
| `PJCCA125` | Diario - Avalúos que cumplen 3 años (reporte) |
| `PJCCA126` | Control adicional |

### Módulo y tipo de operación (Garantías)

| Módulo | Tipo | Descripción |
|--------|------|-------------|
| `70` | `30` | Hipotecario |
| `70` | `31` | Vehículo |

---
