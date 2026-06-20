---
title: "Drop event in Smart Devices"
source_id: 22533
source_url: https://wiki.genexus.com/commwiki/wiki?22533
genexus_version: "18"
---

# Drop event in Smart Devices

This event is executed when dropping content.

### [Syntax](#Syntax)

**Event** *control*.**Drop**( **&**<*parameter>*)  
*Event\_code*  
**Endevent**

The <parameter> can only be a variable. This parameter will be loaded with the corresponding value of the [Drag Event](https://wiki.genexus.com/commwiki/wiki?22532) parameter.

### [Example](#Example)

Having an image in the WorkWithDevicesMeeting List layout, named RecicleBin, and the Drag event shown in the [Drag event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22532) example:

```
Event RecicleBin.Drop(&Meeting)
    Composite
        &MeetingId = &Meeting.MeetingId
        DeleteMeeting(&MeetingId)
        msg('Meeting deleted')
        SdActions.Refresh()
    EndComposite
EndEvent
```

Being DeleteMeeting a rest procedure that deletes the received meeting id. If there is a [DropAccepted event](https://wiki.genexus.com/commwiki/wiki?22542), it will be executed first, and then the Drop event.

To complete the example, see [Drop event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22533), [DropAccepted event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22542) and [DragCanceled event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?25084)

### [Availability](#Availability)

As from [GeneXus X Evolution 2 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?22626,,).

### [See also](#See+also)

* [Drag event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22532)
* [DropAccepted event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22542)
* [DragCanceled event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?25084)
* [Developing Drag and Drop in Panels](https://wiki.genexus.com/commwiki/wiki?22524)


|  |
| --- |
| **Backlinks** |
| [Developing Drag and Drop in Panels](https://wiki.genexus.com/commwiki/wiki?22524) | [Drag event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22532) |
| [DragCanceled event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?25084) | [Drop event](https://wiki.genexus.com/commwiki/wiki?24080) | [Drop event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22533) | [DropAccepted event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22542) |

---
