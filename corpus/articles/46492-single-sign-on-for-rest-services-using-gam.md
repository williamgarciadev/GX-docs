---
title: "Single Sign On for Rest Services using GAM"
source_id: 46492
source_url: https://wiki.genexus.com/commwiki/wiki?46492
genexus_version: "18"
---

# Single Sign On for Rest Services using GAM

This functionality aims to solve centralized authentication between multiple distributed Rest Services.

Consider the scenario where App A wants to invoke a Rest service of App B and, for that, there is a centralized authentication entity that gives App A the token to call the secure Rest service of B.

It's similar to Single Sign On (SSO), except that the login to the centralized authentication entity (the Identity Provider) is done using Rest (not by using a UI).

Some characteristics of this authentication type are as follows:

* The user enters his credentials in a local login and is not redirected to the Identity Provider's login as in [GAM Remote Authentication](https://wiki.genexus.com/commwiki/wiki?25355). The Identity Provider (IDP) is the owner of the user credentials, as always.
* The login is done using [Remote Rest Authentication type (OAuth 2.0)](https://wiki.genexus.com/commwiki/wiki?44833) against the IDP.
* After login, the client app can get from the IDP an *SSO Rest Token* which enables the app to call a Rest service of another app (different than the IDP) which is subscribed to this scheme.

This page contains the following:

* [Architecture overview](#Architecture+overview)
* [Use Cases](#Use+Cases)
* [Implementation](#Implementation)
* [Configuration](#Configuration)

+ [Server-side configuration](#Server-side+configuration)
+ [Client-side configuration](#Client-side+configuration)

* [Sample](#Sample)
* [Availability](#Availability)

### [Architecture overview](#Architecture+overview)

The following is a simplified scheme of the solution. It's based on OAuth 2.0 protocol. For more information, read the Implementation section below.

Suppose that you have 3 KBs (App A, App B, and the IDP). All of them have GAM activated.

1. From App A, log in to the Identity Provider (IDP) using Remote Rest Authentication type (OAuth 2.0).  
   {ClientId + Credentials + Scopes + <RepositoryGUID>} are sent to the IDP.
2. The IDP answers with an access token.
3. Ask for user information.  
   {access token} is sent to the IDP.
4. The IDP answers with user information.
5. Generate GAM session at the IDP.
6. Generate local GAM session in App A.
7. Post to Rest Service of App B.  
   {Authorization: <*SSO Rest Token*>} is sent as an authorization header. The Client ID is sent in the HTTP body request.
8. Using the *SSO Rest Token* received, App B requests a token and User Info to the IDP.  
   {Authorization: <*SSO Rest Token*>} is sent as an authorization header. The Client ID is sent in the HTTP body request.
9. The Token and User info is returned from the IDP to App B.
10. A local GAM session is generated in App B.
11. App B sends the Rest service response to App A.  
      
    `[imagen omitida: wiki id 46494]`

### [Use Cases](#Use+Cases)

As stated above, the use scenario is to have more than one application, which must interact with each other calling Rest services. Once the user has logged in one of them (against an Identity Provider configured to return an SSO Rest token) the application can use this token to call a Rest service of any other application which is subscribed to this scheme.

### [Implementation](#Implementation)

When the user logs in, the client makes a call to ask for a valid token using the following URL:

```
$ServerURL/oauth/gam/v2.0/access_token
```

The user's information is requested through this HTTP request:

```
POST $ServerURL/oauth/gam/v2.0/RequestTokenAndUserInfo HTTP/1.1
```

### [Configuration](#Configuration)

All the KBs need to have [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) activated.

#### [Server-side configuration](#Server-side+configuration)

See [Server-side configuration for SSO in REST applications](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46496,,)

#### [Client-side configuration](#Client-side+configuration)

See [Client-side configuration for SSO in REST applications](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46499,,)

### [Sample](#Sample)

The &GAMSession.SSORestToken property can be used to get the *SSO Rest Token* to call a Rest service subscribed to the same scheme.

```
        &GAMSession = GAMSession.Get(&GAMErrorCollection) 
        if not &GAMSession.SSORestToken.IsEmpty()
       
        &httpClient.AddHeader(!"Content-Type", !"application/x-www-form-urlencoded")
        &httpClient.AddHeader(!"Authorization", &GAMSession.SSORestToken )

        &httpClient.Execute(HttpMethod.Post, &StrCall )
        &ResultHttpC = &httpClient.ToString()
        
       endif
```

### [Availability](#Availability)

Since [GeneXus 17](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46066,,).


|  |
| --- |
| **Backlinks** |
| [GAM - GAMRemoteREST Authentication type (OAuth 2.0)](https://wiki.genexus.com/commwiki/wiki?44833) |
| [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
