---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 5. Préstamos y Cartera"
source_id: 9000013
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 5. Préstamos y Cartera

### Tablas maestras de préstamos

```sql
SELECT TOP 10 * FROM dbo.FSD010  -- Maestro de préstamos
SELECT TOP 10 * FROM dbo.FSD011  -- Saldos contables / Contable de préstamos
SELECT TOP 10 * FROM dbo.FSD014  -- Datos rubros
SELECT TOP 10 * FROM dbo.FSR014  -- Rubros
SELECT TOP 10 * FROM dbo.FST042  -- Relación de rubros
SELECT TOP 10 * FROM dbo.FSR012  -- Relcod=88: Codeudor / Relcod=77: Agentes
SELECT TOP 10 * FROM dbo.FRI101  -- Garantía Real
SELECT TOP 10 * FROM dbo.SNG912  -- Días de mora (SNG912DM)
-- Campos tablón: SNG912Vc=Cuota / SNG912iC=IVA / SNG912Cc=Comisión / SNG912sG=Seguro
```

### Estados de los créditos (FSD010.aostat)

| Código | Descripción |
|--------|-------------|
| `0` | Normal |
| `33` | Castigado |
| `60` | Reestructurado o Reprogramado |
| `61` | Renegociado o Refinanciado |
| `62` | Renovado |
| `63` | Cobro Administrativo |
| `64` | Cobro Judicial |
| `99` | Cancelado |

### Calificación de cartera

```sql
SELECT TOP 10 * FROM dbo.JCCA01  -- Calificación, Frecuencia
SELECT TOP 10 * FROM dbo.JCCA02  -- Calificación
SELECT TOP 10 * FROM dbo.JCCA60  -- Tasa determinación
-- Conteo por estado:
SELECT JCCA60EST, COUNT(*) FROM jcca60 GROUP BY JCCA60EST;
```

### Análisis de una operación específica

```sql
-- Reemplazar 225000167 con el número de operación
SELECT * FROM fsd601 WHERE ppoper = 225000167 ORDER BY Ppfval;
SELECT * FROM fsd602 WHERE ppoper = 225000167 ORDER BY Ppfpag;
SELECT * FROM fsd611 WHERE ppoper = 225000167 ORDER BY Ppfpag;
SELECT * FROM fsd612 WHERE ppoper = 225000167 ORDER BY Ppfpag;
SELECT * FROM fsd010 WHERE aooper = 225000167;
SELECT * FROM fsd011 WHERE Scoper = 225000167 AND SCMOD = 113;
SELECT * FROM X054023 WHERE xllaooper = 225000167;
SELECT * FROM fpp002 WHERE ppoper = 225000167 ORDER BY Ppfpag;
```

### Tablas por cliente (template)

```sql
-- Reemplazar '55131069' y cuentas según el caso
SELECT * FROM FSD001 WHERE PENDOC = '55131069'           -- Maestro persona
SELECT * FROM FSD002 WHERE PFNDOC = '55131069'           -- Datos persona
SELECT * FROM FSR008 WHERE PENDOC = '55131069'           -- Doc → cuenta
SELECT * FROM FSR002 WHERE rpndoc = '55131069'           -- Relaciones
SELECT * FROM FSE001 WHERE d511ndoc = '55131069'         -- Extensión
SELECT * FROM FSE002 WHERE pfxndoc = '55131069'          -- Extensión datos
SELECT * FROM FSD008 WHERE ctnro IN (404028, 404033)     -- Cuentas
SELECT * FROM fsd010 WHERE aocta IN (404028, 404033)     -- Préstamos
SELECT * FROM fsd012 WHERE aocta IN (404028, 404033)     -- Eventos
SELECT * FROM fsd011 WHERE sccta IN (404028, 404033)     -- Saldos
```

### Solicitudes de crédito

```sql
SELECT TOP 10 * FROM dbo.SNG001   -- Solicitud de crédito / Instancia de préstamo
SELECT TOP 10 * FROM dbo.SNG002   -- Solicitud (detalle)
SELECT TOP 10 * FROM dbo.SNG021   -- Usuario que creó la solicitud (Formiik)
SELECT TOP 10 * FROM dbo.SNG120   -- Estados de las solicitudes de crédito
```

### Solicitudes rechazadas (JCCN52)

```sql
SELECT jccn52tdo, jccn52ndo, jccn52nom, JCCN52Ape, jccn52cas,
       jccn52sol, jccn52fan, jccn52cet, jccn52cmo, jccn52obs
FROM jccn52
WHERE jccn52fan BETWEEN '2026-01-01 00:00:00.000' AND '2026-01-13 00:00:00.000';
-- jccn52cet = Etapa | jccn52cmo = Motivo
SELECT * FROM jccn53  -- Etapas
SELECT * FROM jccn54  -- Motivos
```

### Préstamos anulados

```sql
SELECT TOP 10 * FROM dbo.JCCN52  -- Préstamos anulados (KnockOut)
SELECT TOP 10 * FROM dbo.JCCN54  -- Condiciones de anulación
```

### Módulos con saldo

```sql
SELECT DISTINCT FT111.Modulo
FROM dbo.FSD011 FD11
    INNER JOIN dbo.FST111 FT111
        ON FD11.Pgcod = FD11.Pgcod
        AND FT111.Modulo = FD11.Scmod
        AND FT111.Dscod = 50
WHERE FD11.Pgcod = 1 AND FD11.Sccta BETWEEN 0 AND 999999999;
```

---
