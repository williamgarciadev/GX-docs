---
title: "Is Slot property"
source_id: 51306
source_url: https://wiki.genexus.com/commwiki/wiki?51306
genexus_version: "18"
---

# Is Slot property

Declares a container included inside a Stencil as a Slot.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Controls:** [Flex](https://wiki.genexus.com/commwiki/wiki?40521), [Free Style Grid](https://wiki.genexus.com/commwiki/wiki?6058), [Group](https://wiki.genexus.com/commwiki/wiki?6570), [Responsive Table](https://wiki.genexus.com/commwiki/wiki?24961), [Tab](https://wiki.genexus.com/commwiki/wiki?25623), [Table](https://wiki.genexus.com/commwiki/wiki?6001), [Canvas](https://wiki.genexus.com/commwiki/wiki?22452), [Grid](https://wiki.genexus.com/commwiki/wiki?24817), [Smart Table](https://wiki.genexus.com/commwiki/wiki?45577)

### [Description](#Description)

Any container (such as a Table, Flex, Canvas, Tab control, Group, Free Style Grid) included inside a [Stencil](https://wiki.genexus.com/commwiki/wiki?38418) can be declared as a Slot.

By setting a container as a Slot, you will be able to edit/customize that part of the Stencil in each object where the Stencil is included.

To declare a container as a Slot, set this property to True.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Cards typically have a title, a body, an image, and a set of actions. The content of the body will depend on the use of the card. So, you can define the container for the content of the body as a Slot.

The following example shows a Stencil (called StencilCard). It contains a Responsive Table (called Body) and its Is Slot property is set to True.

`[imagen omitida: wiki id 51352]`

The Stencil is included in a Web Panel. The Slot will be only initialized and you will be able to customize it. On the other hand, the rest of the Stencil will be read-only in the object where it is included, and it will maintain the dynamism with the Stencil.

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?49972,,).


|  |
| --- |
| **Backlinks** |
| [DesignOps - Conventions](https://wiki.genexus.com/commwiki/wiki?46872) | [Slots in Stencils](https://wiki.genexus.com/commwiki/wiki?51385) |

---
