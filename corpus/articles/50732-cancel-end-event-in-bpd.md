---
title: "Cancel End Event in BPD"
source_id: 50732
source_url: https://wiki.genexus.com/commwiki/wiki?50732
genexus_version: "18"
---

# Cancel End Event in BPD

It indicates that an embedded subprocess needs to be rolled back.

### [Symbol](#Symbol)

`[imagen omitida: wiki id 50731]`

### [Description](#Description)

When this event is reached, it causes the current thread and all other active threads to end immediately, regardless of their respective states.

It is only possible to attach a [Cancel Intermediate Event](https://wiki.genexus.com/commwiki/wiki?18058) to the embedded subprocess, so once the subprocess is undone, this enables the flow to continue down the path indicated by this event.

To do a rollback you need to associate each activity with a [Compensate Intermediate Event](https://wiki.genexus.com/commwiki/wiki?18060).

### [Example](#Example)

The following example shows how the Cancel End Event is usually used with Error and Compensate events. If an error occurs due to a lack of availability for any reservation, the flow moves down to a Cancel End Event. This will activate the rollback process and any reservation activity that has been completed will be undone. Note that tasks are undone in the reverse order in which they were completed.

`[imagen omitida: wiki id 50752]`

### [Scope](#Scope)

**Objects:** [Business Process Diagram](https://wiki.genexus.com/commwiki/wiki?11423,,)

### [See Also](#See+Also)

[Compensate Intermediate Event](https://wiki.genexus.com/commwiki/wiki?18060)  
[Cancel Intermediate Event](https://wiki.genexus.com/commwiki/wiki?18058)  
[Error Intermediate Event in BPD](https://wiki.genexus.com/commwiki/wiki?18059)  
[Error Handling in BPD](https://wiki.genexus.com/commwiki/wiki?24922)

####


|  |
| --- |
| **Backlinks** |
| [BPD End Events](https://wiki.genexus.com/commwiki/wiki?17271) | [Cancel Intermediate Event in BPD](https://wiki.genexus.com/commwiki/wiki?18058) | [Compensate End Event in BPD](https://wiki.genexus.com/commwiki/wiki?50736) |
| [Compensate Intermediate Event in BPD](https://wiki.genexus.com/commwiki/wiki?18060) | [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
