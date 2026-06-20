---
title: "DashboardViewer control methods"
source_id: 43316
source_url: https://wiki.genexus.com/commwiki/wiki?43316
genexus_version: "18"
---

# DashboardViewer control methods

The following methods apply in the [DashboardViewer control](https://wiki.genexus.com/commwiki/wiki?36770):

* **Refresh()**
  + Causes the Dashboard to be updated.
* **GetFilterValue(&FilterName)**
  + Returns the value of a filter of Value or Range type.
* **GetFilterValues(&FilterName)**
  + Returns the value of a filter of Collection type.
* **SetFilterValue(&FilterName, &FilterValue)**
  + Sets the value of a filter of Value type.
* **SetFilterRange(&FilterNameLowerValue, &FilterLowerValue, &FilterNameUpperValue, &FilterUpperValue)**
  + Sets the value of a filter of Range type (if you want to set the value of only one of the range extremes, the FilterName of the extreme which is not to be changed must be passed empty).
* **SetFilterValues(&FilterName, &ValuesCollection)**
  + Sets the value of a filter of Collection type.

### [Note](#Note)

These methods only work in events that are generated **client**-**side**. These **server**-**side** events have no effect.

### [Example](#Example)

```
Event 'GetFilterValue'
    msg ( DashboardViewer1.GetFilterValue('CustomerAge'))
Endevent

Event 'SetFilterValue'
    DashboardViewer1.SetFilterValue('CustomerAge', '41')
Endevent

Event 'Get Filter Values'
    &Values = DashboardViewer1.GetFilterValues('CarBrandName')
    msg(&Values.ToJson())
Endevent

Event 'Set Filter Values'
    &Values.Clear()
    &Values.Add("Rover")
    &Values.Add("Peugeot")
    DashboardViewer1.SetFilterValues('CarBrandName', &Values)
Endevent

Event 'Get Range Values'
    msg( Format('Initial Age= %1 , End Age= %2', DashboardViewer1.GetFilterValue('CustomerAgeInit'), DashboardViewer1.GetFilterValue('CustomerAgeEnd')))
Endevent

Event 'Set Range Values'
    DashboardViewer1.SetFilterRange('CustomerAgeInit' , '41', 'CustomerAgeEnd' , '51')
Endevent
```

### [Sample](#Sample)

[TestWebQueryViewer](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?36747,,)

### [See also](#See+also)

[DashboardViewer control](https://wiki.genexus.com/commwiki/wiki?36770)  
[Dashboard object](https://wiki.genexus.com/commwiki/wiki?36769)  
[DashboardViewer Control Events](https://wiki.genexus.com/commwiki/wiki?43263)


|  |
| --- |
| **Backlinks** |
| [Category:DashboardViewer control](https://wiki.genexus.com/commwiki/wiki?36770) |

---
