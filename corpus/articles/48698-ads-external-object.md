---
title: "Ads External Object"
source_id: 48698
source_url: https://wiki.genexus.com/commwiki/wiki?48698
genexus_version: "18"
---

# Ads External Object

Allows managing interstitial ads in mobile applications. Interstitial ads are adverts displayed in full screen, completely covering the interface of the application until the user closes them. They are typically shown between application transitions, between activities, or during the pause between levels in some games. The user can tap and be redirected to the ad's destination or close it and return to the application.

|  |  |
| --- | --- |
|  |  |

## [**Scope**](#Scope)

**Platforms:**Android, Apple.

## [**Properties**](#Properties)

It doesn't have any.

## [**Methods**](#Methods)

### [**RequestInterstitial**](#RequestInterstitial)

Loads the interstitial. This has to be called in advance so that it is ready when the user wants to show it.

**Return: None**

**Parameters:**adUnitID:VarChar(40).

### [**IsInterstitialReady**](#IsInterstitialReady)

Checks if the interstitial has loaded correctly, and is ready to be shown; returns True if it is.

**Return:** Boolean

**Parameters:** adUnitID:VarChar(40).

### [**ShowInterstitial**](#ShowInterstitial)

Shows the interstitial if ready and returns True; otherwise, it returns False.

**Return:**Boolean

**Parameters:**adUnitID:VarChar(40).

**Note**

* adUnitId parameter: this value is only needed to load the interstitial but it is required in every call, so it acts as an object identifier. More than one ad can be loaded at the same time if they have a different adUnitId.
* Both providers have an adUnitId for testing. For easy testing, if an adUnitId "TEST" is sent, the corresponding adUnitId test will be used.

## [**Events**](#Events)

### [**InterstitialLoaded**](#InterstitialLoaded)

Called when the interstitial ad loaded successfully.

**Input:**adUnitID:VarChar(40).

**Output: none**

### [**InterstitialFailedToLoad**](#InterstitialFailedToLoad)

Called when the interstitial ad failed to load.

**Input:**adUnitID:VarChar(40).

**Output: none**

### [**InterstitialClicked**](#InterstitialClicked)

Called when the user clicks the ad. The ad is not closed when clicked.

**Input:**adUnitID:VarChar(40).

**Output: none**

### [**InterstitialClosed**](#InterstitialClosed)

Called when the interstitial ad is closed. The ad closes, and the event is called.

**Input:**adUnitID:VarChar(40).

**Output: none**

## [**Example**](#Example)

```
Event 'ShowInterstitial'

Composite

    &AdUnitId = !"TEST"
    Ads.RequestInterstitial(&AdUnitId)
    &success = Ads.ShowInterstitial(&AdUnitId)
    if not &success
         msg(!"Failed!")
    endif

EndComposite

Endevent
```

When this event is executed, you will see the following:

`[imagen omitida: wiki id 48707]`

## [**Availability**](#Availability)

This external object is available as of [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?48247,,).
