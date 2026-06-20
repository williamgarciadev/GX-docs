---
title: "Return After Digression property"
source_id: 48096
source_url: https://wiki.genexus.com/commwiki/wiki?48096
genexus_version: "18"
---

# Return After Digression property

If true, it returns to the previous flow when the current flow is finished.

### [Scope](#Scope)

**Objects:** [Conversational Flows Instance](https://wiki.genexus.com/commwiki/wiki?37113)

### [Description](#Description)

It allows defining, at the end of a digression that had this flow as a target, whether to return to the flow that triggered the digression to end it, depending on whether its value is True or False.

The default value of this property is True; that is to say, when it is necessary to go to another flow to make a query, the default behavior is to return to the main flow, to completely close it.

This property will be visible if the [NLP Provider property](https://wiki.genexus.com/commwiki/wiki?38931) is set to Watson, and if the [Available For Digressions property](https://wiki.genexus.com/commwiki/wiki?48095) is set to True.

`[imagen omitida: wiki id 48258]`

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Availability](#Availability)

This property is available since [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,).

### [See Also](#See+Also)

[Available For Digressions property](https://wiki.genexus.com/commwiki/wiki?48095)  
[Digression property](https://wiki.genexus.com/commwiki/wiki?48097)


|  |
| --- |
| **Backlinks** |
| [Available For Digressions property](https://wiki.genexus.com/commwiki/wiki?48095) | [Digression property](https://wiki.genexus.com/commwiki/wiki?48097) |

---
