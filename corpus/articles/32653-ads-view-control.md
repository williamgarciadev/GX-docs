---
title: "Ads View control"
source_id: 32653
source_url: https://wiki.genexus.com/commwiki/wiki?32653
genexus_version: "18"
---

# Ads View control

Shows [Ads (Advertising)](https://wiki.genexus.com/commwiki/wiki?31361) on your applications in any place. This control is available in the [Toolbox](https://wiki.genexus.com/commwiki/wiki?10000) and supports several providers.

`[imagen omitida: wiki id 46181]`

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects:** | [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [WorkWith](https://wiki.genexus.com/commwiki/wiki?15974) |
| **Generators:** | [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453) |

## [Considerations](#Considerations)

For the Android generator, you must set the [Ads Provider property](https://wiki.genexus.com/commwiki/wiki?46274) at the [Main object](https://wiki.genexus.com/commwiki/wiki?17817) level.

## [Design-time properties](#Design-time+properties)

Specific properties are available depending on the value selected for the [Ads Provider property](https://wiki.genexus.com/commwiki/wiki?46274).

When [Ads Provider property](https://wiki.genexus.com/commwiki/wiki?46274) = 'AdMob'

|  |  |
| --- | --- |
| **Property** | **Description** |
| [Ad Unit Id property](https://wiki.genexus.com/commwiki/wiki?38571) | Identifier of the Ad that this control will display on the screen. This ad must be a [Banner](https://developers.google.com/admob/android/banner).  Refer to [HowTo: Get AdMob Unit Id for advertising in Native Mobile Applications](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?38451,,). |

When [Ads Provider property](https://wiki.genexus.com/commwiki/wiki?46274) = 'GoogleMobileAds'

|  |  |
| --- | --- |
| **Property** | **Description** |
| [Ad Unit Id property](https://wiki.genexus.com/commwiki/wiki?38571) | Identifier of the Ad that this control will display on the screen. This ad must be a [Banner](https://developers.google.com/ad-manager/mobile-ads-sdk/android/banner).  Refer to [Google Ad Manager - Get Started](https://developers.google.com/ad-manager/api/start). |

## [Run-time properties](#Run-time+properties)

### [AdUnitId](#AdUnitId)

Changes the Ad Unit Id design-time property at run-time. Its value must be character-based. Available when *Ads Provider property* has *AdMob* value.

`[imagen omitida: wiki id 38450]`

## [Methods](#Methods)

### [RequestAd](#RequestAd)

It forces the request for a new Ad in a specific time.  
**Return value** None  
**Parameters** None

## [Sample](#Sample)

First, turn on the [Enable Ads property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?38457,,) for the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770) for Native Mobile applications.  
Then drag (at least) one Ads View control from the toolbox inside the layout of a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829).

After that, you must set its properties properly depending on the provider.  
In this case, because the provider is AdMob, the identifier of the ad (occasionally more than one and different from each other).

`[imagen omitida: wiki id 33143]`

In this case, include a fixed ad on the bottom of the screen. You can do it by setting its properties on the Panel.

Finally, run your application and wait until your ads are displayed.

`[imagen omitida: wiki id 37560]`

Note how the controls on the edges of the screen are displayed and there is a fixed advertisement on the bottom.

## [Notes](#Notes)

* With the mechanism described here, you can include an Ad where you want. In the mechanism described in the [Ads (Advertising)](https://wiki.genexus.com/commwiki/wiki?31361) article, the default behavior is that every Panel contains an ad unless *Show Ads property* is disabled for those Panels that you don't want to show an ad.
* You can include multiple Ads View controls on the same [Panel object](https://wiki.genexus.com/commwiki/wiki?24829). In addition, you can set the *Show Ad*s and *Ads Position* properties (at the Panel level) to display them in a fixed position.

##


|  |
| --- |
| **Backlinks** |
| [Ad Unit Id property](https://wiki.genexus.com/commwiki/wiki?38571) | [AdMob Application ID property](https://wiki.genexus.com/commwiki/wiki?43504) |
| [Ads (Advertising)](https://wiki.genexus.com/commwiki/wiki?31361) | [Ads Provider property](https://wiki.genexus.com/commwiki/wiki?46274) |
| [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) |

---
