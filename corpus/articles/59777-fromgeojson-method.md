---
title: "FromGeoJSON method"
source_id: 59777
source_url: https://wiki.genexus.com/commwiki/wiki?59777
genexus_version: "18"
---

# FromGeoJSON method

Receives a representation in GeoJSON format to load attributes or variables based on the Geography data type (or derived data types associated with geometry like GeoPoint, GeoLine, or GeoPolygon).

### [Syntax](#Syntax)

*AttOrVar*.**FromGeoJSON(***Character***)**

**Where:**

*AttOrVar*    
    Is an [attribute](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7240,,) or [variable](https://wiki.genexus.com/commwiki/wiki?7375) based on the [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) (or derived data types associated with geometry like [GeoPoint](https://wiki.genexus.com/commwiki/wiki?58058), [GeoLine](https://wiki.genexus.com/commwiki/wiki?59358), [GeoPolygon](https://wiki.genexus.com/commwiki/wiki?59361)) to which the data will be loaded.

*Character*    
    Is text enclosed in quotation marks that must contain a valid representation of a Point, Line, or Polygon in GeoJSON format. For example:

* To load a Point, *Character* should be:

```
'{"type":"Point","coordinates":[Longitude, Latitude]}'
```

* To load a Line or Multiline, *Character* should be:

```
{ "type": "LineString", "coordinates": [[Longitude1, Latitude1],[Longitude2, Latitude2],[Longitude3, Latitude3]]}'
```

* To load a Polygon, *Character* should be:

```
{ "type": "Polygon", "coordinates": [[[Longitude1,Latitude1],[Longitude2,Latitude2],[Longitude3,Latitude3],[Longitude4,Latitude4]]]}'
```

**Type Returned:**  
[Geography](https://wiki.genexus.com/commwiki/wiki?32408) | [GeoPoint](https://wiki.genexus.com/commwiki/wiki?58058) | [GeoLine](https://wiki.genexus.com/commwiki/wiki?59358) | [GeoPolygon](https://wiki.genexus.com/commwiki/wiki?59361)

### [Scope](#Scope)

**Data Types:** [Geography](https://wiki.genexus.com/commwiki/wiki?32408), [GeoPoint](https://wiki.genexus.com/commwiki/wiki?58058), [GeoLine](https://wiki.genexus.com/commwiki/wiki?59358), [GeoPolygon](https://wiki.genexus.com/commwiki/wiki?59361)    
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

The **FromGeoJSON method** receives a representation in GeoJSON format (Longitude coordinates and Latitude coordinates must always be indicated in that order in the character content [as specified in the standard](https://geojson.org/)) to load attributes or variables based on the Geography data type (or derived data types associated with geometry like GeoPoint, GeoLine, or GeoPolygon).

### [Samples](#Samples)

**1)**&Geography is a variable based on the [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408). &Point is a variable based on the [GeoPoint data type](https://wiki.genexus.com/commwiki/wiki?58058). They are being loaded, for example, inside an object Event or an object Source.

```
&Geography.FromGeoJSON('{"type":"Point","coordinates":[-56.1701774597168,-34.91676309400329]}')
```

or

```
&Point.FromGeoJSON('{"type":"Point","coordinates":[-56.1701774597168,-34.91676309400329]}')
```

**2)**&Geography is a variable based on the [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408). &Line is a variable based on the [GeoLine data type](https://wiki.genexus.com/commwiki/wiki?59358). They are being loaded, for example, inside an object Event or an object Source.

```
&Geography.FromGeoJSON('{"type":"LineString","coordinates":[ [ -56.18528366088867, -34.90571271703311 ], [ -56.17850303649902, -34.90641660705113 ], [ -56.15318298339844, -34.9140182347531 ], [ -56.14863395690918, -34.91521472314688 ] ]}')
```

or

```
&Line.FromGeoJson('{ "type": "LineString", "coordinates": [ [ -56.18528366088867, -34.90571271703311 ], [ -56.17850303649902, -34.90641660705113 ], [ -56.15318298339844, -34.9140182347531 ], [ -56.14863395690918, -34.91521472314688 ] ]}')
```

**3)** Consider the following [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,):

```
Place
{
  PlaceId* 
  PlaceName --> Character data type
  PlaceGeo --> Geography data type
}
```

The following [New command](https://wiki.genexus.com/commwiki/wiki?6714) is defined inside a [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664).

To load the PlaceGeo attribute, the **FromGeoJSON method** is applied to it, passing as a parameter the &geojsonNeighborhood variable (of [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408)) loaded with a Polygon (that corresponds to a neighborhood) in GeoJSON format.

```
new 
  PlaceId = 5
  PlaceName = "Punta Carretas, Neighborhood"
  &geojsonNeighborhood = '{ "type": "Polygon", "coordinates": [ [ [-56.148808,-34.918453], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.154835,-34.917061' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.156059,-34.916466' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.156250,-34.914318' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.162754,-34.914791' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.162003,-34.921761' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.165714,-34.919930' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.165737,-34.919930' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.168247,-34.919525' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.169598,-34.918205' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.171421,-34.919209' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.172668,-34.919685' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.172558,-34.920406' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.171207,-34.921566' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.171852,-34.924698' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.171249,-34.925278' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.169662,-34.925438' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.165329,-34.927372' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.161766,-34.929379' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.159920,-34.930645' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.157967,-34.927776' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.156445,-34.927177' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.153141,-34.925507' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.151508,-34.924644' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.151489,-34.923008' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.149151,-34.921497' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.148506,-34.921585' + '], [' 
  &geojsonNeighborhood = &geojsonNeighborhood + '-56.148808,-34.918453' + '] ] ] }' 
  PlaceGeo.FromGeoJson(&geojsonNeighborhood) 
endnew
```

### [See Also](#See+Also)

[ToGeoJSON method](https://wiki.genexus.com/commwiki/wiki?59810)


|  |
| --- |
| **Backlinks** |
| [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) | [GeoJSON Geographic data format](https://wiki.genexus.com/commwiki/wiki?59399) | [GeoLine data type](https://wiki.genexus.com/commwiki/wiki?59358) |
| [GeoPoint data type](https://wiki.genexus.com/commwiki/wiki?58058) | [GeoPolygon data type](https://wiki.genexus.com/commwiki/wiki?59361) | [KML Geographic data format](https://wiki.genexus.com/commwiki/wiki?59400) | [ToGeoJSON method](https://wiki.genexus.com/commwiki/wiki?59810) |

---
