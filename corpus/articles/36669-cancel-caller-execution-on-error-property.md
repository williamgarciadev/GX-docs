---
title: "Cancel caller execution on error property"
source_id: 36669
source_url: https://wiki.genexus.com/commwiki/wiki?36669
genexus_version: "18"
---

# Cancel caller execution on error property

Indicates that the execution of the calling programs should stop if the call fails.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | The execution will not be cancelled. |
| **Yes** | The execution will be cancelled. This is the default value. |

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293)

### [Description](#Description)

This property is enabled only when the [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) is set to the value ‘SOAP’. If it is set to ‘No’, the execution will not be canceled. The error numeric code can be obtained with the GetSOAPErr() function, and the error message through the GetSOAPErrMsg() function.

### [See Also](#See+Also)

[CancelOnError Property](https://wiki.genexus.com/commwiki/wiki?7020)  
[Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947)  
[GetSOAPErr function](https://wiki.genexus.com/commwiki/wiki?7021)  
[GetSOAPErrMsg function](https://wiki.genexus.com/commwiki/wiki?7022)
