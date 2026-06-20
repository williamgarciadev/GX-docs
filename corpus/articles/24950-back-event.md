---
title: "Back event"
source_id: 24950
source_url: https://wiki.genexus.com/commwiki/wiki?24950
genexus_version: "18"
---

# Back event

Defines an action to be performed when the back button is pressed.

### [Syntax](#Syntax)

Event **Back**  
*<Event\_code>*  
EndEvent

### [Scope](#Scope)

**Objects:** [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [WorkWith](https://wiki.genexus.com/commwiki/wiki?15974)  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

In some cases, you may need to control navigation in your application. For example, in a wizard, users should not return to previous steps once they move forward.

The Back event allows you to control this behavior by changing the back button's action or displaying a confirmation dialog before navigating to the previous [Panel object](https://wiki.genexus.com/commwiki/wiki?24829).

### [Apple Limitations](#Apple+Limitations)

* The body of the Back event is restricted to:
  1. Leaving it empty for disabling the back button.
  2. Programming a [Return command](https://wiki.genexus.com/commwiki/wiki?31353) **only.** No other code is allowed.  
  The reason for this limitation is that Apple does not allow the developer to change the default behavior of a back action (e.g. display a message before back).
* As of [GeneXus 17](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46068,,), the limitation above does not apply when the Panel is called with [CallType.Popup](https://wiki.genexus.com/commwiki/wiki?25322) and CallTargetSize different than Large (that is, when it has value Small, Medium, or Default).  
  In that case, Apple does allow the developer to control how the call is ended, and it is allowed to have a fully supportive Back event.
* When a UI object is called with [CallOption.Target = 'Blank'](https://wiki.genexus.com/commwiki/wiki?25323), ensure that the object does not contain an action on the top-left side of the Application Bar (i.e. Position property = Custom (Apple) and top-left alignment) because the back button will be positioned in that place. If the developer situates a custom button in that place, the back button (and its swipe right gesture) will be disabled and it is the responsibility of the developer to implement the "back action" when it is desired.

### [Samples](#Samples)

**Warning**: All examples work as described in Android and on Apple when the above limitations do not apply, but only examples 1) and 2) always work in Apple.

#### [1) Disable the back button.](#1%29+Disable+the+back+button.)

```
Event Back
EndEvent
```

#### [2) Change the default behavior of the back action by using the return command.](#2%29+Change+the+default+behavior+of+the+back+action+by+using+the+return+command.)

```
Event Back
    Return
EndEvent
```

#### [3) Display a confirm dialog before canceling the action.](#3%29+Display+a+confirm+dialog+before+canceling+the+action.)

```
Event Back
    Composite
      Confirm("Are you sure you want to return?") 
      Actions.Cancel()
    EndComposite
EndEvent
```

#### [4) Call a Panel when the Back button is pressed.](#4%29+Call+a+Panel+when+the+Back+button+is+pressed.)

```
Event Back
      HelloWorldPanel()
EndEvent
```

### [Notes](#Notes)

* If you are trying to skip Panels that have already been done on a wizard, it is recommended to use [CallOptions.Type = Replace](https://wiki.genexus.com/commwiki/wiki?25322) on the caller, instead of calling a Panel on the Back event. With that, you optimize the usage of the application stack, replacing old Panels with new ones when navigating through the application.
* When the Back event is not implemented, on each platform it behaves by default as an execution of the [Actions.Cancel()](https://wiki.genexus.com/commwiki/wiki?31350) method. In such a case, the subsequent code of the caller object won't be executed if it is inside a [Composite command](https://wiki.genexus.com/commwiki/wiki?17389).
* In contrast to the above point, if the Back event is implemented by using the [Return command](https://wiki.genexus.com/commwiki/wiki?31353), the subsequent code of the caller object will be executed. For example, suppose you have two Panels, A and B, and the Panel A calls Panel B as follows:

```
Event 'Call_B'
  Composite
     // ... do something before calling B
     B()  //B is called without parameters
     msg("After calling B")
     // ... do something else after calling B
  EndComposite
EndEvent
```

If no Back event is implemented on B, or it is implemented using the [Actions.Cancel()](https://wiki.genexus.com/commwiki/wiki?31350) method, the message after the calling will not be executed if the code is inside a Composite command. If the Back event is implemented by using the [Return command](https://wiki.genexus.com/commwiki/wiki?31353), the message ("After calling B") will be displayed on Panel A.

### [See Also](#See+Also)

[Native Mobile Applications Events](https://wiki.genexus.com/commwiki/wiki?17042)  
[Server-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24234)  
[Event Triggering Order in Panels](https://wiki.genexus.com/commwiki/wiki?17614)


|  |
| --- |
| **Backlinks** |
| [Client-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24332) | [HowTo: Return from a Panel to the caller Panel in Native Mobile Apps](https://wiki.genexus.com/commwiki/wiki?59817) |
| [Table of contents:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
