---
title: "HowTo: Use PlaceCall method from Interop external object"
source_id: 17309
source_url: https://wiki.genexus.com/commwiki/wiki?17309
genexus_version: "18"
---

# HowTo: Use PlaceCall method from Interop external object

The PlaceCall method offered by the [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) enables making a call if the app is running on a device that supports that feature.

`[imagen omitida: wiki id 54718]`

It receives a parameter based on the [Phone domain](https://wiki.genexus.com/commwiki/wiki?14639).

The following steps guide you on how to use the PlaceCall method.

### [Step 1](#Step+1)

Create a new [Panel object](https://wiki.genexus.com/commwiki/wiki?24829).

### [Step 2](#Step+2)

Define a variable based on the [Phone domain](https://wiki.genexus.com/commwiki/wiki?14639) and insert it in the Panel Layout. This variable will be entered by the user with the phone number to call.

### [Step 3](#Step+3)

Insert a button in the Layout with the following event associated with it :

```
Event 'Call'
    Interop.PlaceCall(&Phone)
EndEvent
```

Done! The entry panel will accept a phone number and when the Call button is tapped, a call will be started.

### [Screenshots](#Screenshots)

[**Android**](https://wiki.genexus.com/commwiki/wiki?14453)

### 

### [Considerations](#Considerations)

When using
[Apple](https://wiki.genexus.com/commwiki/wiki?14917), once the phone call ends the application is redirected to the native "phone call history" application, it does not go back to the original application.

### [Availability](#Availability)

[GeneXus X Evolution 2 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?19995,,).


|  |
| --- |
| **Backlinks** |
| [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) | [Interop external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55183) |

---
