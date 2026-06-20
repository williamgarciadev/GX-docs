---
title: "HowTo: Use PlayAudio method from Interop external object"
source_id: 17339
source_url: https://wiki.genexus.com/commwiki/wiki?17339
genexus_version: "18"
---

# HowTo: Use PlayAudio method from Interop external object

The PlayAudio method offered by the [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) enables listening to an audio track within the application.

`[imagen omitida: wiki id 54719]`

It receives one parameter, based on the URL domain, which will try to reproduce an audio file.

The following steps guide you on how to use the PlaceCall method.

### [Step 1](#Step+1)

Create a new [Panel object](https://wiki.genexus.com/commwiki/wiki?24829).

### [Step 2](#Step+2)

Insert a Button in the Panel Layout.

### [Step 3](#Step+3)

Double-click on the button and add the following code inside the event associated with the button:

```
Event 'Play'
    Interop.PlayAudio("http://www.rzaca.com/GSS-10%20Challenge%2018/game%20sound%20FX/Bionic%20Man.wav")
EndEvent
```

Done! The entry Panel will show a button that, when tapped, will redirect the user to a screen with the play and pause controls.

After the audio file ends, the device goes back to the application.


|  |
| --- |
| **Backlinks** |
| [Audio external object](https://wiki.genexus.com/commwiki/wiki?30041) | [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) | [Interop external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55183) |

---
