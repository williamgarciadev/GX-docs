---
title: "Business Component Insert method"
source_id: 31695
source_url: https://wiki.genexus.com/commwiki/wiki?31695
genexus_version: "18"
---

# Business Component Insert method

Inserts the content assigned to a Business Component variable into the database.

### [Syntax](#Syntax)

**&***VarBasedOnBC*.**Insert()**

**Where:**  
*&VarBasedOnBC*  
     Is a scalar or collection variable based on a Business Component.

**Type returned:**  
Boolean

### [Description](#Description)

When the Insert method is executed, the content assigned in the memory will be inserted, only if the referential integrity doesn't fail and if error rules don't occur.  
This method always returns a boolean value that informs whether the addition to the database could be executed successfully or not. You can evaluate this boolean value if you want to.

### [Samples](#Samples)

Consider the following Transaction as Business Component (by setting its [Business Component property](https://wiki.genexus.com/commwiki/wiki?9548) = True):

```
Customer
{
  CustomerId*     (Autonumber property = True)
  CustomerName
  CustomerAddress
  CustomerPhone
  CustomerEmail
  CustomerAddedDate
  CustomerTotalMiles
}

Customer rule: 
Default(CustomerAddedDate,&today);
```

Thus, a Business Component data type of the Customer Transaction is automatically created in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) and you can define a variable of the new type created in any object.

Assume you define a variable named &Customer, based on the Customer type, in any object.

**1)** The following code (defined for example in a [Procedure](https://wiki.genexus.com/commwiki/wiki?6293) Source or inside an Event in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)) is inserting a customer:

```
&Customer=new() //in this case the new operator can be omitted, but if more than one customer is inserted, it must be used
&Customer.CustomerName = 'Mary'
&Customer.CustomerLastName = 'Brown'
&Customer.CustomerAddress = '767 5th Avenue'
&Customer.CustomerEmail = 'mbrown@gmail.com'
&Customer.Insert()
if &Customer.Success()
   commit   
else   
   msg(&Customer.GetMessages().ToJson(), status)
endif
```

**2)**The following code (defined for example in a [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664) or inside an Event in a Web Panel) is inserting a customer. It is almost equal to the previous example, with the unique variant that the result of applying the Insert method is directly evaluated with an if sentence:

```
&Customer=new() //in this case the new operator can be omitted, but if more than one customer is inserted, it must be used
&Customer.CustomerName = 'Mary'
&Customer.CustomerLastName = 'Brown'
&Customer.CustomerAddress = '767 5th Avenue'
&Customer.CustomerEmail = 'mbrown@gmail.com'
if &Customer.Insert()
    commit    
else
    msg(&Customer.GetMessages().ToJson(), status)
endif
```

**3)**The following Procedure is called from several objects. It receives a &Customer variable based on the Customer type and it only has to perform the addition to the database:

```
Procedure: InsertCustomer
   Rules
      parm(in:&Customer)
   Source
      &Customer.Insert()
      if &Customer.Success()
         commit   
      else
         msg(&Customer.GetMessages().ToJson(), status)
      endif
```

**4)** Now, suppose you define the following Transaction as Business Component (by setting its [Business Component property](https://wiki.genexus.com/commwiki/wiki?9548) = True):

```
Product
{
  ProductId*     
  ProductName
  ProductStock
}
```

So, a Business Component data type of the Product Transaction is automatically created in the Knowledge Base and you can define a variable of the new type created in any object (and it can be set as a collection).

Thus, in a certain object, a variable named &Products is defined based on the Product type and it is set as a collection. The DPProducts Data Provider loads the &Products variable (for example inside an Event). Once the &Products variable is loaded, the Insert method is applied to it as follows:

```
&Products=DPProducts()
if &Products.Insert()
    Commit
else 
    msg(&Products.GetMessages().ToJson(), status) 
endif
```

Look at the DPProducts [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270) definition:

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

In conclusion, a collection of products is loaded and after that, the Insert method is applied to the collection variable. Each product in the collection will be inserted.

**If there's an error in a BC from the list, are the following BCs processed?**

Yes, all elements in the list are processed whether an error occurs or not. Then, it's up to you to commit the changes depending on the errors.

If you want to know which Business Components had an error, you have to scan the list and check each one; for example, after applying the Insert method, you may write the following code:

```
For &Product in &Products
    if &Product.GetMessages().Count > 0
       //msg(...)
    endif
endfor
```

### [Availability](#Availability)

This method is available since [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,).

### [See Also](#See+Also)

[Business Components - Differences between the Save method and the Insert and Update methods](https://wiki.genexus.com/commwiki/wiki?31703)  
[Error handling in Business Components](https://wiki.genexus.com/commwiki/wiki?2279)


|  |
| --- |
| **Backlinks** |
| [API object - Insert service definition and declaration](https://wiki.genexus.com/commwiki/wiki?49778) | [Toc:Business Component](https://wiki.genexus.com/commwiki/wiki?5846) | [Business Component property](https://wiki.genexus.com/commwiki/wiki?9548) |
| [Business Component samples](https://wiki.genexus.com/commwiki/wiki?2278) | [Business Components - Differences between the Save method and the Insert and Update methods](https://wiki.genexus.com/commwiki/wiki?31703) | [Collection property](https://wiki.genexus.com/commwiki/wiki?41179) | [GAM - Full Control Permissions and inheritance](https://wiki.genexus.com/commwiki/wiki?17664) |
| [Output property](https://wiki.genexus.com/commwiki/wiki?41037) |

---
