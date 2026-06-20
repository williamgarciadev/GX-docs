---
title: "Cancel Intermediate Event in BPD"
source_id: 18058
source_url: https://wiki.genexus.com/commwiki/wiki?18058
genexus_version: "18"
---

# Cancel Intermediate Event in BPD

This event indicates that an embedded sub-process was canceled.

### [Symbol](#Symbol)

`[imagen omitida: wiki id 50730]`

### [Description](#Description)

There are two types of Cancel Intermediate Events: *throwing*and *catching*.

Only when it is a catch event, it can be attached to an embedded sub-process, if the sub-process is canceled, the flow can continue down the path indicated by this event.

While if it is a throw event, its behavior will be similar to the [Cancel End Event](https://wiki.genexus.com/commwiki/wiki?50732), but it will not end the sub-process.

### [Scope](#Scope)

**Objects:** [Business Process Diagram](https://wiki.genexus.com/commwiki/wiki?16486)

### [See Also](#See+Also)

[Cancel End Event](https://wiki.genexus.com/commwiki/wiki?50732)

[Compensate Intermediate Event](https://wiki.genexus.com/commwiki/wiki?18060)


|  |
| --- |
| **Backlinks** |
| [BPD Intermediate Events](https://wiki.genexus.com/commwiki/wiki?17270) | [Cancel End Event in BPD](https://wiki.genexus.com/commwiki/wiki?50732) | [Compensate End Event in BPD](https://wiki.genexus.com/commwiki/wiki?50736) |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
