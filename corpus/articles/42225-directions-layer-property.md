---
title: "Directions Layer property"
source_id: 42225
source_url: https://wiki.genexus.com/commwiki/wiki?42225
genexus_version: "18"
---

# Directions Layer property

Enables the possibility to draw the route between two points on the map.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817) (Control Type: [Maps](https://wiki.genexus.com/commwiki/wiki?15309))

### [Description](#Description)

This property is only visible for [Panels](https://wiki.genexus.com/commwiki/wiki?24829) or [WW](https://wiki.genexus.com/commwiki/wiki?15974) Grids whose [Control Type property = Maps](https://wiki.genexus.com/commwiki/wiki?15309).

When the Directions Layer property is set to True, it is possible to draw the route between two points on the map. These points are given by the values loaded using [Location Attribute property](https://wiki.genexus.com/commwiki/wiki?42209) or [Location Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42210).

Two more properties are enabled to configure the Directions layer: [Transport Type property](https://wiki.genexus.com/commwiki/wiki?42226) and [Default Route Class property](https://wiki.genexus.com/commwiki/wiki?40671).

`[imagen omitida: wiki id 40806]`

The implementation of this property is server-side and is done by the DirectionsServiceRequest Rest Service.  
In the case of using Google provider, a Google Directions API Key is necessary. In addition, it is recommended to use security mechanisms such as GAM.

#### [Consideration](#Consideration)

In order to view the directions, it is necessary to have the [Google API Key property at Environment level](https://wiki.genexus.com/commwiki/wiki?44747) configured with a valid API Key. This Key must have the Directions API limit configured.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.

### [See Also](#See+Also)

[Maps Control Type](https://wiki.genexus.com/commwiki/wiki?15309)  
[Transport Type property](https://wiki.genexus.com/commwiki/wiki?42226)


|  |
| --- |
| **Backlinks** |
| [Default Route Class property](https://wiki.genexus.com/commwiki/wiki?40671) | [HowTo: Maps - Mapbox](https://wiki.genexus.com/commwiki/wiki?48350) | [Layers in Maps](https://wiki.genexus.com/commwiki/wiki?40763) |
| [Line Width property (for MapRoute class of Carmine Theme)](https://wiki.genexus.com/commwiki/wiki?40673) | [Maps Control Type Properties](https://wiki.genexus.com/commwiki/wiki?54092) | [Stroke Color property (for MapRoute class of Carmine Theme)](https://wiki.genexus.com/commwiki/wiki?40672) | [Transport Type property](https://wiki.genexus.com/commwiki/wiki?42226) |

---
