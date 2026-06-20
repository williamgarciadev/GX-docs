---
title: "Managing Roles in applications using SSO"
source_id: 25538
source_url: https://wiki.genexus.com/commwiki/wiki?25538
genexus_version: "18"
---

# Managing Roles in applications using SSO

Applications using [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) can implement [Single Sign On (SSO)](http://en.wikipedia.org/wiki/Single_sign-on).

In the GeneXus SSO solution, all the web applications involved have to be connected to a GAM database. Only one of those applications is the Identity Provider (or the server application), and the rest are referenced as client applications. See [Single Sign On in applications using GAM](https://wiki.genexus.com/commwiki/wiki?25385) for details about this topic.

What SSO provides is a solution to the problem of providing centralized authentication for different distributed web applications. As for the authorization, it's always centralized in the client applications.

### [GAM Remote authentication and roles](#GAM+Remote+authentication+and+roles)

As mentioned before, the client applications are in charge of the authorization, which means that the [Roles](https://wiki.genexus.com/commwiki/wiki?17569) and [Permissions](https://wiki.genexus.com/commwiki/wiki?15912) have to be defined in the GAM of the client application.

However, when the user authenticates in the Identity Provider, the information on roles that resides in the GAM of the Identity Provider can be transferred to the GAM of the client application.

The mechanism is as follows:

* When the user authenticates, the list of roles can be transferred from the server to the client application. In order to be assigned to the user, those roles have to be mapped in the GAM of the client application.

The roles need to be mapped using their External ID property. That is, the External ID of the roles in the server have to be the same as the External ID of the role in the client in order to be considered the same role.

##### Picture#1. Roles in the server

##### Picture#2.Roles in the client

* The roles should have the same hierarchy in the server and in the client.

However, as explained before the authorization is centralized in the client application, so what really matters is the definition and the hierarchy of the roles in the client. In addition, the permissions are centralized in the client application.

### [How to transfer roles from the server to the client in the remote authentication](#How+to+transfer+roles+from+the+server+to+the+client+in+the+remote+authentication)

In the Identity Provider's GAM, all the client applications need to be registered with their corresponding Client ID and Client Secret, whereas in the client applications the [GAMRemote Authentication Type](https://wiki.genexus.com/commwiki/wiki?25355) needs to be defined.

1. When running the [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) in the server application, it is necessary to check the "Get User roles" option for the client application registered:

##### Picture#3.Server configuration for SSO : get user roles. Running GAMExampleEntryApplication webpanel.

Note that the ClientAllowGetUserRoles method of the GAMApplication object - which belongs to the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535) - is the method used in the code of this Web Panel (GAMExampleEntryApplication). The GAMExampleEntryApplication object is part of the [GAM - Examples](https://wiki.genexus.com/commwiki/wiki?21993).

```
&Application.ClientAllowGetUserRoles         = &ClientAllowGetUserRoles  //&Application is GAMApplication data type.
```

2. When running the GAM Web Backoffice in the client application, it is necessary to specify in the definition of the GAM Remote authentication type that it is going to manage "Authentication and Roles".

##### Picture#4.Client configuration for SSO : get user roles. Running GAMExampleEntryAuthenticationType webpanel.

When using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535), the code would be:

```
&AuthenticationTypeGAMRemote.FunctionId = &FunctionId.ToString() //&AuthenticationTypeGAMRemote is GAMAuthenticationTypeGAMRemote data type. &FunctionId is based on GAMAuthenticationFunctions domain.
```

After this configuration is made, when the user authenticates using the configured Remote Authentication, he is updated in the client application with the roles he has on the Identity Provider.

Remember that only the roles which are related by their External ID are going to be assigned to the user.


|  |
| --- |
| **Backlinks** |
| [Client side configuration for GAMRemoteREST Authentication type](https://wiki.genexus.com/commwiki/wiki?44841) | [Client side configuration for GAMRemoteREST Authentication type (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?57064) | [GAM - GAMRemote Authentication Type](https://wiki.genexus.com/commwiki/wiki?25355) |
| [Identity Provider Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?57020) | [Server side configuration for GAMRemoteREST Authentication type (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?57068) | [Single Sign On in applications using GAM](https://wiki.genexus.com/commwiki/wiki?25385) |

---
