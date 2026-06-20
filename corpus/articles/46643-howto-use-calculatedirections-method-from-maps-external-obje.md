---
title: "HowTo: Use CalculateDirections method from Maps external object"
source_id: 46643
source_url: https://wiki.genexus.com/commwiki/wiki?46643
genexus_version: "18"
---

# HowTo: Use CalculateDirections method from Maps external object

The CalculateDirections method offered by the [Maps external object](https://wiki.genexus.com/commwiki/wiki?44309) allows getting Directions between two points.

`[imagen omitida: wiki id 54806]`

### [Parameters](#Parameters)

|  |  |  |
| --- | --- | --- |
| **sourceLocation** | GeoPoint | The source location for the route. |
| **destinationLocation** | GeoPoint | The destination location for the route. |
| **transportType** | TransportType | The transport type to use when calculating the route. It is based on the TransportType [Enumerated Domain](https://wiki.genexus.com/commwiki/wiki?2207). The possible values are: Walking, Driving, Bicycling, and Transit. |
| **requestAlternateRoutes** | Boolean | Whether the service will serve multiple alternative routes. |

When you call the CalculateDirections method from a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293), it returns a Directions [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021):

### 

On the other hand, when you call the CalculateDirection method from a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829), the behavior is asynchronous. That is to say, you call the method and it doesn't return anything; however, after a few seconds, the **DirectionCalculate event** is automatically invoked and it receives the Directions SDT as a parameter. So, in this event, you have to define what you want to do with the SDT content.

### [Syntax](#Syntax)

Direction = Maps.CalculateDirections(GeoPoint, GeoPoint, TransportType, Boolean)

### [Sample](#Sample)

```
&directionsMaps = Maps.CalculateDirections(Geopoint.fromwkt("POINT (-56.1983300 -34.9064600)"), Geopoint.fromwkt("POINT (-56.2066700 -34.9101100)"), TransportType.Driving,false)
```

It returns a Direction Route. The serialization Json of this Route should be something like this:

```
{"Routes":[{"name":"Plaza Independencia",
           "distance":1439,
          "expectedTravelTime":266,
          "transportType":"DRIVING",
          "geoline":"LINESTRING (-56.19833 -34.90642, -56.19874 -34.90645, -56.19874 -34.90645, -56.19877 -34.90621, -56.19878 -34.90617, -56.1988 -34.90612, -56.19881 -34.9061,... ,-56.20671 -34.91003)"
          }]
}
```

## [Another use case](#Another+use+case)

Since [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,), the CalculateDirections method can be used with a parameter (shown as DirectionsParameters) based on the DirectionsRequestParameters [SDT](https://wiki.genexus.com/commwiki/wiki?2427) (it allows using waypoints).

`[imagen omitida: wiki id 54808]`

### [Sample](#Sample)

```
&iniGeoPoint.FromString("POINT(-56.134953860299575 -34.901402497181124)") 
&FinGeoPoint.FromString("POINT(-56.146807789135565 -34.88463356035207)")   
&wayPoint1.FromString("POINT(-56.163740158081055 -34.92478600243492)")

&directionsrequestparameter.sourceLocation = &iniGeoPoint
&directionsrequestparameter.destinationLocation = &FinGeoPoint
&directionsrequestparameter.waypoints.Add(&wayPoint1)

&directions = Maps.CalculateDirections(&directionsrequestparameter)
```

### [Availability](#Availability)

This method is available since [GeneXus 16 upgrade 6](https://wiki.genexus.com/commwiki/wiki?43978,,).


|  |
| --- |
| **Backlinks** |
| [Maps external object](https://wiki.genexus.com/commwiki/wiki?44309) |

---
