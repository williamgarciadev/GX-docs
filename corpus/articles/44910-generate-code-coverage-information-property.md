---
title: "Generate Code Coverage information property"
source_id: 44910
source_url: https://wiki.genexus.com/commwiki/wiki?44910
genexus_version: "18"
---

# Generate Code Coverage information property

Indicates whether to generate GeneXus source-level runtime code coverage information.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | GeneXus does not generate source-level runtime code coverage information. This is the default value |
| **Yes** | GeneXus generates source-level runtime code coverage information |

### [Scope](#Scope)

**Objects:** [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270), [Procedure](https://wiki.genexus.com/commwiki/wiki?6293)  
**Platforms:** Web(.Net, .Net Core, Java)  
**Level:** Environment

### [Description](#Description)

Since the property is configured by Environment, and since to apply the changes you must make a Rebuild All, it is recommended to have it always enabled (eg. for development or testing environments) or always off (eg. for production environments), but not changing from one value to another in the same Environment.

Note: Enabling this option may change build performance since more information is added to the generated source file. It can also change the performance as additional information is generated. However, some benchmarks suggested that performance is not significantly affected in a development environment.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a Rebuild All.

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 8](https://wiki.genexus.com/commwiki/wiki?44913,,).

### [See Also](#See+Also)

* [Code Coverage and Profiling](https://wiki.genexus.com/commwiki/wiki?44369)


|  |
| --- |
| **Backlinks** |
| [Code Coverage and Profiling](https://wiki.genexus.com/commwiki/wiki?44369) | [Generate Mockable Objects property](https://wiki.genexus.com/commwiki/wiki?56903) |

---
