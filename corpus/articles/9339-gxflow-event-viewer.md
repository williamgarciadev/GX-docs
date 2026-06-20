---
title: "GXflow Event Viewer"
source_id: 9339
source_url: https://wiki.genexus.com/commwiki/wiki?9339
genexus_version: "18"
---

# GXflow Event Viewer

Through the Event Viewer, administrator users can visualize the events occurring in the workflow system and obtain specific information of each one of them. The following figure shows the Events Viewer interface:

`[imagen omitida: wiki id 52067]`

The following sections describe the different components making up this application.

### [Button Toolbar](#Button+Toolbar)

`[imagen omitida: wiki id 52068]`

* **Details**: It shows a dialog with event details:

`[imagen omitida: wiki id 52069]`

* **Target**: This is the object affected by the event. E.g.: it can be a new document, a new task, an application data, etc.  
  A link for some objects is enabled in this column that allows accessing a dialog containing specific information on the object.  
  In case the object is a task or process, the link will access the process history.

### [Event Grid](#Event+Grid)

The event grid shows the different events that occurred in the system. By default, only those events occurring in the current date will be shown, more events can be enable in [Event Handling](https://wiki.genexus.com/commwiki/wiki?10116).

* **Columns**: It allows selecting the columns wanted to be visible.
  + **Id**: Event Id
  + **Type**: Type of the event that occurred. It may be one of the following:
    - New Instance: a new process or task was created
    - Change of Data: change of the value of an application data
    - Change of Status: change of the status of a process or task
    - Change of Priority: change of the priority of a process or task
    - Change of Assignment: change of the assignment of a task
    - Warning: warning because a process or task is about to expire
    - Deadline: deadline of a process or task. It indicates that the process or task has expired.
    - Error: an error occurred, such as that a user typed his user or password wrongly on attempting to log into the system.
    - Unsatisfied condition: the evaluation of a condition produced an invalid result.
    - Unavailable resource: there are no resources (users) available to process the task.
    - External Event: an event external to the Workflow system occurred.
  + **Source**: GXflow client application where the event occurred.
  + **Target**: This is the object affected by the event. E.g.: it can be a new document, a new task, an application data, etc.  
    A link for some objects is enabled in this column that allows accessing a dialog containing specific information on the object.  
    In case the object is a task or process, the link will access the process history.
  + **User**: User that caused the event (if applicable).
* `[imagen omitida: wiki id 52012]` It allows selecting the columns wanted to be visible.
* `[imagen omitida: wiki id 52013]` It allows refreshing the grid.

For an overview of GXflow client, refer to the [GXflow Client General Structure](https://wiki.genexus.com/commwiki/wiki?17836) section.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [GXflow Client General Structure](https://wiki.genexus.com/commwiki/wiki?17836) |
| [HowTo: Use GXflow Entry Point User Control](https://wiki.genexus.com/commwiki/wiki?10721) |

---
