---
title: "Login retries to lock user property (GeneXus 18 Upgrade 9 or prior)"
source_id: 58371
source_url: https://wiki.genexus.com/commwiki/wiki?58371
genexus_version: "18"
---

# Login retries to lock user property (GeneXus 18 Upgrade 9 or prior)

Login retries to lock user (&GAMRepository.LoginAttemptsToLockUser) is a [GAM Repository](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18463,,) property used to specify the number of login failures until the user is locked.

This property by default is set to 0, this means that regardless of the number of login attempts the user will never be blocked.

### [Sample](#Sample)

The way to use it in GeneXus code (by using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)) is the following:

```
&GAMRepository.LoginAttemptsToLockUser = 2
```

For example, if you make more than 2 unsuccessful attempts using the oauth/access\_token service, you will get the following message:

```
{
    "error": {
        "code": "10",
        "message": "User blocked. Please contact the application administrator."
    }
}
```

When blocked, the user needs to be un-blocked by the Administrator of [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935).

See [GAMUnblockUserTimeout property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18926) as another way to unblock user sessions.

### [See Also](#See+Also)

[LoginAttemptsToLockSession property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18593)  
[GAMUnblockUserTimeout property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18926)  
[GAM Repository features and properties](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18463,,)
