---
title: "Patrón de 9 Campos Arquitectónicos de Bantotal"
source_id: 9000001
source_url: "local:extra_docs/bantotal/9-campos-clave.md"
ingested_by: ingest_docs.py
---

# Patrón de 9 Campos Arquitectónicos de Bantotal

Los 9 campos clave que definen la arquitectura transaccional del Core Bancario Bantotal V3R1.11.

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

## Significado Arquitectónico

Este patrón de 9 campos permite:

- **Identificación única**: CODOPER + FECDESDE + CODSUCU + CORRGRAL
- **Versionado temporal**: Múltiples versiones del mismo registro según FECDESDE
- **Auditoría completa**: Quién (USUACTU), cuándo (FECACTU/HORACTU) modificó
- **Trazabilidad**: Seguimiento completo del ciclo de vida de operaciones
- **Particionamiento**: CODSUCU permite distribuir datos por sucursal

## Identificación en Tablas

Para identificar si una tabla sigue este patrón:

1. Buscar la presencia de CODOPER (casi siempre presente en tablas transaccionales)
2. Verificar FECDESDE (indica versionado temporal)
3. Contar cuántos de los 9 campos están presentes
4. Tablas con 7+ de estos campos son consideradas "tablas arquitectónicas core"

## Ejemplo de Uso

```sql
-- Tabla típica con el patrón completo
CREATE TABLE FST001 (
    CODOPER   NUMERIC(7,0)  NOT NULL,  -- [1]
    FECDESDE  DATE          NOT NULL,  -- [2]
    CODSUCU   NUMERIC(3,0)  NOT NULL,  -- [3]
    CORRGRAL  NUMERIC(5,0)  NOT NULL,  -- [4]
    -- ... otros campos específicos de negocio ...
    FECACTU   DATE          NULL,      -- [5]
    HORACTU   NUMERIC(6,0)  NULL,      -- [6]
    USUACTU   VARCHAR(10)   NULL,      -- [7]
    FECDACTU  NUMERIC(8,0)  NULL,      -- [8]
    VERCFG    NUMERIC(3,0)  NULL,      -- [9]
    CONSTRAINT PK_FST001 PRIMARY KEY (CODOPER, FECDESDE, CODSUCU, CORRGRAL)
);
```

## Variaciones

No todas las tablas tienen los 9 campos:

- **Tablas maestras**: Pueden tener solo FECACTU, HORACTU, USUACTU (auditoría)
- **Tablas de parámetros**: Pueden omitir CODOPER/CORRGRAL
- **Tablas históricas**: Enfatizan FECDESDE para versionado temporal

## Consulta Rápida

| Campo | Tipo | Long | Función |
|-------|------|------|---------|
| CODOPER | N | 7 | Código operación |
| FECDESDE | D | - | Vigencia desde |
| CODSUCU | N | 3 | Sucursal |
| CORRGRAL | N | 5 | Correlativo |
| FECACTU | D | - | Fecha modificación |
| HORACTU | N | 6 | Hora modificación |
| USUACTU | C | 10 | Usuario modificador |
| FECDACTU | N | 8 | Fecha (numérica) |
| VERCFG | N | 3 | Versión config |
