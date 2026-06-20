---
title: "Determining the Base Table for each Grid in a Web Panel"
source_id: 6105
source_url: https://wiki.genexus.com/commwiki/wiki?6105
genexus_version: "18"
---

# Determining the Base Table for each Grid in a Web Panel

This article describes how the [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) is determined for each Grid included in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916).

## [Web Panel with only one Grid](#Web+Panel+with+only+one+Grid)

When the Web Panel contains only one [Grid control](https://wiki.genexus.com/commwiki/wiki?24817), there are two possible scenarios:

**1)** If the Grid has its [Base Trn property](https://wiki.genexus.com/commwiki/wiki?36811) configured, that [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) will be the Base Table of the Grid (and also the Base Table of the Web Panel).

The attributes present in the Web Panel in the following sections must belong to the [Extended Table](https://wiki.genexus.com/commwiki/wiki?6029) of the Base Table (just like in a For each command):

* The Form (Grid and outside the Grid, visible or hidden)
* Grid Order
* Grid Conditions
* Grid Data Selector
* Events (outside all For each commands)

Otherwise, it won't be possible to infer the values of these attributes and the [spc0043 message](https://wiki.genexus.com/commwiki/wiki?6431) will warn about this situation.

**2)** If the Grid doesn't have its [Base Trn property](https://wiki.genexus.com/commwiki/wiki?36811) configured, GeneXus determines the Grid base table by considering the attributes included in the Web Panel in the following sections:

* The Form (Grid and outside the Grid, visible or hidden)
* Grid Order
* Grid Conditions
* Grid Data Selector
* Events (outside all For each commands)

GeneXus calculates the smallest [Extended Table](https://wiki.genexus.com/commwiki/wiki?6029) of all possible extended tables containing the attributes mentioned, and it chooses for the Grid one base table that allows access to the calculated extended table.

The following attributes ARE NOT taken into account in determining theBase Table in any case:

* General Conditions (those included in the Conditions tab)
* Those present inside the [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862)
* Attributes inside a For each command

### [Samples](#Samples)

#### [Sample #1](#Sample+%231)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) Structures:

```
Country
{
   CountryId*
   CountryName
}

Customer
{
   CustomerId*
   CustomerName
   CustomerEmail
   CountryId
   CountryName
}

Invoice
{
   InvoiceId*
   InvoiceDate
   CustomerId
   CustomerName
   InvoiceDescription
   InvoiceAmount
}
```

The following Web Panel contains only one Grid with the attributes shown and the [Base Trn property](https://wiki.genexus.com/commwiki/wiki?36811) configured for the Grid:

`[imagen omitida: wiki id 54110]`  
The Web Panel has no events nor any definition except for the Layout and property shown.

As the Base Trn property is set to Invoice, the [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) determined for the Grid is Invoice. In addition, as the attributes included in the Grid belong to the Invoice [Extended Table](https://wiki.genexus.com/commwiki/wiki?6029), at runtime, the Invoice table is navigated and for each Invoice record, the desired data is obtained and shown as a row in the Grid.

#### [Sample #2](#Sample+%232)

Consider the same objects involved in Sample #1 but with the Grid [Base Trn property](https://wiki.genexus.com/commwiki/wiki?36811) set to Customer.

`[imagen omitida: wiki id 54138]`

As the Base Trn property is set to Customer, the [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) determined for the Grid is Customer.

However, not all the attributes included in the Grid belong to the Customer [Extended Table](https://wiki.genexus.com/commwiki/wiki?6029). So, the CountryName attribute can be inferred for each Customer while the Invoice attributes can't. This is warned with the [spc0043 message](https://wiki.genexus.com/commwiki/wiki?6431).

At runtime, the Customer table is navigated and the Country data is obtained for each Customer record. So, for each Customer, its CustomerName, CustomerEMail, and CountryName are shown as a row in the Grid. The values of the Invoice attributes will be undefined.

#### [Sample #3](#Sample+%233)

Consider the same objects involved in Sample #1 and Sample #2 but with the Grid's [Base Trn property](https://wiki.genexus.com/commwiki/wiki?36811) empty.

`[imagen omitida: wiki id 54218]`

The [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) will be automatically determined by GeneXus analyzing the attributes included in:

* The Form (Grid and outside the Grid, visible or hidden)
* Grid Order
* Grid Conditions
* Grid Data Selector
* Events (outside all For each commands)

The Web Panel has no events nor any definition except for the Layout shown.

The determined Base Table will be Invoice because, by navigating that table, **all the mentioned attributes** belong to the Invoice [Extended Table](https://wiki.genexus.com/commwiki/wiki?6029). Thus, at runtime, the Invoice table is navigated and for each Invoice record, the related data about the customer and country is obtained and shown as a row in the Grid.

## Web Panel with several Grids

When the Web Panel contains more than one [Grid control](https://wiki.genexus.com/commwiki/wiki?24817), there are two possible scenarios:

### [1) Parallel Grids](#1%29+Parallel+Grids)

Read about this in [Parallel Grids in Web Panels](https://wiki.genexus.com/commwiki/wiki?55724,,).

### [2) Nested Grids](#2%29+Nested+Grids)

Read about this in [Nested Grids in Web Panels](https://wiki.genexus.com/commwiki/wiki?6062).
