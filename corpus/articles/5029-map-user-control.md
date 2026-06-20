---
title: "Map User Control"
source_id: 5029
source_url: https://wiki.genexus.com/commwiki/wiki?5029
genexus_version: "18"
---

# Map User Control

The Map User Control allows including a map in a Web Layout (for example, in a [Web Panel Web Layout](https://wiki.genexus.com/commwiki/wiki?8132)) and marking points on it.

`[imagen omitida: wiki id 54246]`

When it is dragged from the Toolbox to a Web Layout, a sample is imported to mark some points on the map. As a result, variables and events are automatically defined. In addition, properties are set in those events and you can replace the default values.

### [Using the control](#Using+the+control)

The control is distributed by GeneXus; however, it is possible to download and install a newer version. To do so, download the control from [here](http://marketplace.genexus.com/product.aspx?mapcontrol) and decompress the zip file to the User control directory of the GeneXus installation.

Currently, there are three providers: Google, Baidu, and Yahoo for any city in the world.

As previously described, you have to drag the Map User Control from the Toolbox to the Web Layout. Then, a sample is imported, marking some points on the map. For each point, a title, text, and link can be specified.

To geoposition the map or to position a point on it, the coordinates (latitude/longitude) are needed. To this end, you can set the [Latitude property](https://wiki.genexus.com/commwiki/wiki?42431) and [Longitude property](https://wiki.genexus.com/commwiki/wiki?42432) (N/E positive number, S/W negative number).These values are in decimal degrees format. In addition, you can configure the Map User Control [City property](https://wiki.genexus.com/commwiki/wiki?42430).

To draw a point on a Map, you just have to program something like the following:

```
&BusStation = new GxMap.Point()
&BusStation.PointLat         = "-34.9056247303566"
&BusStation.pointLong        = "-56.198415756225586"
&BusStation.PointInfowinTit  ='!"Tres Cruces"
&BusStation.PointInfowinDesc = !"Terminal Tres Cruces"
&BusStation.PointInfowinLink = !"https://www.trescruces.com.uy/terminal/"
&Image.fromImage(BusStation)
&BusStation.PontIcon = &Image.ImageUri 

&GxMapdata.Points.Add(&Radisson)
```

At runtime, it is displayed as:

`[imagen omitida: wiki id 54186]`

For more details on how to program the most common use cases, go to [Map User Control Use Cases](https://wiki.genexus.com/commwiki/wiki?54160).

### [Properties](#Properties)

See the list of properties available to set for a Map User Control in: [Map User Control Properties](https://wiki.genexus.com/commwiki/wiki?54170).

### [Licensing](#Licensing)

Google Provider: <https://developers.google.com/maps/pricing-and-plans/>  
Since 22 June 2016, an API key is required: <http://googlegeodevelopers.blogspot.com.uy/2016/06/building-for-scale-updates-to-google.html>  
In order to get an API key, go to [https://developers.google.com/maps/web/](http://www.google.com/apis/maps/signup.html) with the following [terms of use](http://www.google.com/intl/en_ALL/help/terms_maps.html).  
Since June 2018, you must include an API key with all API requests and enable billing on each of your projects.  
<https://developers.google.com/maps/documentation/javascript/usage-and-billing>

Yahoo Provider: The component was discontinued by the provider.

### [Releases](#Releases)

**Breaking change:** To configure a Google Maps API key after [Google's policy changes](http://googlegeodevelopers.blogspot.com.uy/2016/06/building-for-scale-updates-to-google.html) of 22 June 2016, please download version 8.1 or higher from [here](https://wiki.genexus.com/commwiki/wiki?31556,,) or the [marketplace](https://marketplace.genexus.com/product.aspx?mapcontrol,es).

Please visit: [Default Installation Instructions for User Controls](https://wiki.genexus.com/commwiki/wiki?5920).


|  |
| --- |
| **Backlinks** |
| [Anchor Left property](https://wiki.genexus.com/commwiki/wiki?42423) | [Anchor Top property](https://wiki.genexus.com/commwiki/wiki?42424) | [Baidu Key property](https://wiki.genexus.com/commwiki/wiki?42427) |
| [Center When Click property](https://wiki.genexus.com/commwiki/wiki?42418) | [City property](https://wiki.genexus.com/commwiki/wiki?42430) | [Clear\_Overlay property](https://wiki.genexus.com/commwiki/wiki?42419) | [Click Latitude property](https://wiki.genexus.com/commwiki/wiki?42411) |
| [Click Longitude property](https://wiki.genexus.com/commwiki/wiki?42412) | [Display Number Clustered Points property](https://wiki.genexus.com/commwiki/wiki?54842) | [Display Style Clustered Points property](https://wiki.genexus.com/commwiki/wiki?54843) | [GeneXus Markup Language (GXML)](https://wiki.genexus.com/commwiki/wiki?46876) |
| [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) | [Toc:GeoSuite](https://wiki.genexus.com/commwiki/wiki?52770) | [GeoSuite - Geography Data Type in UI](https://wiki.genexus.com/commwiki/wiki?52973) |
| [get Icon property](https://wiki.genexus.com/commwiki/wiki?42416) | [Google Api Key property in Map User Control](https://wiki.genexus.com/commwiki/wiki?42425) | [Gx Map property](https://wiki.genexus.com/commwiki/wiki?42410) | [GXGoogle Visualization Library](https://wiki.genexus.com/commwiki/wiki?10447) |
| [Icon Height property](https://wiki.genexus.com/commwiki/wiki?42422) | [Icon property](https://wiki.genexus.com/commwiki/wiki?42420) | [Icon Width property](https://wiki.genexus.com/commwiki/wiki?42421) | [Information Control property](https://wiki.genexus.com/commwiki/wiki?42413) |
| [KML property](https://wiki.genexus.com/commwiki/wiki?42414) | [KMLURL property](https://wiki.genexus.com/commwiki/wiki?42415) | [Large\_Control property](https://wiki.genexus.com/commwiki/wiki?42403) | [Latitude property](https://wiki.genexus.com/commwiki/wiki?42431) |
| [Longitude property](https://wiki.genexus.com/commwiki/wiki?42432) | [Map Type\_Control\_Style property](https://wiki.genexus.com/commwiki/wiki?42404) | [Map User Control Properties](https://wiki.genexus.com/commwiki/wiki?54170) | [Marker Clustering property for Maps in Web Panels](https://wiki.genexus.com/commwiki/wiki?54841) |
| [Navigation\_Control\_Style property](https://wiki.genexus.com/commwiki/wiki?42405) | [Onclick property](https://wiki.genexus.com/commwiki/wiki?42417) | [Open Links In New Window property](https://wiki.genexus.com/commwiki/wiki?42426) | [Over View\_Control property](https://wiki.genexus.com/commwiki/wiki?42401) |
| [Provider property](https://wiki.genexus.com/commwiki/wiki?42429) | [Purpose Strings properties group](https://wiki.genexus.com/commwiki/wiki?32755) | [Scale\_Control property](https://wiki.genexus.com/commwiki/wiki?42409) | [Scroll Wheel property](https://wiki.genexus.com/commwiki/wiki?42406) |
| [Small\_Control property](https://wiki.genexus.com/commwiki/wiki?42407) | [Small\_Zoom\_Control property](https://wiki.genexus.com/commwiki/wiki?42402) | [Style property in Map User Control](https://wiki.genexus.com/commwiki/wiki?42433) | [Travel\_Mode property](https://wiki.genexus.com/commwiki/wiki?42428) |
| [Type\_Control property](https://wiki.genexus.com/commwiki/wiki?42408) | [Toc:Web User Controls](https://wiki.genexus.com/commwiki/wiki?27212) |

---
