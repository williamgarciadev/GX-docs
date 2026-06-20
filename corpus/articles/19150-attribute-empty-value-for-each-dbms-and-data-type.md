---
title: "Attribute Empty Value for each DBMS and Data Type"
source_id: 19150
source_url: https://wiki.genexus.com/commwiki/wiki?19150
genexus_version: "18"
---

# Attribute Empty Value for each DBMS and Data Type

The following table shows the corresponding empty value for each data type and DBMS.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **DBMS** | **Numeric** | **Date** | **Datetime (\*\*)** | **Character (n)** | **Varchar** | **Long Varchar** | **Blob** |
| **SQL Server** | 0 | 1753-01-01 00:00:00.000 | 1753-01-01 00:00:00.000 | n blanks | <empty string> | <empty string> | <empty file> |
| **Oracle** | 0 | 0001-01-01 00:00:00 | 0001-01-01 00:00:00 | n blanks | 1 blank | 1 blank | <empty file> |
| **DB2 UDB** | 0 | 0001-01-01 | 0001-01-01 00:00:00.000 | n blanks | <empty string> | <empty string> | <empty file> |
| **DB2 iSeries** | 0 | "00000000"  or 0001-01-01 (\*) | 0001-01-01-00.00.00 | n blanks | <empty string> | <empty string> | <empty file> |
| **MySQL** | 0 | 1000-01-01 | 1000-01-01 00:00:00 | <empty string> | <empty string> | <empty string> | <empty file> |
| **PostgreSQL** | 0 | 0001-01-01 | 0001-01-01 00:00:00 | n blanks | <empty string> | <empty string> | <empty file> |
| **Informix** | 0 | 0001-01-01 | 0001-01-01 00:00:00 | n blanks | <empty string> | <empty string> | <empty file> |

(\*) For DB2 iSeries, the empty value depends on the *Date Data Type Definition* model property value.

(\*\*) Empty values are invariable with respect to the [Precision](https://wiki.genexus.com/commwiki/wiki?39306). More information at [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370)


|  |
| --- |
| **Backlinks** |
| [Date Constants](https://wiki.genexus.com/commwiki/wiki?4372) | [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) | [SetEmpty method](https://wiki.genexus.com/commwiki/wiki?9646) |

---
