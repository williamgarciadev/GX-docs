---
title: "Default Form Layout property"
source_id: 51685
source_url: https://wiki.genexus.com/commwiki/wiki?51685
genexus_version: "18"
---

# Default Form Layout property

Specifies the template used to generate the Transaction's default form. The value set for this property will be the default value for the Transaction's "Form Layout" property.

### [Values](#Values)

|  |  |
| --- | --- |
| **Carmine Template** | Selects the default template associated with the Carmine style. |
| **Fiori Template** | Selects the default template associated with the Fiori style. |
| **Flat Template** | Selects the default template associated with the Flat style. |
| **Unanimo Template** | Selects the default template associated with the Unanimo style. |

### [Scope](#Scope)

**Level:** [Version](https://wiki.genexus.com/commwiki/wiki?7860)

### [Description](#Description)

The value configured for this property must be in accordance with the value set for the [Style and Default Style properties](https://wiki.genexus.com/commwiki/wiki?8145).

When values ​​that have no correspondences are configured, no determined behaviors can be obtained.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

### [Compatibility](#Compatibility)

When creating a new KB with GeneXus 18, by default this property is set to "Unanimo Template."
When opening a KB created with a version prior to GeneXus 18 (which uses the Carmine Theme), this property is set to "Carmine Template."

### [See Also](#See+Also)

[Form Layout property](https://wiki.genexus.com/commwiki/wiki?51686)  
[Form Template property](https://wiki.genexus.com/commwiki/wiki?51711)  
[Style and Default Style properties](https://wiki.genexus.com/commwiki/wiki?8145)


|  |
| --- |
| **Backlinks** |
| [Form Layout property](https://wiki.genexus.com/commwiki/wiki?51686) | [Form Template property](https://wiki.genexus.com/commwiki/wiki?51711) | [Migration of KB with Carmine Theme to Unanimo Design System](https://wiki.genexus.com/commwiki/wiki?51821) |
| [Style and Default Style properties](https://wiki.genexus.com/commwiki/wiki?8145) | [Work With for Web pattern](https://wiki.genexus.com/commwiki/wiki?25475) |

---
