---
title: "DFWNext function"
source_id: 8371
source_url: https://wiki.genexus.com/commwiki/wiki?8371
genexus_version: "18"
---

# DFWNext function

**Warning**: This function is maintained for backward compatibility. It is strongly recommended to use the [File data type](https://wiki.genexus.com/commwiki/wiki?6915), its properties, and methods instead of this function.

Saves the record with the values specified by the previous calls to DFWPTxt, DFWPNum, etc., in the delimited text file.

### [Syntax](#Syntax)

**DFWNext()**  
  
**Type Returned:**  
Numeric

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Values](#Values)

This function may return some of the following values:

|  |  |  |
| --- | --- | --- |
| **Value** | **Result** | **Description** |
| **0** | Successful operation | The record has been read. |
| **-1** | Wrong sequence | It occurs when this function is called before calling the DFWOpen function, or when the call to DFWOpen returns a value other than zero (error). |
| **-9** | Recording error | It occurs when an error has occurred upon saving the line in the delimited ASCII file. The cause may be clearly identified by enabling the trace and looking for the message with the code ADF0003 |

### [See Also](#See+Also)

[Delimited ASCII files functions](https://wiki.genexus.com/commwiki/wiki?8364)


|  |
| --- |
| **Backlinks** |
| [Delimited ASCII files functions](https://wiki.genexus.com/commwiki/wiki?8364) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |

---
