---
title: "Security Token Service Client Authorization using GAM"
source_id: 43202
source_url: https://wiki.genexus.com/commwiki/wiki?43202
genexus_version: "18"
---

# Security Token Service Client Authorization using GAM

This functionality aims to implement authentication and centralized authorization among multiple distributed client applications.

In a typical usage scenario involving the [Security Token Service](https://en.wikipedia.org/wiki/Security_token_service)(STS) standard, a client application (A) requests access to another application (B) - for example, to execute a service of this application. Application A redirect to a Security Token Service, which in turn authenticates the client and grants it a security token.   
Client A then presents the token to application B to gain access to the resources provided by the application. This application validates the token against the STS server before executing the service requested by A, and checks if A has permissions to access those resources.  
  
An example of use is the [AGESIC PDI](https://www.agesic.gub.uy/innovaportal/v/1796/9/agesic/security-token-service.html).

The solution is based on the OAuth protocol. As we use the STS standard implemented for the OAuth protocol to dialogue between the GAM Server Identity Provider and the client Applications, any client application not using GAM (or not using GeneXus) could use the GAM service as an STS Identity Provider.

To see how to configure STS using GAM, see [HowTo: Configure GAM to use Security Token Service](https://wiki.genexus.com/commwiki/wiki?43206).

To understand the architecture of this solution, see the diagram below:

##### 

So, consider that AppA needs to access a resource of AppB. This guide explains each of the steps involved in STS mechanism using GAM. Note that this guide goes on deep on the details of the HTTP headers used and other details on the HTTP request because you may need to implement some of the components manually (without using GAM).

- [(1) Request Token Service](#%281%29+Request+Token+Service)
- [(2) STS returns an access token or an error.](#%282%29+STS+returns+an+access+token+or+an+error.)
- [(3) AppA requests AppB resource](#%283%29+AppA+requests+AppB+resource)
- [(4) Query Access Token](#%284%29+Query+Access+Token)
- [(5) Permission granted or denied](#%285%29+Permission+granted+or+denied)
- [(6) Response of AppB resource.](#%286%29+Response+of+AppB+resource.)
- [Implementation details](#Implementation+details)
- [Availability](#Availability)

### [(1) Request Token Service](#%281%29+Request+Token+Service)

AppA requests an access token from the STS. This step is done automatically by GAM. The service invoked is RequestTokenService.

```
POST {ServerURL}/oauth/RequestTokenService HTTP/1.1

Headers:
Content-Type: application/x-www-form-urlencoded
Authorization: Basic {ClientCredentials}

Body:
grant_type=client_credentials
scope={Scopes}
repository={RepositoryGUID}
```

**Where:**

* {ServerURL}: Authorization service URL (STS server)
* {ClientCredentials}: String ClientID: UserPassword of the application on the STS server. It has base64 representation.
* {Scopes}: Scope of the authorization request. It's a list separated by the "+" sign indicating the scope of the resources requested. Each permission must be of the AppName.Permission format, since a token could be requested to access several applications. AppName corresponds to the name of the application on the STS Identity Provider Server.
* {RepositoryGUID}: GUID of the repository in the Server. It is optional, required only for token Servers with multi-tenant GAM.

### [(2) STS returns an access token or an error.](#%282%29+STS+returns+an+access+token+or+an+error.)

In the case that the credentials and **all** the scopes are correct, it will respond:

```
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
Cache-Control: no-store
Pragma: no-cache

{
  "access_token": "{Access Token}",
  "token_type": "Bearer",
  "expires_in": {Lifetime In Seconds},
  "scope": "{Scopes}"
}
```

**Where:**

* {Access Token}: The Access Token issued for this request.
* {Lifetime In Seconds}: The lifetime of the token in seconds.
* {Scopes}: Scope effectively granted to the Access Token.

If an error is returned:

```
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=UTF-8
Cache-Control: no-store
Pragma: no-cache

{
  "error":"{detail}"
}
```

**Where** {detail} is

* {invalid\_request}: The request omits some required parameter, repeats parameters, uses a different verb than the requested one or has some other format error.
* {invalid\_client}: A failure in client authentication occurs.
* {unsupported\_grant\_type}: The request has a different grant than expected.
* {unauthorized\_client}: The client is not authorized for the specified scope.

### [(3) AppA requests AppB resource](#%283%29+AppA+requests+AppB+resource)

The AppA has the Token to be able to consume a service from the AppB and calls the service of B:

```
POST {ServerURL}/rest/{ServiceName} HTTP/1.1
```

Headers:  
Content-Type: application/x-www-form-urlencoded  
GeneXus-Agent: STSOAuth Application  
Authorization: {AccessToken}

Body:  
client\_id={ClientID}  
repository={RepositoryGUID}

where:

* {ServerURL}: URL of AppB
* {ServiceName}: Name of the Service to be consumed
* {AccessToken}: Token obtained from the STS server (step 2)
* {ClientID}: ID of the client application in AppB
* {RepositoryGUID}: GUID of the repository in AppB. It's optional (required only if there is GAM multi-tenant in AppB).

### [(4) Query Access Token](#%284%29+Query+Access+Token)

Once a POST has been received by a REST service in AppB, GAM validates automatically the ClientID it has received. It checks if it exists in the local GAM and if it has STS enabled.  
If this is successful, it validates the AccessToken. To do so, it executes an HTTP POST to the STS server:

```
POST {ServerURL}/oauth/QueryAccessToken HTTP/1.1

Headers:
Content-Type: application/x-www-form-urlencoded
OAUTH-TOKEN: {AccessToken}

Body:
grant_type= authorization_code
```

where:

* {ServerURL}: URL of the STS server.
* {AccessToken}: Token received in the header.

### [(5) Permission granted or denied](#%285%29+Permission+granted+or+denied)

In case the Token is correct and still valid, it will respond:

```
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
Cache-Control: no-store
Pragma: no-cache

{
  "client_id": "{ClientID}",
  "scope": "{Scopes}"
}
```

**Where:**

* {ClientID}: Id of the client application that requested the Token.
* {Scopes}: Scope effectively granted to the Access Token.

If an error is returned:

```
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=UTF-8
Cache-Control: no-store
Pragma: no-cache

{
  "error":"{Detalle}"
}
```

### [(6) Response of AppB resource.](#%286%29+Response+of+AppB+resource.)

The AppB resource returns a response to AppA.

**Note**:

In AppB, GAM will register the request for that remote token in the local database in the Session GAM table.  
It will generate a local token and leave it associated with the remote token received so that the GeneXus user can access the GAMSession using the GAMSession.Get method. In consequence, he will know who is running the service in case it's needed to do additional validations.

To configure GAM for using STS see [HowTo: Configure GAM to use Security Token Service](https://wiki.genexus.com/commwiki/wiki?43206).

### [Implementation details](#Implementation+details)

There are some friendly URLs in the configuration files (web.xml and web.config) to be able to call the services RequestTokenService and QueryAccessToken.

* /oauth/RequestTokenService --> it calls artech.security.api.agamstsauthappgetacccesstoken
* /oauth/QueryAccessToken --> it calls artech.security.api.agamstsauthappvalidacccesstoken

### [Availability](#Availability)

Since [GeneXus 16 upgrade 4](https://wiki.genexus.com/commwiki/wiki?42755,,)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [GetAgentServiceHeader method of GAM object](https://wiki.genexus.com/commwiki/wiki?43221) |
| [GetSTSAuthorizationAccessToken method of GAMRepository Object](https://wiki.genexus.com/commwiki/wiki?43218) | [HowTo: Configure GAM to use Security Token Service](https://wiki.genexus.com/commwiki/wiki?43206) |

---
