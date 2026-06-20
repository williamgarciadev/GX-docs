---
title: "TimeoutToResetCountFailedOAuthLogins property in GAMRepository EO"
source_id: 58201
source_url: https://wiki.genexus.com/commwiki/wiki?58201
genexus_version: "18"
---

# TimeoutToResetCountFailedOAuthLogins property in GAMRepository EO

Sets the timeout (in minutes) to reset the failed login attempt count.

### [Syntax](#Syntax)

*&GAMRepository.**TimeoutToResetCountFailedOAuthLogins**= Number\_Minutes*

**Where:**

*&GAMRepository*  Is a variable based on the GAMRepository data type.

*Number\_Minutes*  
  Time in minutes until the number of failed login attempts is reset.

### [Description](#Description)

This property by default is set to 0, which means that the user will never be blocked.

**Note**: When using the GAM Backoffice, this property can be configured by selecting **Repository > Configuration > General Security Policy**. It is shown with the description "Timeout to reset countdown failed OAuth logins (minutes) (0= Does not block OAuth user)".

### [Sample](#Sample)

To set this property in the GeneXus code (by using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)), the syntax is as follows:

```
&GAMRepository.TimeoutToResetCountFailedOAuthLogins = 60
```

This code implies that if the [LoginAttemptsToLockUser property](https://wiki.genexus.com/commwiki/wiki?18592) is set to 3, the user will have to wait 60 minutes to be able to try to log in again.

## [See Also](#See+Also)

[LoginAttemptsToLockUser property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18592)  
[LoginAttemptsToLockSession property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18593)  
[GAMUnblockUserTimeout property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18926)
