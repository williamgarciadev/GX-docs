---
title: "Layout Behavior properties group"
source_id: 37135
source_url: https://wiki.genexus.com/commwiki/wiki?37135
genexus_version: "18"
---

# Layout Behavior properties group

This set of properties allows the developer to expand the controls defined in the layout.

## [Properties](#Properties)

|  |  |
| --- | --- |
| [Expand Bounds property](https://wiki.genexus.com/commwiki/wiki?37136) | Determines how the control will be expanded. |
| [Expand Bounds Limit property](https://wiki.genexus.com/commwiki/wiki?37137) | Determines the limits where the control will be expanded. |
| [Expand Bounds Directions property](https://wiki.genexus.com/commwiki/wiki?37138) | Determines in which directions the control will be expanded. |

## [Unsafe area concept](#Unsafe+area+concept)

iPhone X has introduced three main features compared with the previous version of this device.

* The *notch* on the middle top of the screen where the camera and other hardware resides.
* The *home indicator*, a thin bar on the middle bottom of the screen that replaces the home button.
* Rounded corners on the screen.

Consequently, the **unsafe area** concept has been enhanced compared to previous versions of the iPhone and has become more significant when the developer designs an application. In the following examples, the unsafe area will be displayed in green color.

Before the iPhone X, there only existed one unsafe area defined by the status bar (when the application bar is invisible) as shown below. In GeneXus, the only mechanism for expanding the displayed content beyond the status bar was setting [Enable Header Row Pattern property](https://wiki.genexus.com/commwiki/wiki?29843).

|  |  |
| --- | --- |
| **Portrait** | **Landscape** |
|  |  |

After the iPhone X, the addition of the notch and the replacement of the home button by the home indicator has introduced new unsafe areas that developers must consider when developing their apps. More specifically, there is a new unsafe area at the bottom of the screen (where the *home indicator* is displayed), and two other unsafe areas on the sides of the screen when the device is in landscape mode (where the *notch* is located and rounded corners became significant). In such conditions, enabling the Header Row pattern is not enough.

|  |  |
| --- | --- |
| **Portrait** | **Landscape** |
|  |  |

To avoid the above problem, GeneXus has introduced this set of properties, enabling the developer to safely expand the content beyond the unsafe areas, significantly improving the UX provided in the generated applications. In the following example, the content is displayed by using a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) with Control Type = SD Maps and we hide the application bar (Layout Behavior properties have default values).

|  |  |
| --- | --- |
| **Portrait** | **Landscape** |
|  |  |

## [Notes](#Notes)

* Default values for this set of properties introduce a **breaking change** (for the better) on the application's look. Up to GeneXus 15 Upgrade 7, the content is not expanded (like None value behavior) leaving margins on unsafe areas, which is an undesired layout design for the iPhone X. As of Upgrade 8, the content will be expanded by default to fill the entire screen area.

## [Availability](#Availability)

This properties group is available as of [GeneXus 15 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?36778,,).

## [Scope](#Scope)

**Controls:** [Grid control](https://wiki.genexus.com/commwiki/wiki?24817), [Tab control](https://wiki.genexus.com/commwiki/wiki?29986), [Canvas control](https://wiki.genexus.com/commwiki/wiki?22452), [Table control](https://wiki.genexus.com/commwiki/wiki?6001)  
**Platforms:** Smart Devices(IOS)

## [See also](#See+also)

* [Enable Header Row Pattern property](https://wiki.genexus.com/commwiki/wiki?29843)


|  |
| --- |
| **Backlinks** |
| [Enable Header Row Pattern property](https://wiki.genexus.com/commwiki/wiki?29843) |

---
