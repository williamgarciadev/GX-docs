---
title: "SetTheme function"
source_id: 41978
source_url: https://wiki.genexus.com/commwiki/wiki?41978
genexus_version: "18"
---

# SetTheme function

Changes the application Theme (or Design System) at runtime for any other Theme (or Design System) included in the [Additional Styles property](https://wiki.genexus.com/commwiki/wiki?40582). The change must be made for the same type of object.

### [Syntax](#Syntax)

**&**Number = **SetTheme**("ObjectName")

**Where:**

*"ObjectName"*  
    Name of the [Theme object](https://wiki.genexus.com/commwiki/wiki?16595) or [Design System object](https://wiki.genexus.com/commwiki/wiki?47375) to change.

**Type returned:**  
Numeric(1)

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

This function changes the application Theme (or Design System) at runtime for any other Theme (or Design System) included in the [Additional Styles property](https://wiki.genexus.com/commwiki/wiki?40582).   
The change must be made for the same type of object.  
The function returns 1 when the change is successful, or 0 otherwise.   
If the object can't be changed, the current object remains as if the function was not executed.   
The change persists as long as the application session is active.

### [Samples](#Samples)

```
Event 'SetTheme'
   &num = SetTheme(!'SimpleAndroid')
Endevent
```

### [Availability](#Availability)

[Design System Object](https://wiki.genexus.com/commwiki/wiki?47375)s are supported by this function since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).


|  |
| --- |
| **Backlinks** |
| [Flipping The Interface for Right-to-Left](https://wiki.genexus.com/commwiki/wiki?54467) | [Rendering precedences for controls with Design System Object](https://wiki.genexus.com/commwiki/wiki?49302) | [SetLanguage function (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54431) |

---
