---
title: "Real-time translation of RTL languages (GeneXus 18 Upgrade 2)"
source_id: 54495
source_url: https://wiki.genexus.com/commwiki/wiki?54495
genexus_version: "18"
---

# Real-time translation of RTL languages (GeneXus 18 Upgrade 2)

If using runtime translation with RTL and LTR languages, you can switch between them in the following way, using [SetTheme](https://wiki.genexus.com/commwiki/wiki?21777) and [SetLanguage](https://wiki.genexus.com/commwiki/wiki?18757) functions in conjunction. For example, suppose you use English and Arabic languages; the [Web Master Panel object](https://wiki.genexus.com/commwiki/wiki?10348) could include the following code:

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

For [Native Mobile Generator](https://wiki.genexus.com/commwiki/wiki?14451) you don't need to change the Theme object, set the desired language and its recommended to set a *GoHome* command ([Actions external object](https://wiki.genexus.com/commwiki/wiki?31350)):

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


|  |
| --- |
| **Backlinks** |
| [Translation types (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54444) |

---
