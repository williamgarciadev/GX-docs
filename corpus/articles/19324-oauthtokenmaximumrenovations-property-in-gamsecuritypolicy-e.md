---
title: "OauthTokenMaximumRenovations property in GAMSecurityPolicy EO"
source_id: 19324
source_url: https://wiki.genexus.com/commwiki/wiki?19324
genexus_version: "18"
---

# OauthTokenMaximumRenovations property in GAMSecurityPolicy EO

Configures how many refresh\_tokens the Identity Provider (IDP) will give to the client application.

### [Syntax](#Syntax)

*&GAM*SecurityPolicy*.**OauthTokenMaximumRenovations****= Number*

**Where:**

*&GAMSecurityPolicy*  
   Is a variable based on the GAMSecurityPolicy data type.

*Number*  
  Number of refresh\_tokens the Identity Provider (IDP) will give to the client application.

### [Description](#Description)

This property allows you to set how many refresh\_tokens the Identity Provider (IDP) will give to the client application. That is, the number of times that the access\_token can expire, and the login will be automatically renewed without asking the user to enter their credentials again.  
  
In other words, the client application can obtain a refresh\_token when requesting an access\_token. When the last access\_token expires, the refresh token can be used to request a new access\_token.

The default value for the property is 0, which means that the IDP **will not give any refresh\_token** to the client application. When the time indicated in the [OauthTokenExpire property](https://wiki.genexus.com/commwiki/wiki?18577) reaches 0, the user must log in again.  
  
The maximum number of refresh\_tokens the IDP can return is 999.

If you set this property with a value higher than zero, when the client application requests an access\_token, the response will look as follows:

```
{
    "access_token": "85a3006c-0606-41d2-980e-223f88463ec2!b1b3e778247c870560d49d17ffd514a2a8467747208b1cf4a641780a267466bc65fba8034c9bbc",
    "token_type": "Bearer",
    "expires_in": 180,
    "refresh_token": "002b9ec850f78b845d883779fa52c91a01",
    "scope": "gam_user_data",
    "user_guid": "139f4332-3f40-47b0-8fb4-ee7b3dbddc4f"
}
```

**Note**: When using the GAM Backoffice, this property is shown with the description "Token maximum renovations".

### [Sample](#Sample)

To set this property in the GeneXus code (by using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)), the syntax is as follows:

```
&GAMSecurityPolicy.OauthTokenExpire  = 180 //minutes
&GAMSecurityPolicy.OauthTokenMaximumRenovations  = 3
```

### [See Also](#See+Also)

[OauthTokenExpire property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?18577)


|  |
| --- |
| **Backlinks** |
| [GAM - OAuth 2.0 Endpoints to use GAM as Web IDP Server](https://wiki.genexus.com/commwiki/wiki?49817) | [GAM - OAuth 2.0 Endpoints to use GAM as Web IDP Server (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56244) | [GAM - Security Policies](https://wiki.genexus.com/commwiki/wiki?18521) |
| [GAM - Security Policies (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58087) | [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) | [OAuth Token expire (minutes) GAM Security Policy property (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58155) |
| [OAuthRefreshTokenExpire property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?58097) | [OauthTokenExpire property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?18577) |

---
