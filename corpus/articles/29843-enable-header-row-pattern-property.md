---
title: "Enable Header Row Pattern property"
source_id: 29843
source_url: https://wiki.genexus.com/commwiki/wiki?29843
genexus_version: "18"
---

# Enable Header Row Pattern property

Allows you to enable or disable a UI pattern called *Header Row* (a.k.a. [Hero Image](https://en.wikipedia.org/wiki/Hero_image)).

## [Values](#Values)

|  |  |
| --- | --- |
| **False** | Default value. The pattern is disabled by default. This means that when you scroll down the screen, the Application Bar and Status Bar will always be visible |
| **True** | The pattern is enabled, unlocking [Header Row Application Bars Class property](https://wiki.genexus.com/commwiki/wiki?37186) which must be set with an Application Bar theme-class. This Theme-Class is used to change the appearance of the application bar when using this pattern. |

## [Description](#Description)

This property is available for the MainTable in [SD Panels](https://wiki.genexus.com/commwiki/wiki?24829) and [WWSD](https://wiki.genexus.com/commwiki/wiki?15974), under Form group.

Header Row pattern working as a visual introduction in the whole top of the screen. Initially, the first row of the layout reaches the space reserved for Application and Status Bars (in conjunction, System Bars) until the end-user scrolls up the content, in which case applies a smooth transition between the theme-class set on [Class property](https://wiki.genexus.com/commwiki/wiki?8741) and those set on [Header Row Application Bars Class property](https://wiki.genexus.com/commwiki/wiki?37186). This first row is considered as a banner, which could be an image, a video, or whatever you want, and [Header Row Application Bars Class property](https://wiki.genexus.com/commwiki/wiki?37186) usually has every color with transparent value, giving the illusion that the banner appears and disappears when the end-user scrolls on the screen. Applications like Google Play uses it to shows a short demo video of the application when you see the description of it.

Technically, the MainTable covers all the device screen, including the space occupied by the application and status bar. Those two elements stay in a particular state (e.g. transparent, giving the illusion that is invisible; but can be other) until that the first row disappears from the upper reaches of the screen as a consequence of scrolling up by the end-user.

## [Run-time/Design-time](#Run-time%2FDesign-time)

This property applies only at design-time.

## [Sample](#Sample)

Suppose you want to apply this UI/UX feature in the [List section](https://wiki.genexus.com/commwiki/wiki?15984)  of WorkWithDevicesSpeaker object for displaying a banner above the speaker list.

For achieving that aim, you will have to design the following layout that includes a video and an image as a header (both embedded in a table in the first row).

`[imagen omitida: wiki id 30420]`

Make sure that the Grid does not contain any Filters (see limitations in the Notes section below) and has Auto Grow property set to True. This last action will enlarge the speaker list, make it scrollable in the entry for the end-user.

`[imagen omitida: wiki id 30421]`

After that, open the Theme object associated with the current layout (in this case, CarmineSD), select the ApplicationBars node, and note that there is a sub-class called ApplicationBarsHeaderRow. Set its properties as it is shown below in order to display the header until the end-user scrolls up the content (in which case, the system bars will appear).

`[imagen omitida: wiki id 30422]`

Finally, set the *Enable Header Row Pattern property* to True at Main Table level and make sure that *Header Row Application Bars Class property* is assigned to the ApplicationBarsHeaderRow value that was previously created.

 `[imagen omitida: wiki id 30423]`

The effect obtained in the application is shown below.

|  |  |
| --- | --- |
| **Android** | **iOS** |
|  |  |

## [Notes](#Notes)

* For the pattern to take effect, it must be used in a scrollable screen (for example, with a grid). In this case, the grid must have the Autogrow property set.
* The first row of the Main Table must have a height greater than the [Application Bar](https://wiki.genexus.com/commwiki/wiki?19486) height to obtain the desired effect. Also, the Autogrow property must be set to True.
* In order to achieve a transparent effect, the *ApplicationBarsHeaderRow* class must satisfy two conditions:  
  1) Every color must be transparent (Background color, Status Bar color, and Forecolor)  
  2) Elevation property (on Android) must be 0 - not empty.
* There are some limitations to the [Autogrow property](https://wiki.genexus.com/commwiki/wiki?22697) that must be taken into account to achieve the desired effect.
* When you use [Navigation Style](https://wiki.genexus.com/commwiki/wiki?16229) in Slide mode, this property indicates if the Slide menu uses the space of the status bar (true) or not (false).
* As of GeneXus 15 Upgrade 8 [Layout Behavior properties group](https://wiki.genexus.com/commwiki/wiki?37135) has been added in order to design apps for iPhone X. Consider using them when HERO pattern is applied because the default values for expanding the controls could not be appropriated in landscape mode.

## [Scope](#Scope)

**Controls:** [Main Table control](https://wiki.genexus.com/commwiki/wiki?6001)  
**Platforms:**Native Mobile (Android,IOS, Angular)

## [Availability](#Availability)

This property is available as of [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,)

## [See also](#See+also)

* [Layout Behavior properties group](https://wiki.genexus.com/commwiki/wiki?37135)


|  |
| --- |
| **Backlinks** |
| [Expand Bounds Limit property](https://wiki.genexus.com/commwiki/wiki?37137) | [Header Row Application Bars Class property](https://wiki.genexus.com/commwiki/wiki?37186) |
| [HowTo: Adding Material Design to Android applications](https://wiki.genexus.com/commwiki/wiki?31004) | [Layout Behavior properties group](https://wiki.genexus.com/commwiki/wiki?37135) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
