---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 15. Servicios Web Bantotal (BTI)"
source_id: 9000023
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 15. Servicios Web Bantotal (BTI)

### Consulta de servicio

```sql
DECLARE @service NVARCHAR(MAX) = 'BTNotificaEmbargo'

SELECT * FROM dbo.BTI004 WHERE BTISrvNom = @service   -- Servicios por Interfaz
SELECT * FROM dbo.BTI007 WHERE BTISrvNom = @service   -- Usuarios habilitados por Servicio/Método-Canal
SELECT * FROM dbo.BTI012 WHERE BTISrvNom = @service   -- Servicios/Métodos por Canal
SELECT * FROM dbo.BTI014 WHERE BTISrvNom = @service   -- Interfaz Servicios - Métodos
SELECT * FROM dbo.BTI019 WHERE BTISrvNom = @service   -- Parámetros de Métodos de Servicios
SELECT * FROM dbo.BTI025 WHERE BTISDTNom = 'SdtNotificaEmbargo_NotificaEmbargoItem'  -- SDT
SELECT * FROM dbo.BTI026 WHERE BTISDTNom = 'SdtNotificaEmbargo_NotificaEmbargoItem'  -- Elementos SDT
```

### Eliminar servicio (usar con precaución)

```sql
-- Descomentar solo cuando sea necesario eliminar
--DELETE FROM dbo.BTI004 WHERE BTISrvNom = @service
--DELETE FROM dbo.BTI007 WHERE BTISrvNom = @service
--DELETE FROM dbo.BTI012 WHERE BTISrvNom = @service
--DELETE FROM dbo.BTI014 WHERE BTISrvNom = @service
--DELETE FROM dbo.BTI019 WHERE BTISrvNom = @service
--DELETE FROM dbo.BTI025 WHERE BTISDTNom = 'SdtNotificaEmbargo_NotificaEmbargoItem'
--DELETE FROM dbo.BTI026 WHERE BTISDTNom = 'SdtNotificaEmbargo_NotificaEmbargoItem'
```

### Consulta autorización de servicios

```sql
SELECT * FROM BTI012  -- Permiso Canal/Servicio
SELECT * FROM BTI007  -- Permisos Usuario/Servicio/Método
SELECT * FROM BTI004  WHERE BTINom='BANTOTAL' AND BTISrvNom='CreditosDECO'
SELECT * FROM BTI014  WHERE BTINom='BANTOTAL' AND BTISrvNom='CreditosDECO'
SELECT * FROM BTI019  WHERE BTINom='BANTOTAL' AND BTISrvNom='CreditosDECO'
SELECT * FROM BTI012  WHERE BTICanNom='BTDIGITAL' AND BTINom='BANTOTAL' AND BTISrvNom='CreditosDECO'
SELECT * FROM BTI001  WHERE BTICanNom='BTDIGITAL'
```

### SDTs

```sql
SELECT * FROM BTI019 WHERE BTISrvNom='BTDepositosAPlazo' AND BTIMtdNom='ObtenerProductosHabilitados'
SELECT * FROM BTI025 WHERE BTISDTNom='SdtsBTProductoDepositoAPlazo'
SELECT * FROM BTI026 WHERE BTISDTNom='SdtsBTProductoDepositoAPlazo'
```

### Programas Bantotal (llamadas)

```
PW103      Call(&Programa, &PgCod, &ItMod, &Ittran, &Itnrel, &Pgfape, &MnCod)    -- Contabiliza con preformato
PRg0010    Call(&Programa, &Pgcod, &Itsuc, &Itmod, &Ittran, &Itnrel)             -- Siguiente Relación
PP006      Call(&Programa, &Pgcod, &Itsuc, &Itmod, &Ittran, &Itnrel, &Pmncod)   -- Contabiliza
PRG0010B   Call(&Programa, &Pgcod, &Itsuc, &Itmod, &Ittran, &Itnrel)             -- Graba Preformato
```

### Generación de UID

```
1. Ingresar a HBTSBT2 — Panel de Generación De Identificador Único (UID)
2. Generar identificador → seleccionar operaciones
3. Módulo 21 / Sucursal 64 / Moneda 0 / Cuenta 200198
4. Generar UID
```

---
