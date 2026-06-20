---
title: "Dashboard object Parameters"
source_id: 42662
source_url: https://wiki.genexus.com/commwiki/wiki?42662
genexus_version: "18"
---

# Dashboard object Parameters

It is possible to set parameters to the [Dashboard object](https://wiki.genexus.com/commwiki/wiki?36769) when instantiated and use them anywhere in the [widget properties](https://wiki.genexus.com/commwiki/wiki?36779).

Use the *Parameters* section within the Dashboard editor to define them.

`[imagen omitida: wiki id 42664]`

The parameter passing must be set from the caller object using the [DashboardViewer control](https://wiki.genexus.com/commwiki/wiki?36770). The syntax is as follows:

```
DashboardViewer1.Object = DashboardObjectName(&Parm1, &Parm2, ..., &ParmN)
```

## [Properties](#Properties)

The properties where parameters can be used are the following:

* Dashboard
  + [Title](https://wiki.genexus.com/commwiki/wiki?40508)(1) and RefreshPeriod
* any [widget](https://wiki.genexus.com/commwiki/wiki?36779)
  + [Frame title](https://wiki.genexus.com/commwiki/wiki?40422)(1)
* [Query object](https://wiki.genexus.com/commwiki/wiki?9026) or [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270)
  + Title(1), [XAxis Title](https://wiki.genexus.com/commwiki/wiki?19680)(1) and [YAxis Title](https://wiki.genexus.com/commwiki/wiki?42240)(1) (for charts)
  + [Page size](https://wiki.genexus.com/commwiki/wiki?40469) (for Table and PivotTable)
* Element of a [Query object](https://wiki.genexus.com/commwiki/wiki?9026) or [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270)
  + Title(1)
  + [Year title](https://wiki.genexus.com/commwiki/wiki?40158)(1), [Semester title](https://wiki.genexus.com/commwiki/wiki?40159)(1), [Quarter title](https://wiki.genexus.com/commwiki/wiki?40160)(1), [Month title](https://wiki.genexus.com/commwiki/wiki?40161)(1), DayOfWeekTitle(1) (for Date or DateTime with grouping)
  + TargetValue, MaximumValue (for attributes in the Data)
  + ShowedValues (if Filter = ShowSomeValues), ExpandedValues (if Expand / Collapse = ExpandSomeValues) and CustomOrder (if Order = Custom).
* Filter
  + Caption(1)
  + Value (if FilterType = Value)
  + LowerValue and UpperValue (if FilterType = Range)
  + Values (if FilterType = Collection)
  + MinValue and MaxValue (if FiterType = Value or Range)
  + InviteMessage(1) (for filters of type Edit).
* [Image object](https://wiki.genexus.com/commwiki/wiki?23387)
  + AlternateText(1)
* [Text Block control](https://wiki.genexus.com/commwiki/wiki?5948)
  + Caption(1)

(1) - in addition to accepting a parameter; it also accepts a string that contains one or more parameters, for example: "&Surname, &Name".

## [Sample](#Sample)

```
Event Start
    &StartDate = &Today - 30
    DashboardViewer1.Object = Statistics(&StartDate)
Endevent
```

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 3](https://wiki.genexus.com/commwiki/wiki?42129,,).


|  |
| --- |
| **Backlinks** |
| [Category:Dashboard object](https://wiki.genexus.com/commwiki/wiki?36769) | [Toc:Reporting in GeneXus](https://wiki.genexus.com/commwiki/wiki?25314) |

---
