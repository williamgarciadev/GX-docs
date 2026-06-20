---
title: "Maximum pool size per route property"
source_id: 48111
source_url: https://wiki.genexus.com/commwiki/wiki?48111
genexus_version: "18"
---

# Maximum pool size per route property

Sets the maximum number of connections per specific route.

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

If you add [httpclient-4.5.13.jar](https://repo1.maven.org/maven2/org/apache/httpcomponents/httpclient/4.5.13/httpclient-4.5.13.jar) and [httpcore-4-4-13.jar](https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcore/4.4.13/httpcore-4.4.13.jar) to the classpath, connections allow for reusability (persistent connections). By setting a value to the Maximum pool size per route property, you can reuse the same connection established for a specific route up to the value assigned. The property supports concurrent tasks.

Default Value: 1000

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, execute [Build any object](https://wiki.genexus.com/commwiki/wiki?17719) with the purpose of generating the \*.config files. |

### [Availability](#Availability)

This property is available since [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,).

### [See Also](#See+Also)

[HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932)


|  |
| --- |
| **Backlinks** |
| [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) | [HttpClient data type (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55613) |
| [Maximum pool size property](https://wiki.genexus.com/commwiki/wiki?48110) |

---
