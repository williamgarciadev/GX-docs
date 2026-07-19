# Sistema de Certificados de Depósito a Término (CDT)

## Introducción

Los objetivos de este documento son:

- Generar una guía para el uso de la operativa.

- Mostrar las funcionalidades que componen el sistema.

## Descripción del Negocio

CDT es la abreviatura de Certificado de Depósito a Término y es principalmente un instrumento
financiero en el cual se deben tener dos aspectos en cuenta:

- El monto mínimo o de apertura del CDT.

- El tiempo o duración de la inversión.

Permite a la entidad financiera captar una cantidad de dinero por cierto periodo de tiempo; la
entidad financiera, luego de vencido el tiempo o duración del CDT le devuelve su dinero al cliente,
junto con sus intereses.

El banco puede invertir tranquilamente el dinero de un CDT sin preocuparse por el cliente, lo que
le permite rentabilizar el 100% del dinero, algo que no puede hacer con un depósito de una cuenta
de ahorros.

El dinero es retenido, hasta el término del periodo, antes de ello, el cliente no puede acceder al
mismo y si lo hace, se debe atener a la penalidad correspondiente (ya sea cobro de una comisión,
o reducción de la tasa).
Si el cliente requiere de disponer del dinero, puede vender el CDT a otra persona, endosándolo,
ya que su naturaleza de título valor permite realizarlo sin inconvenientes.

Existen dos tipos de CDT:

- CDT a tasa fija: ofrecen una tasa fija durante el periodo que dura el CDT. Generalmente aplica
para los de poca duración.

- CDT a tasa variable: ofrecen ganancias extras y aplica generalmente para los CDT de 360
días o más de duración.

En Colombia los tipos de depósitos a plazo (certificados de depósitos) permitidos son:

- CDAT – Certificado de Depósito de Ahorro a Término

Este tipo de producto bancario, está orientado a inversiones a muy corto plazo y respetando una
tasa fija en pesos. Si bien, en el momento de la adquisición se le entregará un certificado por el
depósito realizado, este no es negociable en contraposición a un CDT.

Por otro lado, no pueden ser endosables ni estar a nombres de terceros, solo tendrá un titular y
si la documentación que acredita el CDAT está en manos de otra persona que no sea el titular, no
tiene valor.

- CDT – Certificado de Depósito a Término

La operatoria normal de los CDT lleva a constituir el depósito por un plazo o término de tiempo
determinado que debe ser como mínimo de 30 días.

El CDT es redimible o rembolsable sólo en los plazos y términos pactados. En este sentido,
si el CDT se pactó a 360 días el banco no lo pagará ni podrá ser
obligado a pagarlo hasta tanto se venza dicho término.

Un certificado puede ser materializado o desmaterializado.

- CDT Desmaterializado

Este registro le otorga los mismos derechos que se le adjudican en un CDT expedido físicamente,
pero tiene todos los atributos incorporados desde la tecnología: seguridad frente a los eventos de

robo, fraude, pérdida o deterioro, agilidad en la emisión y facilidad para su negociación y
redención.

El solicitante de un CDT Desmaterializado recibe una constancia de depósito (documento
expedido por DECEVAL) que no es negociable pero reconoce su titularidad sobre el valor y su
custodia desmaterializada.

Esta emisión queda registrada en DECEVAL (Depósito Centralizado de Valores de Colombia), en
la cuenta del depositante directo y en la subcuenta del titular.

Con la emisión desmaterializada, puede convertirse en el depositante directo de su cliente ante
DECEVAL.

- CDT Materializado

Un CDT es un título valor (representa dinero) de contenido crediticio, hecho a nombre de una
persona natural o jurídica, que produce un rendimiento (intereses) y se pacta a un plazo
determinado.

DECEVAL(Depósito Centralizado de Valores de Colombia) identifica los títulos que fueron emitidos
con las mismas condiciones faciales (fecha emisión, fecha de vencimiento, tasa, spread) el cual
se denomina código ISIN (Número de identificación internacional de valores sigla tomada de:
International Securities Identification Number). Código que identifica en forma única un título valor
específico u otro instrumento financiero. (Anexo 1 Código ISIN)

DECEVAL S.A. mediante la Resolución No. 01832 del 17 de octubre de 2006 fue designada como
la agencia numeradora nacional en Colombia con el objetivo de entregar a los miembros y a la
industria de valores como un todo un número de identificación internacional para valores (ISIN)
en una estructura uniforme para ser utilizado en cualquier sistema de negociación y de
administración de valores en la industria de valores internacional.

## 1.0 Generalidades y manejos de los Tipos de Operación

## 1.1 Tipos de Operación

En Bantotal se identifica con el módulo 22, los tipos de operación de los Certificados de Depósitos
a Término.

En el sistema se encuentran definidos los siguientes productos (Módulos/Tipos de operación):

Fig.1 Información de Gestión (programa Hfst004)

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

## 1.3 Administración de los certificados físicos

Bantotal permite realizar la administración de los certificados físicos dentro del sistema.
Para ello previamente se define el documento a utilizar en el sistema, esto se realiza mediante la
configuración del mismo. De esta forma se ha definido el tipo de documento 100 asociado al
módulo 52 de la siguiente forma.

Fig.2 Tipos de Documento (programa Hsch001)

A este tipo de documento se le asocian los distintos estados que puede tomar la solicitud, los
mismos son parametrizables lo que permite agregar o quitar pasos a la solicitud. Los pasos
definidos en el sistema son los siguientes:

- Solicitada

- Enviada al Proveedor

- Recibida del Proveedor

- Solicitud Anulada

## 1.4 Menú

Se accede al siguiente menú operativo:

En caso de ingreso de operaciones, se accede al siguiente punto de menú:

## 2.0 Solicitud de los certificados

## 2.1 Ingreso de la solicitud de Certificados

La solicitud de los certificados se realiza por medio del panel de “Solicitudes de Chequeras
(Stock)”. El usuario deberá ingresar al panel y digitar el módulo de certificados:

Fig.3 Solicitudes de Chequeras (Stock) (programa Hsch501)

Luego se selecciona el tipo de documento para el que desea generar la solicitud, en este caso el
tipo de documento para los certificados es el 100:

Luego se presiona el botón ‘Agregar’:

Se ingresa la cantidad de certificados que se desean solicitar del proveedor, por defecto se
muesta 99999:

Se ingresan por ejemplo 100 y se oprime el botón ‘Confirmar’:

Se visualiza la solicitud de certificados dada de alta:

Mediante el botón ‘Detalle’ se puede visualizar la cantidad de certificados solicitados para la
solicitud seleccionada:

Se visualiza el detalle de la solicitud:

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

## 3.1 Formato de Certificados

El formato está compuesto por un cabezal y el detalle de los certificados que debe generar el
proveedor, el formato se configura mediante este panel:

Fig.6 Trabajar con Aplicaciones (programa HZ999003)

### 3.1.1 Archivos

Al seleccionar este botón (Fig.6), se visualiza el tipo de archivo correspondiente a la aplicación
seleccionada en el panel anterior.

Fig.7 Trabajar con Archivos (programa HZ999004)

### 3.1.1.1 Bandejas

Al pulsar esta opción, se visualiza el siguiente panel donde se encuentra definido un cabezal y un
detalle:

Se selecciona (por ejemplo) el cabezal, y al pulsar el botón registro se visualiza la definición del
mismo:

Si se selecciona el Detalle, se visualiza el siguiente panel:

Se aclaró que este es el formato estándar y en caso de requerirse un formato distinto se debe
levantar el requerimiento de interfases.

## 3.2 Archivos enviados y recibidos

El archivo generado en este caso es el siguiente:

Luego el proveedor envía los certificados en general acompañados con un archivo que contiene
el detalle de los fisicos enviados para procesar en el sitema.

Lectura del Archivo recibido por elproveedor.

El archivo se guarda en un repositorio específico, desde el cual los programas correspondientes
lo toman y lo procesan; el procesamiento se realiza mediante el mismo panel utilizado para la
generación. En este caso se oprime el botón ‘Leer Archivo’:

Se procesaron los certificados de la solicitud.

Una vez recibidos los certificados, la solicitud no se visualiza más:

El archivo utilizado en este caso es el siguiente:

## 4.0 Activación de los Certificados

Luego de procesado el archivo, los certificados se generan en el sistema, pero pendientes de
activar. Para poder asociar los certificados a los CDTs es necesario activarlos.

La activación se realiza por medio del panel de Activación, donde se puede activar un rango de
CDTs, ingresando el mismo y presionando el botón ‘Activar’:

Fig.8 Activación de Certificados (programa HCDT0032)

Se indica el número desde y hasta, y luego se pulsa el botón ‘Activar’:

A partir de este momento los Certificados pueden asociarse alos CDTs.

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

## 5.1 CDT al Vencimiento Materializado

Se ingresa al panel de ejecución, se selecciona la transacción 10 y se oprime el botón
‘Seleccionar’. Se ingresa el número de cuenta cliente y se oprime el botón ‘Continuar’:

Se ingresa el importe del CDT, en este caso 1.000.000 y se oprime el botón ‘Continuar’:

En este momento el usuario selecciona el tipo de CDT que desea dar de alta, materializado o
desmaterializado:

Se pulsa ‘Seleccionar’.

Se ingresa la fecha de vencimiento o el plazo, en este caso se ingresa el plazo:

Se visualiza la tasa cargada para la operación:

Se pueden visualizar los intereses de la operación:

Se ingresa la facultad para el CDT:

Se selecciona la forma de pago en este caso caja:

Se ingresa en el panel de instrucciones, en este caso se selecciona instrucción 6 de renovación
automática:

Se visualiza la instrucción:

Ser selecciona ‘Continuar’.

Se confirma la transacción:

Alta CDT Materializado. Se dio de alta un CDT materializado al vencimiento (transacción 22/10).

El CDT nace con un estado específico que permite identificar a qué CDT se le asocia el certificado
y a cuáles no. De esta forma, una vez que se genera el alta del CDT se le debe asociar el
certificado.

Ver punto 6.1.

## 5.2 Alta CDT Pago Periódico

Desde ingreso de Operaciones, se ejecuta la siguiente transacción:

A diferencia de la transacción 22/10, en el panel donde se indica el plazo, se indicará el
período:

## 5.3 CDT al Vencimiento Desmaterializado

Se ingresa al panel de ingreso, se selecciona la transacción 10 y se oprime el botón ‘Seleccionar’:

Se ingresa el número de cuenta cliente y se oprime el botón ‘Continuar’:

Se ingresa el importe del CDT, en este caso 2.000.000 y se oprime el botón ‘Continuar’:

En este momento el usuario selecciona el tipo de CDT que desea dar de alta, materializado o
desmaterializado:

Se debe ingresar la fecha de vencimiento o el plazo, en este caso se ingresa fecha vencimiento:

Se visualiza la tasa cargada para la operación:

Se pueden visualizar los intereses de la operación:

Se ingresa la facultad para el CDT (el grabado automático de la facultad se verá en las próximas
sesiones):

Se selecciona la forma de pago en este caso Cuenta de Ahorro:

Se selecciona la Cuenta de Ahorro de donde se tomarán los fondos:

Se ingresa ene l panel de instrucciones, en este caso se selecciona instrucción 6 de renovación
automática:

Se visualiza la instrucción:

Se confirma la transacción:

En ese momento se contabiliza la operación.

Se puede visualizar la operación en la consulta de situación del cliente (Ver Manual de Sistema
de Contrapartes):

Seleccionando la operación y oprimiendo el botón ‘Detalle’, se puede visualizar el estado:

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

## 5.5 Renovaciones

Se ejecutan desde ingreso de operaciones.

Se selecciona una transacción y se pulsa ‘Seleccionar’:

En casos de prueba, se debe visualizar el vencimiento de una operación y modificar la fecha de
apertura a tal fecha que permita ingresar la renovación. De lo contrario se presenta el siguiente
error:

Accedemos a la Consulta de Situación de Cuentas, y validamos el vencimiento de una
operación:

Se modifica fecha de apertura:

Se selecciona una transacción de renovación desde Menú de Ingreso de Operaciones/Ingreso
CDT’s:

Se selecciona una operación con vencimiento correspondiente al día de la fecha de apertura y
vencimiento de la operación. Se pulsa ‘Seleccionar’.

Se digita plazo o vencimiento nuevo.

Se pulsa ‘Continuar’:

Se selecciona una forma de pago:

Se pulsa el botón Asiento para visualizar el movimiento contable:

Existen procesos Batch que ejecutan las renovaciones de forma automática al vencimiento de las
mismas, a pesar de esto, existe la posibilidad de ejecutar de forma manual la renovación en caso
que el cliente se presente en la sucursal.
Es preferible que las renovaciones se realicen de forma automática pero es posible que el usuario
lo ejecute de forma manual.

## 5.6 Unificación

La unificación de CDT es la unión de dos o más operaciones en una, es decir que se toman dos o
más CDTs para generar un único CDT. La unificación se puede realizar tanto para los CDTs
materializados como para los desmaterializados.

El sistema controla que los CDTs a unificar posean mismo plazo, tasa y fecha de vencimiento. En
caso de que las operaciones no cumplan estas condiciones no se podrán unificar.

Al realizar la unificación de CDTs materializados se cancelan las operaciones que se están
unificando y se emite un nuevo certificado con un nuevo nº de operación. Esta nueva operación
posee la misma fecha de vencimiento y tasa de los CDTs unificados, y el monto del capital es la
suma del valor de cada uno de los mismos.

Unificación de CDTs desmaterializados: previo a la realización de la unificación en el sistema el
Banco debe ingresar en la página de DECEVAL y realizar la unificación. De esta forma DECEVAL
emite un nuevo nº de ISIN que deberá ser asociado a la nueva operación unificada. Al igual que

en la unificación de los CDTs materializados se cancelan las operaciones que se están unificando
y se genera una nueva operación, con misma fecha de vencimiento y tasa de los CDTs unificados,
y monto de capital igual a la suma del valor del capital de cada uno de los CDTs unificados.

Esta transacción se ejecuta desde el siguiente punto de menú:

Al seleccionar la cuenta se pulsa el botón ‘Agregar’:

Luego de Filtrar por cuenta o cuenta operación, se seleccionan las operaciones a unificar con el
check y posteriormente se pulsa ‘Seleccionar’.
En caso de intereses por pagar para las operaciones seleccionadas, se emite este mensaje:

A modo de realizar el pago de los intereses, se ejecuta el programa PDP00004 (Punto 8.3).

Posteriormente

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

## 6.0 Asignación de Certificados

Mediante el panel de asignación de certificados se asocia el certificado con el CDT, si el usuario
se encuentra en casa central muestra todas las operaciones si no se encuentra en casa central
se muestran sólo CDT de la sucursal.

## 6.1 CDT Materializado

Fig.9 Asignación Certificado CDT (programa HCDT0033)

En la pantalla se selecciona la operación y el certificado a asociarle. Una vez asociado el
certificado el CDT pasa del estado “CDT Materializados No Asig.” al estado “Normal”. El certificado
físico también pasa de estado “activado” a “entregado”.

Se selecciona en este caso (si la operación corresponde a un CDT materializado) el filtro de
certificados “Materializados”, se selecciona la operación y se presiona el botón ‘Seleccionar’:

Se pulsa el botón Seleccionar.

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

## 8.0 SIMULADOR

Mediante este punto de menú, se accede al simulador:

Si es cliente se ingresa el número de cuenta.
Si no es cliente se permite ingresar un nombre para mostrar en el impreso. También se deberá
indicar si la persona está gravada o no por impuesto.

Se ingresa un plazo o fecha de vencimiento y el capital del CDT.

La tasa se puede ingresar manualmente o se puede obtener la tasa haciendo clic en el botón
correspondiente (en el caso que se seleccione algún ajuste de vencimiento actualizará también
el plazo).

Al hacer clic en el botón ‘Calcular’ se muestra el resultado.

En el caso que sea un DPF con pagos periódicos se listan los períodos.

Al hacer clic en el botón ‘Impreso’ se muestra el siguiente reporte:

## 9.0 Procesos Batch

Estos procesos se ejecutan en la cadena de cierre, con la periodicidad que se determine, y
contribuyen al cierre del circuito de CDT:

- PNU00002: Devengado de operaciones a Plazo

- PDP00004: Pago de Intereses Periódicos

- PDP00001: Renovación Automática

## 9.1 Devengado a Plazo (PNU00002)

Este proceso realiza el Devengado de intereses de las operaciones a plazo.

El funcionamiento es el siguiente: recorre los saldos de los rubros de capital de CDT. Realiza el
cálculo de interés hasta la fecha de proceso y asienta la diferencia entre el total de intereses y el
total ya contabilizado, tomando la tasa y el plazo de la operación y considerando si hubo cambios
en la tasa de la operación.

La contabilización de los movimientos es en el módulo 99, transacción 900.

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

## 9.3 Pago Periódico de Intereses de CDTs (PDP00004)

Este proceso realiza el pago periódico de aquellos depósitos que tengan dicha condición.

El funcionamiento es el siguiente: para aquellos depósitos, con instrucciones 7 y 8, recorre los
días de revisión y si corresponde se procede a la acreditación de los intereses. Para los depósitos
con instrucción 7(acreditación periódica de intereses) se acredita según lo indicado en la apertura
del mismo.

Para aquellos depósitos con instrucción 8 (capitalización de intereses) los intereses se
capitalizan.

La contabilización de los movimientos es en el módulo 99, transacción 920.
