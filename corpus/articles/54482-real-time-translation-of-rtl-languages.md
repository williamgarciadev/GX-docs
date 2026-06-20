---
title: "Real-time translation of RTL languages"
source_id: 54482
source_url: https://wiki.genexus.com/commwiki/wiki?54482
genexus_version: "18"
---

# Real-time translation of RTL languages

Runtime translation with right-to-left (RTL) and left-to-right (LTR) languages can be done with the [SetLanguage function](https://wiki.genexus.com/commwiki/wiki?18757). This is valid as long as you use [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) or [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) with  [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) (DSO) with the value None in the [Base CSS property](https://wiki.genexus.com/commwiki/wiki?49256).

For example, if you use the English and Arabic languages, you can include the following in a Web Panel:

```
Event 'SetEnglish'
    &i = SetLanguage(!"English")
    refresh
EndEvent

Event 'SetArabic'
    &i = SetLanguage(!"Arabic")
    refresh
EndEvent
```

The orientation will be determined automatically, because the application generated with DSO uses the ['dir' attribute](https://caniuse.com/?search=html%20dir%20attribute).

### [Considerations](#Considerations+)

1. For [Native Mobile Generator](https://wiki.genexus.com/commwiki/wiki?14451) its recommended to set a *GoHome* command ([Actions external object](https://wiki.genexus.com/commwiki/wiki?31350)):

   ```
   Event 'Arabic'
     Composite
       &Numeric = SetLanguage(!"Arabic")
       Actions.GoHome()
     EndComposite
   Endevent

   Event 'English'
     Composite
       &Numeric = SetLanguage(!"English")
       Actions.GoHome()
     EndComposite
   EndEvent
   ```
2. You must use [SetTheme function](https://wiki.genexus.com/commwiki/wiki?21777) and [SetLanguage function](https://wiki.genexus.com/commwiki/wiki?18757) together, when using Web Panels with [Theme object](https://wiki.genexus.com/commwiki/wiki?16595) or DSO with a value other than None in the Base CSS property.  
     
   For example, taking the example above and assuming you use the [Web Master Panel object](https://wiki.genexus.com/commwiki/wiki?10348), the code should look like the following:

   ```
   Event 'SetEnglish'
       &i = SetTheme(!"Carmine")
       &i = SetLanguage(!"English")
       refresh
   EndEvent

   Event 'SetArabic'
       &i = SetTheme(!"CarmineRTL")
       &i = SetLanguage(!"Arabic")
       refresh
   EndEvent
   ```

   This will enable a smooth transitioning between interfaces once a language change is detected.

### [See Also](#See+Also)

[HowTo: Add RTL styles](https://wiki.genexus.com/commwiki/wiki?42319)


|  |
| --- |
| **Backlinks** |
| [Toc:Getting ready for Right-to-Left Development](https://wiki.genexus.com/commwiki/wiki?42322) | [Real-time translation of RTL languages (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54495) | [Translation types](https://wiki.genexus.com/commwiki/wiki?54437) |

---
