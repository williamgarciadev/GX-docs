---
title: "Maps Control Type"
source_id: 15309
source_url: https://wiki.genexus.com/commwiki/wiki?15309
genexus_version: "18"
---

# Maps Control Type

The Maps Control Type (available for [Grids](https://wiki.genexus.com/commwiki/wiki?24817) included in [Panels](https://wiki.genexus.com/commwiki/wiki?24829)) provides a way to display locations and geometries on a map and interact with them.

Therefore, when you list data in a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) that contains a "location" field, it can be displayed as a map by setting the Grid [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) to **Maps**.

A "location" is an attribute or variable based on the [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) (or its derived data type [GeoPoint](https://wiki.genexus.com/commwiki/wiki?58058)). Although "locations" can also be defined based on the [Geolocation domain](https://wiki.genexus.com/commwiki/wiki?14644), its use will be discontinued and replaced by the Geography data type.

### [Using the Maps Control Type](#Using+the+Maps+Control+Type)

For example, suppose a Waste Containers [Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,) is defined. In that case, you can see the location of the containers on a map, with different icons depending on the type of container.

`[imagen omitida: wiki id 54088]`

For more details on designing this Panel, read [HowTo: Use the Maps Control Type in a Panel Grid](https://wiki.genexus.com/commwiki/wiki?54097).

### [Requirements](#Requirements)

To enable the device to display a map, you must get the API keys for the map providers you will be using in your application.

|  |  |  |
| --- | --- | --- |
| Apple | Apple Maps | No API keys are needed. |
| Google Maps | [Apple Maps API Key property](https://wiki.genexus.com/commwiki/wiki?39268) must be used. |
| Android | Google Maps | [Android Google Services API Key property](https://wiki.genexus.com/commwiki/wiki?37267) must be used. |
| MapBox | [Android Maps API Key property](https://wiki.genexus.com/commwiki/wiki?19115) and [Mapbox API Private Key property](https://wiki.genexus.com/commwiki/wiki?47972) must be used. |
| Baidu Maps | [Android Maps API Key property](https://wiki.genexus.com/commwiki/wiki?19115) must be used. |
| AutoNavi Maps |

### [Properties](#Properties)

The following properties are available for Grids with Control Type property = Maps:  [Maps Control Type Properties](https://wiki.genexus.com/commwiki/wiki?54092).

### [Methods](#Methods)

You can set the following methods for Grids with Control Type property = Maps: [Maps Control Type Methods](https://wiki.genexus.com/commwiki/wiki?54095).

### [Events](#Events+)

The following events are available for Grids with Control Type property = Maps: [Maps Control Type Events](https://wiki.genexus.com/commwiki/wiki?54185).


|  |
| --- |
| **Backlinks** |
| [Android Google Services API Key property](https://wiki.genexus.com/commwiki/wiki?37267) | [Android Maps API Key property](https://wiki.genexus.com/commwiki/wiki?19115) | [Android Maps API property](https://wiki.genexus.com/commwiki/wiki?22729) |
| [Animation Duration Attribute property](https://wiki.genexus.com/commwiki/wiki?43490) | [Animation Duration Field Specifier property](https://wiki.genexus.com/commwiki/wiki?43491) | [Animation Duration property (for Grids with Control Type = SD Maps)](https://wiki.genexus.com/commwiki/wiki?44580) | [Animation End Behavior Attribute property](https://wiki.genexus.com/commwiki/wiki?43493) |
| [Animation End Behavior Field Specifier property](https://wiki.genexus.com/commwiki/wiki?43494) | [Animation End Behavior property](https://wiki.genexus.com/commwiki/wiki?43492) | [Animation Key Attribute property](https://wiki.genexus.com/commwiki/wiki?43488) | [Animation Key Field Specifier property](https://wiki.genexus.com/commwiki/wiki?43489) |
| [Animations Layer property](https://wiki.genexus.com/commwiki/wiki?43487) | [Center property](https://wiki.genexus.com/commwiki/wiki?42220) | [Clear method in Grids with Control Type = Maps](https://wiki.genexus.com/commwiki/wiki?46862) | [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) |
| [Control Type property (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?57964) | [Category:Control Types](https://wiki.genexus.com/commwiki/wiki?20402) | [Custom Center Attribute property](https://wiki.genexus.com/commwiki/wiki?42221) | [Custom Center Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42222) |
| [Default Route Class property](https://wiki.genexus.com/commwiki/wiki?40671) | [Directions Layer property](https://wiki.genexus.com/commwiki/wiki?42225) | [DrawGeography method](https://wiki.genexus.com/commwiki/wiki?47024) | [DrawGeoLine method](https://wiki.genexus.com/commwiki/wiki?47026) |
| [Editable Geographies property](https://wiki.genexus.com/commwiki/wiki?46337) | [Fill Color property](https://wiki.genexus.com/commwiki/wiki?46338) |
| [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) | [GeographySaved Event](https://wiki.genexus.com/commwiki/wiki?46858) | [Geolocation - Show points near me](https://wiki.genexus.com/commwiki/wiki?16473) |
| [Geolocation - Showing My Location](https://wiki.genexus.com/commwiki/wiki?16433) | [Geometry Layer Id Attribute property](https://wiki.genexus.com/commwiki/wiki?48107) | [Geometry Layer Id Field Specifier property](https://wiki.genexus.com/commwiki/wiki?48108) | [Table of contents:GeoSuite](https://wiki.genexus.com/commwiki/wiki?52770) |
| [GeoSuite - Geography Data Type in UI](https://wiki.genexus.com/commwiki/wiki?52973) | [HowTo: Draw animations between locations on a Map](https://wiki.genexus.com/commwiki/wiki?59366) | [HowTo: Get a Google Maps API Key for Apple](https://wiki.genexus.com/commwiki/wiki?39319) |
| [HowTo: Get an API Key from Google](https://wiki.genexus.com/commwiki/wiki?19055) | [HowTo: Group and Visualize Geographic Data Logically](https://wiki.genexus.com/commwiki/wiki?48253) | [HowTo: Select a Location on a Map](https://wiki.genexus.com/commwiki/wiki?59365) |
| [HowTo: Solve Tracking with GeneXus](https://wiki.genexus.com/commwiki/wiki?20832) | [HowTo: Use SD Geolocation Control in Smart Devices](https://wiki.genexus.com/commwiki/wiki?16756) | [Initial Zoom property](https://wiki.genexus.com/commwiki/wiki?42217) | [Initial Zoom Radius Attribute property](https://wiki.genexus.com/commwiki/wiki?42218) |
| [Initial Zoom Radius Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42219) | [Layers in Maps](https://wiki.genexus.com/commwiki/wiki?40763) | [Line Cap property (for MapPolygon class of Carmine Theme)](https://wiki.genexus.com/commwiki/wiki?47646) | [Line Cap property (for MapRoute class of Carmine Theme)](https://wiki.genexus.com/commwiki/wiki?40676) |
| [Line Dash Pattern property (for MapPolygon Theme class)](https://wiki.genexus.com/commwiki/wiki?47647) | [Line Dash Pattern property (for MapRoute Theme class)](https://wiki.genexus.com/commwiki/wiki?40677) | [Line Dash Phase property (for MapPolygon Theme class)](https://wiki.genexus.com/commwiki/wiki?47648) | [Line Dash Phase property (for MapRoute Theme class)](https://wiki.genexus.com/commwiki/wiki?40678) |
| [Line Join property (for MapPolygon class of Carmine Theme)](https://wiki.genexus.com/commwiki/wiki?47644) | [Line Join property (for MapRoute class of Carmine Theme)](https://wiki.genexus.com/commwiki/wiki?40674) | [Line Width property (for MapPolygon class of Carmine Theme)](https://wiki.genexus.com/commwiki/wiki?47643) | [Line Width property (for MapRoute class of Carmine Theme)](https://wiki.genexus.com/commwiki/wiki?40673) |
| [LoadKmlLayer method](https://wiki.genexus.com/commwiki/wiki?51341) | [Location Attribute property](https://wiki.genexus.com/commwiki/wiki?42209) | [Location Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42210) | [Location Selection Target Image property](https://wiki.genexus.com/commwiki/wiki?42224) |
| [Location When In Use Usage Description property](https://wiki.genexus.com/commwiki/wiki?27085) | [Maps Control Type Events](https://wiki.genexus.com/commwiki/wiki?54185) | [Maps Control Type Methods](https://wiki.genexus.com/commwiki/wiki?54095) | [Maps Control Type Properties](https://wiki.genexus.com/commwiki/wiki?54092) |
| [Maps Type property in Grids with Control Type = Maps](https://wiki.genexus.com/commwiki/wiki?42207) | [Marker Clustering property for Maps in Panels](https://wiki.genexus.com/commwiki/wiki?55187) | [MarkerDragEnd Event](https://wiki.genexus.com/commwiki/wiki?46860) | [MarkerDragStarted Event](https://wiki.genexus.com/commwiki/wiki?46859) |
| [Miter Limit property (for MapPolygon class of Carmine Theme)](https://wiki.genexus.com/commwiki/wiki?47645) | [Miter Limit property (for MapRoute class of Carmine Theme)](https://wiki.genexus.com/commwiki/wiki?40675) | [Table of contents:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Pin Image Attribute property](https://wiki.genexus.com/commwiki/wiki?42213) |
| [Pin Image Class property](https://wiki.genexus.com/commwiki/wiki?42245) | [Pin Image Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42214) | [Pin Image Height property](https://wiki.genexus.com/commwiki/wiki?40367) | [Pin Image property](https://wiki.genexus.com/commwiki/wiki?42212) |
| [Pin Image property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54382) | [Pin Image Scale Type property](https://wiki.genexus.com/commwiki/wiki?42227) | [Pin Image Width property](https://wiki.genexus.com/commwiki/wiki?40368) | [Pin Show My Location property](https://wiki.genexus.com/commwiki/wiki?42211) |
| [Polygon Class property](https://wiki.genexus.com/commwiki/wiki?46336) | [SaveEdition method](https://wiki.genexus.com/commwiki/wiki?46861) | [Selection Layer property](https://wiki.genexus.com/commwiki/wiki?42223) | [Selection Target Image Class property](https://wiki.genexus.com/commwiki/wiki?40670) |
| [SetLayerVisible method](https://wiki.genexus.com/commwiki/wiki?54293) | [SetMapCenter method](https://wiki.genexus.com/commwiki/wiki?59362) | [Show My Location property](https://wiki.genexus.com/commwiki/wiki?42206) |
| [Show Traffic property](https://wiki.genexus.com/commwiki/wiki?42216) | [Stroke Color property (for MapPolygon class of Carmine Theme)](https://wiki.genexus.com/commwiki/wiki?47642) | [Stroke Color property (for MapRoute class of Carmine Theme)](https://wiki.genexus.com/commwiki/wiki?40672) |
| [Transport Type property](https://wiki.genexus.com/commwiki/wiki?42226) | [User Can Choose Map Type property](https://wiki.genexus.com/commwiki/wiki?42208) |

---
