---
title: "Skip method"
source_id: 7085
source_url: https://wiki.genexus.com/commwiki/wiki?7085
genexus_version: "18"
---

# Skip method

Skips the following message in the current section.

### [Syntax](#Syntax)

**&***DataType***.Skip()**  
  
**Type Returned:**   
Numeric

### [Scope](#Scope)

**Extended Data Types:** [POP3Session](https://wiki.genexus.com/commwiki/wiki?6966), [XmlReader](https://wiki.genexus.com/commwiki/wiki?6928)  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual Basic (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

**XmlReader:** It allows skipping a full element with all its children. It is valid only for nodes of the Element type.  
  
**Pop3Session:** This method returns an error code, so it is possible to call it as a function (**&**Err **= &**POP3Session.**Skip()**).

### [See Also](#See+Also)

[POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966)  
[XmlReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928)


|  |
| --- |
| **Backlinks** |
| [POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966) | [XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928) |

---
