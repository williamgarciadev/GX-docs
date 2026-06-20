---
title: "GXChart Control"
source_id: 4890
source_url: https://wiki.genexus.com/commwiki/wiki?4890
genexus_version: "18"
---

# GXChart Control

**Deprecated.** Replaced by[QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075).

**Control Description**

The GXChart control enables you to display incredible dinamically-generated charts on your website. The GXChart control is based on GXchart.com, which is an online service that instantly creates any chart you want to visualize according to the data provided. More information can be found at [www.gxchart.com](http://www.gxchart.com).

|  |  |
| --- | --- |
|  |  |

**Using the control**

In order to start using the control, you need to drag and drop the Chart control into a web panel (or transaction). You will then see the chart in your web form and its properties will be shown in the Properties window (which can be activated from the View menu). In addition, when you drop the chart control, an SDT is consolidated: the GXChart.

The idea here is that you will give the chart control a GXChart SDT-based variable containing the x,y values that have to be displayed in the chart. The GXChart SDT contains 2 fields:

* Categories: these are the X values to be displayed in the X axis.
* Series (collection):
  + Name: the name of the series
  + Values: these are the Y values. Each of the values in a series belongs to a category. That is to say, the series should have as many values as there are categories (X=category, Y= series value)

As you may have realized, a Series in a GXChart actually contains a collection of series. This allows you to chart "more than one value" belonging to a category. Consequently, it is possible to create a chart representing, for example, the incomes and expenses for a given period.

Example:

```
&gxChart.Categories.Add("May")
&gxChart.Categories.Add("June")
&gxChart.Categories.Add("July")
&gxChart.Categories.Add("August")
&serie.Name = "Incomes"
&serie.Values.Add(50)
&serie.Values.Add(55)
&serie.Values.Add(60)
&serie.Values.Add(65)
&gxChart.Series.Add(&serie)
&serie =new()
&serie.Name = "Outcomes"
&serie.Values.Add(20)
&serie.Values.Add(25)
&serie.Values.Add(30)
&serie.Values.Add(35)
&gxChart.Series.Add(&serie)
//&gxchart is defined as GXChart //&serie is defined as Gxchart.serie
```

The example shown above will create a graph as follows:

|  |
| --- |
|  |

**Control Properties**

|  |  |
| --- | --- |
| **Property** | **Description** |
| Title | Main chart title |
| X Axis title | Title to show on X axis |
| Y Axis title | Title to show on Y axis |
| Width | Image width in pixels |
| Height | Image height in pixels |
| BG Color 1 | Gradient fill background color for the top left corner |
| BG Color 2 | Gradient fill background color for the bottom right corner |
| Chart BG Color 1 | Gradient fill background color of the chart pane (only for X-Y chart types) in the top left corner |
| Chart BG Color 2 | Gradient fill background color of the chart pane (only for X-Y chart types) in the bottom right corner |
| Draw Shadow | Specify shadows' displayed status |
| Draw Border | Specify border style |
| Show Values | Specify whether each value should be displayed |
| Opacity (Alpha) | Alpha value for chart items |
| Legend Position | Legend position |
| Hatch | Specify the Hatch Fill for black and white charts |
| Codec | Specify the image type |
| Title Font Size | Specify the title font size |
| Category Font Size | Specify the legends font size (Categories, Values, etc.) |
| Category Order | Specify the category order |
| Colors | Colors to be used in the different Data Series |
| Scale | Specify first value of the scale |

More information [GXchart 3.0](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1801,,)


|  |
| --- |
| **Backlinks** |
| [Category:Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) | [User Control Editor](https://wiki.genexus.com/commwiki/wiki?26976) |
|

---
