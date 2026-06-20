---
title: "User Identification"
source_id: 21030
source_url: https://wiki.genexus.com/commwiki/wiki?21030
genexus_version: "18"
---

# User Identification

User Identification is a property from the [GAM Repository](https://wiki.genexus.com/commwiki/wiki?18463,,) to set those attributes identifying a user.

The GAMRepositoryConfiguration Web Panel (located in GAM Example folder) is an example where this property is used.

The way to use it in GeneXus code (by using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)) is the following:

```
&Repository.UserIdentification = GAMRepositoryUserIdentifications.NameEmail
```

### [Values](#Values)

Name  
Email  
Name and Email (default value)

### [Description](#Description)

Defines the [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) User Identification strategy. When using "Name and Email" means that both values must be unique, otherwise an error will occur. The "Name" value will check user Identification against the User Name only. While the "Email" value will check uniqueness on the User Email attribute.

### [See Also](#See+Also)

[GAM Repository features and properties](https://wiki.genexus.com/commwiki/wiki?18463,,)


|  |
| --- |
| **Backlinks** |
| [GAM - External Authentication: version 2.0](https://wiki.genexus.com/commwiki/wiki?21555) | [HowTo: Use GAM and Windows Authentication](https://wiki.genexus.com/commwiki/wiki?24034) |

---
