---
title: "HowTo: Using Global Events in Smart Device applications"
source_id: 30201
source_url: https://wiki.genexus.com/commwiki/wiki?30201
genexus_version: "18"
---

# HowTo: Using Global Events in Smart Device applications

Usually, in smart device applications, an end-user executes a certain sequence of actions on a panel whose effect should alter the information displayed on another panel once the end-user access it. Here the primary activity is the reaction to the receipt of semantically significant signals (a.k.a. 'events'). This goal can be achieved in GeneXus through the [Global Events](https://wiki.genexus.com/commwiki/wiki?31164) concept.

## [Steps to use them](#Steps+to+use+them)

1) Look for the [GlobalEvents external object](https://wiki.genexus.com/commwiki/wiki?31169), under *GeneXus/Common* folder in the Root Module of the Knowledge Base.  
`[imagen omitida: wiki id 30352]`

2) In the Events section, create as many events as you need simply by pressing "Enter" on the node. For each of them you must do two things:

* Set the **Internal Name** property for the new event  

  **Note**: If you want to trigger this event from an offline procedure you must set the **iOS External Name** and **Android External Name** properties with the same value in lowercase.
* Ensure you have the **Is static** property to **True**.

Optionally, you can enter a parameter sequence and the [Domain](https://wiki.genexus.com/commwiki/wiki?25813) each one belongs to.

`[imagen omitida: wiki id 30353]`

3) Once the events are created, you can call or catch them from Panels or Work With for Smart Devices objects, as shown in the Usage Example section below.

## [Usage example](#Usage+example)

Suppose you have two independent Panels for Smart Devices called “Sender” and “Receiver”. The “Sender” will send information to the “Receiver” to update its data. The following table shows how they interact in this simple example.

|  |  |
| --- | --- |
| **SENDER  (trigger)** | **RECEIVER  (handler)** |
| - Send a signal | - Show how many times it receives the signal |
| - Send a Numeric and a String value entered by the user | - Show the last Numeric and String values received |
|  |  |
| ``` Event 'Signal'     GlobalEvents.AnEvent() Endevent  Event 'Send'    GlobalEvents.AnEventParm(&Numeric,&String) Endevent ``` | ``` Event ClientStart     &Count = 0 Endevent  Event GlobalEvents.AnEvent()     &Count += 1 Endevent  Event GlobalEvents.AnEventParm(&OneNumeric,&OneString)     Composite         &Numeric = &OneNumeric         &String = &OneString     EndComposite EndEvent ``` |

Once the “Sender” and “Receiver” panels are designed, you need to create a new panel with two [components](https://wiki.genexus.com/commwiki/wiki?29811) and embed the panels in them to see the results in-line.

|  |
| --- |
| **In-line view** |
|  |

The final behavior (in an Android device) will be as follows:  
`[imagen omitida: wiki id 30358]`

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects** | [Panel for Smart Devices](https://wiki.genexus.com/commwiki/wiki?24829), [Work With for Smart Devices](https://wiki.genexus.com/commwiki/wiki?15974), [Offline Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) |
| **Generators** | SmartDevices(Android,iOS) |
| **Connectivity** | Online, Offline |

## [Availability](#Availability)

This feature is available as from [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,).

* Support for triggering global events from Offline procedures in Smart Devices applications is available as of [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/wiki?39737,,).


|  |
| --- |
| **Backlinks** |
| [Component control](https://wiki.genexus.com/commwiki/wiki?29811) | [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) |
| [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) | [Global Events](https://wiki.genexus.com/commwiki/wiki?31164) |

---
