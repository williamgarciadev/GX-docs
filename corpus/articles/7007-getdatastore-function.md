---
title: "GetDataStore function"
source_id: 7007
source_url: https://wiki.genexus.com/commwiki/wiki?7007
genexus_version: "18"
---

# GetDataStore function

Assigns a GeneXus Data Store to a DBConnection variable.

### [Syntax](#Syntax)

**&***data\_type* **=** **GetDataStore(***Exp***)**

**Where:**  
  
*Exp*  
   Datastore name. Character.

**Type Returned:**  
DBConnection

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual Basic (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

When you have a DBConnection variable, you must assign a GeneXus data store to it. You do this by using the GetDataStore function. The parameter indicates a valid GeneXus data store name (e.g. ‘Default’ indicates the name of the default data store).

### [See Also](#See+Also)

[DBConnection](https://wiki.genexus.com/commwiki/wiki?6923)  
[DataStoreName Property](https://wiki.genexus.com/commwiki/wiki?7006)


|  |
| --- |
| **Backlinks** |
| [DatastoreName Property](https://wiki.genexus.com/commwiki/wiki?7006) | [DBConnection Data Type](https://wiki.genexus.com/commwiki/wiki?6923) |

---
