---
title: "DragCanceled event in Smart Devices"
source_id: 25084
source_url: https://wiki.genexus.com/commwiki/wiki?25084
genexus_version: "18"
---

# DragCanceled event in Smart Devices

This event is executed when we do not drop the dragged element on a control that accepts it.

### [Syntax](#Syntax)

**Event** <*DraggedControl*>**.DragCanceled**([**&***<parameter>*])

*Event\_code*

**endevent**

The <*parameter*> can only be a variable. This parameter will be loaded with the corresponding value of the [Drag event](https://wiki.genexus.com/commwiki/wiki?22532) out parameter of the <DraggedControl>.

### [Example](#Example)

```
Event MeetingTitle.DragCanceled(&Meeting)
    Composite
        msg('Drop it over the recycle bin to delete it')
    EndComposite
EndEvent
```

To complete the example, see [Drop event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22533) , [DropAccepted event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22542) and [DropAccepted event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22542).

### [Availability](#Availability)

As from [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,).

### [See Also](#See+Also)

* [Drop event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22533)
* [Drag event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22532)
* [DropAccepted event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22542)
* [Developing Drag and Drop in Panels](https://wiki.genexus.com/commwiki/wiki?22524)


|  |
| --- |
| **Backlinks** |
| [Developing Drag and Drop in Panels](https://wiki.genexus.com/commwiki/wiki?22524) | [Drag event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22532) | [Drop event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22533) |
| [DropAccepted event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22542) |

---
