---
title: "Create function"
source_id: 8359
source_url: https://wiki.genexus.com/commwiki/wiki?8359
genexus_version: "18"
---

# Create function

Encapsulates an object inside another object. The result of the function must always be assigned to the property of a Component.

### [Syntax](#Syntax)

*Control*.Object = **Create(** xxx, [parameters]**)**

**Where:**  
  
*Control*  
   It is the name of the Component control added to the object.

*xxx*  
   It is a Component or an attribute/variable containing the Component (\*).

*parameters*  
   Is the list of xxx parameters separated by a semicolon.

With the *static* option, you cannot change the web component reference at runtime, while the dynamic option allows you to change the name of the Web Component at run-time, but the parameters and data types are fixed.

**Note**: In mobile apps, it is not the name of the panel; refer to [Call Variable](https://wiki.genexus.com/commwiki/wiki?17489) to know how to name it.

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)   
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [See Also](#See+Also)

[CreateFromURL function](https://wiki.genexus.com/commwiki/wiki?20509)   
[Dynamic Component Creation](https://wiki.genexus.com/commwiki/wiki?5404)   
[Object property](https://wiki.genexus.com/commwiki/wiki?7011)


|  |
| --- |
| **Backlinks** |
| [CreateFromURL function](https://wiki.genexus.com/commwiki/wiki?20509) | [Dynamic Component Creation](https://wiki.genexus.com/commwiki/wiki?5404) | [Object property](https://wiki.genexus.com/commwiki/wiki?7011) |
| [Refresh command in web](https://wiki.genexus.com/commwiki/wiki?25286) |

---
