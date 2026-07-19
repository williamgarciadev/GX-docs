---
title: "Sistema de Certificados de Depósito a Término (CDT) — 5.7 Cancelación Manual"
source_id: 9000059
source_url: "local:extra_docs/bantotal/MDU-10304-CO_Certificado_Deposito_a_Termino.md"
ingested_by: ingest_docs.py
---

## 5.7 Cancelación Manual

Existen procesos Batch que ejecutan las cancelaciones de forma automática al vencimiento de
las operaciones, a pesar de esto se deja la posibilidad de ejecutar de forma manual la cancelación
al vencimiento o en forma anticipada.

En lo que refiere a la cancelación anticipada se explicó que Bantotal cuenta con las siguientes
posibilidades:

- Se puede definir que en caso de cancelar en DPF dentro de x cantidad de días posteriores a
su apertura no pague interés alguno (PRTE256).

- Pagar intereses por la menor de las tasas entre la pizarra que le corresponde a la fecha de
cancelación y la que le hubiera correspondido en el momento del alta, considerando el plazo
transcurrido (PRTE006).

- Pagar a una determinada tasa castigo por el plazo transcurrido, ésta se debe definir en el
tipo de operación 98 del módulo de DPF (PRTE006).

- Pagar tasa diferente ya definida en otro módulo (por ejemplo cuenta de ahorro).
Si puede realizar la cancelación anticipada, diferenciándola según el plazo transcurrido del DPF y
dependiendo de ello indicar que pizarra utilizar o incluso imputar tasa 0 (PRTE006, Guía Especial
de Procesos Nº 11126).

Es posible exceptuar transacciones de la penalidad y que el programa no realice castigo. Por
último, también es posible penalizar mediante el cobro de comisiones parametrizables en la
transacción que corresponda.
