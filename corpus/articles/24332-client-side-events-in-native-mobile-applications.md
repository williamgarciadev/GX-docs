---
title: "Client-side Events in Native Mobile Applications"
source_id: 24332
source_url: https://wiki.genexus.com/commwiki/wiki?24332
genexus_version: "18"
---

# Client-side Events in Native Mobile Applications

Client events allow you to add behavior and logic to the application mixing the execution between the client-side and server-side. As mentioned in [Native Mobile Applications Events](https://wiki.genexus.com/commwiki/wiki?17042), **Start**, **Refresh** and **Load** are server-side(1) events. All other events are **client-side events**, you can mix the power of the server and the resources of our device.

Client-side events must use the [Composite command](https://wiki.genexus.com/commwiki/wiki?17389) when executing more than one action.

### [ClientStart event](#ClientStart+event)

[ClientStart event](https://wiki.genexus.com/commwiki/wiki?24044) is the first event executed on the device, even before executing the Start event (server-side), without user interaction. Allows the developer to initialize the entry screen, e.g. UI, variables, etc.

### [Navigation.Start event](#Navigation.Start+event)

[Navigation.Start event](https://wiki.genexus.com/commwiki/wiki?25668)(2) is executed immediately after the ClientStart event, and allows the developer to initialize aspects related to [navigation style](https://wiki.genexus.com/commwiki/wiki?16229) (e.g. call the main panel when the application has Slide navigation).

### [Back event](#Back+event)

[Back event](https://wiki.genexus.com/commwiki/wiki?24950) allows the developer to capture when the end-user press back button on Android or do a back gesture on iOS.

### [Control and user events](#Control+and+user+events)

These events are the programmatic response of the application to user interaction. These forms of interaction are called [actions](https://wiki.genexus.com/commwiki/wiki?20623) and can be seen in on-screen buttons, images, or other controls that when tapped, long tapped, etc., will execute the event associated to the action. There also exists other predefined events that are executed in special cases or without any user interaction.

Mainly you have two types of events: [**user**](https://wiki.genexus.com/commwiki/wiki?25198,,) and [**control**](https://wiki.genexus.com/commwiki/wiki?24271) events. Both are associated with controls. The slight difference is while the former has a name given by the developer and then associated to the controls themselves (with the tap gesture as the way to trigger them); the latter are automatically predefined, depending on control type, having, in the case of [touch control events](https://wiki.genexus.com/commwiki/wiki?20044), the event itself as the way to trigger them (e.g. *control***.LongTap** event). Other kind of control events are, for example, *control***.PageChanged** event (when control is a grid of certain control type), or *control***.ControlValueChanged** event (when control is a read-write attribute or variable).

What happens when the end-user triggers an action? The associated code is executed on the client-side (i.e. in the device) unless a roundtrip to the server is required; for example, when a procedure must be invoked. In any case, system events are not executed (unless they are explicitly required by the Refresh command).

In this event, the developer is allowed to:

* Call **Rest Web Services**:
  + Call a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) or a [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) exposed as [REST Web Services](https://wiki.genexus.com/commwiki/wiki?14573).  
    For example,
    - &var = **DP**( &parm1, ..., &parmn )
    - &var = **Proc**( &parm1, ..., &parmn )
  + Use [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) in a batch way: BC based variables and items.  
    For example,
    - *&BC***.Load(** *primaryKey* **)**
    - *&BC****.****Attributen* = ...
    - *&BC***.Save()**
    - *&BC**.*****Delete()**
* Call a **WorkWith** 
  + **Edit**  
    [Call a Work With object](https://wiki.genexus.com/commwiki/wiki?17160) Detail node in order to Insert, Update or Delete information:
    - *WorkWithDevicesObject*.*levelname***.Detail.Delete(** *primaryKey* **)**
    - *WorkWithDevicesObject***.***levelname***.Detail.Update(** *primaryKey* **)**
    - *WorkWithDevicesObject***.***levelname***.Detail.Insert(** *&bc* **)**
  + **View**  
    [Call a Work With object](https://wiki.genexus.com/commwiki/wiki?17160) List or Detail:
    - *WorkWithDevicesObject***.***levelname***.Detail(** *primaryKey* **)**
    - *WorkWithDevicesObject***.***levelname***.List( )**
* Call a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)
* Call a [Menu object](https://wiki.genexus.com/commwiki/wiki?16321)
* Invoke the **external objects** of the [Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288). For example,
  + Msg(&var)
  + Confirm (&var)
  + Return
  + Refresh
  + AddressBook.AddContact( ... )
  + etc.
* Call a **[Panel for Web](https://wiki.genexus.com/commwiki/wiki?6916)** by means of the [Component domain](https://wiki.genexus.com/commwiki/wiki?16186).  
  This action displays a web page by the web navigator, loading the web panel without showing the navigator's frame. That can be recovered if the user wishes to do so.
* Call to **[Subroutines](https://wiki.genexus.com/commwiki/wiki?24767)**.
* **Commands**:
  + **Control properties assignments** depending on the control.  
    When the developer enters the control name followed by a dot ("."), an IntelliTip is opened showing all possibilities for this control.  
    For example,
    - *Control***.visible =** ...
    - *Control***.class =** ...
  + Simple **variable assignment**.  
    For exmaple,
    - *&Var* = "Test"
    - *&Var* = 123
    - *&Var* = *proc*.**Udp()**
  + Use **SDT or BC based variables** element assignation.  
    For example,
    - *&Var* = *&SDT*.*Field*
    - *&BC.item* = ...
  + Execute **[For Each Line](https://wiki.genexus.com/commwiki/wiki?8605)** and **[selected line](https://wiki.genexus.com/commwiki/wiki?16149)** commands in grids with multiple selections.
  + Use **If-Else-EndIf**, **Do-Case** and **Do-While** code blocks.  
    Cannot use complex expressions on the conditions such as calling Procedures or External Objects methods; only simple conditions are allowed using variables, attributes or SDT members, and involving operators and standard functions.  
      
    **Note:** As you can see, the [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) is not allowed. So, in case of defining it inside these events, the following error message will be displayed: **error: Line can't be interpreted by devices**.

### [Notes](#Notes)

(1) Note that in this context, "server-side" refers to the architecture and not to the actual location of the code being executed. In [Offline applications](https://wiki.genexus.com/commwiki/wiki?22237), the Start, Refresh and Load events execute locally, but they still have the same limitation regarding the type of code they can execute.

(2) Navigation.Start event actually refers to a family of events. There is one evento for each type of navigation. For example, Tabs.Start or Slide.Start.

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Grammar of Events on the Client Side and Composite Command](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/grammar-of-events-on-the-client-side-and-composite-command?p=3682)  
`[imagen omitida: wiki id 20668]` [Events in Mobile Applications](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/events-in-mobile-applications-6103211?p=3673)

### [See also](#See+also)

* [Event Triggering Order in Panels](https://wiki.genexus.com/commwiki/wiki?17614)
* [Determining the Base Table for the Form and Grid in Panels](https://wiki.genexus.com/commwiki/wiki?24807)
* [Calls to Elements in Work Withs from Native Mobile Applications Events](https://wiki.genexus.com/commwiki/wiki?17160)
* [Actions in objects for Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?20623)
* [Flexibility added to Syntax of Smart Devices User Events](https://wiki.genexus.com/commwiki/wiki?25198,,)


|  |
| --- |
| **Backlinks** |
| [Calls to Elements in Work Withs from Native Mobile Applications Events](https://wiki.genexus.com/commwiki/wiki?17160) | [ClientStart event](https://wiki.genexus.com/commwiki/wiki?24044) | [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911) |
| [Do Case command](https://wiki.genexus.com/commwiki/wiki?31605) | [GUID data type](https://wiki.genexus.com/commwiki/wiki?31772) | [Horizontal Formulas](https://wiki.genexus.com/commwiki/wiki?5864) |
| [HowTo: Format plain text programmatically](https://wiki.genexus.com/commwiki/wiki?31657) | [Msg function](https://wiki.genexus.com/commwiki/wiki?31635) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Category:Native Mobile Applications Events](https://wiki.genexus.com/commwiki/wiki?17042) |
| [Network external object](https://wiki.genexus.com/commwiki/wiki?31310) | [SetEmpty method](https://wiki.genexus.com/commwiki/wiki?9646) | [Specification Codes from spc0150 onwards](https://wiki.genexus.com/commwiki/wiki?6774) | [Synchronization.ResetOfflineDatabase method](https://wiki.genexus.com/commwiki/wiki?29785) |

---
