---
title: "TimeoutForUserChangePasswordAfterLogin property in GAMRepository EO"
source_id: 58085
source_url: https://wiki.genexus.com/commwiki/wiki?58085
genexus_version: "18"
---

# TimeoutForUserChangePasswordAfterLogin property in GAMRepository EO

Configures the time, in minutes, allowed for a user to change the password after logging in.

### [Syntax](#Syntax)

*&GAMRepository.**TimeoutForUserChangePasswordAfterLogin** = Number\_Minutes*

**Where:**

*&GAMRepository*  Is a variable based on the GAMRepository data type.

*Number\_Minutes*  
  Number of minutes available to change the user password after logging in.

### [Description](#Description)

By default, this property is set to 15 minutes. Its value can't be 0.

When a user is required to change their password, either because the **Must change password property** (&GAMUser.MustChangePassword = True) is set, or because the period specified in the **Period change password (days) property** (&GAMSecurityPolicy.PeriodChangePassword) of the applied Security Policies has expired, the user will be redirected to the GAMExampleChangePassword[Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) upon logging in.

The user must change the password in that UI (GAMExampleChangePassword Web Panel) within the time set in the GAMRepository TimeoutForUserChangePasswordAfterLogin property. Otherwise, the session will expire, and the user will have to start the process again.

**Note**: When using the GAM Backoffice, this property can be configured by selecting **Repository > Configuration > General Security Policy**. It is shown with the description "Timeout For User To Change Password After Login (minutes)".

### [Samples](#Samples)

To set this property in the GeneXus code (by using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)), the syntax is as follows:

```
&GAMRepository.TimeoutForUserChangePasswordAfterLogin = 10
```

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244).

### [See Also](#See+Also)

[TimeoutToCompleteRequiredUserDataAfterLogin property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?58082)  
[GAM - Repository](https://wiki.genexus.com/commwiki/wiki?17568)  
[GAM Repository features and properties](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18463,,)


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244) |

---
