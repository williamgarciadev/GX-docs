---
title: "Click event"
source_id: 8177
source_url: https://wiki.genexus.com/commwiki/wiki?8177
genexus_version: "18"
---

# Click event

To take place when the user clicks the left button over a control.

In the case of Web Forms, the event is implemented for the following type of controls: Bitmap, Textblock, Dynamic Combo Box, Combo Box, Sections, and tables (both responsive and common tables).

### [Notes](#Notes)

* In web Forms in combo type controls, the event is executed when changing the value contained in the control. (Use [ControlValueChanged event](https://wiki.genexus.com/commwiki/wiki?22676) instead for this purpose)
* In web Forms where you have the link property defined on a text block type control apart from the click event, the results can be unpredictable (you can execute the event or take into account the property according to the generator and the version). In any other case, it is not recommended to have both programmed at once.
* In the case of tables, if the click event is implemented for two or more nested tables, and the inner table is clicked, only the event of that table is executed (not of its containers).

#### [Checkbox](#Checkbox)

If the attrribute/variable has an associated event, the pointer cursor is configured as 'pointer' (typically an image of a pointing hand).

If the attrribute/variable does not have an associated event, the default cursor is set (standard arrow).

In those cases where the control is disabled:

* The abstract form sets the not-allowed cursor.
* The HTML form uses the default cursor.

### [Example](#Example)

```
Event &Country.Click
    &City.Clear()
    For each 
        Where CountryCod = &Country 
            &City.Additem(CityCod,CityDsc)
    Endfor
EndEvent  // &Country.Click
```

In this example, when choosing an option of the 'Country' combo, (as long as the selected value is different from the pre-existing one) its click event is executed by loading the cities that correspond to the selected country in the city combo.

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects** | [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) |
| **Controls** | Check boxes, Column, Combo boxes, Dynamic combo boxes, Dynamic list boxes, Edits, Image, List boxes, Textblocks, Tables, Sections |
| **Languages** | .NET, Java |


|  |
| --- |
| **Backlinks** |
| [Category:Control Events](https://wiki.genexus.com/commwiki/wiki?24271) | [Events in Transactions](https://wiki.genexus.com/commwiki/wiki?8042) | [GeneXus For SAP Systems - KPI Worklist Floorplan](https://wiki.genexus.com/commwiki/wiki?38645) |
| [GeneXus For SAP Systems - List Report Floorplan](https://wiki.genexus.com/commwiki/wiki?38572) | [GeneXus For SAP Systems - Simple Worklist with global action Floorplan](https://wiki.genexus.com/commwiki/wiki?38796) | [GeneXus For SAP Systems - Split Screen Master List Floorplan](https://wiki.genexus.com/commwiki/wiki?38873) | [GeneXus For SAP Systems - Split Screen Master List with amount Floorplan](https://wiki.genexus.com/commwiki/wiki?38912) |
| [GeneXus For SAP Systems - Split Screen Master List with amount Floorplan (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?55230) | [GeneXus For SAP Systems KPI Worklist Floorplan (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54915) | [GeneXus For SAP Systems List Report Floorplan (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54853) | [GeneXus For SAP Systems Simple Worklist with global action Floorplan (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55017) |
| [GeneXus For SAP Systems Split Screen Master List Floorplan (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54939) | [Category:Grid control](https://wiki.genexus.com/commwiki/wiki?24817) | [Parameters QueryViewer property](https://wiki.genexus.com/commwiki/wiki?19808) |

---
