---
title: "CDoW function"
source_id: 8340
source_url: https://wiki.genexus.com/commwiki/wiki?8340
genexus_version: "18"
---

# CDoW function

Returns the weekday for a given date in a selected language. If no language is specified, the one selected in the Model Properties is used.

The value 'spaces' is returned if the received parameter is null.

### [Syntax](#Syntax)

**Cdow(***date-expression* | *datetime-expression* [ **,***language* ] **)**  
  
**Where:**  
  
*language* must be one of the following:

* spa - Spanish
* eng - English
* por - Portuguese
* ita – Italian
* chs - Simplified Chinese
* cht - Traditional Chinese
* jap - Japanese

**Type returned:**  
Character(9)

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Samples](#Samples)

If English is the set language, and no other language is explicitly used in the function:

```
CDOW(CTOD('08/28/08')) = Thursday
```

If you specify 'spa', that is, Spanish as the language, then the result is displayed in Spanish no matter what default language has been set in the Model Properties.

```
CDOW(CTOD('08/28/08'), 'spa') = Jueves
```

**Note**: Implementation is case sensitive (all three characters have to be lowercase).

### [See Also](#See+Also)

[CMonth function](https://wiki.genexus.com/commwiki/wiki?8343)  
[Dow function](https://wiki.genexus.com/commwiki/wiki?8344)


|  |
| --- |
| **Backlinks** |
| [CMonth function](https://wiki.genexus.com/commwiki/wiki?8343) | [Date expressions](https://wiki.genexus.com/commwiki/wiki?24212) | [DayOfWeek method](https://wiki.genexus.com/commwiki/wiki?12657) |
| [Dow function](https://wiki.genexus.com/commwiki/wiki?8344) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
|

---
