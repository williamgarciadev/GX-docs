---
title: "Map User Control Properties"
source_id: 54170
source_url: https://wiki.genexus.com/commwiki/wiki?54170
genexus_version: "18"
---

# Map User Control Properties

The properties described below are available to be set when working with a [Map User Control](https://wiki.genexus.com/commwiki/wiki?5029).

### [General Control Properties](#General+Control+Properties)

|  |
| --- |
| [Provider](https://wiki.genexus.com/commwiki/wiki?42429) |
| [Google Api Key](https://wiki.genexus.com/commwiki/wiki?42425) |
| Type |
| [City](https://wiki.genexus.com/commwiki/wiki?42430) |
| [Latitude](https://wiki.genexus.com/commwiki/wiki?42431) |
| [Longitude](https://wiki.genexus.com/commwiki/wiki?42432) |
| [Precision](https://wiki.genexus.com/commwiki/wiki?39306) |
| [Style](https://wiki.genexus.com/commwiki/wiki?42433) |
| [ControlName](https://wiki.genexus.com/commwiki/wiki?8754) |
| [Small Control](https://wiki.genexus.com/commwiki/wiki?42407) |
| [Small Zoom](https://wiki.genexus.com/commwiki/wiki?42402) |
| [Large Control](https://wiki.genexus.com/commwiki/wiki?42403) |
| [Over View](https://wiki.genexus.com/commwiki/wiki?42401) |
| [Scale Control](https://wiki.genexus.com/commwiki/wiki?42409) |
| [Icon](https://wiki.genexus.com/commwiki/wiki?42420) |
| [Open Links In New Window](https://wiki.genexus.com/commwiki/wiki?42426) |
| [get Icon](https://wiki.genexus.com/commwiki/wiki?42416) |
| [Onclick](https://wiki.genexus.com/commwiki/wiki?42417) |
| [Click Latitude](https://wiki.genexus.com/commwiki/wiki?42411) |
| [Click Longitude](https://wiki.genexus.com/commwiki/wiki?42412) |
| [KML property](https://wiki.genexus.com/commwiki/wiki?42414) |
| [KMLURL](https://wiki.genexus.com/commwiki/wiki?42415) |
| [Travel Mode](https://wiki.genexus.com/commwiki/wiki?42428) |

**Note**: The Data binding Icon property still isn't taken into account at runtime.

### [Google Provider Properties](#Google+Provider+Properties)

* City – coordinates (Latitude, Longitude) of the city represented in grades. They are defined in User control/Map/Mapdefinition.xml.
* Specific Latitude – the value is represented in grades. N/E positive, S/W negative.
* Specific Longitude – the value is represented in grades. N/E positive, S/W negative.
* Precision - levels 1 to 16 to indicate the zoom (the higher the number, the closer the zoom).

  ```
  map.setCenter(new GLatLng(This.Latitude,this.Longitude), This.Precision );
  ```
* Type

  + Map
  + Satellite Image
  + Hybrid

    ```
     map.setMapType(this.Type);
    ```
* Access Key – the key is obtained from <http://www.google.com/apis/maps/signup.html>. The URL for publishing the map has to be specified. It has some restrictions such as the number of accesses per day to the page.

  + **Small -** let us pan/zoom the map.

    ```
    map.addControl(newGSmallMapControl());
    ```
  + **SmallZoom**

    ```
    map.addControl(new GSmallZoomControl());
    ```
  + **Type** 

    ```
    map.addControl(newGMapTypeControl());
    ```
  + `Overview`(Only Google)

    ```
    map.addControl(new GOverviewMapControl());
    ```
  + **Large**

    ```
    map.addControl(new GLargeMapControl());
    ```
  + **Scale**

    ```
    map.addControl(new GScaleControl());
    ```

### [Yahoo Provider Properties (Deprecated)](#Yahoo+Provider+Properties+%28Deprecated%29+)

`[imagen omitida: wiki id 7351]`

Precision - levels 1 to 16 to indicate the zoom (the smaller the number, the closer the zoom).

* City – Similar to Google's implementation

  ```
  map.drawZoomAndCenter(new YGeoPoint(this.Latitude,this.Longitude, this.Precision)
  ```

  Type
* Specific Latitude – the value is represented in grades. N/E positive, S/W negative.
* Specific Longitude – the value is represented in grades. N/E positive, S/W negative.

  + Map
  + Satellite Image
  + Hybrid

    ```
    map.setMapType(value);
    ```
  + **Small -** lets us pan/zoom the map.

    ```
    map.addZoomLong();
    ```
  + ****SmallZoom****

    ```
    map.addZoomShort();
    ```
  + **Type**

    ```
    map.addTypeControl()
    ```
  + **Large**

    ```
    map.addPanControl();
    ```
  + **Scale**

    ```
    map.addZoomScale()
    ```


|  |
| --- |
| **Backlinks** |
| [Map User Control](https://wiki.genexus.com/commwiki/wiki?5029) |

---
