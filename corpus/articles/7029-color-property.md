---
title: "Color Property"
source_id: 7029
source_url: https://wiki.genexus.com/commwiki/wiki?7029
genexus_version: "18"
---

# Color Property

This property is used to specify:

* the color of the cells (excel cells).
* the color in the rules (transactions and work panels).

### [Syntax (in runtime for Excel Cells)](#Syntax+%28in+runtime+for+Excel+Cells%29)

**&***ExcelDocument***.Cells(…).Color**  
&*ExcelBorderStyle*.Color  
&*excelFont*.Color  
  
**Type Returned:**   
Numeric

### [Values](#Values)

#### [In runtime for Excel cells](#In+runtime+for+Excel+cells)

**Positive Value:** The Excel color index number corresponding to the number indicated will be taken as the value. Ref. <https://docs.microsoft.com/en-us/office/vba/api/Excel.ColorIndex>  
**Negative Value (except –1):** The color number in the RGB scheme corresponding to the absolute number indicated will be the value taken (i.e.: as a value returned by the RGB function).  
**-1:** The default color defined by Excel will be taken.

For [ExcelSpreadSheet data type](https://wiki.genexus.com/commwiki/wiki?46040) methods return a [ExcelColor data type](https://wiki.genexus.com/commwiki/wiki?46086)

#### [In the Color property for transactions and work panels.](#In+the+Color+property+for+transactions+and+work+panels.)

**Default to color rule:** specify the default value specified in the Options command menu.  
Any other color of the possibles.

### [Description](#Description)

If there are cells with different colors in the *ExcelCells* object, this property will return a 0.

### [Scope](#Scope)

**Extended Data Types:** [ExcelCells](https://wiki.genexus.com/commwiki/wiki?6958),[ExcelBorderStyle data type](https://wiki.genexus.com/commwiki/wiki?46308), [ExcelFont Data Type](https://wiki.genexus.com/commwiki/wiki?46318) [Transactions](https://wiki.genexus.com/commwiki/wiki?1908), [Work Panels](https://wiki.genexus.com/commwiki/wiki?7387,,)  
**Languages:** .NET, Java

### [See Also](#See+Also)

[Cells Method](https://wiki.genexus.com/commwiki/wiki?6957)  
[ExcelCells Data Type](https://wiki.genexus.com/commwiki/wiki?6958)  
[ExcelDocument Data Type](https://wiki.genexus.com/commwiki/wiki?2476)  
[ExcelSpreadSheet data type](https://wiki.genexus.com/commwiki/wiki?46040)  
[Styles tab in the Editors configurations](https://wiki.genexus.com/commwiki/wiki?6780)


|  |
| --- |
| **Backlinks** |
| [ExcelBorderStyle data type](https://wiki.genexus.com/commwiki/wiki?46308) | [ExcelCells data type](https://wiki.genexus.com/commwiki/wiki?6958) | [ExcelFont Data Type](https://wiki.genexus.com/commwiki/wiki?46318) |

---
