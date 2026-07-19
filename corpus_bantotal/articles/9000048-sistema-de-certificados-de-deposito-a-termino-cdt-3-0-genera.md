---
title: "Sistema de Certificados de Depósito a Término (CDT) — 3.0 Generación del Archivo a enviar al proveedor"
source_id: 9000048
source_url: "local:extra_docs/bantotal/MDU-10304-CO_Certificado_Deposito_a_Termino.md"
ingested_by: ingest_docs.py
---

## 3.0 Generación del Archivo a enviar al proveedor

Luego de ingresar las solicitudes, se puede generar de forma automática en el sistema un archivo
a enviarle al proveedor con el detalle de los certificados que debe generar el proveedor.

Para esto el usuario ingresa al panel “Archivo plano Chequeras/Certificados” (HCVCO001) y pulsa
el botón “Grabar Archivo”.

Para más información de la instalación ver docuemnto (ETP -10304-CO-V2R3.1 - ARCHIVO AL
PROVEEDOR DECHEQUERA – CERTIFICADO (HCVCO001)).

Fig.4 Archivo plano Chequeras/Certificados (programa HCVCO001)

Una vez que se procesan se muestra un mensaje con la cantidad de solicitudes procesadas:

Una vez generado el archivo, la solicitud cambia su estado a ‘Enviada al Proveedor’. Dicho estado
se puede validar mediante el acceso al stock de solicitudes de chequeras:

Fig.5 Solicitud de Chequeras (stock) (programa HSCH501)

Se indica el módulo 52 correspondiente a los certificados, y se selecciona Sucursal y estado.
Luego se pulsa ‘Filtrar’:
