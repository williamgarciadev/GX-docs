---
title: "WriteCData method"
source_id: 7052
source_url: https://wiki.genexus.com/commwiki/wiki?7052
genexus_version: "18"
---

# WriteCData method

#### [Writes a Cdata section with the indicated value.](#Writes+a+Cdata+section+with+the+indicated+value.)

### [Syntax](#Syntax)

**&***VarBasedOnXmlWriter***.WriteCData(***DataValue***)**  
  
**Where:**  
*DataValue*  
     Value to write as a Cdata section

### [Scope](#Scope)

**Extended Data Types:** [XmlWriter](https://wiki.genexus.com/commwiki/wiki?6938)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

Writes a Cdata section with the indicated value.

**Note**: If the contents specified for the Cdata section include the character sequence ] ] >, it is fractionated and generates as many Cdata sections as needed to get a well-formed XML document.

### [See Also](#See+Also)

[Xmlwriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938)


|  |
| --- |
| **Backlinks** |
| [XMLWriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938) |

---
