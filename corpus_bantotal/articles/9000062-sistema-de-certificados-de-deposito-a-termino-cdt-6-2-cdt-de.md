---
title: "Sistema de Certificados de Depósito a Término (CDT) — 6.2 CDT Desmaterializado"
source_id: 9000062
source_url: "local:extra_docs/bantotal/MDU-10304-CO_Certificado_Deposito_a_Termino.md"
ingested_by: ingest_docs.py
---

## 6.2 CDT Desmaterializado

Si se ingresa un CDT desmaterializado al vencimiento (transacción 22/10). Los CDT nacen con
un estado específico que permite identificar para qué CDT se les asoció el código ISIN y cuáles
no. De esta forma una vez que se genera el alta del CDT se le debe asociar el código ISIN. A
continuación se muestra el ingreso del código ISIN.

Fig.9 Asignación Certificado CDT (programa HCDT0033)

En la pantalla se selecciona la operación y se ingresa el código ISIN a asociarle. Una vez asociado
el código ISIN el CDT pasa del estado “CDT Desmaterializados No Asig.” al estado “Normal”.

Se debe seleccionar en este caso el filtro de certificados “Desmaterializados”, se selecciona la
operación y se presiona el botón ‘Seleccionar’:

En la parte inferior se debe ingresar el código ISIN válido y se presiona el botón ‘Asignar’:

En este momento la operación pasa a estado “Normal”.

El código ISIN se puede consultar mediante el siguiente acceso:

Fig.10 Mantenimiento de ISIN (programa HCDT0033)
