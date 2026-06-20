---
title: "GeneXus Extensions"
source_id: 3243
source_url: https://wiki.genexus.com/commwiki/wiki?3243
genexus_version: "18"
---

# GeneXus Extensions

The GeneXus development environment is actually a generic, extensible [IDE](https://wiki.genexus.com/commwiki/wiki?5272), where modules (called packages) can be added to provide specific features.

The generic [IDE](https://wiki.genexus.com/commwiki/wiki?5272) provides both a generic UI framework -with services allowing for management and interaction with documents, menus, toolbars, toolwindows, etc.- and a [Universal Data Model](https://wiki.genexus.com/commwiki/wiki?1835,,) -which handles basic concepts such as knowledge base, model, object, object versions, etc. Everything else is incorporated by means of additional packages that define new concepts, add features and enrich the user interface. In fact, what we know as GeneXus X is implemented as a collection of packages integrated into the generic IDE. The packages that implement [GeneXus](https://wiki.genexus.com/commwiki/wiki?3146,,) define specific object types (e.g.: Transaction, Domain, Attribute, SubtypeGroup, etc.), provide editors for each of them, validate them, and implement operations such as normalization, specification, generation, etc., among other functions.

In theory, there is no difference between the packages that can be developed by third parties to integrate into [GeneXus IDE](https://wiki.genexus.com/commwiki/wiki?5272) and those developed by Artech itself to implement GeneXus, although of course, not every package needs to have such a degree of complexity or provide that much functionality.

Some of the features that may be included in a package are:

* Defining new object types
* Defining new object parts (to be added to objects of types defined either by the same package or by any other package)
* Providing user interface editors (associated to object part types defined in the same package or in any other)
* Adding options to the main menu and handling the commands associated with any of the menu options
* Adding its own toolbars and toolwindows
* Defining new properties for any object type or any object part type
* Subscription to events published by the [IDE](https://wiki.genexus.com/commwiki/wiki?5272) or other packages, and publication of its own events.
* Using services exposed by the [IDE](https://wiki.genexus.com/commwiki/wiki?5272) or other packages, and exposing its own services.

To try out these possibilities you can [download](https://wiki.genexus.com/commwiki/wiki?27521,,) the SDK platform from the Download Center, and subscribe to the GeneXus Extensions Forum  [here](https://www.genexus.com/en/developers/forums ).

### [See Also](#See+Also)

[Getting Started](https://wiki.genexus.com/commwiki/wiki?4681,,)


|  |
| --- |
| **Pages** |
| [Compatibility Package Number](https://wiki.genexus.com/commwiki/wiki?45252,Compatibility+Package+Number,) | [Extensions and Patterns Compatibility in GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46392,Extensions+and+Patterns+Compatibility+in+GeneXus+17,) | [GeneXus Platform SDK](https://wiki.genexus.com/commwiki/wiki?3271,GeneXus+Platform+SDK,) |
| [HowTo: Install GX extensions](https://wiki.genexus.com/commwiki/wiki?7623) |

---
