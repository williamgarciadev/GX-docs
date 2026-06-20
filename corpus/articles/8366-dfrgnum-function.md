---
title: "DFRGNum function"
source_id: 8366
source_url: https://wiki.genexus.com/commwiki/wiki?8366
genexus_version: "18"
---

# DFRGNum function

**Warning**: This function is maintained for backward compatibility. It is strongly recommended to use the [File data type](https://wiki.genexus.com/commwiki/wiki?6915), its properties, and methods instead of this function.

Reads a numeric type field of the current line (read by DFRnext).

### [Syntax](#Syntax)

**DFRGNum(***Num***)**  
  
**Where:**  
  
*Num*  
    It can be an attribute or variable of Numeric type. The read value will be stored here.

**Type Returned:**  
Numeric

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Values](#Values)

This function may return some of the following values:

|  |  |  |
| --- | --- | --- |
| **Values** | **Result** | **Definition** |
| **0** | Successful operation | The field has been read |
| **-1** | Wrong sequence | It occurs when this function is called before calling the DFRNext function, or when the last call to DFRNext returned a value other than zero (error). If the trace is enabled, you will see the ADF0004 or ADF0006 message. |
| **-5** | Wrong format | The number in the field does not have the correct format. This is mostly because the field you try to read is of a different type (character, date, etc.). If the trace is enabled, you will see the ADF0008 message. |

### [See Also](#See+Also)

[Delimited ASCII files functions](https://wiki.genexus.com/commwiki/wiki?8364)


|  |
| --- |
| **Backlinks** |
| [Delimited ASCII files functions](https://wiki.genexus.com/commwiki/wiki?8364) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |

---
