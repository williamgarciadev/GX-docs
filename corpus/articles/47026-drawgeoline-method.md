---
title: "DrawGeoLine method"
source_id: 47026
source_url: https://wiki.genexus.com/commwiki/wiki?47026
genexus_version: "18"
---

# DrawGeoLine method

**Warning**: It is recommended to use the [DrawGeography method](https://wiki.genexus.com/commwiki/wiki?47024) instead of this method.

Draws a Geoline in a in a Grid whose Control Type property = Maps (included in a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)).

### [Syntax](#Syntax)

GridControlName.**DrawGeoLine**(**&**GeoLine)

**Where:**

*GridControlName*It is the name of the [Grid control](https://wiki.genexus.com/commwiki/wiki?24817).

***&**GeoLine*It is a variable based on the Geoline data type.

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Controls:** | [Grid](https://wiki.genexus.com/commwiki/wiki?24817) (Control Type: [Maps](https://wiki.genexus.com/commwiki/wiki?15309)) |
| **Generators:** | [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453) |

### [Sample](#Sample)

```
&GeoLine.FromString("LINESTRING(-56.082774 -34.884341, -56.074583 -34.881745)")
MapGrid.DrawGeoLine(&GeoLine)
```

### [Availability](#Availability)

This method is available since [GeneXus 16](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?35351,,).

### [See Also](#See+Also)

[Maps](https://wiki.genexus.com/commwiki/wiki?15309)  
[DrawGeography method](https://wiki.genexus.com/commwiki/wiki?47024)


|  |
| --- |
| **Backlinks** |
| [DrawGeography method](https://wiki.genexus.com/commwiki/wiki?47024) | [GeneXus deprecated functions, methods, and rules](https://wiki.genexus.com/commwiki/wiki?6620) |

---
