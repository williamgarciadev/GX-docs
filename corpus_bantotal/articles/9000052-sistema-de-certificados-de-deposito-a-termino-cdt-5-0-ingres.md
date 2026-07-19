---
title: "Sistema de Certificados de Depósito a Término (CDT) — 5.0 Ingreso de CDTs"
source_id: 9000052
source_url: "local:extra_docs/bantotal/MDU-10304-CO_Certificado_Deposito_a_Termino.md"
ingested_by: ingest_docs.py
---

## 5.0 Ingreso de CDTs

Consideraciones en el alta del producto:

- Plazo: Bantotal permite el ingreso del plazo de la operación en días o de la fecha de
vencimiento. El usuario en el alta ingresa alguno de los parámetros el sistema calcula el otro.

- Ajuste del Plazo: Bantotal permite definir cómo se ajustará el vencimiento del plazo fijo en
caso que para el plazo o día de vencimiento seleccionado caiga en un día no hábil. Las
opciones de ajuste son: No Ajustar, Ajustar a Hábil Posterior o Hábil Anterior.

- Período: Para los Plazos Fijos que poseen acreditación periódica de interés se habilita el
ingreso de la periodicidad. Aquí se establece la cantidad de días entre los pagos de intereses.
El usuario debe ingresar el monto.

- Tipo de Plazo: El manejo de tipo de año: calendario o comercial puede ser parametrizable en
el alta del producto.

- Tasa pizarra: Bantotal toma la tasa de pizarra vigente para la fecha valor del alta. Se
ejecutaron distintas altas mostrando cómo dependiendo del capital del CDT, plazo y moneda
toma distintas tasas. El usuario puede modificar las tasas de pizarra dentro del rango de
tolerancia, en caso de modificarse fuera del rango de tolerancia se emite una autorización
por excepción.

- Divisor Tasa: Se mostró como a nivel del transaccional se define el divisor utilizado para la
tasa de interés.

- Instrucciones: En el alta del plazo fijo se puede definir dos tipos de instrucción: las que se
ejecutan al vencimiento del Plazo Fijo y las que se ejecutan a lo largo de la vida del mismo.

- Instrucciones al vencimiento. En el alta del Certificado de Depósito a Término se puede definir
qué acción se tomará con el capital y los intereses al vencimiento de la inversión. Esta
instrucción se ejecuta de forma automática por un proceso Batch. Las posibles instrucciones
son: “Acreditar interés y Capital”, “Acreditar interés y Renovar Capital” o “Renovación
Automática total”. Los códigos utilizados en Bantotal a nivel de instrucciones son: 2
representa “Acreditar interés y Capital”, 4 representa “Acreditar interés y Renovar Capital” y
6 corresponde a “Renovación automática total”. Para las instrucciones 2 y 4 se le debe definir
donde se acreditarán los fondos.

- Instrucciones en la vida del CDT: Para los Plazos Fijos con pago periódico de interés se debe
definir donde se acreditarán los intereses. El código Bantotal para esta instrucción es 7. La
acreditación de dicho interés se hace automática por medio de un proceso Batch
Bantotal permite definir para las instrucciones 2, 4 y 7 una cuenta cliente distinto a la del
CDT. Se puede definir para que no sea posible asociarle una cuenta cliente distinta a la del
plazo fijo.

El ingreso de los CDTs se realiza por medio de la ejecución de transacciones. Mediante el panel
de ingreso de transacciones el usuario puede visualizar todas las transacciones habilitadas para
el módulo. El panel es el siguiente:
