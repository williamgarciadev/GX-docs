---
title: "SetLanguage function"
source_id: 18757
source_url: https://wiki.genexus.com/commwiki/wiki?18757
genexus_version: "18"
---

# SetLanguage function

Sets the language to display the texts and messages in your application.

### [Syntax](#Syntax)

**SetLanguage(**LanguageObjectName**)**

**Where:**

*LanguageObjectName*Name of the [Language object](https://wiki.genexus.com/commwiki/wiki?7258) defined in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) to be used for the translation.

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

The SetLanguage function is used when the [Translation type property](https://wiki.genexus.com/commwiki/wiki?9126) is set to 'Run-time'.

You have to use this function in your code to indicate the language to be used.

It returns 0 if the Language can be changed. Otherwise, it returns a non-zero value. If the specified Language cannot be loaded, then no language change is performed and the current Language remains as if the method had not been executed.

Once the SetLanguage function has been executed successfully, the Language setting remains active for the rest of the session. In Web applications, this means that the GeneXus code automatically saves the value of the current language in the current session.

**Notes:**

* **For Web applications:** To refresh all the texts and language-dependant elements of the web page, a [Refresh command](https://wiki.genexus.com/commwiki/wiki?25069) should be added after the SetLanguage function. This Refresh command will make a GET of the web page (a different behavior than if the Refresh command is not used after the SetLanguage function). Read [SAC #24129](https://www.genexus.com/en/developers/websac?data=24129;;). Remember that making a GET of the web page implies that values entered in editable fields will be lost.  
    
  Browsers running GeneXus applications using [Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) require support for the 'dir' attribute ([HTML attribute: dir](https://caniuse.com/?search=html%20dir%20attribute),  [CSS Logical Properties](https://caniuse.com/?search=logical%20properties)). Read [SAC #52783](https://www.genexus.com/developers/websac?en,,,52783).
* **For Mobile applications:** This function is available from GeneXus X Evolution 3 Upgrade 9 onwards. It's recommended to use the [GoHome Method of the Actions external object](https://wiki.genexus.com/commwiki/wiki?31350) after changing the language to "refresh" the previously loaded [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s. For it to work, the Environment's [Translation type property](https://wiki.genexus.com/commwiki/wiki?9126) must be set to 'Run-time'. Otherwise, a non-zero value will be returned when the function is used. In Android, messages like: "set Language to : LanguageId" / "set Language failed. Language LanguageId not found in catalog." appear when debugging (monitor.bat).
* **For GeneXus X Evolution 2, [.NET](https://wiki.genexus.com/commwiki/wiki?38604):** SetLanguage(&MyLanguage) does not always work. However, SetLanguage(!'Spanish') or SetLanguage(!'English) does. Therefore, type the Language Name instead of using variables if you have problems with the sample code below.

### [Samples](#Samples)

```
Event &MyLanguage.Click
   If SetLanguage(&MyLanguage)<>0
      msg("It was not possible to set the language " + &MyLanguage)
   EndIf
EndEvent

Event &MyLanguage.Click
   &NumericVariable = SetLanguage(!"Spanish")
EndEvent
```

### [See Also](#See+Also)

[GetLanguage function](https://wiki.genexus.com/commwiki/wiki?18751)  
[GeneXus Application Localization](https://wiki.genexus.com/commwiki/wiki?6330)


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
| [Table of contents:GeneXus Application Localization](https://wiki.genexus.com/commwiki/wiki?6330) | [GetLanguage function](https://wiki.genexus.com/commwiki/wiki?18751) | [Real-time translation of RTL languages](https://wiki.genexus.com/commwiki/wiki?54482) | [Real-time translation of RTL languages (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54495) |
| [SetLanguage function (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54431) | [SetTheme function for Web](https://wiki.genexus.com/commwiki/wiki?21777) | [Translation types](https://wiki.genexus.com/commwiki/wiki?54437) | [Translation types (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54444) |

---
