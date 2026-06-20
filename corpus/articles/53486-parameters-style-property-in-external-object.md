---
title: "Parameters Style property in External Object"
source_id: 53486
source_url: https://wiki.genexus.com/commwiki/wiki?53486
genexus_version: "18"
---

# Parameters Style property in External Object

Indicates the structure of the method's SOAP message.

### [Values](#Values)

|  |  |
| --- | --- |
| **Bare** | Does not contain any additional wrapper elements or namespaces. Contains only the SOAP envelope and body. |
| **Wrapped** | Default value. Contains additional wrapper elements that are used to define the structure and format of the data. |

### [Scope](#Scope)

**Objects:** [External Object](https://wiki.genexus.com/commwiki/wiki?5669)  
**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

This property is available at the method level of external objects of [WSDL](https://wiki.genexus.com/commwiki/wiki?6154) type, in which the Style property has been set to Document.

### [Samples](#Samples)

If you want to consume a SOAP service in which you have a method and a Bare parameter, you must not send the name of that parameter. To achieve this, set the Bare value in the Parameters Style property.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?53396).

### [See Also](#See+Also)

[Type property in External Object](https://wiki.genexus.com/commwiki/wiki?53690)


|  |
| --- |
| **Backlinks** |
| [External Object: WSDL - Web Service](https://wiki.genexus.com/commwiki/wiki?6154) | [GeneXus 18 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?53396) |

---
