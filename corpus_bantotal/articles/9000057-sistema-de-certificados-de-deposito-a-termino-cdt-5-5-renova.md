---
title: "Sistema de Certificados de Depósito a Término (CDT) — 5.5 Renovaciones"
source_id: 9000057
source_url: "local:extra_docs/bantotal/MDU-10304-CO_Certificado_Deposito_a_Termino.md"
ingested_by: ingest_docs.py
---

## 5.5 Renovaciones

Se ejecutan desde ingreso de operaciones.

Se selecciona una transacción y se pulsa ‘Seleccionar’:

En casos de prueba, se debe visualizar el vencimiento de una operación y modificar la fecha de
apertura a tal fecha que permita ingresar la renovación. De lo contrario se presenta el siguiente
error:

Accedemos a la Consulta de Situación de Cuentas, y validamos el vencimiento de una
operación:

Se modifica fecha de apertura:

Se selecciona una transacción de renovación desde Menú de Ingreso de Operaciones/Ingreso
CDT’s:

Se selecciona una operación con vencimiento correspondiente al día de la fecha de apertura y
vencimiento de la operación. Se pulsa ‘Seleccionar’.

Se digita plazo o vencimiento nuevo.

Se pulsa ‘Continuar’:

Se selecciona una forma de pago:

Se pulsa el botón Asiento para visualizar el movimiento contable:

Existen procesos Batch que ejecutan las renovaciones de forma automática al vencimiento de las
mismas, a pesar de esto, existe la posibilidad de ejecutar de forma manual la renovación en caso
que el cliente se presente en la sucursal.
Es preferible que las renovaciones se realicen de forma automática pero es posible que el usuario
lo ejecute de forma manual.
