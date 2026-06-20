---
title: "Insert function in Transactions"
source_id: 8326
source_url: https://wiki.genexus.com/commwiki/wiki?8326
genexus_version: "18"
---

# Insert function in Transactions

Returns True when the Transaction is being executed in Insert mode. Otherwise, it returns False.

### [Syntax](#Syntax)

[Any valid Transaction rule](https://wiki.genexus.com/commwiki/wiki?8213) if **Insert**;

**Type Returned:**  
Boolean (True or False)

### [Scope](#Scope)

**Objects:**[Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,)

### [Description](#Description)

The Insert function allows conditioning the triggering of a rule defined in a [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,) so that the rule is executed only if the end user performs an insertion.

### [Samples](#Samples)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,)s:

```
Product
{
  ProductId*
  ProductDescription
  ProductStock
  ProductLastPurchasePrice //stores the price of the last completed order for ProductId
  ProductLastPurchaseDate  //stores the date of the last completed order for ProductId
}

Order
{ 
   OrderId*
   OrderDate
   ProductId
   ProductDescription        //inferred from the Extended Table
   ProductLastPurchasePrice  //inferred from the Extended Table
   ProductLastPurchaseDate   //inferred from the Extended Table
   OrderPrice
}
```

Rules defined within the Order Transaction:

```
ProductLastPurchasePrice = OrderPrice if Insert;
ProductLastPurchaseDate  = OrderDate  if Insert;
```

These assignments imply an update of attributes belonging to the extended table of the current level.

Therefore, every time a new Order **is inserted**, the Product table is updated.

**Note**: In the iSeries environment, when an error rule is defined as conditioned for a certain mode, the corresponding code to support this mode is not generated.

### [See Also](#See+Also)

[Update function](https://wiki.genexus.com/commwiki/wiki?8327)  
[Delete function](https://wiki.genexus.com/commwiki/wiki?8328)


|  |
| --- |
| **Backlinks** |
| [After function](https://wiki.genexus.com/commwiki/wiki?8321) | [Delete function in Transactions](https://wiki.genexus.com/commwiki/wiki?8328) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |
| [Update function in Transactions](https://wiki.genexus.com/commwiki/wiki?8327) |

---
