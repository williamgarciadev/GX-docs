---
title: "Exit event"
source_id: 8046
source_url: https://wiki.genexus.com/commwiki/wiki?8046
genexus_version: "18"
---

# Exit event

This event is activated after the user exits the object. Inside it, you can define actions that will be executed at the end of the object execution.

### [Syntax](#Syntax)

Event Exit  
        *Event\_code*  
EndEvent

**Where:**

*Event\_code*  
    Code associated with the event.

### [Scope](#Scope)

**Objects:**

[Transaction](https://wiki.genexus.com/commwiki/wiki?1908)

### [Description](#Description)

This event takes place after the user exits the object (by closing it) or when the return command is executed.

In this event you may, for example, call a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) when the Transaction is almost closed. Take into account that you don't have attribute values to send as parameters. Variables (that do not belong to a nested level) still maintain their values.

### [Sample](#Sample)

```
Event Exit
      msg('You are leaving this screen. Good bye!')
EndEvent
```


|  |
| --- |
| **Backlinks** |
| [Events in Transactions](https://wiki.genexus.com/commwiki/wiki?8042) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [Prompt rule](https://wiki.genexus.com/commwiki/wiki?6863) |

---
