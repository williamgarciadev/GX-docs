---
title: "Associated table property (in Data Views)"
source_id: 8063
source_url: https://wiki.genexus.com/commwiki/wiki?8063
genexus_version: "18"
---

# Associated table property (in Data Views)

Sets the name of the internal table associated with the Data View.

### [Scope](#Scope)

**Objects:** [Data View](https://wiki.genexus.com/commwiki/wiki?1914)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

In this property, you have to indicate the name of the internal table associated with the Data View. You can select it through the [Select Objects dialog](https://wiki.genexus.com/commwiki/wiki?9889).

#### [**Consideration**](#Consideration)

It is not allowed to have more than one [Data View object](https://wiki.genexus.com/commwiki/wiki?1914) with the same associated table. If this occurs, when impacting the database, the following error will be displayed:

rgz0035, 'Table %1 is associated to more than one Data View (%2).'


|  |
| --- |
| **Backlinks** |
| [Azure Cosmos DB external data store](https://wiki.genexus.com/commwiki/wiki?53330) | [Information Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?45847) |

---
