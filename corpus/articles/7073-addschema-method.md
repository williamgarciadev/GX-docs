---
title: "AddSchema method"
source_id: 7073
source_url: https://wiki.genexus.com/commwiki/wiki?7073
genexus_version: "18"
---

# AddSchema method

Indicates the schema that will be used to validate the XML.

### [Syntax](#Syntax)

**&***DataType***.AddSchema(***URL***,** *[ Namespace ] **)***  
  
**Where:**  
*URL*  
     URL of the schema  
  
*Namespace*   
     Namespace of the xml to be validated

### [Scope](#Scope)

**Extended Data Types:** [XmlReader](https://wiki.genexus.com/commwiki/wiki?6928)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

It indicates the “schema” that will be used to validate the XML in the indicated Namespace. If the Namespace is not indicated, then that of the scheme's targetNamespace attribute is taken.   
Whatever is indicated in this method has priority over the XML document's schemaLocation attribute (to the extent it exists).   
To use this method, you must indicate, in the ValidationType property, that either the validation by scheme or the automatic validation is to be carried out.

### [See Also](#See+Also)

[ValidationType](https://wiki.genexus.com/commwiki/wiki?6969)  
[XmlReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928)


|  |
| --- |
| **Backlinks** |
| [XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928) |

---
