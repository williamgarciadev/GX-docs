---
title: "Sistema de Certificados de Depósito a Término (CDT) — 7.0 Instrucciones al Vencimiento"
source_id: 9000063
source_url: "local:extra_docs/bantotal/MDU-10304-CO_Certificado_Deposito_a_Termino.md"
ingested_by: ingest_docs.py
---

## 7.0 Instrucciones al Vencimiento

El cliente posee hasta el día de vencimiento de la operación para realizar la modificación de la
instrucción al vencimiento. La misma se realiza por medio del siguiente panel, en el mismo se
ingresan los datos de la cuenta y modulo al que pertenece la operación para la que se modificará
la instrucción:

Fig.10 Modificación de Instrucción de Operaciones (programa HW021)

Se pueden visualizar todas las operaciones desde la cuenta seleccionada, para el modulo,
sucursal, moneda y especie seleccionada.

Luego se selecciona la operación y se pueden visualizar las instrucciones asociadas:

Las posibles acciones del usuario son:

- El depósito tiene instrucción y se desean cambiar los datos de destino (por ejemplo: la
instrucción original es acreditar intereses en Cta. Cte. y el nuevo destino es Caja de Ahorro).
Este cambio se realiza a través del botón ‘Modificar’.

- El depósito no tiene instrucción: con el botón ‘Agregar’ se da de alta la instrucción, indicando
asimismo el destino.

- El depósito tiene instrucción y se desea modificar: (por ejemplo: la instrucción asociada
inicialmente es acreditar intereses en caja de ahorro y se quiere indicar renovación
automática): con el botón ‘Eliminar’ se elimina la instrucción actual y con ‘Agregar’ se da de
alta la nueva con los nuevos datos de destino.

- En lo que refiere al panel se puede manejar la autorización por excepción frente a la
modificación de una instrucción o condicionar el ingreso al panel para ciertos usuarios.
