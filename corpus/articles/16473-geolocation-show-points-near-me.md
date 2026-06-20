---
title: "Geolocation - Show points near me"
source_id: 16473
source_url: https://wiki.genexus.com/commwiki/wiki?16473
genexus_version: "18"
---

# Geolocation - Show points near me

**Warning**: The [Maps external object](https://wiki.genexus.com/commwiki/wiki?44309) is newer than the Geolocation external object. Many of the methods and properties provided by both external objects are similar. The difference consists in the fact that the [Maps external object](https://wiki.genexus.com/commwiki/wiki?44309) uses the [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) while the Geolocation external object uses the Geolocation domain (which is deprecated). In addition, the Maps external object includes more functionalities. The use of the Maps external object and the Geography data type is highly recommended. Therefore, to solve this feature, read [HowTo: Solve Geofencing with GeneXus](https://wiki.genexus.com/commwiki/wiki?53557,,).

Show My location and nearby places (20km). In order to do this, we will create a transaction to store all of the post office’s requirements. To view only nearby places, within a range of 20 km from my current position, all distances between my current position and those locations are recalculated. Distance values are stored in the database and filtered by a data selector. Then, the Smart Device application shows the delivery points (using the grid's [Maps Control Type](https://wiki.genexus.com/commwiki/wiki?15309)) type and the current position (using the GetMyLocation method of the GeoLocation External Object).

Below is a detailed description of the four steps required for this implementation.

### [1. Create the PostOffice transaction](#1.+Create+the+PostOffice+transaction)

First, create the transaction that will be used to store all of the Post Office's requirements.

```
POReqId *    // Numeric(10,00) Autonumber property = True
POREqAddress // Character(500): Address or description
POReqLoc     // Geolocation: Latitude, Longitude
POReqDeliver // Boolean
PoReqPin     // Image: Image Icon
POReqNear    // Boolean
POReDistance // Numeric(10,4)
```

### [2. Create a [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) and an Entry Panel **(WWPostNear)**](#2.+Create+a+wiki%3F16321%2CCategory%253AMenu%2Bobject+Menu+object+and+an+Entry+Panel+%28WWPostNear%29)

Apply the WWSmartDevices Pattern (WWPostOffices will be created), and set:

* List/Grid/Control Type = SD MAPS
* List/Grid/Location Attribute = POReqLoc
* List/Grid/Pin image Attribute = POReqPin

`[imagen omitida: wiki id 16475]`

Create a [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) and add the WorkWithDevicesPostOffice Item.

### [3. Get my position and calculate the distance to each point](#3.+Get+my+position+and+calculate+the+distance+to+each+point)

Create a "**NearPoints**" action in the WWPostNear List in the object and invoke the **GetMyLocation** method.

To create the action, click on List node, go to Events and select the Add action button (GetMyLoc). To invoke the GetMyLocation method, go to Events and write the following code:

```
Event 'NearPoints'
         &GetMyLocation = Geolocation.GetMyLocation(0,0,false)
EndEvent
// where:
//     &GetMyLocation is based on GeoLocationInfo Data type, 
//     Geolocation is not a variable , it's an external object's static reference
```

Note: The GetMyLocation method must be invoked from an action; it can’t be invoked from a procedure because this method is executed on the device side.

Create a nested action and from there invoke the procedure that stores “my position” in the database (the [Composite command](https://wiki.genexus.com/commwiki/wiki?17389) clause must be used to synchronically trigger nested actions).

This action sets the GeoLocationInfo parameter, which is the result of invoking the GetMyLocation method mentioned above. It will be similar to the following:

```
Event 'NearPoints'
    Composite
         &GetMyLocation = Geolocation.GetMyLocation(0,0,false) 
         StoreNear_Points(&GetMyLocation)
    EndComposite
EndEvent
```

This means that the **StoreNear\_Points** procedure inserts my position and updates the distance to all points stored in the database.

```
parm(&GetMyLocation)
for each                            // Calculate and update the distance of any points to my current location
     where POReqDeliver = false
         &Currdistance = &GeoLocation.GetDistance(&GetMyLocation.Location, POReqLoc)
         if &Currdistance <  &distance
            POReqNear = true
         else
            POReqNear = false
         endif
         POReqdistance = &distance
endfor
```

Create a nested action to refresh the data, writing code similar to this: **SD Actions.refresh()**.  
  
In the end it will look as follows:

`[imagen omitida: wiki id 16483]`

### [4. Create a [Data Selector object](https://wiki.genexus.com/commwiki/wiki?5271) an apply it to filter the nearby locations](#4.+Create+a+wiki%3F5271%2CCategory%253AData%2BSelector%2Bobject+Data+Selector+object+an+apply+it+to+filter+the+nearby+locations)

Create the Data Selector object as in:

`[imagen omitida: wiki id 16484]`

This condition should be defined: POReqNear = true or POReqdistance < &distance

`[imagen omitida: wiki id 16482]`

The Data Selector must be included in WWPostNear/List/DataSelector.

When executing, it looks as follows:

`[imagen omitida: wiki id 16481]`

A complete Knowledge Base of these samples is available [here](https://wiki.genexus.com/commwiki/wiki?20658,,).


|  |
| --- |
| **Backlinks** |
| [Geolocation - Showing My Location](https://wiki.genexus.com/commwiki/wiki?16433) | [Geolocation API - Scenarios](https://wiki.genexus.com/commwiki/wiki?21763) | [HowTo: Use SD Geolocation Control in Smart Devices](https://wiki.genexus.com/commwiki/wiki?16756) |
|

---
