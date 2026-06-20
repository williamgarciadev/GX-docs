---
title: "OAuthAccessCodeExpire property in GAMSecurityPolicy EO"
source_id: 58098
source_url: https://wiki.genexus.com/commwiki/wiki?58098
genexus_version: "18"
---

# OAuthAccessCodeExpire property in GAMSecurityPolicy EO

Configures the time in seconds that an access\_code will remain active.

### [Syntax](#Syntax)

*&GAMSecurityPolicy.**OAuthAccessCodeExpire** = Number\_Seconds*

**Where:**

*&GAMSecurityPolicy*  
   Is a variable based on the GAMSecurityPolicy data type.

*Number\_Seconds*  
  Time in seconds that an access\_code will remain active.

### [Description](#Description)

This property defines the maximum time (in seconds) available for a Client application to log into the Identity Provider (IDP). It is the time that can elapse from the time the user enters their credentials until it finishes getting the access\_token in the client.

By default, this property is set to 180 seconds. It can't be 0.

In the [Standard OAuth 2.0 flow](https://wiki.genexus.com/commwiki/wiki?49817), the access code (code) is provided by the Identity Provider (IDP) to the Client Application when the user's credentials are validated in the IDP (signin step). Next, this access code is sent by the Client Application in the request to the IDP to obtain an access\_token (access\_token step) and complete the login. The access code is valid for a single use.

**Note**: When using the [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935), this property is shown with the description “OAuth access\_code expiration”.

## [Samples](#Samples)

To set this property in the GeneXus code (by using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)), the syntax is as follows:

```
&GAMSecurityPolicy.OAuthAccessCodeExpire = 200 //seconds
```

## [See Also](#See+Also)

[GAM - OAuth 2.0 Endpoints to use GAM as Web IDP Server](https://wiki.genexus.com/commwiki/wiki?49817)  
[HowTo: Use OAuth 2.0 Endpoints to authenticate with GAM as REST IDP Server](https://wiki.genexus.com/commwiki/wiki?55623)  
[GAM - OAuth 2.0 Authentication Type](https://wiki.genexus.com/commwiki/wiki?39484)


|  |
| --- |
| **Backlinks** |
| [GAM - Security Policies](https://wiki.genexus.com/commwiki/wiki?18521) |

---
