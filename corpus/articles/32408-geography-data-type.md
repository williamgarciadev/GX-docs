---
title: "Geography data type"
source_id: 32408
source_url: https://wiki.genexus.com/commwiki/wiki?32408
genexus_version: "18"
---

# Geography data type

You can formally represent geographical entities with the Geography data type. This implies that at the database level, geographical information is stored using specific data types supported by different database management systems.

There are specialized variants of the Geography data type, named [GeoPoint](https://wiki.genexus.com/commwiki/wiki?58058), [GeoLine](https://wiki.genexus.com/commwiki/wiki?59358), and [GeoPolygon](https://wiki.genexus.com/commwiki/wiki?59361) types. They are derived from the Geography data type.

### [Use cases](#Use+cases)

#### Closest Points

|  |  |
| --- | --- |
| Suppose you need to store tourist attractions, so you define the following [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,):   ``` Place {   PlaceId*   PlaceName --> Character data type   PlaceGeo --> Geography data type } ```   After that, you define a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) in which, given any point and a distance in meters, it displays all tourist attractions located within that radius from the point.   ``` &MyPoint --> Geography data type &Distance --> Numeric data type   Event Load  For each Place   where PlaceGeo.Distance(&MyPoint) < &Distance    &PlaceName=PlaceName     load  endfor  EndEvent ``` |  |

#### Point in a Polygon

|  |  |
| --- | --- |
| Consider the following [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,):   ``` Neighborhood   {   NeighborhoodId*   NeighborhoodName --> Character data type   NeighborhoodPlace --> Geography data type } ```   Suppose you define a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) in which, given a specific tourist attraction (the end user indicates the point in the map), it shows the neighborhood or zone where that attraction is located:   ``` &MyPoint --> Geography data type &NeighborhoodPlace --> Geography data type  Event 'Get_Neighborhood'  For each Neighborhood     Where NeighborhoodPlace.Intersect(&Mypoint)       &NeighborhoodId = NeighborhoodId       &NeighborhoodName = NeighborhoodName       &NeighborhoodPlace = NeighborhoodPlace  endfor Endevent ``` |  |

### [Data Input](#Data+Input)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,):

```
Place
{
  PlaceId* 
  PlaceName --> Character data type
  PlaceGeo --> Geography data type
}
```

You can run the Transaction and double-click on the map associated with the PlaceGeo attribute present in the Layout. When saving, the Geography data will be stored for the place record.

In addition, you can use the [FromWkt](https://wiki.genexus.com/commwiki/wiki?18900) and [FromGeoJSON](https://wiki.genexus.com/commwiki/wiki?59777) methods to load data into an attribute based on the Geography data type.

Although the FromString method could be used, the one to be used is the [FromWkt method](https://wiki.genexus.com/commwiki/wiki?18900)**.**

### [Samples](#Samples)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,):

```
Place
{
  PlaceId* 
  PlaceName --> Character data type
  PlaceGeo --> Geography data type
}
```

The PlaceGeo attribute is defined based on the Geography data type to store Points, Lines, or Polygons as needed.

The first three samples below store Points. If the PlaceGeo attribute were of the [GeoPoint data type](https://wiki.genexus.com/commwiki/wiki?58058), the same proposed syntax would apply identically.

The other examples store Line and Polygon data in the PlaceGeo attribute. The same proposed syntax would apply identically if the PlaceGeo attribute were of the [GeoLine](https://wiki.genexus.com/commwiki/wiki?59358) or [GeoPolygon](https://wiki.genexus.com/commwiki/wiki?58058) data type, respectively.

```
New 
   PlaceId = 1 
   PlaceName = "Palacio Legislativo" 
   PlaceGeo = GeoPoint.New(-34.8910275746741, -56.18720064473088)
endNew

New
   PlaceId = 2
   PlaceName = "Golf Club"
   PlaceGeo.FromWkt("POINT(-56.163740158081055 -34.92478600243492)")
endNew

New
   PlaceId = 3
   PlaceName = "Ramirez Beach"
   PlaceGeo.FromGeoJson('{"type":"Point","coordinates":[-56.1701774597168,-34.91676309400329]}')
endnew

New PlaceId = 4   
   PlaceName = "Constituyente, Avenue"
   PlaceGeo.FromGeoJson('{ "type": "LineString", "coordinates": [ [ -56.18528366088867, -34.90571271703311 ], [ -56.17850303649902, -34.90641660705113 ], [ -56.15318298339844, -34.9140182347531 ], [ -56.14863395690918, -34.91521472314688 ] ] }')
endnew

new
  PlaceId = 5
  PlaceName = "Punta Carretas, Neighborhood" 
    &geojsonNeighborhood = '{ "type": "Polygon",  "coordinates": [ [ [-56.148808,-34.918453], ['
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

New
  PlaceId = 6
  PlaceName = "Bulevar Artigas, Boulevard"
  PlaceGeo.FromString("LINESTRING(-56.16090774536133 -34.928797162523516, -56.1650276184082 -34.89494244739731)") 
endnew

new   
   PlaceId = 7
   PlaceName = "Cerro, Neighborhood"
   PlaceGeo.FromString('POLYGON ((-56.248367 -34.873821, -56.266563 -34.876427, -56.263733 -34.890366, -56.268799 -34.893394, -56.26897 -34.900291, -56.264851 -34.902615, -56.253605 -34.895645, -56.247597 -34.895153, -56.246052 -34.889523, -56.248367 -34.873821, -56.248367 -34.873821))') 
endnew
```

### [KB Sample](#KB+Sample)

[Geography data type Sample](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?32657,,)

### [Requirements](#Requirements)

#### [**- API Key**](#-+API+Key)

To view a geographical variable or attribute in the form, only one provider is used: GoogleMaps. For this, you must configure an API Key.

In the case of Android apps, you must configure the [Android Maps API Key property](https://wiki.genexus.com/commwiki/wiki?19115).

In the case of Web Panels, you must configure the API Key for each control in the form, as follows:

`[imagen omitida: wiki id 32411]`

To obtain an API Key for JavaScript, click [here](http://developers.google.com/maps/documentation/javascript/get-api-key?hl=es).

For it to work properly, most likely you will need to enable more than one API for this Key. For Example: Maps JavaScript API, Maps static API, Geocoding API, Geolocation API are commonly used.

#### [**- Database Management Systems**](#-+Database+Management+Systems)

SQL Server: Version 2008 or higher is required.  
In the case of SQL Server 2014 or higher, the SQL Server 2012 Feature pack must be installed on the web server.

MySQL/MariaDB: Version 5.7.5 or higher.  
Version 8.0 is not supported yet.

Oracle: Oracle Locator or Oracle Spatial installed. For Oracle 11.g or higher, it’s already installed by default.

PostgreSQL: It’s necessary to install the PostGIS extension from PostgreSQL. At the time of database creation, you must set the value “postgis” in the property “PostgreSQL Extensions” (before executing the reorganization).

### [Limitations](#Limitations)

**DBMS:** In GeneXus 15, in DB2 and Informix this functionality is not supported.

### [Compatibility](#Compatibility)

In previous versions, to represent geographical information some functionalities were used, such as:  
- [Geolocation domain](https://wiki.genexus.com/commwiki/wiki?14644) (Deprecated)  
- [Map User Control in Web Panels](https://wiki.genexus.com/commwiki/wiki?5029) (Available)  
- [Grid with Control Type = Maps in Panels](https://wiki.genexus.com/commwiki/wiki?15309) (Available)  
- [Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274) (Available)

### [Geography Properties](#Geography+Properties)

|  |  |  |
| --- | --- | --- |
| **Property** | **Type Returned** | **Description** |
| Srid | int | Spatial Reference System Identifier (SRID). Identifies the reference system for the represented Geographic object.  See <https://en.wikipedia.org/wiki/SRID> |
| FeatureType | Character | String with the type name of the represented Geographic object.  Some supported types are POINT, LINE, and POLYGON; other supported types can be added in future releases.  The empty string represents the null or unsupported object. |

### [Geography Methods](#Geography+Methods)

|  |  |  |
| --- | --- | --- |
| **Method** | **Type Returned** | **Description** |
| [FromWKT(Character)](https://wiki.genexus.com/commwiki/wiki?18900) | Geography | Loads data into an attribute or variable based on the Geography data type from a representation in [WKT](https://wiki.genexus.com/commwiki/wiki?59398) format. |
| FromString(Character) | Geography | Analogous to the FromWkt method. Use the [FromWkt method](https://wiki.genexus.com/commwiki/wiki?18900). |
| [FromGeoJSON(Character)](https://wiki.genexus.com/commwiki/wiki?59777) | Geography | Loads data into an attribute or variable based on the Geography data type from a representation in [GeoJSON](https://wiki.genexus.com/commwiki/wiki?59399) format. |
| [ToGeoJSON()](https://wiki.genexus.com/commwiki/wiki?59810) | Char | Returns the GeoJSON representation of a Geography, GeoPoint, GeoLine, or GeoPolygon data type. |
| ToWkt() | Char | Converts the Geography data to WKT format. |
| [Distance(Geography)](https://wiki.genexus.com/commwiki/wiki?59381) | Int | Calculates the distance (in meters) between the Geography to which the method is applied and the parameter (both Geography data type must be GeoPoints or Geography containing a GeoPoint). |
| [Intersect(Geography)](https://wiki.genexus.com/commwiki/wiki?59378) | Boolean | Returns true if the Geography parameter intersects or is included in the Geography to which the method is applied. |
| ToGeoPoint(Geography) | GeoPoint | Converts the Geography to a GeoPoint type. |
| ToGeoLine(Geography) | GeoLine | Converts the Geography to a GeoLine type. |
| ToGeoPolygon(Geography) | GeoPolygon | Converts the Geography to a GeoPolygon type. |

There is also a static version of these methods.

**Note**: FromString and ToString methods are enabled for Geography data types just for compatibility reasons. Use **FromWkt** and **ToWkt methods**instead.

### [Scope](#Scope)

**DBMSs:** SQL Server, Oracle, MySQL, SAP Hana, PostgreSQL  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)


|  |
| --- |
| **Backlinks** |
| [Center property](https://wiki.genexus.com/commwiki/wiki?42220) | [Custom Center Attribute property](https://wiki.genexus.com/commwiki/wiki?42221) | [Custom Center Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42222) |
| [Distance method](https://wiki.genexus.com/commwiki/wiki?59381) | [DrawGeography method](https://wiki.genexus.com/commwiki/wiki?47024) | [FromGeoJSON method](https://wiki.genexus.com/commwiki/wiki?59777) |
| [FromString method](https://wiki.genexus.com/commwiki/wiki?12694) | [FromWkt method](https://wiki.genexus.com/commwiki/wiki?18900) | [KB:GeoCity Showcase](https://wiki.genexus.com/commwiki/wiki?49231) | [GeographySaved Event](https://wiki.genexus.com/commwiki/wiki?46858) |
| [GeoJSON Geographic data format](https://wiki.genexus.com/commwiki/wiki?59399) | [GeoLine data type](https://wiki.genexus.com/commwiki/wiki?59358) | [Geolocation - Show points near me](https://wiki.genexus.com/commwiki/wiki?16473) | [Geolocation - Showing My Location](https://wiki.genexus.com/commwiki/wiki?16433) |
| [Geolocation API - Scenarios](https://wiki.genexus.com/commwiki/wiki?21763) | [Geolocation domain](https://wiki.genexus.com/commwiki/wiki?14644) | [Geolocation domain and Geolocation external object](https://wiki.genexus.com/commwiki/wiki?52831) | [Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274) |
| [GeoLocation Picker](https://wiki.genexus.com/commwiki/wiki?15969) | [GeoPoint data type](https://wiki.genexus.com/commwiki/wiki?58058) | [GeoPolygon data type](https://wiki.genexus.com/commwiki/wiki?59361) | [Table of contents:GeoSuite](https://wiki.genexus.com/commwiki/wiki?52770) |
| [GeoSuite - Definitions](https://wiki.genexus.com/commwiki/wiki?52772) | [GeoSuite - Geography Data Type in UI](https://wiki.genexus.com/commwiki/wiki?52973) | [HowTo: Group and Visualize Geographic Data Logically](https://wiki.genexus.com/commwiki/wiki?48253) |
| [HowTo: Use the Maps Control Type in a Panel Grid](https://wiki.genexus.com/commwiki/wiki?54097) | [Intersect method](https://wiki.genexus.com/commwiki/wiki?59378) | [IsEmpty method](https://wiki.genexus.com/commwiki/wiki?9645) | [KML Geographic data format](https://wiki.genexus.com/commwiki/wiki?59400) |
| [Location Attribute property](https://wiki.genexus.com/commwiki/wiki?42209) | [Location Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42210) | [Maps Control Type](https://wiki.genexus.com/commwiki/wiki?15309) | [Maps Control Type Properties](https://wiki.genexus.com/commwiki/wiki?54092) |
| [Maps external object](https://wiki.genexus.com/commwiki/wiki?44309) | [OData Support in GeneXus](https://wiki.genexus.com/commwiki/wiki?40713) | [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) | [SetEmpty method](https://wiki.genexus.com/commwiki/wiki?9646) |
| [ToGeoJSON method](https://wiki.genexus.com/commwiki/wiki?59810) | [ToJson method](https://wiki.genexus.com/commwiki/wiki?37817) | [ToString method](https://wiki.genexus.com/commwiki/wiki?7090) | [ToWkt method](https://wiki.genexus.com/commwiki/wiki?59814) |
| [What is a static method](https://wiki.genexus.com/commwiki/wiki?39593) | [WKT Geographic data format](https://wiki.genexus.com/commwiki/wiki?59398) |

---
