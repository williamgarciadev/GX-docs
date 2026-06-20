---
title: "Text Property for Extended Data Types"
source_id: 10197
source_url: https://wiki.genexus.com/commwiki/wiki?10197
genexus_version: "18"
---

# Text Property for Extended Data Types

In ExcelCells, it indicates the value of the cells in text format.

In MailMessage, it is the body of the message in simple text format.

In WordDocument, it indicates the complete text of the document.

### [Syntax](#Syntax)

***&ExcelDocument***.Cells(…).Text

***&DataType***.Text

**Type Returned:**  
Character

**Where:**  
*ExcelDocument*  
   Is an ExcelDocument type variable name

*DataType*  
   Is a MailMessage or WordDocument type variable name

### [Description](#Description)

**WordDocument:** If you want to add new text to an existing document without losing the present format, the Append method is recommended.

**ExcelCells:** If there are cells with different values in the ExcelCells object, the *Text* property will return an empty string.

### [Scope](#Scope)

**Extended Data Types:** [ExcelCells](https://wiki.genexus.com/commwiki/wiki?6958), [MailMessage](https://wiki.genexus.com/commwiki/wiki?6925), [WordDocument](https://wiki.genexus.com/commwiki/wiki?2478,,)  
**Languages:** .NET, Java, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [See Also](#See+Also)

[Append method](https://wiki.genexus.com/commwiki/wiki?6971)  
[Cells method](https://wiki.genexus.com/commwiki/wiki?6957)  
[ExcelCells data type](https://wiki.genexus.com/commwiki/wiki?6958)  
[ExcelDocument data type](https://wiki.genexus.com/commwiki/wiki?2476)  
[MailMessage data type](https://wiki.genexus.com/commwiki/wiki?6925)  
[WordDocument Data Type](https://wiki.genexus.com/commwiki/wiki?2478,,)


|  |
| --- |
| **Backlinks** |
| [Append method](https://wiki.genexus.com/commwiki/wiki?6971) | [ExcelCells data type](https://wiki.genexus.com/commwiki/wiki?6958) | [MailMessage data type](https://wiki.genexus.com/commwiki/wiki?6925) |
| [Text method](https://wiki.genexus.com/commwiki/wiki?8841) |

---
