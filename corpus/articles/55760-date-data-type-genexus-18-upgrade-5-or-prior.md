---
title: "Date data type (GeneXus 18 Upgrade 5 or prior)"
source_id: 55760
source_url: https://wiki.genexus.com/commwiki/wiki?55760
genexus_version: "18"
---

# Date data type (GeneXus 18 Upgrade 5 or prior)

Stores **Date** values.

### [Scope](#Scope)

**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Conversion by DBMS](#Conversion+by+DBMS)

The following table illustrates the conversion GeneXus performs according to the DBMS:

|  |  |
| --- | --- |
| DBMS | Conversion |
| Oracle | DATE |
| DB2 Universal Database | DATE |
| Informix | DATE |
| SQL Server | DATETIME |
| Access | DBDate |
| DB2 for iSeries | CHAR(8) or DATE1 |
| DBF | DATE(8,0) |
| PostgreSQL | DATE |

1 Depends on the value set for the [Date data type definition property](https://wiki.genexus.com/commwiki/wiki?53796).

### [Pictures](#Pictures)

Read about [Pictures that can be applied to Date data types](https://wiki.genexus.com/commwiki/wiki?6800).

### Static methods

```
Date.New(Year,Month,Day)
```

#### [Samples](#Samples)

```
&ExpirationDate = Date.New(2018,6,10)
```

```
If &ExpirationDate >= Date.New(2022,1,4)
   msg("The date has expired")
EndIf
```

### [Consideration](#Consideration)

When generating iOS code, controls based on the Date / DateTime data type, use the [Date format property](https://wiki.genexus.com/commwiki/wiki?39441) and [Hour format property](https://wiki.genexus.com/commwiki/wiki?39440) to infer the native styles [dateStyle](https://developer.apple.com/documentation/foundation/dateformatter/1415411-datestyle) and [timeStyle](https://developer.apple.com/documentation/foundation/dateformatter/1413467-timestyle) which take into account the user's preferences in the device settings.

### [See also](#See+also)

[DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370)  
[Data types list](https://wiki.genexus.com/commwiki/wiki?6779)  
[What is a static method](https://wiki.genexus.com/commwiki/wiki?39593)
