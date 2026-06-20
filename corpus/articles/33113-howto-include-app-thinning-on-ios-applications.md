---
title: "HowTo: Include App Thinning on iOS applications"
source_id: 33113
source_url: https://wiki.genexus.com/commwiki/wiki?33113
genexus_version: "18"
---

# HowTo: Include App Thinning on iOS applications

As of iOS 9, Apple introduces the concept of App Thinning. Its aim is to reduce the size of the application when the end user downloads it from the AppStore.

## [How does it work?](#How+does+it+work%3F)

Apple smart devices execute over the next architecture and, depending on the device traits, it will use some resources or others.

`[imagen omitida: wiki id 33115]`

In these terms, every application properly developed with GeneXus can be published on the AppStore and when the end user downloads it, the application itself will request for the necessary and sufficient resources to execute it in a certain device. This concept of 'variants' is schematically described in the diagram below.

`[imagen omitida: wiki id 33751]`

## [What does "properly developed" mean?](#What+does+%22properly+developed%22+mean%3F)

Every developer should know that is a good practice to develop applications using [multiple layouts](https://wiki.genexus.com/commwiki/wiki?23489), [image variants](https://wiki.genexus.com/commwiki/wiki?31379) and an independent [theme](https://wiki.genexus.com/commwiki/wiki?16595) for each platform (occasionally using inheritance of them). If they follow these simple guidelines, an iOS generated application is able to recognize the "*necessary and sufficient*" resources mentioned a few lines above, and the end users can download only those, saving a significant amount of storage space of their device.

For example, if the developer designs the application for an iPad Mini, certain resources will be downloaded from the AppStore when the end user installs the application

`[imagen omitida: wiki id 33114]`

But, if the developer also designs the application for an iPhone 6 Plus, other resources will be downloaded.

`[imagen omitida: wiki id 33752]`

## [Scope](#Scope)

|  |  |
| --- | --- |
| **SD Generators** | iOS |
| **Languages** | .NET, Java |

## [Availability](#Availability)

This functionality is available as of [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,)

## [See also](#See+also)

`[imagen omitida: wiki id 20668]` [Apple Platforms & GeneXus](https://www5.genexus.com/meeting2016/gx26.tracks.aspx#es/Apple-Platforms-y-GeneXus)
