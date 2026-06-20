---
title: "MarkerDragStarted Event"
source_id: 46859
source_url: https://wiki.genexus.com/commwiki/wiki?46859
genexus_version: "18"
---

# MarkerDragStarted Event

This event is triggered when you start dragging a geoPoint.

### [Syntax](#Syntax)

Event GridControlName**.MarkerDragStarted(&***GeographyId***)**  
   *<event code>*  
EndEvent

**Where:**  
*GridControlName*  
       Is the Grid control name whose [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) is set to Maps.  
  
*<event code>*   
       Code executed when the event is triggered.

Parameters

|  |  |  |
| --- | --- | --- |
|  | **Data Type** | **Description** |
| **&GeographyId** | Character | Identifier (GUID) of the marker which is dragged. |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817) (Control Type: [Maps](https://wiki.genexus.com/commwiki/wiki?15309))

### [Availability](#Availability)

This method is available since [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46066,,).


|  |
| --- |
| **Backlinks** |
| [Editable Geographies property](https://wiki.genexus.com/commwiki/wiki?46337) | [Maps Control Type Events](https://wiki.genexus.com/commwiki/wiki?54185) |

---
