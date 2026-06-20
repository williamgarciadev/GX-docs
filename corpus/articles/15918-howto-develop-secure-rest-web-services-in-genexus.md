---
title: "HowTo: Develop Secure REST Web Services in GeneXus"
source_id: 15918
source_url: https://wiki.genexus.com/commwiki/wiki?15918
genexus_version: "18"
---

# HowTo: Develop Secure REST Web Services in GeneXus

This document explains how to Develop Secure [Rest web services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28213) and provides a brief overview about it.

[REST Web Services](https://wiki.genexus.com/commwiki/wiki?14573) security is based on [OAuth](http://oauth.net/).

Several applications usually expose data update services and data recovery services through [REST](http://es.wikipedia.org/wiki/Representational_State_Transfer), so security is very important regarding data privacy.

In GeneXus, the solution to this problem is to use [GAM](https://wiki.genexus.com/commwiki/wiki?24746) (which hides to the final user the complexity of OAuth technology).

The [GAM API](https://wiki.genexus.com/commwiki/wiki?16535) provides a way to restrict access to users to [REST Web Services](https://wiki.genexus.com/commwiki/wiki?14573) defined in the application.

The following guide explains the steps to follow to incorporate security into your REST web services, and the way to consume these web services from a GeneXus application, too. The way to consume web services from a non-GeneXus application should follow the same main idea.

**Note**: If the consumer application uses GAM, since GeneXus 16 upgrade 7 you can implement this solution based on [Remote Rest Authentication type (OAuth 2.0)](https://wiki.genexus.com/commwiki/wiki?44833)

In this example, the token is obtained manually using HTTP since the consumer application hasn't got GAM, or is of a version lower than GeneXus 16 u7 (GAM Remote Rest is not supported)

### [From the perspective of the "REST web services" Knowledge Base](#From+the+perspective+of+the+%22REST+web+services%22+Knowledge+Base)

**1.** Create the [REST Web Services](https://wiki.genexus.com/commwiki/wiki?14573) of your application. The REST web services can be [Business Component](https://wiki.genexus.com/commwiki/wiki?5846), [Data Providers](https://wiki.genexus.com/commwiki/wiki?5270), or [Procedures](https://wiki.genexus.com/commwiki/wiki?6293), and can expose POST, PUT, DELETE, GET methods.

**2.** Check the security property in the Knowledge Base ([Enable Integrated Security Property](https://wiki.genexus.com/commwiki/wiki?14706)). Afterward, GAM objects will be incorporated into the KB, a reorganization will be done to create a GAM repository, and then this repository will be initiated. For more details see [GeneXus Administration of GAM Repository](https://wiki.genexus.com/commwiki/wiki?15769).

**3.** Create an [application](https://wiki.genexus.com/commwiki/wiki?15910) using GAM API (or just using the [GAM Backend](https://wiki.genexus.com/commwiki/wiki?15935)) in order to identify the "REST web services application" within the GAM repository.

**4.** Create a user which will have access rights to your application. If you want to restrict access to some users, you need to configure [GAM Permissions](https://wiki.genexus.com/commwiki/wiki?15912).

Note that the GAM Examples include a web application (Backend) that facilitates the administration of [Applications](https://wiki.genexus.com/commwiki/wiki?15910), [GAM Roles](https://wiki.genexus.com/commwiki/wiki?17569), Users, and [Permissions](https://wiki.genexus.com/commwiki/wiki?15912).  
  
**5.** In order to enable access to the REST services, you need to provide the Client\_Id, user, and password to the consumer.  
  
Take a look at "GAMExampleApplicationEntry" object (which belongs to the GAM Examples) to see how to use the GAM API to get the Client\_Id.  
In particular, if you run GAMExampleWWApplications, when you edit the Application properties of any Application of the Repository, you can see the Client\_Id of the Application.

`[imagen omitida: wiki id 32325]`

### [From the perspective of the client application, consumer of "REST web services" Knowledge Base](#From+the+perspective+of+the+client+application%2C+consumer+of+%22REST+web+services%22+Knowledge+Base)

In OAuth there is the concept of Client (application), User (userId, userPwd), and permissions (Scope= Read, Write,FullControl).

A GeneXus application that is configured to use GAM generates a Client Id for each [application](https://wiki.genexus.com/commwiki/wiki?15910).

To consume a secure GX REST web service you should:

**1.** Be provided with the Client\_Id of the Application, user, and password with access rights to this application.  
  
**2.** Get an [access\_token](https://wiki.genexus.com/commwiki/wiki?45320) before trying to POST to the web service. To get this access\_token, you have to POST the Client\_Id and user credentials or to use the GAMRepository.GetOauthAccessToken() method. The detailed steps are as follows:

1. First, get the [access\_token](https://wiki.genexus.com/commwiki/wiki?45320).

* **POST** to this URL

*HTTP://<SERVER>/<APPDIR>/oauth/access\_token*  
  
with this body:

```
client_id=<client_id>&grant_type=password&scope=FullControl&username=<user_name>&password=<user_pwd>
```

Example:

```
client_id=f719771ad52a42919a221bc796d0d6b0&granttype=password&scope=FullControl&username=admin&password=admin123
```

In the HTTPResponse, there'll be a JSON response with the access\_token, as this example shows:

```
{
  "access token" : "c9919e10e118"   << Access token which will have to be used in all subsequent calls
  "scope" : "FullControl"
}
```

**Note**: Since GeneXus 16 upgrade 8, the GAMRepository.GetOauthAccessToken() is available.

* Use the method GetOauthAccessToken

```
GAMRepository.GetOauthAccessToken(&UserName, &Password, &GAMLoginAdditionalParameters, &GAMOauthAdditionalParameters, &GAMSession, &GAMErrors)
```

Example:

```
&GAMOauthAdditionalParameters.ClientId = "f719771ad52a42919a221bc796d0d6b0"
&GAMOauthAdditionalParameters.ClientSecret = &ClientSecret
&GAMLoginAdditionalParameters.AuthenticationTypeName = !"local"
&AccessTokenSDT = GAMRepository.GetOauthAccessToken(!"admin", !"admin123",&GAMLoginAdditionalParameters,&GAMOauthAdditionalParameters,&GAMSession,&GAMErrors)
```

2. All the calls to the REST web services should include this header (following the same example):

```
Authorization: OAuth c9919e10e118
```

The following example is a complete sample code that shows how to GET the products list ("DPProduct" is a Data Provider exposed as REST web service), which is a secure web service (GAM is enabled in the KB).  
The Client Id is taken from the application defined automatically in GAM Backend.

Use HTTPClient data type to consume the REST web service.

```
//First get the access_token through an HTTP POST

&addstring ='client_id=be47d883307446b4b93fea47f9264f88&grant_type=password&scope=FullControl&username=test&password=test'

&httpclient.Host= &server
&httpclient.Port = &port

&httpclient.BaseUrl = &urlbase + '/oauth/'  
&httpclient.AddHeader("Content-Type", "application/x-www-form-urlencoded")
&httpclient.AddString(&addstring)
&httpclient.Execute('POST','access_token')

&httpstatus = &httpclient.StatusCode
msg('Http status: ' + &httpstatus,status)
&result = &httpclient.ToString()

&AccessTokenSDT.FromJson(&result) // Load the AccessToken in a SDT which has this structure (*)

//call DPProduct web service

&httpclient.BaseUrl = &urlbase + '/rest/'
&httpclient.AddHeader("Content-Type", "application/json")
&httpclient.AddHeader('Authorization','OAuth ' + &AccessTokenSDT.access_token)
&httpclient.AddHeader("GENEXUS-AGENT","SmartDevice Application")
&httpclient.Execute('GET','DPProduct')
```

This is another example, this time using the GAMRepository.GetOauthAccessToken() method

```
//First get the access_token 
&httpclient.Host= &server
&httpclient.Port = &port

&GAMOauthAdditionalParameters.ClientId = "f719771ad52a42919a221bc796d0d6b0"
&GAMOauthAdditionalParameters.ClientSecret = &ClientSecret
&GAMLoginAdditionalParameters.AuthenticationTypeName = !"local"
&AccessTokenSDT = GAMRepository.GetOauthAccessToken(!"admin", !"admin123",&GAMLoginAdditionalParameters,&GAMOauthAdditionalParameters,&GAMSession,&GAMErrors)

//call DPProduct web service
&httpclient.BaseUrl = &urlbase + '/rest/'
&httpclient.AddHeader("Content-Type", "application/json")
&httpclient.AddHeader('Authorization','OAuth ' + &AccessTokenSDT.access_token)
&httpclient.AddHeader("GENEXUS-AGENT","SmartDevice Application")
&httpclient.Execute('GET','DPProduct')
```

**Note**: Since [GeneXus 16 upgrade 4](https://wiki.genexus.com/commwiki/wiki?42755,,) you can also get the user information when calling a secure Rest service. For more information on this topic, see [SAC 45678](https://www.genexus.com/developers/websac?en,,,45678).

### [Calling a Rest service which runs under a multitenant architecture](#Calling+a+Rest+service+which+runs+under+a+multitenant+architecture)

In the case that the service runs on a server which serves multiple tenants (the GAM has *n* repositories, each for a different tenant), you have to add some additional information to the body of the HTTP Post in order to establish which repository GAM should connect to. In this case, the *connection.gam* on the server has one [Repository connections](https://wiki.genexus.com/commwiki/wiki?16150) for each Repository.

This is done using the additional\_parametes of the body, which is a JSON including the AuthenticationTypeName and the Repository (the GUID of the Repository you're going to connect to).

Example of an HTTP post to access\_token service including the additional\_parameters mentioned:

```
POST /Customer1.NetEnvironment/oauth/access_token HTTP/1.1
GeneXus-Agent: SmartDevice Application
Content-Length: 248
Content-Type: application/x-www-form-urlencoded
Host: 10.0.2.2:88

client_id=ad80c07c0a1046029c0655cdd9d99493&grant_type=password&scope=FullControl&username=adminfull&password=adminfull&additional_parameters={"AuthenticationTypeName":"local","Repository":"1e89a9ca-bc52-482b-a344-c4cda4a9cc8f"}
```

**Notes:**

* The Genexus-Agent:*SmartDevice Application* header is mandatory since Xev2u4.
* The grant\_type in the json body sent to the "access\_token" service maps to the [Authentication Types for GAM](https://wiki.genexus.com/commwiki/wiki?16508), so "password" means Local Authentication, and the other possible values are Facebook, Twitter, Google, externalwebservice, custom, and device (for [Auto Registration](https://wiki.genexus.com/commwiki/wiki?19912)).
* In case that you get *Error39: application not found*, consider adding the following header: Content-Type: application/x-www-form-urlencoded

`[imagen omitida: wiki id 15920]`

Note that the user information can be obtained after the successful authentication, using the GAMUser static methods.

It's recommended to use HTTPS so the communication channel between client and server is secure.

### [See Also](#See+Also)

[Secure Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?16052)  
[Troubleshooting secure rest services](https://wiki.genexus.com/commwiki/wiki?29439,,)


|  |
| --- |
| **Backlinks** |
| [GAM - Authentication Scenarios](https://wiki.genexus.com/commwiki/wiki?15937) | [GAM - GAMRemoteREST Authentication type (OAuth 2.0)](https://wiki.genexus.com/commwiki/wiki?44833) | [HowTo: Access secure REST services defined via API Objects](https://wiki.genexus.com/commwiki/wiki?52864) |
| [HowTo: Use Postman to access secure REST services defined via API Objects](https://wiki.genexus.com/commwiki/wiki?50055) | [OAuth token expire (minutes)](https://wiki.genexus.com/commwiki/wiki?18577) |
| [Toc:Rest web services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28213) | [Secure Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?16052) |

---
