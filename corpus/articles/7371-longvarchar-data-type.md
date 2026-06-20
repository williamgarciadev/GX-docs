---
title: "LongVarChar data type"
source_id: 7371
source_url: https://wiki.genexus.com/commwiki/wiki?7371
genexus_version: "18"
---

# LongVarChar data type

To store long text descriptions.

### [Syntax](#Syntax)

**LongVarChar(***M*, *N***)**

**Where:**  
*M*  
Maximum length value. If the length assigned to the attribute is greater than what is actually supported by the DBMS then the DBMS' maximum will be used.  
  
*N*  
Average length value.

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

### 

### [Description](#Description)

The LongVarChar data type is designed to store a large number of characters, for example maintaining a large text with customer information.

The [Maximum Length](https://wiki.genexus.com/commwiki/wiki?7236) of LongVarChar attributes or variables is the following: 33,563,648. The maximum [Average Length](https://wiki.genexus.com/commwiki/wiki?7237) is 255.

For values higher than 9,999, you can only define as maximum, values that are a multiple of 1Kb. If, for example, you enter the value 10,000, the field is actually defined with size 10,240 (the multiple of 1Kb immediately higher).  
  
The following document states which data types are used for each DBMS: [Data types of attributes in the DBMS](https://wiki.genexus.com/commwiki/wiki?3297)

### [**Notes**](#Notes)

LongVarChar attributes cannot be:

* Part of an index (this also means that they cannot be part of a primary key).
* Defined as redundant.

GeneXus does not control that the size defined by the developer is supported by the DBMS. This implies that if in GeneXus an attribute is defined with size AttSize and the maximum value supported by the DBMS is MaxDBMS, with MaxDBMS being smaller than AttSize, and you try to insert a chain of characters of size StrSize, with MaxDBMS smaller than StrSize, and this is smaller or equal to AttSize, an error will occur at execution time, depending on the DBMS.

### [See also](#See+also)

* [VarChar data type](https://wiki.genexus.com/commwiki/wiki?6778)
* [Data types list](https://wiki.genexus.com/commwiki/wiki?6779)
* [Functions that Manage LongVarchar Fields](https://wiki.genexus.com/commwiki/wiki?8412)
* [SAC 18551 - CLOB support added in GeneXus 9 for Oracle 8 or higher](https://www.genexus.com/developers/websac?,,,18551)


|  |
| --- |
| **Backlinks** |
| [CharAt method](https://wiki.genexus.com/commwiki/wiki?53716) | [Contains method](https://wiki.genexus.com/commwiki/wiki?53708) |
| [Data Type Filter property](https://wiki.genexus.com/commwiki/wiki?40654) | [Data Type property](https://wiki.genexus.com/commwiki/wiki?7232) | [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) | [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) |
| [Dimensions property](https://wiki.genexus.com/commwiki/wiki?7380) | [Displays Keyboard On Focus property](https://wiki.genexus.com/commwiki/wiki?51356) | [EndsWith method](https://wiki.genexus.com/commwiki/wiki?53711) | [FCK HTML Editor Control](https://wiki.genexus.com/commwiki/wiki?4858) |
| [FileTypeAttribute property](https://wiki.genexus.com/commwiki/wiki?8902) | [FromString method](https://wiki.genexus.com/commwiki/wiki?12694) | [Functions that Manage LongVarchar Fields](https://wiki.genexus.com/commwiki/wiki?8412) | [HowTo: In-app search in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?31862) |
| [IndexOf method](https://wiki.genexus.com/commwiki/wiki?12696) | [IsEmpty method](https://wiki.genexus.com/commwiki/wiki?9645) | [LastIndexOf method](https://wiki.genexus.com/commwiki/wiki?12697) | [Length method](https://wiki.genexus.com/commwiki/wiki?12704) |
| [PadLeft method](https://wiki.genexus.com/commwiki/wiki?12705) | [PadRight method](https://wiki.genexus.com/commwiki/wiki?12706) | [Prompt](https://wiki.genexus.com/commwiki/wiki?21635) | [RemoveDiacritics method](https://wiki.genexus.com/commwiki/wiki?24596) |
| [Replace method](https://wiki.genexus.com/commwiki/wiki?12710) | [Rows property - Vector and Matrix](https://wiki.genexus.com/commwiki/wiki?7772) | [SetEmpty method](https://wiki.genexus.com/commwiki/wiki?9646) | [StartsWith method](https://wiki.genexus.com/commwiki/wiki?53700) |
| [StoreManager external object](https://wiki.genexus.com/commwiki/wiki?31320) | [StrSearch function](https://wiki.genexus.com/commwiki/wiki?8529) | [Substring method](https://wiki.genexus.com/commwiki/wiki?12713) | [SynchronizationEvents external object](https://wiki.genexus.com/commwiki/wiki?31341) |
| [ToLower method](https://wiki.genexus.com/commwiki/wiki?12714) | [ToNumeric method](https://wiki.genexus.com/commwiki/wiki?12717) | [ToString method](https://wiki.genexus.com/commwiki/wiki?7090) |
| [ToUpper method](https://wiki.genexus.com/commwiki/wiki?12716) | [Trim method](https://wiki.genexus.com/commwiki/wiki?12718) | [TrimEnd method](https://wiki.genexus.com/commwiki/wiki?12719) | [TrimStart method](https://wiki.genexus.com/commwiki/wiki?12720) |
| [User Control Object - Scripts definition and usage](https://wiki.genexus.com/commwiki/wiki?40598) | [VarChar data type](https://wiki.genexus.com/commwiki/wiki?6778) | [XSLTApply method](https://wiki.genexus.com/commwiki/wiki?12748) |

---
