---
title: "Difference from property"
source_id: 50340
source_url: https://wiki.genexus.com/commwiki/wiki?50340
genexus_version: "18"
---

# Difference from property

Specifies the base value for a difference calculation.

### [Values](#Values)

|  |  |
| --- | --- |
| **First value** | The first value of the series is used as the base value |
| **Previous value** | The previous value is used as the base value (this is the default value) |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** [Query element](https://wiki.genexus.com/commwiki/wiki?19788)

### [Description](#Description)

Note that if previous value is selected as the base value for the comparison, since the first value of the series has no previous value, the difference computed for the first value is zero (it is defined to be zero).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Run the main object.

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?49956,,).

### [See Also](#See+Also)

[Show as percentage property](https://wiki.genexus.com/commwiki/wiki?50341)  
[Show values as property](https://wiki.genexus.com/commwiki/wiki?50338)


|  |
| --- |
| **Backlinks** |
| [How to analyze data trends and evolution with a query object](https://wiki.genexus.com/commwiki/wiki?50410) | [Show as percentage property](https://wiki.genexus.com/commwiki/wiki?50341) | [Show values as property](https://wiki.genexus.com/commwiki/wiki?50338) |

---
