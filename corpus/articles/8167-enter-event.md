---
title: "Enter event"
source_id: 8167
source_url: https://wiki.genexus.com/commwiki/wiki?8167
genexus_version: "18"
---

# Enter event

To define an action that will be executed after pressing Enter or clicking the Confirm button or associated control.

### Syntax

Event Enter  
*Event\_code*  
EndEvent

**Where:**

*Event\_code*   
     Code associated with the event.

### Description

This event occurs after pressing Enter or clicking the Confirm button or the control associated with the event.

While this event is being executed, only the attributes and variables of the grid appearing in the form and those defined in the Hidden rule and the fixed attribute parameters are available for query.

#### Win interface

The associated controls may only be buttons.

#### Web interface

The associated controls may be buttons, images, text blocks and read-only edit boxes.

### Example

In the case of a Work Panel displaying information about Clients, if we want to allow the user to modify this information, when the user presses ENTER while positioned over one of the clients we call the Client's Transaction. In order to do that, we have to define the following:

```
Event Enter
    Client.Call(ClientCode)
EndEvent
```

### Scope

|  |  |
| --- | --- |
| **Objects** | [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916), [Work Panel object](https://wiki.genexus.com/commwiki/wiki?7387,,) |
| **Interfaces** | Win, Web |


|  |
| --- |
| **Backlinks** |
| [Allow Selection property](https://wiki.genexus.com/commwiki/wiki?8680) | [Web Panels events](https://wiki.genexus.com/commwiki/wiki?8178) |

---
