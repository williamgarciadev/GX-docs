---
title: "Global Events"
source_id: 31164
source_url: https://wiki.genexus.com/commwiki/wiki?31164
genexus_version: "18"
---

# Global Events

Generally speaking, in interactive objects (such as [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916), [Panels](https://wiki.genexus.com/commwiki/wiki?24829), etc.) events are actions handled by the program and triggered by the user.

Events are usually local to the program where they are defined. In contrast, *global events* allow defining events global to all the components of an application. A web page (as well as a Smart Device screen) is made up of several components, so the idea is to have every component communicate with each other. Local events are triggered in response to a user action (who may interact with the software by way of, for example, keystrokes on the keyboard); on the other hand, *global events* are code that remains idle until it is invoked from another event (from any other component).

For example, if a user enters an invoice, or receives a notification of some action, another panel of the same screen may react to that action (it can print the invoice, or refresh the related data). Then, the components that constitute a screen can be nested in a very complex way and local events are local to each component. Through *global events*, all the components of the screen can interact with each other because events can be invoked from any component.

**Note**: In summary, a global event can be called from any component, regardless of the component where it was defined.

## [Example](#Example)

For example,

In the picture below, a global event defined in "Component E" could be invoked from "Component A" or vice-versa. Any combination is possible, regardless of the nesting level of the components that form the screen.

`[imagen omitida: wiki id 32496]`

**Note**: Unlike user-defined events, which do not accept parameters, *global events* do.

## [Implementation](#Implementation)

They are implemented through the [GlobalEvents external object](https://wiki.genexus.com/commwiki/wiki?31169).

See [HowTo: Using Global Events in Smart Device applications](https://wiki.genexus.com/commwiki/wiki?30201) and [HowTo: Use Global Events in Web Objects](https://wiki.genexus.com/commwiki/wiki?31167)

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators** | SmartDevices(Android,iOS), Web(.NET, Java) |

## [Notes](#Notes)

* Another source for triggering events is a hardware device (such as a timer). The event handler for this type of events can be implemented using [External Objects for Javascript](https://wiki.genexus.com/commwiki/wiki?31064) or [HowTo: create an External Object which triggers GeneXus events in iOS](https://wiki.genexus.com/commwiki/wiki?26936) which are a kind of global events.

## [Availability](#Availability)

This feature is available as of [GeneXus 15](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?28265,,).

* In Smart Devices, global events for offline procedures are available as of [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?39737,,).


|  |
| --- |
| **Backlinks** |
| [Event Execution Scheme](https://wiki.genexus.com/commwiki/wiki?22472) |
| [GetString method](https://wiki.genexus.com/commwiki/wiki?8831) | [GlobalEvents external object](https://wiki.genexus.com/commwiki/wiki?31169) | [HowTo: Send a message to the chatbot from a menu](https://wiki.genexus.com/commwiki/wiki?40912) | [HowTo: Use Global Events in Web Objects](https://wiki.genexus.com/commwiki/wiki?31167) |
| [HowTo: Using Global Events in Smart Device applications](https://wiki.genexus.com/commwiki/wiki?30201) | [User defined event](https://wiki.genexus.com/commwiki/wiki?8044) |

---
