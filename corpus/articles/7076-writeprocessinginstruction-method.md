---
title: "WriteProcessingInstruction method"
source_id: 7076
source_url: https://wiki.genexus.com/commwiki/wiki?7076
genexus_version: "18"
---

# WriteProcessingInstruction method

Writes a record of the processing instruction type, indicated by an action and a value.

### [Syntax](#Syntax)

**&***DataType*.**WriteProcessingInstruction(***Action***,** *Value***)**

**Where:**  
*Action*  
   Is the action to be performed  
  
*Value*  
   Is the value for the action

### [Scope](#Scope)

**Extended Data Types:** [XmlWriter](https://wiki.genexus.com/commwiki/wiki?6938)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Samples](#Samples)

```
WriteProcessingInstruction(‘play’,‘sound = “Hello.wav”’)
```

Generates the following:  Play sound=”Hello.wav”

### [See Also](#See+Also)

[Xmlwriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938)


|  |
| --- |
| **Backlinks** |
| [XMLWriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938) |

---
