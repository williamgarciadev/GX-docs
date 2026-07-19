---
title: "Sistema de Certificados de Depósito a Término (CDT) — 5.6 Unificación"
source_id: 9000058
source_url: "local:extra_docs/bantotal/MDU-10304-CO_Certificado_Deposito_a_Termino.md"
ingested_by: ingest_docs.py
---

## 5.6 Unificación

La unificación de CDT es la unión de dos o más operaciones en una, es decir que se toman dos o
más CDTs para generar un único CDT. La unificación se puede realizar tanto para los CDTs
materializados como para los desmaterializados.

El sistema controla que los CDTs a unificar posean mismo plazo, tasa y fecha de vencimiento. En
caso de que las operaciones no cumplan estas condiciones no se podrán unificar.

Al realizar la unificación de CDTs materializados se cancelan las operaciones que se están
unificando y se emite un nuevo certificado con un nuevo nº de operación. Esta nueva operación
posee la misma fecha de vencimiento y tasa de los CDTs unificados, y el monto del capital es la
suma del valor de cada uno de los mismos.

Unificación de CDTs desmaterializados: previo a la realización de la unificación en el sistema el
Banco debe ingresar en la página de DECEVAL y realizar la unificación. De esta forma DECEVAL
emite un nuevo nº de ISIN que deberá ser asociado a la nueva operación unificada. Al igual que

en la unificación de los CDTs materializados se cancelan las operaciones que se están unificando
y se genera una nueva operación, con misma fecha de vencimiento y tasa de los CDTs unificados,
y monto de capital igual a la suma del valor del capital de cada uno de los CDTs unificados.

Esta transacción se ejecuta desde el siguiente punto de menú:

Al seleccionar la cuenta se pulsa el botón ‘Agregar’:

Luego de Filtrar por cuenta o cuenta operación, se seleccionan las operaciones a unificar con el
check y posteriormente se pulsa ‘Seleccionar’.
En caso de intereses por pagar para las operaciones seleccionadas, se emite este mensaje:

A modo de realizar el pago de los intereses, se ejecuta el programa PDP00004 (Punto 8.3).

Posteriormente
