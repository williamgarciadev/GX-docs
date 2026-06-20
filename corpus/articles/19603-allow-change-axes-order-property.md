---
title: "Allow Change Axes Order property"
source_id: 19603
source_url: https://wiki.genexus.com/commwiki/wiki?19603
genexus_version: "18"
---

# Allow Change Axes Order property

Sometimes it may happen that, so as not to duplicate a Query object by changing the sort order of its elements in a same area to change the view, the developer changes it at runtime. This property allows sorting the fields in the PivotTable according to the order set in the Query object, or the order in which the developer loaded the &Axes collection in the Web Panel in run-time.

### [Values](#Values)

|  |  |
| --- | --- |
| **False** | The sort order of the elements is as stated in the Query object. This is the default value. |
| **True** | If there is code in any Web Panel event that places the elements in a certain order, this will be the order used. If there isn’t any code that rearranges the elements, the order stated in the Query object will be assumed. |

### [Example](#Example)

In the following example the property is set to True because the sort order in which the developer wants to show the Query object elements is different (reverse) than the order set at design time.

`[imagen omitida: wiki id 19810]`

```
Sub "SetAttributesOrder"
    &Axis = New()
    &Axis.Name = "ClientActive"  // First
    &Axes.Add(&Axis)
    &Axis = New()
    &Axis.Name = "ClientAdmissionDate"  // Second
    &Axes.Add(&Axis)
    &Axis = New()
    &Axis.Name = "ClientName"  // Third
    &Axes.Add(&Axis)
    &Axis = New()
    &Axis.Name = "ClientId"  // Fourth
    &Axes.Add(&Axis)
EndSub
```

`[imagen omitida: wiki id 19605]`

##### [AllowChangeAxesOrder = False vs AllowChangeAxesOrder = True (the code work)](#AllowChangeAxesOrder+%3D+False+vs+AllowChangeAxesOrder+%3D+True+%28the+code+work%29)

### [Scope](#Scope)

**Output type** Table, PivotTable


|  |
| --- |
| **Backlinks** |
| [Axis and Visible property refactoring](https://wiki.genexus.com/commwiki/wiki?47094) | [QueryViewer control properties](https://wiki.genexus.com/commwiki/wiki?32920) |

---
