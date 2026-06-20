---
title: "IsValid event"
source_id: 8049
source_url: https://wiki.genexus.com/commwiki/wiki?8049
genexus_version: "18"
---

# IsValid event

It occurs when the field entered is valid. GeneXus rules, referential integrity, etc. are triggered **before** this event.

### Syntax

**Event** *Control***.IsValid**  
*Event\_code*  
**EndEvent**  
  
**Where:**  
*Control*  
    Is the name of a control inserted in the form.

*Event\_code*  
      Code that is executed when event triggers

### Example

```
Event ClientId.IsValid
    ClientInfo.Call(ClientId)
EndEvent
```

In this example, when the user enters the Client’s identifier, another transaction to enter the client’s information is called when the client id entered is valid.

### Scope

|  |  |
| --- | --- |
| **Objects** | [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) |
| **Controls** | Check Boxes, Combo Boxes, Dynamic Combo Boxes, Dynamic List Boxes, Edits, Grid’s Columns, List Boxes, Radio Buttons |
| **Languages** | .NET, Java, Ruby, Visual FoxPro |
|  |  |

### More details

[IsValid Event for Web Applications](https://wiki.genexus.com/commwiki/wiki?6564)


|  |
| --- |
| **Backlinks** |
| [Category:Control Events](https://wiki.genexus.com/commwiki/wiki?24271) |

---
