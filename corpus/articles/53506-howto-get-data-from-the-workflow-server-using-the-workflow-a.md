---
title: "HowTo: Get data from the Workflow Server using the Workflow API"
source_id: 53506
source_url: https://wiki.genexus.com/commwiki/wiki?53506
genexus_version: "18"
---

# HowTo: Get data from the Workflow Server using the Workflow API

This article describes how to get data from the Workflow Server using the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

With the Workflow Server data type, you can list several workflow objects of your app: process definitions, activities, business events, calendars, process instances, and workitems.

For example, you can get a list of the workitems and display it in a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) [Grid](https://wiki.genexus.com/commwiki/wiki?24817) by defining and executing the following code:

`[imagen omitida: wiki id 53514]`

```
Event Start
    &WorkflowServer.connect('<UserName>','<Password>')
Endevent

Event Grid.Refresh
    &WorkflowWorkitems=&WorkflowServer.ListWorkitemsOrderBy(&WorkflowFilter, WorkflowOrder.CREATED_ASC)
EndEvent

Event Grid.Load    
    For &WorkflowWorkitem in &WorkflowWorkitems
        &WorkflowWorkitemId = &WorkflowWorkitem.Id
        &WorkflowActivityName = &WorkflowWorkitem.Activity.Name
        &WorkflowWorkitemState = &WorkflowWorkitem.State.Substring(&WorkflowWorkitem.State.LastIndexOf(!".")+1, 10)
        &WorkflowSubject = &WorkflowWorkitem.ProcessInstance.Subject
        &WorkflowUserName = &WorkflowWorkitem.Participant.Name
        &Created = &WorkflowWorkitem.Created
        Grid.Load()
    Endfor
EndEvent
```

Where the data type variables are as follows:

```
&WorkflowServer – WorkflowServer
&WorkflowFilter – WorkflowFilter
&WorkflowWorkitems – WorkflowWorkitem (Collection)
&WorkflowWorkitem – WorkflowWorkitem
```

It is possible to get a list of other objects in a similar way; read more in [Workflow Server Data Type](https://wiki.genexus.com/commwiki/wiki?11671).

You can also get a specific object with the following code:

```
&WorkflowServer.Connect(<UserName>,<Password>)
&WorkflowWorkitem = &WorkflowServer.GetWorkitemById(&WorkitemId)
```

Where the data type variables are as follows:

```
&WorkflowServer – WorkflowServer
&WorkflowWorkitem – WorkflowWorkitem
&WorkitemId – WorkflowWorkItemId
```

It is also possible to get a list of other objects in a similar way; read more in [Workflow Server Data Type](https://wiki.genexus.com/commwiki/wiki?11671).

### [See Also](#See+Also)

[Workflow API](https://wiki.genexus.com/commwiki/wiki?51350)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
