---
title: "MapsOffline External Object"
source_id: 48363
source_url: https://wiki.genexus.com/commwiki/wiki?48363
genexus_version: "18"
---

# MapsOffline External Object

It is possible to download the mapping of an area and access it offline. This functionality is offered by mapping providers, such as [Mapbox](https://docs.mapbox.com/android/plugins/guides/offline/).   
Google Maps APIs do not provide this functionality.

## [Scope](#Scope)

Generators: [Android](https://wiki.genexus.com/commwiki/wiki?14453)

## [Description](#Description+)

A specific example is an application that collects points (geopoints) in rural areas with low connectivity. In this case, there is no connectivity to navigate the mapping of the site. Although mapping providers (Google, Apple, Baidu, Mapbox) offer a cache that provides offline access to areas that have already been navigated, this is a very sensitive mechanism. Zooming in is already a connection trigger to obtain the mapping.

## [Implementation](#Implementation)

Create a new MapsOffline External Object.  
`[imagen omitida: wiki id 48457]`

With the following methods, events, and properties:  
`[imagen omitida: wiki id 48458]`

### [**MapsOffline External Object**](#MapsOffline+External+Object+)

#### **Properties**

##### **IsOfflineGeographicDataSupported**

MapsOffline.IsOfflineGeographicDataSupported: Boolean

Indicates whether the map provider being used supports downloading data for offline use.

##### [**DownloadedRegions**](#DownloadedRegions)

MapsOffline.DownloadedRegions: Character Collection

Returns the list of names of the regions already downloaded.

##### [**Size**](#Size)

MapsOffline.Size: Numeric (9.0)

Returns the space currently taken by the offline region database in the KB.  
In Android, this file is Directory.ApplicationDataPath/mbgl-offline.db.

#### [**Methods**](#Methods)

##### **DownloadRegion**

*Boolean = DownloadRegion(Character regionName, Geopoint northEast, GeoPoint southWest, int minZoom, int maxZoom)*

Parameters:

* **RegionName:** identifies the region. If an identifier that already exists is indicated, the method returns false and the download is not performed.
* **NorthEast** and **SouthWest:** determine the rectangular area for which to download the maps.
* **MinZoom** and **MaxZoom** are a number between 1 and 22 that determines the Zoom level. If no min or max values are given, the provider's minimum and maximum values are assumed.

The second version will have parameter overloading and it will be possible to define the region by **center** and **radius.**

*Boolean = DownloadRegion(Character regionName, Geopoint Center, Numerio Radio, int minZoom, int maxZoom)*

Note: There is a restriction to parameter overloading when they have the same quantity and different types; that's why it is not implemented in the first version.

##### [**CancelRegionDownload(Character regionName)**](#CancelRegionDownload%28Character+regionName%29)

Cancels the download of a region pending download or in progress. It has no effect if the region does not exist or was already canceled.

##### [**PauseRegionDownload(Character regionName)**](#PauseRegionDownload%28Character+regionName%29)

Pauses the download of a region pending download or in progress. It has no effect if the download was already paused, canceled, or does not exist.

##### [**ClearRegions**](#ClearRegions)

*ClearRegions()*

Deletes all downloaded zones from the device.

##### [**ClearRegion**](#ClearRegion)

*ClearRegion(Character RegionName)*

Deletes the downloaded zones from the device, based on their names.

##### [**GetRegionStatus**](#GetRegionStatus)

*GetRegionStatus(Character regionName): MapRegion (new SDT)*

The MinZoom and MaxZoom fields contain the current map zooming.

#### [**Event**](#Event)

##### **RegionDownloadEnded**

```
Event MapsOffline.RegionDownloadEnded(Character regionName, Messages messages)
  ...
EndEvent
```

Returns the name of the region that has just been downloaded and the messages associated with the download (errors, warnings, and other information from the provider).

### [**Grid with Control Type = Maps**](#Grid+with+Control+Type+%3D+Maps)

The Grid with Control Type = Maps has the following method:

#### [**GetVisibleRegion**](#GetVisibleRegion)

*MapGrid.GetVisibleRegion:* MapRegion *(new SDT)*

Returns the Northeast and Southwest coordinates of the area displayed on the Grid.

## Use Cases

### [Case 1. Download region by UX](#Case+1.+Download+region+by+UX)

From the application, the area displayed on the map with the specified zoom.

`[imagen omitida: wiki id 53955]`

For this, you must program something like having a Grid with Control Type = Maps and a "download" user event with the following code:

```
Event 'download'
        &MapRegion = MapGrid.GetVisibleRegion()
        DownloadRegion("MyCity", &MapRegion.GeoPointNE, &MapRegion.GeoPointSW, &MinZoom, MaxZoom)
endevent

Event  MapsGrid.downloadRegionEnd("MyRegion")
      &LocalNotificationsItems.Text = "Download Region successfully"
      &LocalNotifications.Add(&LocalNotificationsItems)
      LocalNotifications.CreateAlerts(&LocalNotifications)
EndEvent
```

### [Case 2. Download automatically](#Case+2.+Download+automatically)

Automatically download a region that the application will navigate.

For example, suppose there is a combo box of Cities or Neighborhoods in the App. Based on the user’s selection, a code like the following is invoked (in user event or Client Start):

```
Composite
     GetRegionBoundary("MyCity", &geoPointNE, &geoPointSW, &MinZoom, MaxZoom)
     MapGsOffline.downloadRegion("MyCity", &geoPointNE, &geoPointSW, &MinZoom, MaxZoom)
EndComposite
```

Note: GetRegionBoundary is a procedure that initializes the values to define the region. Returns the Northeast and Southwest extremes, and the minimum and maximum zoom of the area.

## [SDTs](#SDTs)

### [MapRegion](#MapRegion)

`[imagen omitida: wiki id 48459]`

Name: Character  
NorthEast: GeoPoint  
SouthWest: GeoPoint  
MinZoom: Numeric  
MaxZoom: Numeric  
Status {Queued = 1, Downloading, Downloaded, Paused, Canceled}

## [Availability](#Availability)

Since [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,)


|  |
| --- |
| **Backlinks** |
| [HowTo: Maps - Mapbox](https://wiki.genexus.com/commwiki/wiki?48350) |

---
