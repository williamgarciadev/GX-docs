---
title: "Accessible Role property"
source_id: 55453
source_url: https://wiki.genexus.com/commwiki/wiki?55453
genexus_version: "18"
---

# Accessible Role property

Indicates the semantic role of the control (what it is used for).

### [Values](#Values)

|  |  |
| --- | --- |
| **Article** | The control includes a self-contained section in an application, which is intended to be independently distributable or reusable. |
| **Complementary** | The control includes a complementary section related to the main content (control with Accessible Role = Main), but they can stand alone when separated. These sections are often presented as sidebar menus or callout boxes. |
| **Footer** | The control is used as a footer (containing identifying information such as copyright, navigation links and privacy statements of an application). |
| **Header** | The control is used as a header. |
| **List** | The control defines an unordered list of items. |
| **Main** | The control defines the main content of the application. |
| **Region** | The control defines a section or region of a web page. |

### [Scope](#Scope)

**Generators:** [Angular](https://wiki.genexus.com/commwiki/wiki?42550)  
**Controls:** [Canvas](https://wiki.genexus.com/commwiki/wiki?22452), [Flex](https://wiki.genexus.com/commwiki/wiki?40521), [Table](https://wiki.genexus.com/commwiki/wiki?6001)

### [Description](#Description)

* There can only be one control with Accessible Role = Main on the entire page.
* When using Accessible Role = Region, you must set a value for the Accessible Name of the control. Otherwise, there will be a region in the application whose content you will not know.
* It is not always necessary for all containers to have a Role.

**Note**: This property does not impact in any way the performance or functionality of the controls in which it is used; it only provides semantics for them.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

[Sample PlantCare](https://wiki.genexus.com/commwiki/wiki?60789) visually highlights the following Accessible Role of containers:

`[imagen omitida: wiki id 55659]`

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239).

### [See Also](#See+Also)

[Accessible Name property](https://wiki.genexus.com/commwiki/wiki?55454)


|  |
| --- |
| **Backlinks** |
| [Accessible Name Control property](https://wiki.genexus.com/commwiki/wiki?55456) | [Accessible Name Custom property](https://wiki.genexus.com/commwiki/wiki?55469) | [Accessible Name property](https://wiki.genexus.com/commwiki/wiki?55454) |
| [Accessible Name property (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60147) | [Accessible Name property (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57813) | [Accessible Role property in Text Blocks](https://wiki.genexus.com/commwiki/wiki?60913) | [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239) |

---
