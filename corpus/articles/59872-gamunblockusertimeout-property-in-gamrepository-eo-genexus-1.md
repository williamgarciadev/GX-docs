---
title: "GAMUnblockUserTimeout property in GAMRepository EO (GeneXus 18 Upgrade 9 or prior)"
source_id: 59872
source_url: https://wiki.genexus.com/commwiki/wiki?59872
genexus_version: "18"
---

# GAMUnblockUserTimeout property in GAMRepository EO (GeneXus 18 Upgrade 9 or prior)

Controls how long (in minutes) a blocked user will have to wait until their account is automatically unblocked.

### [Syntax](#Syntax)

*&GAMRepository.**GAMUnblockUserTimeout****= Number\_Minutes*

**Where:**

*&GAMRepository*  Is a variable based on the GAMRepository data type.

*Number\_Minutes*  
  Time in minutes a [blocked user](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?19063,,) will have to wait until their account is automatically unblocked.

### [Description](#Description)

This property controls how long (in minutes) a [blocked user](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?19063,,) will have to wait until their account is automatically unblocked.

0 means that the user is never unblocked; in this case, the repository administrator must unblock the user.

**Note**: When using the [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935), this property can be configured by selecting **Repository > Configuration > General Security Policy**. It is shown with the description "GAM Unblock User Timeout".

### [Sample](#Sample)

The GAMRepositoryConfiguration [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) is an example where this property is used.

To set this property in the GeneXus code (by using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)), the syntax is as follows:

```
&GAMRepository.GAMUnblockUserTimeout = 15 //minutes
```

### [See Also](#See+Also)

[LoginAttemptsToLockSession property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18593)  
[LoginAttemptsToLockUser property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18592)  
[GAM Repository features and properties](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18463,,)
