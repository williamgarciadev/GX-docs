---
title: "GXflow Inbox"
source_id: 7465
source_url: https://wiki.genexus.com/commwiki/wiki?7465
genexus_version: "18"
---

# GXflow Inbox

The Inbox allows the user to visualize and manage the list of his pending tasks. The following figure shows the Inbox Grid interface:

`[imagen omitida: wiki id 52247]`

In the following sections, you will find a description of the different components of this application.

### [Actions](#Actions)

The following button allows you to perform some actions over the workitems in the grid.

* **New**: The New button allows the user to start a new process and enables him to execute any task of the process. The user will visualize the following dialog where he can select a process to start and optionally type the process subject:

`[imagen omitida: wiki id 52248]`

* **Execute**: The Execute button allows the user to execute the task in its row. If the task is new, the execute button executes two actions automatically: take and execute the task. And if the task is assigned, it only executes the task.
* **Send**: The user must press the send button when a task can be completed (it has already been executed).
* **History**: By clicking on the history button, the user can access the [history of the process](https://wiki.genexus.com/commwiki/wiki?11936) the task belongs to.
* **Preview**: Tasks may have associated preview applications. The objective of this application is to show specific information on the different tasks so that the user can decide whether he must take a specific task or not. If a task has an associated preview application, the user will be able to access the preview application. If a task has an associated preview application, you will be able to press this button. By clicking the button, the user will be able to access the preview application.
* **Delegate**: This option allows the user to delegate a task to another system user or role. It is also possible to delegate a task with return, if this option is activated when a user completes a task that was delegated to him with return, the task returns to the Inbox of the User that delegated it. The latter will be the user that will complete the task definitely.

`[imagen omitida: wiki id 52249]`

* **Collaborate**: This feature allows a group of users to simultaneously take part in performing a task. This implies that when a user completes a workitem from the task, he will be able to choose a group of collaborator users. Then, all collaborator users will be able to view the workitem in their inboxes and execute it, but only the user who took that workitem first will be able to complete it and assign\unassign users.

`[imagen omitida: wiki id 52250]`

* **Comments**: Some tasks may require the user to enter comments before they are completed. In this case, when the user completes the task, such as by clicking this button, the following dialog will be displayed for the user to enter his comments:

`[imagen omitida: wiki id 52251]`

* **Documents:** It allows the user do actions with documents, if it is allowed in the task.
* **Take**: It allows the user to take a group of tasks that have not been assigned to any user yet. If the task does not allow delegation or collaboration or does not allow documents to be added, this error dialog will appear:

`[imagen omitida: wiki id 52252]`

### [Process Instances Grid](#Process+Instances+Grid)

This grid has the following options:

`[imagen omitida: wiki id 52012]` It allows selecting the columns wanted to be visible.

`[imagen omitida: wiki id 52013]` It allows refreshing the grid.

It is possible to sort some columns by clicking on their title.

This grid consists of the following columns:

**Priority**: The column represented by the priority icon shows each task priority. The following options are used to indicate the priority:

* High priority
* Low priority
* If no icon is shown, the task priority is normal.

**Warning**: Some tasks may have a deadline to be completed. Through this column the user can visualize the tasks with upcoming deadlines. The presence of the deadline icon in this column indicates that the corresponding task is near to reach its deadline.

**Work with documents**: Some tasks may have to work with documents to be completed. The presence of the document icon in this column indicates that the corresponding task has associated documents.

**Collaborators**: It indicates that other users are collaborating with the task.

**Comments**: It indicates that the task has comments associated, currently not availabe if there are tasks in the inbox for performance reasons.

**Id**: Process Id.

**Subject**: Process Instance subject.

**Process Instance Id**: Process Instance Id.

**Process Definition**: Process Definition name.

**Activity**: Activity Name.

**State**: Task current status. The possible statuses are the following:

* Assigned: the task is assigned to a user.
* Quitted: the process the task belongs to was quitted.
* Completed: the task was already completed.
* Delegated: the task was delegated to another user.
* Overdue: the task had a deadline to be completed and this deadline was already reached.
* Exited: the user has exited the task.
* In process: the task is being processed by the user to whom it is assigned.
* New: the task has not been assigned to any user yet.
* Suspended: the task is suspended because the process the task belongs to has been suspended. This implies that the users will not be able to work with the task until the process starts again.
* Finished: the process the task belongs to has been finished because the term for its execution has expired.

**Created**: Process Instance date create.

**Deadline**: Deadline task.

**Execute:** It allows to execute the task.

**Send:** It allows to send the task.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [GXflow Desktop](https://wiki.genexus.com/commwiki/wiki?17852) | [GXflow Entry Point User Control](https://wiki.genexus.com/commwiki/wiki?24184) |
| [GXflow Software Requirements](https://wiki.genexus.com/commwiki/wiki?18393) | [GXflow Software Requirements (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55579) | [HowTo: Use GXflow Entry Point User Control](https://wiki.genexus.com/commwiki/wiki?10721) |
| [On assignment change property](https://wiki.genexus.com/commwiki/wiki?11476) |

---
