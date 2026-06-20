---
title: "GXflow - Access Level property"
source_id: 25723
source_url: https://wiki.genexus.com/commwiki/wiki?25723
genexus_version: "18"
---

# GXflow - Access Level property

This property is only enabled when [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) is **not** used in [GXflow](https://wiki.genexus.com/commwiki/wiki?4179,,). It applies to [GXflow Menus](https://wiki.genexus.com/commwiki/wiki?25709) and [GXflow Actions](https://wiki.genexus.com/commwiki/wiki?25711). This property sets which roles will have the [Menu](https://wiki.genexus.com/commwiki/wiki?25709) or [Action](https://wiki.genexus.com/commwiki/wiki?25711) available in its [GXflow Client General Structure](https://wiki.genexus.com/commwiki/wiki?17836).

### [Values](#Values)

|  |  |
| --- | --- |
| Public | All functional1 roles will be able to use the action—see/open it. This is the default value. |
| Manager | Users with GXflow Manager2 role will be able to use the action. |
| Administrator | Only users with GXflow Administrator role will be able to use the action. |

**Note1**: Functional roles do not include GXflow Administrator, GXflow Manager, GXflow Backend Administrator, GXflow Form Designer or GXflow Security Administrator.

**Note2**: Users with GXflow Administrator role will also be able to access items when the Access Level is set to "Manager"; in other words, the GXflow Administrator will be able to access all the same items as the GXflow Manager.

### [Description](#Description)

It applies to:

* [GXflow Menus](https://wiki.genexus.com/commwiki/wiki?25709)
* [GXflow Actions](https://wiki.genexus.com/commwiki/wiki?25711)

### [How to apply changes](#How+to+apply+changes)

Changes are applied once the [Menu](https://wiki.genexus.com/commwiki/wiki?25709), [Component](https://wiki.genexus.com/commwiki/wiki?25710) or [Action](https://wiki.genexus.com/commwiki/wiki?25711) is created—or updated.

### [See Also](#See+Also)

* [GXflow Backend](https://wiki.genexus.com/commwiki/wiki?25704)
* [GXflow Menus](https://wiki.genexus.com/commwiki/wiki?25709)
* [GXflow Components](https://wiki.genexus.com/commwiki/wiki?25710)
* [GXflow Actions](https://wiki.genexus.com/commwiki/wiki?25711)


|  |
| --- |
| **Backlinks** |
| [GXflow Backend](https://wiki.genexus.com/commwiki/wiki?25704) | [GXflow Menus](https://wiki.genexus.com/commwiki/wiki?25709) |

---
