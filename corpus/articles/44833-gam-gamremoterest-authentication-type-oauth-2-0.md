---
title: "GAM - GAMRemoteREST Authentication type (OAuth 2.0)"
source_id: 44833
source_url: https://wiki.genexus.com/commwiki/wiki?44833
genexus_version: "18"
---

# GAM - GAMRemoteREST Authentication type (OAuth 2.0)

The GAMRemoteREST authentication type allows an application using GAM to use another GAM as an Identity Provider. The user will log in to the application using credentials that are stored in an Identity Provider (IDP).

So, there is a client application (Web or SD, with its own GAM) and an Identity Provider (using GAM) where the user will be authenticated.

In general, this solution is used in a trusted environment, because the user's credentials are entered by the client and flow through that application.

The following is a **very simplified** schema about this solution (implementation details are shown below).

1. The user enters his credentials at the client application.
2. These credentials (and other information, which we detail afterwards) are used to call the Identity Provider's REST authentication services, where the user is authenticated.
3. The Identity Provider sends a response to the caller, and then it returns to the client application (with an error if the authentication fails).

`[imagen omitida: wiki id 44946]`

It's very similar to [GAMRemote Authentication Type](https://wiki.genexus.com/commwiki/wiki?25355) (as it uses OAuth 2.0), but in this case the login is done using REST. So there is no redirection to the Identity Provider's login as in [the SSO scenario](https://wiki.genexus.com/commwiki/wiki?25385).

Some characteristics of this authentication type are:

1. The user enters his credentials in a local login and is not redirected to the Identity Provider's login as in GAM Remote authentication. The Identity Provider is the owner of the user credentials, as always.
2. In fact, the login is done using the same protocol as GAM Remote (OAuth 2.0).

### [Cases for use](#Cases+for+use)

As explained above, in general it will be used in a trusted environment, for credentials are entered at the client.

1. It proves especially useful when you need a token to call a service running under another GAM.

   After the login, a GAMSession is generated at the Identity Provider's GAM and at the client's (the same as with GAM Remote Authentication). The GAMSession has the local token and the external token, to be used for calling any REST service (depending on whether the service is hosted at the client or at the server).

   So, if you need to consume a REST service using GAM from an application that uses GAM as well, you may authenticate to the provider application using GAMRemoteRest authentication type to get a valid token, instead of [using HTTP calls](https://wiki.genexus.com/commwiki/wiki?15918).
2. In case of a Smart Devices app, where you need to authenticate against an Identity Provider and want to avoid the user from being redirected to the IDP's web login.

### Architecture and implementation

The following is an architecture schema (though it does not fully show its complexity, it's useful for understanding what happens under the hoods).

`[imagen omitida: wiki id 44880]`

When the user logs in, instead of redirecting to the Identity Provider, the client makes a call to ask for a valid token, using the following URL:

```
$ServerURL/oauth/gam/v2.0/access_token
```

The information of the user is requested at this URL

```
$ServerURL/oauth/gam/v2.0/userinfo
```

### [Example](#Example)

Calling a REST service running at the client's KB.

First, you log in using GAMRemoteREST.

```
&AdditionalParameter.AuthenticationTypeName = !"gamremoterest" //&AdditionalParameter is of GAMLoginAdditionalParameters data type
&LoginOK = GAMRepository.Login(&user, &password, &AdditionalParameter, &GAMErrors)
```

Then, at any time you can get the Token from the GAMSession to call the REST service.

```
&AccessToken = GAMSession.GetToken()
//Here call REST Service using the Authorization headers.
&httpclient.AddHeader(!"Authorization",!"OAuth " + &AccessToken)
&httpclient.AddHeader(!"GeneXus-Agent",!"SmartDevice Application")
&httpclient.Execute(&method,&getstring) //E.g: &httpclient.Execute(!"GET",!"http://server/baseurl/rest/GetCustomers")
```

The GAMSession.GetToken() method returns the local Token (useful for calling a service of the client KB). Note that for this token, applicable security policies are the web (not OAuth, so the time out expiration of this token is the Web session timeout).

If you want to call a service of the server KB, you must get the external token (to be passed in the authorization headers) using the following:

```
&GAMSession = GAMSession.Get(&GAMErrors)
&AccessToken = &GAMSession.ExternalToken
```

### [GAMRemoteREST authentication for mobile apps](#GAMRemoteREST+authentication+for+mobile+apps)

Take a look at [GAM Login Method](https://wiki.genexus.com/commwiki/wiki?19269).

### [Configuration](#Configuration)

#### [**Server side configuration**](#Server+side+configuration)

See [Server side configuration for GAMRemoteREST Authentication type](https://wiki.genexus.com/commwiki/wiki?44840).

#### [**Client side configuration**](#Client+side+configuration)

See [Client side configuration for GAMRemoteREST Authentication type](https://wiki.genexus.com/commwiki/wiki?44841).

### [Availability](#Availability)

As from [GeneXus 16 upgrade 7](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?44454,,).

### [See Also](#See+Also)

[Single Sign On for Rest Services using GAM](https://wiki.genexus.com/commwiki/wiki?46492)


|  |
| --- |
| **Backlinks** |
| [Client side configuration for GAMRemoteREST Authentication type](https://wiki.genexus.com/commwiki/wiki?44841) | [Client side configuration for GAMRemoteREST Authentication type (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?57064) |
| [GAM - OAuth User Scopes](https://wiki.genexus.com/commwiki/wiki?55603) | [GAM - Two Factor Authentication (2FA)](https://wiki.genexus.com/commwiki/wiki?48254) |
| [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Develop Secure REST Web Services in GeneXus](https://wiki.genexus.com/commwiki/wiki?15918) | [HowTo: Send and receive properties set at the login](https://wiki.genexus.com/commwiki/wiki?44824) | [Server side configuration for GAMRemoteREST Authentication type](https://wiki.genexus.com/commwiki/wiki?44840) |
| [Server side configuration for GAMRemoteREST Authentication type (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?57068) | [Single Sign On for Rest Services using GAM](https://wiki.genexus.com/commwiki/wiki?46492) |

---
