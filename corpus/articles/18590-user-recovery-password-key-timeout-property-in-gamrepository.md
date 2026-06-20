---
title: "User Recovery Password Key Timeout property in GAMRepository"
source_id: 18590
source_url: https://wiki.genexus.com/commwiki/wiki?18590
genexus_version: "18"
---

# User Recovery Password Key Timeout property in GAMRepository

Sets the validity time for the password recovery key. Is a [GAM Repository](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18463,,) property that allows the administrator in the [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) to define the period during which the key generated for user password recovery will remain valid.

The GAMRepositoryConfiguration Web Panel (located in [GAM Example folder](https://wiki.genexus.com/commwiki/wiki?15935)) is an example of this property being used.

### [Values](#Values)

Any valid time in minutes.

### [Description](#Description)

[GeneXus Access Manager](https://wiki.genexus.com/commwiki/wiki?24746) enables the final users to recover their password in several ways. See [GAM: A way to solve Forgot Password](https://wiki.genexus.com/commwiki/wiki?16923) for more information.

The key provided to the developer for sending recovery emails to users has an expiration time, which is set in minutes using the User Recovery Password Key Timeout property in the GAM Repository.

### [Sample](#Sample)

The way to use it in GeneXus code (by using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)) is the following:

```
&GAMRepository.UserRecoveryPasswordKeyTimeOut = &UserRecoveryPasswordKeyTimeOut
```

### [See Also](#See+Also)

[GAM: A way to solve Forgot Password](https://wiki.genexus.com/commwiki/wiki?16923)  
[GAM Repository features and properties](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18463,,)


|  |
| --- |
| **Backlinks** |
| [GAM: A way to solve Forgot Password](https://wiki.genexus.com/commwiki/wiki?16923) | [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) |

---
