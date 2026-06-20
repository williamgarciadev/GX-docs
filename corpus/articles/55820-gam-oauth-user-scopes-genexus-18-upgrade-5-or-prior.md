---
title: "GAM - OAuth User Scopes (GeneXus 18 Upgrade 5 or prior)"
source_id: 55820
source_url: https://wiki.genexus.com/commwiki/wiki?55820
genexus_version: "18"
---

# GAM - OAuth User Scopes (GeneXus 18 Upgrade 5 or prior)

This document contains a list of the possible scopes in an authentication ([Web SSO](https://wiki.genexus.com/commwiki/wiki?25385)) or token request (OAuth 2.0), and explains the purpose of each one.

### [GAM Scopes](#GAM+Scopes)

To use several scopes you have to concatenate with “+”.

#### [gam\_user\_data](#gam_user_data)

This scope allows to share the user's information detailed in the red box on the following picture.

#### [gam\_user\_additional\_data](#gam_user_additional_data)

This scope allows to share the user's dynamic attributes.   
This corresponds to the property &Application.ClientAllowGetUserAdditionalData that has to be set to TRUE.  
In the following picture it corresponds to sharing the "attributes" property.

#### [gam\_user\_roles](#gam_user_roles)

This scopes allows to share the user's roles.   
In the following picture it corresponds to sharing the "roles" property.

gam\_session\_initial\_prop

This scopes allows to share initials properties.   
In the following picture it corresponds to sharing the "initial\_properties" property.

For more details, see [HowTo: Send and receive properties set at login](https://wiki.genexus.com/commwiki/wiki?44824)

#### [fullcontrol](#fullcontrol)

This scopes allows to share all user data.

In addition, you can request as much as possible from the user.

`[imagen omitida: wiki id 55766]`

Also, the user can have Custom Attributes, to request those attributes, for example if the user has an ID,Company and a Salary:

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

### 

### [See Also](#See+Also)

[HowTo: Use GAM as an OAuth 2.0 provider](https://wiki.genexus.com/commwiki/wiki?45493)  
[GAM - OAuth 2.0 Endpoints to use GAM as Web IDP Server](https://wiki.genexus.com/commwiki/wiki?49817)
