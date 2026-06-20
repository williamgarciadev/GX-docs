---
title: "Maximum Size of LongVarChar Fields"
source_id: 7767
source_url: https://wiki.genexus.com/commwiki/wiki?7767
genexus_version: "18"
---

# Maximum Size of LongVarChar Fields

To detail the Maximum size of Long Varchar fields.

### [Description](#Description)

Some platforms support attributes of this type with a size larger than the ones that could be defined in GeneXus.

The maximum size (Max) of a Long Varchar attribute or variable, since GeneXus 7.0 is: 33563648. The maximum average value (Avg. Len) is 255.

For values higher than 9999 you can only define as maximum, values that are multiples of 1Kb. If, for example, you enter the value 10000, the field is actually defined with size 10240, that is: the multiple of 1Kb immediately higher.

#### [Important:](#Important%3A)

GeneXus does not control that the size defined by the user is supported by the DBMS. This implies that if in GeneXus an attribute is defined with AttSize and the maximum value supported by the DBMS is MaxDBMS, being MaxDMBS smaller than AttSize, when you try to insert a chain of characters of size StrSize, with MaxDBMS smaller than StrSize, and this is smaller or equal to AttSize, an error will occur at execution time, depending on the DBMS.

Maximums and limits:

* The maximum supported by the Visual FoxPro Client/Server generator is 2 MB.
* In Visual Basic, the limit is at 32 KB, but this limit will widen in upcoming versions of the generator.
* There are no limitations in Java and .NET.

Note that all management of these fields is performed in memory, so, upon selecting the maximum size you must take into account the power of the client machine that will have to execute the application.

### [Scope](#Scope)

**Objects:** [Transactions](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916), [Procedures](https://wiki.genexus.com/commwiki/wiki?6293)  
**Languages:** Cobol, RPG, Visual FoxPro, Java, .NET, Ruby

####


|  |
| --- |
| **Backlinks** |
| [Average length property](https://wiki.genexus.com/commwiki/wiki?7237) | [Maximum length property](https://wiki.genexus.com/commwiki/wiki?7236) | [Technical specifications of GeneXus](https://wiki.genexus.com/commwiki/wiki?55715) |

---
