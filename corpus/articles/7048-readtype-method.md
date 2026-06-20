---
title: "ReadType method"
source_id: 7048
source_url: https://wiki.genexus.com/commwiki/wiki?7048
genexus_version: "18"
---

# ReadType method

Moves forward to the following node, but only if constraints established are fulfilled.

### [Syntax](#Syntax)

**&***DataType***.ReadType(***NodeTypeConstraint* [ **,***NameConstraint* ] **)**  
  
**Where:**  
*NodeTypeConstraint*  
            Specifies the node types to be read, by indicating the node type constants concatenated with the character “+”. For example: NodeTypeConstraint = 1 + 4 (It specifies the Element and Text type).

Possible node types are:

|  |  |
| --- | --- |
| **Node Type** | **Value** |
| Element | **1** |
| EndTag | **2** |
| Text | **4** |
| Comment | **8** |
| WhiteSpace | **16** |
| CData | **32** |
| ProcessingInstruction | **64** |
| Doctype | **128** |

*NameConstraint*   
       Specifies the value for the name of the node to be read –as long as the node is Element or EndTag type.  
  
**Type Returned:**  
Numeric

### [Scope](#Scope)

**Extended Data Types:** [XmlReader](https://wiki.genexus.com/commwiki/wiki?6928)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

As the [Read method](https://wiki.genexus.com/commwiki/wiki?7049), this method moves forward to the following node, but only if constraints established are fulfilled. If a node is read, It returns a whole value greater than zero. Otherwise, it returns zero.

For more information see [this](https://www.w3schools.com/xml/dom_nodetype.asp) link.

### [See Also](#See+Also)

[Read()](https://wiki.genexus.com/commwiki/wiki?7049)  
[XmlReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928)


|  |
| --- |
| **Backlinks** |
| [ExistsAttribute method](https://wiki.genexus.com/commwiki/wiki?7062) | [GetAttributeByIndex method](https://wiki.genexus.com/commwiki/wiki?7081) | [GetAttributeByName method](https://wiki.genexus.com/commwiki/wiki?7082) |
| [ReadRawXML method](https://wiki.genexus.com/commwiki/wiki?7099) | [XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928) |

---
