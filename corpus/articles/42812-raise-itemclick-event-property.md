---
title: "Raise ItemClick event property"
source_id: 42812
source_url: https://wiki.genexus.com/commwiki/wiki?42812
genexus_version: "18"
---

# Raise ItemClick event property

True if the item raises the ItemClick event when clicked.

### [Description](#Description)

When displaying a query in the QueryViewer or DashboardViewer control, you may want to enable the ItemClick event only for some of the attributes and not for all of them. This property at query attribute level allows you to do just that. The ItemClick event will be raised only for those attributes that have this property set to true (this is the default value). Also, the visual feedback when moving the mouse over the attribute value (i.e., changing the pointer icon and underlining the attribute value) will only occur for these attributes.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at run-time and at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Build with this Only of the object.

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 4](https://wiki.genexus.com/commwiki/wiki?42755,,).

### [Scope](#Scope)

**Objects:** Dashboard, Query  
**Platforms:** Web(.Net, .Net Core, Java)

### [See Also](#See+Also)

[ItemClick Event](https://wiki.genexus.com/commwiki/wiki?19570)


|  |
| --- |
| **Backlinks** |
| [Allow Selection property in QueryViewer](https://wiki.genexus.com/commwiki/wiki?42903) | [ItemClick Event](https://wiki.genexus.com/commwiki/wiki?19570) | [On item click property](https://wiki.genexus.com/commwiki/wiki?40126) |

---
