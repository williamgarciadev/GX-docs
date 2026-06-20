---
title: "HowTo: Group and Visualize Geographic Data Logically"
source_id: 48253
source_url: https://wiki.genexus.com/commwiki/wiki?48253
genexus_version: "18"
---

# HowTo: Group and Visualize Geographic Data Logically

This article explains how to show sets of Geography data grouped in a logical way (for example, if they are streets or avenues, etc.) with the same style (color, width, etc.). In other words, how to define Geometry Layers.

## [Scope](#Scope)

**Controls:**[Grid](https://wiki.genexus.com/commwiki/wiki?24817) (Control Type: [Maps](https://wiki.genexus.com/commwiki/wiki?15309))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

## [Description](#Description)

When you include in a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) with its Control Type property set to Maps, you may need to display different Geography data sets (based on the [Geography](https://wiki.genexus.com/commwiki/wiki?32408), [GeoPoint](https://wiki.genexus.com/commwiki/wiki?58058), [GeoLine](https://wiki.genexus.com/commwiki/wiki?59358), or [GeoPolygon](https://wiki.genexus.com/commwiki/wiki?59361) data types) that are logically grouped, each with a specific style.  
  
For example, to show information about an urban area, including:

* Streets (Geolines)
* Avenues (Geolines)
* Neighborhoods (GeoPolygons)
* Municipalities (GeoPolygons)
* Educational centers (GeoPoints)

You may need to show only Avenues and/or distinguish Streets from Avenues by color or thickness.

You can define different Geometry Layers to configure their specific display properties (color, width, icon, etc.) and whether they should be shown.

## [How to define Geometry Layers](#How+to+define+Geometry+Layers)

Here is an example to illustrate this. In the following map:

`[imagen omitida: wiki id 48362]`

The following Geometry Layers are displayed for a city area:

1. Avenue
2. BikeWay
3. Electric BusWay
4. Train

Each one is identified by its style (color, width, icon) and it is possible to choose whether to display each layer.

The implementation involves the following [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,)s:

```
UrbanArea
{
 UrbanAreaId* - Numeric
 UrbanAreaGeo - Geography
 UrbanAreaGeoLayerID
 UrbanAreaGeoLayerWayType
}

UrbanAreaGeoLayer
{
 UrbanAreaGeoLayerID* - Character
 UrbanAreaGeoLayerWayType - Character
}
```

Assume the following data is stored in the UrbanArea table:

`[imagen omitida: wiki id 54303]`

### [Alternatives to define Geometry Layers](#Alternatives+to+define+Geometry+Layers)

Geometry Layers can be defined in two ways:

#### [****1- Configuring two properties** **in a Panel Grid with its Control Type = Maps****](#1-+Configuring+two+properties+in+a+Panel+Grid+with+its+Control+Type+%3D+Maps+)

A map like the one shown above should be displayed if you set the following properties for the Panel [Grid](https://wiki.genexus.com/commwiki/wiki?24817) whose Control Type = [Maps](https://wiki.genexus.com/commwiki/wiki?15309):

* [Geometry Layer Id Attribute property](https://wiki.genexus.com/commwiki/wiki?48107) = UrbanAreaGeoLayerID
* [Location Attribute property](https://wiki.genexus.com/commwiki/wiki?42209) *=* UrbanAreaGeo

#### [**2-  Loading a KML file**](#2-+Loading+a+KML+file)

The [LoadKmlLayer method](https://wiki.genexus.com/commwiki/wiki?51341) draws geometries from a KML file that contains the style definition.

Consider the following code:

```
&LayerData = "<kml xmlns="http://www.opengis.net/kml/2.2">"
&LayerData += "<Placemark> <name>Trabajo</name> <description>LATU</description>"
&LayerData += "<Point> <coordinates>-56.2</coordinates> </Point> "
&LayerData += "</Placemark> </kml>"
MapGrid.LoadKmlLayer("Work",&LayerData,false)
```

**Note**: The ID or class visibility cannot be set.

## How to draw all Geometry Layers with the same color

The style of the geometries is given by the following [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) Class properties:  
  
`[imagen omitida: wiki id 54301]`

The Class property of the Grid allows configuring all the map geographies with the same color.

## How to display each Geometry Layer with a different color

To display each Geometry Layer with a different color, in a Grid with a [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) something similar to the following code should be defined in the Load event:

```
Event load 
    Do case 
         Case UrbanAreaGeoLayerID= "Avenue"
                   GeoLayerAtt.Class = "Orange"
         Case UrbanAreaGeoLayerID= "BikeWay"
 ​​​​​                   GeoLayerAtt.Class = "Green"
         ....
     endcase
endevent
```

## How to hide/show a Geometry Layer

Use the [SetLayerVisible method](https://wiki.genexus.com/commwiki/wiki?54293) as shown in the following samples:

```
MapGrid.SetLayerVisible(UrbanAreaGeoLayerID, true)

MapGrid.SetLayerVisible(UrbanAreaGeoLayerID, false)
```

## How to add a Geography to an existing Geometry Layer

 1. If the Grid has an associated [Base Table](https://wiki.genexus.com/commwiki/wiki?6347), it is automatically done. Adding a record to the GeoLayer table is enough.   
 2. Use the [DrawGeography method](https://wiki.genexus.com/commwiki/wiki?47024) and its new Layer ID parameter, as shown below:

```
&GeographyId =  MapGrid.DrawGeography(&geography, "class",  UrbanAreaGeoLayerID)
```

## How to delete a Geometry from a Geometry Layer

 1. If the Grid has an associated [Base Table](https://wiki.genexus.com/commwiki/wiki?6347), clear the Layer ID attribute for that record.

 2. Directly clear that geography with the Clear method using the ID.

```
  Clear(GeographyId)
```

To move it to another layer or leave it without an associated layer, redraw it using the DrawGeography method and clear the Layer ID parameter.

```
&GeographyId =  MapGrid.DrawGeography(&geography, "class",  "")
```

## How to draw Geometries of a layer with different colors

To differentiate each Geometry layer with colors too, something similar to case 2 must be done by adding the necessary conditions.  
For example, if you have the Walking or Drive paths and want to differentiate them, program it as follows:

```
Event load 
    Do case 
         Case UrbanAreaGeoLayerID= "BikeWay" and UrbanAreaGeoLayerWayType = "BikeTwoWay"
                   GeoLayerAtt.Class= "GreenSolidLine"
        Case UrbanAreaGeoLayerID= "BikeWay" and UrbanAreaGeoLayerWayType = "Street 3km" 
                   GeoLayerAtt.Class= "GreenDottedLine"
         ....
     endcase

endevent
```

Where:  
BlueWidth5 is a class defined for lines, based on SDMapRoute, with blue color and width 5.

BlueWidth1 property is a class defined for lines, based on SDMapRoute, with blue color and width 1 property.

## [Lists of properties and methods involved](#Lists+of+properties+and+methods+involved)

### [Properties](#Properties)

|  |  |  |
| --- | --- | --- |
| **Property** | **Values** | **Description** |
| [Geometry Layer Id Attribute property](https://wiki.genexus.com/commwiki/wiki?48107) | Attribute or variable of Character / Numeric data type. | Configures the attribute or variable that determines the Logical layer to which the Geography specified in the LocationAttribute or LocationAttribute Field Specifier belongs. |
| [Location Attribute property](https://wiki.genexus.com/commwiki/wiki?42209) | Attribute or variable of Geography / GeoPolygon / GeoLine / GeoPoint data type. | Configures the attribute or variable of the grid that determines the geographies to draw. |
| [Geometry Layer Id Field Specifier property](https://wiki.genexus.com/commwiki/wiki?48108) | SDT item that determines the Logical layer to which the Geography belongs. | It has the same goal as [Geometry Layer Id Attribute property](https://wiki.genexus.com/commwiki/wiki?48107) but the grid is bound to an SDT. |
| Location Attribute Field Specifier | SDT item that determines the geography to draw. | It has the same goal as [Location Attribute property](https://wiki.genexus.com/commwiki/wiki?42209) but the grid is bound to an SDT. |

**Note**: Geographies are not associated with any layer by default if a [Geometry Layer Id Attribute property](https://wiki.genexus.com/commwiki/wiki?48107) is not assigned.

### [Methods](#Methods)

|  |  |  |
| --- | --- | --- |
| **Method** | **Parameter** | **Description** |
| GetLayerVisible | LayerID: Character | Returns a Boolean value indicating whether the given Geometry layer is shown on the map. |
| [SetLayerVisible](https://wiki.genexus.com/commwiki/wiki?54293) | LayerID: Character, Visible: Boolean | Shows or hides a given layer using its identifier (of character type). |
| [DrawGeography](https://wiki.genexus.com/commwiki/wiki?47024) | Geography: Geography, Class: Character, LayeriD: Character | Draws a geography and specifies the layer. |
| LoadLayer |  |  |
| [LoadKmlLayer](https://wiki.genexus.com/commwiki/wiki?51341) | LayerID character, LayerData Longvarchar, AllowSelection boolean | Loads the specified layer on the Map (Grid) in KML format. |
| LoadKMLLayerFile | LayerId character, LayerDataPath String, AllowSelection boolean | Loads on the Map (Grid) the layer specified by a file in KML format. |

## 

## [Availability](#Availability)

Since [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?47936,,).


|  |
| --- |
| **Backlinks** |
| [Geometry Layer Id Attribute property](https://wiki.genexus.com/commwiki/wiki?48107) | [Geometry Layer Id Field Specifier property](https://wiki.genexus.com/commwiki/wiki?48108) | [Table of contents:GeoSuite](https://wiki.genexus.com/commwiki/wiki?52770) |
| [HowTo: Maps - Mapbox](https://wiki.genexus.com/commwiki/wiki?48350) | [Layers in Maps](https://wiki.genexus.com/commwiki/wiki?40763) | [SetLayerVisible method](https://wiki.genexus.com/commwiki/wiki?54293) |

---
