---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 1. Geografía y Estructura Organizacional"
source_id: 9000009
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 1. Geografía y Estructura Organizacional

### Tablas maestras

| Tabla | Descripción |
|-------|-------------|
| `FBC205` | Regiones |
| `FBC206` | Zonas |
| `FST811` | Relación Zona ↔ Oficina |
| `FST001` | Sucursales / Oficinas |
| `FST198` | Guías Especiales de Proceso |

### Consulta jerárquica: Región → Zona → Oficina

```sql
-- Región base
SELECT TOP 10 * FROM dbo.FBC205
WHERE BC205Id1D IN ('Codigo Zona','Código Zona')
ORDER BY BC205Id1D;

-- Región + Zona
SELECT TOP 10 * FROM dbo.FBC205 RE
    INNER JOIN dbo.FBC206 ZO ON RE.BC205Emp = ZO.BC205Emp AND RE.BC205Cod = ZO.BC205Cod
WHERE RE.BC205Cod IN (811, 812, 813, 814, 815)
ORDER BY RE.BC205Id1D;

-- Jerarquía completa: Región → Zona → Oficina (versión ordenada)
SELECT
    RE.BC205Emp, RE.BC205Cod, RE.BC205Dsc,
    ZO.BC206Id1, ZO.BC206Chr1,
    OFI.Sucurs, OFI.Scnom
FROM dbo.FBC205 RE
    INNER JOIN dbo.FBC206 ZO  ON RE.BC205Emp = ZO.BC205Emp AND RE.BC205Cod = ZO.BC205Cod
    INNER JOIN dbo.FST811 RZO ON ZO.BC205Emp = RZO.Pgcod AND ZO.BC206Id1 = RZO.RegCod
    INNER JOIN dbo.FST001 OFI ON RZO.Pgcod = OFI.Pgcod AND RZO.OfiCod = OFI.Sucurs
WHERE RE.BC205Emp = 1 AND RE.BC205Cod IN (811, 812, 813, 814, 815)
ORDER BY RE.BC205Emp, RE.BC205Cod, ZO.BC206Id1, OFI.Scnom;

-- Jerarquía completa desde Guía Especial
SELECT
    RE.BC205Emp, RE.BC205Cod, RE.BC205Dsc,
    ZO.BC206Chr1, RZO.RegCod,
    OFI.Sucurs, OFI.Scnom, OFI.Scciud, OFI.Scdept
FROM dbo.FBC205 RE
    INNER JOIN dbo.FBC206 ZO  ON RE.BC205Emp = ZO.BC205Emp AND RE.BC205Cod = ZO.BC205Cod
    INNER JOIN dbo.FST811 RZO ON ZO.BC205Emp = RZO.Pgcod AND ZO.BC206Id1 = RZO.RegCod
    INNER JOIN dbo.FST001 OFI ON RZO.Pgcod = OFI.Pgcod AND RZO.OfiCod = OFI.Sucurs
    INNER JOIN dbo.FST198 GRE ON GRE.Tp1nro1 = RE.BC205Cod
        AND GRE.Tp1cod = 1 AND GRE.Tp1cod1 = 81013
        AND GRE.Tp1corr1 = 10 AND GRE.Tp1corr2 = 20 AND GRE.Tp1corr3 <> 0;
```

### Consulta LEFT JOIN (oficinas sin región asignada incluidas)

```sql
SELECT * FROM dbo.FST001 SUC
LEFT JOIN (
    SELECT ZO.BC205Emp, RE.BC205Cod, RE.BC205Dsc, ZO.BC206Id1, ZO.BC206Chr1, RZO.OfiCod
    FROM dbo.FBC205 RE
        INNER JOIN dbo.FBC206 ZO  ON RE.BC205Emp = ZO.BC205Emp AND RE.BC205Cod = ZO.BC205Cod
        INNER JOIN dbo.FST811 RZO ON ZO.BC205Emp = RZO.Pgcod AND ZO.BC206Id1 = RZO.RegCod
    WHERE RE.BC205Id1D IN ('Codigo Zona','Código Zona') AND ZO.BC205Emp = 1
) RZO ON RZO.BC205Emp = SUC.Pgcod AND RZO.OfiCod = SUC.Sucurs
WHERE SUC.Pgcod = 1;
```

### Parametrización de Códigos de Regiones

```sql
-- Guía Especial 81013: Códigos de región
SELECT * FROM dbo.FST198
WHERE Tp1cod = 1 AND Tp1cod1 = 81013
    AND Tp1corr1 = 10 AND Tp1corr2 = 20 AND Tp1corr3 <> 0;

-- Guía Especial 81016: Reportes por región (zonificación)
SELECT * FROM FST198 WHERE TP1COD1 = 81016 AND TP1CORR1 = 10;
-- tp1nro1: quien puede ver (1=Todo / 5=Solo Oficina)
-- 10 = Reporte de mora | 30 = Reporte comparativo de cartera
```

### Geografía Colombia

```sql
SELECT TOP 10 * FROM dbo.FST068 WHERE Pais = 169  -- Departamentos
SELECT TOP 10 * FROM dbo.FST013 WHERE Pais = 169  -- País
SELECT TOP 10 * FROM dbo.FST070 WHERE Pais = 169  -- Ciudades
SELECT TOP 10 * FROM dbo.DECO50 WHERE DECO50PAIS = 169  -- Centro Poblado
SELECT TOP 10 * FROM dbo.FST071 WHERE Fst071Pai = 169   -- Barrios
SELECT TOP 10 * FROM dbo.FSE071                         -- Sector Barrio
```

---
