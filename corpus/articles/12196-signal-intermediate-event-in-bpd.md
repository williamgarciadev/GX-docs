---
title: "Signal Intermediate Event in BPD"
source_id: 12196
source_url: https://wiki.genexus.com/commwiki/wiki?12196
genexus_version: "18"
---

# Signal Intermediate Event in BPD

It indicates that the process is triggered when a signal is detected. This signal was broadcast communication from a business participant or another process.

### [Symbol](#Symbol)

`[imagen omitida: wiki id 12296]`

### [Description](#Description)

There are two types of Signal Intermediate events: *throwing* and *catching*. This is a consequence from a trigger which is a signal what can broadcast or receive.

Sign Event can operate across Proccess levels. For example, a Signal Event could trigger status reports to a customer, indicating that the process had reached and agreed milestone.

### [Example](#Example)

When executing **A, B**and**C**are created. Then, if you complete **B,** the process waits until it receives a signal called **TestSignalEvent.**So, completing the **C**task, the **D**will be created because the signal was thrown and the intermediate signal catch it.

Note that both signal events have the same name.

`[imagen omitida: wiki id 50694]`

### [Scope](#Scope)

**Objects:** [Business Process Diagram](https://wiki.genexus.com/commwiki/wiki?11423,,)

### [See Also](#See+Also)

[None Event](https://wiki.genexus.com/commwiki/wiki?12193)  
[Time Event](https://wiki.genexus.com/commwiki/wiki?12194)  
[Conditional Event](https://wiki.genexus.com/commwiki/wiki?12300)


|  |
| --- |
| **Backlinks** |
| [BPD Intermediate Events](https://wiki.genexus.com/commwiki/wiki?17270) | [Conditional Intermediate Event in BPD](https://wiki.genexus.com/commwiki/wiki?12300) | [Error Intermediate Event in BPD](https://wiki.genexus.com/commwiki/wiki?18059) |
| [Event Gateway](https://wiki.genexus.com/commwiki/wiki?17504) | [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [Link Intermediate Event in BPD](https://wiki.genexus.com/commwiki/wiki?18061) | [None Intermediate Event in BPD](https://wiki.genexus.com/commwiki/wiki?12193) |
| [Workflow Server Data Type](https://wiki.genexus.com/commwiki/wiki?11671) |

---
