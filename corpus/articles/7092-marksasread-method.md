---
title: "MarksAsRead method"
source_id: 7092
source_url: https://wiki.genexus.com/commwiki/wiki?7092
genexus_version: "18"
---

# MarksAsRead method

Marks the last message received through the *Receive* method as read.

### [Syntax](#Syntax)

**&***VarBasedOnExtendedDataType***.MarksAsRead()**  
  
**Type Returned:**   
Numeric

### [Scope](#Scope)

**Extended Data Types:** [MAPISession](https://wiki.genexus.com/commwiki/wiki?6935), [OutlookSession](https://wiki.genexus.com/commwiki/wiki?6936)  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

If the *Receive* method was not called, or if the last call did not return a message (for instance, due to an error), the call to *MarkAsRead* results in error 26.   
This property must be configured after performing the *Receive*.  
  
**Notes:**

* In order to use this property you must set the “Functions” property with the “Allow non-standard functions on saving” value in design, and the prototype/production “Functions” property with the “Allow non-standard functions on specifying” value.
* This method returns an error code, so it is possible to call it as follows: **&**Err **=** **&**DataType**.MarksAsRead()**

### 

### [See Also](#See+Also)

[Receive Method](https://wiki.genexus.com/commwiki/wiki?6964)  
[Send Method](https://wiki.genexus.com/commwiki/wiki?6965)  
[MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935)  
[OutlookSession Data Type](https://wiki.genexus.com/commwiki/wiki?6936)


|  |
| --- |
| **Backlinks** |
| [MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935) | [OutlookSession Data Type](https://wiki.genexus.com/commwiki/wiki?6936) |

---
