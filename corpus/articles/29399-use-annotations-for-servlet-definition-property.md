---
title: "Use annotations for servlet definition property"
source_id: 29399
source_url: https://wiki.genexus.com/commwiki/wiki?29399
genexus_version: "18"
---

# Use annotations for servlet definition property

Enables the creation of web applications valid for the Servlet 3.0 or higher specification.

### [Values](#Values)

|  |
| --- |
| **No** |
| **Yes** | Default Value. |

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

#### [Notes:](#Notes%3A)

* If Tomcat 7.x or higher is detected, the value of the property is Yes; otherwise, if there is a lower version of Tomcat (or it isn't installed), the value is No.
* Servlet annotations are not compatible with versions lower than Servlet 3.0; an application generated with the property enabled will not work on an application server with lower specification support.
* For more information, read [SAC #29992](https://www.genexus.com/en/developers/websac?data=29992;;).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).


|  |
| --- |
| **Backlinks** |
| [Deploy to cloud property](https://wiki.genexus.com/commwiki/wiki?15041) | [Tomcat 9 support](https://wiki.genexus.com/commwiki/wiki?31497) |

---
