---
title: "OAuthRefreshTokenExpire property in GAMSecurityPolicy EO"
source_id: 58097
source_url: https://wiki.genexus.com/commwiki/wiki?58097
genexus_version: "18"
---

# OAuthRefreshTokenExpire property in GAMSecurityPolicy EO

Sets the time, in minutes, that a refresh\_token will remain active.

### [Syntax](#Syntax)

*&GAMSecurityPolicy.***OAuthRefreshTokenExpire** *= Number\_Minutes*

**Where:**

*&GAMSecurityPolicy*  Is a variable based on the GAMSecurityPolicy data type.

*Number\_Minutes*  
  Number in minutes that a refresh\_token will remain active.

### [Description](#Description)

The **OAuthRefreshTokenExpire** property allows setting the time, in minutes, that a refresh\_token will remain active.

It makes sense to configure this property if the [OauthTokenMaximumRenovations property](https://wiki.genexus.com/commwiki/wiki?19324) (available in the same EO) > 0.

The **OAuthRefreshTokenExpire** property default value is 43200 minutes (30 days). Its value can't be 0.

As long as a refresh\_token is valid, it can be used to request a new OAuth Token.

When a client makes a request to an Identity Provider (IDP) to obtain a new access\_token based on a refresh\_token, the IDP validates if the refresh\_token received is not expired.

**Note**: When using the GAM Backoffice, this property is shown with the description "OAuth refresh\_token expiration (minutes)".

### [Samples](#Samples)

To set this property in the GeneXus code (by using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)), the syntax is as follows:

```
&GAMSecurityPolicy.OAuthRefreshTokenExpire = 60 //minutes
```

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244).

### [See Also](#See+Also)

[GAM - Security Policies](https://wiki.genexus.com/commwiki/wiki?18521)  
[GAM - OAuth 2.0 Endpoints to use GAM as Web IDP Server](https://wiki.genexus.com/commwiki/wiki?49817)  
[HowTo: Use OAuth 2.0 Endpoints to authenticate with GAM as REST IDP Server](https://wiki.genexus.com/commwiki/wiki?55623)  
[GAM - OAuth 2.0 Authentication Type](https://wiki.genexus.com/commwiki/wiki?39484)


|  |
| --- |
| **Backlinks** |
| [GAM - Security Policies](https://wiki.genexus.com/commwiki/wiki?18521) | [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244) |

---
