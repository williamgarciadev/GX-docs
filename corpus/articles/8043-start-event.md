---
title: "Start event"
source_id: 8043
source_url: https://wiki.genexus.com/commwiki/wiki?8043
genexus_version: "18"
---

# Start event

It is a system event that is activated when an object starts running. It is commonly used to assign values to variables that, during the object's execution, will be used either for arithmetical operations or as flags.

### [Syntax](#Syntax)

**Event Start**  
*Event\_code*  
**EndEvent**  
  
**Where:**  
  
*Event\_code*  
   Code associated with the event.

### [Scope](#Scope)

**Objects:**[Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [WorkWith](https://wiki.genexus.com/commwiki/wiki?15974)

### [Description](#Description)

The Start event is activated when an object starts running. It is commonly used to initialize variable values that may be displayed on the screen or not; after that, during the object's execution, those variables are used, for example, for arithmetical operations or as flags. In this event, you can also invoke objects or codify whatever you need to do when the object starts running.

Attribute values are not instantiated yet. Only attributes received by parameter (in the [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862)) contain those received values.

In [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s and [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s, the Start event is executed when the page is loaded (GET) and with every POST to the server.

In [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s, it is executed only the first time it is opened on a device. It is not executed again unless the panel is exited and opened again.

### [Samples](#Samples)

**1)** In a Panel object you may want to keep the date and time the object was opened:

```
Event Start
    &DateTime = Now()
EndevEnt
```

2) When executing a Web Panel, you may want to control access by calling a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293):

```
Event Start
   ChkSecurity(&WebUserExtKey, &WebUserLogin, &aUserProfiles(), &aUserRights(), &Message)
   if not Null(&Message)
      ShowMessage(&Message)
   EndIf
EndEvent
```


|  |
| --- |
| **Backlinks** |
| [ClientStart event](https://wiki.genexus.com/commwiki/wiki?24044) | [Custom Start Event Code property](https://wiki.genexus.com/commwiki/wiki?51459) | [Events in Transactions](https://wiki.genexus.com/commwiki/wiki?8042) |
| [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [HowTo: Use an external CSS file on a Web Panel](https://wiki.genexus.com/commwiki/wiki?24387) | [Prompt rule](https://wiki.genexus.com/commwiki/wiki?6863) |
| [Runtime external object](https://wiki.genexus.com/commwiki/wiki?33076) | [Save State property](https://wiki.genexus.com/commwiki/wiki?46017) | [Server-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24234) | [Slide.Start event](https://wiki.genexus.com/commwiki/wiki?25585) |
| [Web Panels events](https://wiki.genexus.com/commwiki/wiki?8178) |

---
