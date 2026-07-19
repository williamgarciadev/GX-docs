---
title: "Sistema de Certificados de Depósito a Término (CDT) — 9.2 Renovación CDTs (PDP00001)"
source_id: 9000067
source_url: "local:extra_docs/bantotal/MDU-10304-CO_Certificado_Deposito_a_Termino.md"
ingested_by: ingest_docs.py
---

## 9.2 Renovación CDTs (PDP00001)

Este proceso realiza la cancelación y cobro de los depósitos a plazo, así como la renovación de
los mismos.

El funcionamiento es el siguiente: recorre los saldos de rubros de capital vigente, con fecha menor
o igual a la fecha de proceso.

Procede según las instrucciones dadas en el alta. Para aquellos depósitos generados sin
instrucción se puede: acreditar en cuentas vista, renovar por un plazo de 30 días sólo el capital,
renovar por el plazo original del depósito sólo el capital, renovar el capital más los intereses o se
puede no tomar acción.

Para los CDT afectados en Garantía, se pueden renovar respetando la instrucción o sin importar
que instrucción tenga.

La contabilización de los movimientos es en el módulo 99, transacción 999.
