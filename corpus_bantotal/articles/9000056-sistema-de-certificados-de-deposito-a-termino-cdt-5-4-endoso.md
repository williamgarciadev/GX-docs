---
title: "Sistema de Certificados de Depósito a Término (CDT) — 5.4 Endoso/ Fraccionamiento"
source_id: 9000056
source_url: "local:extra_docs/bantotal/MDU-10304-CO_Certificado_Deposito_a_Termino.md"
ingested_by: ingest_docs.py
---

## 5.4 Endoso/ Fraccionamiento

La operación de endoso implica el traspaso del CDT de un titular a otro, llevado específicamente
a Bantotal Implica el cambio de una cuenta cliente a otra.
Para los materializados no se realiza la impresión ya que el endoso se escribe en la parte de atrás
del certificado original. Para el desmaterializado se traspasa el Nº de ISIN.

El endoso se ingresa desde el panel de ingreso de transacciones al igual que el fraccionamiento.
A continuación se muestra el ingreso de un endoso en Bantotal.

### 5.4.1 Endoso

Se ingresa al panel de ejecución, se selecciona la transacción 40 y se oprime el botón
‘Seleccionar’:

Se selecciona la operación de endoso, la operación a endosar y se presiona el botón ‘Ejecutar’:

Se visualiza el detalle de la operación por pantalla y se oprime el botón ‘Proceder’ para continuar
con el ingreso del endoso:

Se ingresa el número de cuenta a la cual se le endosa el CDT, se ingresa la instrucción para la
operación y se presiona el botón ‘Validar’.

En caso de validarse los datos ingresados se habilita el botón ‘Confirmar’:

Se confirma la transacción:

Se verifica que el CDT se visualiza de forma correcta en la cuenta cliente nº 12:

### 5.4.2 Fraccionamiento

Se ejecuta la misma transacción indicada en el punto 5.3.1, seleccionando la opción
Fraccionamiento:

Se realiza tanto para materializados como para desmaterializados. Se emiten X nuevos
certificados con nuevos nº de operación y titulares. DECEVAL emite un nuevo nº ISIN por cada CDT
fraccionado.

Mediante este panel se indica el monto de las fracciones hasta que el Saldo Restante queda en
0. Por cada cuenta/monto, se indica ‘Proceder’, hasta quedar en 0.

En este caso se pulsa validar, y al completar el Saldo, se muestra el siguiente panel:

Se debe indicar ‘Confirmar’ tantas veces como se haya fraccionado.

Luego se continúa con la ejecución de la transacción hasta confirmar:
