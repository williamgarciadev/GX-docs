---
title: "Composite command"
source_id: 17389
source_url: https://wiki.genexus.com/commwiki/wiki?17389
genexus_version: "18"
---

# Composite command

Groups GeneXus code that's executed sequentially up to the last line, unless there is an error that interrupts it.

### [Syntax](#Syntax)

Event **'***ClientEventName***'** | *Control***.***AssociatedControlEvent*  
**Composite**  
*Event\_code*  
**EndComposite**  
EndEvent

#### [**Where:**](#Where%3A)

*ClientEventName*  
     Is the user event name.

*Control*  
     Is the control name that you program the event *AssociatedControlEvent*

*AssociatedControlEvent*  
     Is one of the events associated with controls (such as tap, long tap, drag, drop, PageChanged, ControlValueChanged, etc. -depending on the control type-)

*Event\_code*  
    It details the code to be executed when the event occurs.  At least two commands are needed.

### [Description](#Description)

The code block Composite/EndComposite groups GeneXus code. This code is executed sequentially to the last line, except when an error in any of such lines occurs. In this case, the sequence will be interrupted.

Therefore, its two main premises are:

1. If one of the instructions (calls or assignments) fails, the rest are not executed.
2. Error messages (automatic ones as well as loaded by the developer) are displayed on the device screen.

The use of this command is not a must when two or more invocations are performed on an event. Instead, error handling can be done through the &Err and &ErrMsg variables.

The &Err variable takes on a value greater than 0 when an error occurs, while it is set to 0 if the operation runs smoothly.  
  
The possible values of &Err are used to identify the nature of the error:

* 1 for a generic error,
* 2 if the user cancels the action,
* 3 for incorrect parameters.

When an event invokes a GeneXus object located on the server side, such as a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) or a [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270), the value of &Err will reflect the HTTP code returned by that call in case of error. For example, HTTP 404 or 500.

In situations where no response is received from the server (no HTTP code), &Err will be set to 1.   
  
The &ErrMsg variable contains the description of the error that would be displayed on screen if it were inside a Composite block.  
  
It is important to note that in the case without Composite, an error message is not automatically displayed to the end user, and it is your responsibility to manage how these errors are handled and communicated to the end user.

### [Sample](#Sample)

#### [Sample with the composite command](#Sample+with+the+composite+command)

```
Event 'UpdateEmail'
  Composite 
    UpdateEMail.Call(ClientId,&ClientEmail) 
    Interop.SendMessage("Your Email has been updated successfully in my database", ClientMobilePhone) 
  EndComposite
EndEvent
```

#### [Sample without the composite command](#Sample+without+the+composite+command)

```
Event 'UpdateEmail'
   UpdateEMail.Call(ClientId,&ClientEmail) 
   If &Err <> 0 
      msg(&ErrMsg) 
   Else 
      Interop.SendMessage ("Your Email has been updated successfully in my database", ClientMobilePhone) 
   EndIf
EndEvent
```

### [See Also](#See+Also)

[Composite examples](https://wiki.genexus.com/commwiki/wiki?15551)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Grammar of Events on the Client Side and Composite Command](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/grammar-of-events-on-the-client-side-and-composite-command?p=3682)  
`[imagen omitida: wiki id 20668]` [Events in Mobile Applications](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/events-in-mobile-applications-6103211?p=3673)


|  |
| --- |
| **Backlinks** |
| [Calling objects from Menu Events](https://wiki.genexus.com/commwiki/wiki?17392) | [Client-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24332) |
| [Composite examples](https://wiki.genexus.com/commwiki/wiki?15551) | [Error handling when Composite command is not used](https://wiki.genexus.com/commwiki/wiki?51603) |
| [Geolocation - Show points near me](https://wiki.genexus.com/commwiki/wiki?16473) | [Geolocation - Showing My Location](https://wiki.genexus.com/commwiki/wiki?16433) | [HowTo: Use Confirm method from Interop external object](https://wiki.genexus.com/commwiki/wiki?17334) | [HowTo: Using the ShowError method from Interop in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?51446) |
| [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) | [Interop external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55183) | [Synchronization.Receive method](https://wiki.genexus.com/commwiki/wiki?23603) | [Tabs offered in Panel and Work With objects](https://wiki.genexus.com/commwiki/wiki?16847) |

---
