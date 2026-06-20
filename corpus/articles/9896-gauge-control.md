---
title: "Gauge Control"
source_id: 9896
source_url: https://wiki.genexus.com/commwiki/wiki?9896
genexus_version: "18"
---

# Gauge Control

#### [Introduction](#Introduction)

There are many scenarios where we need to show a numeric value as a gauge in order to give the final user a better data visualization for the number.

#### [Examples](#Examples)

The user control is really simple, you just need to set one property in order to get the control working. The Data property. The Data property has not a strict schema.

You can assign a simple numeric variable to the property, a collection of numbers, an SDT with at least a number field, a collection of SDTs.

#### [Show a simple numeric value: the speed](#Show+a+simple+numeric+value%3A+the+speed)

* Drag and drop the Gauge Control
* Assign to the Data property a numeric variable or attribute.
* Optionally set the Title property in order to show a label inside the control.

A classical sample can be show the Speed.

`[imagen omitida: wiki id 9897]`

#### [Show a serie of numeric values: speeds](#Show+a+serie+of+numeric+values%3A+speeds)

* Drag and drop the Gauge Control
* Assign to the Data property a numeric collection variable : &speed
* Optionally set the Title property in order to show a label inside the control.

```
Event Start
	&speed.Add(30)
	&speed.Add(50)
	&speed.Add(80)
EndEvent
```

`[imagen omitida: wiki id 9898]`

#### [Show a serie of numeric values with labels: the speed by driver](#Show+a+serie+of+numeric+values+with+labels%3A+the+speed+by+driver)

* Drag and drop the Gauge Control

In this case we have a simple SDT with:

```
Driver C(20)
Speed  N(4)
```

And we define a collection of this type and assign to the Data property.

We need to load data in the start event.

```
Event Start
	&driver = new()
	&driver.Driver = "JNJ"
	&driver.Speed = 130
	&drivers.Add(&driver)

	&driver = new()
	&driver.Driver = "ALevin"
	&driver.Speed = 210
	&drivers.Add(&driver)

EndEvent
```

`[imagen omitida: wiki id 9899]`

As you can see in the image the maximum value now is 250, we can change the maximum and minimun value of the control using the Max and Min properties under the Range category.

At first look we can say that ALevin is faster than JNJ.

Sometimes we need additional information for each Driver, if we add a new attribute to the SDT we can see more information

```
Driver C(20)
Speed  N(4)
SpeedingTickets N(4)
```

`[imagen omitida: wiki id 9900]`

#### [Show Several Values based on a SDT or BC](#Show+Several+Values+based+on+a+SDT+or+BC)

This control support any SDT or BC variable in its Data property. Basically the control will display a Gauge for each numeric item of the SDT or BC.

So, if for example we have the following SDT : Computer

```
ComputerName     C(30)
Memory           Numeric
CPU              Numeric
Network          Numeric
```

And we associate a Computer variable to our control, in runtime we are going to get:

`[imagen omitida: wiki id 9901]`

Take into account that non-numeric fields are ignored.

#### [Enhance the Gauge Drawing](#Enhance+the+Gauge+Drawing)

The Gauge Control has many properties in order to enhance the visualization of your values.

Basically, you can draw ranges with green, yellow or red color.  So there are 6 properties for this

<Color>Form = The lowest value for a range marked by a <Color> color.

<Color>To = The highest value for a range marked by a <Color> color.

So we can set the values for the Uruguay traffic rules in terms of speed.

GreenTo = 45  
YellowFrom = 45  
YellowTo = 60  
RedFrom = 60  
RedTo = 210

`[imagen omitida: wiki id 9902]`

Is it difficult to stay in the green area? Yes, it is ;)

You can add using MajorTicksLabels property for major tick marks. The number of labels defines the number of major ticks in all gauges. The default is five major ticks, with the labels of the minimal and maximal gauge value.

So, in the sample, you can set the property to the variable &labels, where &labels is a string collection variable

```
	&labels.Add("0")
	&labels.Add("$$$")
	&labels.Add("Warning!")
	&labels.Add("Jail")
```

So now we have the following gauge for our numeric value

`[imagen omitida: wiki id 9903]`

You can set how many minor Ticks are between each major Tick mark using the MinorTicks property.

#### [To Install It](#To+Install+It)

Please visit: [HowTo: Install User Controls](https://wiki.genexus.com/commwiki/wiki?5920)

#### [Implementation Details](#Implementation+Details)

GeneXus Gauge Control is based on the [Google Gauge Control](https://developers.google.com/chart/interactive/docs/gallery/gauge).

One or more gauges are rendered within the browser using SVG or VML.

### [Scope](#Scope)

**Objects:** [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)


|  |
| --- |
| **Backlinks** |
| [GXGoogle Visualization Library](https://wiki.genexus.com/commwiki/wiki?10447) |

---
