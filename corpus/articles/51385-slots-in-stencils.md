---
title: "Slots in Stencils"
source_id: 51385
source_url: https://wiki.genexus.com/commwiki/wiki?51385
genexus_version: "18"
---

# Slots in Stencils

Any container (such as a [Table](https://wiki.genexus.com/commwiki/wiki?6001), [Flex](https://wiki.genexus.com/commwiki/wiki?40521), [Canvas](https://wiki.genexus.com/commwiki/wiki?22452), Tab control, [Group](https://wiki.genexus.com/commwiki/wiki?6570), [Free Style Grid control](https://wiki.genexus.com/commwiki/wiki?6058)) can be declared as a Slot in a [Stencil](https://wiki.genexus.com/commwiki/wiki?38418).

Setting a container as a Slot allows you to edit/customize that part of the Stencil in each object where the Stencil is included.

To declare a container as a Slot in a Stencil, set the container’s [Is Slot property](https://wiki.genexus.com/commwiki/wiki?51306) to True.

After that, when you include the Stencil in a [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), Component, etc., the Stencil Slot will only be initialized and you will be able to freely customize the Slot instance. The dynamic relationship with the Stencil will be maintained, but not with its Slots.

**Consideration:** The outer Table of the Stencil cannot be a Slot.

### [Sample](#Sample)

Cards typically have a title, a body, an image, and a set of actions. The content of the body will depend on the use of the card. Therefore, you can define the container for the content of the body as a Slot.

The following example shows a Stencil (called *StencilCard*). It contains a Responsive Table (called Body) and its Is Slot property is set to True.

`[imagen omitida: wiki id 51352]`

The Stencil is included in a Web Panel. As explained before, the Slot will only be initialized and you will be able to customize it. On the other hand, the rest of the Stencil will be read-only in the object where it is included, and it will maintain the dynamism with the Stencil.

### [See Also](#See+Also)

[Is Slot property](https://wiki.genexus.com/commwiki/wiki?51306)  
[Stencil object](https://wiki.genexus.com/commwiki/wiki?38418)


|  |
| --- |
| **Backlinks** |
| [Category:Stencil object](https://wiki.genexus.com/commwiki/wiki?38418) | [Total Experience with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51570) |

---
