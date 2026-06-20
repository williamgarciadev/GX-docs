---
title: "Default clause"
source_id: 25407
source_url: https://wiki.genexus.com/commwiki/wiki?25407
genexus_version: "18"
---

# Default clause

If the Default clause is present, the [Data Provider Group](https://wiki.genexus.com/commwiki/wiki?25082) will go to the Output only if the preceding Group (with the same name) is not present.

### [Syntax](#Syntax)

```
'['Default']'
```

View [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626)

### [Samples](#Samples)

If you have a Taxes table:

```
Taxes ( TaxInitialDate*, TaxFinalDate*, TaxVAT, TaxIncome )
```

A Data Provider that returns the current tax values can be as follows:

```
CurrentTaxes 
   Where TaxInitialDate >= today()
   Where TaxFinalDate <= today() 
{ 
   VAT = TaxVAT 
   Income = TaxIncome 
}
CurrentTaxes [Default] 
{ 
   VAT = 0.7 
   Income = 0.3 
}
```

Here, the last Group will return the default values if there aren't any taxes in the period.

Note that the Default clause is equivalent to a [When none](https://wiki.genexus.com/commwiki/wiki?8603) in a For Each.

The default clause applies to all groups at the same level (brothers). The Default group is executed if none of the previous condition was satisfied.

Look at this in more detail with a sample.

```
MySdtColl
{
      MySdtCollItem
      {
        Element where &a>3 { A=1 }
        Element where &a=5 { A=2 }
        Element [Default] where &a=2 { A=3 }
        Element [Default] { A=4 }
       }
}
```

...and its behavior in runtime with some cases:

If &a=5 return two items (A=1 and A=2)

If &a=6 return one item (A=1)

If &a=2 return one item (A=3)

If &a=1 return one item (A=4)

Another sample, suppose you want to return a collection with the name of the products belonging to some Category or if not exist any product in the given category you want to return a text indicating ‘No products in the given category’.

You can write the following Data Provider:

```
ProductsInCategory
{
      ProductsInCategoryItem
      Where ProductCategoryId = &CategoryId
      {
           ProductName
      }
      ProductsInCategoryItem [Default]
      {
            ProductName = 'No product in the given category'
       }
}
```


|  |
| --- |
| **Backlinks** |
| [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082) | [Toc:Data Provider language](https://wiki.genexus.com/commwiki/wiki?5309) |

---
