---
title: "VarChar data type"
source_id: 6778
source_url: https://wiki.genexus.com/commwiki/wiki?6778
genexus_version: "18"
---

# VarChar data type

Stores text values that vary in length. However, unlike with characters, it optimizes database storage.

### [Syntax](#Syntax)

**VarChar(***M*, *N***)**  
  
**Where:**  
*M*  
Specifies the possible maximum length that is predetermined by the DBMS you are using. If the length assigned to the attribute is greater than what is actually supported by the DBMS then the DBMS' maximum will be used.  
  
*N*  
Is the average length. This is used to optimize disk accesses in some DBMSs (particularly in the iSeries). The idea is that when the value of a varchar attribute is less than or equal to N, as N characters are stored (filled with blanks) in the file's record, only one disk access is required to read or store its value. If the value of the varchar attribute is greater than N, the first N are stored in the file's record and the rest are placed in an overflow area for which an additional access is required to ensure that the value is read as a whole.

### [Definition](#Definition)

The following table illustrates the properties used to define the Data Type:

|  |
| --- |
| [Maximum length property](https://wiki.genexus.com/commwiki/wiki?7236) |
| [Average length property](https://wiki.genexus.com/commwiki/wiki?7237) |
| [Enable national language support property](https://wiki.genexus.com/commwiki/wiki?11500) |
| [Value range property](https://wiki.genexus.com/commwiki/wiki?6797) |
| [Initial value property](https://wiki.genexus.com/commwiki/wiki?11765) |
| [Picture Properties Group](https://wiki.genexus.com/commwiki/wiki?6800) |

### [Description](#Description)

All functions and operators can be applied to this character data type.

The varchar data type is equivalent to character data types in all senses except in the way that they are stored in databases.

For those DBMSs that do not support this data type, it will be created as Character.  
  
The following table illustrates the maximum length tolerated by each DBMS, with the last column showing the conversion done by GeneXus:

|  |  |  |  |
| --- | --- | --- | --- |
| **DBMS** | **Max Length (M)** | **Avg. Length (N)** | **Conversion** |
| ORACLE | 4000 | Not used | Varchar(M) or Varchar2(M) 3 |
| DB2 Universal Database | 4000 | Not used | Varchar(M) |
| Informix | 32000 1 | 0 to Max length | Varchar(M,N) |
| SQL Server | 8000 | Not used | Varchar(M) |
| DB2 UDB for iSeries / iSeries Native | 320006 | 0 to Max length | Varchar(M,N) |
| Visual FoxPro | 254 2 | Not used | Character(M) |
| PostgreSQL |  | Not used | Varchar(M) |
| MySQL | 255 4  21000 5 |  |  |

1 If a column is defined in GX as Varchar(x), where x >= 255 (or 254, if it is part of an index), the field will be defined as lvarchar in the database. Besides, in this case, the average length is ignored.  
  
2 The DBMS does not support strings that vary in length (except for Long Varchar). Strings are implemented with fixed lengths. That is, a character is generated taking the length from Max Length.

3 Varchar or Varchar2; depending on the [Declare Varchar as Varchar 2](https://wiki.genexus.com/commwiki/wiki?7369) Data Store(Oracle) property.

4 Before Mysql 5.0.3.

5 In Mysql 5.0.3 and later versions. (\*)

6 16000 if [Enable national language support property](https://wiki.genexus.com/commwiki/wiki?11500) is Yes

(\*) Maximums can vary depending on the collation of the database, the MySQL version, and if [Enable national language support property](https://wiki.genexus.com/commwiki/wiki?11500) is set to YES. ref.: <https://stackoverflow.com/questions/13506832/what-is-the-mysql-varchar-max-size?lq=1>, [MySQL version property](https://wiki.genexus.com/commwiki/wiki?9420).

### [**Note**](#Note)

Attributes and variables assigned to these data types appear in reports/selectors as V (for example: V(40)). Although this data type makes use of the auto-resize facility in forms and print blocks, they can never display anything over 255 characters.

### [See also](#See+also)

* [Data types of attributes in the DBMS](https://wiki.genexus.com/commwiki/wiki?3297)
* [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370)
* [LongVarChar data type](https://wiki.genexus.com/commwiki/wiki?7371)
* [Data types list](https://wiki.genexus.com/commwiki/wiki?6779)


|  |
| --- |
| **Backlinks** |
| [Analytics external object](https://wiki.genexus.com/commwiki/wiki?31415) | [Audio external object](https://wiki.genexus.com/commwiki/wiki?30041) | [AWSQueue.MessageQueueProvider external object](https://wiki.genexus.com/commwiki/wiki?51778) |
| [AzureEventGrid.EventGridRouterProvider external object](https://wiki.genexus.com/commwiki/wiki?55341) | [AzureQueue.MessageQueueProvider external object](https://wiki.genexus.com/commwiki/wiki?51737) | [AzureQueue.MessageQueueProvider external object (GeneXus 18 Upgrade 5)](https://wiki.genexus.com/commwiki/wiki?55673) | [AzureServiceBus.MessageBrokerProvider external object](https://wiki.genexus.com/commwiki/wiki?51784) |
| [AzureServiceBus.MessageBrokerProvider external object (GeneXus 18 Upgrade 5)](https://wiki.genexus.com/commwiki/wiki?55677) | [Beacons external object](https://wiki.genexus.com/commwiki/wiki?27025) | [Case property](https://wiki.genexus.com/commwiki/wiki?39416) | [Character data type](https://wiki.genexus.com/commwiki/wiki?6777) |
| [CharAt method](https://wiki.genexus.com/commwiki/wiki?53716) | [ClientInformation external object](https://wiki.genexus.com/commwiki/wiki?31271) | [ConfigurationManager external object](https://wiki.genexus.com/commwiki/wiki?40085) |
| [Contains method](https://wiki.genexus.com/commwiki/wiki?53708) | [CrashAnalytics external object](https://wiki.genexus.com/commwiki/wiki?55161) | [CreateFromURL function](https://wiki.genexus.com/commwiki/wiki?20509) | [Data Type Filter property](https://wiki.genexus.com/commwiki/wiki?40654) |
| [Data Type property](https://wiki.genexus.com/commwiki/wiki?7232) | [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) | [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) | [Declare Varchar as Varchar2 property](https://wiki.genexus.com/commwiki/wiki?7369) |
| [DesignOps - Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871) | [Dimensions property](https://wiki.genexus.com/commwiki/wiki?7380) | [Displays Keyboard On Focus property](https://wiki.genexus.com/commwiki/wiki?51356) | [DynamoDB Support in GeneXus](https://wiki.genexus.com/commwiki/wiki?50498) |
| [EndsWith method](https://wiki.genexus.com/commwiki/wiki?53711) | [FCK HTML Editor Control](https://wiki.genexus.com/commwiki/wiki?4858) | [Files external object](https://wiki.genexus.com/commwiki/wiki?44917) | [FileTypeAttribute property](https://wiki.genexus.com/commwiki/wiki?8902) |
| [FromString method](https://wiki.genexus.com/commwiki/wiki?12694) | [GXtest UI Commands - Get Text from PDF](https://wiki.genexus.com/commwiki/wiki?49951) | [HowTo: In-app search in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?31862) | [HowTo: Use ScanBarcode method from Scanner external object in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?21661) |
| [HowTo: Use SendEmailAdvanced method from Interop external object in Native Mobile apps](https://wiki.genexus.com/commwiki/wiki?18193) | [IndexOf method](https://wiki.genexus.com/commwiki/wiki?12696) | [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) |
| [Interop external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55183) | [IsEmpty method](https://wiki.genexus.com/commwiki/wiki?9645) | [LastIndexOf method](https://wiki.genexus.com/commwiki/wiki?12697) | [Length method](https://wiki.genexus.com/commwiki/wiki?12704) |
| [LocalNotifications external object](https://wiki.genexus.com/commwiki/wiki?39554) | [LocalNotifications external object (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54527) | [Log external object](https://wiki.genexus.com/commwiki/wiki?37872) | [LongVarChar data type](https://wiki.genexus.com/commwiki/wiki?7371) |
| [PadLeft method](https://wiki.genexus.com/commwiki/wiki?12705) | [PadRight method](https://wiki.genexus.com/commwiki/wiki?12706) | [Permissions external object for Android applications](https://wiki.genexus.com/commwiki/wiki?50045) |
| [Printer external object](https://wiki.genexus.com/commwiki/wiki?48131) | [RemoteConfig external object](https://wiki.genexus.com/commwiki/wiki?48160) | [RemoveDiacritics method](https://wiki.genexus.com/commwiki/wiki?24596) | [Replace method](https://wiki.genexus.com/commwiki/wiki?12710) |
| [Rows property - Vector and Matrix](https://wiki.genexus.com/commwiki/wiki?7772) | [Runtime external object](https://wiki.genexus.com/commwiki/wiki?33076) | [Scanner external object](https://wiki.genexus.com/commwiki/wiki?31316) | [SetEmpty method](https://wiki.genexus.com/commwiki/wiki?9646) |
| [Share external object](https://wiki.genexus.com/commwiki/wiki?29800) | [StartsWith method](https://wiki.genexus.com/commwiki/wiki?53700) | [StoreManager external object](https://wiki.genexus.com/commwiki/wiki?31320) | [StrSearch function](https://wiki.genexus.com/commwiki/wiki?8529) |
| [Substring method](https://wiki.genexus.com/commwiki/wiki?12713) | [SynchronizationEvents external object](https://wiki.genexus.com/commwiki/wiki?31341) | [ToFormattedString method](https://wiki.genexus.com/commwiki/wiki?12722) | [ToLower method](https://wiki.genexus.com/commwiki/wiki?12714) |
| [ToNumeric method](https://wiki.genexus.com/commwiki/wiki?12717) | [ToString method](https://wiki.genexus.com/commwiki/wiki?7090) | [ToUpper method](https://wiki.genexus.com/commwiki/wiki?12716) | [Trim method](https://wiki.genexus.com/commwiki/wiki?12718) |
| [TrimEnd method](https://wiki.genexus.com/commwiki/wiki?12719) | [TrimStart method](https://wiki.genexus.com/commwiki/wiki?12720) | [User Control Object - Scripts definition and usage](https://wiki.genexus.com/commwiki/wiki?40598) | [XSLTApply method](https://wiki.genexus.com/commwiki/wiki?12748) |

---
