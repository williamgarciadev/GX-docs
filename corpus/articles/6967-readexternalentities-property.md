---
title: "ReadExternalEntities Property"
source_id: 6967
source_url: https://wiki.genexus.com/commwiki/wiki?6967
genexus_version: "18"
---

# ReadExternalEntities Property

Indicates whether the parsed external entities that make up the XML document being processed must be read or not.

### [Syntax](#Syntax)

**&***DataType***.ReadExternalEntities**

### [Description](#Description)

This property indicates whether the parsed external entities that make up the XML document being processed are to be read (it includes the DTD external sub-set). If  reading is enabled, the XMLReader object will read and process, in a transparent way for the user, all references to external files or URLs included in the document. Otherwise, the references to external entities are ignored.

## [Security tips](#Security+tips)

This property default value is false. Allowing it to read External Entities may expose the application to XML External Entities (XXE) attacks. Proper sanitization is advised.

### [Scope](#Scope)

**Extended Data Types:** [XmlReader](https://wiki.genexus.com/commwiki/wiki?6928)  
**Languages:** .NET, Java, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [See Also](#See+Also)

[XmlReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928)


|  |
| --- |
| **Backlinks** |
| [A05:2021 - Security misconfiguration](https://wiki.genexus.com/commwiki/wiki?50185) |
| [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) | [Security Scanner built-in tool (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?52570) | [XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928) |

---
