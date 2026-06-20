---
title: "Control Type property"
source_id: 9550
source_url: https://wiki.genexus.com/commwiki/wiki?9550
genexus_version: "18"
---

# Control Type property

Sets which kind of control to show. Possible values depend on whether the control is an Attribute/Variable, a Grid, an Action Group, or another, as well as on the platform, etc.

### [Values](#Values)

|  |
| --- |
| **Combo Box** |
| **Radio Button** |
| **Edit** |
| **Image** |
| **Check Box** |
| **Dynamic Combo Box** |
| **List Box** |
| **Dynamic List Box** |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Controls:** Attribute/Variable, [Grid](https://wiki.genexus.com/commwiki/wiki?24817)

### [Description](#Description)

For **Attribute/Variable** controls, the possible types are:

* Check Box
* Combo Box
* Dynamic Combo Box
* Dynamic List Box Setup
* Edit
* List Box
* Radio Button
* FCK Html Editor
* GXSpreadsheet
* [Scanner](https://wiki.genexus.com/commwiki/wiki?15310) (\*)
* [Rating Control](https://wiki.genexus.com/commwiki/wiki?18350) (only for variables or domains)
* [Linear Gague](https://wiki.genexus.com/commwiki/wiki?16269) (\*)
* [Multi Wheel](https://wiki.genexus.com/commwiki/wiki?20171) (\*)
* [Physical Measures](https://wiki.genexus.com/commwiki/wiki?17951) (\*)
* Advanced Image (\*)
* [Wheel](https://wiki.genexus.com/commwiki/wiki?16239) (\*)
* [Facebook Button](https://wiki.genexus.com/commwiki/wiki?31841) (\*)
* [SearchBox](https://wiki.genexus.com/commwiki/wiki?31862) (\*)
* [Chronometer](https://wiki.genexus.com/commwiki/wiki?25058)
* [Switch](https://wiki.genexus.com/commwiki/wiki?29973)
* Touch Controls - Carousel (\*)
* Web Linear Gauge

(\*) Only for [Native Mobile Generator](https://wiki.genexus.com/commwiki/wiki?14451)

Note: This property is not available when the attribute is a formula.

For **Grid** controls included in [Panel object](https://wiki.genexus.com/commwiki/wiki?24829), the possible types are:

* [Charts](https://wiki.genexus.com/commwiki/wiki?16106)
* [Flex Grid](https://wiki.genexus.com/commwiki/wiki?35354)
* Grid (default value)
* [Horizontal Grid](https://wiki.genexus.com/commwiki/wiki?30592)
* [Image Map](https://wiki.genexus.com/commwiki/wiki?17823)
* Legacy Grid
* [Magazine Viewer](https://wiki.genexus.com/commwiki/wiki?17567)
* [Maps](https://wiki.genexus.com/commwiki/wiki?15309)
* [Matrix Grid](https://wiki.genexus.com/commwiki/wiki?25139)
* [Spark Line](https://wiki.genexus.com/commwiki/wiki?17110,,)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.

### [See Also](#See+Also)

[Check Box properties in Web Forms](https://wiki.genexus.com/commwiki/wiki?8738)  
[Combo Box, Radio Button and List Box properties in Web Forms](https://wiki.genexus.com/commwiki/wiki?8739)  
[Dynamic Combo Box and Dynamic List Box Properties in Web Forms](https://wiki.genexus.com/commwiki/wiki?8740)


|  |
| --- |
| **Backlinks** |
| [AddItem method](https://wiki.genexus.com/commwiki/wiki?8668) | [Advanced Image Control](https://wiki.genexus.com/commwiki/wiki?20497) | [Align Content property](https://wiki.genexus.com/commwiki/wiki?36110) |
| [Align Items property](https://wiki.genexus.com/commwiki/wiki?36111) | [Attribute-checkbox class for Design System objects](https://wiki.genexus.com/commwiki/wiki?52932) | [Attribute-date class for Design System objects](https://wiki.genexus.com/commwiki/wiki?52976) | [Attribute-radiobutton class for Design System objects](https://wiki.genexus.com/commwiki/wiki?52968) |
| [Attribute/Variable control properties in Web Forms](https://wiki.genexus.com/commwiki/wiki?8133) | [Barcode Types property](https://wiki.genexus.com/commwiki/wiki?42176) | [Beep on each read property](https://wiki.genexus.com/commwiki/wiki?48530) | [Checked Value property](https://wiki.genexus.com/commwiki/wiki?8734) |
| [Clear method in Grids with Control Type = Maps](https://wiki.genexus.com/commwiki/wiki?46862) | [Control Title property](https://wiki.genexus.com/commwiki/wiki?8736) | [Counting Type property](https://wiki.genexus.com/commwiki/wiki?42253) | [Data Cell Height property](https://wiki.genexus.com/commwiki/wiki?40389) |
| [Data Source From property](https://wiki.genexus.com/commwiki/wiki?22945) | [Data Source From property (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55489) | [Display mode property](https://wiki.genexus.com/commwiki/wiki?48528) | [Display Value property](https://wiki.genexus.com/commwiki/wiki?42203) |
| [DrawGeography method](https://wiki.genexus.com/commwiki/wiki?47024) | [DrawGeoLine method](https://wiki.genexus.com/commwiki/wiki?47026) | [Edit with Suggest](https://wiki.genexus.com/commwiki/wiki?55531) | [External Object: Native Object](https://wiki.genexus.com/commwiki/wiki?6148) |
| [External Object: Native Object (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?56447) | [Facebook Button control](https://wiki.genexus.com/commwiki/wiki?31841) | [FCK HTML Editor Control](https://wiki.genexus.com/commwiki/wiki?4858) | [Flex Direction property](https://wiki.genexus.com/commwiki/wiki?36107) |
| [Toc:Flex Layout Container](https://wiki.genexus.com/commwiki/wiki?35354) | [Flex Wrap property](https://wiki.genexus.com/commwiki/wiki?36109) | [Format property (for att/var with Control Type=Relative Timer)](https://wiki.genexus.com/commwiki/wiki?42530) | [GeneXus Markup Language (GXML)](https://wiki.genexus.com/commwiki/wiki?46876) |
| [GeographySaved Event](https://wiki.genexus.com/commwiki/wiki?46858) | [Category:Grid control](https://wiki.genexus.com/commwiki/wiki?24817) | [Grids with Selection By Code for Panels](https://wiki.genexus.com/commwiki/wiki?35987) | [HowTo: In-app search in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?31862) |
| [HowTo: Use a Matrix Grid Control](https://wiki.genexus.com/commwiki/wiki?25139) | [HowTo: Use Charts Control](https://wiki.genexus.com/commwiki/wiki?16106) | [HowTo: Use Combo Box in Panels](https://wiki.genexus.com/commwiki/wiki?18408) | [HowTo: Use Horizontal Grid control in Panels](https://wiki.genexus.com/commwiki/wiki?18180) |
| [HowTo: Use MultiWheel Control](https://wiki.genexus.com/commwiki/wiki?20171) | [HowTo: Use Radio Button in Panels](https://wiki.genexus.com/commwiki/wiki?18434) | [HowTo: Use SD Geolocation Control in Smart Devices](https://wiki.genexus.com/commwiki/wiki?16756) | [HowTo: Use the Data Source From property](https://wiki.genexus.com/commwiki/wiki?22948) |
| [HowTo: Use the Dynamic Combo Box Control for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?16778) | [HowTo: Use the Image Map Control](https://wiki.genexus.com/commwiki/wiki?17823) | [HowTo: Use the Maps Control Type in a Panel Grid](https://wiki.genexus.com/commwiki/wiki?54097) | [HowTo: Use the Native Mobile PhysicalMeasures Control](https://wiki.genexus.com/commwiki/wiki?17951) |
| [HowTo: Use the Wheel Control](https://wiki.genexus.com/commwiki/wiki?16239) |
| [Image Annotations](https://wiki.genexus.com/commwiki/wiki?45373) | [Is Password property](https://wiki.genexus.com/commwiki/wiki?8803) |
| [Justify Content property](https://wiki.genexus.com/commwiki/wiki?36108) | [Layers in Maps](https://wiki.genexus.com/commwiki/wiki?40763) | [Linear Gauge Control](https://wiki.genexus.com/commwiki/wiki?16269) | [LoadKmlLayer method](https://wiki.genexus.com/commwiki/wiki?51341) |
| [Maps Control Type](https://wiki.genexus.com/commwiki/wiki?15309) | [MarkerDragEnd Event](https://wiki.genexus.com/commwiki/wiki?46860) | [MarkerDragStarted Event](https://wiki.genexus.com/commwiki/wiki?46859) | [Max Value Image property](https://wiki.genexus.com/commwiki/wiki?42268) |
| [Min Value Image property](https://wiki.genexus.com/commwiki/wiki?42267) | [Operation mode property](https://wiki.genexus.com/commwiki/wiki?48529) | [PageChanged event](https://wiki.genexus.com/commwiki/wiki?22735) | [Radio Direction property](https://wiki.genexus.com/commwiki/wiki?8818) |
| [Rating Class property](https://wiki.genexus.com/commwiki/wiki?43943) | [Results Panel property](https://wiki.genexus.com/commwiki/wiki?42205) | [Scanner Control](https://wiki.genexus.com/commwiki/wiki?15310) | [SetLayerVisible method](https://wiki.genexus.com/commwiki/wiki?54293) |
| [Show Page Controller property](https://wiki.genexus.com/commwiki/wiki?38864) | [Step property](https://wiki.genexus.com/commwiki/wiki?42477) | [Switch Control](https://wiki.genexus.com/commwiki/wiki?29973) | [Tick Interval property](https://wiki.genexus.com/commwiki/wiki?42188) |
| [Unchecked Value property](https://wiki.genexus.com/commwiki/wiki?8737) | [User Control Object - Using as Control Type](https://wiki.genexus.com/commwiki/wiki?40652) | [Values property](https://wiki.genexus.com/commwiki/wiki?49297) | [Values property (for Check Boxes, List Boxes and Radio Buttons)](https://wiki.genexus.com/commwiki/wiki?8819) |
| [Category:Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) | [X-Axis Height property](https://wiki.genexus.com/commwiki/wiki?42107) | [Y-Axis Width property](https://wiki.genexus.com/commwiki/wiki?42108) |

---
