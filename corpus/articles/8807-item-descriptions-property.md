---
title: "Item Descriptions property"
source_id: 8807
source_url: https://wiki.genexus.com/commwiki/wiki?8807
genexus_version: "18"
---

# Item Descriptions property

Indicates the attribute or SDT member returned by a Data Provider whose data (descriptions that contain semantic meaning) will be displayed instead of the corresponding identifiers.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** Attribute/Variable (Control Type: [Dynamic Combo Box](https://wiki.genexus.com/commwiki/wiki?7598), [Dynamic List Box](https://wiki.genexus.com/commwiki/wiki?7599), Edit)

### [Description](#Description)

This property is available for attributes/variables whose [InputType property](https://wiki.genexus.com/commwiki/wiki?8799) is set to Descriptions.

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

When choosing option 1) you must configure the [Item Values property](https://wiki.genexus.com/commwiki/wiki?8808)and the **Item Descriptions property** with attributes.

So, for the same attribute/variable (in this example, CountryId) set:

* Its [Item Values property](https://wiki.genexus.com/commwiki/wiki?8808)to CountryId (this configuration will be done by default).
* Its **Item Descriptions property** to CountryName.

Thus, on the screen, the CountryId attribute will be “disguised” as CountryName. End users will see a field to type/select a CountryName, but the attribute is CountryId.

When an end user types/selects “Uruguay”, an internal search is performed to retrieve the CountryId value that corresponds to "Uruguay". That value (for example: 1) is stored in the CountryId attribute. For the end user, this is totally transparent.

When choosing option 2) you must configure the [Data Provider property](https://wiki.genexus.com/commwiki/wiki?56081)to a name of a [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) that is in charge of loading an SDT collection that loads the [Item Values property](https://wiki.genexus.com/commwiki/wiki?8808)and the **Item Descriptions property**.

The first numeric member and the first descriptor member of the SDT returned by the Data Provider are automatically assigned to the [Item Values property](https://wiki.genexus.com/commwiki/wiki?8808)and **Item Descriptions property**. You can update these default values.

**Note:** Although in this example the CountryId attribute configured is in a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908), it could be a &CountryId variable present in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) or [Panel object](https://wiki.genexus.com/commwiki/wiki?24829).

### [See Also](#See+Also)

[Item Values property](https://wiki.genexus.com/commwiki/wiki?8808)


|  |
| --- |
| **Backlinks** |
| [Dynamic Combo Box and Dynamic List Box Properties in Web Forms](https://wiki.genexus.com/commwiki/wiki?8740) | [Edit with Suggest](https://wiki.genexus.com/commwiki/wiki?55531) | [GetDescriptionByKey Procedure Parameters property](https://wiki.genexus.com/commwiki/wiki?55468) |
| [GetDescriptionByKey Procedure property](https://wiki.genexus.com/commwiki/wiki?55413) | [HowTo: Use the Data Source From property](https://wiki.genexus.com/commwiki/wiki?22948) | [Item Descriptions property (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?56079) | [Item Values property](https://wiki.genexus.com/commwiki/wiki?8808) |
| [Item Values property (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?56077) |

---
