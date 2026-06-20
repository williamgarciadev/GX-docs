---
title: "Style and Default Style properties"
source_id: 8145
source_url: https://wiki.genexus.com/commwiki/wiki?8145
genexus_version: "18"
---

# Style and Default Style properties

Assigns the object (Design System or Web Theme) with which the style will be applied.

### [Scope](#Scope)

**Objects:** [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Level:** [Version](https://wiki.genexus.com/commwiki/wiki?7860)

### [Description](#Description)

Every [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) and every [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) offers the **Style property** so that you can assign a [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) or a [Web Theme object](https://wiki.genexus.com/commwiki/wiki?6420) to it.

If you do not assign an explicit object to this property, it inherits the object set in the **Default Style property** (offered at [version level](https://wiki.genexus.com/commwiki/wiki?7860)).

To apply the corresponding changes when the **Default Style property** value is configured, you have to execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691). On the other hand, to apply the corresponding changes when the **Style property** value is configured, you have to execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

Consider that the value configured for these properties must be in accordance with the values set for the [Default Form Layout](https://wiki.genexus.com/commwiki/wiki?51685) and [Form Layout](https://wiki.genexus.com/commwiki/wiki?51686) properties.

When values ​​that have no correspondences are configured, no determined behaviors can be obtained.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?48247,,).

### [See Also](#See+Also)

[Style property in Work With for Web Pattern Settings](https://wiki.genexus.com/commwiki/wiki?52134)  
[Style property for Platforms](https://wiki.genexus.com/commwiki/wiki?43966)  
[Platform Overrides property](https://wiki.genexus.com/commwiki/wiki?40583)


|  |
| --- |
| **Backlinks** |
| [Class property](https://wiki.genexus.com/commwiki/wiki?8741) | [Column Class property in Grid and Tabular Grid](https://wiki.genexus.com/commwiki/wiki?24908) | [Column Class property in Theme Class (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54472) |
| [Considerations to develop a Responsive Web Application](https://wiki.genexus.com/commwiki/wiki?29133) | [Customize Unanimo](https://wiki.genexus.com/commwiki/wiki?52178) | [Default Form Layout property](https://wiki.genexus.com/commwiki/wiki?51685) | [Design System Object - How to associate a Design System Object to your screens](https://wiki.genexus.com/commwiki/wiki?48696) |
| [DesignOps - Sample - Travel Agency web back-office](https://wiki.genexus.com/commwiki/wiki?47052) | [Form Layout property](https://wiki.genexus.com/commwiki/wiki?51686) | [Form Template property](https://wiki.genexus.com/commwiki/wiki?51711) |
| [How to convert my application to make it responsive](https://wiki.genexus.com/commwiki/wiki?25214) | [How to use Unanimo](https://wiki.genexus.com/commwiki/wiki?52176) | [KB Platforms](https://wiki.genexus.com/commwiki/wiki?24284) | [Migrate to Unanimo](https://wiki.genexus.com/commwiki/wiki?52177) |
| [Migration of KB with Carmine Theme to Unanimo Design System](https://wiki.genexus.com/commwiki/wiki?51821) | [My first Responsive Web Application](https://wiki.genexus.com/commwiki/wiki?25206) | [My first Theme object](https://wiki.genexus.com/commwiki/wiki?16237) | [New Knowledge Base](https://wiki.genexus.com/commwiki/wiki?9596) |
| [Style property for Platforms](https://wiki.genexus.com/commwiki/wiki?43966) | [Style property in Work With for Web Pattern Settings](https://wiki.genexus.com/commwiki/wiki?52134) | [Style property in Work With for Web Pattern Settings (GeneXus 18)](https://wiki.genexus.com/commwiki/wiki?53343) | [Web Form Defaults property](https://wiki.genexus.com/commwiki/wiki?25135) |
| [Category:Web Theme object](https://wiki.genexus.com/commwiki/wiki?6420) |

---
