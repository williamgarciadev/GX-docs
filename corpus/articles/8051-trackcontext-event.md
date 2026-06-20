---
title: "TrackContext event"
source_id: 8051
source_url: https://wiki.genexus.com/commwiki/wiki?8051
genexus_version: "18"
---

# TrackContext event

Web User Interfaces are context-sensitive. This means that, while the end user is moving the cursor (through attributes, variables, etc.), the TrackContext event can be triggered (depending on the received parameters) and you can take actions.

### [Syntax](#Syntax)

Event TrackContext (parameters)  
 *Event\_code*  
EndEvent

**Where:**

*Event\_code*   
    Code associated with the event.

*parameters*  
    They can only be variables.

### [Scope](#Scope)

**Objects:**[Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:**[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

It is possible to trigger events and take actions while the end user moves the cursor in a Web User Interface.

The TrackContext event is qualified by the parameters it receives. That is, you can have any number of TrackContext Events in the same object, that are differentiated by the parameters they receive.

### [Sample](#Sample)

Suppose a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) that is made up of several [Web Components](https://wiki.genexus.com/commwiki/wiki?1864).

You can trigger an event in one of the Web Components as soon as the end user changes his/her context information in another component (changes the focus to a control, or selects a grid line).

Basically, the web controls that you want to track changes on "subscribe" to an event which listens to the context changes of any other control.

Defining a TrackContext event, allows you to retrieve the context information and take the desired actions.

`[imagen omitida: wiki id 28575]`

`[imagen omitida: wiki id 28576]`

### [See Also](#See+Also)

[Context Sensitive User Interfaces](https://wiki.genexus.com/commwiki/wiki?5285)


|  |
| --- |
| **Backlinks** |
| [Events in Transactions](https://wiki.genexus.com/commwiki/wiki?8042) | [Events in Web Panels](https://wiki.genexus.com/commwiki/wiki?8178) | [Table of contents:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) |

---
