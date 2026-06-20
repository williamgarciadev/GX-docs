---
title: "Clear method in Grids with Control Type = Maps"
source_id: 46862
source_url: https://wiki.genexus.com/commwiki/wiki?46862
genexus_version: "18"
---

# Clear method in Grids with Control Type = Maps

Clears the geographies drawn (all or one given by its Id).

### [Syntax](#Syntax)

GridControlName.**Clear**([GeographyId])

**Where:**

*GridControlName*  
       Is the Grid control name whose [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) is set to Maps.

*GeographyId*Optional parameter, based on the character data type, that contains the identifier of the geometry (Line, point, or polygon) to delete.

### [Description](#Description)

To delete a specific geography, you must send its identifier as a parameter. It can be obtained in edit mode, when using the [Editable Geographies property](https://wiki.genexus.com/commwiki/wiki?46337), or when using the [DrawGeography method](https://wiki.genexus.com/commwiki/wiki?47024).

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817) (Control Type: [Maps](https://wiki.genexus.com/commwiki/wiki?15309))

### Samples

To clear all the geographies drawn in a Panel Grid with Control Type = Maps:

```
MapGrid.Clear()
```

To clear a specific Geography (a Geoline for example):

```
Event 'DrawGeoLine'
      &LineId = MapGrid.DrawGeoography(&Geoline)
Endevent

Event 'RemoveLine'
    MapGrid.Clear(&LineId)
Endevent
```

### [Availability](#Availability)

This method is available since [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46066,,).

### [See Also](#See+Also+)

[DrawGeography method](https://wiki.genexus.com/commwiki/wiki?47024)


|  |
| --- |
| **Backlinks** |
| [Editable Geographies property](https://wiki.genexus.com/commwiki/wiki?46337) | [Maps Control Type Methods](https://wiki.genexus.com/commwiki/wiki?54095) |

---
