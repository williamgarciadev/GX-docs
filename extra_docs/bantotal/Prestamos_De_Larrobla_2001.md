# Préstamos en Bantotal

> Fuente: presentación de capacitación "PRESTAMOS", De Larrobla & Asociados —
> Capacitación, Montevideo, 3 de mayo de 2001.

## Qué es un préstamo?

- Dinero que el banco entrega a un cliente el cual deberá ser devuelto y al
  cual se le cobra intereses.

## Cómo se define el préstamo? — Conceptos base

Un préstamo se define en base a los siguientes conceptos:

- **Capital**: Es el importe de dinero que recibe el cliente, puede ser en
  cualquier moneda.
- **Plazo**: Es la cantidad de tiempo transcurrido hasta la devolución total
  del capital.
- **Fecha valor**: Es la fecha en la que se otorga el préstamo.
- **Fecha de vencimiento**: Es la fecha en la que vence el total del
  préstamo = fecha valor + plazo.
- **Periodo**: Es la cantidad de días entre las cuotas de un préstamo.

## Cómo se define el préstamo? (continuación) — Tasa y tipo de tasa

- **Tasa y tipo de tasa**: Porcentaje del capital que el banco cobrará por
  entregar el dinero.
  - La tasa se define en función del plazo y la moneda.
  - Ej: Tasa de un 15% anual para dólares. Tasa de un 40% anual para pesos.
    Tasa de un 1% mensual para dólares. Tasa de un 4% mensual para pesos.

Existen dos "tipos" de tasa:

- **Nominal (lineal)**: Se asume un capital constante para el periodo.
- **Efectiva**: Se asume que los intereses se suman al capital diariamente.

## Cómo se define el préstamo? (continuación) — Plan de pagos

**Plan de pagos**: Es el cronograma y composición de cada pago.

Existen cuatro formas de realizar el cronograma:

- **Plazo fijo**: Se define un solo pago de capital e intereses.
- **Francés**: Se definen n cuotas pero el cliente siempre paga el mismo
  importe.
- **Alemán**: Se definen n cuotas pero el cliente siempre paga el mismo
  capital.
- **Plan de pagos**: Se definen libremente los pagos de capital e intereses.

## Cómo se define el préstamo? (continuación) — Tasa de mora, tipo de año, tipo de día

- **Tasa de mora**: Porcentaje que el banco cobrará si el cliente incumple
  en sus pagos previstos.
- **Tipo de año**: Define si el año se considera de 360 días (comercial) o
  de 365 días (calendario).
- **Tipo de día**: Define si para armar el calendario de pagos se utilizan
  meses de 30 días o según el calendario.

## Bantotal: conceptos básicos sobre préstamos

- **Módulo**: "Agrupación de rubros que representan lo mismo (Ej. préstamos,
  cuentas corrientes, etc)".
- **Sistema**: "Agrupación de módulos que representan lo mismo (Ej.
  préstamos, cuentas corrientes, etc)".
- **Intereses**: Dinero que el banco recibe como compensación por la
  entrega del capital.

## Fórmula para cálculo de intereses

El interés se calcula en función de la tasa, el capital, el plazo y el tipo
de año.

```
Capital(C) = 10000
Plazo (P) = 360 días

Si tasa 15% lineal anual (T)
  Año comercial:
      Interés = C*T*P/36000 = 10000*15*360/36000 = 1500
  Año calendario:
      Interés = C*T*P/36000 = 10000*15*360/36500 = 1479.45

Si tasa 15% efectiva anual (T)
  Año comercial:
      Interés = C*(1+(T/100))^(360/360)-1 = 1500
  Año calendario:
      Interés = C*(1+(T/100))^(360/365)-1 = 1478
```

## Ejemplos de préstamos

Parámetros del ejemplo:

- Capital = 10000
- Tasa = 15% lineal anual
- Tipo de año = Comercial
- Tipo de día = Comercial
- Fecha valor = 01/01/2000
- Plazo = 90 días
- Periodo = 30 días

**Préstamo plazo fijo:**

| Fecha de pago | Capital | Interés | Saldo capital | Cuota |
|---|---|---|---|---|
| 01/04/2000 | 10000 | 375 | 0 | 10375 |

**Préstamo Alemán:**

| Fecha de pago | Capital | Interés | Saldo capital | Cuota |
|---|---|---|---|---|
| 01/02/2000 | 3333.33 | 125 | 6666.67 | 3458.35 |
| 01/03/2000 | 3333.33 | 83.33 | 3333.34 | 3416.68 |
| 01/04/2000 | 3333.34 | 41.66 | 3333.34 | 3375.01 |

**Préstamo Francés:**

| Fecha de pago | Capital | Interés | Saldo capital | Cuota |
|---|---|---|---|---|
| 01/02/2000 | 3292 | 125 | 6708 | 3417 |
| 01/03/2000 | 3333.15 | 83.85 | 3374.85 | 3417 |
| 01/04/2000 | 3374.85 | 42.19 | 3333.34 | 3117.04 |

## Tablas utilizadas por préstamos — Fst024: Tipos de tasas

```
*Tzttas    N(1)     Tipo tasa
 Tznom     C(20)    Nombre
 TzEfLi    C(1)     Tipo: 1=Efectiva 2=Lineal
 TzAnMe    C(1)     Tipo: 1=Mensual 2=Anual
```

En esta tabla se definen los tipos de tasas que se pueden utilizar.

## Tablas utilizadas por préstamos — Fst003: Módulos

```
*Modulo   N(3)    Modulo
 Mdnom    C(30)   Nombre de modulo
 Mdncor   N(9)    Nro.correlativo-Oper/Ext/Event
 Mdciva   C(1)    Cobra IVA en el Pago?
 Mdfunc   N(2)    Función
 Mdaltf   C(1)    Altera Función?
 Mdptrn   C(1)    Participa en transaccional?
 Mdnume   N(9)    Numerador de Operac.
 Mdbcu    C(1)    Cod.BCU?
 Mdfval   C(1)    F/valor?
 Mdfvto   C(1)    F/Vto.
 Mdtasa   C(1)    Tasa?
 Mdmora   C(1)    Mora?
 Mdprdt   C(1)    Préstamo/Descuento
 Mdmnca   C(1)    Pzo.s/calendario?
 Mdmeca   C(1)    Pzo.calendario M/E?
 Mdanio   N(3)    Días del ano:
 Mdclas   C(1)    Cod.Clasif.?
 Mdprgo   C(1)    País de Riesgo?
```

En esta tabla se definen los módulos de bantotal.

## Tablas utilizadas por préstamos — FST110 y Fst111: Sistemas y relación sistema/módulo

**FST110 : SISTEMAS**

```
*Dscod      N(3)    Código de sistema
 Dsnom      C(30)   Nombre de sistema
```

En esta tabla se define el sistema de préstamos, el código del sistema de
préstamos es el 50.

**Fst111 : Relación sistema / módulo**

```
*Dscod      N(3)    Código de sistema
*Modulo     N(3)    Modulo
```

En esta tabla se definen los módulos que integran el sistema.

## Tablas utilizadas por préstamos — FST004: Tipos de operación por módulo

```
*Modulo     N(3)     Modulo
*Totope     N(3)     Tipo Oper.
 Totpiz     N(2)     Tipo de Pizarra relacionada
 Tonom      C(30)    Nombre T.operac.
 Toperi     N(2)     Periodo de acredit.de interés
 Tosn1      C(1)     Analiza Historia?
 Tosn2      C(1)     Uso de Pizarra
 Tosn3      C(1)     Tosn3
 Tosn4      C(1)     Tosn4
 Tosn5      C(1)     Tosn5
 Tocd1      N(3)     Tocd1
 Tocd2      N(3)     Tocd2
 Tocd3      N(3)     Tocd3
 Tocd4      N(3)     Tocd4
 Tocd5      N(3)     Tocd5
 Toeleg     C(1)     ¿Elegible por el operador?
```

En esta tabla se definen los tipos de operación que soporta este módulo.
Por ejemplo, préstamo francés, préstamo alemán, etc.

Datos importantes en esta tabla: atributo **TOCD5**, indica el tipo de
préstamo que se utiliza con este tipo de operación:

- `0` = Plazo fijo
- `1` = Francés
- `2` = Alemán
- `3` = Plan de pagos

## Tablas utilizadas por préstamos — Fsd010: Operaciones

Solo atributos que se usan en préstamos:

```
*Pgcod     N(3)      Cod.
*Aomod     N(3)      Modulo
*Aosuc     N(3)      Sucursal
*Aomda     N(4)      Moneda
*Aopap     N(4)      Aopap
*Aocta     N(9)      Cuenta
*Aooper    N(9)      Operación
*Aosbop    N(3)      Sub-operac.
*Aotope    N(3)      Tipo operac.
 Aofval    D(8)      F/valor
 Aofvto    D(8)      F/vto
 Aopzo     N(5)      Plazo
 Aottas    N(1)      Tipo de Tasa
 Aotasa    N(11.6)   Tasa
 Aotmor    N(11.6)   Tasa Mora
 Aotdia    N(1)      Tipo de días
 Aotano    N(1)      Tipo de ano
 Aodrev    N(5)      Días p/revisión de Tasa
 Aoimp     N(15.2)   Importe
 Aotvto    C(1)      Tipo de ajuste en vencto.
 Aoperiod  N(5)      Período (Itper)
```

En esta tabla se almacenan los siguientes datos: capital original (aoimp),
tasa y tipo de tasa (aottas, aotasa), tasa de mora (aotmor), tipo de año
(aotano), tipo de día (aotdia), periodo entre cuotas (aoperiod).

## Tablas utilizadas por préstamos — Fsd012: Cambios de tasa

Solo datos importantes:

```
*Pgcod      N(3)      Cod.
*Aomod      N(3)      Modulo
*Aosuc      N(3)      Sucursal
*Aomda      N(4)      Moneda
*Aopap      N(4)      Aopap
*Aocta      N(9)      Cuenta
*Aooper     N(9)      Operación
*Aosbop     N(3)      Sub-operac.
*Aotope     N(3)      Tipo operac.
*Evcorr     N(9)      Correlativo evento
 Evfval     D(8)      Fecha valor
 Evtasa     N(11.6)   Tasa
 Evcd01     N(2)      Evcd01
 D012co     C(1)      ¿Contabilizado?
 D012cd     N(3)      pgcod
 D012mo     N(3)      hcmod
 D012su     N(3)      hsucor
 D012tr     N(3)      htran
 D012re     N(4)      hnrel
 D012fc     D(8)      hfcon
 D012or     N(2)      hcord
 D012sb     N(3)      hcsubo
 Evtipo     N(2)      Evtipo
 Evttas     N(1)      Tipo de tasa
```

Las tasas de una operación pueden ser cambiadas, en ese caso los cambios de
tasa se almacenan en esta tabla.

- `Evtipo = 3` => Cambio de tasa de la operación
- `Evtipo = 4` => Cambio de tasa de mora

## Tablas utilizadas por préstamos — Fsd601: Calendario de pagos

```
*Pgcod      N(3)       Cod.
*Ppmod      N(3)       Ppmod
*Ppsuc      N(3)       Ppsuc
*Ppmda      N(4)       Ppmda
*Pppap      N(4)       Pppap
*Ppcta      N(9)       Ppcta
*Ppoper     N(9)       Operación
*Ppsbop     N(3)       Suboperación
*Pptope     N(3)       Tipo de operación
*Ppfpag     D(8)       Fecha de pago prevista
*Pptipo     C(1)       Tipo de cuota
 Ppfval     D(8)       Desde fecha
 Ppfvto     D(8)       Hasta fecha
 Pppzo      N(5)       Plazo de la cuota
 Ppcap      N(15.2)-   Capital de la cuota
 Ppint      N(15.2)-   Interés de la cuota
 Ppicap     N(15.2)-   Impuesto sobre capital
 Ppiint     N(15.2)-   Impuesto sobre interés
 Ppstat     C(1)       Estado de la cuota
 Ppnume     N(9)       Numerador de pagos a la cuota
 Ppfinv     N(8)       Fecha de pago inversa
 D601cd     N(3)       D601cd
 D601mo     N(3)       D601mo
 D601su     N(3)       D601su
 D601tr     N(3)       D601tr
 D601re     N(4)       D601re
 D601fc     D(8)       D601fc
 D601or     N(2)       D601or
 D601sb     N(3)       D601sb
 D601co     C(1)       D601co
 PpintMex   N(15.2)-   Interés p/impuesto Mex.
```

En la tabla fsd601 se almacena el cronograma de pagos previsto para el
préstamo, algunos datos importantes en esta tabla:

- **Ppfval**: Fecha valor de la cuota, es la fecha desde la que se calculan
  intereses para la cuota.
- **Ppfvto**: Fecha vencimiento de la cuota, es la fecha hasta la que se
  calculan intereses para la cuota.
- **Ppfpag**: Fecha en la que debe ser pagada la cuota.
- **Ppcap**: Capital que deberá ser pagado en esta cuota.
- **PPNUme**: Numerador de pagos de la cuota.
- **d601co**: Si está confirmado el registro; solo los registros con
  d601co en "S" son tomados en cuenta por bantotal.

## Tablas utilizadas por préstamos — Fsd602: Pagos realizados al préstamo

```
*Pgcod      N(3)       Cod.
*Ppmod      N(3)       Ppmod
*Ppsuc      N(3)       Ppsuc
*Ppmda      N(4)       Ppmda
*Pppap      N(4)       Pppap
*Ppcta      N(9)       Ppcta
*Ppoper     N(9)       Operación
*Ppsbop     N(3)       Suboperación
*Pptope     N(3)       Tipo de operación
*Ppfpag     D(8)       Fecha de pago prevista
*Pptipo     C(1)       Tipo de cuota
*Pp1nump    N(9)       Número de pago a la cuota
 Pp1fech    D(8)       Fecha de pago
 Pp1cap     N(15.2)-   Cuotaparte de pago a capital
 Pp1int     N(15.2)-   Cuotaparte de pago a interés
 Pp1intm    N(15.2)-   Cuotaparte de pago a int.mora
 Pp1icap    N(15.2)-   Cuotparte a impuesto de capit.
 Pp1iint    N(15.2)-   Cuotaparte a impuesto de int.
 Pp1iintm   N(15.2)-   Cuotaparte a impu. de int.mora
 Pp1salcap  N(15.2)-   Saldo de capital de cuota
 Pp1salint  N(15.2)-   Saldo de interés de cuota
 Pp1salmor  N(15.2)-   Saldo de int. de mora de cuota
 D602cd     N(3)       D602cd
 D602mo     N(3)       D602mo
 D602su     N(3)       D602su
 D602tr     N(3)       D602tr
 D602re     N(4)       D602re
 D602fc     D(8)       D602fc
 D602or     N(2)       D602or
 D602sb     N(3)       D602sb
 D602co     C(1)       D602co
 Pp1stat    C(1)       Estado de la cuota
```

En la tabla fsd602 se almacenan los pagos que se realizaron al préstamo.
Datos importantes:

- **PP1fech**: Fecha en que se pagó.
- **Pp1cap**: Cuánto pagó de capital.
- **Pp1int**: Cuánto pagó de interés.
- **Ppp1mor**: Cuánto pagó de interés de mora.
- **PP1salcap**: Cuánto capital resta pagar en esta cuota.
- **Pp1salint**: Cuánto falta pagar de interés en esta cuota.
- **PP1salmor**: Cuánto falta pagar de interés de mora en esta cuota.
- **D602co**: Solo los registros con d602co en "S" son tomados en cuenta
  por bantotal.

## Rutinas utilizadas en préstamos — RRg0003

```
RRg0003(&Ppgcod, &Psucurs, &Fval, &Fvto, &Plazo, &Tplzo, &Tvto)
```

Esta rutina se utiliza para obtener la fecha de vto dada la fecha valor y
el plazo, o el plazo dada la fecha valor y la fecha de vencimiento.

Parámetros que recibe:

- **&Ppgcod**: empresa en la que se trabaja.
- **&Psucurs**: Sucursal en la que está el préstamo.
- **&fval**: fecha inicial.
- **&fvto**: fecha final (si se envía en blanco, la devuelve, sino
  devuelve el plazo).
- **&plazo**: cantidad de días.
- **&tplzo**: tipo de año (1 = comercial, 2 = calendario).
- **&Tvto**:
  - `'P'` si la fecha final calculada es un día feriado, ajusta al
    siguiente hábil.
  - `'A'` si la fecha final calculada es un día feriado, ajusta al hábil
    anterior.
  - `'N'` si la fecha final calculada es un día feriado, no realiza
    ajuste.

Parámetros que devuelve: `&fvto`, `&plazo`.

## Rutinas utilizadas en préstamos — RRg0004

```
RRg0004(&Ttas, &Tasa, &Tano, &Plazo, &Tint, &Coef)
```

Esta rutina se utiliza para calcular intereses.

Parámetros que recibe:

- **&ttas**: Tipo de tasa.
- **&tasa**: Tasa.
- **&tano**: Tipo de año (1 = comercial, 2 = calendario).
- **&plazo**: cantidad de días.
- **&tint**: Enviar "C".

Parámetros que devuelve: `&coef`.
