---
title: "Date data type"
source_id: 7373
source_url: https://wiki.genexus.com/commwiki/wiki?7373
genexus_version: "18"
---

# Date data type

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

The Date data type has two [static method](https://wiki.genexus.com/commwiki/wiki?39593) available only for the .NET, .NET Framework and Java generators.

#### [New](#New)

Generates Date instances with specific values for the date.

##### [Syntax](#Syntax)

Date.New(Year,Month,Day)

##### [Samples](#Samples)

```
&ExpirationDate = Date.New(2018,6,10)
```

```
If &ExpirationDate >= Date.New(2022,1,4)
   msg("The date has expired")
EndIf
```

#### Today

Gets the current system date.

##### [Syntax](#Syntax)

Date.Today()

##### [Samples](#Samples)

```
&date = Date.Today(); 
&dateString = &date.ToString()
msg(&dateString) // 09/12/23
```

### [Consideration](#Consideration)

When generating iOS code, controls based on the Date / DateTime data type, use the [Date format property](https://wiki.genexus.com/commwiki/wiki?39441) and [Hour format property](https://wiki.genexus.com/commwiki/wiki?39440) to infer the native styles [dateStyle](https://developer.apple.com/documentation/foundation/dateformatter/1415411-datestyle) and [timeStyle](https://developer.apple.com/documentation/foundation/dateformatter/1413467-timestyle) which take into account the user's preferences in the device settings.

### [See also](#See+also)

[DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370)  
[Data types list](https://wiki.genexus.com/commwiki/wiki?6779)


|  |
| --- |
| **Backlinks** |
| [AddDays method](https://wiki.genexus.com/commwiki/wiki?8313) | [AddMonths method](https://wiki.genexus.com/commwiki/wiki?12674) | [AddYears method](https://wiki.genexus.com/commwiki/wiki?12673) |
| [Age method](https://wiki.genexus.com/commwiki/wiki?12687) | [Attribute-date class for Design System objects](https://wiki.genexus.com/commwiki/wiki?52976) | [Calendar external object](https://wiki.genexus.com/commwiki/wiki?39346) |
| [Data Type Filter property](https://wiki.genexus.com/commwiki/wiki?40654) | [Data Type property](https://wiki.genexus.com/commwiki/wiki?7232) | [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) | [Date data type (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55760) |
| [Date data type definition property](https://wiki.genexus.com/commwiki/wiki?53796) | [DatePicker property](https://wiki.genexus.com/commwiki/wiki?8998) | [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) | [DateTime picker for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?34167) |
| [Day method](https://wiki.genexus.com/commwiki/wiki?12646) | [DayOfWeek method](https://wiki.genexus.com/commwiki/wiki?12657) | [Dimensions property](https://wiki.genexus.com/commwiki/wiki?7380) | [EndOfMonth method](https://wiki.genexus.com/commwiki/wiki?12656) |
| [FromString method](https://wiki.genexus.com/commwiki/wiki?12694) | [HowTo: Use the Data Source From property](https://wiki.genexus.com/commwiki/wiki?22948) | [IsEmpty method](https://wiki.genexus.com/commwiki/wiki?9645) | [Month method](https://wiki.genexus.com/commwiki/wiki?12647) |
| [Category:Panel object](https://wiki.genexus.com/commwiki/wiki?24829) | [RemoteConfig external object](https://wiki.genexus.com/commwiki/wiki?48160) | [Rows property - Vector and Matrix](https://wiki.genexus.com/commwiki/wiki?7772) | [Server Side Functions/Methods](https://wiki.genexus.com/commwiki/wiki?11572) |
| [Set method](https://wiki.genexus.com/commwiki/wiki?6810) | [SetEmpty method](https://wiki.genexus.com/commwiki/wiki?9646) | [TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019) | [ToFormattedString method](https://wiki.genexus.com/commwiki/wiki?12722) |
| [ToString method](https://wiki.genexus.com/commwiki/wiki?7090) | [WorkflowUser Data Type](https://wiki.genexus.com/commwiki/wiki?17273) | [Year function](https://wiki.genexus.com/commwiki/wiki?8380) | [Year method](https://wiki.genexus.com/commwiki/wiki?12648) |

---
