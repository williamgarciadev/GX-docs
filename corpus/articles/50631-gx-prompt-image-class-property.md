---
title: "gx-prompt-image-class property"
source_id: 50631
source_url: https://wiki.genexus.com/commwiki/wiki?50631
genexus_version: "18"
---

# gx-prompt-image-class property

Sets the class to style the button located near a primary key attribute that opens a prompt on click.

### [Syntax](#Syntax)

**control.** gx-prompt-image-class   

gx-prompt-image-class: PromptImageClass;

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** [Design System Style Class](https://wiki.genexus.com/commwiki/wiki?49309)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

The following example shows a class called .Attribute that styles the button located near a primary key attribute (that opens a prompt on click) by referring to another class called .PromptImageClass. This reference is made through the gx-prompt-image-class property.

```
.Attribute{
    gx-prompt-image-class: PromptImageClass;
}
.PromptImageClass{
    content: gx-image(PromptImage);
}
```

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?49971,,).

### [See Also](#See+Also)

[HowTo: Configure Design System Class Properties](https://wiki.genexus.com/commwiki/wiki?49494)  
[DSO properties that begin with gx- and end with class](https://wiki.genexus.com/commwiki/wiki?55707)
