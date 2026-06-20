---
title: "Base Trn property"
source_id: 36811
source_url: https://wiki.genexus.com/commwiki/wiki?36811
genexus_version: "18"
---

# Base Trn property

Indicates the Transaction name or Transaction.Level name to be used as the base table for the Grid / Free Style Grid / Tabular Grid navigation.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817), [Free Style Grid](https://wiki.genexus.com/commwiki/wiki?6058), [Tabular Grid](https://wiki.genexus.com/commwiki/wiki?54449)

### [Description](#Description)

Although optional, the **Base Trn property**allows you to declare your navigation intention and improve the specification time (because the algorithm that calculates the [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) of the control is not executed).

You can indicate a list of Transaction names and/or Transaction levels. In this case, a kind of 'product' between the tables is performed, solving queries that imply navigation over different tables that are difficult to express in another way, or that cannot be solved in a single SQL statement.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s:

```
User            //Transaction 1st. level name
{
   UserId*
   UserName
   UserType
   Role        //Transaction 2nd. level name
   {
      RoleId*
   }
}

Role            //Transaction 1st. level name
{
   RoleId*
   RoleName
}
```

The following image shows a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) that receives a UserId value in its [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) and displays, in a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817), the roles associated with that user:

`[imagen omitida: wiki id 36810]`

Note the **Base Trn property** is set to User.Role to indicate that the table that must be navigated is the one associated with that Transaction level.

### [See Also](#See+Also)

[Base Transaction clause](https://wiki.genexus.com/commwiki/wiki?25418)


|  |
| --- |
| **Backlinks** |
| [Base Transaction clause](https://wiki.genexus.com/commwiki/wiki?25418) | [Base Trn property (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55948) | [Base Trn property for Grid of Work With Pattern Instance](https://wiki.genexus.com/commwiki/wiki?52768) |
| [Determining the Base Table for each Grid in a Web Panel](https://wiki.genexus.com/commwiki/wiki?6105) | [Load command](https://wiki.genexus.com/commwiki/wiki?8196) | [Load event](https://wiki.genexus.com/commwiki/wiki?8188) | [Orders and Filters in Grids of Panels](https://wiki.genexus.com/commwiki/wiki?24805) |

---
