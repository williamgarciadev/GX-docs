---
title: "Unbind method"
source_id: 7053
source_url: https://wiki.genexus.com/commwiki/wiki?7053
genexus_version: "18"
---

# Unbind method

Leaves a document open, after ending the application.

### [Syntax](#Syntax)

**&***DataType***.Unbind()**  
  
**Type Returned:**   
Numeric

### [Scope](#Scope)

**Extended Data Types:** [ExcelDocument](https://wiki.genexus.com/commwiki/wiki?2476), [WordDocument](https://wiki.genexus.com/commwiki/wiki?2478,,)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

This method is useful to keep a document open after you have lost reach of the object, even after the application is finished.   
When releasing a document, the reference between the object and the open document is totally lost. Operations on the object no longer affect the document. In fact, the object behaves as if it didn't have an open document, until the *Open* method is called again.

**Note**: This method returns an error code, so it is possible to call it as a function (**&**Err **=** **&**DataType**.Unbind()**).

### [See Also](#See+Also)

[Open Method](https://wiki.genexus.com/commwiki/wiki?6992)  
[ExcelDocument Data Type](https://wiki.genexus.com/commwiki/wiki?2476)  
[WordDocument Data Type](https://wiki.genexus.com/commwiki/wiki?2478,,)


|  |
| --- |
| **Backlinks** |
| [ExcelDocument data type](https://wiki.genexus.com/commwiki/wiki?2476) |

---
