---
title: "MinimumTimeToChangePasswords property in GAMSecurityPolicy EO"
source_id: 18942
source_url: https://wiki.genexus.com/commwiki/wiki?18942
genexus_version: "18"
---

# MinimumTimeToChangePasswords property in GAMSecurityPolicy EO

Specifies the minimum time, in minutes, that a user must wait until they can change their password again. Its default value is 0, which means that the user doesn't have to wait between password changes.

### [Syntax](#Syntax)

*&GAMSecurityPolicy.***MinimumTimeToChangePasswords***= Number\_Minutes*

**Where:**

*&GAMSecurityPolicy*  Is a variable based on the GAMSecurityPolicy data type.

*Number\_Minutes*  
  Minimum time, in minutes, that a user must wait until they can change their password.

### [Description](#Description)

This property allows configuring the minimum time, in minutes, that a user must wait until they can change their password again.

Its default value is 0, which means that the user doesn't have to wait between password changes.

**Note**: When using the GAM Backoffice, this property is shown with the description "Minimum waiting time between password changes (minutes)".

### [Samples](#Samples)

The GAMExampleEntrySecurityPolicy [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) is an example of where this property is used.   
  
To set this property in the GeneXus code (by using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)), the syntax is as follows:

```
&GAMSecurityPolicy.MinimumTimeToChangePasswords  =  60 //minutes
```

The above example means that the user will have to wait 60 minutes to change their password again.

### [See also](#See+also)

[GAM Repository features and properties](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18463,,)


|  |
| --- |
| **Backlinks** |
| [GAM - Security Policies](https://wiki.genexus.com/commwiki/wiki?18521) | [GAM - Security Policies (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58087) | [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) |

---
