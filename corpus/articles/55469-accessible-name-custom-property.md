---
title: "Accessible Name Custom property"
source_id: 55469
source_url: https://wiki.genexus.com/commwiki/wiki?55469
genexus_version: "18"
---

# Accessible Name Custom property

Defines the Accessible Name (a short string to provide users with a label for an element) directly (by entering the text).

### [Scope](#Scope)

**Generators:** [Angular](https://wiki.genexus.com/commwiki/wiki?42550)  
**Controls:** Attribute/Variable, [AudioController](https://wiki.genexus.com/commwiki/wiki?31046), [Button](https://wiki.genexus.com/commwiki/wiki?6011), [Canvas](https://wiki.genexus.com/commwiki/wiki?22452), [Flex](https://wiki.genexus.com/commwiki/wiki?40521), [Grid](https://wiki.genexus.com/commwiki/wiki?24817), [Image](https://wiki.genexus.com/commwiki/wiki?5939), [Tab](https://wiki.genexus.com/commwiki/wiki?25623), [Table](https://wiki.genexus.com/commwiki/wiki?6001)

### [Description](#Description)

The default value depends on the control. For most controls, the default value is empty.

For the Button control, it takes the value from the Caption.

For Attribute/Variable controls, it takes the value from the Label Caption.

### [Recommendations](#Recommendations)

* The Accessible Name of the controls should be concise (one to three words). Otherwise, screen readers may cut the Accessible Name if it is too long.
* Do not repeat the inherent role of the controls in the Accessible Name. For example, in the Submit Button on a form:
  + Do not use an Accessible Name = Submit Button
  + Use Accessible Name = Submit

The reason is that when a control receives the focus, assistive technologies can concatenate the platform role description with its Accessible Name.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239).

### [See Also](#See+Also)

[Accessible Name property](https://wiki.genexus.com/commwiki/wiki?55454)  
[Accessible Role property](https://wiki.genexus.com/commwiki/wiki?55453)


|  |
| --- |
| **Backlinks** |
| [Accessible Name property](https://wiki.genexus.com/commwiki/wiki?55454) | [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239) |

---
