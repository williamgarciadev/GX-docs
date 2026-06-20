---
title: "HowTo: Configure GAM to use Security Token Service"
source_id: 43206
source_url: https://wiki.genexus.com/commwiki/wiki?43206
genexus_version: "18"
---

# HowTo: Configure GAM to use Security Token Service

This guide shows how to configure GAM to use Security Token Service (STS).

In this scenario, a client application (AppA) requests access to another application (AppB) - for example, to execute a service of this application. Application A redirects to a Security Token Service, which in turn authenticates the client and grants it a security token.   
Client A then presents the token to application B to gain access to the resources provided by the application. This application validates the token against the STS server before executing the service requested by A and checks if A has permissions to access those resources.

For more information on this topic, see [Security Token Service Client Authorization using GAM](https://wiki.genexus.com/commwiki/wiki?43202).

### [STS server configuration](#STS+server+configuration)

1. In the GAM Identity Provider STS, each application that can request an STS Token (e.g.: AppA) must be configured.

`[imagen omitida: wiki id 43207]`

In each [GAM Application](https://wiki.genexus.com/commwiki/wiki?15910) you must configure a Client ID (Client Application Identifier). You must enable the STS protocol and configure STS Mode = Server (Token Server).

`[imagen omitida: wiki id 43208]`

A user must be created for each application, which may be exclusively a local user; in this case, a user named "user1" was created and assigned to AppA application.  
This user will be used to validate scopes received when requesting a token. All token requests must have a valid scope (it can be more than one), and all must be valid for a token to be returned.

2. In the GAM STS Identity Provider, you must also configure the application for which you want to request a Token, in our scheme "AppB."

Note that you have to set [Require Access Permissions Application Property](https://wiki.genexus.com/commwiki/wiki?18512) to True. On the other hand, the STS server will only authenticate and will return a token regardless of the Application rights to be accessed.

`[imagen omitida: wiki id 43211]`

AppB must have defined the Permissions that AppA will use to call it.

`[imagen omitida: wiki id 43222]`

The user defined ("user1") has to have those permissions (it can be through roles or directly assigned to the user):

`[imagen omitida: wiki id 43213]`

### [Configuring GAM in "AppA"](#Configuring+GAM+in+%22AppA%22)

This is to configure GAM where the request of a service will be executed.

In the Client KB, named in the example as "AppA," that application must exist. It must be defined as "AppA" with the same Client ID as in the IP Server STS.

`[imagen omitida: wiki id 43214]`

In addition, it must have enabled the STS protocol and configured STS Mode = Get token.  
The Client Password is the password of the user of this App in the STS Identity Provider (in the example, it is the password of "user1"). Finally, configure the URL of the STS server.

`[imagen omitida: wiki id 43215]`

To call the service in AppB from AppA, you should use the [GetSTSAuthorizationAccessToken method](https://wiki.genexus.com/commwiki/wiki?43218) to get the correct authorization header, and the [GetAgentServiceHeader method](https://wiki.genexus.com/commwiki/wiki?43221) to get the appropriate headers to call the service.

#### [Example](#Example)

```
&client_id = !"8e2ec1ea4058491c93c1bfe3bc90a5ad"
&scope = !"AppB.Prm1+AppB.Prm2"
&GAMSTSAuthorizationToken = GAMRepository.GetSTSAuthorizationAccessToken(&client_id, &scope, &GAMErrors)
If &Errors.Count = 0
    &access_token = &GAMSTSAuthorizationToken.access_token
    GAM.GetAgentServiceHeader(GAMServiceTypesHeader.STSOauth, &HeaderName, &HeaderValue)
    &StrCall = "http://localhost/ClientSTS2.NetEnvironment/rest/ProcRest_testSTS"
    &httpClient.AddHeader(&HeaderName, &HeaderValue)
    &httpClient.AddHeader(!"Content-Type",!"application/x-www-form-urlencoded")
    &httpClient.AddHeader(!"Authorization", &access_token)
    &httpClient.AddVariable(!"client_id", &client_id) //Note that the &client_id is passed as a variable in the body of the request.
    &httpClient.Execute(!"POST", &StrCall)

    msg(format(!"ErroCode %1 (%2)",&httpClient.ErrCode.ToString() + !" " + &httpClient.ErrDescription))
    msg ("Service Result:" + &httpClient.ToString())

   if &httpClient.ErrCode <> 0
     //Process Error
   Endif

Else
    msg(format(!"%1 (%2)",&Errors.Item(1).Message,&Errors.Item(1).code))
Endif
```

You should check if there is an [error](https://wiki.genexus.com/commwiki/wiki?27734,,), and take action.

For example, consider that you execute the code above and have the following error:

*ErrCode 1 (The remote server returned an error: (401) Unauthorized.)  
Service Result: {"error":{"code":"280","message":"http:\/\/localhost\/ServerSTS.NetEnvironment\/oauth\/QueryAccessToken access error (expired\_token). Please contact the application administrator."}}{}*

The first error line is thrown by the code : msg(format(!"ErroCode %1 (%2)",&httpClient.ErrCode + !" " + &httpClient.ErrDescription))  
The second one is thrown by: msg ("Service Result:" + &httpClient.ToString())

This error means that you have to ask for a new token because the one that you are using has expired.

### [Configuring GAM in "AppB"](#Configuring+GAM+in+%22AppB%22)

This is to configure GAM in the KB where the service that will be called by AppA runs.   
The service to be invoked has to have [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) = Authentication (or Authorization).  
In this KB, the [Application ID property](https://wiki.genexus.com/commwiki/wiki?18667) is set to the value of the client ID of AppB. So, the application.gam file (which contains the web [GAM Application](https://wiki.genexus.com/commwiki/wiki?15910)) references the AppB.

In GAM, the same "AppA" must be defined **with the same Client ID as defined before** (in theIP Server STS), in order to enable this application to consume services using an STS Token.  
You must have the STS protocol enabled and configure STS Mode = Check token.  
Define a local user for the local sessions of GAM to be generated (in the example we call it "user1" but it can be any).  
In addition, configure the URL of the server where AppA requests the tokens (STS server).

`[imagen omitida: wiki id 43217]`

AppB in GAM of App B must have defined the Permissions that AppA will use to call it.

Notes:

When it throws the error 60 (Missing required data (scope)), it is that the SCOPE sent is not mapped with the WEB application of that KB. This mapping is done by application name. If the App is called AppB, the received scope must be AppB.Prm1.  
When it throws the error 153 (Permission not found), it is that the Prm1 permission is not defined in the web app.

The local user in this GAM is used when a Service of AppB is called by AppA. If the STS token is correct, a local session related to this user and AppA will be generated, to have registered in the database that the service was executed by a remote application. This will allow the service to know who is running it (the user of AppA) using the GAM methods in the same way it is used if the service is executed using a local token of this KB (for example you could use GAMUser.GetId method).

**Summary**

Note that you only need to configure the environment, and consider some aspects to call the resources provided by AppB.  
When you call the Rest service in AppB, the invocation to RequestTokenService is executed automatically by GAM when you use the [GetSTSAuthorizationAccessToken method](https://wiki.genexus.com/commwiki/wiki?43218).

Then, GAM executes the invocation to QueryAccessToken automatically and continues with the execution of the service in AppB, if there is no security error. On the other hand, it throws an error that is received by the consumer in AppA.

**Availability**

Since [GeneXus 16 upgrade 4](https://wiki.genexus.com/commwiki/wiki?42755,,)

**Troubleshooting**

In case any error occurs, you can [generate a GAM trace](https://wiki.genexus.com/commwiki/wiki?25395,,), and the information is shown in the logs.

As the information of GAM is thrown in the generator's trace, in the case of NET the ASP Net trace ([Log output property](https://wiki.genexus.com/commwiki/wiki?39568) = ASP.NET trace) is very useful to see the headers and the variables sent in the body of the HTTP requests.

Note that depending on the error displayed, you may need to generate the trace in some or all the components (STS server, "AppA" server, and "AppB" server).  
For example, the RequestTokenService is executed against the STS server, so in the server, you can see the details of the invocation.

`[imagen omitida: wiki id 43241]`

There's a section of the trace where you can see:

`[imagen omitida: wiki id 43242]`

In the "AppA" side (where the invocation has been done), you can see in the trace (this information is written by GAM):

|  |  |
| --- | --- |
| 2019-05-21 13:06:55,954 <35> DEBUG GeneXus.Http.Client.GxHttpClient - Start HTTPClient buildRequest: requestUrl: method:POST name:http://localhost/ServerSTS.NetEnvironment/oauth/RequestTokenService | 0.017558 |
| GeneXus.Http.Client.GxHttpClient | 2019-05-21 13:06:55,954 <35> DEBUG GeneXus.Http.Client.GxHttpClient - Start SendStream.Read: BytesRead 0 |
| GeneXus.Http.Client.GxHttpClient | 2019-05-21 13:06:57,102 <35> DEBUG GeneXus.Http.Client.GxHttpClient - Reading response... |
| GeneXus.Http.Client.GxHttpClient | 2019-05-21 13:06:57,102 <35> DEBUG GeneXus.Http.Client.GxHttpClient - BytesRead 192 |
| GeneXus.Http.Client.GxHttpClient | 2019-05-21 13:06:57,102 <35> DEBUG GeneXus.Http.Client.GxHttpClient - BytesRead 0 |
| GeneXus.Http.Client.GxHttpClient | 2019-05-21 13:06:57,102 <35> DEBUG GeneXus.Http.Client.GxHttpClient - \_responseString {"access\_token":"2819262c-cdfd-4389-a1b3-b6548ec96add!2cb084f437f88ea7ec0d2c6b7c420fd2ff877447e7b7392f876cbaed9bdf54b6a1e0383b63cddb","token\_type":"Bearer","expires\_in":60,"scope":"AppB.Prm1"} |
| Artech.Security.API.repositorygetstsauthorizationaccesstoken | 2019-05-21 13:06:57,102 <35> INFO  Artech.Security.API.repositorygetstsauthorizationaccesstoken - GAMTrace-RepositoryGetClientAuthorizationAccessToken URL:http://localhost/ServerSTS.NetEnvironment/oauth/RequestTokenService |
| Artech.Security.API.repositorygetstsauthorizationaccesstoken | 2019-05-21 13:06:57,102 <35> INFO  Artech.Security.API.repositorygetstsauthorizationaccesstoken - GAMTrace-RepositoryGetClientAuthorizationAccessToken Response:{"access\_token":"2819262c-cdfd-4389-a1b3-b6548ec96add!2cb084f437f88ea7ec0d2c6b7c420fd2ff877447e7b7392f876cbaed9bdf54b6a1e0383b63cddb","token\_type":"Bearer","expires\_in":60,"scope":"AppB.Prm1"} |
| Artech.Security.API.repositorygetstsauthorizationaccesstoken | 2019-05-21 13:06:57,102 <35> INFO  Artech.Security.API.repositorygetstsauthorizationaccesstoken - &Errors....................:[] |

Any tool which allows you to analyze the network traffic should also be useful to see the HTTP requests and the HTTP responses.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [GetSTSAuthorizationAccessToken method of GAMRepository Object](https://wiki.genexus.com/commwiki/wiki?43218) | [Security Token Service Client Authorization using GAM](https://wiki.genexus.com/commwiki/wiki?43202) |

---
