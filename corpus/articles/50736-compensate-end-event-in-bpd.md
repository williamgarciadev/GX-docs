---
title: "Compensate End Event in BPD"
source_id: 50736
source_url: https://wiki.genexus.com/commwiki/wiki?50736
genexus_version: "18"
---

# Compensate End Event in BPD

It allows indicating that an activity must be compensated. It happens when a subprocess is canceled and its activities need to be rolled back.

### [Symbol](#Symbol)

`[imagen omitida: wiki id 50735]`

### [Description](#Description)

The activity to be compensated must be identified with an event attribute–BPMN doesn’t specify which one should be used. This activity must be included in the same process as the Compensate End Event; in addition, it must have an attached [Compensate Intermediate Event](https://wiki.genexus.com/commwiki/wiki?18060). If the activity to compensate is not specified, all the activities that have been successfully completed and have an attached compensation event will be compensated.

### [Example](#Example)

The figure below shows an example of this modeling pattern. In this case, an error in the Charge Credit Card task will activate the Compensate End Event, and the activities with a Compensate Intermediate Event attached will be rolled back.

`[imagen omitida: wiki id 50753]`

### [Scope](#Scope)

Objects: [Business Process Diagram](https://wiki.genexus.com/commwiki/wiki?16486)

### [See Also](#See+Also)

[Compensate Intermediate Event](https://wiki.genexus.com/commwiki/wiki?18060)  
[Cancel End Event](https://wiki.genexus.com/commwiki/wiki?50732)  
[Error End Event in BPD](https://wiki.genexus.com/commwiki/wiki?24840)  
[Cancel Intermediate Event](https://wiki.genexus.com/commwiki/wiki?18058)


|  |
| --- |
| **Backlinks** |
| [BPD End Events](https://wiki.genexus.com/commwiki/wiki?17271) | [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
