---
title: "Example: Data Provider Break"
source_id: 6043
source_url: https://wiki.genexus.com/commwiki/wiki?6043
genexus_version: "18"
---

# Example: Data Provider Break

Some [Data Provider](https://wiki.genexus.com/commwiki/wiki?5309) **groups** involve an access to the Database in order to retrieve information, and this may generate several entries in the output. GeneXus infers this in a similar way as it does in a For Each.

Let's see an example of the well-known Break . Suppose that we need to report the customers by country in our system. Suppose our Country and Customer transactions have the following structures:

```
Country                     Customer

CountryId*                  CustomerId*
CountryName                 CustomerName
                            CountryId
                            CountryName
                            CustomerAddress
                            ...
```

Regardless of the output, and assuming that it is not structured, the source of the procedure used to retrieve all customers grouped by country will be the following:

```
for each order CountryName
         defined by CustomerName
    Id = CountryId
    Name = CountryName
    for each
        CustomerId = CustomerId
        CustomerName = CustomerName
    endfor
endfor
```

In other words, it is a Break.

But what if the output is a structured one? We will need an SDT as the output, and its structure will look as follows:

`[imagen omitida: wiki id 6045]`

In order to insert the information inside the SDT, we will need to change the source of the previous procedure, by declaring a &countries variable of the 'Countries' SDT, a &country variable of the 'Countries.Country' SDT and a &customer variable of the 'Countries.Country.Customer' SDT:

```
for each order CountryName
         defined by CustomerName
    &country.Id = CountryId
    &country.Name = CountryName
    for each
        &customer.Id = CustomerId
        &customer.CustomerName = CustomerName
        &country.Customers.Add( &customer )
        &customer = new Countries.Country.Customer()
    endfor
    &countries.Add( &country )
    &country = new Countries.Country()
endfor
```

But what if we instead declare the following source of a Data Provider?

`[imagen omitida: wiki id 6046]`

Or if we omit the innermost group (the result is exactly the same):

`[imagen omitida: wiki id 6047]`

Much easier!

Note how the 'Country' group is just like a For Each whose base table is CUSTOMER (because of the 'Defined by'), and how the 'Customers' group is just like a for each over the CUSTOMER base table, thus implementing a Break! The navigation report will show exactly the same as in the Procedure code! Also, note how the CustomerName Element is not assigned because the attribute name is exactly the same (to refresh that idea read: [Data Providers Language Description: Elements](https://wiki.genexus.com/commwiki/wiki?5309)).


|  |
| --- |
| **Backlinks** |
| [Category:Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) |

---
