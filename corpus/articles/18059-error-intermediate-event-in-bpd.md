---
title: "Error Intermediate Event in BPD"
source_id: 18059
source_url: https://wiki.genexus.com/commwiki/wiki?18059
genexus_version: "18"
---

# Error Intermediate Event in BPD

For managing error occurrences during the execution of a certain activity or at a certain point of a process flow.

### [Symbol](#Symbol)

`[imagen omitida: wiki id 19988]`

### [Description](#Description)

This event can only be associated with one activity and must lead to an alternative path when it captures an error.

### [Scope](#Scope)

Objects: [Business Process Diagram](https://wiki.genexus.com/commwiki/wiki?16486)

### [Example](#Example)

This case shows an *Error Intermediate Event* associated with task 'A'.

When the error occurs (Code = 1), the task 'B' will be executed, otherwise, the process is finished.

`[imagen omitida: wiki id 39521]`

This is a code example to force the error on Task 'A':

```
Event 'Error'
    &WorkflowContext.Workitem.ThrowError('1')
    commit
    return    
Endevent
```

### [See Also](#See+Also)

[Signal Event](https://wiki.genexus.com/commwiki/wiki?12196)  
[Timer Event](https://wiki.genexus.com/commwiki/wiki?12194)  
[Conditional Event](https://wiki.genexus.com/commwiki/wiki?12300)


|  |
| --- |
| **Backlinks** |
| [BPD Intermediate Events](https://wiki.genexus.com/commwiki/wiki?17270) | [Cancel End Event in BPD](https://wiki.genexus.com/commwiki/wiki?50732) | [Compensate Intermediate Event in BPD](https://wiki.genexus.com/commwiki/wiki?18060) |
| [Error End Event in BPD](https://wiki.genexus.com/commwiki/wiki?24840) | [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
