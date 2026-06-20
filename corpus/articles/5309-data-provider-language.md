---
title: "Data Provider language"
source_id: 5309
source_url: https://wiki.genexus.com/commwiki/wiki?5309
genexus_version: "18"
---

# Data Provider language

The language used in [Data Providers](https://wiki.genexus.com/commwiki/wiki?5270) can be defined as output-based declarative language. It has three main components: **Groups**, **Elements**, and **Variables**. For example:

```
Customers    // this is a Group
{
   &StartTime = now()  // this is a Variable
   Customer  // this is a Group
   {
      Code = CustomerId    // this is an Element
      Name = CustomerName  // this is an Element
   }
}
```

'Customers' and 'Customer' are Groups, 'Code' and 'Name' are Elements, and '&StartTime' is a variable.

This example follows the syntax conventions of the three components of Data Providers: [Groups](https://wiki.genexus.com/commwiki/wiki?25082), [Subgroups](https://wiki.genexus.com/commwiki/wiki?25412), [Variables](https://wiki.genexus.com/commwiki/wiki?25413) and [Elements](https://wiki.genexus.com/commwiki/wiki?25103).

Remember that the output will be hierarchical data, loaded in an [SDT](https://wiki.genexus.com/commwiki/wiki?10021) or [BC](https://wiki.genexus.com/commwiki/wiki?5846) that is specified in the [Output property](https://wiki.genexus.com/commwiki/wiki?41037). The hierarchical structure that is obtained with the names of groups and elements must exactly match this structure.


* [Group](https://wiki.genexus.com/commwiki/wiki?25082)
* [Element](https://wiki.genexus.com/commwiki/wiki?25096)
* [Element statement](https://wiki.genexus.com/commwiki/wiki?25103)
* [Variable](https://wiki.genexus.com/commwiki/wiki?25413)
* [Subgroup](https://wiki.genexus.com/commwiki/wiki?25412)
* Advanced Group options
  + [Default clause](https://wiki.genexus.com/commwiki/wiki?25407)
  + [Paging clauses](https://wiki.genexus.com/commwiki/wiki?25410)
  + [NoOutput clause](https://wiki.genexus.com/commwiki/wiki?25408)
  + [OutputIfDetail clause](https://wiki.genexus.com/commwiki/wiki?25409)
  + [Input clause](https://wiki.genexus.com/commwiki/wiki?25406)
  + [One clause](https://wiki.genexus.com/commwiki/wiki?25411)

### 

####

---
