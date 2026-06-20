---
title: "Signal End Event in BPD"
source_id: 12337
source_url: https://wiki.genexus.com/commwiki/wiki?12337
genexus_version: "18"
---

# Signal End Event in BPD

It indicates that the end  of a process path results in the broadcast of a signal. When a token reaches this event, it triggers the broadcast before consuming the token.

### [Symbol](#Symbol)

`[imagen omitida: wiki id 12340]`

### [Example](#Example)

`[imagen omitida: wiki id 14243]`

When executing **A, B** and**D**are created. Then, if you complete **B,** the process waits until it receives a signal called **TestEndSignalEvent.** So, completing the **D** task, the **C** will be created because the signal was thrown and the intermediate signal catch it.

### [Scope](#Scope)

**Objects:** [Business Process Diagram](https://wiki.genexus.com/commwiki/wiki?11423,,)

### [See Also](#See+Also)

[None End Event](https://wiki.genexus.com/commwiki/wiki?12307)

[Terminate End Event](https://wiki.genexus.com/commwiki/wiki?12316)

[Error End Event](https://wiki.genexus.com/commwiki/wiki?24840)


|  |
| --- |
| **Backlinks** |
| [BPD End Events](https://wiki.genexus.com/commwiki/wiki?17271) | [Error End Event in BPD](https://wiki.genexus.com/commwiki/wiki?24840) | [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |
| [None End Event in BPD](https://wiki.genexus.com/commwiki/wiki?12307) | [Terminate End Event in BPD](https://wiki.genexus.com/commwiki/wiki?12316) |

---
