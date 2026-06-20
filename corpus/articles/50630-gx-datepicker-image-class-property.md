---
title: "gx-datepicker-image-class property"
source_id: 50630
source_url: https://wiki.genexus.com/commwiki/wiki?50630
genexus_version: "18"
---

# gx-datepicker-image-class property

Sets the class to style the button next to a date attribute that displays the date picker.

### [Syntax](#Syntax)

**control.** gx-datepicker-image-class   

gx-datepicker-image-class: DatePickerImageClass;

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** [Design System Style Class](https://wiki.genexus.com/commwiki/wiki?49309)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

The following example shows a class called .Attribute that styles the button near a date by referring to another class called .DatePickerImageClass. This reference is made through the gx-datepicker-image-class property.

```
.Attribute{
    gx-datepicker-image-class: DatePickerImageClass;
}
.DatePickerImageClass{
    content: gx-image(DatePickerImage);
}
```

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?49971,,).

### [See Also](#See+Also)

[HowTo: Configure Design System Class Properties](https://wiki.genexus.com/commwiki/wiki?49494)  
[DSO properties that begin with gx- and end with class](https://wiki.genexus.com/commwiki/wiki?55707)
