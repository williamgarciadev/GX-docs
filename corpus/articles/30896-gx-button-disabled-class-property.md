---
title: "gx-button-disabled-class property"
source_id: 30896
source_url: https://wiki.genexus.com/commwiki/wiki?30896
genexus_version: "18"
---

# gx-button-disabled-class property

Sets the appearance of disabled buttons in the Abstract layout (Button class and its descendants).

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** [Design System Style Class](https://wiki.genexus.com/commwiki/wiki?49309)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

The Delete button of the default [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) form is associated with the (predefined) BtnDelete class.

The **gx-button-disabled-class** **property** of the BtnDelete class is set to "BtnDeleteDisabled" (which contains the settings for the disabled buttons that have been associated with the BtnDelete class).

So, when a Transaction is called in INS mode, its Delete button is disabled and its appearance depends on the **gx-button-disabled-class**settings (it belongs to the BtnDelete class).

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).

### [See Also](#See+Also)

[Design System Object](https://wiki.genexus.com/commwiki/wiki?47375)  
[DSO properties that begin with gx- and end with class](https://wiki.genexus.com/commwiki/wiki?55707)
