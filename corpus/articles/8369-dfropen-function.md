---
title: "DFROpen function"
source_id: 8369
source_url: https://wiki.genexus.com/commwiki/wiki?8369
genexus_version: "18"
---

# DFROpen function

**Warning**: This function is maintained for backward compatibility. It is strongly recommended to use the [File data type](https://wiki.genexus.com/commwiki/wiki?6915), its properties, and methods instead of this function.

Opens a text file for its processing.  It is the first function to be called to begin reading a text file.

### [Syntax](#Syntax)

**DFROpen(**FileName [ , length [ ,  fdel [ ,  sdel [ ,  encoding ] ] ] ] **)**

**Where:**  
  
*FileName*  
    It can be an attribute, variable or constant of the char type.  Its value will be considered as the file name to be processed.  It may contain directory specifications or not.  If it doesn’t, it will be searched in the current directory.

*length (deprecated)*  
    It can be an attribute, variable or constant of the numeric type, optional, which indicates the maximum size, in number of characters, of the record to be read.  See that the delimited ASCII files have records (lines) of variable length.  If specified, the value should correspond to the maximum quantity of characters that a line may have.  The default value is 1024.

*fdel*  
    It can be an attribute, variable or constant of the character type, optional, which indicates the delimiting character among fields.  If you wish to specify the tab character as separator, the value of this parameter must be the string “\t”.  The default value is "," (comma).

*sdel*  
    It can be an attribute, variable or constant of the character type, optional,  which indicates the delimiting character of the string fields.  Only the first character of the parameter value is considered.  Its value may be any character not appearing in the texts.  Thedefault value is “ (quotation mark).

*encoding*  
    It can be an attribute, variable or constant of the character type, optional, which indicates the encoding to be used to read the file. If you specify this parameter, it means that the length used in the function [DFRGTxt](https://wiki.genexus.com/commwiki/wiki?8367) means “number of bytes”.

**Type Returned:**  
Numeric

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),  [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Values](#Values)

This function may return some of the following values:

|  |  |  |
| --- | --- | --- |
| **Value** | **Result** | **Description** |
| **0** | Successful operation. | The file has been opened. |
| **-1** | Wrong sequence. | It occurs when this function is called more than once without previously calling the DFRClose function. If the trace is activated you will see the ADF0005 message indicating this error. |
| **-2** | Opening error. | It occurs when the file identified as <filename> could not be opened.  The cause may be identified by enabling the trace and looking for the message with ADF0001 code. It is most common that the file does not exist. |
| **-8** | Not enough memory. | It occurs when it isn’t possible to reserve a buffer of <length> bytes.  If the trace is activated, you will see the ADF0007 message indicating this error. |

### [Sample](#Sample)

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
| [Delimited ASCII files functions](https://wiki.genexus.com/commwiki/wiki?8364) | [DFRGTxt function](https://wiki.genexus.com/commwiki/wiki?8367) | [Encodings in GeneXus](https://wiki.genexus.com/commwiki/wiki?19316) |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |

---
