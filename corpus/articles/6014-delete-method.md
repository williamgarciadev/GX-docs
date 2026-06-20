---
title: "Delete method"
source_id: 6014
source_url: https://wiki.genexus.com/commwiki/wiki?6014
genexus_version: "18"
---

# Delete method

Deletes, from the server, the last message that was received via the *Receive* method.

### [Syntax](#Syntax)

**&***VarBasedOnExtendedDataType***.Delete()**  
  
**Type Returned:**   
Numeric

### [Scope](#Scope)

**Extended Data Types:** [MAPISession](https://wiki.genexus.com/commwiki/wiki?6935), [OutlookSession](https://wiki.genexus.com/commwiki/wiki?6936), [POP3Session](https://wiki.genexus.com/commwiki/wiki?6966)  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258),
Ruby (up to GeneXus X Evolution 3),
Visual Basic (up to GeneXus X Evolution 3),
Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

* **MAPISession/OutlookSession:** The deleted message will be moved to the “Deleted Items” folder.
* **POP3Session:** The message is permanently deleted, and this is performed when the *Logout* is executed.
* If the *Receive* method was not called, or if the last call did not return a message (for instance, due to an error), the call to *Delete* will result in Error 26.

**Note**: This method returns an error code, so it is possible to call it as follows: **&**Err **=** **&**DataType**.Delete()**

### [See Also](#See+Also)

[Receive method](https://wiki.genexus.com/commwiki/wiki?6964)  
[Send method](https://wiki.genexus.com/commwiki/wiki?6965)  
[MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935)  
[OutlookSession Data Type](https://wiki.genexus.com/commwiki/wiki?6936)  
[POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966)


|  |
| --- |
| **Backlinks** |
| [Err variable](https://wiki.genexus.com/commwiki/wiki?51028) | [GeneXus deprecated functions, methods, and rules](https://wiki.genexus.com/commwiki/wiki?6620) |
| [MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935) | [OutlookSession Data Type](https://wiki.genexus.com/commwiki/wiki?6936) | [POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966) |

---
