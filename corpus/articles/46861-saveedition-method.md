---
title: "SaveEdition method"
source_id: 46861
source_url: https://wiki.genexus.com/commwiki/wiki?46861
genexus_version: "18"
---

# SaveEdition method

Finishes the edition of the current geography and triggers the [GeographySaved Event](https://wiki.genexus.com/commwiki/wiki?46858), with the current geography as a parameter.

### [Syntax](#Syntax)

GridControlName.**SaveEdition()**

**Where:**

*GridControlName*  
Is the Grid control name whose Control Type property is set to [Maps](https://wiki.genexus.com/commwiki/wiki?15309).

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects:** | [Grid](https://wiki.genexus.com/commwiki/wiki?24817) (Control Type: [Maps](https://wiki.genexus.com/commwiki/wiki?15309)) |
| **Generators:** | [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453) |

### [Sample](#Sample)

```
MapGrid.SaveEdition()
```

**Notes:**

* Note that any edition after calling this method will create a new geography, and will not affect the saved geography.
* Also note that saving does not save the geography to a permanent store, it is up to you to perform any saving of the geography in the GeographySaved event.

### Availability

This method is available since [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46066,,).

### [See also](#See+also)

[Editable Geographies property](https://wiki.genexus.com/commwiki/wiki?46337)


|  |
| --- |
| **Backlinks** |
| [Editable Geographies property](https://wiki.genexus.com/commwiki/wiki?46337) | [GeographySaved Event](https://wiki.genexus.com/commwiki/wiki?46858) | [Maps Control Type Methods](https://wiki.genexus.com/commwiki/wiki?54095) |

---
