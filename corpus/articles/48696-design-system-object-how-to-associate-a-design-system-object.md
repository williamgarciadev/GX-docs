---
title: "Design System Object - How to associate a Design System Object to your screens"
source_id: 48696
source_url: https://wiki.genexus.com/commwiki/wiki?48696
genexus_version: "18"
---

# Design System Object - How to associate a Design System Object to your screens

So that a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) take the definitions of the Design System object [Classes](https://wiki.genexus.com/commwiki/wiki?49309) and [Tokens](https://wiki.genexus.com/commwiki/wiki?47378), set the Web Panel [Style property](https://wiki.genexus.com/commwiki/wiki?8145). In the example, it was changed from the default value, Carmine, to the name given to the Design System object.

`[imagen omitida: wiki id 48649]`

However, something more general could also be done. For example, modify this default by changing the property at the version level; in this way, any new object created with Style will have the Design System Object indicated there.

`[imagen omitida: wiki id 48650]`

Note: For a while, the Theme object will coexist with the [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) that has been released to replace it. That’s why the Carmine Theme is still the default. However, you can always convert it to a Design System Object:

`[imagen omitida: wiki id 48651]`

Take into account that for Native Mobile or Angular objects, the [Style property](https://wiki.genexus.com/commwiki/wiki?43966) can be set for each Platform (under the [Platforms node](https://wiki.genexus.com/commwiki/wiki?24284)). In addition, the [Platform Overrides property](https://wiki.genexus.com/commwiki/wiki?40583) is available for the same objects when they are set as main, to be able to assign them a different Style than that of the Platform.

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).


|  |
| --- |
| **Backlinks** |
| [Category:Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) | [Toc:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) | [HowTo: Set the style of a read-only Attribute/Variable control using DSO](https://wiki.genexus.com/commwiki/wiki?49906) |

---
