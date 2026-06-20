---
title: "HowTo: Use a Matrix Grid Control"
source_id: 25139
source_url: https://wiki.genexus.com/commwiki/wiki?25139
genexus_version: "18"
---

# HowTo: Use a Matrix Grid Control

Sometimes, you want to display information in two-dimensions on a single screen. For example: to list a Dentist's patients per hour/day, to show the programming of a television channel, among others. But the creation of this type of interfaces, with horizontal and vertical scroll, is too complicated, so you often find this idea implemented by a series of completely unnecessary steps. You can resolve this problem using the Matrix Grid Control to display data in two-dimensional grids.

`[imagen omitida: wiki id 25290]`

### [How is it used?](#How+is+it+used%3F)

The Matrix Grid Control is a type of [Grid control](https://wiki.genexus.com/commwiki/wiki?24817). To use it, you just need to insert a Grid on your screen and set the [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) to Matrix Grid.

The Matrix Grid Control defines a set of custom properties to determine the data to be shown and to control its appearance. Three important things have to be established: the X-axis, the Y-axis, and the data. Each data has its X and Y position attached.

Also note that as it is a Grid, some behavior is inherited from the Grid control, like:

* The data items in the Matrix Grid are drawn by taking into account the item layout defined in the Grid (in the Layout editor in GeneXus).
* The Grid's Default Action is also available and works as expected, that is, when tapping on an item in the Matrix Grid, the Default Action will be executed for that item.

### [Components](#Components)

This type of Grids is composed of three elements:

* The X-Axis
* The Y-Axis
* The Data, each data element indicates it's X and Y position.

For each of these three items is important to determine:

* Size
* Aspect
* Data

And this has to be done using the following properties.

### [General Properties](#General+Properties)

This set of properties determines the size of each data grid cell.

| Property | Description |
| --- | --- |
| [Selection Type](https://wiki.genexus.com/commwiki/wiki?24120) | Defines the behavior of the Grid's rows when they are selected. |
| [Data Cell Height](https://wiki.genexus.com/commwiki/wiki?40389) | Sets the height of the Matrix Grid data cells. |
| [Selected Row Height](https://wiki.genexus.com/commwiki/wiki?40395) | Sets the "selected" row height of a Matrix Grid. |
| [Data Cell Width](https://wiki.genexus.com/commwiki/wiki?40396) | Sets the width of the Matrix Grid data cells. |

`[imagen omitida: wiki id 46450]`

### [Section Axes Properties](#Section+Axes+Properties)

**X-Axis** — refers to the values on the horizontal axis.

`[imagen omitida: wiki id 27483]`

| Property | Description |
| --- | --- |
| X-Axis Width | The width of the X-axis row. |
| [X-Axis SDT](https://wiki.genexus.com/commwiki/wiki?42159) | The SDT which contains the values for the X-axis. |
| [X-Axis Value Field Specifier](https://wiki.genexus.com/commwiki/wiki?42160) | The SDT's item with the value to use as an identifier. |
| [X-Axis Title Field Specifier](https://wiki.genexus.com/commwiki/wiki?42161) | The SDT's item with the title to use. |
| [X-Axis Description Field Specifier](https://wiki.genexus.com/commwiki/wiki?42162) | The SDT's item with the description to use. |

### [Samples](#Samples)

**Example 1**

Loading X-Axis, hours a day every 30 minutes. This is the load of the SDT &TimeAxis. &TimeAxis is assigned to the X-Axis SDT property.

```
// Load Time Axis
&TimeAxis = new()
&vTime = YMDHMStoT(&DayReference.Year(),&DayReference.Month(),&DayReference.Day(),0,0,0)
for &i=1 to 60 * 24  step 30 // 24 hours to minutes
  &TimeAxisItem = new ()
  &TimeAxisItem.Id = &vTime.Hour() * 60 + &vTime.Minute()
  // 24 to 12 hs conversion
  &ampm = iif(&vTime.Hour() >= 12, "pm", "am")
  &vTimeHour = iif(&vTime.Hour() >= 12, &vTime.Hour() - 12 , &vTime.Hour())
  &vTimeHour = iif(&vTimeHour = 0, 12, &vTimeHour)
 
  &TimeAxisItem.Description = format("%1:%2 %3", &vTimeHour, trim(iif(&vTime.Minute()=0,"00",&vTime.Minute().ToString())), &ampm)
 
  &TimeAxis.Add(&TimeAxisItem)
  &vTime = &vTime.AddMinutes(30)
endfor
```

Using a [Data Provider](https://wiki.genexus.com/commwiki/wiki?4417):

```
TimeAxis
{
   &vTime = YMDHMStoT(&DayReference.Year(),&DayReference.Month(),&DayReference.Day(),0,0,0)
   TimeAxisItem input &i = 1 to 60 * 24  step 30 // 24 hours to minutes
   {
      Id = &vTime.Hour() * 60 + &vTime.Minute()
      // 24 to 12 hs conversion
      &ampm      = iif(&vTime.Hour() >= 12, "pm", "am")
      &vTimeHour = iif(&vTime.Hour() >= 12, &vTime.Hour() - 12 , &vTime.Hour())
      &vTimeHour = iif(&vTimeHour = 0, 12, &vTimeHour)
 
      Description = format("%1:%2 %3", &vTimeHour, trim(iif(&vTime.Minute()=0,"00",&vTime.Minute().ToString())), &ampm)
   }
   &vTime = &vTime.AddMinutes(30)
}
```

**Y-Axis**— refers to the values on the vertical axis.

`[imagen omitida: wiki id 27484]`

| Property | Description |
| --- | --- |
| Y-Axis Height | The height of the Y-axis column. |
| [Y-Axis SDT](https://wiki.genexus.com/commwiki/wiki?42163) | The SDT which contains the values for the Y-axis. |
| [Y-Axis Value Field Specifier](https://wiki.genexus.com/commwiki/wiki?42164) | The SDT's item with the value to use as an identifier. |
| [Y-Axis Title Field Specifier](https://wiki.genexus.com/commwiki/wiki?42165) | The SDT's item with the title to use. |
| [Y-Axis Description Field Specifier](https://wiki.genexus.com/commwiki/wiki?42166) | The SDT's item with the description to use. |
| [Y-Axis Selection Flag Field Specifier](https://wiki.genexus.com/commwiki/wiki?42167) | The SDT's item that indicates if the row is selected or not. |

**Example 2**

Loading Y-Axis, days of the week -2 weeks. The row corresponding with the current data is marked as selected and the "Today" subtitle is added.

```
// Load Day Axis
&DayAxis = new()
&FirstDayOfWeek = today()
&varFirstDayOfWeek =ymdhmstot(&FirstDayOfWeek.Year(),&FirstDayOfWeek.Month(),&FirstDayOfWeek.Day(),0,0,0)
&varFirstDayOfWeekD =ymdtod(&FirstDayOfWeek.Year(),&FirstDayOfWeek.Month(),&FirstDayOfWeek.Day())
for &i = 0 to 13// 7 days of week based on reference day
  &DayAxisItem = new()
  &DayAxisItem.Id = &FirstDayOfWeek.AddDays(&i)
  &DayAxisItem.Title = upper(&DayAxisItem.Id.DayOfWeekName())
  &DayAxisItem.Title += format("%1%2 DE %3", newline(), &DayAxisItem.Id.Day(), upper(&DayAxisItem.Id.MonthName()))
  &DayAxisItem.Selected = iif(&DayAxisItem.Id = Today(), TRUE, FALSE)
  if (&DayAxisItem.Selected)
   &DayAxisItem.Subtitle = "Today"
  endif
  &DayAxis.Add(&DayAxisItem)
endfor
```

Using a [Data Provider](https://wiki.genexus.com/commwiki/wiki?4417):

```
DayAxis
{
   &FirstDayOfWeek     = today()
   &varFirstDayOfWeek  = ymdhmstot(&FirstDayOfWeek.Year(),&FirstDayOfWeek.Month(),&FirstDayOfWeek.Day(),0,0,0)
   &varFirstDayOfWeekD = ymdtod(&FirstDayOfWeek.Year(),&FirstDayOfWeek.Month(),&FirstDayOfWeek.Day())
   DayAxisItem input &i = 0 to 13// 7 days of week based on reference day
   {
      Id        = &FirstDayOfWeek.AddDays(&i)
      &Title    = upper(&DayAxisItem.Id.DayOfWeekName())
      &Title    = &Title + format("%1%2 DE %3", newline(), &DayAxisItem.Id.Day(), upper(&DayAxisItem.Id.MonthName()))
      Title     = &Title
      &Selected = iif(&DayAxisItem.Id = Today(), TRUE, FALSE)
      Selected  = &Selected
      Subtitle  = iif(&Selected, "Today", "")
   }
}
```

**X-Axis Data**— refers to the position of the data on the horizontal axis.

`[imagen omitida: wiki id 27485]`

| Property | Description |
| --- | --- |
| [X-Data From Attribute](https://wiki.genexus.com/commwiki/wiki?42168) | Attribute or variable — with the value of one identifier defined on the *X-Axis Value Field Specifier —* which indicates the starting position. |
| [X-Data From Field Specifier](https://wiki.genexus.com/commwiki/wiki?42169) | Sets the member name of the SDT (with the value of one identifier defined on the X-Axis Value Field Specifier) which indicates the starting position. |
| [X-Data To Attribute](https://wiki.genexus.com/commwiki/wiki?42170) | Attribute or variable —with the value of the identifier defined on the *X-Axis Value Field Specifier* — which indicates the final position. |
| [X-Data To Field Specifier](https://wiki.genexus.com/commwiki/wiki?42171) | Sets the member name of the SDT (with the value of one identifier defined on the X-Axis Value Field Specifier) which indicates the final position. |

**Y-Axis Data**— refers to the position of the data on the vertical axis.

`[imagen omitida: wiki id 27486]`

| Property | Description |
| --- | --- |
| [Y-Data From Attribute](https://wiki.genexus.com/commwiki/wiki?42172) | Attribute or variable — with the value of the identifier defined on the Y*-Axis Value Field Specifier*  — which indicates the starting position. |
| [Y-Data From Field Specifier](https://wiki.genexus.com/commwiki/wiki?42173) | Sets the member name of the SDT (with the value of the identifier defined on the Y-Axis Value Field Specifier) which indicates the starting position. |
| [Y-Data To Attribute](https://wiki.genexus.com/commwiki/wiki?42174) | Attribute or variable — with the value of the identifier defined on the Y*-Axis Value Field Specifier*  — which indicates the final position. |

**Example 3**

In the load event of the grid, load values for each cell specifying the X, Y where the data should be placed:

Value X=  &TimeFromNumeric (Start Time) y &TimeToNumeric (End Time)  
Value Y= CartaProgramacionFecha

```
Event Grid1.Load
  &timeFromNumeric = val(CartaProg_Hora_Inicio.Substring(1,2)) * 60 + val(CartaProg_Hora_Inicio.Substring(4,2))
  &timeToNumeric = val(CartaProg_Hora_Fin.Substring(1,2)) * 60 + val(CartaProg_Hora_Fin.Substring(4,2))
EndEvent
```

**Example 4**

Here is another load sample without base table:

```
Event Grid1.Load
  &XAxisfrom = <XAxis position to start showing data>
  &XAxisto = <XAxis position where data finishes>
  &YAxisfrom = <YAxis position to start showing data>
  &YAxisto = <YAxis position where data finishes>
  &DataToShow = <Value showed in grid position (x,y)>
  load
  &XAxisfrom = <XAxis position to start showing data>
  &XAxis = <XAxis position where data finishes> 
  &YAxisfrom =<YAxis position to start showing data>
  &YAxis = <YAxis position where data finishes> 
  &DataToShow = <Value2 showed in grid position (x2,y2)>
  load
Endevent
```

This is an example of loading two values. You can load as many values as you need.

### [Appearance](#Appearance)

See the [Matrix theme-class for Smart Devices](https://wiki.genexus.com/commwiki/wiki?25692) for more information.


|  |
| --- |
| **Backlinks** |
| [Cell Table Class property](https://wiki.genexus.com/commwiki/wiki?40354) | [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) | [Category:Control Types](https://wiki.genexus.com/commwiki/wiki?20402) |
| [Data Cell Height property](https://wiki.genexus.com/commwiki/wiki?40389) | [Data Cell Width property](https://wiki.genexus.com/commwiki/wiki?40396) | [Even Row Table Class property](https://wiki.genexus.com/commwiki/wiki?40358) |
| [Horizontal Rules Class property](https://wiki.genexus.com/commwiki/wiki?40362) | [Matrix theme-class for Smart Devices](https://wiki.genexus.com/commwiki/wiki?25692) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Odd Row Table Class property](https://wiki.genexus.com/commwiki/wiki?40359) |
| [Selected Cell Table Class property](https://wiki.genexus.com/commwiki/wiki?40355) | [Selected Row Height property](https://wiki.genexus.com/commwiki/wiki?40395) | [Selected Row Table Class property](https://wiki.genexus.com/commwiki/wiki?40360) |
| [Show Horizontal Rules property](https://wiki.genexus.com/commwiki/wiki?40361) | [Show Vertical Rules property](https://wiki.genexus.com/commwiki/wiki?40364) | [Vertical Rules Class property](https://wiki.genexus.com/commwiki/wiki?40363) | [X Axis Label Class property](https://wiki.genexus.com/commwiki/wiki?40353) |
| [X Axis Table Class property](https://wiki.genexus.com/commwiki/wiki?40356) | [X-Axis Description Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42162) | [X-Axis Height property](https://wiki.genexus.com/commwiki/wiki?42107) | [X-Axis SDT property](https://wiki.genexus.com/commwiki/wiki?42159) |
| [X-Axis Title Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42161) | [X-Axis Value Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42160) | [X-Data From Attribute property](https://wiki.genexus.com/commwiki/wiki?42168) | [X-Data From Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42169) |
| [X-Data To Attribute property](https://wiki.genexus.com/commwiki/wiki?42170) | [X-Data To Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42171) | [X-Scale Type property](https://wiki.genexus.com/commwiki/wiki?42146) | [Y Axis Description Label Class property](https://wiki.genexus.com/commwiki/wiki?40352) |
| [Y Axis Table Class property](https://wiki.genexus.com/commwiki/wiki?40357) | [Y-Axis Description Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42166) | [Y-Axis SDT property](https://wiki.genexus.com/commwiki/wiki?42163) |
| [Y-Axis Selection Flag Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42167) | [Y-Axis Title Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42165) | [Y-Axis Value Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42164) | [Y-Axis Width property](https://wiki.genexus.com/commwiki/wiki?42108) |
| [Y-Data From Attribute property](https://wiki.genexus.com/commwiki/wiki?42172) | [Y-Data From Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42173) | [Y-Data To Attribute property](https://wiki.genexus.com/commwiki/wiki?42174) | [Y-Data To Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42175) |
| [Y-Scale Type property](https://wiki.genexus.com/commwiki/wiki?42147) |

---
