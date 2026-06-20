---
title: "GAM - OAuth User Scopes"
source_id: 55603
source_url: https://wiki.genexus.com/commwiki/wiki?55603
genexus_version: "18"
---

# GAM - OAuth User Scopes

This document contains a list of the possible scopes in an authentication ([Web SSO](https://wiki.genexus.com/commwiki/wiki?25385)) or token request (OAuth 2.0), and explains the purpose of each one.

### [GAM Scopes](#GAM+Scopes)

To use several scopes you have to concatenate with “+”.

**gam\_user\_data**  
This scope allows to share the user's information detailed in the red box on the following picture.

**gam\_user\_additional\_data**  
This scope allows to share the user's dynamic attributes.  
This corresponds to the property &Application.ClientAllowGetUserAdditionalData that has to be set to TRUE.  
In the following picture it corresponds to sharing the "attributes" property.

**gam\_user\_roles**  
This scopes allows to share the user's roles.  
In the following picture it corresponds to sharing the "roles" property.

**session\_initial\_prop**  
This scopes allows to share initials properties.  
In the following picture it corresponds to sharing the "initial\_properties" property.  
For more details, see [HowTo: Send and receive properties set at login](https://wiki.genexus.com/commwiki/wiki?44824)

**session\_application\_data**  
This scopes allows to share session application data.  
In the following picture it corresponds to sharing the "application\_data" property.  
For more details, see [GetApplicationData and SetApplicationData method of GAMSession object](https://wiki.genexus.com/commwiki/wiki?21575)

**fullcontrol**  
This scopes allows to share all user data (add all scopes detailed before).

### [Other Scopes](#Other+Scopes)

In the IDP and the Client there is the possibility of declaring additional scopes (Additional Scopes), for example if you want to share/request only the email and telephone: user\_mail+user\_phone.  
  
When using [GAMRemote](https://wiki.genexus.com/commwiki/wiki?25355) or [GAMRemoteREST](https://wiki.genexus.com/commwiki/wiki?44833), if you do not select the "gam\_user\_data" scope, at least one of these scopes **must be included** in order to identify the user: **user\_guid, user\_email, user\_username or user\_external\_id**, if any of this scopes it's not requested the GAMError 5: "User identification not valid" will be displayed.

The list of additional user scopes is detailed in the red box in the image below.

`[imagen omitida: wiki id 55766]`  
  
Also as Additional Scopes you can add the Custom Attributes of a user implemented by each developer.  
For example, if the Custom Attributes EmployeeID and Salary were added to the user, the additional scopes would be: user\_EmployeeID+user\_Salary.

Code example of how to add custom attributes:

```
    &GAMUserAtt = new()
    &GAMUserAtt.Id           = !"EmployeeID"
    &GAMUserAtt.IsMultiValue = False
    &GAMUserAtt.Value        = !"123100"
    &GAMUser.Attributes.Add(&GAMUserAtt)
    &GAMUserAtt = new()
    &GAMUserAtt.Id           = !"Salary"
    &GAMUserAtt.IsMultiValue = False
    &GAMUserAtt.Value        = !"20000"
    &GAMUser.Attributes.Add(&GAMUserAtt)
    &GAMUserAtt = new()
    &GAMUserAtt.Id           = !"CompanyID"
    &GAMUserAtt.IsMultiValue = True
    &GAMUserAttMV = new()
    &GAMUserAttMV.Id        = !"GX"
    &GAMUserAttMV.Value     = !"GeneXus"
    &GAMUserAtt.MultiValues.Add(&GAMUserAttMV)
    &GAMUserAttMV = new()
    &GAMUserAttMV.Id        = !"GL"
    &GAMUserAttMV.Value     = !"Globant"
    &GAMUserAtt.MultiValues.Add(&GAMUserAttMV)
    &GAMUser.Attributes.Add(&GAMUserAtt)
    &GAMUser.Save()
```

The above code creates the Salary, Company and EmployeeID Attributes and assigns sample values to them.

To get the scope according to these attributes, the syntax is as follow: user\_<AttributeID>.

For example: user\_Salary, user\_EmployeeID.

However, the property (**&GAMApplication.ClientDoNotShareUserIDs : Boolean**) is created, which in the GAM Backoffice appears as "**Do not share user IDs**" which enables that both the User GUID and the ExternalID of the same are never sent, for this case a GUID is generated for this Client and it is returned in the external\_id field.

In additive also creates the property (**&GAMApplication.ClientAuthenticationRequestMustIncludeUserScopes : Boolean**), which in the GAM Backoffice appears as "**Authentication request must include user scopes?**" which enables that when requesting an access\_token it is not required to send the Scopes, in this case it will respond with all the Scopes that the application has enabled.

### [See Also](#See+Also)

[HowTo: Use GAM as an OAuth 2.0 provider](https://wiki.genexus.com/commwiki/wiki?45493)  
[GAM - OAuth 2.0 Endpoints to use GAM as Web IDP Server](https://wiki.genexus.com/commwiki/wiki?49817)


|  |
| --- |
| **Backlinks** |
| [Access\_token GAM Service](https://wiki.genexus.com/commwiki/wiki?45320) | [Client Configuration for GAM Remote Authentication](https://wiki.genexus.com/commwiki/wiki?37039) | [Client side configuration for GAMRemoteREST Authentication type](https://wiki.genexus.com/commwiki/wiki?44841) |
| [GAM - OAuth 2.0 Endpoints to use GAM as Web IDP Server](https://wiki.genexus.com/commwiki/wiki?49817) | [GAM - OAuth 2.0 Endpoints to use GAM as Web IDP Server (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56244) | [GAM - OAuth User Scopes (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55820) | [GAM - One Time Password (OTP)](https://wiki.genexus.com/commwiki/wiki?48197) |
| [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo - Use OAuth 2.0 endpoints to authenticate a Mini App from a Super App](https://wiki.genexus.com/commwiki/wiki?56035) | [HowTo: Use API Key to request services from an application](https://wiki.genexus.com/commwiki/wiki?56104) | [HowTo: Use GAM as an OAuth 2.0 provider](https://wiki.genexus.com/commwiki/wiki?45493) |
| [HowTo: Use OAuth 2.0 Endpoints to authenticate with GAM as REST IDP Server](https://wiki.genexus.com/commwiki/wiki?55623) | [Identity Provider Configuration for GAM Remote Authentication](https://wiki.genexus.com/commwiki/wiki?37038) | [Server side configuration for GAMRemoteREST Authentication type](https://wiki.genexus.com/commwiki/wiki?44840) |

---
