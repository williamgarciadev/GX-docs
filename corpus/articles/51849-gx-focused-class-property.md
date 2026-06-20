---
title: "gx-focused-class property"
source_id: 51849
source_url: https://wiki.genexus.com/commwiki/wiki?51849
genexus_version: "18"
---

# gx-focused-class property

Sets the class to style a control when it has the focus.

### [Syntax](#Syntax)

**control.** gx-focused-class   

```
gx-focused-class: <name_of_class>;
```

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)  
**Level:** [Design System Style Class](https://wiki.genexus.com/commwiki/wiki?49309)

### [Description](#Description)

By setting the **gx-focused-class** property you can obtain the same result as by setting all these others:

gx-attribute-focused-class  
gx-button-focused-class  
gx-image-focused-class  
gx-textblock-focused-class  
gx-tabpage-focused-class

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

This definition:

```
.SpecialClass 
{ 
    gx-focused-class: classA; 
}
```

Is equivalent to this one:

```
.SpecialClass 
{ 
   gx-attribute-focused-class: classA;
   gx-button-focused-class: classA;
   gx-image-focused-class: classA;
   gx-textblock-focused-class: classA;
   gx-tabpage-focused-class: classA; 
}
```

GeneXus ensures that a class using gx-focused-class works on all platforms and on all the controls listed below.

**Note:** Once defined, the .SpecialClass can be assigned as a class of these controls: [Button](https://wiki.genexus.com/commwiki/wiki?6011), [Text Block](https://wiki.genexus.com/commwiki/wiki?5948), Attribute, [Image](https://wiki.genexus.com/commwiki/wiki?5939), [Tab](https://wiki.genexus.com/commwiki/wiki?25623).

### [See Also](#See+Also)

[DSO properties that begin with gx- and end with class](https://wiki.genexus.com/commwiki/wiki?55707)


|  |
| --- |
| **Backlinks** |
| [DSO properties that begin with gx- and end with class](https://wiki.genexus.com/commwiki/wiki?55707) |

---
