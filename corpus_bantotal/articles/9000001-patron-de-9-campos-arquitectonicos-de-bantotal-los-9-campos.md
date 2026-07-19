---
title: "Patrón de 9 Campos Arquitectónicos de Bantotal — Los 9 Campos Fundamentales"
source_id: 9000001
source_url: "local:extra_docs/bantotal/9-campos-clave.md"
ingested_by: ingest_docs.py
---

## Los 9 Campos Fundamentales

Estas columnas aparecen en la mayoría de las tablas transaccionales de Bantotal y definen el modelo operativo:

1. **CODOPER** (N, 7)
   - Código de operación
   - Identifica la transacción u operación bancaria
   - Parte de la clave primaria en tablas transaccionales

2. **FECDESDE** (D)
   - Fecha desde vigencia
   - Define el inicio de vigencia del registro
   - Clave para versionado temporal

3. **CODSUCU** (N, 3)
   - Código de sucursal
   - Identifica la sucursal donde se realizó la operación
   - Parte de la segmentación organizacional

4. **CORRGRAL** (N, 5)
   - Correlativo general
   - Número secuencial de la operación
   - Garantiza unicidad dentro de una operación

5. **FECACTU** (D)
   - Fecha de actualización
   - Última fecha en que se modificó el registro
   - Auditoría de cambios

6. **HORACTU** (N, 6)
   - Hora de actualización (formato HHMMSS)
   - Hora exacta de la última modificación
   - Complementa FECACTU para auditoría

7. **USUACTU** (C, 10)
   - Usuario actualizador
   - Código del usuario que realizó la última modificación
   - Trazabilidad de cambios

8. **FECDACTU** (N, 8)
   - Fecha de actualización en formato numérico (AAAAMMDD)
   - Versión numérica de FECACTU
   - Facilita ordenamiento y comparaciones

9. **VERCFG** (N, 3)
   - Versión de configuración
   - Versión del esquema/configuración de la tabla
   - Permite evolución del modelo sin romper compatibilidad
