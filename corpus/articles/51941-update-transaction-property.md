---
title: "Update Transaction property"
source_id: 51941
source_url: https://wiki.genexus.com/commwiki/wiki?51941
genexus_version: "18"
---

# Update Transaction property

Indicates whether to update the Transaction(s) sections when applying the pattern.

### [Values](#Values)

|  |  |
| --- | --- |
| **Apply WW Style** | The first time the pattern is applied to the Transaction, its behavior will be the same as if you selected the Create Default value. The next time it is selected, the header, footer, and buttons in the web layout will be changed, but not the Data area. Rules and events will also be modified. |
| **Create default** | The web layout, rules, and events will be modified. |
| **Do not update** | The Transaction won't be modified (web layout, rules, and events are kept). |
| **Only rules and events** | Only rules and events are modified, but not the web layout. |

### [Scope](#Scope)

**Objects:** [Work With for Web](https://wiki.genexus.com/commwiki/wiki?25475)

### [Description](#Description)

The [Work With for Web pattern](https://wiki.genexus.com/commwiki/wiki?25475) pattern creates, from one [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) (or any number of Transactions you want), all the objects needed to obtain a web application. However, in order to fully implement the pattern, besides generating new objects the Transactions involved must have certain definitions: they must have the same look and feel as the other objects, and they must include a [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862), etc. These changes are applied to the Transactions by the pattern itself so that you do not have to do it manually, and to make sure that all the necessary conditions will be met.  
  
The changes to be made to the Transactions involved are as follows:

* Applying the style to the Transaction Layout.
* Associating the Header and Footer Web Components to the Transaction Web Layout.
* Modifying or adding the [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862), depending on the Pattern configuration.
* Adding the After Transaction event with the code required to call the Transaction Controller.

The **Update Transaction** property is located in the [Work With for Web pattern](https://wiki.genexus.com/commwiki/wiki?25475) pattern instance.

`[imagen omitida: wiki id 51940]`

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.


|  |
| --- |
| **Backlinks** |
| [Work With for Web pattern](https://wiki.genexus.com/commwiki/wiki?25475) |

---
