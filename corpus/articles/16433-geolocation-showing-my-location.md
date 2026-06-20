---
title: "Geolocation - Showing My Location"
source_id: 16433
source_url: https://wiki.genexus.com/commwiki/wiki?16433
genexus_version: "18"
---

# Geolocation - Showing My Location

**Warning**: The [Maps external object](https://wiki.genexus.com/commwiki/wiki?44309) is newer than the Geolocation external object. Many of the methods and properties provided by both external objects are similar. The difference consists in the fact that the [Maps external object](https://wiki.genexus.com/commwiki/wiki?44309) uses the [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) while the Geolocation external object uses the Geolocation domain (which is deprecated). In addition, the Maps external object includes more functionalities. The use of the Maps external object and the Geography data type is highly recommended. Therefore, to solve this feature, read [HowTo: Use GetLocation method from Maps external object](https://wiki.genexus.com/commwiki/wiki?46780).

Every day, the postal service employee has to deliver many letters, and for this reason he needs to know the places near his delivery points, based on his current location.

To this end, we will create a Transaction where we will store all of the post office's requirements. In addition, we will have a smart device application to display, in a map, the delivery points (using the [Control type SDMaps](https://wiki.genexus.com/commwiki/wiki?15309)) and its current position (using the GetMyLocation method of the GeoLocation External Object).

Below is a detailed description of the four steps required for this implementation. See in detail the four steps to perform this implementation.

### [1. Create the PostOffice Transaction](#1.+Create+the+PostOffice+Transaction)

First, create the [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) that will be used to store all of the Post Office's requirements.

```
POReqId *           // Numeric(10.00) Autonumber property = True
POREqAddress        // Character(500): Address or description
POReqLoc            // Geolocation: Latitude, Longitude
POReqDeliver        // Boolean
PoReqPin            // Image: Image Icon
```

### [2. Create a [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) and an Entry Panel (WWPostNear) based on WorkWithdevicesPostOffice](#2.+Create+a+wiki%3F16321%2CCategory%253AMenu%2Bobject+Menu+object+and+an+Entry+Panel+%28WWPostNear%29+based+on+WorkWithdevicesPostOffice)

Apply the Work With for Smart Devices pattern (WorkWithDevicesPostOffice will be created) and set:

* List/Grid/Control Type = SD MAPS
* List/Grid/Location Attribute = POReqLoc
* List/Grid/Pin image Attribute = POReqPin

`[imagen omitida: wiki id 16435]`

Create a [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) and add WorkWithDevicesPostOffice item. (For further information see [Applying Work With Pattern](https://wiki.genexus.com/commwiki/wiki?15975)).

### [3. Get my location and store it in the database](#3.+Get+my+location+and+store+it+in+the+database)

Create the "**GetMyLoc**" action in the WorkWithDevicesPostOffice List object, and invoke the **GetMyLocation** method.

To create the action, click on List node, go to Events and select the "Add" action button (GetMyLoc). To invoke the GetMyLocation method, go to Events and write the following code:

```
Event 'GetMyloc'
    &GetMyLocation = Geolocation.GetMyLocation(0,0,false)
EndEvent
// where:
//        &GetMyLocation is based on GeoLocationInfo Data type, 
//        Geolocation is not a variable, it's an external object's static reference
```

Note: The GetMyLocation method must be invoked from an action; it can’t be invoked from a procedure because this method is executed on the device side.

Create a nested action and from there invoke the procedure that stores “my position” in the database (the [Composite command](https://wiki.genexus.com/commwiki/wiki?17389) clause must be used to synchronically trigger nested actions). This action sets the GeoLocationInfo parameter, which is the result of invoking the GetMyLocation method mentioned above. It will be similar to the following:

```
Event 'GetMyloc' 
    Composite
         &GetMyLocation = Geolocation.GetMyLocation(0,0,false) 
         StoreMyLocation(&GetMyLocation)
    EndComposite
EndEvent
```

The **StoreMyLocation** procedure is similar to the following:

```
parm(&GetMyLocation); //Important: the name of the parmeter MUST Be the same of the Method which is invoked

new
    POReqAddress = 'I am Here'
    POReqLoc = &GetMyLocation.Location
    POReqDeliver = false
    PoReqPin.FromImage(here)
endnew
```

Create a nested action to refresh the data, writing code similar to this: SD Actions.Refresh().  
  
In the end it will look as follows:

`[imagen omitida: wiki id 16436]`

### [4. Execute](#4.+Execute+)

When executing, it looks like:

`[imagen omitida: wiki id 16439]`

A complete Knowledge Base of these examples is available [here](https://wiki.genexus.com/commwiki/wiki?20658,,).

### [See also](#See+also)

[Geolocation - Show points near me](https://wiki.genexus.com/commwiki/wiki?16473)  
[Geolocation - Showing My Location](https://wiki.genexus.com/commwiki/wiki?16433)  
[Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274)


|  |
| --- |
| **Backlinks** |
| [Geolocation - Showing My Location](https://wiki.genexus.com/commwiki/wiki?16433) | [Geolocation API - Scenarios](https://wiki.genexus.com/commwiki/wiki?21763) | [GetMyLocation method](https://wiki.genexus.com/commwiki/wiki?25164) |
| [HowTo: Use SD Geolocation Control in Smart Devices](https://wiki.genexus.com/commwiki/wiki?16756) |

---
