---
title: "MarkerDragEnd Event"
source_id: 46860
source_url: https://wiki.genexus.com/commwiki/wiki?46860
genexus_version: "18"
---

# MarkerDragEnd Event

This event is triggered when you finish dragging a geoPoint.

### [Syntax](#Syntax)

Event GridControlName**.MarkerDragEnd(**[**&**GeographyId [, **&**GeoPoint]]**)**  
   *<event code>*  
EndEvent

**Where:**  
*GridControlName*  
       Is the Grid control name whose [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) is set to Maps.  
  
*<event code>*   
       Code executed when the event is triggered.

#### [Parameters](#Parameters+)

|  |  |  |
| --- | --- | --- |
|  | **Data Type** | **Description** |
| **&GeographyId** | Character | Identifier (GUID) of the marker which is dragged. |
| **&GeoPoint** | GeoPoint | It's the new coordinate, got after you finish dragging the marker. |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817) (Control Type: [Maps](https://wiki.genexus.com/commwiki/wiki?15309))

**Note**: This event is not triggered when the Marker (geoPoint) was drawn in the Map editing mode (Property: Editable Geographies = True). In this case, the point is updated with the new coordinates and the [GeographySaved Event](https://wiki.genexus.com/commwiki/wiki?46858) is executed, but not the MarkerDragEnd.

### Availability

This method is available since [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46066,,).


|  |
| --- |
| **Backlinks** |
| [Editable Geographies property](https://wiki.genexus.com/commwiki/wiki?46337) | [Maps Control Type Events](https://wiki.genexus.com/commwiki/wiki?54185) |

---
