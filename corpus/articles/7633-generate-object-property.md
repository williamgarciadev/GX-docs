---
title: "Generate Object property"
source_id: 7633
source_url: https://wiki.genexus.com/commwiki/wiki?7633
genexus_version: "18"
---

# Generate Object property

This property allows you to enable/disable the object specification and generation.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Description](#Description)

Default value: True.

There may be objects in a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) that, for different reasons, must stay there (i.e. not deleted) but not be generated. Transactions are usually a good example of these type of objects. The [BC](https://wiki.genexus.com/commwiki/wiki?2416) is used but their User interface is not.

The Generate Object property is intended to save specification and generation time: do not generate objects that the application does not use. A [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) used only as a BC should have this property set to False.

When the value is set to False and you try to view it's navigation, the following message will be displayed:

**spc0140** 'This object cannot be specified as it has the GenerateObject property set to false'.

### [Scope](#Scope)

**Objects:** Procedure, Transaction, Web Panel, Web Component


|  |
| --- |
| **Backlinks** |
| [Category:API object](https://wiki.genexus.com/commwiki/wiki?46151) |

---
