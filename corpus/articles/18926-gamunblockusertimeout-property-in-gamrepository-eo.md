---
title: "GAMUnblockUserTimeout property in GAMRepository EO"
source_id: 18926
source_url: https://wiki.genexus.com/commwiki/wiki?18926
genexus_version: "18"
---

# GAMUnblockUserTimeout property in GAMRepository EO

Controls how long (in minutes) a blocked user will have to wait until their account is automatically unblocked.

### [Syntax](#Syntax)

*&GAMRepository.**GAMUnblockUserTimeout*** *= Number\_Minutes*

**Where:**

*&GAMRepository*  Is a variable based on the GAMRepository data type.

*Number\_Minutes*  
  Time in minutes a [blocked user](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?19063,,) will have to wait until their account is automatically unblocked.

### [Description](#Description)

This property controls how long (in minutes) a [blocked user](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?19063,,) will have to wait until their account is automatically unblocked.

0 means that the user is never unblocked; in this case, the repository administrator must unblock the user.

**Note**: When using the [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935), this property can be configured by selecting **Repository > Configuration > Users**. It is shown with the description "Timeout to automatically unlock users (minutes)".

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


|  |
| --- |
| **Backlinks** |
| [GAMUnblockUserTimeout property in GAMRepository EO (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?59872) | [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) | [Login retries to lock user property (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58371) |
| [LoginAttemptsToLockUser property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18592) | [TimeoutToResetCountFailedOAuthLogins property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?58201) |

---
