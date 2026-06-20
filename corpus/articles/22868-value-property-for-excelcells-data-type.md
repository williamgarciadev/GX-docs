---
title: "Value property for ExcelCells data type"
source_id: 22868
source_url: https://wiki.genexus.com/commwiki/wiki?22868
genexus_version: "18"
---

# Value property for ExcelCells data type

Indicates the value (result) of formula cells in text format.

### Syntax

**&***ExcelDocument***.Cells(…).***Value*  
  
**Type Returned:**   
Character

### Description

It returns the result of the selected formula cells of the Excel Document in text format.

If the result type of this formula is a date or number, then returns the ToString () of the value.

If the cell is not a formula, then returns the ToString() of the value contained on the cell.

### Considerations

This property is readonly. It cannot be assigned.

### Availability

Since GeneXus X Evolution 2 Upgrade 4.

### Scope

|  |  |
| --- | --- |
| **Extended data types** | [ExcelCells data type](https://wiki.genexus.com/commwiki/wiki?6958) |
| **Languages** | .NET, Java |
|  |  |

### See also

[Cells Method](https://wiki.genexus.com/commwiki/wiki?6957)  
[ExcelCells Data Type](https://wiki.genexus.com/commwiki/wiki?6958)  
[ExcelDocument Data Type](https://wiki.genexus.com/commwiki/wiki?2476)


|  |
| --- |
| **Backlinks** |
| [ExcelCells data type](https://wiki.genexus.com/commwiki/wiki?6958) |

---
