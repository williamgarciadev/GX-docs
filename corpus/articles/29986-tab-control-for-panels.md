---
title: "Tab control for Panels"
source_id: 29986
source_url: https://wiki.genexus.com/commwiki/wiki?29986
genexus_version: "18"
---

# Tab control for Panels

The tab control is used to display a set of controls grouped in different tabs, in an analogous way to [Tab control for Web Panels](https://wiki.genexus.com/commwiki/wiki?25623).

## [Properties](#Properties)

### [Design time](#Design+time)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | | **Value** | **Description** |
| **Item Control Name** | | *String* | Control name of each tab page. |
| **Control Name** | | *String* | Name of tab control. |
| ***Control Info*** | | | |
|  | **Auto Grow** | *True* | Adjusts the size of a control whose content exceeds the size of the container. |
| *False* (default) |
| ***TabControl Appearance*** | | | |
|  | **Tab Control Class** | [*Theme Class*](https://wiki.genexus.com/commwiki/wiki?16595) | Theme class associated with the Tab Control. |
|  | **Tab Control Visible** | *True*(default) | Hides or shows the Tab Control. |
| *False* |
|  | **Invisible Mode** | *Keep Space*(default) | Specifies whether the control keeps or collapses the space when it is not visible. |
| *Collapse Space* |
|  | **Enable** | *True*(default) | Determines whether the control is enabled. |
| *False* |
| ***Tabs Behavior*** | | | |
|  | **[Tabs Distribution](https://wiki.genexus.com/commwiki/wiki?40234)** |  |  |
|  |
|  |
|  | **Interactive Navigation** | *Platform Default*(default) | Enables the option to move between tabs by tapping (false) or scrolling smoothly (true).  According to the standards, *Platform Default* means *true* for Android and *false* for iOS. |
| *True* |
| *False* |
|  | **More Button Selected image** | [*Image*](https://wiki.genexus.com/commwiki/wiki?23387) | Image to show when the "more" button is selected. |
|  | **More Button Unselected image** | [*Image*](https://wiki.genexus.com/commwiki/wiki?23387) | Image to show when the "more" button is unselected. |
| ***TabPage Appearance*** | | | |
|  | **Selected Tab Page Class** | [*Theme Class*](https://wiki.genexus.com/commwiki/wiki?16595) | Theme class associated with the Tab Page when selected. |
|  | **Unselected Tab Page Class** | [*Theme Class*](https://wiki.genexus.com/commwiki/wiki?16595) | Theme class associated with the Tab Page when unselected. |
|  | **Caption** | *String* | Text to display on the tab. See also [HowTo: Format plain text programmatically](https://wiki.genexus.com/commwiki/wiki?31657). |
|  | **Tab Page Visible** | *True*(default) | Makes the tab page visible. It can be changed at runtime. |
| *False* |
|  | **Tab Page Enabled** | *True*(default) | Determines whether the tab page is enabled. |
| *False* |
|  | **Image** | [*Image*](https://wiki.genexus.com/commwiki/wiki?23387) | Image associated with the Tab Page when selected. |
|  | **Unselected Image** | [*Image*](https://wiki.genexus.com/commwiki/wiki?23387) | Image associated with the Tab Page when unselected. |
|  | [Image Position](https://wiki.genexus.com/commwiki/wiki?40705) |  |  |

### [Runtime](#Runtime)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | | **Value** | **Description** |
| **ActivePage** | | *Numeric* | Active page index (first tab index is 1) |

## [Events](#Events)

**ActivePageChanged**Triggered when selecting any new tab page.

## [How to use](#How+to+use)

Refer to [HowTo: Using Tab Control in Panels](https://wiki.genexus.com/commwiki/wiki?16800).

## [See also](#See+also)

[Tab Page Control for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?25638)  
[Android Material Design Guidelines for Tabs](https://material.io/guidelines/components/tabs.html)  
[iOS Human Interface Guidelines for Tabs](https://developer.apple.com/ios/human-interface-guidelines/ui-bars/tab-bars/)


|  |
| --- |
| **Backlinks** |
| [Accessible Name Control property](https://wiki.genexus.com/commwiki/wiki?55456) | [Expand Bounds Directions property](https://wiki.genexus.com/commwiki/wiki?37138) | [Expand Bounds Limit property](https://wiki.genexus.com/commwiki/wiki?37137) |
| [Expand Bounds property](https://wiki.genexus.com/commwiki/wiki?37136) | [GeneXus Markup Language (GXML)](https://wiki.genexus.com/commwiki/wiki?46876) | [Image Position property](https://wiki.genexus.com/commwiki/wiki?40705) |
| [Layout Behavior properties group](https://wiki.genexus.com/commwiki/wiki?37135) | [Tabs Distribution property](https://wiki.genexus.com/commwiki/wiki?40234) |

---
