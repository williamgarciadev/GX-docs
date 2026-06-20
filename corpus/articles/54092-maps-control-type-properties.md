---
title: "Maps Control Type Properties"
source_id: 54092
source_url: https://wiki.genexus.com/commwiki/wiki?54092
genexus_version: "18"
---

# Maps Control Type Properties

When you set the Control Type property = 'Maps' for a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) included in a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829), the following properties are available to configure several behaviors:

|  |  |
| --- | --- |
| [Show My Location](https://wiki.genexus.com/commwiki/wiki?42206) | If this property is set to True, the current device position will be displayed on the map. |
| [Map Type](https://wiki.genexus.com/commwiki/wiki?42207) | Indicates the type of map that will be used in the control.  * **Standard:** Shows streets. * **Satellite:** Shows satellite images of the Earth. * **Hybrid:** Shows streets over the satellite images. |
| [User Can Choose Map Type](https://wiki.genexus.com/commwiki/wiki?42208) | If this property is set to True, the screen will have a button for the user to choose the map type at runtime. |
| [Location Attribute](https://wiki.genexus.com/commwiki/wiki?42209) | **Required**. Specifies which attribute or variable will be used to load the point on the map. If the [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) is linked to an [SDT](https://wiki.genexus.com/commwiki/wiki?10021) variable, the [Location Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42210) must be used. |
| [Pin Show My Location](https://wiki.genexus.com/commwiki/wiki?42211) | Specifies which [Image object](https://wiki.genexus.com/commwiki/wiki?23387) will be used to display the device's current position. If this property is not set, the pin image is taken from the [Pin Image property](https://wiki.genexus.com/commwiki/wiki?42212) (if set) or the default pin for the platform is used. |
| [Pin Image](https://wiki.genexus.com/commwiki/wiki?42212) | Specifies which [Image object](https://wiki.genexus.com/commwiki/wiki?23387) will be used as the pin image for all the pins appearing on the map.  If this property is not set (nor the [Pin Image Attribute property](https://wiki.genexus.com/commwiki/wiki?42213)), the default pin image for the platform is used. |
| [Pin Image Attribute](https://wiki.genexus.com/commwiki/wiki?42213) | If this property is set, the value loaded in the indicated attribute/variable will be used to display each point on the map. This is useful when different pin images must be used for the various points on the map. If the [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) is linked to an [SDT](https://wiki.genexus.com/commwiki/wiki?10021) variable, the [Pin Image Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42214) must be used. |
| [Pin Image Class](https://wiki.genexus.com/commwiki/wiki?42245) | [Theme](https://wiki.genexus.com/commwiki/wiki?16595) class used to display the pin images on the map. |
| [Show Traffic](https://wiki.genexus.com/commwiki/wiki?42216) | If this property is set to True, the traffic information will be displayed. The traffic information is only shown when the map provider provides that information for the specific region that is shown. |
| [Initial Zoom](https://wiki.genexus.com/commwiki/wiki?42217) | Indicates how the map will be displayed at startup:  * **Show all points:** (Default value) The map is adjusted to display all the loaded points (and the current device location if Show My Location is set to True). * **Nearest point visible:** The map is adjusted to display the current device location and shows my location and the nearest point. * **Radius:** The map is adjusted to display a fixed radius, from the specified [center](https://wiki.genexus.com/commwiki/wiki?42220). The radius value is specified using the [Initial Zoom Radius Attribute property](https://wiki.genexus.com/commwiki/wiki?42218) (see below). * **No initial zoom**: No specific action is taken regarding the initial zoom. The behavior will depend on the platform and provider used. |
| [Initial Zoom Radius Attribute](https://wiki.genexus.com/commwiki/wiki?42218) | It should be of the numeric type. Indicates the minimum distance (in meters) that should be visible around the designated [center](https://wiki.genexus.com/commwiki/wiki?42220) point. The map's zoom level will be adjusted so that at least this distance will be visible in all directions. If an [SDT](https://wiki.genexus.com/commwiki/wiki?10021) variable is used in this property, the [Initial Zoom Radius Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42219) has to be set. |
| [Center](https://wiki.genexus.com/commwiki/wiki?42220) | Indicates the position where the map will be centered at startup:  * **Default:** The map center is determined by the points loaded in it. * **My Location:** The map is centered on the current device location. * **Custom:** A specific location is used to center the map. This location is specified in the [Custom Center Attribute property](https://wiki.genexus.com/commwiki/wiki?42221) (see below). |
| [Custom Center Attribute](https://wiki.genexus.com/commwiki/wiki?42221) | It should be of the [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) (or based on [Geolocation domain](https://wiki.genexus.com/commwiki/wiki?14644)). It indicates the point that will be used as the map center. If an [SDT](https://wiki.genexus.com/commwiki/wiki?10021) variable is used in this property, the [Custom Center Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42222) has to be set. |
| [Selection Layer](https://wiki.genexus.com/commwiki/wiki?42223) | Enables the possibility of navigating the map and selecting a location point using the map center in addition to executing an event. Read [Layers in Maps](https://wiki.genexus.com/commwiki/wiki?40763) for detailed information. |
| [Directions Layer](https://wiki.genexus.com/commwiki/wiki?42225) | Enables the possibility of drawing the route between two points on the map. Read [Layers in Maps](https://wiki.genexus.com/commwiki/wiki?40763) for detailed information. |
| [Animation Layer](https://wiki.genexus.com/commwiki/wiki?43487) | Enables the possibility of viewing the animation of a point on the map in a Grid whose Control Type = Maps. |
| [Editable Geographies](https://wiki.genexus.com/commwiki/wiki?46337) | It enables the Map in Edit mode and allows drawing a specific geometry (Point, Line, or Polygon). |

### See Also

[Maps Control Type](https://wiki.genexus.com/commwiki/wiki?15309)


|  |
| --- |
| **Backlinks** |
| [Maps Control Type](https://wiki.genexus.com/commwiki/wiki?15309) |

---
