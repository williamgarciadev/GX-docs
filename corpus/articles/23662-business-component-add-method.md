---
title: "Business Component Add method"
source_id: 23662
source_url: https://wiki.genexus.com/commwiki/wiki?23662
genexus_version: "18"
---

# Business Component Add method

Adds a new item set as a parameter to a variable based on a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) collection.

### [Syntax](#Syntax)

*&varBasedOnBCCollection***.add(***&varBasedOnBC***)**

**Where:**  
*&varBasedOnBCCollection*  
    Is a variable based on a Business Component that is a collection.

*&varBasedOnBC*  
    Is a variable based on the same data type of the collection but corresponds to only one instance.

### [Samples](#Samples)

Consider the following two-level [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) set as a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846):

```
Attraction
{ 
   AttractionId*       (Autonumber property = Yes)
   AttractionName
   CategoryId
   CategoryName
   CountryId
   CountryName
   CityId
   CityName
   AttractionLastTicketId
   Ticket
   {
      AttractionTicketId*
      AttractionTicketDescription
      AttractionTicketPrice
   }
}
```

that contains the following defined rule:

```
Serial(AttractionTicketId,AttractionLastTicketId,1);
```

Suppose you need to add a new ticket to the attraction whose AttractionName = Eiffel Tower.

To do so, define in a certain object (for example in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916), [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) or a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293)):

* An &Attraction variable based on the Attraction data type.
* An &AttractionTicket variable based on the Attraction.Ticket data type.

After that, in the context you are positioned (for example, in the Events section of a Panel object or in a Procedure source) write the following code:

```
&Id = Find(AttractionId,AttractionName="Eiffel Tower",0) 
&Attraction.Load(&Id)
&AttractionTicket = new()
&AttractionTicket.AttractionTicketDescription = "Vip"
&AttractionTicket.AttractionTicketPrice = 200
&Attraction.Ticket.Add(&AttractionTicket)
&Attraction.Save() 
If &Attraction.Success()
   Commit     
else
   Rollback
endif
```

Read the article titled [Business Component InsertOrUpdate method](https://wiki.genexus.com/commwiki/wiki?31697) that presents another way to meet the same need.

### [See Also](#See+Also)

[Business Components Methods](https://wiki.genexus.com/commwiki/wiki?2277)


|  |
| --- |
| **Backlinks** |
| [Toc:Business Component](https://wiki.genexus.com/commwiki/wiki?5846) | [Business Component samples](https://wiki.genexus.com/commwiki/wiki?2278) |

---
