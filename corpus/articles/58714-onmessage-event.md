---
title: "OnMessage event"
source_id: 58714
source_url: https://wiki.genexus.com/commwiki/wiki?58714
genexus_version: "18"
---

# OnMessage event

Defines the action to be performed when a web notification is received.

### [Syntax](#Syntax)

Event OnMessage(&VbleBasedOnNotificationInfoSDT)  
        *Event\_code*  
EndEvent

**Where:**

*&VbleBasedOnNotificationInfoSDT*  
Variable based on the "NotificationInfo" [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021).

*Event\_code*  
    Code defined inside the event to process the info received in*&VbleBasedOnNotificationInfoSDT*.

### [Scope](#Scope)

**Objects:**[Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

By using the [Server.Socket external object](https://wiki.genexus.com/commwiki/wiki?22442), it is possible to send information from the server to a client (or all of them) without being requested by the client. These are silent notifications received on the client side.

Thus, when a web notification is received on the client side, the OnMessage Event is executed receiving by parameter a variable based on the "NotificationInfo" SDT:

`[imagen omitida: wiki id 58717]`

Inside this event, the received information must be processed as you consider convenient.

For example, consider a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) to manage hotel reservations.

Suppose that when a hotel reservation is inserted, all the users viewing that hotel should receive a notification alerting that someone has made a reservation.

On the server side, after loading the SDT variable, the broadcast method must be executed to send the notification to all users.

On the client side ([Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) or [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)), inside the OnMessage event, you have to enter the code to compare if the **Id** SDT member (the reserved hotel) matches one of the shown hotels to display a message.

### [See Also](#See+Also)

[Server.Socket external object](https://wiki.genexus.com/commwiki/wiki?22442)


|  |
| --- |
| **Backlinks** |
| [Events in Transactions](https://wiki.genexus.com/commwiki/wiki?8042) | [Events in Web Panels](https://wiki.genexus.com/commwiki/wiki?8178) |

---
