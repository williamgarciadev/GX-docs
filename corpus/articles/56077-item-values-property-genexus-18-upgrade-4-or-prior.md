---
title: "Item Values property (GeneXus 18 Upgrade 4 or prior)"
source_id: 56077
source_url: https://wiki.genexus.com/commwiki/wiki?56077
genexus_version: "18"
---

# Item Values property (GeneXus 18 Upgrade 4 or prior)

Indicates the attribute or SDT member returned by a Data Provider from which an identifier value (that corresponds to a description entered by the end user) will be automatically loaded.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** Attribute/Variable (Control Type: [Dynamic Combo Box](https://wiki.genexus.com/commwiki/wiki?7598), [Dynamic List Box](https://wiki.genexus.com/commwiki/wiki?7599))

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s:

```
Country
{
  CountryId*
  CountryName
}

Customer
{ 
  CustomerId*
  CustomerName
  CountryId
  CountryName 
}
```

Suppose that, in the Customer Transaction, you set the [InputType property](https://wiki.genexus.com/commwiki/wiki?8799) of the CountryId attribute to Descriptions.

After that, you have two configuration options for the same attribute/variable (in this example, CountryId):

**1)** Set its [Data Source From property](https://wiki.genexus.com/commwiki/wiki?22945) to **Attributes** (this is the default value).  
**2)**Set its [Data Source From property](https://wiki.genexus.com/commwiki/wiki?22945) to **Data Provider.**

When choosing option 1) you must configure the **Item Values** **property** and the [Item Descriptions property](https://wiki.genexus.com/commwiki/wiki?8807) with attributes.

So, for the same attribute/variable (in this example, CountryId) set:

* Its **Item Values** **property** to CountryId (this configuration will be done by default).
* Its [Item Descriptions property](https://wiki.genexus.com/commwiki/wiki?8807) to CountryName.

Thus, on the screen, the CountryId attribute will be “disguised” as CountryName. End users will see a field to type/select a CountryName, but the attribute is CountryId.

When an end user types/selects “Uruguay”, an internal search is performed to retrieve the CountryId value that corresponds to "Uruguay". That value (for example: 1) is stored in the CountryId attribute. For the end user, this is totally transparent.

When choosing option 2) you must configure the [Data Provider property](https://wiki.genexus.com/commwiki/wiki?56081)to a name of a [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) that is in charge of loading an SDT collection that loads the **Item Values** **property** and the [Item Descriptions property](https://wiki.genexus.com/commwiki/wiki?8807).

The first numeric member and the first descriptor member of the SDT returned by the Data Provider are automatically assigned to the **Item Values** **property** and [Item Descriptions property](https://wiki.genexus.com/commwiki/wiki?8807). You can update these default values.

**Note:** Although in this example the CountryId attribute configured is in a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908), it could be a &CountryId variable present in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) or [Panel object](https://wiki.genexus.com/commwiki/wiki?24829).
