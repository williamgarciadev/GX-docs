---
title: "TimeoutToFinishOAuthAuthenticationUsingIDP property in GAMRepository EO"
source_id: 58086
source_url: https://wiki.genexus.com/commwiki/wiki?58086
genexus_version: "18"
---

# TimeoutToFinishOAuthAuthenticationUsingIDP property in GAMRepository EO

Configures the time, in minutes, that the State will remain valid when a client authenticates using OAuth 2.0 to an Identity Provider (IDP).

### [Syntax](#Syntax)

*&GAMRepository.**TimeoutToFinishOAuthAuthenticationUsingIDP** = Number\_Minutes*

**Where:**

*&GAMRepository*  
Is a variable based on the GAMRepository data type.

*Number\_Minutes*  
Number of minutes that the State will remain valid when a client authenticates using OAuth 2.0 to an Identity Provider (IDP).

### [Description](#Description)

This is a [GAMRepository](https://wiki.genexus.com/commwiki/wiki?17568) property that allows you to configure the time, in minutes, that the State **will remain valid** when a client authenticates using OAuth 2.0 to an Identity Provider (IDP).  
  
By default, this property is set to 15 minutes. Its value can't be 0.  
  
If a specific value is set for this property in the Identity Provider repository configuration, and the user does not complete the credentials in the specified time, they will be redirected to the login object with the error: GAM533 “State IDP Expired” and will have to log in again.

**Note**: When using the GAM Backoffice, this property can be configured by selecting **Repository > Configuration > General Security Policy**. It is shown with the description "Timeout to finish OAuth authentication (state) using an IDP (minutes)".

### [Samples](#Samples)

To set this property in the GeneXus code (by using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)), the syntax is as follows:

```
&GAMRepository.TimeoutToFinishOAuthAuthenticationUsingIDP = 10
```

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244).

### [See Also](#See+Also)

[GAM - GAMRemote Authentication Type](https://wiki.genexus.com/commwiki/wiki?25355)  
[Client Configuration for GAM Remote Authentication](https://wiki.genexus.com/commwiki/wiki?37039)  
[Identity Provider Configuration for GAM Remote Authentication](https://wiki.genexus.com/commwiki/wiki?37038)  
[GAM Repository features and properties](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18463,,)


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244) |

---
