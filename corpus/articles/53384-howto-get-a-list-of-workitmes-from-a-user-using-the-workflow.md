---
title: "HowTo: Get a list of Workitmes from a user using the Workflow API"
source_id: 53384
source_url: https://wiki.genexus.com/commwiki/wiki?53384
genexus_version: "18"
---

# HowTo: Get a list of Workitmes from a user using the Workflow API

Below is a description of how you can get a list of Workitmes from a user using the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

Define and execute the following code in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) that contains a grid:

`[imagen omitida: wiki id 53515]`

```
Event Start
    &WorkflowServer.Connect(&UserName, &UserPassword)
Endevent

Event Grid.Refresh
    &WorkflowUser = &WorkflowServer.ConnectedUser
    &WorkflowWorkitems=&WorkflowUser.GetWorklistOrderBy(&WorkflowFilter, WorkflowOrder.CREATED_ASC)
EndEvent

Event Grid.Load
    For &WorkflowWorkitem in &WorkflowWorkitems
        &WorkflowWorkitemId = &WorkflowWorkitem.Id
        &WorkflowActivityName = &WorkflowWorkitem.Activity.Name
        &WorkflowWorkitemState = Lower(&WorkflowWorkitem.State.Substring(&WorkflowWorkitem.State.LastIndexOf(!".")+1, 10))
        Do Case
            Case &WorkflowWorkitemState = !'ready'
                &WorkflowWorkitemState = 'Ready'
                &WorkflowWorkitemState.Class = styleclass:badge-success
            Case &WorkflowWorkitemState = !'in_process'
                &WorkflowWorkitemState = 'Working'
                &WorkflowWorkitemState.Class = styleclass:badge-warning
            Case &WorkflowWorkitemState = !'assigned'
                &WorkflowWorkitemState = 'Assigned'
                &WorkflowWorkitemState.Class = styleclass:badge-info
        Endcase    
        &WorkflowSubject = &WorkflowWorkitem.ProcessInstance.Subject
        &Created = &WorkflowWorkitem.Created
        Grid.Load()
    Endfor
EndEvent
```

Where the data types variables are the following:

```
&WorkflowServer – WorkflowServer
&WorkflowOrganizationalModel – WorkflowOrganizationalModel
&WorkflowUser – WorkflowUser
&WorkflowWorkitem – WorkflowWorkitem
&WorkflowWorkitems – WorkflowWorkitem (collection)
&WorkflowFilter – WorkflowFilter
&WorkflowWorkitemId – WorkflowWorkitemId
&WorkflowActivityName – WorkflowActivityName
&WorkflowWorkitemState – Character(20)
&WorkflowSubject – WorkflowSubject
&Created – DateTime
&UserName – Character(100)
&UserPassword – Character(30)
```

For further information about the Workflow API, go to [API](https://wiki.genexus.com/commwiki/wiki?51350).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
