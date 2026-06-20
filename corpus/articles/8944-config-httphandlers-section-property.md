---
title: "Config HttpHandlers section property"
source_id: 8944
source_url: https://wiki.genexus.com/commwiki/wiki?8944
genexus_version: "18"
---

# Config HttpHandlers section property

Determines how assemblies are mapped at runtime.

### [Values](#Values)

|  |  |
| --- | --- |
| **ASHX files** | Doesn’t use the web.config file. This option is deprecated. |
| **HttpHandler for each object** | Creates one entry per object in the web.config file. ASPX request is mapped here with the assembly GeneXus.Programs.object (bin\object.dll). |
| **HttpHandlerFactory** | Creates only one entry in the web.config file. This is the default value. |

### [Scope](#Scope)

**Platforms:** Web(.Net)

### [Description](#Description)

With the “HttpHandler for each object” value, it is faster at runtime but slower in the initial loading. Besides, it allows having objects (\*.aspx) not generated with GeneXus, while it is not possible with HttpHandlerFactory.

With the “HttpHandlerFactory” value, it is faster to prototype but slower in each call since the mapping is solved in each requirement. This option may send poorly descriptive error messages, which makes prototyping more difficult. The generated programs are slower in each call but faster in the first load.

“ASHX files” generates one ASHX file per object, and doesn’t use the web.config file.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691). |

### [See Also](#See+Also)

[Compiler flags property](https://wiki.genexus.com/commwiki/wiki?8943)  
[.Net Application namespace property](https://wiki.genexus.com/commwiki/wiki?8947)


|  |
| --- |
| **Backlinks** |
| [.Net Application namespace property](https://wiki.genexus.com/commwiki/wiki?8947) | [Compiler flags property](https://wiki.genexus.com/commwiki/wiki?8943) |

---
