---
title: "Use Native Soap property"
source_id: 13446
source_url: https://wiki.genexus.com/commwiki/wiki?13446
genexus_version: "18"
---

# Use Native Soap property

Determines the serialization support and SOAP communication method to use. It can be used both for providing and consuming web services.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | Generated serialization support. This is the default value. |
| **Use Environment property value** | The value of the same property name configured at the Environment will be used. |
| **Yes** | Uses the native infrastructure to serialize SOAP messages. |

### [Scope](#Scope)

**Objects:** [External Object](https://wiki.genexus.com/commwiki/wiki?5669), [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

When providing a web service, the property applies to the web service ([Procedure object](https://wiki.genexus.com/commwiki/wiki?6293)) itself and all the Structured Data types related to it.

When consuming a web service, the property applies to the External object and all the Structured Data types related to it.

#### [Notes](#Notes)

* **Java generator:** This implementation is used to provide web services. See [Use native SOAP support in Java](https://wiki.genexus.com/commwiki/wiki?27172).
* **.Net generator:** When the property is set to yes, for it to work properly, it is necessary to compile with .Net framework 3.5 or higher.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

[Expose as Web Service property](https://wiki.genexus.com/commwiki/wiki?36480)


|  |
| --- |
| **Backlinks** |
| [.NET Platform restrictions](https://wiki.genexus.com/commwiki/wiki?39853) | [Applying property changes](https://wiki.genexus.com/commwiki/wiki?17719) | [Enable MTOM property](https://wiki.genexus.com/commwiki/wiki?43441) |
| [External Object: WSDL - Web Service](https://wiki.genexus.com/commwiki/wiki?6154) | [Location data type](https://wiki.genexus.com/commwiki/wiki?6981) | [MTOM Threshold property](https://wiki.genexus.com/commwiki/wiki?43442) | [SOAP Action property in Data Providers](https://wiki.genexus.com/commwiki/wiki?56002) |
| [TLS Services](https://wiki.genexus.com/commwiki/wiki?39253) | [Use native SOAP support in Java](https://wiki.genexus.com/commwiki/wiki?27172) | [WSSecurity Data Type](https://wiki.genexus.com/commwiki/wiki?44552) |

---
