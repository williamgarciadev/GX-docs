---
title: "WriteAttribute method"
source_id: 7068
source_url: https://wiki.genexus.com/commwiki/wiki?7068
genexus_version: "18"
---

# WriteAttribute method

Creates an attribute in the current element.

### [Syntax](#Syntax)

**&***DataType***.WriteAttribute(***AttName**,** AttValue***)**  
  
**Where:**  
*AttName*  
   Attribute name  
  
*AttValue*  
   Attribute value

### [Scope](#Scope)

**Extended Data Types:** [XmlWriter](https://wiki.genexus.com/commwiki/wiki?6938)  

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), 
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

Creates an attribute in the current element, that is the one created with the last invoking to WriteStartElement(*ElementName*) or WriteElement(*ValueName*, *ElementValue*).

**Note**: When working with documents with namespace, the WriteAttribute method has a special behavior for certain attributes. If the attribute’s name is ‘xmlns’ or starts with ‘xmlns:’ the attribute’s definition is registered like the definition of a name space. Thus, in future invocations of a WriteNSStartElement or WriteNSElement method, it is possible to determine the prefix corresponding to a certain URI.

### [See Also](#See+Also)

[XmlWriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938)  
[WriteStartElement](https://wiki.genexus.com/commwiki/wiki?7069)  
[WriteElement](https://wiki.genexus.com/commwiki/wiki?7070)


|  |
| --- |
| **Backlinks** |
| [XMLWriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938) |

---
