---
title: "Sistema de Certificados de Depósito a Término (CDT) — 1.2 Manejo de Operación y Sub operación:"
source_id: 9000043
source_url: "local:extra_docs/bantotal/MDU-10304-CO_Certificado_Deposito_a_Termino.md"
ingested_by: ingest_docs.py
---

## 1.2 Manejo de Operación y Sub operación:

Al generarse un nuevo CDT, se le asigna un número de operación, este número identifica a la
inversión.
En la sub operación se almacena la cantidad de renovaciones que tuvo dicha inversión, nace en
0 y se incrementa en 1 cada vez que se renueva. Es decir que el número de operación se mantiene
constante frente a renovaciones y se incrementa la sub operación.

Por ejemplo:

Cliente 110000569
Operación 2116 sub operación 0 Capital $ 500.000
Operación 2300 sub operación 2 $ 60.000
La operación 2116 no fue renovada, mientras que la operación 2300 fue renovada 2 veces.
