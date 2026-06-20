---
title: "Underline Property"
source_id: 6956
source_url: https://wiki.genexus.com/commwiki/wiki?6956
genexus_version: "18"
---

# Underline Property

Specifies whether the cells are shown underlined or not.

### [Syntax](#Syntax)

**&***ExcelDocument***.Cells*(****Row, Column,*[ *Height***,** *Width* ] **).Underline    
&**Excelfont**.Underline**  
  
**Where:**  
  
**&***ExcelDocument*Is a variable based on the [ExcelCells data type](https://wiki.genexus.com/commwiki/wiki?6958).

*Cells*  
    Refers to the [Cells method](https://wiki.genexus.com/commwiki/wiki?6957). Read the above link to find out about its parameters.

**&***Excelfont*Is a variable based on the [ExcelFont Data Type](https://wiki.genexus.com/commwiki/wiki?46318).

**Type Returned:**   
Numeric

### [Scope](#Scope)

**Data Types:** [ExcelCells](https://wiki.genexus.com/commwiki/wiki?6958) [ExcelFont](https://wiki.genexus.com/commwiki/wiki?46318)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604),

[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

The Underline property will return the value 1 only if all the cells in the ExcelCells object are underlined. Otherwise, it will return a 0.

### [See Also](#See+Also)

[Cells Method](https://wiki.genexus.com/commwiki/wiki?6957)  
[ExcelCells Data Type](https://wiki.genexus.com/commwiki/wiki?6958)  
[ExcelDocument Data Type](https://wiki.genexus.com/commwiki/wiki?2476)  
[ExcelSpreadSheet data type](https://wiki.genexus.com/commwiki/wiki?46040)  
[HowTo: Format plain text programmatically](https://wiki.genexus.com/commwiki/wiki?31657)


|  |
| --- |
| **Backlinks** |
| [ExcelCells data type](https://wiki.genexus.com/commwiki/wiki?6958) | [ExcelFont Data Type](https://wiki.genexus.com/commwiki/wiki?46318) |

---
