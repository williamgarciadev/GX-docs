---
title: "Level Sentence"
source_id: 18742
source_url: https://wiki.genexus.com/commwiki/wiki?18742
genexus_version: "18"
---

# Level Sentence

Used in User Defined events for [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) to identify the level where the event is to be activated. It must be placed immediately after the Event command.

#### Syntax

Event '*UserEventName*' [*Key*]  
        [**Level** *att*]  
        *Event\_code*  
EndEvent

Where:  
*UserEventName*  
   Name of the user event.  
  
*Key*  
   Number of function key associated to the event. Optional.  
  
Level  
   Only to be used in transactions. Optional.  
  
*Att*  
   An atributte of the structure of the transaction. It indicates the associated level.  
  
*Event\_code*  
   Code associated to the event.

### Example

To view the details of a particular row belonging to the Invoices Transaction:

```
Event 'View Stock' 2
   Level ProductCode
   Vstock.Call(ProductCode)
EndEvent
```

Notice that LEVEL ensures that the event is activated when the code identifying the Product (ProductCod) has been entered (Invoice's detail lines level) and not at the start of the Invoices transaction (Invoice's header level).

### Scope

|  |  |
| --- | --- |
| **Objects** | [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) |
| **Interfaces** | Win |
|  |  |


|  |
| --- |
| **Backlinks** |
| [User defined event](https://wiki.genexus.com/commwiki/wiki?8044) |

---
