---
title: "Calendars Write Only Usage Description property"
source_id: 57643
source_url: https://wiki.genexus.com/commwiki/wiki?57643
genexus_version: "18"
---

# Calendars Write Only Usage Description property

Message that informs users why the application is requesting access to create calendar events.

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

This property allows you to describe why the application is requesting permission to write to the iOS device calendar  
(although it does not need full access).

Unlike [Calendars Full Access Usage Description property](https://wiki.genexus.com/commwiki/wiki?57644), this one is used when the app only needs permissions to add events to the calendar, but not to access or modify existing events.

**Notes:**

* This property is not required if your app uses the [Calendar external object](https://wiki.genexus.com/commwiki/wiki?39346).
* When generating the app, the text written in this property is assigned to the [NSCalendarsWriteOnlyAccessUsageDescription](https://developer.apple.com/documentation/bundleresources/information_property_list/nscalendarswriteonlyaccessusagedescription).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?54243).


|  |
| --- |
| **Backlinks** |
| [Calendars Full Access Usage Description property](https://wiki.genexus.com/commwiki/wiki?57644) | [GeneXus 18 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?54243) |

---
