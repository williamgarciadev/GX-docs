---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 3. Personas y Clientes"
source_id: 9000011
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 3. Personas y Clientes

### Maestro de personas

```sql
SELECT TOP 10 * FROM dbo.FSD001   -- Maestro de personas (Alta inconclusa: Pefbaj = '1830-01-01')
SELECT TOP 10 * FROM dbo.FSD002   -- Detalle personas natural/física (nombres, fecha nacimiento)
SELECT TOP 10 * FROM dbo.FSD003   -- Detalle personas jurídicas
SELECT TOP 10 * FROM dbo.FSR003   -- PJ - Representante Legal
SELECT TOP 10 * FROM dbo.FSD004   -- Detalle de empresas
SELECT TOP 10 * FROM dbo.FSD703   -- PJ extendido
SELECT TOP 10 * FROM dbo.FSD704   -- PJ extendido
```

### Datos complementarios

```sql
SELECT TOP 10 * FROM dbo.FSE001                    -- Extensión datos persona
SELECT TOP 10 * FROM dbo.FSE002                    -- Extensión datos persona / País: Nacionalidad
SELECT TOP 10 * FROM dbo.FSE201                    -- Documentos electrónicos
SELECT TOP 10 * FROM dbo.SNGC11                    -- Estrato / Lugar nacimiento / sngc11Dat1: Fecha expedición
SELECT TOP 10 * FROM dbo.SNGC11 WHERE sngc11Cmb2 = 1  -- Clientes marca PEP
SELECT TOP 10 * FROM dbo.SNGC81                    -- Clientes PEP - Información adicional
SELECT TOP 10 * FROM dbo.SNGC31                    -- Fecha expedición cédula
SELECT TOP 10 * FROM dbo.SNGC13 WHERE sngc13Corr = 1  -- Direcciones (Docod: 2=Personal / 4=Empresa)
SELECT TOP 10 * FROM dbo.SNGC32                    -- Direcciones por cuenta cliente
SELECT TOP 10 * FROM dbo.SNGC33                    -- Direcciones por cédula
SELECT TOP 10 * FROM dbo.FSD005                    -- Domicilios activos por personas
SELECT TOP 10 * FROM dbo.FSD006                    -- Domicilios activos por cuenta cliente
SELECT TOP 10 * FROM dbo.FSD212                    -- Categoría de clientes
SELECT TOP 10 * FROM dbo.FSR002 WHERE Rpccyg = 25  -- Relación personas con cónyuge
SELECT TOP 10 * FROM dbo.FSR008                    -- Integración Cuenta/Personas
SELECT TOP 10 * FROM dbo.FSE508                    -- Marcas cliente (FSE508Vic: Víctima)
SELECT TOP 10 * FROM dbo.DECO850                   -- Información financiera
```

### Actividad económica e información SARLAFT

```sql
SELECT TOP 10 * FROM dbo.SNGC60                                 -- Actividad CIIU
SELECT TOP 10 * FROM dbo.SNGC20 WHERE SNGC20CTA = 219159       -- Segmentación actual (campo SNGC20NM1)
SELECT TOP 10 * FROM dbo.SNGC70                                 -- Información adicional
-- sngc70Atr = 'HSNGCPF1_CHECK_1': Tratamiento datos
-- sngc70Atr = 'HSNGCPF1_CHECK_3': Autoriza envío correo
-- sngc70Atr = 'HSNGCPF1_CMBAUX4': Fondeador PN (val='3')
-- sngc70Atr = 'HSNGCPJ1_CHECK_1': Fondeador PJ (val='S')
SELECT TOP 10 * FROM dbo.SNG039  -- JOIN con SNGC70 (SNG039ValC = sngc70Val)
SELECT TOP 10 * FROM dbo.SNG036  -- JOIN con SNG039 (SNG036LtCo = SNG039LtCo)
```

### Correos electrónicos — consolidado en una línea

```sql
-- Versión STRING_AGG (SQL Server 2017+)
SELECT Pepais, Petdoc, Pendoc, Txcod,
    STRING_AGG(TRIM(Pextxt), ';')
FROM dbo.FSX001 WHERE Txcod = 0
GROUP BY Pepais, Petdoc, Pendoc, Txcod;

-- Versión STUFF + FOR XML (compatible versiones anteriores)
SELECT FX001.Pepais, FX001.Petdoc, FX001.Pendoc, FX001.Txcod,
    STUFF((
        SELECT TRIM(Pextxt), CASE WHEN Pextxt = '' THEN '' ELSE '|' END
        FROM dbo.FSX001 IFX001
        WHERE Pepais = 169 AND Txcod = 0
            AND IFX001.Pepais = FX001.Pepais
            AND FX001.Petdoc = IFX001.Petdoc
            AND IFX001.Pendoc = FX001.Pendoc
        FOR XML PATH('')
    ), 1, 0, '') CORREO
FROM dbo.FSX001 FX001
WHERE FX001.Pepais = 169 AND Txcod = 0
GROUP BY FX001.Pepais, FX001.Petdoc, FX001.Pendoc, FX001.Txcod;
```

### Tablas de referencia — Personas

```sql
SELECT TOP 10 * FROM dbo.FST014  -- Tipo de documento
SELECT TOP 10 * FROM dbo.FST020  -- Vínculos / Tipos de relaciones
SELECT TOP 10 * FROM dbo.FST023  -- Homologación géneros (sexo)
SELECT TOP 10 * FROM dbo.FST009  -- Estados civil
SELECT TOP 10 * FROM dbo.FST015  -- Tipos de domicilio
SELECT TOP 10 * FROM dbo.FST104  -- Sector
SELECT * FROM dbo.FST116         -- Códigos ocupación
SELECT * FROM dbo.FST114         -- Códigos nivel educativo
SELECT * FROM dbo.FST115         -- Códigos profesión
SELECT * FROM dbo.FST750         -- Códigos actividad económica
SELECT * FROM dbo.FST752         -- Códigos tipo actividad económica
SELECT * FROM dbo.SNGCP4         -- Tipos de identificación / longitud
SELECT TOP 10 * FROM dbo.FSR005  -- Teléfono personas
SELECT TOP 10 * FROM dbo.FSR006 WHERE Docod = 4 AND Doord = 1  -- Teléfono empresas
```

### Consulta completa de persona natural

```sql
SELECT DISTINCT
    B.Pftdoc AS TIPO_DOCUMENTO,
    A.PENDOC AS NUMERO_DOCUMENTO,
    A.Pepais AS PAIS_RESIDENCIA,
    G.sngc11Dpto AS DEP_NACIMIENTO,
    P.DepNom AS DEPARTAMENTO_NAC,
    G.SNGC11PROV AS CIUDAD_NACIMIENTO,
    O.LocNom AS NOMBRE_NACIM,
    B.Pfpnac AS PAIS_NACIMIENTO,
    G.sngc11Dat1 AS FECHA_EXP,
    J.SNGC31AUN1 AS DEP_EXP,
    Q.DepNom AS DEPARTENTO_EXP,
    J.SNGC31AUN2 AS CIUDAD_EXP,
    A.PETIPO AS TIPO_PERSONA,
    C.CTNRO AS CUENTA,
    B.PFAPE1 AS APELLIDO1, B.PFAPE2 AS APELLIDO2,
    B.PFNOM1 AS NOMBRE1,  B.PFNOM2 AS NOMBRE2,
    B.Pfcant AS SEXO,
    H.SNGC13PDOC AS PAIS_RESIDENCIA,
    H.sngc13Dpto AS DEPARTAMENTO,
    R.DepNom AS DEPARTAMENTO_NOM,
    H.sngc13Prov AS CIUDAD,
    M.LocNom AS NOMBRE_CIUDAD,
    H.DOCOD AS TIPO_DOMICILIO,
    H.SNGC13DIR AS DIRECCIÓN,
    I.SNGC60OCUP AS OCUPACIÓN,
    I.SNGC60NOME AS NOMBRE_NEGOCIO,
    I.SNGC60FINI AS FECHA_INIC_NEGOCIO,
    I.SNGC60AUX1 AS ORIGEN_RECURSOS,
    I.SNGC60TIPA AS TIPO_ACT,
    I.SNGC60ACTE AS CIIU,
    E.PEXTXT AS CORREO_ELECTRONICO
FROM FSD001 AS A
LEFT JOIN FSD002 AS B ON A.PETDOC = B.PFTDOC AND A.PENDOC = B.PFNDOC
LEFT JOIN FSR008 AS C ON A.PETDOC = C.PETDOC AND A.PENDOC = C.PENDOC
LEFT JOIN SNGC60 AS I ON A.PETDOC = I.SNGC60Tdoc AND A.PENDOC = I.SNGC60Ndoc
LEFT JOIN DECO850 AS K ON A.PETDOC = K.DECO850TDC AND A.PENDOC = K.DECO850NDC
LEFT JOIN SNGC11 AS G ON A.Pendoc = G.sngc11Ndoc
LEFT JOIN SNGC31 AS J ON A.PeTdoc = J.sngc31Tdoc AND A.PENDOC = J.SNGC31NDoc
LEFT JOIN SNGC13 AS H ON A.PeTdoc = H.sngc13Tdoc AND A.Pendoc = H.sngc13Ndoc
LEFT JOIN FSD006 AS D ON C.CTNRO = D.CTNRO
LEFT JOIN FSX001 AS E ON A.PETDOC = E.PETDOC AND A.PENDOC = E.PENDOC
LEFT JOIN FST070 AS M ON H.sngc13Prov = M.LOCCOD
LEFT JOIN FST070 AS O ON G.sngc11Prov = O.LOCCOD
LEFT JOIN FST068 AS P ON H.sngc13Dpto = P.DepCod
LEFT JOIN FST068 AS Q ON G.sngc11Dpto = Q.depcod
LEFT JOIN FST068 AS R ON H.sngc13Dpto = R.depcod
WHERE B.pfndoc = '1110558172'
    AND E.pexren = 1 AND E.txcod = 0
    AND G.sngc11Dat1 <> '1753-01-01 00:00:00.000'
    AND H.DOCOD IN (2,3,4)
ORDER BY A.Pendoc;
```

### Programas de alta de personas

| Programa | Función |
|----------|---------|
| `HSNGCA01` | Alta de persona |
| `HSNGCPF1` | Alta de persona física |
| `HSNGCPJ1` | Alta de persona jurídica |
| `HSNGC22` | Alta de domicilios |
| `HSNGC50` | Alta de cuenta cliente |
| `HSNGC48A` | Integración de cuentas |
| `HSNGCT14` | Condición ante impuestos |
| `HSNGCRD2` | Documentos adicionales |
| `HSNGCCHD` | Cambio de documento de persona |
| `HSNGC47` | Mantenimiento de domicilios |
| `HIF001A` | Alta de Instituciones Financieras / Creación cuentas bancos |

---
