---
title: "Introduction to BPMN - Activities"
source_id: 24916
source_url: https://wiki.genexus.com/commwiki/wiki?24916
genexus_version: "18"
---

# Introduction to BPMN - Activities

They represent the work performed in a business process and are drawn as a rounded rectangle. An activity usually takes a certain time to be run and it will involve one or more resources from the organization. In addition, it will usually require a certain type of input data and will produce some type of output.

Activities are classified as atomic or compound. Atomic activities, which are called tasks, are the lowest level of detail represented in the diagram. Compound activities are called sub-processes and encapsulate a greater level of detail of the process.

Tasks

There are seven types of tasks:

* None: A generic or unidentified task. It is normally used in the initial stages of the modeling process.
* Manual: A non-automated task, that is to say, a task performed by a person outside the control of a workflow engine.
* Receive: It waits for the arrival of a message from a participant (another process). It is similar to the catch Message Event.
* Send: It sends a message to an external participant. It is similar to the throw Message Event.
* Script: It runs a script specified by the process modeler.
* Service: It connects to some sort of service, which can be a web service or an automated application.
* User: A typical workflow task where a user runs it with the assistance of a software application.

From the business analyst standpoint, the only core task type is None. The other types of tasks are intended for more advanced uses of BPMN.

Behavior

When the process flow reaches a task, a new instance of this task is generated. It remains in “list” status until all the requirements defined, such as data input, are met. When this happens, the task is moved to an “active” status.

Looping

This is another type of behavior that can be specified for a task. It allows defining a loop condition, without the need to include it explicitly in the diagram. The operation depends on [Loop Type](https://wiki.genexus.com/commwiki/wiki?11898)  chosen in the property of the same name.

Standard Task

When a task is assigned a loop condition, it is represented as shown below:

`[imagen omitida: wiki id 24924]`

There are two variants of looping:

* **While loop:**the condition is checked before running the task.
* **Until loop:**the condition is checked after running the task.

The specification of attributes over the task makes it possible to set the maximum number of loops. When this maximum number of loops is reached, it will end even when the condition is still met.

Multi-instance tasks

This type of behavior determines the number of times that a task will be performed. The condition is checked once and returns the number of instances that must be created. These instances can be executed in parallel or in sequence depending on the task attributes which are not visible in the diagram. In addition, attributes can be used to specify how these tasks converge after they are performed. The possible values are None, One, All or Complex and they are equal to using Gateways (read [Gateways](https://wiki.genexus.com/commwiki/wiki?24918)).

The tasks defined for this type of behavior are represented with three vertical lines in the lower half as shown below:

`[imagen omitida: wiki id 24925]`

Sub-processes

There are two graphical representations:

* **Collapsed:**it is represented in the same way as a task with the addition of a '+' sign in the lower half. Details on the sub-process are not displayed in the diagram; only a reference is made to the process.
* **Expanded:**it is represented with a rounded rectangle containing all the sub-process details.

The figure below shows both types of sub-processes:

`[imagen omitida: wiki id 24926]`

In addition, BPMN also makes another classification of sub-processes:

* Embedded: It is considered as part of the parent process and it can be reused by other processes. This implies that all the relevant details of the parent process are available for the sub-process with no need for mapping or translation. They can’t be started with trigger-type events (such as a timer), only with None Events (the basic start symbol with no associated semantics; it only marks the start point) because only the parent process decides when they should be started.
* Reusable: These processes can be reused in more than one parent process. Just like embedded processes, they must have a None Start Event because the parent process determines when the sub-process should be started. Since sub-processes of this type are independent they could serve as top-level processes. Therefore, they could also have other Start Events of trigger type (such as a timer or a condition event). There is no graphical difference between embedded and reusable sub-processes, but BPMN 2.0 is expected to introduce notation differences.

Just like with tasks, the parent process will connect to the sub-process with paths towards the boundary of the sub-process symbol. However, for expanded sub-processes, Start Events can be placed on the boundary of the sub-process. In this way, the parent process will connect different paths to each one of these events.

Once again, just as it happens with tasks, every time that the flow reaches a sub-process a new instance of the process is created.

[Go to the main article](https://wiki.genexus.com/commwiki/wiki?24913) -   [Return to the previous section](https://wiki.genexus.com/commwiki/wiki?24915) - [Go to the next section](https://wiki.genexus.com/commwiki/wiki?24917)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [Introduction to BPMN](https://wiki.genexus.com/commwiki/wiki?24913) |
| [Introduction to BPMN - Events](https://wiki.genexus.com/commwiki/wiki?24917) | [Introduction to BPMN - Overview](https://wiki.genexus.com/commwiki/wiki?24914) | [Introduction to BPMN - Process Categories](https://wiki.genexus.com/commwiki/wiki?24915) |

---
