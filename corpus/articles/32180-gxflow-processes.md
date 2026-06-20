---
title: "GXflow Processes"
source_id: 32180
source_url: https://wiki.genexus.com/commwiki/wiki?32180
genexus_version: "18"
---

# GXflow Processes

Through this application, the process administrator user can monitor and control the workflow processes.  
The following figure shows the Process application interface:

`[imagen omitida: wiki id 52253]`

### [Actions](#Actions)

* **Abort**: It allows quitting a group of active processes.
* **Reactivate**: It allows to reactivate a closed instance.
* **Suspend**: It allows suspending a group of processes that are in execution. This implies that the users will not be able to work with the tasks of these processes until their execution is resumed.
* **Resume**: It allows resuming the execution of a group of processes that were suspended.
* **History**: It allows to view the process history.
* **High Priority**: It allows to set a high priority to the process.
* **Low Priority**: It allows to set a low priority to the process.
* **Change Deadline**: It allows to change the deadline defined.
* **Organizational Units**: It allows to see the process organizational units.
* **Application Data**: It allows access a list with the current data of a specific process application data.
* **Comments**: It allows access the process comments.
* **Migrate to Active Version**: It allows to migrate a process instance to the active version.
* **Clean Workflow History**: It allows to choose the process to delete from the database using filters of dates and states.The deleted processes are those with a date prior to the one selected.  
  It is associated with the **apwfcleanhistory** program that can be executed through the command line and achieve the same effect.

### [Processes Grid](#Processes+Grid)

This grid has the following options:

`[imagen omitida: wiki id 52012]` It allows selecting the columns wanted to be visible.

`[imagen omitida: wiki id 52013]` It allows refreshing the grid.

It is possible to sort some columns by clicking on their title.

This grid has the following columns:

**Priority**: The column represented by the priority icon shows each task priority. The following options are used to indicate the priority:

* High priority
* Low priority
* If no icon is shown, the task priority is normal.

**Warning**: Some tasks may have a deadline to be completed. Through this column, the user can visualize the tasks with upcoming deadlines. The presence of the deadline icon in this column indicates that the corresponding task is near to reach its deadline.

**Documents**: The column represented with the clip icon indicates whether the task has associated documents or not. If it is so, the clip icon will be shown in this column. By clicking on this icon, the user accesses the Work with Documents application, which allows working with the documents associated to the task.

**Comments**: If a task has associated comments, the ballon icon is shown in this column. By clicking on the former icon a dialog will be displayed showing the comments associated to the task.

**Id:**Process Id.

**Subject**: Process Instance subject.

**Process**: Name of the process definition the process is based on.

**Version**: Process Definition version.

**State**: The possible statuses are the following:

* Not\_Initiated: the process was created but it has not been executed yet (the tasks have not been created yet).
* Suspended: the process was suspended. This implies that the users will not be able to execute the tasks associated to this process until the process execution is resumed.
* Executing: the process is in execution.
* Quitted: the process was quitted. This implies that the users will no longer be able to execute any task associated to this process.
* Completed: the process was completed normally. Every process task was completed.
* Finished: the process had a deadline to be completed and this deadline was reached.

**Owner**: Task assigned user.

**Created**: Process creation date.

**Ended**: Process finalization date. This column will appear in blank for those tasks that are still active.

**Duration**: Process instance duration.

**Abort:**It allows to abort the process.

**Reactivate:**It allows to reactivate the process.

**View History:**It shows the history of the process.

​​​​​


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [GXflow Process Manager](https://wiki.genexus.com/commwiki/wiki?17857) |
| [HowTo: Use GXflow Entry Point User Control](https://wiki.genexus.com/commwiki/wiki?10721) |

---
