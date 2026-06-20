---
title: "SelectSheet method"
source_id: 7087
source_url: https://wiki.genexus.com/commwiki/wiki?7087
genexus_version: "18"
---

# SelectSheet method

Changes from an active worksheet to a specified one.

### [Syntax](#Syntax)

**&***ExcelDocument***.SelectSheet(***SheetName***)**  
  
**Where:**  
*SheetName*  
   Name of the Sheet that will be selected. When the specified worksheet does not exist, it is created.

**Type Returned:**   
Numeric

### [Scope](#Scope)

**Extended Data Types:** [ExcelDocument](https://wiki.genexus.com/commwiki/wiki?2476)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

**Note**: This method returns an error code, so it is possible to call it as a function (**&**Err **=** **&**ExcelDocument**.SelectSheet(…..)**).

### [See Also](#See+Also)

[ExcelDocument Data Type](https://wiki.genexus.com/commwiki/wiki?2476)


|  |
| --- |
| **Backlinks** |
| [ExcelDocument data type](https://wiki.genexus.com/commwiki/wiki?2476) |

---
