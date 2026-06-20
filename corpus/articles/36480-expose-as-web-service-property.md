---
title: "Expose as Web Service property"
source_id: 36480
source_url: https://wiki.genexus.com/commwiki/wiki?36480
genexus_version: "18"
---

# Expose as Web Service property

Exposes the object as a Web Service, so that this object can be consumed from other systems.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270), [Business Component](https://wiki.genexus.com/commwiki/wiki?5846)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

To facilitate the exchange of information between systems, the most common practice is the use of Web Services.

For this reason, if you have a [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), a [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270), or a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) that returns any information, you can enable it to be published as a Web Service.

To achieve this, set the **Expose as Web Service** object property to True:

`[imagen omitida: wiki id 36479]`

Note: When you set the Expose as Web Service property to True, the [Exposed namespace property](https://wiki.genexus.com/commwiki/wiki?8083) is automatically enabled with the name of the [KB](https://wiki.genexus.com/commwiki/wiki?2428) and you can change it if you want.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [See Also](#See+Also)

[SOAP Protocol property](https://wiki.genexus.com/commwiki/wiki?37253)  
[REST Protocol property](https://wiki.genexus.com/commwiki/wiki?37254)  
[Web Service Protocol property](https://wiki.genexus.com/commwiki/wiki?57754)


|  |
| --- |
| **Backlinks** |
| [Applying Work With Pattern](https://wiki.genexus.com/commwiki/wiki?15975) | [Business Component - Publication as Web Service](https://wiki.genexus.com/commwiki/wiki?2282) | [Business Components as Rest web services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28214) |
| [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) | [Data Providers as Rest Web Services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28216) | [Expose a Data Provider as Web Service](https://wiki.genexus.com/commwiki/wiki?11231) | [GeneXus Cognitive API - Process procedure](https://wiki.genexus.com/commwiki/wiki?41042) |
| [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) | [Integrated Security Level property (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54226) | [Modules Distribution in GeneXus](https://wiki.genexus.com/commwiki/wiki?31376) | [Procedures as Rest Web Services in GeneXus](https://wiki.genexus.com/commwiki/wiki?21467) |
| [REST Protocol property](https://wiki.genexus.com/commwiki/wiki?37254) | [SOAP Action property in Data Providers](https://wiki.genexus.com/commwiki/wiki?56002) | [SOAP Protocol property](https://wiki.genexus.com/commwiki/wiki?37253) | [Use Native Soap property](https://wiki.genexus.com/commwiki/wiki?13446) |
| [Web Service Protocol property](https://wiki.genexus.com/commwiki/wiki?57754) |

---
