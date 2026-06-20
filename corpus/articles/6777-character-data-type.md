---
title: "Character data type"
source_id: 6777
source_url: https://wiki.genexus.com/commwiki/wiki?6777
genexus_version: "18"
---

# Character data type

Stores text values.

### [Definition](#Definition)

**Character(***M***)**  
  
**Where:**  
*M*  
Specifies the length of the character, where the maximum length is 9999.

The length of a Character field is fixed so that you cannot change the length you declared for that field when you created the table. All functions and operators can be applied to this data type.  
  
The following table illustrates the maximum length tolerated by each DBMS and the conversion done by GeneXus according to the DBMS:

|  |  |  |
| --- | --- | --- |
| **DBMS** | **Length** | **Conversion** |
| Oracle | 255 | Char |
| DB2 Universal Database | 255 | Char |
| Informix | 9999 | Char |
| SQL Server | 8000 | Char |
| Access | 254 | dbText |
| DB2 for iSeries | 320001 | Char |
| DBF | 254 | Char |
| PostgreSQL | 9999 | Char |

132765 in [Genexus 15 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?38023,,) or previous.  
  
The Character and [VarChar data type](https://wiki.genexus.com/commwiki/wiki?6778) Data types are similar but differ in the way they are stored and retrieved.

### [See also](#See+also)

[VarChar data type](https://wiki.genexus.com/commwiki/wiki?6778)  
[Data types list](https://wiki.genexus.com/commwiki/wiki?6779)


|  |
| --- |
| **Backlinks** |
| [Actions external object](https://wiki.genexus.com/commwiki/wiki?31350) | [Analytics external object](https://wiki.genexus.com/commwiki/wiki?31415) | [Analytics external object (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54509) |
| [Analytics external object (GeneXus 18 Upgrade 7 or prior)](https://wiki.genexus.com/commwiki/wiki?57371) | [Audio external object](https://wiki.genexus.com/commwiki/wiki?30041) | [AudioRecorder external object](https://wiki.genexus.com/commwiki/wiki?34096) | [Case property](https://wiki.genexus.com/commwiki/wiki?39416) |
| [CharAt method](https://wiki.genexus.com/commwiki/wiki?53716) | [Checkpermission method of GAMRepository Object](https://wiki.genexus.com/commwiki/wiki?20599) | [ClientStorage external object](https://wiki.genexus.com/commwiki/wiki?31272) | [Clipboard external object](https://wiki.genexus.com/commwiki/wiki?31273) |
| [Contacts external object](https://wiki.genexus.com/commwiki/wiki?31276) | [Contains method](https://wiki.genexus.com/commwiki/wiki?53708) | [Data Type Filter property](https://wiki.genexus.com/commwiki/wiki?40654) |
| [Data Type property](https://wiki.genexus.com/commwiki/wiki?7232) | [Category:Data Types](https://wiki.genexus.com/commwiki/wiki?6558) | [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) | [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) |
| [Dimensions property](https://wiki.genexus.com/commwiki/wiki?7380) | [Displays Keyboard On Focus property](https://wiki.genexus.com/commwiki/wiki?51356) | [EndsWith method](https://wiki.genexus.com/commwiki/wiki?53711) | [Facebook external object](https://wiki.genexus.com/commwiki/wiki?38432) |
| [FileTypeAttribute property](https://wiki.genexus.com/commwiki/wiki?8902) | [FromString method](https://wiki.genexus.com/commwiki/wiki?12694) | [Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274) | [Geolocation external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55149) |
| [GXScheduler User Control](https://wiki.genexus.com/commwiki/wiki?11583) | [HowTo: In-app search in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?31862) | [IndexOf method](https://wiki.genexus.com/commwiki/wiki?12696) | [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) |
| [Interop external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55183) | [IsEmpty method](https://wiki.genexus.com/commwiki/wiki?9645) | [LastIndexOf method](https://wiki.genexus.com/commwiki/wiki?12697) | [Length method](https://wiki.genexus.com/commwiki/wiki?12704) |
| [Maps external object](https://wiki.genexus.com/commwiki/wiki?44309) | [Navigation external object](https://wiki.genexus.com/commwiki/wiki?32395) | [PadLeft method](https://wiki.genexus.com/commwiki/wiki?12705) | [PadRight method](https://wiki.genexus.com/commwiki/wiki?12706) |
| [Progress external object](https://wiki.genexus.com/commwiki/wiki?39341) | [RemoveDiacritics method](https://wiki.genexus.com/commwiki/wiki?24596) | [Replace method](https://wiki.genexus.com/commwiki/wiki?12710) | [Rows property - Vector and Matrix](https://wiki.genexus.com/commwiki/wiki?7772) |
| [SetEmpty method](https://wiki.genexus.com/commwiki/wiki?9646) | [StartsWith method](https://wiki.genexus.com/commwiki/wiki?53700) | [Storage Provider API](https://wiki.genexus.com/commwiki/wiki?32087) |
| [StrSearch function](https://wiki.genexus.com/commwiki/wiki?8529) | [Substring method](https://wiki.genexus.com/commwiki/wiki?12713) | [ToFormattedString method](https://wiki.genexus.com/commwiki/wiki?12722) | [ToLower method](https://wiki.genexus.com/commwiki/wiki?12714) |
| [ToNumeric method](https://wiki.genexus.com/commwiki/wiki?12717) | [ToString method](https://wiki.genexus.com/commwiki/wiki?7090) | [ToUpper method](https://wiki.genexus.com/commwiki/wiki?12716) | [Trim method](https://wiki.genexus.com/commwiki/wiki?12718) |
| [TrimEnd method](https://wiki.genexus.com/commwiki/wiki?12719) | [TrimStart method](https://wiki.genexus.com/commwiki/wiki?12720) | [Twitter external object](https://wiki.genexus.com/commwiki/wiki?39432) | [User Control Object - Definition of properties](https://wiki.genexus.com/commwiki/wiki?39541) |
| [User Control Object - Definition of properties (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53689) | [User Control Object - Scripts definition and usage](https://wiki.genexus.com/commwiki/wiki?40598) | [XSLTApply method](https://wiki.genexus.com/commwiki/wiki?12748) |

---
