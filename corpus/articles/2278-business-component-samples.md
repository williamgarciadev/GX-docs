---
title: "Business Component samples"
source_id: 2278
source_url: https://wiki.genexus.com/commwiki/wiki?2278
genexus_version: "18"
---

# Business Component samples

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) defined as a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846):

`[imagen omitida: wiki id 50161]`

For all the following examples, you have to define an &Attraction variable based on the Attraction data type in a certain object (for example, in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916), [Panel object](https://wiki.genexus.com/commwiki/wiki?24829), or [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293)). After that, you can code the following samples in the corresponding object section (Web Panel object Events, Panel object Events, Procedure object Source, etc.).

### [1) Samples to Insert](#1%29+Samples+to+Insert)

Suppose you want to insert a new attraction.

**1.1)** To do so, you can use the [Business Component Save method](https://wiki.genexus.com/commwiki/wiki?23229) as shown below:

```
&Attraction.AttractionName = "Eiffel Tower"
&Attraction.CountryId = 2                    //France
&Attraction.CityId = 1                       //Paris
&Attraction.Save()
If &Attraction.Success()
  commit
  msg("The data has been added")
Else
  rollback
  msg(&Attraction.GetMessages().ToJson()) 
Endif
```

**Notes**

* The CategoryId was omitted, but since that foreign key allows nulls, the record will be inserted without failure.
* The AttractionId has its [Autonumber property](https://wiki.genexus.com/commwiki/wiki?6798) set to True, so it will be autonumbered by the database.
* After executing the Save() method, &Attraction.Mode() is set to Update ("UPD") and all attributes are instantiated.

**1.2)** You can use the [Business Component Insert method](https://wiki.genexus.com/commwiki/wiki?31695) as shown below:

```
    &Attraction.AttractionName = "Eiffel Tower"
    &Attraction.CategoryId = 2                 //Monument
    &Attraction.CountryId = 2                  //France
    &Attraction.CityId = 1                     //Paris
    &Attraction.Insert()
    If &Attraction.Success()
       Commit
       msg("The data has been added")
    Else
       rollback
       msg(&Attraction.GetMessages().ToJson()) 
    Endif
```

Read [Differences between the Save method and the Insert and Update methods](https://wiki.genexus.com/commwiki/wiki?31703).  
  
**1.3)** The following sample is almost the same as the previous one. The only difference is that the result of applying the Insert method is directly evaluated with an if sentence (so, the Success method is not used):

```
   &Attraction.AttractionName = "Eiffel Tower"
   &Attraction.CategoryId = 2                  //Monument
   &Attraction.CountryId = 2                   //France
   &Attraction.CityId = 1                      //Paris
   If &Attraction.Insert()
       Commit
       msg("The data has been added")
   Else
       rollback
       msg(&Attraction.GetMessages().ToJson()) 
   Endif
```

**1.4)** You can use a [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270).

To do so, create a Data Provider (for example, named DPOneAttraction). Drag the Attraction Transaction from the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) to the Data Provider Source and fill in the data as shown:

```
Attraction
{
    AttractionName = "Eiffel Tower"
    CategoryId = 2
    CountryId = 2
    CityId = 1
}
```

Next, call the Data Provider in the context you are positioned (for example, in the Events section of a Panel object or Web Panel object):

```
Event 'InsertAttraction'
    &Attraction = DPOneAttraction()
    If &Attraction.Insert()
        commit
        msg("The update has been successfully completed")
    Else
        rollback
        msg("Unable to insert")
    Endif
Endevent
```

**1.5)**  Now, suppose you want to insert several attractions. To do so, you can define a Data Provider (for example, named DPSeveralAttractions).

First, drag the Attraction Transaction from the KB Explorer to the Data Provider Source and fill in the data, as shown below:

`[imagen omitida: wiki id 50162]`

Note that the Data Provider [Output property](https://wiki.genexus.com/commwiki/wiki?41037) was filled automatically (with “Attraction”) because you dragged the Attraction Transaction to the source.

To indicate that you want to return several attractions, set the [Collection property](https://wiki.genexus.com/commwiki/wiki?41179) to True.

After defining the Data Provider, define a variable (for example, named &Attractions) in an object (for example, in a Panel, Web Panel, or Procedure) and set it as a collection by selecting the “Is Collection” checkbox, as shown in the image below:

`[imagen omitida: wiki id 50163]`

Next, call the Data Provider in the context you are positioned (for example, in the Events section of a Panel object or Web Panel object) and complete the code as shown below:

```
Event 'InsertAttractions'
    &Attractions = DPSeveralAttractions()
    If &Attractions.Insert()
        commit
        msg("The data has been added")
    Else
        rollback
        msg("Unable to insert")
    Endif
Endevent
```

Note that you load the attractions data inside the Data Provider and then call the Data Provider that returns the data in a variable set as a collection. Finally,  the data is inserted into the database.

**1.6)** Now, consider the following two-level Transaction set as [Business Component](https://wiki.genexus.com/commwiki/wiki?5846):

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
   Ticket
   {
      AttractionTicketId*
      AttractionTicketDescription
      AttractionTicketPrice
   }
}
```

Its first level exactly matches the Attraction [Transaction Structure](https://wiki.genexus.com/commwiki/wiki?7661) used for the above examples. Also, it contains a nested level.

Suppose you want to insert a new attraction with two lines (two tickets).

To do so, create a Data Provider (for example, named DPAttractionWithTickets).

Next, drag the Attraction Transaction from the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) to the Data Provider Source and fill in the data as shown:

```
Attraction
{
   AttractionName = "Eiffel Tower"
   CategoryId = 2
   CountryId = 2
   CityId = 1
   Ticket
   {
      AttractionTicketId = 1
      AttractionTicketDescription = "Popular"
      AttractionTicketPrice = 100 
   }
   Ticket
   { 
      AttractionTicketId = 2
      AttractionTicketDescription = "Vip"
      AttractionTicketPrice = 300 
   }
}
```

The Data Provider [Output property](https://wiki.genexus.com/commwiki/wiki?41037) will be filled automatically with the “Attraction” value because you dragged the Attraction Transaction to its source.

After defining the Data Provider, define a variable (for example, named &AttractionWithTickets) in an object (for example, in a Panel, Web Panel, or Procedure) based on the Attraction Business Component data type. Finally, call the Data Provider in the context you are positioned (for example, in the Events section of a Panel object or Web Panel object) and complete the code as shown below:

```
Event 'InsertAttractionWithTickets'
    &AttractionWithTickets = DPAttractionWithTickets()
    If &AttractionWithTickets.Insert()
        commit
        msg("The data has been added")
    Else
        rollback
        msg("Unable to insert")
    Endif
Endevent
```

Note that you load the attraction with two tickets' data inside the Data Provider and then call the Data Provider that returns the data in a variable. Finally, the data is inserted into the database.

### [2) Samples to Update](#2%29+Samples+to+Update)

Suppose you need to update certain attraction data (for example, its category).

**2.1)**You can use the [Business Component Save method](https://wiki.genexus.com/commwiki/wiki?23229) as shown in the code below:

```
   &Attraction.Load(1)
   &Attraction.CategoryId = 1      //Monument
   &Customer.Save()
   If &Attraction.Success()
      commit
      msg("The data has been updated")
   Else 
      rollback
      msg(&Attraction.GetMessages().ToJson()) 
   Endif
```

**2.2)** You can use the [Business Component Update method](https://wiki.genexus.com/commwiki/wiki?31696) as shown below:

```
&Attraction = new()
&Attraction.AttractionId = 20
&Attraction.CategoryId = 2     //Monument
If &Attraction.Update()
   Commit
   msg("The update has been successfully completed")
Else
   rollback
   msg(&Attraction.GetMessages().ToJson())
Endif
```

Read [Differences between the Save method and the Insert and Update methods](https://wiki.genexus.com/commwiki/wiki?31703).

**2.3)**You can use a [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270).

To do so, create a Data Provider (for example, named DPOneAttraction). Drag the Attraction Transaction from the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) to the Data Provider Source and fill in the data as shown:

```
Attraction
{
    AttractionId = 1 
    CategoryId = 1
}
```

After that, call the Data Provider in the context you are positioned (for example, in the Events section of a Panel object or Web Panel object):

```
Event 'UpdateAttraction'
    &Attraction = DPOneAttraction()
    If &Attraction.Update()
        commit
        msg("The update has been successfully completed")
    Else
        rollback
        msg(&Attraction.GetMessages().ToJson())
    Endif
Endevent
```

**2.4)**Now, suppose you want to update several attractions. To do so, you can define a Data Provider (for example, named DPSeveralAttractions).

Drag the Attraction Transaction from the KB Explorer to the Data Provider Source and fill in the data as shown below:

`[imagen omitida: wiki id 50168]`

Note that the Data Provider [Output property](https://wiki.genexus.com/commwiki/wiki?41037) was filled automatically (with “Attraction”) because you dragged the Attraction Transaction to the source.

To indicate that you want to return several attractions, set the [Collection property](https://wiki.genexus.com/commwiki/wiki?41179) to True.

After defining the Data Provider, define a variable (for example, named &Attractions) in an object (for example, in a Panel, Web Panel, or Procedure) and set it as a collection by selecting the “Is Collection” checkbox, as shown in the image below:

`[imagen omitida: wiki id 50163]`

Next, call the Data Provider in the context you are positioned (for example, in the Events section of a Panel object or Web Panel object) and complete the code as shown below:

```
Event 'UpdateAttractions'
    &Attractions = DPSeveralAttractions()
    If &Attractions.Update()
        commit
        msg("The data has been updated")
    Else
        rollback
        msg("Unable to update")
    Endif
Endevent
```

Note that you load the attractions data inside the Data Provider and then call the Data Provider that returns the data in a variable set as a collection. Finally, the data is updated in the database.

### [3) Samples to Delete](#3%29+Samples+to+Delete)

**3.1)**To delete an attraction—for example, the Attraction with ID 1—use the [Business Component Delete method](https://wiki.genexus.com/commwiki/wiki?23238) as shown below:

```
   &Attraction.Load(1)
   &Attraction.Delete()
   If &Attraction.success()
      commit
      msg("The update has been successfully completed")
   Else 
      rollback 
      msg(&Attraction.GetMessages().ToJson()) 
   Endif
```

**3.2)**To delete several attractions—for example, all the monuments (attractions with CategoryId=2)—scan the desired attractions using the [For Each command](https://wiki.genexus.com/commwiki/wiki?24744). Next, inside the loop load each attraction and delete it as shown:

```
   For each Attraction
       where CategoryId = 2
             &Attraction.Load(AttractionId)
             &Attraction.Delete()
             If &Attraction.success()
                commit
             Else 
                rollback 
             Endif    
   Endfor
```

### [4) Samples to Insert or Update](#4%29+Samples+to+Insert+or+Update)

Read the article titled [Business Component InsertOrUpdate method](https://wiki.genexus.com/commwiki/wiki?31697) that describes several examples.

### 

### [5) Samples to Insert an Attraction line](#5%29+Samples+to+Insert+an+Attraction+line)

Read the article titled [Business Component Add method](https://wiki.genexus.com/commwiki/wiki?23662) that describes an example to solve it.

### [6) Samples to Update an Attraction line](#6%29+Samples+to+Update+an+Attraction+line)

Consider the following two-level Transaction set as [Business Component](https://wiki.genexus.com/commwiki/wiki?5846):

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

**6.1)** Suppose you need to update for the AttractionId = 6 its AttractionTicketId=3 with a different price.

Read the article titled [Business Component GetByKey method](https://wiki.genexus.com/commwiki/wiki?31846) article that solves this case.

**6.2)** Considering the same two-level Transaction set as Business Component, suppose that for AttractionId = 6 you need to update the price of the ticket with description="Without tour guide".

To achieve this, the code is as follows:

```
  &Attraction.Load(6)
  For &Ticket in &Attraction.Ticket
      If &Ticket.AttractionTicketDescription="Without tour guide"
          &Ticket.AttractionTicketPrice=100
      Endif
  Endfor
  &Attraction.Save()
  If &Attraction.success()
     commit
     msg("The update has been successfully completed")
  Else
     rollback
     msg(&Attraction.GetMessages().ToJson())
  Endif
```

### [7) Samples to Delete an Attraction line](#7%29+Samples+to+Delete+an+Attraction+line)

Consider the following two-level Transaction set as [Business Component](https://wiki.genexus.com/commwiki/wiki?5846):

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

**7.1)**Suppose that for AttractionId = 6 you need to delete the line with AttractionTicketId=3.

Read the article titled [Business Component RemoveByKey method](https://wiki.genexus.com/commwiki/wiki?31847) that solves this case.

**7.2)**Considering the same two-level Transaction set as Business Component, suppose you need to delete the first Ticket of the AttractionId = 6, regardless of the AttractionTicketId value.

To achieve this, the code is as follows:

```
  &Attraction.Load(6)
  &Attraction.Ticket.Remove(1)
  &Attraction.Save()
  If &Attraction.success()
     commit
     msg("The line deletion has been successfully completed")
  Else
     rollback
     msg(&Attraction.GetMessages().ToJson())
  Endif
```

### [8) Samples to expose a Business Component as a web service](#8%29+Samples+to+expose+a+Business+Component+as+a+web+service)

Read the article titled [Business Component - Publication as Web Service](https://wiki.genexus.com/commwiki/wiki?2282) that contains examples.


|  |
| --- |
| **Backlinks** |
| [Toc:Business Component](https://wiki.genexus.com/commwiki/wiki?5846) |

---
