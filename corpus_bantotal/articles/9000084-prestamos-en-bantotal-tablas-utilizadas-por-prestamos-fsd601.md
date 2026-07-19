---
title: "Préstamos en Bantotal — Tablas utilizadas por préstamos — Fsd601: Calendario de pagos"
source_id: 9000084
source_url: "local:extra_docs/bantotal/Prestamos_De_Larrobla_2001.md"
ingested_by: ingest_docs.py
---

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
