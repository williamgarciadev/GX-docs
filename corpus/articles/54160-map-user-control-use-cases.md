---
title: "Map User Control Use Cases"
source_id: 54160
source_url: https://wiki.genexus.com/commwiki/wiki?54160
genexus_version: "18"
---

# Map User Control Use Cases

### [1. Draw Point](#1.+Draw+Point)

```
&Radisson = new GxMap.Point()
&Radisson.PointLat         = "-34.9056247303566"
&Radisson.pointLong        = "-56.198415756225586"
&Radisson.PointInfowinTit  ='XIX International GeneXus Meeting'
&Radisson.PointInfowinDesc = "Radisson Montevideo Victoria Plaza Hotel - September 14-16"
&Radisson.PointInfowinLink = "http://genexus.com/event/"

&Radisson.PointInfowinLinkDsc = "Genexus Site" 

&Radisson.PointIcon       = "Red" // or &Radisson.PointIcon = "http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=|FE6256|000000"
&Radisson.PointInfowinImg = "http://wiki.gxtechnical.com/commwiki/servlet/apgetwikiimage?6327,1" // Some image
&GxMapdata.Points.Add(&Radisson)
```

**Note**: Google has a [dynamic icon generator](https://developers.google.com/chart/image/docs/gallery/dynamic_icons).

The sample is consolidated in the object's start event when dragging and dropping the control.

### [2. Draw Line](#2.+Draw+Line)

```
&MapLine = new()
&MapLinePoint = new()
&MapLinePoint.PointLat  = '31.223182'
&MapLinePoint.PointLong = '121.44654'
&MapLine.Points.Add(&MapLinePoint)

&MapLinePoint = new()
&MapLinePoint.PointLat  = '31.228209'
&MapLinePoint.PointLong = '121.474006'
&MapLine.Points.Add(&MapLinePoint) 

&GxMapData.Lines.Add(&MapLine)
```

### [3. Draw Polygon](#3.+Draw+Polygon)

```
&GxMapPolygon = new GxMap.Polygon(

&GxMapPolygon.PolygonFill = "#00AAFF"
&GxMapPolygon.PolygonFillOpacity = 0.80
&GxMapPolygon.PolygonStroke ="#FFAA00"
&GxMapPolygon.PolygonStrokeOpacity = 0.50
&GxMapPolygon.PolygonStrokeWeight = 2
&GxMapPolygon.PolygonInfowinHtml = "Plaza Independencia"

&GxMapPolyPath = new GxMap.Polygon.Path()

&GxMapPolyPath.PathLat = '-34.90691372574081'
&GxMapPolyPath.PathLong = '-56.198716163635254'
&GxMapPolygon.Paths.Add(&GxMapPolyPath )

&GxMapPolyPath = new GxMap.Polygon.Path()

&GxMapPolyPath.PathLat = "-34.906077860733134"
&GxMapPolyPath.PathLong = "-56.19883418083191"
&GxMapPolygon.Paths.Add(&GxMapPolyPath )

&GxMapPolyPath = new GxMap.Polygon.Path()

&GxMapPolyPath.PathLat = "-34.90617464553802"
&GxMapPolyPath.PathLong = "-56.20078682899475"
&GxMapPolygon.Paths.Add(&GxMapPolyPath )

&GxMapPolyPath = new GxMap.Polygon.Path()

&GxMapPolyPath.PathLat = "-34.90718647984938"
&GxMapPolyPath.PathLong = "-56.200679540634155"
&GxMapPolygon.Paths.Add(&GxMapPolyPath )

&GxMapPolyPath = new GxMap.Polygon.Path()

&GxMapPolyPath.PathLat = "-34.90691372574081"
&GxMapPolyPath.PathLong = "-56.198716163635254"
&GxMapPolygon.Paths.Add(&GxMapPolyPath )

&GxMapData.Polygons.Add(&GxMapPolygon )
```

### [4. Get coordinate from address (Geocoding - Google)](#4.+Get+coordinate+from+address+%28Geocoding+-+Google%29)

```
 &CollectionGeopoints = Maps.GeocodeAddress(&address)
 for &geopoint in &CollectionGeopoints
      GoogleMapControl1.Latitude = &geopoint.latitude.Tostring() //center the map in the coordinates
      GoogleMapControl1.Longitude = &geopoint.longitude.Tostring()
      GoogleMapControl1.Precision = &precision
      exit
  endfor
```

Or another way to do the same is as follows:

```
&httpclient.Host = 'maps.google.com'                       //load the associated host
&httpclient.Secure = 1
&httpclient.BaseUrl     = '/maps/api/geocode/'
&postvar = 'xml?address=' + &address + '&sensor=false&key=' + &apikey
&httpclient.Execute('GET',&postvar)                       //execute a GET operation
&var = &httpclient.ToString()

&xmlreader.OpenFromString(&var) //parse the coordinates
&xmlreader.Read()
&xmlreader.ReadType(1,'lat')
&lat = &xmlreader.Value
&xmlreader.ReadType(1,'lng')
&long = &xmlreader.Value

GoogleMapControl1.Latitude =&lat //center the map in the coordinates
GoogleMapControl1.Longitude = &long
GoogleMapControl1.Precision = &precision
```

According to the new google security policies, it is necessary to acquire an API key and send it in each request, more [details here](https://developers.google.com/maps/documentation/javascript/examples/geocoding-simple).  
Other service offer the same geocoding service, such us [Here](https://developer.here.com/api-explorer/rest/geocoder/latitude-longitude-by-free-form-address), [OpenStreetMap](https://nominatim.openstreetmap.org/search?q=Avenida%20Italia+6201+Montevideo&format=xml&polygon=1&addressdetails=1), [ArcGis](https://www.arcgis.com/home/item.html?id=305f2e55e67f4389bef269669fc2e284)

Other design (or runtime) properties of the control are as follows:

* Precision (zoom scale is 1 to 16)
* Type of map (map, satellite photo, or hybrid)
* Controls can be included within the map such as zoom, overview, etc.

### [5. Get route between two points](#5.+Get+route+between+two+points)

* Set the **Travel\_Mode** control property -> Driving or Walking
* Populate the [SDT](https://wiki.genexus.com/commwiki/wiki?2427) Routing points, programming something like the following:

```
&routingpoint = new()
&routingpoint.Latitude = 'xxxxxxx'
&routingpoint.Longitude = 'yyyyyy'
&routingpoint.Description = 'Work'
&routingpoint.Pin = "blank.png"
&GxMapData.Routing.add(&routingpoint)

&routingpoint = new()
&routingpoint.Latitude = 'xxxxxxx2'
&routingpoint.Longitude = 'yyyyyyy2'
&routingpoint.Description = 'House'
&routingpoint.Pin = "blank.png"
&GxMapData.Routing.Add(&routingpoint)
```

`[imagen omitida: wiki id 40199]`

### [6. Get coordinates just by clicking on the map](#6.+Get+coordinates+just+by+clicking+on+the+map)

* Set the **On Click** control property = Get Value
* In an event, program something like this:

```
    for &point in &GxMapData.Points
        msg(&point.PointLat)
        msg(&point.PointLong)
    endfor
```

Where &point is based on GxMap.Point Data type and GX Map Control property = &GxMapData (based on GXMap Type).

**Important:** getLongitude and getLatitude properties were used in previous versions (deprecated).

### [7. Get coordinates and open a popup just by clicking on the map](#7.+Get+coordinates+and+open+a+popup+just+by+clicking+on+the+map)

Set Click\_Lat and Click\_Long variables into ClickLatitude/ClickLongitude design properties.

```
Event GoogleMapControl1.Click
        &Window.Object = WPAsPopup.Create(&ClickLatitude , &ClickLonigtude)
        &Window.Open()
EndEvent
```

### [8. How to Import KML file on the map](#8.+How+to+Import+KML+file+on+the+map)

To show the United State Map provided by a KmL file located under http://developers.google.com/kml/documentation/us\_states.kml , programming something like the following:

```
Event Start
    GoogleMapControl1.KML = true
    GoogleMapControl1.KMLURL = "developers.google.com/kml/documentation/us_states.kml"
Endevent
```

`[imagen omitida: wiki id 40200]`


|  |
| --- |
| **Backlinks** |
| [KMLURL property](https://wiki.genexus.com/commwiki/wiki?42415) | [Map User Control](https://wiki.genexus.com/commwiki/wiki?5029) |

---
