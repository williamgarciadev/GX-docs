---
title: "Update behavior property"
source_id: 31158
source_url: https://wiki.genexus.com/commwiki/wiki?31158
genexus_version: "18"
---

# Update behavior property

Update behavior is a Team Development property which allows determining what to do if the [Update operation](https://wiki.genexus.com/commwiki/wiki?10627) fails: keep those objects which were successfully Updated or make a [Revert Operation](https://wiki.genexus.com/commwiki/wiki?17480,,) of the entire Update.

This property attempts to solve, for example, the following problem:

A user has a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) synchronised with a GeneXus Server instance and other user makes a huge [Commit](https://wiki.genexus.com/commwiki/wiki?10626) to the same GeneXus Server instance.

The first user makes an Update of **all** the things the other user had committed. **If for some reason, the Update fails for any object, the entire Update fails, making a** [Revert Operation](https://wiki.genexus.com/commwiki/wiki?17480,,) **in those objects which were successfully Updated and Merged.**

### [Values](#Values)

|  |  |
| --- | --- |
| **Values** | **Description** |
| **Fail on errors** | The entire Update fails if any object fails. This is the default property value. |
| **Continue on errors** | The Update will be successful for those objects which were Updated correctly and will fail only for those objects which weren't. |

### [Availability](#Availability)

The Update behavior property it's available in the Team Development node of the Tool Tab at the [GeneXus IDE](https://wiki.genexus.com/commwiki/wiki?5272) (Tools -> Options -> Team Development).

`[imagen omitida: wiki id 31176]`


|  |
| --- |
| **Backlinks** |
| [Update From GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10627) | [Warn When Adding Or Removing Objects From Selection Property](https://wiki.genexus.com/commwiki/wiki?21078) |

---
