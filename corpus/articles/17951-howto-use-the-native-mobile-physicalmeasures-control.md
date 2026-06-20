---
title: "HowTo: Use the Native Mobile PhysicalMeasures Control"
source_id: 17951
source_url: https://wiki.genexus.com/commwiki/wiki?17951
genexus_version: "18"
---

# HowTo: Use the Native Mobile PhysicalMeasures Control

The Physical Measures control lets you easily manage physical measures such as height, weight, volume, temperature, etc.

It also enables the **end-user** to choose in which metric system they want to work.

**Note**: This control applies to attributes and variables. Also it is only supported in Apple and Android devices.

### [Samples](#Samples)

Start by defining the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) with the Work With pattern applied:

```
Person
{
PersonId*              Numeric(4.0)
PersonName             Varchar(40)
PersonHeight           Varchar(40)
PersonWeight           Varchar(40)
}
```

Once you have applied the Work With pattern, you need to enable the Physical Measures control. To do this, go to Section (General), select the attribute, and set its [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) to "PhysicalMeasure" value. You must do this both in the View and Edit layouts.

`[imagen omitida: wiki id 53749]`

This will enable the Measure Type property, as seen in the image. For this example, choose Height.

Now, just press F5.

Doing this, the user of the application will have the possibility to choose the unit for the height (feet or meters) at the moment of inserting or updating the value.

### [Snapshots](#Snapshots)

#### [In iPad](#In+iPad)

`[imagen omitida: wiki id 18051]`

(The field above the wheels shows the current value, not the one selected in the wheels.)

#### [In Android](#In+Android)

`[imagen omitida: wiki id 18052]`

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Controls: SD Maps, Rating, SD Smart Grids, Switch](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/controls-sd-maps-rating-sd-smart-grids-switch?p=3649)


|  |
| --- |
| **Backlinks** |
| [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) | [Category:Control Types](https://wiki.genexus.com/commwiki/wiki?20402) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
