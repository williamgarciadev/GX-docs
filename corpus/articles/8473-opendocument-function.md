---
title: "OpenDocument function"
source_id: 8473
source_url: https://wiki.genexus.com/commwiki/wiki?8473
genexus_version: "18"
---

# OpenDocument function

Opens any document that can be opened from the operating system.

### [Syntax](#Syntax)

**&***ret* **= OpenDocument(‘***document**’*****)**  
  
**Type Returned:**  
Numeric

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)   
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),  [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

This function enables you to open any document from the operating system, provided that the association is made (the document type is registered and the application handling it is installed).

If the OpenDocument function was successfully executed, it returns 0 (zero), otherwise it returns a number other than 0, depending on the error.

Similar examples could be: JPGs, PDFs, Word DOCs, (or any Office document), .AVIs (videos), MP3 audio, etc. It is also possible to open a URL with this function (For example: an HTML or a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)).

### [Availability](#Availability)

Since Genexus 16 Upgrade 2 you must include the GXClasses.Win.dll file manually in your deploy when you use this function. See [SAC#44468](https://www.genexus.com/developers/websac?en,,,44468)

This is available for Windows applications and batch procedures.

### [Security Tips](#Security+Tips)

If this function is used, sanitizing external user's inputs is a must.

### [See Also](#See+Also)

[PrintDocument Function](https://wiki.genexus.com/commwiki/wiki?8474)


|  |
| --- |
| **Backlinks** |
| [PrintDocument function](https://wiki.genexus.com/commwiki/wiki?8474) |

---
