---
title: "Marker Clustering property for Maps in Panels"
source_id: 55187
source_url: https://wiki.genexus.com/commwiki/wiki?55187
genexus_version: "18"
---

# Marker Clustering property for Maps in Panels

Groups nearby markers under the same cluster depending on the map's current zoom level.

### [Values](#Values)

|  |
| --- |
| **True** |
| **False** |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817) (Control Type: [Maps](https://wiki.genexus.com/commwiki/wiki?15309))

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Drag a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) to the Layout of a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829). Set its [Control Type property](https://wiki.genexus.com/commwiki/wiki?15309) to "Maps".

Next, complete the Grid [Location Attribute property](https://wiki.genexus.com/commwiki/wiki?42209) with the attribute or variable that contains the location to load the points on the map. Then set the **Marker Clustering property** to True.

At runtime, a large number of markers that are close to each other are grouped into one cluster (which is a marker).

If there are many near points, the markers do not overlap and are shown as follows:

|  |  |
| --- | --- |
| **Apple** | **Android** |
|  |  |

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239).

### [See Also](#See+Also)

[Marker Clustering property for Maps in Web Panels](https://wiki.genexus.com/commwiki/wiki?54841)
