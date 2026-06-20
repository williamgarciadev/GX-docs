---
title: "Data Selector object"
source_id: 5271
source_url: https://wiki.genexus.com/commwiki/wiki?5271
genexus_version: "18"
---

# Data Selector object

Stores a set of Parameters, Conditions, Orders, and a Defined By clause in order to invoke it from different queries, calculations, etc. and reuse the same navigation several times.

Defining Data Selectors brings the following advantages:

* Saving and reusing code: You define a Data Selector once and you can use that definition in several places in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).
* Less maintenance: You change a Data Selector definition in one place and it applies automatically everywhere it is used in the Knowledge Base.
* They facilitate training in GeneXus: They provide code encapsulation and are easy to learn, define, and use.

### [Samples](#Samples)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

```
Customer
{
   CustomerId*
   CustomerName 
   CustomerAddress
   CustomerStatus //One of the values that it stores is “Active”
}
```

Note it contains the *CustomerStatus* attribute. One of the possible values that it stores is “Active”.

Suppose that you need to query the "active customers" (*CustomerStatus*= “Active”) in many definitions in your KB. For example:

* In a [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) that queries active customers, grouped by Gender.
* In a For each command that applies a discount for active customers.
* In a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) (included in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) or [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)) that shows the total purchases of each active customer.

So, it is appropriate to define a Data Selector object with the filter condition and invoke it from the necessary places.

The following image shows a Data Selector named "ActiveCustomers" that defines the proposed filter:

`[imagen omitida: wiki id 54801]`

Once the Data Selector is defined, it can be invoked from:

* [For Each groups](https://wiki.genexus.com/commwiki/wiki?5312)
* [Data Provider groups](https://wiki.genexus.com/commwiki/wiki?6501)
* [Grid controls](https://wiki.genexus.com/commwiki/wiki?5386)
* [Aggregate formula definitions](https://wiki.genexus.com/commwiki/wiki?5432)
* [Work With Pattern List Node](https://wiki.genexus.com/commwiki/wiki?15984)

### [See Also](#See+Also)

[Data Selector Editor](https://wiki.genexus.com/commwiki/wiki?5544)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Data Selectors](https://training.genexus.com/en/learning/courses/genexus/genexus-16-course-analyst/data-selectors-v16?p=5414)


|  |
| --- |
| **Pages** |
| [Data Selector Editor](https://wiki.genexus.com/commwiki/wiki?5544) | [Data Selector property](https://wiki.genexus.com/commwiki/wiki?5361) | [Data Selector property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?57171) |
| [Data Selectors in Aggregations](https://wiki.genexus.com/commwiki/wiki?5432) | [Data Selectors in Data Providers](https://wiki.genexus.com/commwiki/wiki?6501) | [Data Selectors in Grids](https://wiki.genexus.com/commwiki/wiki?5386) |
| [Data Selectors in Grids (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?57179) | [Order property](https://wiki.genexus.com/commwiki/wiki?9842) | [Using Data Selectors - Examples](https://wiki.genexus.com/commwiki/wiki?5384) |
| [Using Read Replicas in GeneXus](https://wiki.genexus.com/commwiki/wiki?54289) |

---
