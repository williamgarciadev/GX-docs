---
title: "Total For Rows property in QueryViewer"
source_id: 49723
source_url: https://wiki.genexus.com/commwiki/wiki?49723
genexus_version: "18"
---

# Total For Rows property in QueryViewer

Determines whether to show a total of all values in the pivot table rows.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | Total will be hidden. |
| **Yes** | Total will be shown (this is the default value). |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Controls:** [QueryViewer](https://wiki.genexus.com/commwiki/wiki?9075)

### [Description](#Description)

When working with a PivotTable, you can show or hide row totals for the entire table.

`[imagen omitida: wiki id 49766]`

This is useful when some of the attributes in the data area can't be summarized by one of the attributes in the rows (i.e. Sales by different currencies).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at run-time and at design-time.

### [Samples](#Samples)

QueryViewer1.TotalForRows = QueryViewerTotal.No

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?49616,,).

### [See Also](#See+Also)

[Total For Columns property in QueryViewer](https://wiki.genexus.com/commwiki/wiki?49724)


|  |
| --- |
| **Backlinks** |
| [Query Object Compatibility](https://wiki.genexus.com/commwiki/wiki?11032) | [QueryViewer control properties](https://wiki.genexus.com/commwiki/wiki?32920) |
| [Total For Columns property in QueryViewer](https://wiki.genexus.com/commwiki/wiki?49724) |

---
