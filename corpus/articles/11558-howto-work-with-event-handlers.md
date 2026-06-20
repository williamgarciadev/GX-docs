---
title: "HowTo: Work With Event Handlers"
source_id: 11558
source_url: https://wiki.genexus.com/commwiki/wiki?11558
genexus_version: "18"
---

# HowTo: Work With Event Handlers

This document explains how to work with Event Handlers and provides a brief overview about it.

The event handlers allow defining the actions to be executed when specific events occur in the workflow system.

Specifically, for each event, you can associate a group of [Procedures](https://wiki.genexus.com/commwiki/wiki?6293) that will be executed when the event takes place. These Procedures are developed in GeneXus and must receive a specific parameter that represents the occurred event. See more about the requirements of each event type in [Event Handler procedure structure](https://wiki.genexus.com/commwiki/wiki?17393,,).

While modeling, you can associate events handlers in four levels: [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836), [Business Process](https://wiki.genexus.com/commwiki/wiki?48918), Task and Document. These levels of handlers association are described below.

### [Associating event handlers at Knowledge Base level](#Associating+event+handlers+at+Knowledge+Base+level)

When an event is associated with a handler at Knowledge Base level, this handler will be called whenever an event occurs, regardless in which process or task it occurs.

To associate a handler to an event in Business Process Diagram at knowledge base level, you must go to **Knowledge Base Properties > Workflow > Event Handling**.

`[imagen omitida: wiki id 52558]`

### [Associating event handlers at Business Process level](#Associating+event+handlers+at+Business+Process+level)

When an event is associated with a handler at Business Process level, this handler will be called whenever an event occurs in an instance of this process, regardless of the task it occurs in.

To associate event handlers at Business Process level, you must open the properties dialog of the business process in question.

`[imagen omitida: wiki id 52559]`

### [Associating event handlers at Task level](#Associating+event+handlers+at+Task+level)

When an event is associated to a handler at Task level, this handler will be called whenever an event occurs in an instance of this task.

To associate event handlers at Task level, you must open the properties dialog of the task in question.

`[imagen omitida: wiki id 52560]`

### [Associating events handlers at Document level](#Associating+events+handlers+at+Document+level)

It is also possible to associate events handlers to the [OnActionPerformed event](https://wiki.genexus.com/commwiki/wiki?11868) that occurs when executing an operation with a document.

To associate handlers to this type of events, you must access the documents dialog through the **Preferences > Workflow > Documents** option of the Knowledge Base Navigator. Then, you must select a document (to which you want to associate event handlers) and press the Events button to access the events dialog.

### [Configuration of preferences](#wiki%3F52561%2CEventHandling5_png%2C+Configuration+of+preferences)

After you have selected the properties at any level, to associate a Procedure with an event, you must open the Event Handlers dialog and select a Procedure.

`[imagen omitida: wiki id 52562]`

Once you have associated a Procedure with the Event, it is necessary to enable it in the GXflow client. To do this, go to **Server Settings > Advanced > Event Handling**.

`[imagen omitida: wiki id 52563]`

### [See Also](#See+Also)

[Event Handling Property](https://wiki.genexus.com/commwiki/wiki?10959,,)  
[Event Handler procedure structure](https://wiki.genexus.com/commwiki/wiki?17393,,)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [On action performed property](https://wiki.genexus.com/commwiki/wiki?11868) | [On assignment change property](https://wiki.genexus.com/commwiki/wiki?11476) |
| [On assignment change property (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55694) | [On data change property](https://wiki.genexus.com/commwiki/wiki?11754) | [On deadline property](https://wiki.genexus.com/commwiki/wiki?11477) |
| [On new instance property](https://wiki.genexus.com/commwiki/wiki?11479) | [On priority change property](https://wiki.genexus.com/commwiki/wiki?11480) | [On resource non available property](https://wiki.genexus.com/commwiki/wiki?11481) | [On state change property](https://wiki.genexus.com/commwiki/wiki?11483) |
| [On unsatisfied condition property](https://wiki.genexus.com/commwiki/wiki?11870) | [On warning property](https://wiki.genexus.com/commwiki/wiki?11478) |

---
