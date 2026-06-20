---
title: "Compensate Intermediate Event in BPD"
source_id: 18060
source_url: https://wiki.genexus.com/commwiki/wiki?18060
genexus_version: "18"
---

# Compensate Intermediate Event in BPD

This event is used for undoing activities in case a transaction subprocess has been canceled or needs rollback.

### [Symbol](#Symbol)

`[imagen omitida: wiki id 36351]`

### [Description](#Description)

It only can be attached to activities when it is a catching event. When it is a throwing event, it can be added to the normal flow process.

When the event is attached, it only can be associated with a Script Task, using association connectors –not sequence connectors.

### [Example](#Example)

In the below diagram, each activity with an Intermediate Compensate Event associated with a Script Task will be undone if an error is triggered.

`[imagen omitida: wiki id 50752]`

### [Scope](#Scope)

Objects: [Business Process Diagram](https://wiki.genexus.com/commwiki/wiki?16486)

### [See Also](#See+Also)

[Cancel End Event](https://wiki.genexus.com/commwiki/wiki?50732)

[Error Intermediate Event](https://wiki.genexus.com/commwiki/wiki?18059)


|  |
| --- |
| **Backlinks** |
| [BPD Intermediate Events](https://wiki.genexus.com/commwiki/wiki?17270) | [Cancel End Event in BPD](https://wiki.genexus.com/commwiki/wiki?50732) | [Cancel Intermediate Event in BPD](https://wiki.genexus.com/commwiki/wiki?18058) |
| [Compensate End Event in BPD](https://wiki.genexus.com/commwiki/wiki?50736) | [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
