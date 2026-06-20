---
title: "GeoSuite - Maps Control Type in Grids"
source_id: 54084
source_url: https://wiki.genexus.com/commwiki/wiki?54084
genexus_version: "18"
---

# GeoSuite - Maps Control Type in Grids

The Maps Control Type (offered in Grids) provides a way to display locations and geometries, using a map and interacting with them.

So, when you list data in a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) that contains a "location" field, it may be displayed as a map by setting the Grid Control Type property to **Maps**.

A "location" is an attribute or variable based on the [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) (or its derived data type GeoPoint). [Geolocation domain](https://wiki.genexus.com/commwiki/wiki?14644) can also be used to define locations, but its use will be discontinued (Geography will replace it).

For example, if a [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) of Waste Containers is defined, you could see the location of the containers on a map, with their different icons depending on the type of container.

`[imagen omitida: wiki id 54088]`

To see more details on how to design that Panel, go to [Maps Control Type - Using the control](https://wiki.genexus.com/commwiki/wiki?54097).

### [Requirements](#Requirements)

To enable the device to display a map, you must get the API keys for the map providers you will be using in your application.

|  |  |  |
| --- | --- | --- |
| Apple | Apple Maps | No API keys needed |
| Google Maps | [Apple Maps API Key property](https://wiki.genexus.com/commwiki/wiki?39268) must be used |
| Android | Google Maps | [Android Google Services API Key property](https://wiki.genexus.com/commwiki/wiki?37267) must be used |
| MapBox | [Android Maps API Key property](https://wiki.genexus.com/commwiki/wiki?19115) and [Mapbox API Private Key property](https://wiki.genexus.com/commwiki/wiki?47972) must be used |
| Baidu Maps | [Android Maps API Key property](https://wiki.genexus.com/commwiki/wiki?19115) must be used |
| AutoNavi Maps |

### [Properties, Methods & Events](#Properties%2C+Methods+%26+Events+)

There are several properties, Methods and Events for controlling the behavior of the Maps control.

For example, there are properties to indicate the attribute/variable that offers the coordinates (Location attribute), properties to specify the GeoPoints icons (Pin Image), or properties to Zoom or Center, are some of the functionalities. There are also properties to turn on and off the different Layers (Selection, Direction, Animation).

To get more details about the available properties, go to [GeoSuite - Maps Control Type Properties](https://wiki.genexus.com/commwiki/wiki?54092).

A set of methods and events are available that allow, among other things, to use the map in edit mode, draw geometries, and load KML files.

Properties para indicar el atributo/variable que ofrece las coordenadas (Location attribute) , o propiedades para especificar los iconos de los geopuntos( Pin Image) o propiedades para hacer Zoom o Center son algunas de las funcionalidades. Tambien propiedades para prender y apagar las diferentes Layers (Selection, Directom aniimation) are available   
Para obtener todo el detalle de las propiedades disponibles diirijirse a [GeoSuite - Maps Control Type Properties](https://wiki.genexus.com/commwiki/wiki?54092)

Se disponibilizan un conjunto de metodos y eventos que permiten entre otras cosas ,usar el mapa en modod ediciomn, dibujar geometrias y cargar archivos KML

[GeoSuite - Maps Control Type Events Methods](https://wiki.genexus.com/commwiki/wiki?54095)
