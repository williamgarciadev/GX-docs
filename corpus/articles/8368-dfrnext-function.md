---
title: "DFRNext function"
source_id: 8368
source_url: https://wiki.genexus.com/commwiki/wiki?8368
genexus_version: "18"
---

# DFRNext function

**Warning**: This function is maintained for backward compatibility. It is strongly recommended to use the [File data type](https://wiki.genexus.com/commwiki/wiki?6915), its properties, and methods instead of this function.

Reads the following record (line) of a delimited text file. A line is defined as a sequence of characters followed by a line feed ("\n"), a carriage return ("\r"), or a carriage return immediately followed by a line feed ("\r\n"). The string that is returned does not contain the terminating carriage return or line feed.

### [Syntax](#Syntax)

**DFRNext()**  
  
**Type Returned:**  
Numeric

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Values](#Values)

This function may return some of the following values:

|  |  |  |
| --- | --- | --- |
| **Value** | **Result** | **Description** |
| **0** | Successful operation. | The record has been read. |
| **-1** | Wrong sequence. | It occurs when this function is called before calling the dfropen function, or when this call returned a value other than zero (error). |
| **-3** | Reading error. | It occurs when an error has occurred when reading a line of the delimited ASCII file.  The cause may be clearly identified, enabling the trace and looking for the message with code ADF0002. |
| **-4** | End of data. |  |

### [Samples](#Samples)

For this example, the parameter field separator is not required.

```
&Text = ""
&i = DFRopen( "Test.txt",1024,,"")
If &I = 0
    Do while DFRnext( ) = 0
       &i = DFRgtxt(&Linetxt) // The length of the line is given by the size of the variable.
       &Text = &Text + Newline() + &Linetxt
    EndDo
    &i = DFRclose( )
else
    &Text = "Could not open file"
EndIf
```

### [See Also](#See+Also)

[Delimited ASCII files functions](https://wiki.genexus.com/commwiki/wiki?8364)


|  |
| --- |
| **Backlinks** |
| [Delimited ASCII files functions](https://wiki.genexus.com/commwiki/wiki?8364) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |

---
