---
title: "gx-multimedia-upload-clear-class property"
source_id: 50633
source_url: https://wiki.genexus.com/commwiki/wiki?50633
genexus_version: "18"
---

# gx-multimedia-upload-clear-class property

Sets the class to style the multimedia uploader's Clear button.

### [Syntax](#Syntax)

**control.** gx-multimedia-upload-clear-class   

gx-multimedia-upload-clear-class: UploadClear;

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** [Design System Style Class](https://wiki.genexus.com/commwiki/wiki?49309)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

The following example shows a class called .ImageAttribute that styles the multimedia uploader's Clear button by referring to another class called .UploadClear. This reference is made through the gx-multimedia-upload-clear-class property.

```
.ImageAttribute{
    gx-multimedia-upload-clear-class: UploadClear;
}

.UploadClear
{
    color: red;
}
```

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?49971,,).

### [See Also](#See+Also)

[HowTo: Configure Design System Class Properties](https://wiki.genexus.com/commwiki/wiki?49494)  
[gx-multimedia-upload-class property](https://wiki.genexus.com/commwiki/wiki?50632)  
[gx-multimedia-upload-empty-class property](https://wiki.genexus.com/commwiki/wiki?50635)


|  |
| --- |
| **Backlinks** |
| [DSO properties that begin with gx- and end with class](https://wiki.genexus.com/commwiki/wiki?55707) | [gx-multimedia-upload-change-class property](https://wiki.genexus.com/commwiki/wiki?50634) | [gx-multimedia-upload-class property](https://wiki.genexus.com/commwiki/wiki?50632) |
| [gx-multimedia-upload-empty-class property](https://wiki.genexus.com/commwiki/wiki?50635) |

---
