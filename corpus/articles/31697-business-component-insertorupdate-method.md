---
title: "Business Component InsertOrUpdate method"
source_id: 31697
source_url: https://wiki.genexus.com/commwiki/wiki?31697
genexus_version: "18"
---

# Business Component InsertOrUpdate method

Performs an “upsert” operation. An addition will be attempted, but if it fails because a duplicate key error is triggered, an update will be performed.

### [Syntax](#Syntax)

**&***VarBasedOnBC*.**InsertOrUpdate()**

**Where:**  
*&VarBasedOnBC*  
     Is a scalar or collection variable based on a Business Component.

**Type returned:**  
Boolean

### [Samples](#Samples)

**1)** Suppose you define the following [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) as a Business Component (by setting its [Business Component property](https://wiki.genexus.com/commwiki/wiki?9548) = True):

```
Customer
{
  CustomerId*     
  CustomerName
  CustomerAddress
  CustomerPhone
  CustomerEmail
  CustomerAddedDate
}
```

A Business Component data type of the Customer Transaction is automatically created in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) and you can define a variable of the new type created in any object.

Thus, the following [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) receives a &Customer variable based on the Customer type. In its source, the **InsertOrUpdate**method is applied to the variable to try to Insert the customer or Update it if the addition fails because a duplicate key error is triggered, that is, the typical 'Record already exists' error message.

```
Procedure: InsertOrUpdateCustomer
   Rules
      parm(in:&Customer)
   Source
      &Customer.InsertOrUpdate()
      if &Customer.success()
         commit
      else
         rollback
      endif
```

**2)** Consider the following Transaction defined as a Business Component (by setting its [Business Component property](https://wiki.genexus.com/commwiki/wiki?9548)  = True):

```
Product
{
  ProductId*     
  ProductName
  ProductStock
}
```

A Business Component data type of the Product Transaction is automatically created in the Knowledge Base and you can define a variable of the new type created in any object.

You can define a variable named &Products based on the Product data type and set it as a collection in any object.

The objective of this example is to assign to the &Products variable a collection of products (returned by a [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270)) and, after that, apply the **InsertOrUpdate** method to the &Products variable. Therefore, each insertion will be attempted and if some product of the collection already exists, it will be updated.

To achieve this, write the following code in the corresponding object section (Web Panel object Events, Panel object Events, Procedure object Source, etc.):

```
&Products=DPProducts()
if &Products.InsertOrUpdate()
    commit    
else
    rollback
endif
```

The DPProducts [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) definition is as follows:

```
Data Provider: DPProducts
Properties: Output:Product / Collection:True
   
Source:
Product
{
   ProductId = 100
   ProductName = 'X Muscular Pain Medicine'
   ProductStock = 1000
}
Product
{ 
  ProductId = 101
  ProductName = 'J Headache Medicine'
  ProductStock = 1500
}
```

**3)** Now, consider the following two-level Transaction as Business Component (by setting its [Business Component property](https://wiki.genexus.com/commwiki/wiki?9548) = True):

```
Country
{
  CountryId*     
  CountryName
  CountryFlag 
  CountryPopulation 
  City
  {
   CityId*
   CityName
  }
}
```

A Business Component data type of the Country Transaction is automatically created in the Knowledge Base and you can define a variable of the new type created in any object.

You can define a variable named &Countries based on the Country data type and set it as a collection in any object. This variable will be loaded with a collection of countries (returned by a [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270)). After that, the **InsertOrUpdate** method will be applied to the variable. Each insertion will be attempted and if some country of the collection already exists, it will be updated.

Suppose that a record with CountryId=1 is already stored; its corresponding CountryName='Uruguay', its CountryPopulation=3300000, the CountryFlag has the corresponding stored image, and the following related cities are also stored:

1, 1, Montevideo  
1, 2, Maldonado  
1, 3, Colonia

Now, define a DPCountries Data Provider as shown:

```
Data Provider: DPCountries
Properties: Output:Country / Collection:True

Source:
Country
{
  CountryId = 1
  CountryPopulation = 3445863
  City
  {
    CityId = 4
    CityName = 'Salto'
  }
  City
  {
    CityId = 5
    CityName = 'Paysandu'
  }
}

Country
{ 
  CountryId = 2 
  CountryName = Argentina
  CountryFlag = ArgentinaFlag.Link()
  CountryPopulation = 43000000
  City
  { 
    CityId = 1
    CityName = 'Buenos Aires'
  }
  City
  { 
    CityId = 2
    CityName = 'Rosario'
  } 
  City
  {
    CityId = 3
    CityName = 'Cordoba'
  } 
}
```

After that, write the following code in the corresponding object section ([Web Panels events](https://wiki.genexus.com/commwiki/wiki?8178), [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) events, [Procedure object Source](https://wiki.genexus.com/commwiki/wiki?6664), etc.):

```
&Countries=DPCountries()
&Countries.InsertOrUpdate()
if &Countries.success()
    commit    
else
    rollback
endif
```

For the CountryId=1, the insertion will be attempted, but the CountryId=1 already exists. So, its CountryPopulation will be Updated and the CityId=4 and the CityId=5 will be added related to it. Besides, for the CountryId=2, the insertion will be attempted and it will be successful.

**If there's an error in a BC from the list, are the following BCs processed?**   
Yes, all elements in the list are processed whether an error occurs or not. Then, it's up to you to commit the changes.

To find out which BCs had an error, scan the list and check each one; for example, after applying the **InsertOrUpdate**method, you may write the following code:

```
For &Product in &Products
    if &Product.GetMessages().Count > 0
       //msg(...)
    endif
endfor
```

**Note**: if the primary key has its [Autonumber property](https://wiki.genexus.com/commwiki/wiki?6798) set to True, the method will always insert, since a duplicate key will never be detected (because a new identifier value is always generated).

### [Availability](#Availability)

This method is available since [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,).  
For 
[Apple](https://wiki.genexus.com/commwiki/wiki?14917) offline applications it is available since [GeneXus 15 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?32886,,).

### [See Also](#See+Also)

[Error handling in Business Components](https://wiki.genexus.com/commwiki/wiki?2279)


|  |
| --- |
| **Backlinks** |
| [Toc:Business Component](https://wiki.genexus.com/commwiki/wiki?5846) | [Business Component Add method](https://wiki.genexus.com/commwiki/wiki?23662) | [Business Component samples](https://wiki.genexus.com/commwiki/wiki?2278) |
| [Collection property](https://wiki.genexus.com/commwiki/wiki?41179) | [Output property](https://wiki.genexus.com/commwiki/wiki?41037) |

---
