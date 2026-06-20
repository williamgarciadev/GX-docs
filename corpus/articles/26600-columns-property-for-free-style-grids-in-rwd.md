---
title: "Columns property for Free Style Grids in RWD"
source_id: 26600
source_url: https://wiki.genexus.com/commwiki/wiki?26600
genexus_version: "18"
---

# Columns property for Free Style Grids in RWD

Customize column display in Free Style Grids with the Responsive Rendering Mode by setting the number of columns for different screen sizes during design time.

### [Scope](#Scope)

**Controls:** [Free Style Grid](https://wiki.genexus.com/commwiki/wiki?6058)

### [Description](#Description)

It enables the customization of column displays based on screen device sizes during design time. With this setting, you can specify the number of columns shown for each screen device size.

`[imagen omitida: wiki id 28454]`

The possible screen sizes are as follows:

* Extra Small (Phones < 768 px)
* Small (Tablets >= 768 px)
* Medium (Desktop >= 992 px)
* Large (Desktop >= 1200 px)

*Note*: The total number of records shown in all the screen sizes is the same, and it's the greatest number of records depending on the Columns property configuration for some screen sizes.

The [Rows property](https://wiki.genexus.com/commwiki/wiki?2452) also affects the resulting number of records to be loaded.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

If the [Free Style Grid](https://wiki.genexus.com/commwiki/wiki?6058) has the Rows property set to 3 and it shows 2 columns for small devices and only one column for extra small devices, 6 records are going to be shown in both screens (remember that in extra small screens, all columns will be shown in only one column).

### [See Also](#See+Also)

[Rendering Mode property for free style grids](https://wiki.genexus.com/commwiki/wiki?26598)  
[Responsive Web Applications](https://wiki.genexus.com/commwiki/wiki?25159)


|  |
| --- |
| **Backlinks** |
| [HowTo: Use Horizontal Grid control in Web Panels](https://wiki.genexus.com/commwiki/wiki?30594) |

---
