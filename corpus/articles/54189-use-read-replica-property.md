---
title: "Use Read Replica property"
source_id: 54189
source_url: https://wiki.genexus.com/commwiki/wiki?54189
genexus_version: "18"
---

# Use Read Replica property

Sets the name of a Data Store configured to work as a Read Replica (so that the navigation is performed using that Data Store).

### [Scope](#Scope)

**Objects:** [Data Selector](https://wiki.genexus.com/commwiki/wiki?5271)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

In a [Data Selector object](https://wiki.genexus.com/commwiki/wiki?5271), you can set its **Use Read Replica property** with the name of a [Data Store](https://wiki.genexus.com/commwiki/wiki?7117) that has been set to work as a Read Replica ([Read Replica property](https://wiki.genexus.com/commwiki/wiki?54190) = "Default Data Store").

Thus, the Data Selector navigation will read a Replica of the primary database to improve performance.

You can invoke the Data Selector in any database request (for example, in a [For Each command](https://wiki.genexus.com/commwiki/wiki?24744), [Panel](https://wiki.genexus.com/commwiki/wiki?24829) Grid, [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) Grid, [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082), etc.).

More information in [Using Read Replicas in GeneXus](https://wiki.genexus.com/commwiki/wiki?54289).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853).

### [See Also](#See+Also)

[Using Read Replicas in GeneXus](https://wiki.genexus.com/commwiki/wiki?54289)  
[Read Replica property](https://wiki.genexus.com/commwiki/wiki?54190)


|  |
| --- |
| **Backlinks** |
| [Read Replica property](https://wiki.genexus.com/commwiki/wiki?54190) | [Using Read Replicas in GeneXus](https://wiki.genexus.com/commwiki/wiki?54289) |

---
