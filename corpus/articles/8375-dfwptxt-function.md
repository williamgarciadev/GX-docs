---
title: "DFWPTxt function"
source_id: 8375
source_url: https://wiki.genexus.com/commwiki/wiki?8375
genexus_version: "18"
---

# DFWPTxt function

**Warning**: This function is maintained for backward compatibility. It is strongly recommended to use the [File data type](https://wiki.genexus.com/commwiki/wiki?6915), its properties, and methods instead of this function.

Saves a character type field in the current record of the delimited ASCII file.

### [Syntax](#Syntax)

**DFWPTxt(** *text* [ , *length* ] **)**  
  
**Where:**  
  
*text*  
   It can be an attribute, variable or constant of the character type. Its value will be saved in the corresponding field.  
  
*length*  
   It can be an attribute, variable or constant of the numeric type and it is optional. It indicates the number of characters to be saved.  In case they are omitted, it is assumed as the size defined for the <txt> parameter.

**Note**: If the parameter *encoding* was specified in the function DFWOpen, this length means “number of bytes”.

**Type returned:**  
Numeric

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:**  [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3).

### [Values](#Values)

This function may return some of the following values:

|  |  |  |
| --- | --- | --- |
| **Value** | **Result** | **Description** |
| **0** | Successful operation | The field has been saved. |
| **-1** | Wrong sequence | It occurs when this function is called before calling the DFWOpen function, or when the last call to DFWOpen returned a value other than zero (error). If the trace is enabled, you will see the ADF0004 message. |

### [See Also](#See+Also)

[Delimited ASCII files functions](https://wiki.genexus.com/commwiki/wiki?8364)


|  |
| --- |
| **Backlinks** |
| [Delimited ASCII files functions](https://wiki.genexus.com/commwiki/wiki?8364) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |

---
