---
title: "Server Side Functions/Methods"
source_id: 11572
source_url: https://wiki.genexus.com/commwiki/wiki?11572
genexus_version: "18"
---

# Server Side Functions/Methods

Whenever a navigation group (For Each, Data Provider Group with Base Table, Grid with Base Table, Formula, etc) references a function or method, GeneXus determines whether that function can be evaluated in the server by the DMBS handler. If it is resolved by the DMBS it is better because the whole navigation could be evaluated on the server side, thus optimizing the access to them; instead of solved by program.  
  
The list that follows shows the function or method that currently are evaluated on the server side for at least one of the DBMS.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **GeneXus Function/Method** | **SQLServer** | **Oracle** | **MySQL** | **DB2** | **DB2 ISERIES** | **Informix** | **PostgreSQL** | **SQLite** |
| ***Dates Handling*** |
| Day3 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | - |
| Month3 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | - |
| Year3 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | - |
| Hour3 | Yes | Yes1 | Yes | Yes | Yes | Yes | Yes | - |
| Minute3 | Yes | Yes 1 | Yes | Yes | Yes | Yes | Yes | - |
| Second | Yes | Yes 1 | Yes | Yes | Yes | Yes | Yes | - |
| AddMth / AddMonths | Yes | NO | Yes | Yes | Yes 2 | Yes | Yes | - |
| AddYr / AddYears | Yes | Yes | Yes | Yes | Yes2 | Yes | Yes | - |
| + Operator / AddDays | Yes | Yes | Yes | Yes | Yes | Yes | Yes | - |
| Age | Yes | Yes | Yes | Yes | Yes2 | Yes | Yes | - |
| Dow3 / DayOfWeek3 | Yes | NO | Yes | Yes | Yes2 | Yes | Yes | - |
| Eom3 / EndOfMonth3 | Yes | Yes | NO | NO | Yes2 | Yes | Yes | - |
| TAdd / AddSeconds | Yes | NO | Yes | NO | NO | Yes | Yes | - |
| TDiff / Difference | Yes | Yes | Yes | Yes | Yes | Yes | Yes | - |
| ServerNow | Yes | Yes | Yes | Yes | Yes4 | NO | Yes | - |
| ServerDate | Yes | Yes | Yes | Yes | Yes4 | NO | Yes | - |
| ***Numeric Values Handling*** |
| Int / Integer | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Round | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Trunc / Truncate | Yes | Yes | Yes | Yes | Yes | Yes | Yes | - |
| ***Strings Handling*** |
| Asc | Yes | Yes | Yes | Yes | NO | Yes | Yes | - |
| Val / ToNumeric | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Len / Length | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Lower / ToLower | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Ltrim / TrimStart | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Padl / PadLeft | Yes | Yes | Yes | Yes | NO | Yes | Yes | Yes |
| Padr / PadRight | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Rtrim / TrimEnd | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Str | Yes | Yes | Yes | NO | NO | Yes | Yes | - |
| Strreplace / Replace | Yes | Yes | Yes | Yes | NO | Yes | Yes | Yes |
| Strsearch / IndexOf | Yes | Yes | Yes | Yes | Yes | NO | Yes | - |
| Strsearchrev / LastIndexOf | Yes | Yes | NO | NO | NO | NO | NO | - |
| Substr / Substring | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Trim | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Upper / ToUpper | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Concat | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| + (to concatenate) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| ***GUID Handling*** |
| FromString5 | Yes (2012+) | Yes | Yes | NO | NO | NO | Yes | NO |
| ToString5 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | - |
| ***Geography Handling*** | | | | | | | | |
| Distance | Yes |  | Yes (5.7.7+) |  |  |  |  |  |
| Intersect | Yes |  | NO |  |  |  |  |  |
| ***Other functions*** |
| iif | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| IsMatch | NO | Yes | Yes | NO | NO | NO | Yes | NO |
| ReplaceRegEx | NO | Yes | NO | NO | NO | NO | Yes | NO |

### [Notes](#Notes)

* When navigation group (For Each, Data Provider, Grid) includes in their **Where/Condition** clause a function or method that can not be evaluated by the DBMS, a warning icon `[imagen omitida: wiki id 21326]` will be shown for that condition in the navigation list. Passing the mouse over it displays: "Constraint evaluated in the client. This may lead to poor performance"
* 1 Supported as "Server Side" since Oracle 9.
* 2 Supported as "Server Side" only if the value of the property [Date data type](https://wiki.genexus.com/commwiki/wiki?7373) definition is "Date" and argument is Date (not DateTime).
* 3 Some of the functions handling Datetime fields may not be evaluated in the DBMS when [TimeZone Support](https://wiki.genexus.com/commwiki/wiki?21988) is Enabled. See [TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019) for more information.
* 4 It only applies if the value of the property [Date data type](https://wiki.genexus.com/commwiki/wiki?7373) definition is "Date".
* 5 Supported as "Server Side" since [GeneXus 16 upgrade 5](https://wiki.genexus.com/commwiki/wiki?43446,,)


|  |
| --- |
| **Backlinks** |
| [IsEmpty method](https://wiki.genexus.com/commwiki/wiki?9645) | [Locking in GeneXus Applications](https://wiki.genexus.com/commwiki/wiki?45652) | [Server Paging](https://wiki.genexus.com/commwiki/wiki?15589) |
| [Specification Codes from spc0050 to spc0099](https://wiki.genexus.com/commwiki/wiki?6432) | [Specification Codes from spc0100 to spc0149](https://wiki.genexus.com/commwiki/wiki?6433) | [ToNumeric method](https://wiki.genexus.com/commwiki/wiki?12717) | [Val function](https://wiki.genexus.com/commwiki/wiki?8528) |

---
