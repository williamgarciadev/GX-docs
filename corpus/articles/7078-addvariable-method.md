---
title: "AddVariable method"
source_id: 7078
source_url: https://wiki.genexus.com/commwiki/wiki?7078
genexus_version: "18"
---

# AddVariable method

Adds a value for a variable to the ‘form’.

### [Syntax](#Syntax)

**&***DataType***.AddVariable*(****Name**,** Value***)**  
  
**Where:**  
*Name*  
     Name of the variable. It must be String.  
  
*Value*  
     Value of the variable. It must be String.

### [Scope](#Scope)

**Extended Data Types:** [HttpClient](https://wiki.genexus.com/commwiki/wiki?6932)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Samples](#Samples)

```
AddVariable(“CliCod”, &CliCod)
```

It set the variable “CliCod” of the form with the value of &Clicod.

### [See Also](#See+Also)

[HttpClient Data Type](https://wiki.genexus.com/commwiki/wiki?6932)


|  |
| --- |
| **Backlinks** |
| [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) | [HttpClient data type (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55613) |

---
