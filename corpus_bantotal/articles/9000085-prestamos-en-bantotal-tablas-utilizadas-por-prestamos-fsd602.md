---
title: "Préstamos en Bantotal — Tablas utilizadas por préstamos — Fsd602: Pagos realizados al préstamo"
source_id: 9000085
source_url: "local:extra_docs/bantotal/Prestamos_De_Larrobla_2001.md"
ingested_by: ingest_docs.py
---

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
