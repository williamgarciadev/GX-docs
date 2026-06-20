---
title: "HowTo: Use Camera external object in GeneXus"
source_id: 31298
source_url: https://wiki.genexus.com/commwiki/wiki?31298
genexus_version: "18"
---

# HowTo: Use Camera external object in GeneXus

An [external object called Camera](https://wiki.genexus.com/commwiki/wiki?31296) enables interaction with the device's photo camera. The main purpose of this external object is to invoke the Camera of the device, take a picture, and be able to use that image in the application.

This article offers a step-by-step tutorial to use this feature.

### [Step 1: External Object Camera](#Step+1%3A+External+Object+Camera)

To interact with the camera, the external object named Camera has to be used.

`[imagen omitida: wiki id 53885]`

TakePhoto: This method invokes the device's camera native application, so the user can take a picture and select it to use it in the application.

### [Step 2: Learn by Example](#Step+2%3A+Learn+by+Example)

#### 2.1. Create a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829):

**Layout**  
`[imagen omitida: wiki id 19319]`

**Variable**  
&photo based on [Image data type](https://wiki.genexus.com/commwiki/wiki?15204)

**Event**

```
Event 'TakePhoto'
    &photo = Camera.TakePhoto()
Endevent
```

#### 2.2. Execution

Once the action is executed:

`[imagen omitida: wiki id 19321]`

After taking a picture:

`[imagen omitida: wiki id 19322]`

After using it:

`[imagen omitida: wiki id 19323]`

### [Scope](#Scope)

**Generators:**[Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)


|  |
| --- |
| **Backlinks** |
| [Camera external object](https://wiki.genexus.com/commwiki/wiki?31296) | [Camera external object (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53919) | [HowTo: Use Camera external object in GeneXus for Native Mobile apps (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53920) |
| [HowTo: Using PhotoLibrary external object for Smart Devices](https://wiki.genexus.com/commwiki/wiki?26933) | [PhotoLibrary external object](https://wiki.genexus.com/commwiki/wiki?39397) |

---
