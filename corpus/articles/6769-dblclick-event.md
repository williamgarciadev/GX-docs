---
title: "DblClick event"
source_id: 6769
source_url: https://wiki.genexus.com/commwiki/wiki?6769
genexus_version: "18"
---

# DblClick event

Occurs when the user double-clicks on a control.

### Syntax

*Control*.**DblClick**

#### Where:

*Control*  
    is the name of a control inserted in the form.

### Example

```
Event Photo.DblClick 
    ShowCustomer.Call(CustomerCode)
EndEvent
```

 In this example, when the user double-clicks on a bitmap containing the client’s photo, a web panel that displays the client’s information is called.

### Scope

|  |  |
| --- | --- |
| **Objects** | [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) |
| **Controls** | Dynamic List Boxes, Edits, , Images, List Boxes, Text Blocks |
| **Languages** | .Net, Java, Ruby |
| **Interfaces** | Web |
|  |  |


|  |
| --- |
| **Backlinks** |
| [Category:Control Events](https://wiki.genexus.com/commwiki/wiki?24271) | [Events in Transactions](https://wiki.genexus.com/commwiki/wiki?8042) |

---
