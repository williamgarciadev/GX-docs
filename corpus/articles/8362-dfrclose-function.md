---
title: "DFRClose function"
source_id: 8362
source_url: https://wiki.genexus.com/commwiki/wiki?8362
genexus_version: "18"
---

# DFRClose function

**Warning**: This function is maintained for backward compatibility. It is strongly recommended to use the [File data type](https://wiki.genexus.com/commwiki/wiki?6915), its properties, and methods instead of this function.

Closes the file opened by DFROpen. This function must be called after a successful call (without error) to DFROpen.

### [Syntax](#Syntax)

**DFRClose()**  
  
**Type Returned:**  
Numeric

### [Scope](#Scope)

**Objects:**   [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:**  [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Values](#Values)

This function may return some of the following values:

|  |  |  |
| --- | --- | --- |
| **Value** | **Result** | **Description** |
| **0** | Successful operation | The file has been read. |
| **-1** | Wrong sequence | It occurs when this function is called before calling the DFROpen function, or when the call to DFROpen returned a value other than zero (error). |

### Samples

For this example, the parameter field separator is not required.

```
&Text = ""
&i = dfropen( "Test.txt",1024,,"") 
If &I = 0
    Do while dfrnext( ) = 0
       &i = dfrgtxt(&Line) // The length of the line is given by the size of the variable.
       &Text = &Text + Newline() + &Line
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
| [Delimited ASCII files functions](https://wiki.genexus.com/commwiki/wiki?8364) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |

---
