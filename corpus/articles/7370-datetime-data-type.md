---
title: "DateTime data type"
source_id: 7370
source_url: https://wiki.genexus.com/commwiki/wiki?7370
genexus_version: "18"
---

# DateTime data type

Stores **date**, **time**, **seconds**, and **milliseconds** values.

### [Properties](#Properties)

The following table illustrates the properties used to define the Data Type:

|  |
| --- |
| [Value range property](https://wiki.genexus.com/commwiki/wiki?6797) |
| [Initial value property](https://wiki.genexus.com/commwiki/wiki?11765) |
| [Picture Properties Group](https://wiki.genexus.com/commwiki/wiki?6800) |
| [Precision property](https://wiki.genexus.com/commwiki/wiki?39306) |

### [Scope](#Scope)

**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Conversion by DBMS](#Conversion+by+DBMS)

The following table illustrates the conversion done by GeneXus according to the DBMS:

|  |  |  |
| --- | --- | --- |
| **DBMS** | **Native Type (Seconds Precision)** | **Native Type (Milliseconds Precision)** |
| Oracle | Date | TimeStamp |
| DB2 Universal Database | Timestamp | Timestamp |
| Informix | DateTime | DateTime(3) |
| SQL Server | DateTime | DateTime2 |
| DB2 UDB for iSeries | Timestamp | Timestamp |
| PostgreSQL | Timestamp | Timestamp |
| SAP Hana | SecondDate | TimeStamp |
| MySQL | DateTime | Datetime(3) |

### [Static methods](#Static+methods)

The DateTime data type has two [static methods](https://wiki.genexus.com/commwiki/wiki?39593) available only for the .NET, .NET Framework, and Java generators.

#### [New](#New)

Generates DateTime instances with specific values for date and time.

##### [Syntax](#Syntax)

DateTime.New(Year,Month,Day, [Hour],[Minute],[Second],[Millisecond])

##### [Samples](#Samples)

```
&ExpirationDateTime = DateTime.New(2018,6,5,18,0,0,0)
```

```
If &ExpirationDateTime >= DateTime.New(2018,6,5,18,0,0,0)
   msg("The date and time is not allowed")
EndIf
```

#### Now

Obtains the current system date and time.

##### [Syntax](#Syntax)

DateTime.Now()

##### [Samples](#Samples)

```
&datetime = Datetime.Now() 
&dateString = &datetime.ToString()
msg(&dateString) // 09/12/23 12:35 PM
```

### Equivalencies Between Date and DateTime

**Assignments**  
Assignments between Date and DateTime attributes are allowed according to the following rules:

```
Date = DateTime //The receiving field loses the value corresponding to the time.

DateTime = Date //The receiving field’s time value is 12:00:00 AM (00:00:00 in 24-hour format).
```

**Comparisons**  
Comparisons between Date and DateTime fields in conditions are not allowed. To compare these two data types, you must convert one into the other using assignments.

For example, if &DT is a DateTime variable and &D is a Date variable, you can use any of the following schemes to compare them.

```
Scheme 1: Create a temporary DateTime variable and compare

&DT1 = &D  //Converts &D to DateTime and its value remains in &DT1
           //The time part is 12:00.000 AM
if &DT > &DT1
   …
endif

Scheme 2: Create a temporary Date variable and compare

&D1 = &DT    //Converts &DT to Date and its value remains in &D1
             //The time part is lost
if &D > &D1
   …
endif
```

**Parameter Passing**  
Date and DateTime data types are not equivalent. Programs that expect a Date value cannot be called by programs passing a DateTime value and vice versa; otherwise, an error will occur at specification time.  
  
**Indexes and Search**  
It is possible to create indexes containing DateTime attributes as the only component or as part of the key. They can be ascending or descending (as long as the DBMS allows it).  
  
As far as the search is concerned, consider that it is not possible to search for those that 'have the same date' in a direct way. It will be necessary to implement, for example, the following code:

```
// Code to search for a DateTime attribute value within a given date.

&dtFrom = ymdhmstot(1995, 10, 28, 0, 0, 0)
&dtTo = ymdhmstot( 1995,10, 29, 0, 0, 0) – 1 // Next day minus 1 second
For each
    Where dtAttribute >= &dtFrom
    Where dtAttribute <= &dtTo
          …
EndFor
```

### [**Reorganization**](#Reorganization)

The following table discusses the possible data type changes of an attribute during the reorganization process.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Original Data type** | **Data type to which it is converted** | | | |
|  | Char1 | Numeric2 | Date | Datetime |
| Char1 | N/A | Yes4, if [val](https://wiki.genexus.com/commwiki/wiki?8528) is used. | Yes, if [CtoD function](https://wiki.genexus.com/commwiki/wiki?7472) is used. | Yes, if [CtoT function](https://wiki.genexus.com/commwiki/wiki?7473) is used. |
| Numeric2 | Yes, if [Str function](https://wiki.genexus.com/commwiki/wiki?7474) is used. | N/A | N/A | N/A |
| Date | Yes3, if [DtoC function](https://wiki.genexus.com/commwiki/wiki?7475) is used. | N/A | N/A | Yes, if time 12:00:00.00 AM is assumed. |
| DateTime | Yes3, if [TtoC function](https://wiki.genexus.com/commwiki/wiki?8361) is used with the default values. | No | Yes. The time part is lost. | N/A |

N/A. - Not applicable.  
Yes. - Conversion is allowed.  
No. - Conversion is not allowed. The values are lost.  
1 - [Character](https://wiki.genexus.com/commwiki/wiki?6777), [Varchar](https://wiki.genexus.com/commwiki/wiki?6778) and [Long Varchar](https://wiki.genexus.com/commwiki/wiki?7371) types.  
2 - Any numeric data type.  
3 - The receiving attribute may be truncated to the right if it is not large enough.  
4 - The attribute may be truncated to the left if it is not large enough.

#### [Notes](#Notes)

* Changes in the picture of the DateTime attribute **do not** imply database reorganization. This is because the way the attribute is stored is independent of how it is displayed.
* Changes in precision **may** imply a database reorganization.
* [Empty values](https://wiki.genexus.com/commwiki/wiki?19150) are invariable with respect to [Precision](https://wiki.genexus.com/commwiki/wiki?39306). Even though the [minimum value for a Datetime2 in SQL Server is 0001-01-01](https://docs.microsoft.com/en-us/sql/t-sql/data-types/datetime2-transact-sql?view=sql-server-2017), in GeneXus empty and minimum are the same as the one for Datetime: 1753-01-01.

### [Consideration](#Consideration)

When generating iOS code, controls based on the Date / DateTime data type use the [Date format property](https://wiki.genexus.com/commwiki/wiki?39441) and [Hour format property](https://wiki.genexus.com/commwiki/wiki?39440) to infer the native styles [dateStyle](https://developer.apple.com/documentation/foundation/dateformatter/1415411-datestyle) and [timeStyle](https://developer.apple.com/documentation/foundation/dateformatter/1413467-timestyle) that take into account the user's preferences in the device settings.

### [See Also](#See+Also)

[Date data type](https://wiki.genexus.com/commwiki/wiki?7373)  
[Data types list](https://wiki.genexus.com/commwiki/wiki?6779)


|  |
| --- |
| **Backlinks** |
| [AddDays method](https://wiki.genexus.com/commwiki/wiki?8313) | [AddHours method](https://wiki.genexus.com/commwiki/wiki?19209) | [AddMilliseconds method](https://wiki.genexus.com/commwiki/wiki?39524) |
| [AddMinutes method](https://wiki.genexus.com/commwiki/wiki?19205) | [AddMonths method](https://wiki.genexus.com/commwiki/wiki?12674) | [AddSeconds method](https://wiki.genexus.com/commwiki/wiki?12676) | [AddYears method](https://wiki.genexus.com/commwiki/wiki?12673) |
| [Age method](https://wiki.genexus.com/commwiki/wiki?12687) | [Attribute Empty Value for each DBMS and Data Type](https://wiki.genexus.com/commwiki/wiki?19150) | [Attribute-date class for Design System objects](https://wiki.genexus.com/commwiki/wiki?52976) |
| [Counting Type property](https://wiki.genexus.com/commwiki/wiki?42253) | [CurrentOffset method](https://wiki.genexus.com/commwiki/wiki?21917) | [Data Type Filter property](https://wiki.genexus.com/commwiki/wiki?40654) | [Data Type property](https://wiki.genexus.com/commwiki/wiki?7232) |
| [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) | [Date data type](https://wiki.genexus.com/commwiki/wiki?7373) | [Date data type (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55760) | [Date data type definition property](https://wiki.genexus.com/commwiki/wiki?53796) |
| [Date expression procedure property](https://wiki.genexus.com/commwiki/wiki?47342) | [DatePicker property](https://wiki.genexus.com/commwiki/wiki?8998) | [DateTime picker for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?34167) | [Day method](https://wiki.genexus.com/commwiki/wiki?12646) |
| [DayOfWeek method](https://wiki.genexus.com/commwiki/wiki?12657) | [Dictionary External Object](https://wiki.genexus.com/commwiki/wiki?58246) | [Difference method](https://wiki.genexus.com/commwiki/wiki?12677) | [Dimensions property](https://wiki.genexus.com/commwiki/wiki?7380) |
| [EndOfMonth method](https://wiki.genexus.com/commwiki/wiki?12656) | [Facebook external object](https://wiki.genexus.com/commwiki/wiki?38432) | [FromString method](https://wiki.genexus.com/commwiki/wiki?12694) |
| [Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274) | [Geolocation external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55149) | [GXScheduler User Control](https://wiki.genexus.com/commwiki/wiki?11583) | [Hour format property](https://wiki.genexus.com/commwiki/wiki?39440) |
| [IsEmpty method](https://wiki.genexus.com/commwiki/wiki?9645) | [JWT Utils](https://wiki.genexus.com/commwiki/wiki?43986) | [LocalNotifications external object](https://wiki.genexus.com/commwiki/wiki?39554) | [LocalNotifications external object (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54527) |
| [Maps external object](https://wiki.genexus.com/commwiki/wiki?44309) | [Maximum Seconds property](https://wiki.genexus.com/commwiki/wiki?42256) | [Maximum Text property](https://wiki.genexus.com/commwiki/wiki?42257) | [MilliSecond method](https://wiki.genexus.com/commwiki/wiki?39523) |
| [Minimum Seconds property](https://wiki.genexus.com/commwiki/wiki?42258) | [Minimum Text property](https://wiki.genexus.com/commwiki/wiki?42259) | [Month method](https://wiki.genexus.com/commwiki/wiki?12647) | [Precision property](https://wiki.genexus.com/commwiki/wiki?39306) |
| [Prefix Text property](https://wiki.genexus.com/commwiki/wiki?42254) | [Relative Timer control](https://wiki.genexus.com/commwiki/wiki?42490) | [RemoteConfig external object](https://wiki.genexus.com/commwiki/wiki?48160) | [Rows property - Vector and Matrix](https://wiki.genexus.com/commwiki/wiki?7772) |
| [Set method](https://wiki.genexus.com/commwiki/wiki?6810) | [SetEmpty method](https://wiki.genexus.com/commwiki/wiki?9646) | [SetTimeZone method](https://wiki.genexus.com/commwiki/wiki?21893) | [Simple example with DynamoDB](https://wiki.genexus.com/commwiki/wiki?50607) |
| [Suffix Text property](https://wiki.genexus.com/commwiki/wiki?42255) | [SynchronizationEvents external object](https://wiki.genexus.com/commwiki/wiki?31341) | [TAdd function](https://wiki.genexus.com/commwiki/wiki?8512) | [TDiff function](https://wiki.genexus.com/commwiki/wiki?8513) |
| [The TimeZone problem](https://wiki.genexus.com/commwiki/wiki?22135) | [Time domain](https://wiki.genexus.com/commwiki/wiki?15050) | [TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019) | [ToDate method](https://wiki.genexus.com/commwiki/wiki?14231) |
| [ToFormattedString method](https://wiki.genexus.com/commwiki/wiki?12722) | [ToString method](https://wiki.genexus.com/commwiki/wiki?7090) | [ToUniversalTime method](https://wiki.genexus.com/commwiki/wiki?16416) | [TtoC function](https://wiki.genexus.com/commwiki/wiki?8361) |
| [VarChar data type](https://wiki.genexus.com/commwiki/wiki?6778) | [View DateTime values in a selected time zone - TimeZone Scenario](https://wiki.genexus.com/commwiki/wiki?22140) | [What is a static method](https://wiki.genexus.com/commwiki/wiki?39593) | [WorkflowProcessInstance Data Type](https://wiki.genexus.com/commwiki/wiki?17771) |
| [Year function](https://wiki.genexus.com/commwiki/wiki?8380) | [Year method](https://wiki.genexus.com/commwiki/wiki?12648) |

---
