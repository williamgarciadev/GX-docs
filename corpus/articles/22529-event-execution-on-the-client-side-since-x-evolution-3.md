---
title: "Event execution on the client side since X Evolution 3"
source_id: 22529
source_url: https://wiki.genexus.com/commwiki/wiki?22529
genexus_version: "18"
---

# Event execution on the client side since X Evolution 3

In versions prior to [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,) the user events which do not need to perform actions in the server are executed in the client (in the browser).

In [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,) more commands are executed client side, not only those which do not need to connect to the server.

We call client side events in this context, to the events which are executed using a javascript routine that executes in the client (and the other part executes in the server), but the page does not refresh at all, and the execution is done asynchronously.

For those events that all the lines of code are executed client side, the entire event is executed in the client. This changes the behavior of the event so it does not execute a Refresh of the entire page, as is characteristic of client-side events.

Note that this is independent from [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) because when Web User experience= Smooth, all the events are executed client side.

### [1. Creation and Refresh of web components](#1.+Creation+and+Refresh+of+web+components)

In GeneXus Evolution 3, the [web components](https://wiki.genexus.com/commwiki/wiki?1864) creation and refresh is also executed client-side. This implies that if a user event only includes the creation of a web component or the refresh of a web component, this event is executed in the client. The result is that the corresponding web component is loaded or refreshed but the container object does not execute Start, Refresh or Load Events.

More specifically, if you have the following code, it does not force a full refresh of the page, only the WebComponent1 refreshes.

```
Event "CreateWebComponent"
    //Here code that also executes client side
    webcomp1.object = WebComponent1.create(&param1,&param2) //webcomp1 is a Web Component control
EndEvent
```

or

```
Event "RefreshWebComponent"
    //Here code that also executes client side
    WebComponent1.Refresh()
EndEvent
```

### [2. For Each Line Command](#2.+For+Each+Line+Command)

In GeneXus Evolution 3, the [For Each Line command](https://wiki.genexus.com/commwiki/wiki?8605) is executed client-side as long as the code inside the command is executed client-side. The event which includes the command is executed client-side if all the code can be executed that way.

In summary, the following commands are executed client-side in GeneXus Evolution 3:

* [For Each Line command](https://wiki.genexus.com/commwiki/wiki?8605)
* [<Webcomp><webcomp>.Refresh](https://wiki.genexus.com/commwiki/wiki?22579)</webcomp>
* <Webcomp>.Create

Note that this functionality is independent from [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449).

### [Note:](#Note%3A)

The Enter event in web panels in GeneXus Evolution 3 is considered as a user event.


|  |
| --- |
| **Backlinks** |
| [External Objects for Javascript](https://wiki.genexus.com/commwiki/wiki?31064) |
| [How to implement a dictionary data type using JS and server side code](https://wiki.genexus.com/commwiki/wiki?31066) | [HowTo:Develop a messaging web page](https://wiki.genexus.com/commwiki/wiki?22527) | [Refresh Web Component command](https://wiki.genexus.com/commwiki/wiki?22579) |

---
