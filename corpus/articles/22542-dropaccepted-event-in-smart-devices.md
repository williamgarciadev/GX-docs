---
title: "DropAccepted event in Smart Devices"
source_id: 22542
source_url: https://wiki.genexus.com/commwiki/wiki?22542
genexus_version: "18"
---

# DropAccepted event in Smart Devices

This event is executed when the dragged element is accepted by a drop target.

### [Syntax](#Syntax)

**Event** <*DraggedControl*>**.DropAccepted**([**&***<parameter>*])

*Event\_code*

**endevent**

The <*parameter*> can only be a variable. This parameter will be loaded with the corresponding value of the [Drag event](https://wiki.genexus.com/commwiki/wiki?22532) out parameter of the <DraggedControl>.

### [Example](#Example)

```
Event MeetingTitle.DropAccepted(&Meeting)
    Composite
        MeetingTitle.Visible = True
    EndComposite
EndEvent
```

To complete the example, see [Drop event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22533), [DropAccepted event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22542) and [DragCanceled event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?25084).

This event will be executed before the Drop one.

### [Availability](#Availability)

As from [GeneXus X Evolution 2 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?22626,,).

### [See Also](#See+Also)

* [Drop event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22533)
* [Drag event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22532)
* [DragCanceled event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?25084)
* [Developing Drag and Drop in Panels](https://wiki.genexus.com/commwiki/wiki?22524)


|  |
| --- |
| **Backlinks** |
| [Developing Drag and Drop in Panels](https://wiki.genexus.com/commwiki/wiki?22524) | [Drag event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22532) |
| [DragCanceled event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?25084) | [Drop event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22533) | [DropAccepted event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22542) |

---
