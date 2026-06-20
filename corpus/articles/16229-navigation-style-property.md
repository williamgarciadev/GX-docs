---
title: "Navigation Style property"
source_id: 16229
source_url: https://wiki.genexus.com/commwiki/wiki?16229
genexus_version: "18"
---

# Navigation Style property

Defines the Platform navigation style.

### [Values](#Values)

|  |  |
| --- | --- |
| **Default** | Split or Flip are automatically selected depending on the screen size. Usually Flip is for phones and Split is for tablets. This is the default value. |
| **Flip** | Detail information is displayed on a separate screen once an item is selected in List. |
| **Split** | List and Detail information is displayed on the same screen. This value is ignored when running on phones. |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Level:** Platforms node > Platform

### [Description](#Description)

Depending on the features of the target device platform (OS, Size, OS version) you may want to vary how the user interacts with and, more specifically, how the user navigates your app. To achieve this, GeneXus provides the Navigation Style property that allows you to change this behavior at the platform level.

Note that you can only define one navigation style in your application for each possible combination of the above characteristics.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

#### [**Split navigation style**](#Split+navigation+style)

The information on the screen is divided into two sections. As shown in the picture below, there is a panel on the left (in this case, a list of speakers) and the main area is on the right. Note that the orientation is landscape. If the device were in portrait mode, the only area shown would be the main one, and the left one would be hidden until you made it visible by sliding to the right. When running it on a Smartphone device, the Split value will be ignored and the default value will be assumed.

**Android**

`[imagen omitida: wiki id 37219]`

**Apple**

`[imagen omitida: wiki id 37220]`

It works on Tablets and Smartphones. Data is displayed in a single area and may not be divided.

#### [**Flip navigation style**](#Flip+navigation+style)

This style is used when the application displays detailed content on a separate screen after a user selects an item from a list.

|  |  |
| --- | --- |
| **Android** | **Apple** |

#### 

#### [**Slide navigation style**](#Slide+navigation+style)

It works on Tablets and Smartphones. The menu is always available through a button on the upper left corner or by sliding to the right. Read more in [Slide Navigation Style](https://wiki.genexus.com/commwiki/wiki?21285).

|  |  |
| --- | --- |
| **Android** | **Apple** |

#### 

#### [**Cascade navigation style**](#Cascade+navigation+style)

It works on Tablets and Smartphones. As shown in the picture below, the main menu is displayed in the left area, the actual panel is shown on the right, and the last navigated panel is in the middle. When you select an element from the main menu, the cascade navigation panels are reset. The main menu is always accessible.

#### [**Apple**](#Apple)

`[imagen omitida: wiki id 37225]`

### [[Notes](https://wiki.genexus.com/commwiki/wiki?16229)](#Notes)

* **Cascade** value is available for Apple as of [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?20247,,).
* **Slide** value is available for Apple as of [GeneXus X Evolution 2 Upgrade 3](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?22061,,) and for Android as of [GeneXus X Evolution 2 Upgrade 4](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?22626,,).
* **Split**value is available for Android as of [GeneXus 15 Upgrade 4](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?33798,,).

### [See Also](#See+Also)

[Navigation Start Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?25668)  
[Slide Navigation Style](https://wiki.genexus.com/commwiki/wiki?21285)  
[Pattern settings](https://wiki.genexus.com/commwiki/wiki?6546)


|  |
| --- |
| **Backlinks** |
| [Actions external object](https://wiki.genexus.com/commwiki/wiki?31350) | [Audio external object](https://wiki.genexus.com/commwiki/wiki?30041) | [CallOptions Target](https://wiki.genexus.com/commwiki/wiki?25323) |
| [Cascade.Start event](https://wiki.genexus.com/commwiki/wiki?25587) | [Client-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24332) | [ClientStart event](https://wiki.genexus.com/commwiki/wiki?24044) | [Control Type property in Action Group for Panels](https://wiki.genexus.com/commwiki/wiki?25113) |
| [Enable Header Row Pattern property](https://wiki.genexus.com/commwiki/wiki?29843) | [Flip.Start event](https://wiki.genexus.com/commwiki/wiki?25571) | [Flip.Start event (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55467) |
| [Getting Started with tvOS](https://wiki.genexus.com/commwiki/wiki?40787) | [HowTo: Adding Material Design to Android applications](https://wiki.genexus.com/commwiki/wiki?31004) | [Images in Panels](https://wiki.genexus.com/commwiki/wiki?31379) |
| [KB Platforms](https://wiki.genexus.com/commwiki/wiki?24284) | [Live Editing in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?27806) | [Table of contents:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Navigation Start Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?25668) |
| [Platform Overrides property](https://wiki.genexus.com/commwiki/wiki?40583) | [Several ways to show a Menu](https://wiki.genexus.com/commwiki/wiki?16098) | [Slide.Start event](https://wiki.genexus.com/commwiki/wiki?25585) | [Split.Start event](https://wiki.genexus.com/commwiki/wiki?25586) |
| [Tabs.Start event](https://wiki.genexus.com/commwiki/wiki?25596) |

---
