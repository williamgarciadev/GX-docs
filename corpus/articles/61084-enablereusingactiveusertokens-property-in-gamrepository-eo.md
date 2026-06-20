---
title: "EnableReusingActiveUserTokens property in GAMRepository EO"
source_id: 61084
source_url: https://wiki.genexus.com/commwiki/wiki?61084
genexus_version: "18"
---

# EnableReusingActiveUserTokens property in GAMRepository EO

Allows the reuse of an active, unexpired access token when requesting a new one.

### [Syntax](#Syntax)

*&GAMRepository.**EnableReusingActiveUserTokens** = True / False*

**Where:**

*&GAMRepository*  
Is a variable based on the GAMRepository data type.

### [Description](#Description)

This property determines whether an existing active access token can be reused when a new token is requested.

This property allows you to specify whether you want to enable the reuse of active and unexpired access tokens for a user.

It applies when requesting tokens from any of the following endpoints:

* oauth/access\_token
* oauth/gam/v2.0/access\_token
* oauth/gam/access\_token

This means that if the user has an active token and it has not expired, when requesting a token, it will be provided until it expires or remains active.

By default, this property is set to False.

**Note**: When using the [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935), this property can be configured by selecting **Repository > Configuration > General Security Policy**. It is shown with the description "Enable reuse of active user tokens". For more information, read [General Security Policy tab](https://wiki.genexus.com/commwiki/wiki?61036).

### [Sample](#Sample)

To set this property in the GeneXus code (by using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)), the syntax is as follows:

```
&GAMRepository.EnableReusingActiveUserTokens = True //boolean
```

The GAMRepositoryConfiguration [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) is an example where this property is used.

### [Availability](#Availability)

Since [GeneXus 18 Upgrade 14](https://wiki.genexus.com/commwiki/wiki?59631).

### [See Also](#See+Also)

[GAM Repository features and properties](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18463,,)  
[GAM Web Backoffice - Repository section](https://wiki.genexus.com/commwiki/wiki?61036)


|  |
| --- |
| **Backlinks** |
| [GAM Web Backoffice - Repository section](https://wiki.genexus.com/commwiki/wiki?61036) |

---
