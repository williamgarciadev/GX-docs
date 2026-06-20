---
title: "Customizable Layout property"
source_id: 24473
source_url: https://wiki.genexus.com/commwiki/wiki?24473
genexus_version: "18"
---

# Customizable Layout property

It allows to set whether one particular procedure with Layout or all the procedures with Layout defined in a Knowledge Base for a certain Generator, will allow the end-users to customize the Layouts with a simple tool called GeneXus Report Editor.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | The procedure will not allow to end-users to customize its Layout. |
| **Use Environment property value** | The procedure will take into account the value set for the property at Generator level. This is the default value. |
| **Yes** | The procedure will allow to end-users to customize its Layout. |

### [Description](#Description)

This property is available for each [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293)  and also at Generator level.

#### [**At Generator level (Java/.Net):**](#At+Generator+level+%28Java%2F.Net%29%3A)

**Yes =** All the procedures that have its **Customizable Layout** property set to **Use Environment Property****Value**, will allow to end-users to customize their Layouts.

**No =** All the procedures that have its **Customizable Layout** property set to **Use Environment Property Value**, will not allow to end-users to customize their Layouts. This is the default value.

To apply changes at generator level Rebuild the main object.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Build with this Only of the object.

### [Availability](#Availability)

This property is available since [GeneXus X Evolution 2 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?22626,,).

### [Scope](#Scope)

**Objects:** Procedure  
**Platforms:** Web(.Net, Java)

### [See Also](#See+Also)

[End user customizable reports](https://wiki.genexus.com/commwiki/wiki?18909)  
[Layout Metadata Directory property](https://wiki.genexus.com/commwiki/wiki?24561)  
[Procedure Layout](https://wiki.genexus.com/commwiki/wiki?5468)  
[Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836)


|  |
| --- |
| **Backlinks** |
| [End user customizable reports](https://wiki.genexus.com/commwiki/wiki?18909) | [Layout Metadata Directory property](https://wiki.genexus.com/commwiki/wiki?24561) |
| [Toc:Reporting in GeneXus](https://wiki.genexus.com/commwiki/wiki?25314) |

---
