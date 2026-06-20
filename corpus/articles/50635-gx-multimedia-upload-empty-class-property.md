---
title: "gx-multimedia-upload-empty-class property"
source_id: 50635
source_url: https://wiki.genexus.com/commwiki/wiki?50635
genexus_version: "18"
---

# gx-multimedia-upload-empty-class property

Sets the class to style the multimedia uploader when it is empty.

### [Syntax](#Syntax)

**control.** gx-multimedia-upload-empty-class   

gx-multimedia-upload-empty-class: UploadEmpty;

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** [Design System Style Class](https://wiki.genexus.com/commwiki/wiki?49309)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

The following example shows a class called .ImageAttribute that styles the multimedia uploader when it is empty, by referring to another class called .UploadEmpty. This reference is made through the gx-multimedia-upload-empty-class property.

```
.ImageAttribute{
    gx-multimedia-upload-empty-class: UploadEmpty;
}
.UploadEmpty
{
    background-image: gx-image(EmptyImage);
    background-repeat: no-repeat;
    border: 3px red solid;
}
```

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?49971,,).

### [See Also](#See+Also)

[HowTo: Configure Design System Class Properties](https://wiki.genexus.com/commwiki/wiki?49494)  
[gx-multimedia-upload-class property](https://wiki.genexus.com/commwiki/wiki?50632)  
[gx-multimedia-upload-clear-class property](https://wiki.genexus.com/commwiki/wiki?50633)  
[gx-multimedia-upload-change-class property](https://wiki.genexus.com/commwiki/wiki?50634)  
[DSO properties that begin with gx- and end with class](https://wiki.genexus.com/commwiki/wiki?55707)


|  |
| --- |
| **Backlinks** |
| [DSO properties that begin with gx- and end with class](https://wiki.genexus.com/commwiki/wiki?55707) | [gx-multimedia-upload-change-class property](https://wiki.genexus.com/commwiki/wiki?50634) | [gx-multimedia-upload-class property](https://wiki.genexus.com/commwiki/wiki?50632) |
| [gx-multimedia-upload-clear-class property](https://wiki.genexus.com/commwiki/wiki?50633) |

---
