---
title: "Empty Target Background Image property"
source_id: 37352
source_url: https://wiki.genexus.com/commwiki/wiki?37352
genexus_version: "18"
---

# Empty Target Background Image property

Sets an image to be used as default background when the target layout does not have any.

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

The value of this property must be an [Image object](https://wiki.genexus.com/commwiki/wiki?23387) with several [sizes and resolutions](https://wiki.genexus.com/commwiki/wiki?31379) of every different device (iPhone, iPad, etc) for which the application was designed.

## [Notes](#Notes)

This property, as of [GeneXus X Evolution 3 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?26959,,), replaces:

* iPad Landscape Background Image
* iPad Retina Landscape Background Image
* iPad Portrait Background Image
* iPad Retina Portrait Background Image

All of them will be agglomerated in a single property, being necessary to include multiple sizes and resolutions for the associated [Image object](https://wiki.genexus.com/commwiki/wiki?23387).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691). |

### [See Also](#See+Also)

* [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817)
* [Images in Panels](https://wiki.genexus.com/commwiki/wiki?31379)


|  |
| --- |
| **Backlinks** |
| [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) |

---
