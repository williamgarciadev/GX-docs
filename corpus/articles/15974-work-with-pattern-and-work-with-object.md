---
title: "Work With pattern and Work With object"
source_id: 15974
source_url: https://wiki.genexus.com/commwiki/wiki?15974
genexus_version: "18"
---

# Work With pattern and Work With object

After [applying the Work With Pattern](https://wiki.genexus.com/commwiki/wiki?15975) to a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) you can access, edit and configure the *WorkWith<TransactionName>* object.

In the image below, the Work With Pattern has been applied to the "Property" Transaction, so the "WorkWithProperty" object has been generated:

`[imagen omitida: wiki id 51902]`

You can access the *WorkWith<TransactionName>* object in two ways:

1) In the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210), under the Transaction involved, you can open the *WorkWith<TransactionName>* with a double-click.  
2) Open the Transaction involved, select the Patterns selector, and then click on the "Work With" tab.

The image below shows the "WorkWithProperty" object opened:

`[imagen omitida: wiki id 52760]`

### WorkWith*<TransactionName>* object Nodes

#### 1) List

It is the list on which the end user will be working. Conceptually, what is associated with a list is a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) that contains a grid with the data. Over this panel, there is a default Action that basically indicates that when a record of the List is selected, its Detail has to be displayed.

It is possible to apply filters, orders, and searches to lists.  
  
There are also several ways to show the data and it is even possible to perform actions on the records list.

Since conceptually it is just a Panel, the same elements of a Panel are available: [Actions](https://wiki.genexus.com/commwiki/wiki?20623), Conditions, Layouts by platform, etc.

Read more at [Work With List Node](https://wiki.genexus.com/commwiki/wiki?15984).

#### 2) Detail

It's the [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) in which the selected record details will be displayed.

For example, when looking at a properties list and selecting one, it gives access to:

* Detailed info about the record.
* Related information (e.g. appointments).
* Actions (schedule a visit, send an email to the real estate firm offering the property, approve orders, etc.)

Read more at [Work With Detail Node](https://wiki.genexus.com/commwiki/wiki?15985).

#### 3) Sections

When displaying a set of data and its relations, there's always the problem of how to show this data in an ordered manner that the end user can understand. For this reason, the Work With Pattern provides the Section concept in a Detail.

When using Sections, you must have a way to organize them within a Detail. To do so, in the Detail Layout you can make reference to one or more sections.

Given that the Detail allows multiple Layouts per platform, it may happen that some sections are displayed on one platform but not on another.

Read more at [Work With Section Node](https://wiki.genexus.com/commwiki/wiki?20624).

### Generated application

The following image shows the generated application as a result of having applied the Work With Pattern to the Property Transaction:

`[imagen omitida: wiki id 52224]`

### [See Also](#See+Also)

[Applying Work With Pattern](https://wiki.genexus.com/commwiki/wiki?15975)  
[Work With Pattern instance for Multi-level Transactions](https://wiki.genexus.com/commwiki/wiki?16004)  
[Work With Pattern Settings](https://wiki.genexus.com/commwiki/wiki?17353)


|  |
| --- |
| **Pages** |
| [Check For New Data After Minutes Elapsed property](https://wiki.genexus.com/commwiki/wiki?18329) | [Check For New Data property](https://wiki.genexus.com/commwiki/wiki?18322) | [Deep Link Name property](https://wiki.genexus.com/commwiki/wiki?36162) |
| [Enable Data Caching property](https://wiki.genexus.com/commwiki/wiki?18302) | [Enable Show Password property](https://wiki.genexus.com/commwiki/wiki?35577) | [Lapse property](https://wiki.genexus.com/commwiki/wiki?17303) |
| [PageChanged event](https://wiki.genexus.com/commwiki/wiki?22735) | [Registration Handler property](https://wiki.genexus.com/commwiki/wiki?22981) |

---
