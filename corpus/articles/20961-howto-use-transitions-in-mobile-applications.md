---
title: "HowTo: Use Transitions in Mobile applications"
source_id: 20961
source_url: https://wiki.genexus.com/commwiki/wiki?20961
genexus_version: "18"
---

# HowTo: Use Transitions in Mobile applications

User Experience and User Interface are very important aspects of today's mobile applications.

Users either like or dislike an app by the way they interact with it, so the main goal is to make them feel good using an app and make it look as nice as possible.

This is why the possibility of using Transitions when calling [Objects for Native Mobile applications development](https://wiki.genexus.com/commwiki/wiki?20087) has been incorporated.

### [Information](#Information)

The Transitions that can be used in GeneXus Mobile applications are as follows:

* Default (default effect of the platform)
* CurlUp (iOS only)
* CurlDown (iOS only)
* FlipFromLeft (iOS only)
* FlipFromRight (iOS only)
* SlideDown
* SlideUp
* SlideLeft
* SlideRight
* PushUp
* PushDown
* PushLeft
* PushRight
* Fade
* None

### [Important facts](#Important+facts)

**1.** Some effects are only supported by the iOS platform.

**2.** The Default value in iOS is different depending how the panel is invoked.

For Example:

```
Panel.Call()  / PushLeft
Panel.PopUp() / SlideUp
```

**3.** The default value for Android may vary depending on OS Version and Device Manufacturer.

**4.** If an effect that is only supported by iOS is executed on an Android app, the effect displayed will be the Default Android effect.

**5.** Some Exit Effects do not work if they are executed one after the other. For example:

Slide Up - Slide Down  
Slide Down - Slide Up  
Curl Down - Curl Up   
Flip Left - Flip Right

**6.** Transitions can be modified at runtime using [CallOptions](https://wiki.genexus.com/commwiki/wiki?23666).

### [Example in GeneXus](#Example+in+GeneXus)

To add this feature to a GeneXus Mobile Application follow these steps:

**1.** The first step is to check the Form Class in the Theme with its properties and values:

`[imagen omitida: wiki id 20964]`

**2.** As you can see, this class and its subclasses allow picking an Enter Effect and an Exit Effect for a Form. The effects that can be chosen are those listed above.

    The Enter Effect will be the effect displayed on the screen when the panel is invoked. On the other hand, the Exit Effect will be the effect displayed on the screen when the current panel returns to the previous panel.

    Remember that when Returning to a panel, the screen effect will be the Exit Effect of the current panel, not the Enter Effect of the target panel.

    Also, when setting an Enter Effect its opposite will be automatically set as the Exit Effect. However, you can change the Exit Effect for any of the lists.

`[imagen omitida: wiki id 20965]`

**3.** Set the property Form Class in the Layout of an object for Mobile apps.

`[imagen omitida: wiki id 20966]`

**Note**: Up to GeneXus X Evolution 2 Upgrade 4 the "Exit Effect" property was called "Close Effect".

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]`  [Transitions in X Encontro Brasil app](http://www.youtube.com/watch?v=ioZMwkeAl08)


|  |
| --- |
| **Backlinks** |
| [CallOptions Transitions](https://wiki.genexus.com/commwiki/wiki?25321) | [DesignOps - Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871) |
| [DesignOps - Guide for developers](https://wiki.genexus.com/commwiki/wiki?46877) | [DynamicCall External Object](https://wiki.genexus.com/commwiki/wiki?47056) | [Form theme-class for Smart Devices](https://wiki.genexus.com/commwiki/wiki?37648) |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
