---
title: "HowTo: Assign a GXflow task with relevant data"
source_id: 51447
source_url: https://wiki.genexus.com/commwiki/wiki?51447
genexus_version: "18"
---

# HowTo: Assign a GXflow task with relevant data

This article explains how to automatically assign a task with relevant data.

To do this, define a relevant data value and store in it the ID of the user you want to assign to the task; note that it must be of character(100) data type. The task to be assigned must have this relevant data associated in its [Assign from a user in a relevant data property](https://wiki.genexus.com/commwiki/wiki?11889). Once a Workitem associated with this task is created, it will be automatically assigned to the user with the ID stored in the relevant data.

This function doesn't check if the user role can be assigned to the task.

### [See Also](#See+Also)

[HowTo: Get and Set a Relevant Data Value](https://wiki.genexus.com/commwiki/wiki?11720)


|  |
| --- |
| **Backlinks** |
| [Assign from a user in a relevant data property](https://wiki.genexus.com/commwiki/wiki?11889) | [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
