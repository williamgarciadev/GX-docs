---
title: "Refresh method for Grid controls (GeneXus 18 Upgrade 2 or prior)"
source_id: 57357
source_url: https://wiki.genexus.com/commwiki/wiki?57357
genexus_version: "18"
---

# Refresh method for Grid controls (GeneXus 18 Upgrade 2 or prior)

Refreshes only the Grid to which the method is applied. It triggers the Grid Refresh event and subsequently the Grid Load event (N times or once, depending on whether or not the Grid has a base table).

### [Syntax](#Syntax)

Event 'User-event'  
     .......  
     GridName.**Refresh()**  
endevent

**Where:**

*GridName*  
     Is the name of the Grid control to be refreshed.

### [Scope](#Scope)

**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817), [Free Style Grid](https://wiki.genexus.com/commwiki/wiki?6058)  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),

[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

**Note**: In [Java](https://wiki.genexus.com/commwiki/wiki?12258), this method is supported when the [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) is set to "Smooth".

### [Samples](#Samples)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s defined in a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) for a Travel Agency:

```
Attraction
{
  AttractionId*
  AttractionName
  CountryId
  CountryName
  CityId
  CityName
  AttractionPhoto
}

Restaurant              //Its Business Component property = True
{
  RestaurantId*
  RestaurantName
  RestaurantAddress
  CountryId 
  CountryName
  CityId
  CityName
  RestaurantSpecialDiscount  (Boolean)
}

Country
{
  CountyId*
  CountryName
  City
  {
     CityId*
     CityName
  }
}
```

The following [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916), which contains two [Grid control](https://wiki.genexus.com/commwiki/wiki?24817)s in its Web Layout, is defined in the KB:

`[imagen omitida: wiki id 55878]`

The Grid's navigations are independent. They are [Parallel Grids](https://wiki.genexus.com/commwiki/wiki?55724,,).

* Grid1: It has a base table (Attraction)
* Grid2: It has a base table (Restaurant)

The Web Panel contains a [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) that receives two attributes, as follows:

```
Parm(CountryId,CityId);
```

So, the CountryId and CityId values work as filters for the whole object.

Therefore:

* Grid1 shows the Attractions of the CountryId and a CityId received.
* Grid2 shows the Restaurants of the CountryId and a CityId received.

Look at the second Grid (named 'Grid2'). As the attributes in Web Panels are read-only, the end user can't check/uncheck the RestaurantSpecialDiscount attribute. It is shown checked if its value is True or unchecked if its value is False. Therefore, two images were added to the second Grid for the following purposes:

* When the end user clicks on the &SpecialDiscount image, the RestaurantSpecialDiscount attribute is set to True and saved in the database.
* When the end user clicks on the &NoDiscount image, the RestaurantSpecialDiscount attribute is set to False value and saved in the database.

Suppose that, at runtime, the Web Panel is called with the CountryId corresponding to 'France' and the CityId corresponding to 'Paris'. So, it will look as follows:

`[imagen omitida: wiki id 55880]`

In order to implement the described behavior, the following events were defined in the Events tab of the Web Panel:

```
Event Start
    &SpecialDiscount.FromImage(success_ico_green)
    &NoDiscount.FromImage(close_ico)
Endevent

Event 'RestaurantHasSpecialDiscount'    //This event is assigned to the On Click Event property of the &SpecialDiscount.
   &Restaurant.Load(RestaurantId)       //&Restaurant is based on the Restaurant Business Component data type. 
   &Restaurant.RestaurantSpecialDiscount = True
   &Restaurant.Update()
   Commit    
   Grid2.Refresh()                      //If you do not execute this method, the database is updated but the Grid2 isn't refreshed.
Endevent

Event 'RestaurantHasNoDiscount'         //This event is assigned to the On Click Event property of the &NoDiscount.
   &Restaurant.Load(RestaurantId)       //&Restaurant is based on the Restaurant Business Component data type.  
   &Restaurant.RestaurantSpecialDiscount = False
   &Restaurant.Update()
   Commit    
   Grid2.Refresh()                      //If you do not execute this method, the database is updated but the Grid2 isn't refreshed.
Endevent
```

The Grid Refresh method is applied to the Grid2 control in both User events after the database update. Otherwise, after the database update, Grid2 isn't refreshed and the end user does not see that the value of the RestaurantSpecialDiscount attribute was changed.

The execution of the Refresh method associated with a certain Grid (in this case, with the Grid2), triggers the Grid2.Refresh event and subsequently the Grid2.Load event (N times because the Grid has a base table).
