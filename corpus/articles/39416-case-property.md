---
title: "Case property"
source_id: 39416
source_url: https://wiki.genexus.com/commwiki/wiki?39416
genexus_version: "18"
---

# Case property

Sets whether a Character or Varchar field has to be shown and stored in uppercase.

### [Values](#Values)

|  |  |
| --- | --- |
| **None** | The Character or Varchar field will not be shown nor stored in uppercase. |
| **Upper** | The Character or Varchar field will be shown and stored in uppercase. |

### [Scope](#Scope)

**Level:** [Attribute](https://wiki.genexus.com/commwiki/wiki?7240), [Variable](https://wiki.genexus.com/commwiki/wiki?7375)

### [Description](#Description)

This property is offered for attributes and variables which their data type is [Character](https://wiki.genexus.com/commwiki/wiki?6777) or [VarChar](https://wiki.genexus.com/commwiki/wiki?6778).

It allows you to set if you want it to be entered, shown and stored with uppercase or not.

Note: If you use the [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) as [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) the values assigned to the attributes will not be automatically stored with uppercase because the Business Component concept does not consider the attributes properties values related to UI. So, if this is relevant, you have to explicitly assign values with uppercase.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.


|  |
| --- |
| **Backlinks** |
| [Picture Properties Group](https://wiki.genexus.com/commwiki/wiki?6800) |

---
