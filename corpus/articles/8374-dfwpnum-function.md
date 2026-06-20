---
title: "DFWPNum function"
source_id: 8374
source_url: https://wiki.genexus.com/commwiki/wiki?8374
genexus_version: "18"
---

# DFWPNum function

**Warning**: This function is maintained for backward compatibility. It is strongly recommended to use the [File data type](https://wiki.genexus.com/commwiki/wiki?6915), its properties, and methods instead of this function.

Saves a numeric type field in the current record of the delimited ASCII file.

### [Syntax](#Syntax)

**DFWPNum(***num* [ **,** *dec* ] **)**  
  
**Where:**  
  
*num*  
    It can be an attribute, variable or constant of the numeric type. Its value will be the one saved in the corresponding field.  
  
*dec*  
    It can be an attribute, variable or constant of the numeric type, optional, indicating the decimal quantity to be specified in the field.

**Type Returned:**  
Numeric

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),  [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Values](#Values)

This function may return some of the following values:

|  |  |  |
| --- | --- | --- |
| **Value** | **Result** | **Description** |
| **0** | Successful operation | The field has been saved. |
| **-1** | Wrong sequence | It occurs when this function is called before calling the DFWOpen function, or when the last call to DFWOpen returned a value other than zero (error). If the trace is enabled, you will see the ADF0004 message. |

### [See Also](#See+Also)

[Delimited ASCII files functions](https://wiki.genexus.com/commwiki/wiki?8364)

      {{Category:GeneXus 16 Help}}}


|  |
| --- |
| **Backlinks** |
| [Delimited ASCII files functions](https://wiki.genexus.com/commwiki/wiki?8364) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |

---
