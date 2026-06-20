---
title: "Column Chart Control"
source_id: 10450
source_url: https://wiki.genexus.com/commwiki/wiki?10450
genexus_version: "18"
---

# Column Chart Control

#### [Introduction](#Introduction+)

A column chart displays a series as a set of vertical bars that are grouped by category. Column charts are useful for showing data changes over a period of time or for illustrating comparisions among items. Column Chart Control is an interactive chart, try clicking on a column or on the legend entries.

#### [Examples](#Examples+)

The user control is really simple, you just need to set one property in order to get the control working. The Data property.

#### [Show a simple column chart to illustrate a comparision between Sales and Expenses for certain years](#Show+a+simple+column+chart+to+illustrate+a+comparision+between+Sales+and+Expenses+for+certain+years+)

* Drag and drop Google Charts Control.
* Set Column Chart to property named Type.
* Assign to the Data property a variable based on GoogleChartData data type (this SDT is automatically imported when dropping the control to a web form).
* Load the information that will be shown by the chart using a variable based on GoogleChartData.

```
//Sample code for GoogleCharts  
Sub 'LoadGoogleChartData'  
    &GoogleChartData.Categories.Add("2005")  
    &GoogleChartData.Categories.Add("2006")  
    &GoogleChartData.Categories.Add("2007")  
    &GoogleChartData.Categories.Add("2008")  
      
    &GoogleChartSeries = new()  
    &GoogleChartSeries.Name = "Sales"  
    &GoogleChartSeries.Values.Add(3045)  
    &GoogleChartSeries.Values.Add(4246)  
    &GoogleChartSeries.Values.Add(6537)  
    &GoogleChartSeries.Values.Add(2537)  
    &GoogleChartData.Series.Add(&GoogleChartSeries)  
      
    &GoogleChartSeries = new()  
    &GoogleChartSeries.Name = "Expenses"  
    &GoogleChartSeries.Values.Add(2045)  
    &GoogleChartSeries.Values.Add(3246)  
    &GoogleChartSeries.Values.Add(4537)  
    &GoogleChartSeries.Values.Add(5537)  
    &GoogleChartData.Series.Add(&GoogleChartSeries)  
EndSub
```

`[imagen omitida: wiki id 10463]`

#### [Adding more series to be displayed by the control](#Adding+more+series+to+be+displayed+by+the+control+)

* Add a new series and its corresponding values to GeneXusColumnData variable (the variable assigned to control's ChartData property.

```
&GoogleChartSeries = new()  
&GoogleChartSeries.Name = "Others"  
&GoogleChartSeries.Values.Add(1045)  
&GoogleChartSeries.Values.Add(4244)  
&GoogleChartSeries.Values.Add(2537)  
&GoogleChartSeries.Values.Add(1537)  
&GoogleChartData.Series.Add(&GoogleChartSeries)
```

`[imagen omitida: wiki id 10464]`

#### [Handling events](#Handling+events+)

As we mentioned before, Column Chart Control is an interactive chart. That is, when clicking on series legend the corresponding columns will be highlighted. In addition, when clicking on a column, a tooltip will be displayed and also a GeneXus event wil be fired.

```
//GoogleChartsControl event handler  
Event GoogleCharts1.Select  
    msg(!"Selected Category Name: " + &GoogleChartSelectedData.CategoryName)  
    msg(!"Selected Series Name: " + &GoogleChartSelectedData.SeriesName)  
    msg(!"Selected Series Value: " + str(&GoogleChartSelectedData.SeriesValue))  
EndEvent
```

Note: &GoogleChartSelectedData is based on GoogleChartSelectedData SDT (this SDT is also automatically imported when dropping the control to a web form.

`[imagen omitida: wiki id 10466]`

#### [Implementation Details](#Implementation+Details)

Column Chart Control is based on the [Google Column Chart Control](http://code.google.com/apis/visualization/documentation/gallery/columnchart.html).


|  |
| --- |
| **Backlinks** |
| [Bar Chart](https://wiki.genexus.com/commwiki/wiki?10454) | [Google Charts](https://wiki.genexus.com/commwiki/wiki?10449) | [GXGoogle Visualization Library](https://wiki.genexus.com/commwiki/wiki?10447) |
| [Pie Chart](https://wiki.genexus.com/commwiki/wiki?10456) | [Scatter Chart](https://wiki.genexus.com/commwiki/wiki?10457) |

---
