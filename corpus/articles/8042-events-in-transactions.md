---
title: "Events in Transactions"
source_id: 8042
source_url: https://wiki.genexus.com/commwiki/wiki?8042
genexus_version: "18"
---

# Events in Transactions

[Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s support Event Driven Programming, allowing you to create dynamic and responsive logic. This means you can include code within specific events, which remain inactive until triggered.

For example, an event can be associated with a control, and when that control is pressed, the event is activated and any associated code is executed.

Additionally, some events are triggered automatically by the system.

The events available in Transactions are:

|  |
| --- |
| [After Trn event](https://wiki.genexus.com/commwiki/wiki?8045) |
| Delete event (\*) |
| [Exit event](https://wiki.genexus.com/commwiki/wiki?8046) |
| Insert event (\*) |
| [OnMessage event](https://wiki.genexus.com/commwiki/wiki?58714) |
| [Start event](https://wiki.genexus.com/commwiki/wiki?8043) |
| [TrackContext event](https://wiki.genexus.com/commwiki/wiki?8051) |
| Update event (\*) |

(\*) The Insert, Update, and Delete events only apply to a special use case of Transactions: [Dynamic Transactions](https://wiki.genexus.com/commwiki/wiki?28062) that allow updating data. Read about them at [Dynamic Transactions that update data](https://wiki.genexus.com/commwiki/wiki?28656).

You can also define [User defined event](https://wiki.genexus.com/commwiki/wiki?8044)s.

### [See Also](#See+Also)

[Triggering context for Events and Rules](https://wiki.genexus.com/commwiki/wiki?11735)


|  |
| --- |
| **Backlinks** |
| [Commands in Transactions](https://wiki.genexus.com/commwiki/wiki?8649) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Table of contents:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) |
| [Category:Insert - Function...](https://wiki.genexus.com/commwiki/wiki?6877) | [Insert - Rule...](https://wiki.genexus.com/commwiki/wiki?13683) | [Transaction events when executed as Business Component](https://wiki.genexus.com/commwiki/wiki?23813) | [Category:Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) |
| [Triggering context for Events and Rules](https://wiki.genexus.com/commwiki/wiki?11735) |

---
