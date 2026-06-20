---
title: "CancelOnError Property"
source_id: 7020
source_url: https://wiki.genexus.com/commwiki/wiki?7020
genexus_version: "18"
---

# CancelOnError Property

This property is used to indicate how errors will be handled when calling a GeneXus object through SOAP and when invoking a Web Service imported with GeneXus WSDL Inspector.

### [Syntax](#Syntax)

**&***DataType***.CancelOnError**  
  
**Type Returned:**   
Numeric

### [Values](#Values)

|  |  |
| --- | --- |
| **0** | For SOAP it calls the behavior depends on the value of the Cancel Caller Execution On Error Property.  For Web Services invocation caller program will always cancel execution.  This is the default value. |
| **1** | Caller program cancels execution when an error occurs. |
| **2** | Caller program does not stop execution. Error information can be obtained using the [GetSoapErr](https://wiki.genexus.com/commwiki/wiki?7021) and [GetSoapErrMsg](https://wiki.genexus.com/commwiki/wiki?7022) functions. |

### [Scope](#Scope)

**Extended Data Types:** [Location](https://wiki.genexus.com/commwiki/wiki?6981)  
**Languages:** .NET, Java, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [See Also](#See+Also)

[Location Data Type](https://wiki.genexus.com/commwiki/wiki?6981)  
[Locations](https://wiki.genexus.com/commwiki/wiki?6981)


|  |
| --- |
| **Backlinks** |
| [Cancel caller execution on error property](https://wiki.genexus.com/commwiki/wiki?36669) | [Location data type](https://wiki.genexus.com/commwiki/wiki?6981) |

---
