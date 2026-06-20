---
title: "User Automatic Activate TimeOut property"
source_id: 18934
source_url: https://wiki.genexus.com/commwiki/wiki?18934
genexus_version: "18"
---

# User Automatic Activate TimeOut property

Using [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746), when a new account is created, a user activation e-mail with a user activation key is sent to the new user. The user activation key can be set to expire after a certain period of time (hours), for security reasons.

This property lets you set the amount of time, in hours, the activation key is valid. After that period, a new activation key must be generated. See [User Activation Method Repository property](https://wiki.genexus.com/commwiki/wiki?18932) for details on this mechanism.

You can configure this property using [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935).

### [Sample](#Sample)

The GAMRepositoryConfiguration [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) (located in GAM Example folder) is an example where this property is used in combination with User Activation Method Repository property.

The way to use it in GeneXus code (by using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)) is the following:

```
&Repository.UserAutomaticActivateTimeOut = &UserAutomaticActivateTimeOut
```


|  |
| --- |
| **Backlinks** |
| [GAM configuration to send emails](https://wiki.genexus.com/commwiki/wiki?48421) | [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) | [User Activation Method Repository property](https://wiki.genexus.com/commwiki/wiki?18932) |

---
