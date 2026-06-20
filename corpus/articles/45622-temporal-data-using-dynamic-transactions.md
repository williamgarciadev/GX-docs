---
title: "Temporal Data using Dynamic Transactions"
source_id: 45622
source_url: https://wiki.genexus.com/commwiki/wiki?45622
genexus_version: "18"
---

# Temporal Data using Dynamic Transactions

The most common way to model a value that changes sporadically over time is to store it in the database just when the value changed. For example, to record the prices of products that change over time, it is reasonable to define a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) that records, for each Product, when the Price changed and what the new Price is:

```
ProductLog
{
   ProductId*
   ProductLogDate*
   ProductLogPrice
   ProductLogName
}
```

At the same time, the most common query is to find out, given a Product and a Date, what the Price of the Product was on that Date. The traditional way to model this scenario is to have a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) that receives a Product and a Date as parameters and returns the corresponding Price:

```
Procedure GetProductPriceInDate
   Rules
      parm(in:&ProductId, in:&Date, out:&ProductPrice);
   Source
      for each ProductLog order ProductId, (ProductLogPrice)
         where ProductId      = &ProductId
         where ProductLogDate <= &Date
         &ProductPrice        = ProductLogPrice
         exit
      endfor
```

Although it is very simple, this solution has some drawbacks:

* It properly solves the query that obtains the Price given a Product and a Date, but not the other common query: Given a Date, get the Prices of all Products on this Date.
* What to do if there is no Price for the Product on this Date? (e.g. when the requested date is prior to the first date recorded for the product).
  + Normally for this case, you must define a special Price value (generally 0) to indicate there is no corresponding Price. This is not a good practice because, for example: how can you tell if a Product is free (Price = 0) or if it's not available?
* If, besides the Price, you need to retrieve more attributes (like the Name on a given Date) the procedure must return more than one attribute, with the drawback that it cannot be used in a Formula.
* The Procedure must be called explicitly every time the Price is needed.

Defining [Dynamic Transactions](https://wiki.genexus.com/commwiki/wiki?28062) makes it possible to have a model without these difficulties.

Consider the same Transaction shown in the previous example:

```
ProductLog
Struct
   {
      ProductId*
      ProductLogDate*
      ProductLogPrice
      ProductLogName
   }
```

And the following Dynamic Transaction:

```
Product //Dynamic Transaction
Struct
  {
     ProductId*
     ProductQueryDate*
     ProductPrice
     ProductName
  }
Data
   Data Provider property  = True
   Used to property = Retrieve data
   Data Provider
      Parm(in:ProductQueryDate);
      ProductPriceCollection
        {
            Product From ProductLog
                where ProductLogDate = Max(ProductLogDate, ProductLogDate <= ProductQueryDate)
            {
                ProductId
                ProductQueryDate
                ProductPrice = ProductLogPrice
                ProductName = ProductLogName
            }
        }
```

Note that the Data Provider associated with the Dynamic Transaction retrieves the Price of the Product for any possible Date.

Also, note that the Data Provider associated with the Dynamic Transaction has a parameter (ProductQueryDate) to indicate that this attribute must always have a value when the query is executed. Thus, the following query (given a Date, it prints the corresponding Price for each Product) is valid:

```
For Each Product
   where ProductQueryDate = &Today
   Print ProductId, ProductPrice
Endfor
```

But the following query (which "tries" to print all product prices in all possible dates) is not valid:

```
For Each Product
   Print ProductId, ProductPrice
Endfor
```

This is because GeneXus does not know how to obtain all possible dates (besides being an infinite number). In this case, GeneXus gives the following error at specification time:

```
error spc0214: Attribute(s) ProductQueryDate should be instantiated to navigate table Product in group starting at line 8.
```

The way to use the Dynamic Transaction is like any other Transaction. You just use its attributes and GeneXus solves the corresponding navigations. For example, consider the Sales Transaction that requires knowing the Price of the Product on the Sale Date:

```
Sale     // to simplify just one Product per Sale is assumed
Struct
   {
      SaleId* 
      SaleDate
      ProductId
      ProductQueryDate
      ProductPrice
      ProductName
   }
Rules
   ProductQueryDate = SaleDate;
```

GeneXus automatically controls temporal referential integrity. You will not be able to record a Sale if the Product does not have a Price in the SaleDate (in other words if there is no record in ProductLog).

### [Availability](#Availability)

This feature is available since [GeneXus 16 upgrade 9](https://wiki.genexus.com/commwiki/wiki?45275,,).


|  |
| --- |
| **Backlinks** |
| [Toc:Dynamic Transactions](https://wiki.genexus.com/commwiki/wiki?28062) |

---
