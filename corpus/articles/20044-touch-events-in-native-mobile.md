---
title: "Touch Events in Native Mobile"
source_id: 20044
source_url: https://wiki.genexus.com/commwiki/wiki?20044
genexus_version: "18"
---

# Touch Events in Native Mobile

The UX (**U**ser e**X**perience, look & Feel) of the applications is very important on mobile platforms. This can be improved by a better design, better screen navigation, and also how the information is organized throughout the whole app. But there is also a key feature that the users of Native Mobile expect, that is the applications react to what they do on their devices.

In touchscreen devices, the way to input information or commands is done by interacting with the screen.

These inputs are called **gestures** and the applications have to consider them to provide a good UX.

### [Which Gestures does GeneXus recognize?](#Which+Gestures+does+GeneXus+recognize%3F)

* **Tap**  
  Touch briefly the control with the fingertip.
* **DoubleTap**  
  Touch rapidly the control twice with the fingertip.
* **LongTap**  
  Touch the control for an extended period with the fingertip.
* **Drag and Drop**  
  Touch the control with the fingertip and move it to a new position without losing contact, until reaching the goal.
* **SwipeRight**  
  Touch the control with the fingertip and move it rapidly to the right.
* **SwipeLeft**  
  Touch the control with the fingertip and move it rapidly to the left.
* **SwipeUp**  
  Touch the control with the fingertip and move it up rapidly.
* **SwipeDown**  
  Touch the control with the fingertip and move it down rapidly.
* **Swipe**  
  Any of the previous swipe gestures

### [Which objects can accept gestures?](#Which+objects+can+accept+gestures%3F)

* Image
* Textblock
* Table
* Attribute (read-only)
* Variable (read-only)
* And mostly every other control.

All these gestures are encoded in GeneXus as events related to the screen controls.

### [How to link an event to a Control?](#How+to+link+an+event+to+a+Control%3F)

#### [Example](#Example)

The first mechanism is by right-clicking on the user control (previously dragged from the toolbox to the layout).  
This action will display a contextual menu (as it is shown below) with every possible event associated with that control.

`[imagen omitida: wiki id 33319]`

Once you select one of these options, automatically will be redirected from the Layout tab to the Event tab and the selected event associated with the control (in this case a TextBlock named "Textblock1") will be ready to be filled.

```
Event Textblock1.Tap 
    Msg("Textblock Tap Event Executed")
EndEvent
```

As an alternative mechanism, you can be positioned on the Event tab and start writing the event with a suggest menu.  
This menu will be displayed when you write the [Control Name](https://wiki.genexus.com/commwiki/wiki?8754) of the control following by a dot (e.g. 'Textblock1.').

`[imagen omitida: wiki id 33318]`

### [Controls and Containers: which touch event will be executed?](#Controls+and+Containers%3A+which+touch+event+will+be+executed%3F)

Some of the objects that support touch events are containers; others are non-editable controls. There is a special consideration when control and container have touch events.

#### [**Example**](#Example)

Suppose in a layout you have a table control, named **MainTable,** and an image control, named **MyImg**, **inside** the MainTable control (i.e. MainTable is a container).

Furthermore, for MainTable it was codified the **Tap** and **Swipe** events.  And for MyImag you have **LongTap** and **Swipe**.

If a Tap Event is executed on **MyImg** (as it doesn't handle it) the touch event is propagated to its container **following a hierarchically order**until one container is found which handles the tap event. In our case, the Tap event of the **MainTable**will be executed.

If a swipe event is performed to **MyImg** the only code executed will be the one defined for **MyImg**.Swipe as the event was executed this is not propagated to its container.

### [Platform Limitations](#Platform+Limitations)

* Android touch events propagation: If a Control does not have any touch events defined, it will propagate the events to its container. If the control has one or more touch events defined it will not propagate the event even though its container may handle those events.

### [Feedback to user](#Feedback+to+user)

For the user to receive feedback when executing a gesture, the **Tap**, **DoubleTap,** and **LongTap** gestures trigger the highlighting of the control. That is: if you tap on a control, its "Highlighted Background" class property will be considered to give feedback to the user.


|  |
| --- |
| **Backlinks** |
| [Client-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24332) | [Category:Control Events](https://wiki.genexus.com/commwiki/wiki?24271) |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
