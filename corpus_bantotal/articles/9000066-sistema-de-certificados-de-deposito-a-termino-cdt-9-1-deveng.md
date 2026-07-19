---
title: "Sistema de Certificados de Depósito a Término (CDT) — 9.1 Devengado a Plazo (PNU00002)"
source_id: 9000066
source_url: "local:extra_docs/bantotal/MDU-10304-CO_Certificado_Deposito_a_Termino.md"
ingested_by: ingest_docs.py
---

## 9.1 Devengado a Plazo (PNU00002)

Este proceso realiza el Devengado de intereses de las operaciones a plazo.

El funcionamiento es el siguiente: recorre los saldos de los rubros de capital de CDT. Realiza el
cálculo de interés hasta la fecha de proceso y asienta la diferencia entre el total de intereses y el
total ya contabilizado, tomando la tasa y el plazo de la operación y considerando si hubo cambios
en la tasa de la operación.

La contabilización de los movimientos es en el módulo 99, transacción 900.
