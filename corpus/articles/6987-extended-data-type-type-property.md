---
title: "Extended Data Type Type Property"
source_id: 6987
source_url: https://wiki.genexus.com/commwiki/wiki?6987
genexus_version: "18"
---

# Extended Data Type Type Property

Returns the value type for a specific cell.

### [Syntax](#Syntax)

**&***ExcelDocument***.Cells(…).Type**  
  
**Type Returned:**   
Character

### [Values](#Values)

**D:** For date or datetime types  
**C:** For character type  
**N:** For numeric type  
**U:** If the type is unknown

### [Description](#Description)

If there are cells with different types in the *ExcelCells* object, the *Type* property will return a “U”.  
This is a read-only property, it cannot be assigned.

### [Scope](#Scope)

**Extended Data Types:** [ExcelCells](https://wiki.genexus.com/commwiki/wiki?6958)  
**Languages:** .NET, Java, Ruby, Visual Basic, Visual FoxPro

### [See Also](#See+Also)

[Cells Method](https://wiki.genexus.com/commwiki/wiki?6957)  
[ExcelCells Data Type](https://wiki.genexus.com/commwiki/wiki?6958)  
[ExcelDocument Data Type](https://wiki.genexus.com/commwiki/wiki?2476)


|  |
| --- |
| **Backlinks** |
| [ExcelCells data type](https://wiki.genexus.com/commwiki/wiki?6958) |

---
