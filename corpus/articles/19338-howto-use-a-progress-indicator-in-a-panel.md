---
title: "HowTo: Use a Progress Indicator in a Panel"
source_id: 19338
source_url: https://wiki.genexus.com/commwiki/wiki?19338
genexus_version: "18"
---

# HowTo: Use a Progress Indicator in a Panel

The purpose of this article is to explain the necessary steps to enable the Progress Indicator in Panels.

### [Scope](#Scope)

**Objects:** [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Work With](https://wiki.genexus.com/commwiki/wiki?15974)  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Step 1. External Object - Properties and Methods](#Step+1.+External+Object+-+Properties+and+Methods)

See Progress Indicator in order to understand the API of the control.

### [Step 2. Learn by Example](#Step+2.+Learn+by+Example)

Use a Procedure with the [Sleep function](https://wiki.genexus.com/commwiki/wiki?8075) set to 4 in order to simulate an elapsed time.

For this example, create the following [Panel](https://wiki.genexus.com/commwiki/wiki?24829):

#### [Layout](#Layout)

`[imagen omitida: wiki id 37942]`

#### [Events](#Events)

```
Event 'Determinate'
    Composite
        Progress.Type = ProgressIndicatorType.Determinate
        progress.MaxValue = 100
        progress.Value = 0
        Progress.ShowWithTitleAndDescription("ProcessDeterminate","Sleeping...")
        sleepingProc()
        Progress.Value =25
        sleepingProc()
        Progress.Value =50
        sleepingProc()
        Progress.Value =75
        sleepingProc()
        Progress.Value =100
   EndComposite
EndEvent
```

```
Event 'Indeterminate'
    Composite
        Progress.Title = "Process Indeterminate"
        Progress.Description = "Sleeping..."
        Progress.Class = "Table.Progress"
        Progress.Type = ProgressIndicatorType.Indeterminate
        Progress.Show()
        sleepingProc()
   EndComposite
EndEvent
```

#### [Facts: (In Evolution 2 Upgrade 2)](#Facts%3A+%28In+Evolution+2+Upgrade+2%29)

* At the end of an Event an implicit Hide() is done. this is in case the Hide() call hasn't been done by the user.
* The scope of the properties of a Progress Indicator is per Panel. So, if calls are done between two Panels which have a Progress Indicator the properties are **not** going to be shared.
* Any UI element invoked by an action which also has a call to the Progress Indicator will be shown over the progress Indicator (Call, MSG, Confirm, etc).

### [Step 3. Execution](#Step+3.+Execution)

#### [Determinate](#Determinate)

`[imagen omitida: wiki id 19339]` `[imagen omitida: wiki id 19340]` `[imagen omitida: wiki id 19341]` `[imagen omitida: wiki id 19342]`

#### [Indeterminate](#Indeterminate)

`[imagen omitida: wiki id 19343]`

### [Restrictions](#Restrictions)

* The Progress Indicator external object can only be called from client-side events of Panels and from **offline** Procedures objects.


|  |
| --- |
| **Backlinks** |
| [How To: Use a Progress Indicator in a Web Panel](https://wiki.genexus.com/commwiki/wiki?32779) |
| [Progress external object](https://wiki.genexus.com/commwiki/wiki?39341) | [Progress Indicator User Control](https://wiki.genexus.com/commwiki/wiki?31275) |

---
