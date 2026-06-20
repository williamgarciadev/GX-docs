---
title: "Introduction to BPMN - Events"
source_id: 24917
source_url: https://wiki.genexus.com/commwiki/wiki?24917
genexus_version: "18"
---

# Introduction to BPMN - Events

An event is something that happens while a process is running. They affect the process flow and usually have a trigger or a result. They can start, pause, interrupt or end a process flow.

An event is represented with a circle, and the border style indicates its type. The three types of events available are as follows:

* Start (thin narrow line)
* Intermediate (thin double line)
* End (thick single line)

In turn, each type is subdivided into other events which are represented with an icon displayed within the circle.

Start Events

Start Events show where a process can begin. There are different types of Start Events that allow you to indicate the different circumstances that can trigger the beginning of a process. These circumstances, such as the arrival of a message or a timer-based alarm, are called ‘triggers’.

Below is a description of the types of Start Events, which are classified as core and advanced.

Core Start Events

* **None:** a trigger is not specified (triggers are not mandatory; they can be specified later). They are mandatory in sub-processes.
* **Timer:** the trigger is a one-time or recurring date/time.
* **Message:**the trigger is a message that arrives from another business entity or participant (it must come from another Pool).
* **Signal:**the trigger is a signal transmitted by another process. Signals have only one ID and are not sent to a predefined destination (broadcast). Unlike messages, signals can operate within a process (for example, between a sub-process and its parent process) or among processes of different participants.

Advanced Start Events

* **Conditional:** the trigger is a conditional expression that must be met for the process to begin. Typically, conditions imply changes to the values of the process relevant data. They can be expressions in natural language or a formal language to be run with a workflow engine.
* **Multiple:** it defines two or more triggers that can be any combination of the above, and any of them will start the process.

A process can have more than one start event. In addition, start events are optional for top-level processes or sub-processes. In this case, the activities that don’t have predecessors will be the initial tasks.

The figure below shows the symbols used to represent each one of these events:

`[imagen omitida: wiki id 24985]`

Intermediate Events

They represent things that happen during the normal course of a process and usually take place between activities. They can interrupt the normal processing of an activity.

All the types of intermediate events can catch events, and some of them can also throw them. When a process flow reaches a *catch* event, the process stops until the expected event occurs. On the other hand, when the flow reaches a *throw* event, it is immediately triggered and the flow continues. The types of events that catch events are represented with an empty icon, and those that trigger events are represented with a filled icon. Intermediate events are as follows:

**Core Intermediate Events**

* **None:** (catching) – No trigger is specified.
* **Timer:** (catching) – The same as the timer start event.
* **Message:** (catching, throwing) – The trigger is a message sent to or received from another participant (Pool).
* **Signal:** (catching, throwing) – The trigger is a signal that is broadcast or received.

**Advanced Intermediate Events**

* **Error:**(catching) – It defines an event that usually interrupts the process or requires a correction.
* **Cancel:** (catching) – It is used to cancel a Transaction Sub-Process.
* **Compensation:** (catching, throwing) – It is used to set the behavior required to undo activities when a transaction sub-process is canceled or has to be undone (rollback).
* **Conditional:** (catching) – It defines a rule that must be met for the process to continue.
* **Link:** (catching, throwing) – It is used to create a "Go-To" visual mechanism to hide long flow sequences.
* **Multiple:** It defines two or more triggers that can be any combination of messages, timers, errors, conditions or signals.

The figure below shows the symbols used to represent *catching* Intermediate Events:

`[imagen omitida: wiki id 24986]`

The figure below shows the symbols used to represent *throwing* Intermediate Events:

*`[imagen omitida: wiki id 24987]`*

Interruption of Activities using Intermediate Events

Events can be attached to the boundary of an activity to model exceptions to the normal flow of the process. The attached event indicates that the task must be interrupted when the event is triggered. These types of events are always *catching* events. Both tasks and sub-processes are interrupted in the same way.

The types of events that can interrupt an activity are as follows:

* Timer
* Message
* Error
* Cancel
* Conditional
* Signal
* Multiple

Compensation events can also be attached to an activity even if they don’t interrupt it, because these events always occur after the task is completed.

**None Event**

As with Start Events, a trigger is not always required for an Intermediate Event. These events are used to document that certain activities have been completed or that the process has reached a certain milestone. The name of the Event can provide enough information for this purpose.

Timer Event

They are used to catch events that indicate that a time period has elapsed and can be used to model delays or deadlines.

Delays

They are modeled by inserting the Timer Event between activities. They can represent a specific date and time (e.g., wait until April 15 at 5pm), a relative date (e.g., wait 6 days) or a relative repetitive date (e.g., wait until next Monday at 8am). When the timer generates an alert, the process flow continues.

The element prior to a delay can be an activity, a gateway or another intermediate event.

If the event has a specific date that is in the past, the process is stopped indefinitely.

The figure below shows an example of how a delay is modeled:

`[imagen omitida: wiki id 24988]`

Deadlines

They are modeled by attaching the timer event to the activity. If the event occurs before the corresponding activity is completed, it is immediately interrupted and the flow continues down the path indicated by the event.

The figure below shows an example of how a deadline is modeled:

`[imagen omitida: wiki id 24989]`

BPMN 1.1 doesn’t allow for the modeling of the case where a deadline should occur without interrupting the task. To this end, we suggest using a pattern similar to the one shown below:

`[imagen omitida: wiki id 24990]`

BPMN 2.0 will include the ability to have intermediate events that don’t interrupt activities.

Message Event

They always operate between Pools. For a *catching* Message Event, if the message arrives before the flow reaches this element, the message is ignored and the flow is stopped until a new message arrives. They can also be attached to tasks.

Signal Event

It makes it possible to send or receive signals, which can be exchanged between across process levels (parent process and sub-processes, and vice versa) or between Pools. They are not designed for any specific entity. A *catching* Signal Event can catch a certain signal identified by its name or any signal.

If the Signal Event occurs before the process flow reaches the Signal Event symbol, the process is stopped until a new event arrives.

This type of events can be used as follows:

* Handling exceptions
* Connecting processes, indicating the start of a process after the end of another process
* Highlighting that a specific milestone has occurred
* Communication between processes; it is especially useful when parallel paths require synchronization.

The figure below shows an example of how the Signal Event is used:

`[imagen omitida: wiki id 24991]`

In the example, the first sub-process triggers two Signal Events: an intermediate event called 'Concepts Completed' and another one at the end with an end event that is called 'Text Edited' and will be described later. The second sub-process has a *catching* Signal Intermediate Event that will stop the process until the arrival of a 'Concepts Completed' signal. Note that a Signal Start Event is not used because it is a sub-process and therefore the start is determined by the parent process. This sub-process ends with the triggering of a Signal End Event called 'Cover completed'. In parallel to these sub-processes there is a waiting period for the arrival of the signals 'Text Edited' and 'Cover Completed'. The flow continues only after both signals are received.

Error Event

They are always *catch* events and are used attached to an activity. They indicate that the activity to which they are attached must be interrupted if an error occurs.  Errors are generated by applications or systems involved in the activity (transparent to the process).

Cancel Event

They are used to handle situations in which a transaction is canceled. They can only be attached to transaction sub-processes and for this reason they are always *catch* events. These events are triggered by Cancel End Events included in sub-processes.

Compensation Event

*Catch*Compensation Events can only be attached to activities. On the other hand, *throw*events are used in the normal flow of a process.

For more details about these events, read [Compensation and Transactions](https://wiki.genexus.com/commwiki/wiki?24922)

Conditional Event

The Conditional Event is used to model a situation in which the process waits for a condition to be met. This condition will usually involve the relevant data of the process. They can be used attached to a task, in the normal flow or as part of a gateway based on events (read [Gateways](https://wiki.genexus.com/commwiki/wiki?24918))

Link Event

They are always used in pairs, with a *source* (*throw*) and a*target (catch)*event*.*To ensure the pairing, both events must have the same label. Their objective is to create a virtual sequence flow and must exist within a single process. They can't be used for communicating between processes –Signal Events are used for this purpose.

These events are used in two ways:

* 'Off-Page' Connectors: to include a jump from a certain page of a diagram to another. This is useful to print diagrams.
* 'Go-To' Objects: they are used to reduce the number of paths when diagrams are too long.

There can only be one *target* link event with the same label, but there can be many *source*link events with the same label.

Multiple Event

It represents a collection of Intermediate Event triggers. The collection of triggers must be all *throwing* or all *catching* events, but it can’t contain both at the same time. The events that can be used in this collection are as follows: Message, Compensation and Signal. When the flow reaches a *throwing*Multiple Event, all the events included in it are fired. On the other hand, when the flow reaches a *catching* event, it waits for any event included in it.

End Events

An End Event marks where a process or, more specifically, a path ends. There are different types of End Events to indicate the possible results for a process. They are all *throw* events.

Core End Events

* **None:** no result is defined. The process doesn’t end if there are other parallel paths which are still active.
* **Message:** communication to another business entity (Participant or Process).
* **Signal:** defines a broadcast event that any process can see and react to.
* **Terminate:** stops all process activities, even if there are ongoing activities in other parallel paths.

Advanced End Events

* **Error:** an end state that will disrupt the process or require correction. The error triggered by this type of event will eventually be caught by an Error Intermediate Event in a higher level. In addition to including a name, this type of event includes an error code. Unlike signals, these events are not broadcast to all processes. Instead, they have a specific visibility scope and can only be detected by parent processes. The event moves upwards in the process hierarchy and is caught by the first parent process that has an Error Intermediate Event attached to the sub-process activity.
* **Cancel:** used with the Transaction Sub-process, this event causes the cancellation of the Transaction Sub-process (read [Compensation and Transactions](https://wiki.genexus.com/commwiki/wiki?24922))
* **Compensation:** also used with the Transaction Sub-process, this event throws the undo trigger (read [Compensation and Transactions](https://wiki.genexus.com/commwiki/wiki?24922)).
* **Multiple:** defines two or more results of Message, Error, Compensation or Signal type (fires all events).

The figure below shows the symbols used to represent End Events:

`[imagen omitida: wiki id 24992]`

[Go to the main article](https://wiki.genexus.com/commwiki/wiki?24913) -   [Return to the previous section](https://wiki.genexus.com/commwiki/wiki?24916) - [Go to the next section](https://wiki.genexus.com/commwiki/wiki?24918)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [Introduction to BPMN](https://wiki.genexus.com/commwiki/wiki?24913) |
| [Introduction to BPMN - Activities](https://wiki.genexus.com/commwiki/wiki?24916) | [Introduction to BPMN - Gateways](https://wiki.genexus.com/commwiki/wiki?24918) | [Introduction to BPMN - Overview](https://wiki.genexus.com/commwiki/wiki?24914) | [Model Automation](https://wiki.genexus.com/commwiki/wiki?25115) |

---
