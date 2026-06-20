---
title: "Add rule"
source_id: 6845
source_url: https://wiki.genexus.com/commwiki/wiki?6845
genexus_version: "18"
---

# Add rule

Adds the value of one attribute to the value of another attribute, if you are inserting.  
Subtracts the value of one attribute to the value of another attribute, if you are deleting.  
Calculates the difference between the new and old value of the attribute you update and that difference is added to another attribute if you are updating.

### [Syntax](#Syntax)

**Add(**att1 , att2**)** [ if *cond* ] ;  
  
In mode:

* **Insert:** the value of the att1 attribute is added to the value of the att1 attribute (if the specified condition is true).
* **Delete:** the value of the att1 attribute is subtracted from the value of the att2 attribute (if the specified condition is true).
* **Update:** the difference between the new and old value of the att1 attribute is added to the value of the att2 attribute (if the specified condition is true).

### [Samples](#Samples)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s:

```
Customer                              Trip                           Country   
{                                     {                              { 
    CustomerId*                          TripId*                       CountryId*
    CustomerName                         TripDate                      CountryName
    CustomerLastName                     CountryId                     City
    CustomerPhone                        CountryName                   {
    CustomerTotalMiles                   CityId                          CityId*
    Trip                                 CityName                        CityName
    {                                    TripMiles                     } 
      TripId*                          }
      TripDate                                                       }
      CountryId
      CountryName
      CityId
      CityName
      TripMiles
    }
}
```

Suppose that a customer makes several trips and accumulates miles.  
  
To implement the customer’s mileage accumulation, you define the following rule in the Customer Transaction:

```
Add(TripMiles, CustomerTotalMiles);
```

The following behavior is incorporated into the Add rule:

* If a new trip is added for the customer, the value of TripMiles is added to CustomerTotalMiles.
* If a trip is deleted from the customer, the value of TripMiles is subtracted from CustomerTotalMiles.
* If the value of TripMiles associated with a customer’s trip is changed, its configured value is automatically subtracted and the new value is added to the customer’s total miles.

### [See Also](#See+Also)

[Subtract rule](https://wiki.genexus.com/commwiki/wiki?6860)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [Level associated to a Transaction rule](https://wiki.genexus.com/commwiki/wiki?23108) | [Subtract rule](https://wiki.genexus.com/commwiki/wiki?6860) |
| [Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213) |

---
