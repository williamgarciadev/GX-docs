---
title: "gx-table-row-cell-class property"
source_id: 25796
source_url: https://wiki.genexus.com/commwiki/wiki?25796
genexus_version: "18"
---

# gx-table-row-cell-class property

Specifies the Design System Class to style all the Table controls and Responsive Table cells of a row.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Level:** [Design System Style Class](https://wiki.genexus.com/commwiki/wiki?49309)

### [Description](#Description)

This property is available for the TableRow class in the Styles section of the Design System Object, as well as for the [Table](https://wiki.genexus.com/commwiki/wiki?6001)s and [Free Style Grid control](https://wiki.genexus.com/commwiki/wiki?6058).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

In the Styles section of your Design System Object, define the following in the TableRow class created to style the table cells of a row:

```
.Table
{
    gx-table-row-class: TableRow
}

.TableRow

{
    gx-table-row-cell-class: TableCell;
    border-style: none;
    border-width: 0px;
}
```

Where Table Cell class is defined as follows:

```
.TableCell

{
     border-style: none;
     border-width: 0px;
}
```

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).

### [See Also](#See+Also)

[gx-grid-row-class property](https://wiki.genexus.com/commwiki/wiki?32772)  
[DSO properties that begin with gx- and end with class](https://wiki.genexus.com/commwiki/wiki?55707)


|  |
| --- |
| **Backlinks** |
| [How to change cell width in RWA](https://wiki.genexus.com/commwiki/wiki?26077) | [How to configure Table control styles in web apps](https://wiki.genexus.com/commwiki/wiki?32687) |

---
