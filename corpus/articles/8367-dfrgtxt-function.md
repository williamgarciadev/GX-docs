---
title: "DFRGTxt function"
source_id: 8367
source_url: https://wiki.genexus.com/commwiki/wiki?8367
genexus_version: "18"
---

# DFRGTxt function

**Warning**: This function is maintained for backward compatibility. It is strongly recommended to use the [File data type](https://wiki.genexus.com/commwiki/wiki?6915), its properties, and methods instead of this function.

Reads a character type field of the current line (read by dfrnext).

### [Syntax](#Syntax)

**DFRGTxt(** *Text* [ , *Length* ] **)**  
  
**Where:**  
  
*Text*  
    It can be an attribute or variable or character or varchar type. The read value will be stored here.  
  
*Length*  
    It can be an attribute, variable or constant of numeric type, optional,  indicating the maximum number of characters to be read.  Their value, if specified, **may not exceed** the size defined for <txt>. In case it is omitted, it is assumed as the size defined for the attribute or variable  <txt>. If this parameter exceeds the <txt> size, results become unpredictable.

**Note**: If the parameter *encoding* was specified in the function [DFROpen](https://wiki.genexus.com/commwiki/wiki?8369), this length means “number of bytes”.

**Type Returned:**  
Numeric

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:**  [.NET](https://wiki.genexus.com/commwiki/wiki?38604), , [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Values](#Values)

This function may return some of the following values:

|  |  |  |
| --- | --- | --- |
| **Value** | **Result** | **Description** |
| **0** | Successful operation. | The field has been read. |
| **-1** | Wrong sequence. | It occurs when this function is called before calling the dfrnext function, or when the last call to dfrnext returned a value other than zero (error). If the trace is enabled you will see the ADF0004 or ADF0006 message. |
| **-5** | Wrong format. | The string in the field does not have the correct format. This is mostly because the field you are trying to read is of a different type (number, date, etc.) If the trace is enabled you will see the ADF0009 message. |
| **-6** | Overflow. | This is a warning indicating that the string length in the record is greater than the maximum specified (or assumed) in the <length> parameter. The value read is cut to <length> characters. |

### [Samples](#Samples)

For this example, the parameter field separator is not required.

```
&Text = ""
&i = dfropen( "Test.txt",1024,,"") 
If &I = 0
    Do while dfrnext( ) = 0
       &i = dfrgtxt(&Linetxt) // The length of the line is given by the size of the variable.
       &Text = &Text + Newline() + &Linetxt
    EndDo
    &i = dfrclose( )
else
    &Text = "Could not open file"
EndIf
```

### [See Also](#See+Also)

[Delimited ASCII files functions](https://wiki.genexus.com/commwiki/wiki?8364)


|  |
| --- |
| **Backlinks** |
| [Delimited ASCII files functions](https://wiki.genexus.com/commwiki/wiki?8364) | [DFROpen function](https://wiki.genexus.com/commwiki/wiki?8369) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) |
| [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |

---
