---
title: "DFRGDate function"
source_id: 8365
source_url: https://wiki.genexus.com/commwiki/wiki?8365
genexus_version: "18"
---

# DFRGDate function

**Warning**: This function is maintained for backward compatibility. It is strongly recommended to use the [File data type](https://wiki.genexus.com/commwiki/wiki?6915), its properties, and methods instead of this function.

Reads a date type field of the current line (read by DFRNext). The date value **is not** adjusted according to the "First  Year of 20th Century" (generator property).

### [Syntax](#Syntax)

**DFRGDate(***Date* [ , *fmt* [ , *sep* ] ] **)**  
  
**Where:**  
  
*Date*  
    It can be a date type attribute or variable.  The read value is stored here.  
  
*fmt*  
    It can be a character type attribute, variable or constant, optional, with at least three characters. It indicates the format that the date has in the field to be read. Each field character may have the “y”, “m” or “d” values.  Their combination generates the format.  For example, if the string contains the “ymd” characters the field date to be read is assumed (and validated) in Year, Month Day format. If, on the contrary, the string contains the “dmy” characters, the field date to be read is assumed in Day, Month, and Year format. It is **important** to note that the characters **must** be in lowercase letters. The **default value** is “ymd”.  
  
*sep*  
    It can be an attribute, variable or constant of character type, which value must have **at least** one character. It indicates which the element separator of a date is.  The values commonly used are “/”, “-“and “.”. The **default** **value** is “-”.

**Type Returned:**  
Numeric

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** 
[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Values](#Values)

|  |  |  |
| --- | --- | --- |
| **Value** | **Result** | **Description** |
| **0** | Successful operation | The field has been read. |
| **-1** | Wrong sequence | It occurs when you call this function before calling the dfrnext function, or the last call to dfrnext returned a value other than zero (error). If the trace is enabled you will see the ADF0004 or ADF0006 message. |
| **-5** | Wrong format | The string in the field does not have the right format. This is mostly because the field you are trying to read is of a different type (number, date, etc.). |
| **-7** | Invalid date | The found value in the field does not correspond to a valid date. Normally, it occurs because the (fmt) format or the (sep) separator does not correspond to those in the file. If the trace is enabled, you will see the ADF0010 message. |
| **-10** | Wrong Format | The fmt parameter has a wrong format. If the trace is enabled, you will see the ADF0012 message. |

### [See Also](#See+Also)

[Delimited ASCII files functions](https://wiki.genexus.com/commwiki/wiki?8364)


|  |
| --- |
| **Backlinks** |
| [Delimited ASCII files functions](https://wiki.genexus.com/commwiki/wiki?8364) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |

---
