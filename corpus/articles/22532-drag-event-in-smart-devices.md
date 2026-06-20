---
title: "Drag event in Smart Devices"
source_id: 22532
source_url: https://wiki.genexus.com/commwiki/wiki?22532
genexus_version: "18"
---

# Drag event in Smart Devices

This Event is executed when content is dragged (through long-tap). It allows you to code the activity of the element to be dragged.

### [Syntax](#Syntax)

**Event** *<control>.***Drag(**[**out:**] *&dataParameter*[**,***&booleanParameter*]**)**  
*Event\_code*  
**EndEvent**

Where:

*control*  
      The name of the form control over the drag operation is performed.

*&dataParameter*   
      The data parameter is only one, and it is always an out variable. It will be loaded with the data you want to drag. To drag several elements you have to load them into an [SDT](https://wiki.genexus.com/commwiki/wiki?2427).

*&booleanParameter*  
      It indicates if the Drag event can be executed. This parameter is optional and its default value is True. If set to False inside *Event\_code*, the drag will not be allowed for that control.

*Event\_code*  
      Code associated with the event. The *&dataParameter* will be loaded here with the data you want to drop into another control as a consecuence of the drag operation. To drag several elements of information you have to load them into an SDT, as mentioned above.

### [Example](#Example)

Having the [Work with for Smart Devices](https://wiki.genexus.com/commwiki/wiki?15974) applied to Meeting transaction: to drag the MeetingTitle attribute (part of the List grid), the event would be as follows:

```
Event MeetingTitle.Drag(&Meeting,&bool)
    Composite
       &bool = True
       &Meeting.MeetingId = MeetingId
    EndComposite
EndEvent
```

Note: The MeetingId (primary key) attribute is always sent to the Device even if not explicitly inserted into the grid. Because of that, running the event over a MeetingTitle line, its value is known.

To complete the example, see [Drop event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22533), [DropAccepted event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22542) and [DragCanceled event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?25084).

### [Availability](#Availability)

As from [GeneXus X Evolution 2 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?22626,,).

### [See also](#See+also)

* [Drop event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22533)
* [DropAccepted event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22542)
* [DragCanceled event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?25084)
* [Developing Drag and Drop in Panels](https://wiki.genexus.com/commwiki/wiki?22524)


|  |
| --- |
| **Backlinks** |
| [Developing Drag and Drop in Panels](https://wiki.genexus.com/commwiki/wiki?22524) | [Drag event](https://wiki.genexus.com/commwiki/wiki?24081) |
| [DragCanceled event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?25084) | [Drop event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22533) | [DropAccepted event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22542) |

---
