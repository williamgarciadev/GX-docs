---
title: "User Remember Me Timeout"
source_id: 18586
source_url: https://wiki.genexus.com/commwiki/wiki?18586
genexus_version: "18"
---

# User Remember Me Timeout

User Remember Me Timeout is a [GAM Repository](https://wiki.genexus.com/commwiki/wiki?18463,,) property related to [User Remember Me Type](https://wiki.genexus.com/commwiki/wiki?18584) property, available in GAMRepositoryConfiguration [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) of [GAM Backend](https://wiki.genexus.com/commwiki/wiki?15935). You can find GAMRepositoryConfiguration object in GAM Examples folder.

The purpose of this property is to set a Timeout in days in which the login is not remembered anymore, so if

* [UserRememberMeType property](https://wiki.genexus.com/commwiki/wiki?18584) = Login, the [WEB Login](https://wiki.genexus.com/commwiki/wiki?15590) object will not instantiate the last login information (the login information will be empty) when the session expires.
* [UserRememberMeType property](https://wiki.genexus.com/commwiki/wiki?18584) = Authentication, the [WEB Login](https://wiki.genexus.com/commwiki/wiki?15590) object will be shown when the session expires.

The property can be used in any object, by using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535), as the following code shows:

```
&Repository.UserRememberMeTimeOut = &UserRememberMeTimeOut
```

Take as an example the "GAMExampleLogin" object which is part of the GAM Examples Library to see how the property [User Remember Me Type](https://wiki.genexus.com/commwiki/wiki?18584) is used in combination with User Remember Me Timeout.

### [Values](#Values)

Any valid value in days. 0 means infinite.

### [See also](#See+also)

[User Remember Me Type](https://wiki.genexus.com/commwiki/wiki?18584)  
[GAM Repository features and properties](https://wiki.genexus.com/commwiki/wiki?18463,,)


|  |
| --- |
| **Backlinks** |
| [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) | [UserRememberMeType property](https://wiki.genexus.com/commwiki/wiki?18584) |

---
