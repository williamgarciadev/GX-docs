---
title: "Unique Clause"
source_id: 24592
source_url: https://wiki.genexus.com/commwiki/wiki?24592
genexus_version: "18"
---

# Unique Clause

Declares attributes so that, if they have duplicate values in different records, they are considered only once for the query output.

### [Syntax](#Syntax)

**unique** *<Att1,...,AttN>*

**Where:**

*Att1,...,AttN*  
          List of attributes (including [formula attributes](https://wiki.genexus.com/commwiki/wiki?6440)) that are going to be processed together —only once in the output. Thus, if two or more records have the same values for that list of attributes, only one of them is taken into account. The attributes must belong to the [Extended Table](https://wiki.genexus.com/commwiki/wiki?6029) of the [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) queried and there are certain aspects to take into account that are illustrated below with examples.

### [Description](#Description)

Below are described two scenarios of use.

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,)s for all the examples proposed:

```
Customer
{
  CustomerId*
  CustomerName
}

Product
{
  ProductId*
  ProductName
  ProductPrice
}

Invoice
{
  InvoiceId*
  InvoiceDate
  CustomerId
  CustomerName
  InvoiceTotal - Formula Attribute: SUM(InvoiceLineAmount)
  Line
  {   
     ProductId*
     ProductName
     ProductPrice
     InvoiceLineQuantity
     InvoiceLineAmount - Formula Attribute: ProductPrice * InvoiceLineQuantity
   }
}
```

#### **1. Simple scenario: To avoid duplicates.**

Suppose you need to list all the dates for which there are invoices, without repeating dates:

```
For each Invoice
unique InvoiceDate
   print PBDate //printblock with InvoiceDate attribute
endfor
```

#### [**2. More complex scenario: To show groups of data with aggregation.**](#2.+More+complex+scenario%3A+To+show+groups+of+data+with+aggregation.)

Suppose you need to list, for each invoice date, the total amount of all invoices on that date:

```
For each Invoice
unique InvoiceDate
   &total = Sum(InvoiceTotal)
   print PBTotalAmountDate //printblock with: InvoiceDate, &total
endfor
```

Note that the [For each](https://wiki.genexus.com/commwiki/wiki?24744) Base Table is the same as the [Sum](https://wiki.genexus.com/commwiki/wiki?6500) aggregate inline formula Base Table (Invoice). Thus, the formula will add from the context an implicit condition for the evaluation: It will sum all the invoice totals for the**attribute mentioned in the Unique clause**(InvoiceDate), as the navigation report shows:

`[imagen omitida: wiki id 25508]`

**Consideration**

The base table of the formula defined inside the For each command is determined taking into account the attributes involved in its definition **and also in the context of the For each with Unique clause**.

For example, if you want to count and show, for each product, in how many invoices it was purchased without considering those products that have never been purchased, and you define the following code:

```
For each InvoiceLine unique ProductId            
    &ProductInvoicesQuantity = count(ProductId)  //the formula base table will not be Product. It will be InvoiceLine.
    print PBProductWithInvoiceQty                //printblock with: ProductId, ProductName, &ProductInvoicesQuantity
endfor
```

The formula base table will not be Product. It will be InvoiceLine because not only the ProductId attribute is taken into account but also the context of the For each with Unique clause. Thus, the For each base table and the formula base table are the same, and the formula will add an implicit condition for the evaluation: It will count for each ProductId (theattribute mentioned in the Unique clause) how many times it was ordered.

### [Restrictions](#Restrictions)

* The Unique clause cannot be declared in nested For each commands.
* Expressions are not allowed in the attributes list of the Unique clause. So, the following code is not allowed:

```
For each Invoice
unique InvoiceDate.Year()  //not allowed
    //do something
endfor
```

Instead, you can define a formula attribute (InvoiceDateYear in the Invoice Transaction first level) calculated as: InvoiceDate.Year() and reference that attribute in the Unique clause.

* Both in the body of the [For each command](https://wiki.genexus.com/commwiki/wiki?24744) and in the [Data Provider group](https://wiki.genexus.com/commwiki/wiki?25082), but outside inline formulas, you can only use attributes that have unique values with respect to those declared in the Unique clause.   
    

  **Note**: When referring to body, it does not include the order, using, where clauses, etc. That is, the restriction applies once the records are filtered, ordered, etc..

    
  So, the following code is incorrect:

  ```
  for each Unique InvoiceDate
      print PBInvoiceData //printblock with: InvoiceDate, InvoiceId
  Endfor
  ```

  The InvoiceId value is not unique for the records that have the same InvoiceDate value. Therefore, the following error will be displayed:

```
error: spc0206: Cannot reference attribute(s) InvoiceId unless they are referenced in Unique clause in group starting at line xx.
```

* Formulas in the body of a For each / Data Provider  
  + [Horizontal Formulas](https://wiki.genexus.com/commwiki/wiki?5864) included in the body of a For each / Data Provider  
    The attributes involved in the formula have to be reachable with a unique value from the attributes of the Unique clause.
  + [Aggregate Formulas](https://wiki.genexus.com/commwiki/wiki?5868) included in the body of a For each / Data Provider  
    The attributes involved in the formula do not need to be reachable with a unique value from the attributes of the Unique clause. That is why the following example is valid.  
      
    Suppose you need to print, for each customer with invoices from a certain date, his/her name and the total amount of those invoices:

```
For each Invoice
unique CustomerName
where InvoiceDate >= &fromDate
   &total = Sum(InvoiceTotal, InvoiceDate>=&fromDate)
   print PBCustomerInfo //printblock with: CustomerName, &total
endfor
```

InvoiceDate is not reachable with a unique value from CustomerName, but InvoiceDate is not in the body of the For each command, outside the Aggregate formula. It is mentioned only in the where clause, acting as a filter to obtain the records over with the body code itself will be executed. It is also in the Sum definition, indicating a filter over the records to be navigated in order to evaluate the formula.

### [Scope](#Scope)

|  |  |
| --- | --- |
| Commands: | [For each command](https://wiki.genexus.com/commwiki/wiki?24744), [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082) |

### [See Also](#See+Also)

[Unique clause in Data Providers](https://wiki.genexus.com/commwiki/wiki?24594)  
[Option Distinct clause](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?23811,,) (replaced by Unique clause, maintained for compatibility reasons)


|  |
| --- |
| **Backlinks** |
| [Aggregate Formulas](https://wiki.genexus.com/commwiki/wiki?5868) | [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082) | [For each command](https://wiki.genexus.com/commwiki/wiki?24744) |
| [Order Clause Specification](https://wiki.genexus.com/commwiki/wiki?5100) |
| [Unique Clause (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?57977) | [Unique clause in Data Providers](https://wiki.genexus.com/commwiki/wiki?24594) | [Unique property](https://wiki.genexus.com/commwiki/wiki?39891) | [Unique property (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55955) |

---
