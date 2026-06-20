---
title: "Subtract rule"
source_id: 6860
source_url: https://wiki.genexus.com/commwiki/wiki?6860
genexus_version: "18"
---

# Subtract rule

Subtracts the value of one attribute to the value of another attribute when inserting.  
Adds the value of one attribute to the value of another attribute when deleting.  
Calculates the difference between the new and old value of the attribute you update and that difference is subtracted from another attribute when updating.

### [Syntax](#Syntax)

**Subtract(**att1 , att2**)** [ if *cond* ] ;

In mode:

* **Insert:** the value of the att1 attribute is subtracted from the value of the att2 attribute (if the specified condition is true)
* **Delete:** the value of the att1 attribute is added to the value of the att2 attribute (if the specified condition is true)
* **Update:** the difference between the new and old value of the att1 attribute is subtracted from the value of the att2 attribute (if the specified condition is true)

### [Samples](#Samples)

Look at the following example:

```
Customer                              Trip                      Prize                    Country  
{                                     {                         {                        {
    CustomerId*                          TripId*                  PrizeId*                  CountryId*
    CustomerName                         TripDate                 PrizeDate                 CountryName
    CustomerLastName                     CountryId                PrizeDescription          City
    CustomerPhone                        CountryName              PrizeMiles                {
    CustomerTotalMiles                   CityId                   CustomerId                  CityId*
    Trip                                 CityName                 CustomerName                CityName
    {                                    TripMiles                CustomerTotalMiles        }
      TripId*                          }                        }                         }
      TripDate                                                                     
      CountryId
      CountryName
      CityId
      CityName
      TripMiles
    }
}
```

The Prize Transaction allows defining rewards to be traded for miles.

Each prize requires a number of miles to be assigned to a customer who has accrued that number of miles (or who has an even larger number of miles). Therefore, when trying to assign one customer to one prize, you must check if the customer has enough miles to be able to assign this prize. If the customer has enough miles and accepts the prize, you must subtract the traded miles. If the customer doesn’t have enough miles, you need to show an error message.

In the Prize transaction the two following rules were defined:

```
Subtract(PrizeMiles, CustomerTotalMiles);
Error(“Customer doesn’t have enough miles accrued”) if CustomerTotalMiles < 0;
```

The following behavior is provided by Subtract rule:

* If a new prize is inserted, the value of PrizeMiles is subtracted from CustomerTotalMiles.
* If a prize is deleted, the value of PrizeMiles is added to CustomerTotalMiles.
* If the value of PrizeMiles is changed, its old value is automatically added to the customer’s total miles and the new value is subtracted from the customer’s total miles.

Since the Subtract and Error rules involve the CustomerTotalMiles attribute and one of the rules updates the attribute while the other one assesses its value, GeneXus determines that first, it must make the subtraction that updates the CustomerTotalMiles attribute and after that, it evaluates what happened with its value.

As the subtraction is made first, if the customer has fewer miles than those required by the reward, the CustomerTotalMiles attributes will have a negative value. For this reason, the Error rule evaluates if CustomerTotalMiles<0. If this happens, the Error rule is triggered, the error message is displayed and the subtract rule is undone; that is to say, its execution is reverted as if nothing was done and the customer’s total number of miles is not modified.

If CustomerTotalMiles doesn’t have a negative value (CustomerTotalMiles<0) after making the subtraction, it means that the subtract operation has been performed.

Note that if the record of a prize assigned to the customer is deleted, the subtract rule adds instead of subtracting. That is to say, it adds the number of miles corresponding to the reward (PrizeMiles), to the total number of miles accrued by the customer (CustomerTotalMiles).

### [See Also](#See+Also)

[Add rule](https://wiki.genexus.com/commwiki/wiki?6845)


|  |
| --- |
| **Backlinks** |
| [Add rule](https://wiki.genexus.com/commwiki/wiki?6845) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213) |

---
