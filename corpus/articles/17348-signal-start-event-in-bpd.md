---
title: "Signal Start Event in BPD"
source_id: 17348
source_url: https://wiki.genexus.com/commwiki/wiki?17348
genexus_version: "18"
---

# Signal Start Event in BPD

It indicates that the process is triggered when a signal is detected. This signal was broadcast communication from a business participant or another process.

### [Symbol](#Symbol)

`[imagen omitida: wiki id 12188]`

### [Description](#Description)

The trigger is a signal transmitted by another process. Signals have only one ID and are not sent to a predefined destination (broadcast). The Signals can operate within a process (for example, between a subprocess and its parent process) or among the processes of different participants.

### [Example](#Example)

The above picture provides an example where the first process throws a signal to start an "Accept Travel Voucher" process. This process will start when the signal is received and will evaluate the document for processing.

Note that both signal events have the same name.

`[imagen omitida: wiki id 12289]`

### [Scope](#Scope)

**Objects:** [Business Process Diagram](https://wiki.genexus.com/commwiki/wiki?16486)

### [See Also](#See+Also)

[None Start Event](https://wiki.genexus.com/commwiki/wiki?17347)

[Message Start Event](https://wiki.genexus.com/commwiki/wiki?12184)


|  |
| --- |
| **Backlinks** |
| [BPD Start Events](https://wiki.genexus.com/commwiki/wiki?17269) | [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [None Start Event in BPD](https://wiki.genexus.com/commwiki/wiki?17347) |

---
