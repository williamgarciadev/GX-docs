---
title: "Input clause"
source_id: 25406
source_url: https://wiki.genexus.com/commwiki/wiki?25406
genexus_version: "18"
---

# Input clause

Is used in a [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082) in order to the associated group could iterate N times, being N the number of elements taken from an **input** that is not a Database table, but a variable that assume multiple values.

Scanning these variable values, for each one, you will have a group item in the output. That is to say, for each iteration into the variable, you will have an iteration into the group. Thus, you can use the variable iteration information as an input for the group.

### [Syntax](#Syntax)

```
Input <forIter> | <forIn>
```

View [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626)

**Where:**

*ForIter*  
        It is like the For command to iterate. It is defined as follows: **&**var **=** *<numberFrom>*  **to**<numberTo>.

*ForIn*  
        It is like the [For in command](https://wiki.genexus.com/commwiki/wiki?6359). It is defined as follows: **&**var **in** *<SDTcollection>* .

### [Description](#Description)

It is usually necessary to have other kinds of Input data besides Database. For example, the output of some Procedure or Data Provider. The obvious way to work with that is through variables that, once assigned, can be treated as usual.

### [Samples](#Samples)

Suppose you need a Data Provider that outputs a collection of clients that live in the same neighborhood as the customer returned by another Data Provider. Then 'DPSpendsMoreClient' is an already declared Data Provider that returns **a customer SDT** with the country, city and neighborhood information of the higher spending customer in the Database.

```
Clients
{
   &Customer = DPSpendsMoreClient()
   Client 
      where CountryId = &Customer.CountryId
      where CityId = &Customer.CityId
      where CustomerNeighborhood = &Customer.Neighborhood
   {
      Name = CustomerName
      Address = CustomerAddress
      Phone = CustomerPhone
   }
}
```

As you can see, the &Customer was taken from another Data Provider and used as usual. But what if you need to work not with a simple data type, but with a collection returned by a Procedure or Data Provider? Or if you need to iterate at certain fixed times? The Input clause lets you work with these other cases.

The simpler one is just a **set of fixed values**, for example, a Data Provider that Outputs the months:

```
VerySimple
{
   Month Input &i = 1 to 12
   {
      MonthNumber = &i
   }
}
```

**Note:** this is similar to a For &i = 1 to 12 in the procedural language.

A more sophisticated Input can be another SDT **collection,** as follows:

```
CustomersFromAnotherDataProvider
{
   &CustomersSDT = GetCustomers() // a Data Provider that Outputs Customers collection
   Customer Input &Customer in &CustomersSDT
   {
      Id   = &Customer.Code
      Name = &Customer.Name
   }
}
```

In sum, any [collection variable](https://wiki.genexus.com/commwiki/wiki?6352) should be treated through the **Input clause** to achieve iteration.

For a summary of the different Input sources, read [Data Provider: Input](https://wiki.genexus.com/commwiki/wiki?6292).


|  |
| --- |
| **Backlinks** |
| [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082) | [Toc:Data Provider language](https://wiki.genexus.com/commwiki/wiki?5309) |

---
