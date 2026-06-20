---
title: "Cells method"
source_id: 6957
source_url: https://wiki.genexus.com/commwiki/wiki?6957
genexus_version: "18"
---

# Cells method

Returns a cell or a group of cells.

### [Syntax](#Syntax)

**&***ExcelDocument***.Cells*(****Row, Column,*[ *Height***,** *Width* ] **)**  
  
**Where:**  
  
*Row*  
     Is the row where the area will begin.  
  
*Column*  
     Is the column where the area will begin.  
  
*Height*  
     Is the height of the cells.  
  
*Width*  
     Is the width of the cells.

**Type Returned:**   
Numeric

### [Scope](#Scope)

**Extended Data Types:** [ExcelDocument data type](https://wiki.genexus.com/commwiki/wiki?2476)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

It returns an ExcelCells object with cells forming the area which starts on a Row (row specified) and Column (column specified) and has a certain Height (cell height indicated) and Width (cells width indicated).   
If the Heightand Width parameters are not specified, only the cell located in the Row and Column will be returned.

**Note**: This method returns an error code, so it is possible to call it as a function (**&**Err **=** **&**ExcelDocument.**Cells(…..)**).

### [See Also](#See+Also+)

[ExcelCells Data Type](https://wiki.genexus.com/commwiki/wiki?6958)  
[ExcelDocument Data Type](https://wiki.genexus.com/commwiki/wiki?2476)


|  |
| --- |
| **Backlinks** |
| [Bold Property](https://wiki.genexus.com/commwiki/wiki?6986) | [Color Property](https://wiki.genexus.com/commwiki/wiki?7029) | [Date Property](https://wiki.genexus.com/commwiki/wiki?7036) |
| [ExcelCells data type](https://wiki.genexus.com/commwiki/wiki?6958) | [ExcelDocument data type](https://wiki.genexus.com/commwiki/wiki?2476) | [ExcelSpreadSheet data type](https://wiki.genexus.com/commwiki/wiki?46040) | [Extended Data Type Font Property](https://wiki.genexus.com/commwiki/wiki?7002) |
| [Extended Data Type Size Property](https://wiki.genexus.com/commwiki/wiki?7004) | [Extended Data Type Type Property](https://wiki.genexus.com/commwiki/wiki?6987) | [Italic Property](https://wiki.genexus.com/commwiki/wiki?6973) | [Number Property](https://wiki.genexus.com/commwiki/wiki?7010) |
| [Text Property for Extended Data Types](https://wiki.genexus.com/commwiki/wiki?10197) | [Underline Property](https://wiki.genexus.com/commwiki/wiki?6956) | [Value property for ExcelCells data type](https://wiki.genexus.com/commwiki/wiki?22868) |

---
