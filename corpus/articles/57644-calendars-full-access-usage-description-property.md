---
title: "Calendars Full Access Usage Description property"
source_id: 57644
source_url: https://wiki.genexus.com/commwiki/wiki?57644
genexus_version: "18"
---

# Calendars Full Access Usage Description property

Message that informs users why the application is requesting access to read and write calendar data.

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

Defining this property with a clear and understandable description informs the user why the application needs full access to their Apple device calendar. It is used when the application requires access to read, write, modify, or delete events from the user's calendar.

**Notes:**

* This property is not required if your app uses the [Calendar external object](https://wiki.genexus.com/commwiki/wiki?39346).
* When generating the app, the text written in this property is assigned to the [NSCalendarsFullAccessUsageDescription](https://developer.apple.com/documentation/bundleresources/information_property_list/nscalendarsfullaccessusagedescription).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?54243).

### [See Also](#See+Also)

[Calendars Write Only Usage Description property](https://wiki.genexus.com/commwiki/wiki?57643)


|  |
| --- |
| **Backlinks** |
| [Calendars Write Only Usage Description property](https://wiki.genexus.com/commwiki/wiki?57643) | [GeneXus 18 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?54243) |

---
