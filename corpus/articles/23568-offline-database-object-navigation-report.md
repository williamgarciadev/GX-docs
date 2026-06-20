---
title: "Offline Database Object Navigation Report"
source_id: 23568
source_url: https://wiki.genexus.com/commwiki/wiki?23568
genexus_version: "18"
---

# Offline Database Object Navigation Report

As any other GeneXus object, the [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509) specifies a Navigation Report about all the Tables, Conditions, Events, etc. that it will access.

This navigation report shows the **Start** **Event** navigation (See [Offline Database Object events](https://wiki.genexus.com/commwiki/wiki?23566)), and one **Synchronize** **Event** navigation for each table synchronized by the [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509). For each Synchronize Event, it shows the **conditions** that apply to that table, from the conditions specified in the Conditions tab.

### [Example](#Example)

For instance, in the Simple Offline Application sample the condition

CustomerStatus = CustomerStatus.Active;

will generate the following Synchronize Event events in the navigation report:

`[imagen omitida: wiki id 23572]`

Also, if there is a Start Event in the Events section like this:

```
Event Start
    &ClientId = ClientInformation.Id
    For Each
    where DeviceId = &DeviceId
        &SalesAreaId = SalesAreaId
    EndFor
Endevent
```

The corresponding navigation of that event will be shown in the Offline Database object navigation:

`[imagen omitida: wiki id 23573]`

### [Note](#Note+)

Since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,) the navigation report of an Offline Database object shows for each table one object name that references it (although it is possible that other objects also reference the table).

Message style:

* Table Country is used at least by Procedure prc: SearchCountries (base table)
* BusinessComponent Country is used at least by SDPanel MySDPanel (base table)

This makes it easier to understand how the structure of the Offline Database is created, and it is useful in tracking and fixing any related issue or error.

### [See also](#See+also)

* [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509)
* [Offline Database Object conditions](https://wiki.genexus.com/commwiki/wiki?23570)
* [Offline Database Object events](https://wiki.genexus.com/commwiki/wiki?23566)
* [View Navigation object option](https://wiki.genexus.com/commwiki/wiki?7196)


|  |
| --- |
| **Backlinks** |
| [My first Offline Native Mobile application](https://wiki.genexus.com/commwiki/wiki?20249) | [Category:Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509) | [Offline Database Object conditions](https://wiki.genexus.com/commwiki/wiki?23570) |
| [Offline Database reorganization](https://wiki.genexus.com/commwiki/wiki?27121) | [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) |

---
