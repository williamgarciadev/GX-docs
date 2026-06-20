---
title: "Terminate End Event in BPD"
source_id: 12316
source_url: https://wiki.genexus.com/commwiki/wiki?12316
genexus_version: "18"
---

# Terminate End Event in BPD

Cause the immediate cessation of the Process instance at its current level and for any Sub-Process, but it will not terminate a higher-level parent Process.

### [Symbol](#Symbol)

`[imagen omitida: wiki id 12317]`

### [Description](#Description)

When the Terminate event is reached, it causes the current thread and all other active threads to end immediately, regardless of their respective states.

### [Example](#Example)

The following example shows how this event is often used. There are two parallel paths. The upper is effectively an infinite loop, and when the lower reaches the Terminate event, the work of the upper path will be stopped, thereby stopping the infinite loop too.

`[imagen omitida: wiki id 12338]`

### [Scope](#Scope)

**Objects:** [Business Process Diagram](https://wiki.genexus.com/commwiki/wiki?11423,,)

### [See Also](#See+Also)

[None End Event](https://wiki.genexus.com/commwiki/wiki?12307)

[Signal End Event](https://wiki.genexus.com/commwiki/wiki?12337)

[Error End Event](https://wiki.genexus.com/commwiki/wiki?24840)


|  |
| --- |
| **Backlinks** |
| [BPD End Events](https://wiki.genexus.com/commwiki/wiki?17271) | [Error End Event in BPD](https://wiki.genexus.com/commwiki/wiki?24840) | [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |
| [None End Event in BPD](https://wiki.genexus.com/commwiki/wiki?12307) | [Signal End Event in BPD](https://wiki.genexus.com/commwiki/wiki?12337) |

---
