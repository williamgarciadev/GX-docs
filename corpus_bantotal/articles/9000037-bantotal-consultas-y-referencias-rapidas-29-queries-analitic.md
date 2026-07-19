---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 29. Queries Analíticos Complejos"
source_id: 9000037
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 29. Queries Analíticos Complejos

### Consulta seguros (JCCA52)

```sql
SELECT DISTINCT
    A.JCCA52MOD AS MODULO, A.JCCA52SUC AS SUCURSAL,
    A.JCCA52CUC AS CUENTA,  A.JCCA52OPE AS OPERACION,
    B.PFNOM1 AS NOMBRE1,    B.PFNOM2 AS NOMBRE2,
    B.Pfape1 AS APELLIDO1,  B.PFAPE2 AS APELLIDO2,
    B.Pffnac AS FECHA_NACIMIENTO, B.Pfcant AS SEXO,
    A.JCCA52NDO AS NUMERO_DOCUMENTO, A.JCCA52TDO AS TIPO_DOCUMENTO,
    A.JCCA52SEG AS TIPO_SEGURO,      A.JCCA52ASE AS ASEGURADORA,
    A.JCCA52FIP AS FECHA_INICIO,     A.JCCA52FIP AS FECHA_FINAL,
    A.JCCA52PlC AS PLAZO,            A.JCCA52VPM AS VPM,
    A.JCCA52VAP AS VAP,              A.JCCA52VAR AS VAR,
    A.JCCA52EDP AS ESTADO,           A.JCCA52COM AS CODIGO,
    A.JCCA52CAS AS CODIGO_ASESOR
FROM JCCA52 AS A
LEFT JOIN FSD002 AS B ON A.JCCA52NDO = B.PFNDOC;
```

### Canje histórico

```sql
SELECT DISTINCT
    A.Hsucor AS SUCURSAL, A.HCMOD AS MODULO, A.HTRAN AS TRANSACCIÓN,
    C.Cle101Fch AS FECHA, A.HCTA AS CUENTA, A.HOPER AS OPERACION,
    A.Hnrel AS RELACION, A.Hcpzo AS PLAZO,
    C.CLE101BCO AS BANCO, C.CLE101ctal AS CTA_BANCO,
    A.Hccheq AS CHEQUE, A.HCIMP1 AS MONTO
FROM CLE101 AS C
LEFT JOIN fsH016 AS A
    ON C.CLE101SUC=A.Hsucor AND C.cle101cta=A.HCTA
    AND c.Cle101Chq=A.Hccheq AND C.Cle101Mod=A.Hmodul AND C.Cle101Imp=A.Hcimp1
LEFT JOIN fsh015 AS B
    ON A.PGCOD=B.PgCod AND a.hsucor=B.hsucor AND A.HCMOD=B.HCMOD
    AND A.Htran=B.Htran AND A.Hnrel=B.Hnrel AND A.HFCON=B.Hfcon
WHERE A.HCMOD=22 AND A.Htran IN (60,65,66)
    AND A.HTPOASR <> 'A' AND B.Hccorr <> 99
    AND A.Hrubro = '9170000021'
ORDER BY C.Cle101Fch;
```

### Pizarra de tasas (FSD026 + FSR026 + FSP026)

```sql
SELECT
    A.Comod AS Modulo, A.Cocod AS Pizarra, A.Cofech AS Fecha,
    A.Comto AS Monto, A.Cotasa AS Tasa,
    A.Comin AS Monto_Minimo, A.Comax AS Monto_Maximo, A.Coimp AS Importe,
    C.Comto AS Monto, C.Copzo AS Plazo, C.CotasaP AS Tasa,
    C.CominP AS Margen, C.ComaxP AS Maximo, C.CoimpP AS Importe
FROM FSD026 AS A
INNER JOIN FSR026 AS B ON A.Comod = B.Comod
INNER JOIN FSP026 AS C ON A.Comod = C.Comod
WHERE A.Comod=113 AND A.Cocod=11301
ORDER BY A.Cofech;
```

### Crédito mora y garantía real

```sql
SELECT *
FROM FRI101 AS A
LEFT JOIN SNG912 AS B ON A.RI101Cta=B.SNG912CTA AND A.RI101Ope=B.SNG912Op
WHERE SNG912DM > 1;
```

### Fondeadores

```sql
SELECT
    C70.Sngc11tdoc AS TipoId,
    C70.Sngc11ndoc AS Identificacion,
    ISNULL(D001.Penom,'') AS Nombre_Razon_social,
    ISNULL(R003.Pftdo1,0) AS TipoId_RL,
    ISNULL(R003.Pfndo1,0) AS Identificacion_RL,
    ISNULL(DR001.Penom,'') AS Nombre_RL,
    ISNULL(R003.Pfpai1,0) AS Pais_Sede_principal
FROM sngc70 C70
LEFT JOIN FSD001 D001  ON D001.pepais=c70.sngc11pais AND D001.petdoc=C70.Sngc11tdoc AND D001.Pendoc=C70.Sngc11ndoc
LEFT JOIN FSR003 R003  ON R003.pjpais=c70.sngc11pais AND R003.pjtdoc=C70.Sngc11tdoc AND R003.Pjndoc=C70.Sngc11ndoc AND vicod=1
LEFT JOIN FSD001 DR001 ON DR001.pepais=R003.pfpai1 AND DR001.petdoc=R003.pftdo1 AND DR001.Pendoc=R003.Pfndo1
WHERE (C70.sngc70Atr='HSNGCPF1_CMBAUX4' AND C70.sngc70Val='3')
   OR (C70.sngc70Atr='HSNGCPJ1_CHECK_1' AND C70.sngc70Val='S');
```

### Formas de desembolso (Órdenes de Pago)

```sql
-- Referencia: Reporte Regulatorio (FSH016.Hcord)
WHEN FSH016.Hcord='83' AND FSH016.Htran<>981 THEN '(Orden de Pago)'
WHEN FSH016.Hcord='81' AND FSH016.Htran=981  THEN '(Orden de Pago)'
WHEN FSH016.Hcord='75' AND FSH016.Htran=982  THEN '(Orden de Pago)'
WHEN FSH016.Hcord='82' AND FSH016.Htran=981  THEN '(Convenio)'
WHEN FSH016.Hcord='84' AND FSH016.Htran<>981 THEN '(Con cheque)'
WHEN FSH016.Hcord='83' AND FSH016.Htran=981  THEN '(Con cheque)'
WHEN FSH016.Hcord='84' AND FSH016.Htran=981  THEN '(Transferencia)'
WHEN FSH016.Hcord='85' AND FSH016.Htran<>981 THEN '(Transferencia)'
```

---
