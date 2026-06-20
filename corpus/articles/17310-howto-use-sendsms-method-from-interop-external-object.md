---
title: "HowTo: Use SendSMS method from Interop external object"
source_id: 17310
source_url: https://wiki.genexus.com/commwiki/wiki?17310
genexus_version: "18"
---

# HowTo: Use SendSMS method from Interop external object

The SendSMS method offered by the [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) enables opening the SMS native application, filling the message fields with the parameter's values and sending it.

`[imagen omitida: wiki id 54660]`

The following steps show an example of how this feature is used.

### [Step 1](#Step+1)

Create a new [Panel object](https://wiki.genexus.com/commwiki/wiki?24829).

### [Step 2](#Step+2)

Define a variable based on the [Phone domain](https://wiki.genexus.com/commwiki/wiki?14639) (for example &To) and a variable based on the VarChar(200) type (for example &message).

### [Step 3](#Step+3)

Add the variables and a button to the Panel Layout.

### [Step 4](#Step+4)

Define the event associated with the button as follows:

```
Event 'Send'
    Interop.SendSMS(&to, &Message)
EndEvent
```

Done! The entry Panel will accept a phone number and a msg and when the *Send* button is tapped the SMS native application will be invoked.

`[imagen omitida: wiki id 17319]`

`[imagen omitida: wiki id 17320]`


|  |
| --- |
| **Backlinks** |
| [HowTo: Use SendMessage method from Interop external object](https://wiki.genexus.com/commwiki/wiki?15528) | [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) | [Interop external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55183) |
| [Key Color](https://wiki.genexus.com/commwiki/wiki?23130) |

---
