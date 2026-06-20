---
title: "Label Position property"
source_id: 34141
source_url: https://wiki.genexus.com/commwiki/wiki?34141
genexus_version: "18"
---

# Label Position property

The Label Position property is available for every attribute and variable defined in a form and it is used by the developer to indicate where the label will be positioned.  
Its possible values are displayed in the [Abstract Layout](https://wiki.genexus.com/commwiki/wiki?25209) as WYSIWYG.

## [Values](#Values)

|  |  |  |  |
| --- | --- | --- | --- |
| **Value** | **Description** | **Run-time effect** | |
| **Platform Default** | Default value in all GeneXus editions but [GeneXus for SAP Systems](https://wiki.genexus.com/commwiki/wiki?33616)  The position of the label adopts the default position on each platform (top for Android, left for iOS). | Android |  |
| iOS |  |
| **None** | The label will not be displayed.  *Note*: The value displayed is the [Invite Message property](https://wiki.genexus.com/commwiki/wiki?19697), but no label is displayed. | Android |  |
| iOS |  |
| **Left** | The label will be displayed on the left side of the attribute/variable content. | Android |  |
| iOS |  |
| **Right** | The label will be displayed on the right side of the attribute/variable content. | Android |  |
| iOS |  |
| **Top** | The label will be displayed on the top side of the attribute/variable content. | Android |  |
| iOS |  |
| **Bottom** | The label will be displayed on the bottom side of the attribute/variable content. | Android |  |
| iOS |  |
| **Float** | Default value in [GeneXus for SAP Systems](https://wiki.genexus.com/commwiki/wiki?33616).  The label will be displayed once the end user starts writing as if it were floating from the bottom to the top of the attribute/variable content. | Android |  |
| iOS |  |

## [Note](#Note)

* The Float value is available as of [GeneXus 15 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?33798,,).  
  Some considerations:
  + It only applies for Character or Numeric based attributes/variables. Another data types (such as Image, Audio, etc) will behave as its value would have been Top.
  + On Android, the value of the invite message and the label must be the same; otherwise, the label adopts the value of the invite message.
* As of [GeneXus 15 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?33798,,) the default value of this property can be changed at the [Pattern settings](https://wiki.genexus.com/commwiki/wiki?6546) of the Work With for Smart Devices Pattern.
* For web environments, so far only the options "None" and "Left" are supported.

## [Scope](#Scope+)

|  |  |
| --- | --- |
| **Objects** | [Panel for Smart Devices](https://wiki.genexus.com/commwiki/wiki?24829), [Work With for Smart Devices](https://wiki.genexus.com/commwiki/wiki?15974) |
| **Data type** | Numeric, Character, Image, Audio, Video |
| **SD Generators** | iOS, Android |
| **Languages** | .NET, Java |


|  |
| --- |
| **Backlinks** |
| [Invite Message property](https://wiki.genexus.com/commwiki/wiki?19697) | [InviteMessage property (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53870) |
| [Label Width property](https://wiki.genexus.com/commwiki/wiki?47219) |

---
