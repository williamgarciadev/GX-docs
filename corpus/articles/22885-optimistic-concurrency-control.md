---
title: "Optimistic concurrency control"
source_id: 22885
source_url: https://wiki.genexus.com/commwiki/wiki?22885
genexus_version: "18"
---

# Optimistic concurrency control

GeneXus uses the [Optimistic concurrency control](http://en.wikipedia.org/wiki/Optimistic_concurrency_control) mechanism when updating records via [Transaction objects](https://wiki.genexus.com/commwiki/wiki?1908) and [Business Components](https://wiki.genexus.com/commwiki/wiki?5846).

This mechanism assumes that multiple "database transactions" can complete without affecting each other and that therefore these "database transactions" can proceed without locking the data resources that they affect. Before performing an update, each database transaction verifies that no other database transaction has modified its data.

This has a relation with the stateless nature of the web; which makes locking infeasible for web user interfaces. It's common for a user to start editing a record, then leave without following a "cancel" or "logout" link. If locking is used, other users who attempt to edit the same record must wait until the first user's lock times out.

Instead of locking every record every time that it is used, the system merely looks for indications that two users actually did try to update the same record at the same time. If that evidence is found, then one user's updates are discarded and the user is informed.

In the GeneXus context, when two or more users want to update the same record, the first one will be able to update it and the others will get an error (because they were about to save new data based on outdated information updated by another user). So, in these last cases, the committing transaction rolls back.

Optimistic concurrency control is based on the [Old Function](https://wiki.genexus.com/commwiki/wiki?8472,,). When a record is confirmed, the "old" values for all attributes are compared with current database values; if one value does not match, an error is displayed: "*Table was changed*", which means that another user modified the record since the time you get the values.

### [Notes](#Notes)

* Only the attributes present in the Transaction structure are taken into account. In other words, if there are [Parallel Transactions](https://wiki.genexus.com/commwiki/wiki?20209) with more attributes, they are not checked.
* This mechanism does not apply to Blob based attributes (Image,Video,Audio),  Longvarchar, and [Additive Attributes](https://wiki.genexus.com/commwiki/wiki?2006,,).


|  |
| --- |
| **Backlinks** |
| [Toc:Concurrency control](https://wiki.genexus.com/commwiki/wiki?45563) | [Pseudo Conversational Dialog Property](https://wiki.genexus.com/commwiki/wiki?13998) |

---
