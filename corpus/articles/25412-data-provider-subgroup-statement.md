---
title: "Data Provider Subgroup statement"
source_id: 25412
source_url: https://wiki.genexus.com/commwiki/wiki?25412
genexus_version: "18"
---

# Data Provider Subgroup statement

It is one of the components of the [Data Provider output-based declarative language](https://wiki.genexus.com/commwiki/wiki?5309). A subgroup is the declarative equivalent of a [subroutine](https://wiki.genexus.com/commwiki/wiki?24767) in a procedural language. Once declared, could be invoked instead of an [element statement](https://wiki.genexus.com/commwiki/wiki?25103)  by means of a Subgroup element insertion.

## [Syntax](#Syntax+)

```
subgroup <subgroupName>([<parm1>,…,<parmN>])
          <mainGroupList>
endsubgroup
```

View [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626)

**Where:**

*subgroupName*  
          It is the name of the subgroup.

*parm1*, …, *parmN*   
          It is a list of variables that will be used as a parameter for the subgroup.

*mainGroupList*  
          Is a list of subsequent [Group statements](https://wiki.genexus.com/commwiki/wiki?25082).

**Note**: The subgroups should be defined all together at the end of the Data Provider source, that is: after all the [Group statements](https://wiki.genexus.com/commwiki/wiki?25082).

### [Samples](#Samples)

```
Customers
{
   Customer
   {
      Code = CustomerId
      Name = CustomerName
      AddressGroup.Insert(CustomerAddress, CityName)
   }
}

SubGroup AddressGroup(&Street, &City)
Address 
{ 
   Street = &Street
   City = &City 
}
EndSubGroup
```

A Subgroup can be internal (like this one) or external (defined as another Data Provider). For example, if you have an 'Address' SDT with Street and City as its members, and a Data Provider 'GetAddress' :

```
Output: Address
Collection: False
Rules: parm( &Street, &City );
```

```
Address
{
    Street = &street
    City = &city 
}
```

You can declare the previous 'GetCustomers' Data Provider like:

```
Customers
{
    Customer
    {
         Code = CustomerId
         Name = CustomerName
         Address = GetAddress( CustomerAddress, CityName )
    }
}
```

The Address member of the 'Customer' output SDT must have the 'Address' SDT data type (the output of 'GetAddress'). Otherwise, an error will appear.  
  
Note the difference between 'inserting' a subgroup and 'assigning' an element calling a Data Provider.  
  
One interesting use of this is the [recursive one](https://wiki.genexus.com/commwiki/wiki?4891).

####


|  |
| --- |
| **Backlinks** |
| [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082) | [Toc:Data Provider language](https://wiki.genexus.com/commwiki/wiki?5309) |

---
