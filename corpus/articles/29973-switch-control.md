---
title: "Switch control"
source_id: 29973
source_url: https://wiki.genexus.com/commwiki/wiki?29973
genexus_version: "18"
---

# Switch control

The Switch control is presented as a toggle that allows selecting one of two possible values: on or off.

It is one of the built-in controls and can be selected from the [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550).

It may be used as a replacement for the traditional Check Box control, and it's available for [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s and for [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s.

## [Web Panels](#Web+Panels)

Only the [Abstract Layout](https://wiki.genexus.com/commwiki/wiki?25209) supports this control.

`[imagen omitida: wiki id 29976]`

`[imagen omitida: wiki id 30009]`

## [Panels](#Panels)

`[imagen omitida: wiki id 48705]`

`[imagen omitida: wiki id 29975]`

## [How to change the appearance of the control](#How+to+change+the+appearance+of+the+control)

As of [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?48247,,), both Web and Native Mobile applications support configuring the visual aspect of the control via a Theme Class.

`[imagen omitida: wiki id 30007]`

`[imagen omitida: wiki id 30008]`

## [Properties](#Properties)

|  |  |
| --- | --- |
| **Name** | **Description** |
| *Auto Grow (only for Native Mobile apps)* | [Auto Grow property](https://wiki.genexus.com/commwiki/wiki?20204) |
| *Checked Value* | Indicates the "switch on" value |
| *Unchecked Value* | Indicates the "switch off" value |
| *ON Text (only for Web apps)* | Indicates the text displayed when the ON value is selected |
| *OFF Text (only for Web apps)* | Indicates the text displayed when the OFF value is selected |

## [Events](#Events)

[ControlValueChanged event](https://wiki.genexus.com/commwiki/wiki?22676)

## [Compatibility notes](#Compatibility+notes)

The ValueChanged event for the Switch control in iOS has been deprecated. The [ControlValueChanged event](https://wiki.genexus.com/commwiki/wiki?22676) must be used instead.


|  |
| --- |
| **Backlinks** |
| [Abstract Layout](https://wiki.genexus.com/commwiki/wiki?25209) | [Checked Value property](https://wiki.genexus.com/commwiki/wiki?8734) | [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) |
| [Control Type property (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?57964) | [Off Text property](https://wiki.genexus.com/commwiki/wiki?42232) |
| [On Text property](https://wiki.genexus.com/commwiki/wiki?42231) | [Unchecked Value property](https://wiki.genexus.com/commwiki/wiki?8737) |

---
