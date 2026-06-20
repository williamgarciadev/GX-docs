---
title: "Business Component Save method"
source_id: 23229
source_url: https://wiki.genexus.com/commwiki/wiki?23229
genexus_version: "18"
---

# Business Component Save method

Executes something equivalent to what happens when the user presses the confirm button in a [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) Form.

### [Syntax](#Syntax)

**&***VarBasedOnBC*.**Save()**

**Where:**  
*&VarBasedOnBC*  
     Is a variable defined in a GeneXus object, based on a Business Component.

### [Description](#Description)

As this method is applied to a variable based on a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846), the formulas and rules defined in the Transaction are triggered and the referential integrity is checked, before saving physically the involved data.

It can be used to insert and update physically.

GeneXus understands the Save method is used to insert if you assign values to the [properties of a variable](https://wiki.genexus.com/commwiki/wiki?2276) based on a Business Component and execute the Save method to the variable, but you haven't instantiated data in memory previously by using the [Load method](https://wiki.genexus.com/commwiki/wiki?23211).

On the other hand, if you apply the Load method to the Business Component variable to instantiate certain data in memory first, and you assign values to the properties of the Business Component variable and save after that, GeneXus understands you are updating the data you have loaded as a first step.

It's essential to know that the Save method is only valid to be applied to Business Component variables of the Transaction first [level](https://wiki.genexus.com/commwiki/wiki?42569). This is easy to be understood since the behavior is the same, as the Confirm button offers in a Transaction Form: when it is pressed, it saves all the data present in the form (belonging to all the Transaction levels).

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
```

Customer rule:

```
Default(CustomerAddedDate,&today);
```

Thus, a Business Component data type of the Customer Transaction is automatically created in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) and you are able to define in any object, a variable of the new type created. So, in any object define a variable named &Customer based on the Customer type.

**1)** The following code (defined for example in a [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664) or inside an event in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)) is inserting a customer:

```
  &Customer.CustomerName = 'Mary'
  &Customer.CustomerLastName = 'Brown'
  &Customer.CustomerAddress = '767 5th Avenue'
  &Customer.CustomerEmail = 'mbrown@gmail.com'
  &Customer.save()
  if &Customer.success()
     commit
  else
     rollback
  endif
```

**2)** The following code (defined for example in a Procedure Source or inside an event in a Web Panel) is updating a customer:

```
  &Customer.Load(8)
  &Customer.CustomerEmail = 'marybrown@gmail.com'
  &Customer.save()
  if &Customer.success()
     commit
  else
     rollback
  endif
```

### [See Also](#See+Also)

[Error handling in Business Components](https://wiki.genexus.com/commwiki/wiki?2279)


|  |
| --- |
| **Backlinks** |
| [Toc:Business Component](https://wiki.genexus.com/commwiki/wiki?5846) | [Business Component - Publication as Web Service](https://wiki.genexus.com/commwiki/wiki?2282) | [Business Component Check method](https://wiki.genexus.com/commwiki/wiki?23401) |
| [Business Component Fail method](https://wiki.genexus.com/commwiki/wiki?23402) | [Business Component GetMessages method](https://wiki.genexus.com/commwiki/wiki?23475) | [Business Component Load method](https://wiki.genexus.com/commwiki/wiki?23211) | [Business Component Mode method](https://wiki.genexus.com/commwiki/wiki?23790) |
| [Business Component property](https://wiki.genexus.com/commwiki/wiki?9548) | [Business Component samples](https://wiki.genexus.com/commwiki/wiki?2278) | [Business Component Success method](https://wiki.genexus.com/commwiki/wiki?23404) | [Business Components - Differences between the Save method and the Insert and Update methods](https://wiki.genexus.com/commwiki/wiki?31703) |
| [Error handling in Business Components](https://wiki.genexus.com/commwiki/wiki?2279) | [Using Data Providers in Other GX Objects](https://wiki.genexus.com/commwiki/wiki?5310) |

---
