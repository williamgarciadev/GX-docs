---
title: "Business Component Update method"
source_id: 31696
source_url: https://wiki.genexus.com/commwiki/wiki?31696
genexus_version: "18"
---

# Business Component Update method

Updates the content assigned to a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) variable into the database. You must have previously assigned the desired data to the variable.

### [Syntax](#Syntax)

***&**VarBasedOnBC*.**Update()**

**Where:**  
*&VarBasedOnBC*  
     Is a scalar or collection variable based on a Business Component.

**Type returned:**  
Boolean

### [Description](#Description)

When the Update method is executed, the database will be updated only if the referential integrity doesn't fail and if error rules don't occur.  
The method always returns a boolean value that informs whether the Update could be executed successfully or not. This boolean value can be evaluated if you want to.

### [Samples](#Samples)

Suppose you define the following Transaction as Business Component (by setting its [Business Component property](https://wiki.genexus.com/commwiki/wiki?9548) = True):

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

Thus, a Business Component data type of the Customer Transaction is automatically created in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) and you can define a variable of the new type created in any object. So, in any object, you can define a variable named &Customer based on the Customer type.

**1)** The following code (defined for example in a [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664) or inside an Event in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)) is updating a customer:

```
 &Customer = new() 
 &Customer.CustomerId = 8
 &Customer.CustomerEmail = 'marybrown@gmail.com'
 &Customer.Update()
 if &Customer.Success()
    commit
 else
    msg(&Customer.GetMessages().ToJson())
 endif
```

**2)** The following code (defined for example in a Procedure Source or inside an Event in a Web Panel) is updating a customer. It is almost equal to the previous example with the only variant that the result of applying the Update method is directly evaluated with an if sentence:

```
 &Customer = new() 
 &Customer.CustomerId = 8
 &Customer.CustomerEmail = 'marybrown@gmail.com'
 if &Customer.Update()
    commit
  else
    msg(&Customer.GetMessages().ToJson())
  endif
```

**3)** The following Procedure is called from several objects. It receives a &Customer variable based on the Customer type and it only has to update the database:

```
Procedure: UpdateCustomer
   Rules
      parm(in:&Customer)
   Source
      &Customer.Update()
      if &Customer.Success()
         commit
      else
         msg(&Customer.GetMessages().ToJson())
      endif
```

**4)** Now, suppose you define the following Transaction as Business Component (by setting its [Business Component property](https://wiki.genexus.com/commwiki/wiki?9548) = True):

```
Product
{
  ProductId*     
  ProductName
  ProductStock
}
```

So, a Business Component data type of the Product Transaction is automatically created in the Knowledge Base and you can define a variable of the new type created in any object (and it can be set as a collection).

Thus, in a certain object, a variable named &Products is defined based on the Product type and it is set as a collection. The DPProducts Data Provider loads the &Products variable (for example inside an Event). Once the &Products variable is loaded, the Update method is applied to it as follows:

```
&Products=DPProducts()
&Products.Update()
if &Products.success()
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
    ProductStock = 5000
}
Product
{ 
   ProductId = 101
   ProductStock = 6000
}
```

In conclusion, a collection of products is loaded and after that, the Update method is applied to the collection variable. Each product in the collection will be updated.

**If there's an error in a BC from the list, are the following BCs processed?**   
Yes, all elements in the list are processed whether an error occurs or not. Then, it's up to you to commit the changes depending on the errors.

If you want to know which BCs had an error, you have to scan the list and check each one; for example, after applying the Updatemethod, you may write the following code:

```
For &Product in &Products
    if &Product.GetMessages().Count > 0
       //msg(...)
    endif
endfor
```

### Availability

This method is available since [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,).

### See Also

[Differences between the Save method and the Update method](https://wiki.genexus.com/commwiki/wiki?31703)  
[Error handling in Business Components](https://wiki.genexus.com/commwiki/wiki?2279)


|  |
| --- |
| **Backlinks** |
| [API object - Update service definition and declaration](https://wiki.genexus.com/commwiki/wiki?49780) | [Toc:Business Component](https://wiki.genexus.com/commwiki/wiki?5846) | [Business Component samples](https://wiki.genexus.com/commwiki/wiki?2278) |
| [Business Components - Differences between the Save method and the Insert and Update methods](https://wiki.genexus.com/commwiki/wiki?31703) | [GAM - Full Control Permissions and inheritance](https://wiki.genexus.com/commwiki/wiki?17664) |

---
