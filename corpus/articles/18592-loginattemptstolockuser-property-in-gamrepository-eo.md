---
title: "LoginAttemptsToLockUser property in GAMRepository EO"
source_id: 18592
source_url: https://wiki.genexus.com/commwiki/wiki?18592
genexus_version: "18"
---

# LoginAttemptsToLockUser property in GAMRepository EO

Configures the number of login failures until the user is locked. Its default value is 0, which means that regardless of the number of login attempts, the user will never be blocked.

### [Syntax](#Syntax)

*&GAMRepository.**LoginAttemptsToLockUser****= Number*

**Where:**

*&GAMRepository*  Is a variable based on the GAMRepository data type.

*Number*  
  Number of login failures until the user is locked.

### [Description](#Description)

This property allows you to set the number of login failures until the user is locked.

Its default value is 0, which means that regardless of the number of login attempts, the user will never be blocked.

This property is also taken into account for login attempts through the *oauth/access\_token* and *oauth/gam/v2.0/access\_token* services.

**Note**: When using the GAM Backoffice, this property can be configured by selecting **Repository > Configuration > Users**. It is shown with the description "Login retries to lock user".

### [Sample](#Sample)

To set this property in the GeneXus code (by using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)), the syntax is as follows:

```
&GAMRepository.LoginAttemptsToLockUser = 2
```

For example, if the user makes more than 2 unsuccessful attempts using the oauth/access\_token service, the following message will be displayed:

```
{
    "error": {
        "code": "10",
        "message": "User blocked. Please contact the application administrator."
    }
}
```

When blocked, the user needs to be unblocked by the [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) Administrator.

See [GAMUnblockUserTimeout property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18926) as another way to unblock user sessions.

### [See Also](#See+Also)

[LoginAttemptsToLockSession property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18593)  
[GAMUnblockUserTimeout property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18926)  
[GAM Repository features and properties](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18463,,)


|  |
| --- |
| **Backlinks** |
| [GAMUnblockUserTimeout property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18926) | [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) | [Login retries to lock user property (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58371) |
| [LoginAttemptsToLockSession property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18593) | [TimeoutToResetCountFailedOAuthLogins property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?58201) |

---
