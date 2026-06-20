---
title: "MaximumPasswordHistoryEntries property in GAMSecurityPolicy EO"
source_id: 18579
source_url: https://wiki.genexus.com/commwiki/wiki?18579
genexus_version: "18"
---

# MaximumPasswordHistoryEntries property in GAMSecurityPolicy EO

Indicates how many passwords must be stored in the list of the user's last passwords, to avoid repeating any of those passwords when they define a new one.

### [Syntax](#Syntax)

*&GAMSecurityPolicy.***MaximumPasswordHistoryEntries** *= Number*

**Where:**

*&GAMSecurityPolicy*   Is a variable based on the GAMSecurityPolicy data type.

*Number*  
    Number of passwords to store in the list of the user's last passwords.

### [Description](#Description)

This property allows indicating how many passwords must be stored in the list of the user's last passwords, to avoid repeating any of those passwords when they define a new one.

**Note**: When using the [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935), this property is shown with the description "Maximum password history entries".

### [Samples](#Samples)

The GAMExampleEntrySecurityPolicy [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) is an example of where this property is used.  
  
To set this property in the GeneXus code (by using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)), the syntax is as follows:

```
&GAMSecurityPolicy.MaximumPasswordHistoryEntries = 5 // The user cannot define a password equal to their last 5 passwords.
```


|  |
| --- |
| **Backlinks** |
| [GAM - Security Policies](https://wiki.genexus.com/commwiki/wiki?18521) | [GAM - Security Policies (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58087) | [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) |

---
