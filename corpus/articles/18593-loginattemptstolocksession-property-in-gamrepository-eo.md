---
title: "LoginAttemptsToLockSession property in GAMRepository EO"
source_id: 18593
source_url: https://wiki.genexus.com/commwiki/wiki?18593
genexus_version: "18"
---

# LoginAttemptsToLockSession property in GAMRepository EO

Determines the number of times a user can try to log in before the session is blocked and they need to close the browser and try again.

### [Syntax](#Syntax)

*&GAMRepository.**LoginAttemptsToLockSession**= Number*

**Where:**

*&GAMRepository*  Is a variable based on the GAMRepository data type.

*Number*  
  Number of times a user can try to log in before the session is blocked and they need to close the browser and try again.

### [Description](#Description)

**Note**: When using the [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935), this property can be configured by selecting **Repository > Configuration > General Security Policy**. It is shown with the description "Login attempts to lock session (WEB)".

### [Samples](#Samples)

The GAMRepositoryConfiguration [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) is an example of where this property is used.

To set this property in the GeneXus code (by using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)), the syntax is as follows:

```
&GAMRepository.LoginAttemptsToLockSession = 3
```

### [See also](#See+also)

[LoginAttemptsToLockUser property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18592)  
[GAM Repository features and properties](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18463,,)


|  |
| --- |
| **Backlinks** |
| [GAMUnblockUserTimeout property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18926) | [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) | [Login retries to lock user property (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58371) |
| [LoginAttemptsToLockUser property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18592) | [TimeoutToResetCountFailedOAuthLogins property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?58201) |

---
