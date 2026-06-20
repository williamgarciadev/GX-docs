---
title: "Include Trend Property"
source_id: 33127
source_url: https://wiki.genexus.com/commwiki/wiki?33127
genexus_version: "18"
---

# Include Trend Property

Include Trend Property it's a [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) and a [Query object](https://wiki.genexus.com/commwiki/wiki?9026) property. It's only available when the [Type property in QueryViewer control](https://wiki.genexus.com/commwiki/wiki?19612) has the [Card](https://wiki.genexus.com/commwiki/wiki?31810) value assigned and allows indicating the trending of the returned data.

### [Values](#Values)

|  |  |
| --- | --- |
| **False** | Tending it's not shown. This is the default value. |
| **True** | Trending it's shown with an arrow at the left of the value |

### [Description](#Description)

If the Query object includes a Date or DateTime attribute, trending can be indicated by setting the Include Trend Property in True:

`[imagen omitida: wiki id 31812]`

This it's calculated with the least squares method by adjusting a straight line to the Data of a defined period and calculating the slope of the curve (positive, negative or zero) and representing it with an arrow to the left of the value:

`[imagen omitida: wiki id 31813]`

### [Availability](#Availability)

This property's available as of [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,).

### [See also](#See+also)

* [Query Card Type](https://wiki.genexus.com/commwiki/wiki?31810)
* [Include Sparkline Property](https://wiki.genexus.com/commwiki/wiki?33131)
* [Include Max and Min Property](https://wiki.genexus.com/commwiki/wiki?33158)
* [Orientation Property](https://wiki.genexus.com/commwiki/wiki?33178)


|  |
| --- |
| **Backlinks** |
| [Dashboard Card Include trend property](https://wiki.genexus.com/commwiki/wiki?40464) | [Include Max and Min Property](https://wiki.genexus.com/commwiki/wiki?33158) | [Include Sparkline Property](https://wiki.genexus.com/commwiki/wiki?33131) |
| [Orientation Property](https://wiki.genexus.com/commwiki/wiki?33178) | [Query Card Type](https://wiki.genexus.com/commwiki/wiki?31810) | [Trend period property](https://wiki.genexus.com/commwiki/wiki?40125) |

---
