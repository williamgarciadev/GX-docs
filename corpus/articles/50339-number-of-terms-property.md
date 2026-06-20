---
title: "Number of terms property"
source_id: 50339
source_url: https://wiki.genexus.com/commwiki/wiki?50339
genexus_version: "18"
---

# Number of terms property

Number of terms considered in a rolling average calculation.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** [Query element](https://wiki.genexus.com/commwiki/wiki?19788)

### [Description](#Description)

Use this property to control the number of terms involved in a rolling average calculation.

When going through the series values, new values are considered for the average, while older values are discarded.

Note that, at the beginning of the series (as well as at the end when performing a central rolling average), it is not possible to have enough terms to compute the average. In that case, the calculation uses the maximum number of terms available.

Also, keep in mind that, for a central rolling average calculation, an odd number is required for this property because it considers an equal number of terms on both sides of the value, plus the value itself.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Run the main object.

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?49956,,).

### [See Also](#See+Also)

[Average type property](https://wiki.genexus.com/commwiki/wiki?50386)  
[Show values as property](https://wiki.genexus.com/commwiki/wiki?50338)


|  |
| --- |
| **Backlinks** |
| [Average type property](https://wiki.genexus.com/commwiki/wiki?50386) | [How to analyze data trends and evolution with a query object](https://wiki.genexus.com/commwiki/wiki?50410) | [Show values as property](https://wiki.genexus.com/commwiki/wiki?50338) |

---
