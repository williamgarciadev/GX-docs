---
title: "DFWOpen function"
source_id: 8372
source_url: https://wiki.genexus.com/commwiki/wiki?8372
genexus_version: "18"
---

# DFWOpen function

**Warning**: This function is maintained for backward compatibility. It is strongly recommended to use the [File data type](https://wiki.genexus.com/commwiki/wiki?6915), its properties, and methods instead of this function.

Opens a text file for processing.  It is the first function to call to begin writing a text file.

### [Syntax](#Syntax)

**DFWOpen(***FileName* [ **,**  *fdel* [ **,**  *sdel* [ **,**  *append* [ **,**  *encoding* ] ] ] ] **)**

**Where:**  
  
*FileName*  
    It can be an attribute, variable or constant of the character type.  Its value will be considered as the file name to be processed.  It may contain directory specifications or not.  If it does not have them, it will be created in the current directory.

*fdel*  
    It can be an attribute, variable or constant of the character type, optional, which indicates the delimiter character among fields.  If you wish to specify the tab character as a separator, the value of this parameter must be the string “\t” string.

*sdel*  
    It can be an attribute, variable or constant of the character type, optional,  which indicates the delimiter character of the string fields.  Only the first character of the parameter value is considered.  Its value may be any character not appearing in the texts.  Its default value is the “ (quotation mark).

*append*  
    It can be an attribute, variable or constant of the numeric type, optional, which indicates what to do if the file exists. If it is 1, the file will be opened for append; if it is 0, the file will be overwritten with a new one.

*encoding*  
    It can be an attribute, variable or constant of the character type, optional, which indicates the encoding to be used to write the file. If you specify this parameter, it means that the length used in the function DFWPTxt means “number of bytes”.

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
| **0** | Successful operation | The file has been opened. |
| **-1** | Wrong sequence | It occurs when this function is called more than once without previously calling the dfwclose function. If the trace is activated you will see the ADF0005 message indicating this error. |
| **-2** | Opening error | It occurs when the file identified as <filename> could not be opened. The cause may be clearly identified by enabling the trace and looking for the message with ADF0001 code. It is most common for the file not to exist. |
| **-8** | Not enough memory | It occurs when it is not possible to reserve a buffer of <length> bytes.  If the trace is activated you will see the ADF0007 message indicating this error. |

### [See Also](#See+Also)

[Delimited ASCII files functions](https://wiki.genexus.com/commwiki/wiki?8364)


|  |
| --- |
| **Backlinks** |
| [Delimited ASCII files functions](https://wiki.genexus.com/commwiki/wiki?8364) | [Encodings in GeneXus](https://wiki.genexus.com/commwiki/wiki?19316) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) |
| [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |

---
