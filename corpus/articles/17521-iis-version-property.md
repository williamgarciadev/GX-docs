---
title: "IIS Version property"
source_id: 17521
source_url: https://wiki.genexus.com/commwiki/wiki?17521
genexus_version: "18"
---

# IIS Version property

It allows to set the Internet Information Services (IIS) version number installed on the server where the application would be installed.

### [Values](#Values)

|  |
| --- |
| **IIS6 or lower** |
| **IIS7** |
| **IIS8 or higher** |

### [Description](#Description)

This property must be taken into account at deploy time. It means, the default value depends on the version installed on the server, but at deploy time is necessary to set the IIS version installed on the server where the application would be installed.

`[imagen omitida: wiki id 28602]`

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Build with this Only of the object.

### [Compatibility](#Compatibility)

If the working knowledge base has been converted from GeneXus XEV1, then the IIS Version value will be set as "IIS6 or lower".

### [Scope](#Scope)

**Platforms:** Web(.Net)

### [See Also](#See+Also)

[Deploy to cloud property](https://wiki.genexus.com/commwiki/wiki?15041)  
[Deploy Server URL property](https://wiki.genexus.com/commwiki/wiki?15042)  
[Deploy Virtual Directory property](https://wiki.genexus.com/commwiki/wiki?18342)


|  |
| --- |
| **Backlinks** |
| [User Properties](https://wiki.genexus.com/commwiki/wiki?25111) |
| [Web Notifications and Progress UC requirements](https://wiki.genexus.com/commwiki/wiki?27740) |

---
