---
title: "Error End Event in BPD"
source_id: 24840
source_url: https://wiki.genexus.com/commwiki/wiki?24840
genexus_version: "18"
---

# Error End Event in BPD

In combination with and an [Error Intermediate Event](https://wiki.genexus.com/commwiki/wiki?18059), this model allows us to find the situation that caused the error in the sub-process and take various actions in the main process.

### [Symbol](#Symbol)

`[imagen omitida: wiki id 24841]`

### [Description](#Description)

The error triggered by this event will eventually be caught by an error intermediate event on a higher level. Besides including a name, this type of event includes an error code.

These events differ from the signals because they aren't broadcasted to all processes. They have a specific range of visibility and only can be detected by a parent process.

The event moves up in the hierarchy of processes and is trapped by the first ancestor process possessing an intermediate error event attached to the subprocess symbol.

### [Example](#Example)

The following example shows how this event is used. The Flight Ticket Reservation process has a subprocess called Validate Reservation, which validates the details of the reservation that has been entered.

For example, if there are no tickets available, you need to indicate that the ticket validation process must be canceled. Also, you must return to the main process to notify the customer and offer the possibility to request new dates for the reservation.

To model this, you insert an Error End Event in the Validate Reservation process, and in his event Error Code property, you type “NO\_TICKETS\_AVAILABLE”. This type of end event throws an error that allows the flow to continue in the ancestor process, to which you will add an intermediate error event to find this error.

You accomplish that by attaching an Error Intermediate Event to the Validate Reservation subprocess in the Flight Ticket Reservation process, and you set the Error Code event’s properties with the text “NO\_TICKETS\_AVAILABLE”, exactly the same text you used before in the Error End Event.

`[imagen omitida: wiki id 24842]`

### [Scope](#Scope)

Objects: [Business Process Diagram](https://wiki.genexus.com/commwiki/wiki?16486)

### [See Also](#See+Also)

[None End Event](https://wiki.genexus.com/commwiki/wiki?12307)

[Terminate End Event in BPD](https://wiki.genexus.com/commwiki/wiki?12316)

[Signal End Event](https://wiki.genexus.com/commwiki/wiki?12337)


|  |
| --- |
| **Backlinks** |
| [BPD End Events](https://wiki.genexus.com/commwiki/wiki?17271) | [Compensate End Event in BPD](https://wiki.genexus.com/commwiki/wiki?50736) | [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |
| [None End Event in BPD](https://wiki.genexus.com/commwiki/wiki?12307) | [Signal End Event in BPD](https://wiki.genexus.com/commwiki/wiki?12337) | [Terminate End Event in BPD](https://wiki.genexus.com/commwiki/wiki?12316) |

---
