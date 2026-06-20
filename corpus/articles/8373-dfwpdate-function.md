---
title: "DFWPDate function"
source_id: 8373
source_url: https://wiki.genexus.com/commwiki/wiki?8373
genexus_version: "18"
---

# DFWPDate function

**Warning**: This function is maintained for backward compatibility. It is strongly recommended to use the [File data type](https://wiki.genexus.com/commwiki/wiki?6915), its properties, and methods instead of this function.

Saves a date type field in the current record of the delimited ASCII file. If it has GeneXus null value, the date "00/00/0000" will be saved.

### [Syntax](#Syntax)

**DFWPDate(***date* [ , *fmt* [ , *sep* ] ] **)**

**Where:**  
  
*date*  
    It can be an attribute or variable of the date type. The read value will be saved here. It cannot be a constant.

*fmt*  
    It can be an attribute, variable or constant of the character type, optional, with at least three characters. It indicates the format of the date in the field to be saved. Each character of the field may have a “y”, “m” or “d” value. Its combination generates the format. For example, if the string contains the “ymd” character, the field date to be saved is assumed in Year, Month, Day format. If, on the contrary, the string contains the “dmy” characters, the field date to be read is assumed in Day, Month, Year format. It is important to note that the characters should be in small letters. The default value is “ymd”.

*sep*  
    It is a parameter of the character type, optional, with  at least one character. It indicates the separator element of a date. Commonly used values are “/”, “-“ and “.”. The default value is “-”.

**Type Returned:**  
Numeric

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### Values

|  |  |  |
| --- | --- | --- |
| **Value** | **Result** | **Description** |
| **0** | Successful operation | The field has been read. |
| **-1** | Wrong sequence | It occurs when this function is called before calling the dfwopen function, or when the last call to dfwopen returned a value other than zero (error). If the trace is enabled, you will see the ADF0004 message. |
| **-5** | Wrong format | The string in the field does not have the right format. This is mostly because the field you are trying to read is of a different type (number, date, etc.). |
| **-10** | Wrong format | The fmt parameter has a wrong format. If the trace is enabled, you will see the ADF0012 message. |

### [See Also](#See+Also)

[Delimited ASCII Files Functions](https://wiki.genexus.com/commwiki/wiki?8364)


|  |
| --- |
| **Backlinks** |
| [Delimited ASCII files functions](https://wiki.genexus.com/commwiki/wiki?8364) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |

---
