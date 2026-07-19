---
title: "Sistema de Certificados de Depósito a Término (CDT) — 9.3 Pago Periódico de Intereses de CDTs (PDP00004)"
source_id: 9000068
source_url: "local:extra_docs/bantotal/MDU-10304-CO_Certificado_Deposito_a_Termino.md"
ingested_by: ingest_docs.py
---

## 9.3 Pago Periódico de Intereses de CDTs (PDP00004)

Este proceso realiza el pago periódico de aquellos depósitos que tengan dicha condición.

El funcionamiento es el siguiente: para aquellos depósitos, con instrucciones 7 y 8, recorre los
días de revisión y si corresponde se procede a la acreditación de los intereses. Para los depósitos
con instrucción 7(acreditación periódica de intereses) se acredita según lo indicado en la apertura
del mismo.

Para aquellos depósitos con instrucción 8 (capitalización de intereses) los intereses se
capitalizan.

La contabilización de los movimientos es en el módulo 99, transacción 920.
