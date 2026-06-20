---
title: "Editable Geographies property"
source_id: 46337
source_url: https://wiki.genexus.com/commwiki/wiki?46337
genexus_version: "18"
---

# Editable Geographies property

Geography-derived map elements that can be edited at runtime.

### [Syntax](#Syntax)

**control.** Editable Geographies   

It can be configured in the property or in the code as follows:

```
MapGrid.EditableGeographies = !"None"
MapGrid.EditableGeographies = !"Points"
MapGrid.EditableGeographies = !"Lines"
MapGrid.EditableGeographies = !"Polygons"
```

### [Values](#Values)

|  |  |
| --- | --- |
| **Lines** | It draws a line. |
| **None** | Default value. No geography enabled to draw. |
| **Points** | It draws a point. |
| **Polygons** | It draws a polygon. |

### [Scope](#Scope)

**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817) (Control Type: [Maps](https://wiki.genexus.com/commwiki/wiki?15309))

### [Description](#Description)

It applies to Grids with their Control type property = [Maps Control Type](https://wiki.genexus.com/commwiki/wiki?15309) and allows drawing a specific geography at runtime.

The SaveEdition method and GeographySaved event allow programming geography editing. In addition, the SDT MapGeographies stores the geographies drawn.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at runtime and at design time.

### [Samples](#Samples)

A [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) with a Maps grid could define four User Events (Points, Lines, Polygons, None), to change the geography to draw or turn off the edition. When one of this events is triggered, where changes the edit mode by code, the GeographySaved event is called  
Another User Event (SaveEdition) invoke the Save Edition method which stores the geographies drawn. It means,  this event, ends the edition of that geography.

```
Event 'Points'
    MapGrid.EditableGeographies = !"Points"
Endevent

Event 'Lines'
    MapGrid.EditableGeographies = !"Lines"
Endevent

Event 'Polygons'
    MapGrid.EditableGeographies = !"Polygons"
Endevent

Event 'None'  
   MapGrid.EditableGeographies = !"None"
Endevent

Event 'SaveEdition'
    MapGrid.SaveEdition()
Endevent

Event MapGrid.GeographySaved(&Geography , &GeographyId)
    composite
        &GeographySDT = new()
        &GeographySDT.Id = &GeographyId
        &GeographySDT.Feature = &Geography
        &Geographies.Add(&GeographySDT)
    endcomposite
Endevent
```

where the variable & Geographies is based on MapGeographies Collection and is where all geographies are stored.

If it is displayed, for example, in a user event, the content of & Geographies.Tojson () will look as follows:

```
[{"Feature": "POINT(-56.163397898 -34.653212890)", "Id":"4f9dc59...."};
  {"Feature":"LINESTRING(-56.163397898 -34.653212890, -56.163397898 -34.576488320)", "Id": "ec3f-...."};
  {"Feature":"POLYGON(-56.163397898 -34.653212890, -56.163397898 -34.576488320, ...)", "Id": "7918ad1-...."}]
```

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.

### [Availability](#Availability)

This property is available since [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46066,,).

### [See Also](#See+Also)

[Maps Control Type](https://wiki.genexus.com/commwiki/wiki?15309)  
[Layers in Maps](https://wiki.genexus.com/commwiki/wiki?40763)  
  
[GeographySaved Event](https://wiki.genexus.com/commwiki/wiki?46858)  
[MarkerDragStarted Event](https://wiki.genexus.com/commwiki/wiki?46859)  
[MarkerDragEnd Event](https://wiki.genexus.com/commwiki/wiki?46860)  
  
[SaveEdition method](https://wiki.genexus.com/commwiki/wiki?46861)  
[Clear method in Grids with Control Type = Maps](https://wiki.genexus.com/commwiki/wiki?46862)


|  |
| --- |
| **Backlinks** |
| [Clear method in Grids with Control Type = Maps](https://wiki.genexus.com/commwiki/wiki?46862) | [GeographySaved Event](https://wiki.genexus.com/commwiki/wiki?46858) | [HowTo: Maps - Mapbox](https://wiki.genexus.com/commwiki/wiki?48350) |
| [Maps Control Type Properties](https://wiki.genexus.com/commwiki/wiki?54092) | [SaveEdition method](https://wiki.genexus.com/commwiki/wiki?46861) |

---
