---
title: "Base Trn property (GeneXus 18 Upgrade 5 or prior)"
source_id: 55948
source_url: https://wiki.genexus.com/commwiki/wiki?55948
genexus_version: "18"
---

# Base Trn property (GeneXus 18 Upgrade 5 or prior)

Indicates the Transaction name or Transaction.Level name to be used as the base table for the Grid navigation.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817), [Free Style Grid](https://wiki.genexus.com/commwiki/wiki?6058)

### [Description](#Description)

Although optional, allows you to declare its navigation intention and to improve time for specification (because it isn't needed to do the calculation of the grid Base Table).

It may be a list of Transaction levels. In that case, a kind of 'product' between the tables is done, solving queries that imply navigation over different tables that are difficult to express in another way, or that cannot be solved in a single SQL sentence.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Having the following Transactions:

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

Look at the following image that shows a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) (same concept for [Panel](https://wiki.genexus.com/commwiki/wiki?24829)) that receives a UserId value in its [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) and displays in a grid the roles associated with that user:

`[imagen omitida: wiki id 36810]`

Note the Base Trn grid property set with User.Role in order to indicate the base table associated with that level.

### [Availability](#Availability)

This property is available since [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?20247,,).

### [See Also](#See+Also)

[Base Transaction clause](https://wiki.genexus.com/commwiki/wiki?25418)
