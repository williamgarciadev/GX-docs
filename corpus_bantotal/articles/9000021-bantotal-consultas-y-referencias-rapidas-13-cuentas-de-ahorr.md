---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 13. Cuentas de Ahorro"
source_id: 9000021
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 13. Cuentas de Ahorro

### Tablas maestras

```sql
SELECT * FROM moi000  -- Estados de cuentas de ahorro
SELECT * FROM moi001  -- Detalle (Moi000cod = código de estado)
SELECT * FROM MPE001  -- Preformato Ctas de Ahorro
```

### Pizarras Ahorros

```sql
SELECT * FROM FSD025 WHERE Pgcod=1 AND Tamod=21  -- Ahorros
SELECT * FROM FSR025 WHERE Pgcod=1 AND Tamod=21  -- Ahorros
```

### Devengamiento

```sql
SELECT * FROM FST101 WHERE pbproc = 'PCC00003'
SELECT * FROM fsd130 WHERE devccmod = 21
SELECT * FROM fst004 WHERE modulo=21 AND totope=7
```

### Cuenta de Ahorros Niños / Junior

```sql
SELECT * FROM fst036 WHERE trmod=21 AND trnro=901   -- Rubro para alta de cuenta
SELECT * FROM FST098 WHERE TPCOD=1836                -- Módulo y Tipo de Operación
SELECT * FROM FST098 WHERE TPCOD=6065               -- Parámetros Titular y Apoderado
-- Corr1=Titular: Edad mínima (ValEsp) / Edad máxima (ImpEsp)
-- Corr2=Apoderado: igual estructura
SELECT * FROM fst098 WHERE tpcod=1543               -- Tipos de documento por alta
```

### FATCA

```sql
SELECT * FROM rep001 WHERE rep001cod IN (180,181)           -- Formulario PN y PJ
SELECT * FROM SNGDP1 WHERE sngdp1mod=22 AND sngdp1top=1    -- CDT FATCA
SELECT * FROM fst198 WHERE tp1cod1=14801 AND tp1corr1=4    -- Cuenta de Ahorros FATCA
```

### Programas

| Programa | Función |
|----------|---------|
| `hpap001` | Mantenimiento de Especies e Índices |
| `HPAP001C` | Confirmación modificaciones Cotizaciones de Especies |
| `hpp9040` | Administrador de Préstamos / Condonación / Pago de Créditos |
| `hsip570` | Alta de créditos reducida |
| `hsip571` | Alta reducida de Crédito |
| `hfsr601` | Cuentas para Cobranza de Préstamos |
| `hjcca060` | Determinación de la tasa para el crédito |

---
