---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 17. Reportes y Regulatorio"
source_id: 9000025
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 17. Reportes y Regulatorio

### Reporteador

```sql
SELECT TOP 10 * FROM dbo.REP001
SELECT TOP 10 * FROM dbo.REP002
SELECT TOP 10 * FROM dbo.REP003
SELECT TOP 10 * FROM dbo.REP004
```

### Reportes Normativos

```sql
SELECT * FROM fsi001  -- Campos de Información
SELECT * FROM fsi002  -- Valores Campo
SELECT * FROM fsi003  -- Integración de Informe
SELECT * FROM fsi004  -- Informes
SELECT * FROM fsi005  -- Campos Totalizadores
SELECT * FROM fsi006  -- Integración de Campo
SELECT * FROM fsi008  -- Agrupación de Campo
SELECT * FROM fsi010  -- Tipos de Campo
SELECT * FROM fsi011  -- Tipo de Importe
SELECT * FROM fsl001  -- Límite global por cuenta
```

### RACT — Reporte Anual de Costos Totales

```sql
SELECT * FROM dbo.DECO60   -- Parametrización de conceptos
SELECT * FROM dbo.DECO61   -- Parametrización de rubros - conceptos
SELECT * FROM dbo.DECO62   -- Parametrización de productos - conceptos
SELECT TOP 10 * FROM dbo.DECO63  -- Ejecución diaria

-- Programa en Cadena de Cierre:
SELECT * FROM fst101 WHERE PBPROC = 'PDECO310'
SELECT * FROM fst101 WHERE PBPROC = 'PDECO604'
SELECT * FROM fsr101 WHERE PBNSEC = 77007
SELECT * FROM fsr101 WHERE PBNSEC IN (1233, 1303)
SELECT * FROM fst198 WHERE tp1cod1 = 33301
```

### Consulta de desembolsos regulatorio

```sql
SELECT
    A.Hsucor AS SUCURSAL, A.HCMOD AS MODULO, A.HTRAN AS TRANSACCION,
    A.HNREL AS RELACION, B.HMODUL AS TIPO_DE_CREDITO,
    A.HFCON AS FECHA_DESEMBOLSO, A.HUSING AS USUARIO_DESEMBOLSO,
    B.HCTA AS CUENTA, B.HOPER AS OPERACION,
    C.PETDOC AS TIPO_IDENTIFICACION, C.PENDOC AS NUMERO_DOCUMENTO,
    E.PFAPE1 AS APELLIDO1, E.PFAPE2 AS APELLIDO2,
    E.PFNOM1 AS NOMBRE1,  E.PFNOM2 AS NOMBRE2,
    E.Pfcant AS SEXO,
    D.sngc11Dpto AS DEP_NACIMIENTO, D.SNGC11PROV AS CIUDAD_NACIMIENTO,
    D.sngc11Dat1 AS FECHA_EXP,
    G.SNGC60FINI AS FECHA_INICIO_NEGOCIO,
    F.PEXTXT AS CORREO_ELECTRONICO,
    G.SNGC60OCUP AS OCUPACION, G.SNGC60nome AS NOMBRE_NEGOCIO,
    G.SNGC60UBIC AS UBICACION_NEGOCIO, G.SNGC60RZSO AS RAZON_SOCIAL
FROM fsh015 AS A
INNER JOIN FSH016 AS B ON A.PGCOD=B.PgCod AND A.Hsucor=B.Hsucor AND A.Hcmod=B.Hcmod
    AND A.Htran=B.Htran AND A.HNREL=B.Hnrel AND A.HFCON=B.Hfcon
INNER JOIN FSr008 AS C ON B.HCTA=C.CTNRO
INNER JOIN SNGC11 AS D ON C.PETDOC=D.SNGC11TDOC AND C.PENDOC=D.SNGC11NDOC
INNER JOIN FSD002 AS E ON C.PETDOC=E.PFTDOC AND C.PENDOC=E.PFNDOC
INNER JOIN FSX001 AS F ON C.PETDOC=F.PETDOC AND C.PENDOC=F.PENDOC
INNER JOIN SNGC60 AS G ON C.PETDOC=G.SNGC60TDOC AND C.PENDOC=G.SNGC60NDOC
WHERE A.PgCod=1 AND A.Hcmod=30
    AND A.Htran IN (5,30,33,34,35,40,43,45,981,982)
    AND A.hfcon BETWEEN '2024-03-19' AND '2024-03-19'
    AND A.Hccorr <> 99 AND A.Htpoas <> 'A'
    AND B.Hcord=10 AND F.TXCOD=0 AND G.SNGC60CORR=0
ORDER BY B.Hoper;
```

---
