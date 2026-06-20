---
title: "GetSTSAuthorizationAccessToken method of GAMRepository Object"
source_id: 43218
source_url: https://wiki.genexus.com/commwiki/wiki?43218
genexus_version: "18"
---

# GetSTSAuthorizationAccessToken method of GAMRepository Object

Gets a Security Token Service (STS) authorization token.

### [Syntax](#Syntax)

*&GAMSTSAuthorizationToken* = GAMRepository**.GetSTSAuthorizationAccessToken(**in: *&Client\_id*, in: *&scope*, out: *&GAMErrors***)**

**Where:**

*&GAMSTSAuthorizationToken*  
     Is GAMSTSAuthorizationToken external object data type.  
  
`[imagen omitida: wiki id 43220]`

*&Client\_id*  
     Is the ClientID of the [GAM Application](https://wiki.genexus.com/commwiki/wiki?15910) which requests a Token to make a call to a resource afterwards ("AppA"). It's a GUID.

*&scope*  
     Is a string of the form <ApplicationName>.

**Note**: ApplicationName is the application where the resource to be called is defined ("AppB"). If there is more than one, they should be separated by the '+' sign (e.g: AppB.Prm1+AppB.Prm2...+AppB.PrmN).

*&GAMErrors*  
     Is a collection of GAMError.

### [Description](#Description)

The GAMRepository object of [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) Library has the *GetSTSAuthorizationAccessToken* method that is used to get a Security Token Service (STS) authorization token.

For more information about this scenario, read [Security Token Service Client Authorization](https://wiki.genexus.com/commwiki/wiki?43202).

Consider the example where a client application (AppA) requests access to another application (AppB) - for example, to execute a service of this application.

This method internally executes the RequestTokenService service explained [here](https://wiki.genexus.com/commwiki/wiki?43202).

### [Samples](#Samples)

```
   &GAMSTSAuthorizationToken = GAMRepository.GetSTSAuthorizationAccessToken(&client_id, &scope, &Errors)
    If &Errors.Count = 0
        &access_token = &GAMSTSAuthorizationToken.access_token
        &GAMSTSAuthorizationToken_Expires_in = &GAMSTSAuthorizationToken.expires_in.ToString()
        &GAMSTSAuthorizationToken_Scope = &GAMSTSAuthorizationToken.scope
        &GAMSTSAuthorizationToken_token_type = &GAMSTSAuthorizationToken.token_type
    Else
        msg(format(!"%1 (%2)",&Errors.Item(1).Message,&Errors.Item(1).code))
    Endif
```

**Notes:**

* The Scope property of *&GAMSTSAuthorizationToken* returned is the same as the one passed in the parameter.
* Expires in is 0 unless you create a [Security Policy](https://wiki.genexus.com/commwiki/wiki?18521) in the STS server, with an [OAuth token expire (minutes)](https://wiki.genexus.com/commwiki/wiki?18577) value different than zero. This security policy should be assigned to the user defined for the AppA STS configuration in the STS server.  
    
  Security Policy configuration:  
  `[imagen omitida: wiki id 43224]`  
    
  User configuration:  
  `[imagen omitida: wiki id 43225]`

### [Availability](#Availability)

Since [GeneXus 16 upgrade 4](https://wiki.genexus.com/commwiki/wiki?42755,,)

### [See Also](#See+Also)

* [HowTo: Configure GAM to use Security Token Service](https://wiki.genexus.com/commwiki/wiki?43206)


|  |
| --- |
| **Backlinks** |
| [GetAgentServiceHeader method of GAM object](https://wiki.genexus.com/commwiki/wiki?43221) | [HowTo: Configure GAM to use Security Token Service](https://wiki.genexus.com/commwiki/wiki?43206) |

---
