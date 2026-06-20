---
title: "GetLocation function"
source_id: 7696
source_url: https://wiki.genexus.com/commwiki/wiki?7696
genexus_version: "18"
---

# GetLocation function

Assigns an existing location to a Location variable.

### [Syntax](#Syntax)

**&***data\_type* **= GetLocation(** *Exp* **)**  
  
**Where:**  
  
*Exp*  
    Is the Location name(a Character value). If the location refers to a web service that has been imported to the Knowlege Base as an External object, the External object's name is the location name.

**Type Returned:**   
Location

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

When you have a Location variable, you must assign a location name to it. You do this by using the GetLocation function. The parameter indicates an existing location, that is, a GeneXus main object must exist with that value in the Location property, or the Name property for Web Services.

```
&Location = getlocation(!'ExtObjectName')
```

In case of using Modules, the locationName should be ModuleName\_ExternalObjecName, something like this:

```
&Location = getlocation(!'Module_ExtObjectName')
```

### [See Also](#See+Also)

[Location](https://wiki.genexus.com/commwiki/wiki?6981)


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
| [Location data type](https://wiki.genexus.com/commwiki/wiki?6981) |

---
