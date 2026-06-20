---
title: "Paging Controls property"
source_id: 55744
source_url: https://wiki.genexus.com/commwiki/wiki?55744
genexus_version: "18"
---

# Paging Controls property

Indicates how paging controls will be displayed.

### [Values](#Values)

|  |  |
| --- | --- |
| **Navigation buttons** | Only navigation buttons will be shown: First, Previous, Next, Last. |
| **Pages buttons** | One page button for each page number will be shown. |
| **Navigation and Pages buttons** | Both navigation buttons and page buttons will be shown. This is the default value. |

### [Scope](#Scope)

**Generators:** [Angular](https://wiki.genexus.com/commwiki/wiki?42550)  
**Controls:** [Tabular Grid](https://wiki.genexus.com/commwiki/wiki?54449)

### [Description](#Description)

This property is available for the [Tabular Grid control](https://wiki.genexus.com/commwiki/wiki?54449) (included in a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)) when the Tabular Grid [Paging property](https://wiki.genexus.com/commwiki/wiki?55902) = "One page at a time".

**Consideration**  
Showing the pages implies knowing how many records are in the query performed. To solve this, a RecordCount is previously executed (when the navigation has a base table). This may be costly, depending on several factors such as the number of records, the filters applied, indexes, etc. In case of performance problems, it is recommended to set the **Paging Controls property** to "Navigation buttons" to avoid executing a RecordCount.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?54240).

### [See Also](#See+Also)

[Paging property in Tabular Grid Control](https://wiki.genexus.com/commwiki/wiki?55902)


|  |
| --- |
| **Backlinks** |
| [Paging property in Tabular Grid Control](https://wiki.genexus.com/commwiki/wiki?55902) |

---
