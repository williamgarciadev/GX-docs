---
title: "Application Bars Class property"
source_id: 37518
source_url: https://wiki.genexus.com/commwiki/wiki?37518
genexus_version: "18"
---

# Application Bars Class property

Assigns a Theme class (or DSO class) to an Application Bar.

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974)  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

This property is available in every [Application Bar](https://wiki.genexus.com/commwiki/wiki?19486) included in an object for Native Mobile applications (like a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)).

It allows indicating the [Theme Class](https://wiki.genexus.com/commwiki/wiki?6246) or [Design System Class](https://wiki.genexus.com/commwiki/wiki?49309) that sets a style to the object's Application Bar.

To change the associated Theme Class at runtime, write the following user-event code:

```
Event 'ChanageApplicationBarClass'
     ApplicationBar.Class = StyleClass:ApplicationBarsCustomClass
EndEvent
```

**Notes:**

* This property has the same behavior as the [Class property](https://wiki.genexus.com/commwiki/wiki?8741) but is applied to Application Bars, and can be used to read or write.
* Runtime changes to this property are not available in the [Menu object](https://wiki.genexus.com/commwiki/wiki?16321).


|  |
| --- |
| **Backlinks** |
| [Application Bar control in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?19486) | [ApplicationBars Theme Class](https://wiki.genexus.com/commwiki/wiki?17879) | [ApplicationBars Theme Class (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56454) |
| [Show Application Bars property](https://wiki.genexus.com/commwiki/wiki?23305) |

---
