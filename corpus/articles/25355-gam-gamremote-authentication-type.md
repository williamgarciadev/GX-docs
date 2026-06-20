---
title: "GAM - GAMRemote Authentication Type"
source_id: 25355
source_url: https://wiki.genexus.com/commwiki/wiki?25355
genexus_version: "18"
---

# GAM - GAMRemote Authentication Type

Applications that use [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) can be [Identity Provider](http://en.wikipedia.org/wiki/Identity_provider)s. In a scenario with an Identity Provider and one or more client applications, the applications will use GAMRemote Authentication Type to authenticate using the Identity Provider (from now on, the server).  
  
Each client application may be connected to a different GAM database and have [Integrated Security](https://wiki.genexus.com/commwiki/wiki?15214) enabled. Otherwise, depending on your solution, you can use the same GAM database for all. See [SAC 43517](https://www.genexus.com/en/developers/websac?data=43517;;) for more details on this topic.

When the client authenticates, its behavior is the same as when an application authenticates to Facebook or Twitter, because a session is generated in the Identity Provider and used by the application while it continues to be valid.

That's why this functionality is very useful for implementing [Single Sign On in applications](https://wiki.genexus.com/commwiki/wiki?25385).

### [Configuration](#Configuration+)

The necessary configuration for this authentication type includes the following steps:

        1. Identity Provider (Server) Configuration

            The Identity Provider must be configured using the Client Application URL. This information must be provided to the server administrator.

       2. Defining a New GAM Application

           Given the Client Application URL information of the first step, a new GAM Application has to be defined in the Identity Provider. The administrator will configure the Application using some **Client Id** and **Client Secret** values. Afterward, these values have to be given to the Client's administrator to configure his GAM.

      3. Client Configuration

            In the GAM client, the **GAMRemote Authentication Type** is going to be configured, using the Application credentials (Client Id and Client Secret) given by the Identity Provider's administrator (obtained in the previous step). The Remote server URL will also be needed.

### [Troubleshooting](#Troubleshooting)

**HTTP Error 403 - Forbidden:**could appear if a default document is not configured for the requested URL, and **D****irectory Browsing** is not enabled on the server.

#### [**Solution:**](#Solution%3A)

* Open **IIS Manager**
* In the Features view, double-click **Directory Browsing**
* On the Directory Browsing page, in the Actions pane, click **Enable**.

For more information, see [Identity Provider Configuration](https://wiki.genexus.com/commwiki/wiki?37038) and [Client Configuration](https://wiki.genexus.com/commwiki/wiki?37039).

### [GAM Remote Authentication Type for Native mobile applications](#GAM+Remote+Authentication+Type+for+Native+mobile+applications)

See [GAMRemote Authentication type for Native mobile applications](https://wiki.genexus.com/commwiki/wiki?29672).

### [Implementation Details](#Implementation+Details)

#### [GAM User](#GAM+User)

* When authenticating through the Identity Provider, the user is created or updated in the client GAM database using the same GAM User GUID from the GAM of the Identity Provider. The password is stored only in the GAM of the Identity Provider.
* The default data transferred from the Identity Provider database to the client is: Guid, Username, EMail, First\_Name, Last\_name, External\_id, Birthday, Gender, Url\_image, Url\_profile, Phone, Address, City, State, Post\_code, Language, Timezone.
* When additional data must be passed (such as dynamic attributes of GAM User), you must, then, add "gam\_user\_additional\_data" additional scope at the GAM remote Authentication Type configuration, and check the "**Can get user additional data**" at the Indentity Provider's configuration. As since [GeneXus 16 upgrade 7](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?44454,,) you have the &AuthenticationTypeGAMRemote.GAMRemote.AddUserAdditionalDataScope property, which sets the "gam\_user\_additional\_data" automatically at the client.

### [Security Policies](#Security+Policies)

* The password [Security Policies](https://wiki.genexus.com/commwiki/wiki?18521) applicable are those of the Identity Provider GAM.
* The applicable security policies not related to the password are those of the client GAM database.

### [Data required for user registration](#Data+required+for+user+registration)

* The information required must be completed on the server and also on the client. So, if the server security policies require the email address, its entry will be requested. Likewise, when any other data is required in the client GAM, it will be asked to complete it as well.

### [Session logout](#Session+logout)

See [Logout options for Single Sign On using GAM](https://wiki.genexus.com/commwiki/wiki?32336).

### [**Notes:**](#Notes%3A)

* The Identity provider may use all authentication types (Local, Custom, OAuth 2.0, Google, etc.).
* The solution of GAMRemote Authentication is based on [OAuth 2.0](http://es.wikipedia.org/wiki/OAuth).

### [See Also](#See+Also)

[Single Sign On in applications using GAM](https://wiki.genexus.com/commwiki/wiki?25385)  
[Managing Roles in applications using SSO](https://wiki.genexus.com/commwiki/wiki?25538)


|  |
| --- |
| **Backlinks** |
| [Client Configuration for GAM Remote Authentication](https://wiki.genexus.com/commwiki/wiki?37039) | [Client Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?57067) |
| [GAM - Authentication Scenarios](https://wiki.genexus.com/commwiki/wiki?15937) | [GAM - Authentication Types](https://wiki.genexus.com/commwiki/wiki?16508) | [GAM - Events subscription](https://wiki.genexus.com/commwiki/wiki?32698) |
| [GAM - Events subscription (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57625) | [GAM - GAMRemoteREST Authentication type (OAuth 2.0)](https://wiki.genexus.com/commwiki/wiki?44833) | [GAM - Impersonation](https://wiki.genexus.com/commwiki/wiki?24241) | [GAM - OAuth User Scopes](https://wiki.genexus.com/commwiki/wiki?55603) |
| [GAM Login Method](https://wiki.genexus.com/commwiki/wiki?19269) |
| [GAMRemote Authentication type for Native mobile applications](https://wiki.genexus.com/commwiki/wiki?29672) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Emulate SSO without using GAM remote authentication](https://wiki.genexus.com/commwiki/wiki?38116) | [HowTo: Get user's additional information from the GAM Identity Provider](https://wiki.genexus.com/commwiki/wiki?37703) |
| [HowTo: Send and receive properties set at the login](https://wiki.genexus.com/commwiki/wiki?44824) |
| [HowTo: Signout from a SSO applications not using GAM](https://wiki.genexus.com/commwiki/wiki?36239) | [HowTo: Use GAM as an OAuth 2.0 provider](https://wiki.genexus.com/commwiki/wiki?45493) | [Identity Provider Configuration for GAM Remote Authentication](https://wiki.genexus.com/commwiki/wiki?37038) |
| [Identity Provider Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?57020) | [Identity Provider Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57694) | [Managing Roles in applications using SSO](https://wiki.genexus.com/commwiki/wiki?25538) | [Multi-tenant GAM applications using Single Sign On](https://wiki.genexus.com/commwiki/wiki?30495) |
| [Repository GUID property](https://wiki.genexus.com/commwiki/wiki?34090) | [Single Sign On for Rest Services using GAM](https://wiki.genexus.com/commwiki/wiki?46492) | [Single Sign On in applications using GAM](https://wiki.genexus.com/commwiki/wiki?25385) | [TimeoutToFinishOAuthAuthenticationUsingIDP property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?58086) |

---
