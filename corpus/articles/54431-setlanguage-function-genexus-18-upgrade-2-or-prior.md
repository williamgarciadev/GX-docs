---
title: "SetLanguage function (GeneXus 18 Upgrade 2 or prior)"
source_id: 54431
source_url: https://wiki.genexus.com/commwiki/wiki?54431
genexus_version: "18"
---

# SetLanguage function (GeneXus 18 Upgrade 2 or prior)

Sets the language to display literals in your application.

### [Syntax](#Syntax)

**SetLanguage(***LanguageObjectName***)**

### [Scope](#Scope)

**Objects:**[Language](https://wiki.genexus.com/commwiki/wiki?7258)

### [Description](#Description)

The SetLanguage function returns 0 if the Language can be changed. Otherwise, it returns a non-zero value. If the specified [language](https://wiki.genexus.com/commwiki/wiki?7258) cannot be loaded, then no language change is performed and the current language remains as if the method had not been executed. Once the SetLanguage function has been executed successfully, the Language setting remains active for the rest of the session. In Web applications, this means that the GeneXus code automatically saves the value of the current language in the current session.

**Notes:**

* **For Web applications:** In order to refresh all the texts and language dependant elements of the web page, a refresh command should be added after the call to SetLanguage function. This refresh command will make a GET of the web page, a different behavior than if the command is not used after a SetLanguage function (check [SAC #24129](http://www2.gxtechnical.com/portal/hgxpp001.aspx?15,4,61,O,S,0,,24129)). Remember that making a GET of the web page implies that values entered in editable fields will be lost.
* **For Mobile applications:** This function is available from GeneXus X Evolution 3 Upgrade 9 and higher. It's recommendable to use [GoHome Method](https://wiki.genexus.com/commwiki/wiki?31350) after changing the language in order to "refresh" the previously loaded panels.  For it to work set the environment's property "Translation type" to "Run-time".
* **For Evo2, [.NET](https://wiki.genexus.com/commwiki/wiki?38604):** SetLanguage(&MyLanguage) does not always work, but SetLanguage(!'Spanish') or SetLanguage(!'English) does. So use a literal instead of variables if you have troubles with the sample code below.

**Tip**: Remember to set [Translation type property](https://wiki.genexus.com/commwiki/wiki?9126) to "run-time" in order to change the language in runtime and to enable the need language objects in the KB. Otherwise a non-zero value will be returned when the function is used. If Android is used messages like: "set Language to : LanguageId" / "set Language failed. Language LanguageId not found in catalog." appears when debugging (monitor.bat)

### [Samples](#Samples)

```
Event &MyLanguage.Click
   If SetLanguage(&MyLanguage)<>0
      ...
   EndIf
EndEvent

Event &MyLanguage.Click
   &NumericVariable = SetLanguage(!"Spanish")
EndEvent
```

### [See Also](#See+Also)

[GetLanguage function](https://wiki.genexus.com/commwiki/wiki?18751)  
[SetTheme function](https://wiki.genexus.com/commwiki/wiki?41978)
