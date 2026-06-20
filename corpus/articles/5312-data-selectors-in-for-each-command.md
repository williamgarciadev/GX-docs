---
title: "Data Selectors in For each command"
source_id: 5312
source_url: https://wiki.genexus.com/commwiki/wiki?5312
genexus_version: "18"
---

# Data Selectors in For each command

There are two ways to use [Data Selectors](https://wiki.genexus.com/commwiki/wiki?5271) in a [For each command](https://wiki.genexus.com/commwiki/wiki?24744):

1. Through the USING clause.
2. Through the IN operator in the Where clause.

Depending on how they are used, the attributes included in the Data Selector definition are involved or not in determining the [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) of the For each command.

## [1. 'USING' clause](#1.+%27USING%27+clause)

### [**Syntax**](#Syntax)

```
For each [<BaseTrn1>|<BaseTrn.Level1>,...,<BaseTrnN>|<BaseTrn.LevelN>] 
    USING <DataSelectorName>([<parm1>,...,<parmN>])
      <MainCode>
EndFor
```

View [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626)

**Where:**

*BaseTrn1* | *BaseTrn.Level1,...,BaseTrnN* | *BaseTrn.LevelN*  
   Is a Transaction or a Transaction.Level name separated by a comma.

*DataSelectorName*  
   Is the name of the Data Selector.

*parm1, …, parmN*  
   Are variables defined in the called object or attributes.

*MainCode*  
   It is the list of commands.

### [Samples](#Samples)

#### [**Sample A**](#Sample+A)

Suppose you have the following [Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,):

```
Customer
{
   CustomerId*
   CustomerName
   CustomerImage
   CustomerStatus     
}
```

The "ActiveCustomers" Data Selector definition is as follows:

`[imagen omitida: wiki id 51133]`

This Data Selector has a condition defined to show the Active Customers.

Then, you can define the following code in the Source of the Procedure Object (or Web Panel, for example), to invoke the Data Selector:

```
For each Customer USING ActiveCustomers()
   print printblock1   //The printblock1 contains the attributes: CustomerId, CustomerName
EndFor
```

#### [**Sample B**](#Sample+B)

Suppose you have the following Transaction:

```
Invoice
{
   InvoiceId*
   InvoiceNumber
   InvoiceDate
}
```

Define a Data Selector called InvoicesByDate as follows:

`[imagen omitida: wiki id 51134]`

The Data Selector has a date condition and orders by InvoiceDate.

You can define the following code inside an Event of a Web Panel (or in the Source of a Procedure, for example), to invoke the Data Selector:

```
For each USING InvoicesByDate(&FromDate, &ToDate)
      &InvoiceId = InvoiceId
      &InvoideDate = InvoiceDate
EndFor
```

### [Considerations](#Considerations)

When invoking a Data Selector through the USING clause in a For each, the Data Selector doesn't have an associated navigation (it doesn't have a base table by itself). At specification time, the Data Selector definition is combined with the For each definition to determine the table that will be navigated, taking into account the attributes of both definitions. In addition:

* If the For each and the Data Selector have Conditions, both are considered
* If the For each and the Data Selector have Order clause(s), the resulting Order will be a combination of them. The For each order has priority, so in the event that GeneXus discards a Data Selector Order, a warning [spc0135](https://wiki.genexus.com/commwiki/wiki?6433) will be triggered at specification time

Suppose you have the following For each command that invokes the "ActiveCustomers" Data Selector through the USING clause:

```
For each Using ActiveCustomers()
    Where CountryName = "Uruguay"
          ...
EndFor
```

This is expanded at specification time to:

```
For each 
    Where CustomerStatus = "Active"
    Where CountryName = "Uruguay"
          ...
EndFor
```

**Note**: if you invoke the Data Selector within the For each (above example), performance is the same as if you wrote both Where clauses within the For each.

Note that the Data Selector is not detailed in the Navigation:

`[imagen omitida: wiki id 13238]`

Suppose you have defined a For each sentence that contains conditional orders + one unconditional order ('default' order), and it invokes a Data Selector through the USING clause. As the [For each command](https://wiki.genexus.com/commwiki/wiki?24744) only accepts one 'default' order, the specification's result will be the For each with its conditional orders + Data Selector conditional orders + the For each 'default' order (the Data Selector 'default' order will be discarded, and the navigation report will show a spc0135 warning).

## [2. 'IN' Operator in the Where clause](#2.+%27IN%27+Operator+in+the+Where+clause)

### [Syntax](#Syntax)

```
For each [<BaseTrn1>|<BaseTrn.Level1>,...,<BaseTrnN>|<BaseTrn.LevelN>] 
     Where [not] <attribute> IN <DataSelectorName>([<parm1>,...,<parmN>, …])
    <MainCode>
EndFor
```

View [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626)

**Where:**

*BaseTrn1* | *BaseTrn.Level1,...,BaseTrnN* | *BaseTrn.LevelN*  
   Same as Base Transaction clause in For each command.

*Attribute*  
   Is The name of the attribute that can belong or not to the extended table of the Data Selector base table.

*DataSelectorName*  
   Is the name of the Data Selector.

*parm1, …, parmN*  
   Are variables defined in the called object or attributes.

*MainCode*  
   It is the list of commands.

### [Samples](#Samples)

```
For each
    Where CustomerId IN InvoicesByDate(&FromDate,&ToDate)
          ...
Endfor
```

### [Considerations](#Considerations)

When invoking a Data Selector through the IN operator in the For each Where clause, the Data Selector **has a base table by itself**. This means that a SELECT sentence will be generated for the Data Selector definition, which will be a different and independent SELECT from the SELECT sentence that will be generated in relation to the For each.

Up to [GeneXus 15 Upgrade 5](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?34646,,), the attribute that precedes the IN operator must belong to the extended table of the Data Selector base table. In the above example, *CustomerId* belongs to the extended table of INVOICE, which is the "InvoicesByDate" Data Selector base table. Since [GeneXus 15 Upgrade 6](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?35908,,) the attribute associated to the IN operator does not necessarily need to belong to the extended table. The following specification is valid where there is no relationship between tables Customer and Provider.

```
For each Where CustomerId In ProviderIds()
    ...
EndFor
```

ProviderIds Data Selector specification is as follows:

```
Defined by: ProviderId
```

Notice the usage of the *Defined by* clause. The resulting SQL statement is similar to the following, where there is no relationship between tables Power and User.

```
SELECT.... FROM [Customer] WITH
WHERE [CustomerId] IN (SELECT [ProviderId] FROM [Provider])
```

The Data Selector query will return a collection of values corresponding to the same definition as the attribute which precedes the IN operator. In the above example, the Data Selector returns “a customers list” with invoices in the given range.

So, the For each base table is determined by taking into account only the For each attributes (Data Selector attributes are not considered). The For each will navigate its [base table](https://wiki.genexus.com/commwiki/wiki?6347) and [extended table](https://wiki.genexus.com/commwiki/wiki?6029), filtering the records which contain a customer of the customers list returned by the Data Selector.

In other words, in the above example, the Data Selector will return what you need as long as the attribute to the left belongs to the extended table of the Data Selector base table. The internal mechanism of the extraction operation is not important; what's important is that you can declare a Data Selector and it can be called by any other object.

Note that the Data Selector is not detailed in the Navigation:

`[imagen omitida: wiki id 13240]`

Some doubts may arise in relation to the order displayed in the Navigation Report, as the order specified in the Data Selector is InvoiceDate and the order detailed in the Navigation Report is CustomerId. Actually, the latter corresponds to the order of the For each command. The Data Selector, whose navigation is not detailed by GeneXus, accesses through InvoiceDate.

### [**Advanced notes**](#Advanced+notes)

The Data Selector's navigation will be generated as a subselect of the For each select. So, if the Data Selector has its own conditions, they must be evaluated in the server by the DMBS. Taking this into account, the following error/warnings could appear at specification time:

* [spc0053](https://wiki.genexus.com/commwiki/wiki?6432) Conditional constraint %1 cannot be generated in group starting at line n. Changed to standard constraint.

If the Data Selector has a [conditional constraint](https://wiki.genexus.com/commwiki/wiki?12566), it will be automatically changed to a standard constraint.

* [spc0144](https://wiki.genexus.com/commwiki/wiki?6433) Condition %1 found in DataSelector %2 cannot be evaluated in server.

There are still some [functions](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1999,,) that cannot be evaluated in the server.

### [Compound Keys considerations](#Compound+Keys+considerations)

The IN Operator takes into account the attribute preceding the IN clause; if you want to filter using a compound key you will need to create a new redundant formula attribute with the concatenation needed. Using the above example, suppose you want to add multi-tenant support; a possible design is to add a TenantId\* (key composition) attribute as part of all tables. To use the *In* operation, you will need to create a TenantIdCustomerId redundant attribute to do the filter.

```
For each
    Where TenantIdCustomerId IN InvoicesByDate(&FromDate,&ToDate)
          ...
Endfor
```

### [See Also](#See+Also)

[Data Selectors in Grids](https://wiki.genexus.com/commwiki/wiki?5386)  
[Data Selectors in Aggregations](https://wiki.genexus.com/commwiki/wiki?5432)  
[Data Selectors in Data Providers](https://wiki.genexus.com/commwiki/wiki?6501)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Data Selectors](https://www.youtube.com/watch?v=Mx9pCjxGdMQ)


|  |
| --- |
| **Backlinks** |
| [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082) | [Category:Data Selector object](https://wiki.genexus.com/commwiki/wiki?5271) | [Data Selector property](https://wiki.genexus.com/commwiki/wiki?5361) |
| [Data Selector property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?57171) | [Data Selectors in Aggregations](https://wiki.genexus.com/commwiki/wiki?5432) | [Data Selectors in Data Providers](https://wiki.genexus.com/commwiki/wiki?6501) | [Data Selectors in Grids](https://wiki.genexus.com/commwiki/wiki?5386) |
| [Data Selectors in Grids (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?57179) | [For each command](https://wiki.genexus.com/commwiki/wiki?24744) | [Table of contents:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [IN Operator](https://wiki.genexus.com/commwiki/wiki?11688) |
| [Order Clause Specification](https://wiki.genexus.com/commwiki/wiki?5100) | [Specification Codes from spc0050 to spc0099](https://wiki.genexus.com/commwiki/wiki?6432) | [Specification Codes from spc0100 to spc0149](https://wiki.genexus.com/commwiki/wiki?6433) | [Specification Codes from spc0150 onwards](https://wiki.genexus.com/commwiki/wiki?6774) |
| [Using Read Replicas in GeneXus](https://wiki.genexus.com/commwiki/wiki?54289) | [Where clause](https://wiki.genexus.com/commwiki/wiki?8578) |

---
