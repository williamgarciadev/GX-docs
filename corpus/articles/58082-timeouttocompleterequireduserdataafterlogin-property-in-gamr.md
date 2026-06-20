---
title: "TimeoutToCompleteRequiredUserDataAfterLogin property in GAMRepository EO"
source_id: 58082
source_url: https://wiki.genexus.com/commwiki/wiki?58082
genexus_version: "18"
---

# TimeoutToCompleteRequiredUserDataAfterLogin property in GAMRepository EO

Configures the time, in minutes, allowed for a user to complete the required data in the repository they want to access.

### [Syntax](#Syntax)

*&GAMRepository.**TimeoutToCompleteRequiredUserDataAfterLogin** = Number\_Minutes*

**Where:**

*&GAMRepository*  
   Is a variable based on the GAMRepository data type.

*Number\_Minutes*  
  Number of minutes available for a user to complete the required data in the repository they want to access.

### [Description](#Description)

By default, this property is set to 15 minutes. Its value can't be 0.

When the [Repository](https://wiki.genexus.com/commwiki/wiki?17568) needs specific information from the user that is not provided at the time of login, the user is redirected to a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) called GAMExampleUpdateRegisterUser.

The user must complete the missing information in that UI (GAMExampleUpdateRegisterUserWeb Panel) within the time set in the GAMRepository TimeoutToCompleteRequiredUserDataAfterLogin property.   
  
Only after providing the required data within that time, the user can access the application.

**Note**: When using the GAM Backoffice, this property can be configured by selecting **Repository > Configuration > General Security Policy**. It is shown with the description "Timeout to complete required user data after login (minutes)".

### [Samples](#Samples)

To set this property in the GeneXus code (by using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)), the syntax is as follows:

```
&GAMRepository.TimeoutToCompleteRequiredUserDataAfterLogin = 10
```

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244).

### [See Also](#See+Also)

[GAM Repository features and properties](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18463,,)


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244) | [TimeoutForUserChangePasswordAfterLogin property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?58085) |

---
