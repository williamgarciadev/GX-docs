---
title: "Filter by UI property"
source_id: 55701
source_url: https://wiki.genexus.com/commwiki/wiki?55701
genexus_version: "18"
---

# Filter by UI property

Selects a User Interface to filter the Design System Class Properties that are applicable to it.

### [Values](#Values)

|  |  |
| --- | --- |
| **Panels** | Filters the properties available to be set only in objects generated for Native Mobile (Apple and Android) and Angular apps. (It does not only apply to Panels but also to Menus, etc.). |
| **Web Panels** | Filters the properties available to be set only in web objects generated for .NET and Java apps. (It does not only apply to Web Panels but also to Web Components, Web Master Panel, etc.). |
| **Web** | Filters the properties available to be set only in objects generated for Angular, .NET, and Java apps. |
| **Any** | It does not filter properties that apply to interfaces. |
| **All** | Filters the properties that apply to all interfaces (Apple, Android, Angular, .NET, Java). |

### [Scope](#Scope)

**Objects:** [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

When a value other than "Any" is selected in the "Filter by UI" property, only the [Design System Class Properties](https://wiki.genexus.com/commwiki/wiki?49323) associated with the selected category will be displayed, excluding the others.

For example, if you choose "Web Panels", you will see GeneXus-specific Class properties that begin with the prefix "gx-". On the other hand, if you select "Web", additional CSS properties will be listed that are not available when you choose the values "All" or "Panels".

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

No action is required to apply the corresponding changes when the property value is configured.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239).


|  |
| --- |
| **Backlinks** |
| [HowTo: Configure Design System Class Properties](https://wiki.genexus.com/commwiki/wiki?49494) |

---
