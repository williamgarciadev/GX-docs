---
title: "Business Component RemoveByKey method"
source_id: 31847
source_url: https://wiki.genexus.com/commwiki/wiki?31847
genexus_version: "18"
---

# Business Component RemoveByKey method

Removes a record that corresponds to a "line" of a variable based on a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) type of a two-[level](https://wiki.genexus.com/commwiki/wiki?42569) [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) by specifying its key.

First, all the structure must be loaded in memory by using the [Load method](https://wiki.genexus.com/commwiki/wiki?23211), and after that, the **RemoveByKey** method can be used to remove the desired "line" by specifying the second level identifier.

### [Samples](#Samples)

Suppose you define the following two-level Transaction as a Business Component (by setting its [Business Component property](https://wiki.genexus.com/commwiki/wiki?9548) = True):

```
Attraction
{
   AttractionId*
   AttractionName
   CategoryId
   CategoryName
   CountryId
   CountryName
   CityId
   CityName

   Ticket
   {
      AttractionTicketId*
      AttractionTicketDescription
      AttractionTicketPrice
   }
}
```

If you need to delete for the AttractionId = 6 the line whose AttractionTicketId=3, you can do so by defining this code for example in the Source of a Procedure or in the Events of an object:

```
&Attraction.Load(6)
&Success = &Attraction.Ticket.RemoveByKey(3)    //&Success: Boolean
&Attraction.Save()
If &Attraction.Success()
   commit
else
   rollback
endif
```

Variables:

```
&Attraction: based on BC Attraction. 
&AttractionTicket: based on BC  Attraction.Ticket.
```

### [Availability](#Availability)

This method is available since [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,).

For [Apple](https://wiki.genexus.com/commwiki/wiki?14917) is available since [GeneXus 15 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?32886,,).

**Note**: This method also applies to a collection of "headers". That is to say, it applies to a collection of Business Components in order to remove a header.


|  |
| --- |
| **Backlinks** |
| [Toc:Business Component](https://wiki.genexus.com/commwiki/wiki?5846) | [Business Component samples](https://wiki.genexus.com/commwiki/wiki?2278) |
|

---
