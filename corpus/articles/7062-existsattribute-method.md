---
title: "ExistsAttribute method"
source_id: 7062
source_url: https://wiki.genexus.com/commwiki/wiki?7062
genexus_version: "18"
---

# ExistsAttribute method

Indicates if there is an attribute in the current node.

### [Syntax](#Syntax)

**&***VarBasedOnXmlReader***.ExistsAttribute(***Name***)**  
  
**Where:**  
*Name*  
    Is the attribute's name.

**Type Returned:**  
Numeric

### [Scope](#Scope)

**Extended Data Types:** [XmlReader](https://wiki.genexus.com/commwiki/wiki?6928)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

It returns 1 when the attribute called *Name* in the current node obtained through the [Read](https://wiki.genexus.com/commwiki/wiki?7049) or the [ReadType](https://wiki.genexus.com/commwiki/wiki?7048) method exists. Otherwise, it returns 0. It is valid only for nodes of the [GXflow Elements](https://wiki.genexus.com/commwiki/wiki?25812) type.

### [See Also](#See+Also)

[Read](https://wiki.genexus.com/commwiki/wiki?7049)  
[ReadType](https://wiki.genexus.com/commwiki/wiki?7048)  
[XmlReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928)


|  |
| --- |
| **Backlinks** |
| [XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928) |

---
