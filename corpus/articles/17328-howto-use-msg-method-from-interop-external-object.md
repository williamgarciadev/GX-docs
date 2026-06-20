---
title: "HowTo: Use Msg method from Interop external object"
source_id: 17328
source_url: https://wiki.genexus.com/commwiki/wiki?17328
genexus_version: "18"
---

# HowTo: Use Msg method from Interop external object

The Msg method offered by the [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) enables displaying a message in a pop-up window.

`[imagen omitida: wiki id 54717]`

Below is an example of how this feature is used.

### [Step 1](#Step+1)

Create a new [Panel object](https://wiki.genexus.com/commwiki/wiki?24829).

### [Step 2](#Step+2)

Define a variable based on VarChar(200). Suppose you call it &MsgPopup and it is present in the Panel Layout. This variable will allow entering a message to be shown in a pop-up window on the device.

### [Step 3](#Step+3)

Add a new button in the Panel Layout (associated with an Event called PopMSG).

### [Step 4](#Step+4)

Go to the event by double-clicking on the button and define the following code:

```
Event 'PopMSG'
    Interop.Msg(&MsgPopup)
EndEvent
```

Done! The entry Panel will accept a message and when the button is tapped, the text in a message dialogue will be prompted.

Since [GeneXus 16 upgrade 9](https://wiki.genexus.com/commwiki/wiki?45275,,), the Msg method accepts two parameters: the message and the button text. For example:

```
Event 'PopMSG'
    Interop.Msg("This is a test", "Ok, thanks")
EndEvent
```

`[imagen omitida: wiki id 45401]`


|  |
| --- |
| **Backlinks** |
| [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) | [Interop external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55183) |

---
