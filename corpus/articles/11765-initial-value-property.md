---
title: "Initial value property"
source_id: 11765
source_url: https://wiki.genexus.com/commwiki/wiki?11765
genexus_version: "18"
---

# Initial value property

Initializes attributes and variables based on domains in any object, with a constant value, formula or procedure, when a reorganization is necessary.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

It initializes the value of attributes of any GeneXus object. It initializes variables based on attributes or domains, and performs initial value calling procedures, and loading SDTs, too. The values to be given to the property must correspond to the attribute's data type.

#### [Notes:](#Notes%3A)

* This property is not available when the attribute is a formula.
* If you want to initialize an attribute or variable of [GUID data type](https://wiki.genexus.com/commwiki/wiki?31772), you must set the value False in the [Autogenerate Guid property](https://wiki.genexus.com/commwiki/wiki?40892).

### [Samples](#Samples)

To date: **#10-12-23#**  
To datetime: **#10-12-23 08:12:36#**  
To numeric integer: **4326**  
To numeric decimal: **4326.93**  
To character (take into account the quotes):**'Hello World'**  
To boolean:**TRUE/FALSE**  
To GUID: **GUID.fromstring("4f7d4021-63de-4253-b57f-ac5bce9b9279")**


|  |
| --- |
| **Backlinks** |
| [Autogenerate Guid property](https://wiki.genexus.com/commwiki/wiki?40892) | [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) | [GUID data type](https://wiki.genexus.com/commwiki/wiki?31772) |
| [Initial value property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54229) | [LongVarChar data type](https://wiki.genexus.com/commwiki/wiki?7371) | [VarChar data type](https://wiki.genexus.com/commwiki/wiki?6778) |

---
