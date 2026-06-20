---
title: "SetTheme function for Web"
source_id: 21777
source_url: https://wiki.genexus.com/commwiki/wiki?21777
genexus_version: "18"
---

# SetTheme function for Web

Changes the current application Web Theme (or Design System) for any other Web Theme (or Design System) at runtime. The change must be made for the same type of object.

### [Syntax](#Syntax)

**&**Number = **SetTheme**("ObjectName")

**Where:**

*"ObjectName"*  
    Name of the [Web Theme object](https://wiki.genexus.com/commwiki/wiki?6420) or [Design System object](https://wiki.genexus.com/commwiki/wiki?47375) to change.

**Type returned:**  
Numeric(1)

### [Scope](#Scope)

**Objects:**[Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270), [Panel](https://wiki.genexus.com/commwiki/wiki?24829)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604),[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),[Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

This function changes the application Web Theme (or Design System) for another WebTheme (or Design System) at runtime.  
The change must be made for the same type of object.  
The function returns 1 when the object could be changed. Otherwise, it returns 0.   
If the object can't be changed, the current object remains as if the function was not executed.   
Once the SetTheme function has been successful, the Web Theme setting remains active for the rest of the session. In Web applications, it means that [GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) code automatically saves the value of the current Web Theme in the current session.

### [Samples](#Samples)

```
Event &MyTheme.Click
    If SetTheme(&MyTheme)<>0
       ...
    EndIf
EndEvent
```

```
Event 'Orange'
    &NumVar = SetTheme(!'Orange')   // Set the web page with the Orange theme inmediately.
EndEvent
```

Take into account the "!" symbol before the theme name for translation purposes. (For further information, see [GeneXus Application Localization](https://wiki.genexus.com/commwiki/wiki?6330)).

### [Availability](#Availability)

[Design System Object](https://wiki.genexus.com/commwiki/wiki?47375)s are supported by this function since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).

### [See Also](#See+Also)

[GetTheme function](https://wiki.genexus.com/commwiki/wiki?21778)  
[SetLanguage function](https://wiki.genexus.com/commwiki/wiki?18757)


|  |
| --- |
| **Backlinks** |
| [Flipping The Interface for Right-to-Left (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54489) | [GetTheme function](https://wiki.genexus.com/commwiki/wiki?21778) |
| [Real-time translation of RTL languages](https://wiki.genexus.com/commwiki/wiki?54482) | [Real-time translation of RTL languages (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54495) | [Rendering precedences for controls with Design System Object](https://wiki.genexus.com/commwiki/wiki?49302) |
| [Translation types](https://wiki.genexus.com/commwiki/wiki?54437) | [Translation types (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54444) |

---
