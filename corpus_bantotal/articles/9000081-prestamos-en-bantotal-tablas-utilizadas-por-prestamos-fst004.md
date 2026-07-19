---
title: "Préstamos en Bantotal — Tablas utilizadas por préstamos — FST004: Tipos de operación por módulo"
source_id: 9000081
source_url: "local:extra_docs/bantotal/Prestamos_De_Larrobla_2001.md"
ingested_by: ingest_docs.py
---

## Tablas utilizadas por préstamos — FST004: Tipos de operación por módulo

```
*Modulo     N(3)     Modulo
*Totope     N(3)     Tipo Oper.
 Totpiz     N(2)     Tipo de Pizarra relacionada
 Tonom      C(30)    Nombre T.operac.
 Toperi     N(2)     Periodo de acredit.de interés
 Tosn1      C(1)     Analiza Historia?
 Tosn2      C(1)     Uso de Pizarra
 Tosn3      C(1)     Tosn3
 Tosn4      C(1)     Tosn4
 Tosn5      C(1)     Tosn5
 Tocd1      N(3)     Tocd1
 Tocd2      N(3)     Tocd2
 Tocd3      N(3)     Tocd3
 Tocd4      N(3)     Tocd4
 Tocd5      N(3)     Tocd5
 Toeleg     C(1)     ¿Elegible por el operador?
```

En esta tabla se definen los tipos de operación que soporta este módulo.
Por ejemplo, préstamo francés, préstamo alemán, etc.

Datos importantes en esta tabla: atributo **TOCD5**, indica el tipo de
préstamo que se utiliza con este tipo de operación:

- `0` = Plazo fijo
- `1` = Francés
- `2` = Alemán
- `3` = Plan de pagos
