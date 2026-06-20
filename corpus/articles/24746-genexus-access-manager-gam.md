---
title: "GeneXus Access Manager (GAM)"
source_id: 24746
source_url: https://wiki.genexus.com/commwiki/wiki?24746
genexus_version: "18"
---

# GeneXus Access Manager (GAM)

Most modern applications require some authentication/authorization scheme. To cover these aspects, GeneXus offers the GeneXus Access Manager (GAM), a centralized mechanism to manage application authentication and authorization.

The GeneXus Access Manager (GAM) provides a [GAM API](https://wiki.genexus.com/commwiki/wiki?16535) to manage all the security issues concerning an application. Therefore, the security module of any application (web applications and mobile applications) is provided by GAM. Also, security controls are automatically performed by GAM.

The [GAM API](https://wiki.genexus.com/commwiki/wiki?16535) implements all the functionalities related to security issues: user administration (registration, authentication, password administration, security policies), roles, etc.

To activate GAM in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836), set the [Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) to True.

GAM is based on the [Role Based Access Control (RBAC)](https://wiki.genexus.com/commwiki/wiki?17808) model.

It has its own database, logically independent from the database application, even though they can both be physically the same (with different table schemas).

You can manage users and security policies through the [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935).

### [Requirements](#Requirements)

1. GAM initializes the database using the same platform as the model. In a Java model, the GAM processes that run within the IDE to initialize the GAM database structure and the metadata (registration of applications, creation of permissions, etc.) are executed in Java.  
   For those DBMSs for which GeneXus doesn't distribute the JDBC drivers, you must copy them manually to <genexus>\gxjava\drivers (to the classpath configured in GeneXus).
2. If the GAM Data Store differs from MySQL or SQL Server, a setup is launched from the GeneXus IDE to install the GAM platform corresponding to the selected DBMS. See [GAM platforms](https://wiki.genexus.com/commwiki/wiki?22119) for more information. The setup is distributed to run it in standalone mode, under <GeneXus>\Library\GAM\Setup folder.
3. In web applications, GAM uses the web session to store user session data. As in any other web application, when load balancing environments are used, the servers need to persist the session (or use server affinity) so that the web session is available to the workers who respond to the request.

### [See Also](#See+Also)

[GAM - Getting Started](https://wiki.genexus.com/commwiki/wiki?19946)   
[GAM - Authentication](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18456,,)  
[GAM - Authorization](https://wiki.genexus.com/commwiki/wiki?17918)


* Built-in Security Module
  + [Getting Started](https://wiki.genexus.com/commwiki/wiki?19946)
    - [GAM repository creation](https://wiki.genexus.com/commwiki/wiki?29701)
    - [Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935)
      * [Main Menu](https://wiki.genexus.com/commwiki/wiki?61064)
        + [Dashboard section](https://wiki.genexus.com/commwiki/wiki?60978)
        + [Users section](https://wiki.genexus.com/commwiki/wiki?60983)
        + [Roles section](https://wiki.genexus.com/commwiki/wiki?61009)
        + [Sessions section](https://wiki.genexus.com/commwiki/wiki?61014)
        + [Applications section](https://wiki.genexus.com/commwiki/wiki?61016)
        + [Security Policies section](https://wiki.genexus.com/commwiki/wiki?61029)
        + [Repository section](https://wiki.genexus.com/commwiki/wiki?61036)
          - [Configuration](https://wiki.genexus.com/commwiki/wiki?61036)
          - [Connections](https://wiki.genexus.com/commwiki/wiki?61036)
        + [Settings section](https://wiki.genexus.com/commwiki/wiki?61051)
          - [Authentication Types](https://wiki.genexus.com/commwiki/wiki?61051)
          - [Event Subscriptions](https://wiki.genexus.com/commwiki/wiki?61051)
          - [GAM Configuration](https://wiki.genexus.com/commwiki/wiki?61051)
          - [General](https://wiki.genexus.com/commwiki/wiki?61051)
    - [GAM Examples](https://wiki.genexus.com/commwiki/wiki?21993)
      * [First login on a Web application](https://wiki.genexus.com/commwiki/wiki?45644)
    - [My first Native Mobile application with GAM](https://wiki.genexus.com/commwiki/wiki?15275)
  + [GAM architecture for Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?14978)
  + [Secure Native Mobile applications Architecture](https://wiki.genexus.com/commwiki/wiki?16052)
* [Authentication](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18456,,)
  + [Authentication Scenarios](https://wiki.genexus.com/commwiki/wiki?15937)
  + [Native Mobile Authentication](https://wiki.genexus.com/commwiki/wiki?15222)
  + [Authentication flow with an external OAuth2.0 provider](https://wiki.genexus.com/commwiki/wiki?52539)
  + [Authentication Types](https://wiki.genexus.com/commwiki/wiki?16508)
    - [Local](https://wiki.genexus.com/commwiki/wiki?20703)
    - Built-in
      * [APIKey](https://wiki.genexus.com/commwiki/wiki?56104)
      * [Apple](https://wiki.genexus.com/commwiki/wiki?44478)
      * [Facebook](https://wiki.genexus.com/commwiki/wiki?29007)
      * [GAMRemote](https://wiki.genexus.com/commwiki/wiki?25355)
        + [GAMRemote Authentication type for Native mobile applications](https://wiki.genexus.com/commwiki/wiki?29672)
        + [Server side configuration](https://wiki.genexus.com/commwiki/wiki?37038)
        + [Client side configuration](https://wiki.genexus.com/commwiki/wiki?37039)
      * [GAMRemoteREST](https://wiki.genexus.com/commwiki/wiki?44833)
        + [Server side configuration](https://wiki.genexus.com/commwiki/wiki?44840)
        + [Client side configuration](https://wiki.genexus.com/commwiki/wiki?44841)
      * [Google](https://wiki.genexus.com/commwiki/wiki?29013)
      * [Twitter](https://wiki.genexus.com/commwiki/wiki?17208)
      * [WeChat](https://wiki.genexus.com/commwiki/wiki?45037)
    - OAuth 2.0
      * [How to configure](https://wiki.genexus.com/commwiki/wiki?39484)
      * Samples
        + [HowTo: Authenticate to Microsoft Entra ID using GAM](https://wiki.genexus.com/commwiki/wiki?48906)
        + [HowTo: Configure OAuth 2.0 authentication with Microsoft Entra ID](https://wiki.genexus.com/commwiki/wiki?54371)
        + [HowTo: Authenticate to Facebook using GAM](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?54310,,)
        + [HowTo: Authenticate to Google using GAM](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?54309,,)
        + [HowTo: Authenticate to Instagram using GAM](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?54307,,)
        + [HowTo: Authenticate to LinkedIn using GAM](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?54308,,)
        + [HowTo: Authenticate to Mercado Libre using GAM](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?54306,,)
        + [HowTo: Authenticate to Office 365 using GAM](https://wiki.genexus.com/commwiki/wiki?39166)
        + [HowTo: Authenticate to WeChat using GAM](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?54311,,)
    - OpenID Connect
      * [How to configure](https://wiki.genexus.com/commwiki/wiki?49183)
      * Samples
        + [HowTo: Authenticate to Azure AD using OpenID Connect with GAM](https://wiki.genexus.com/commwiki/wiki?55121)
        + [HowTo: Authenticate to Google using OpenID Connect with GAM](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?55185,,)
    - SAML 2.0
      * [How to configure](https://wiki.genexus.com/commwiki/wiki?41212)
      * [Generating certificates](https://wiki.genexus.com/commwiki/wiki?41243)
      * Samples
        + [SAP](https://wiki.genexus.com/commwiki/wiki?41235)
        + [Agesic](https://wiki.genexus.com/commwiki/wiki?41266)
        + [Okta](https://wiki.genexus.com/commwiki/wiki?49660)
        + [Azure](https://wiki.genexus.com/commwiki/wiki?54751)
    - OTP - One Time Password
      * How to configure
        + [One Time Password](https://wiki.genexus.com/commwiki/wiki?48197)
        + [One Time Password for mobile](https://wiki.genexus.com/commwiki/wiki?50664)
        + [Time Based One Time Password](https://wiki.genexus.com/commwiki/wiki?49974)
        + [Time Based One Time Password for mobile](https://wiki.genexus.com/commwiki/wiki?50708)
      * [How to translate OTP notifications](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?58017,,)
    - 2FA - Two Factor Authentication
      * How to configure
        + [Two Factor Authentication](https://wiki.genexus.com/commwiki/wiki?48254)
        + [Two factor Authentication for mobile](https://wiki.genexus.com/commwiki/wiki?50726)
    - [External](https://wiki.genexus.com/commwiki/wiki?21755)
      * [Interface version 1.0](https://wiki.genexus.com/commwiki/wiki?21548)
      * [Interface version 2.0](https://wiki.genexus.com/commwiki/wiki?21555)
      * [Web Service](https://wiki.genexus.com/commwiki/wiki?16512)
    - [Custom](https://wiki.genexus.com/commwiki/wiki?21751)
      * Samples
        + [LDAP](https://wiki.genexus.com/commwiki/wiki?29474)
        + [Windows](https://wiki.genexus.com/commwiki/wiki?24034)
  + [Impersonation](https://wiki.genexus.com/commwiki/wiki?24241)
  + SSO
    - [Single Sign On (SSO)](https://wiki.genexus.com/commwiki/wiki?25385)
    - [Logout options for Single Sign On](https://wiki.genexus.com/commwiki/wiki?32336)
    - [HowTo: Single Logout from a SSO applications not using GAM (SLO)](https://wiki.genexus.com/commwiki/wiki?36239)
* [Authorization](https://wiki.genexus.com/commwiki/wiki?17918)
  + [Authorization Scenarios](https://wiki.genexus.com/commwiki/wiki?17583)
    - [Roles](https://wiki.genexus.com/commwiki/wiki?17569)
      * [Main Role of a user](https://wiki.genexus.com/commwiki/wiki?21643)
      * [HowTo: Manage Roles through external authentication programs](https://wiki.genexus.com/commwiki/wiki?16929)
    - [Permissions](https://wiki.genexus.com/commwiki/wiki?15912)
      * [Automatic Permissions by GeneXus](https://wiki.genexus.com/commwiki/wiki?17916)
      * [Permissions in Mobile Applications](https://wiki.genexus.com/commwiki/wiki?17925)
      * [Permissions Created by the User](https://wiki.genexus.com/commwiki/wiki?29723)
      * [Full Control](https://wiki.genexus.com/commwiki/wiki?17664)
      * [Grouping of permissions](https://wiki.genexus.com/commwiki/wiki?18536)
      * [Define a Menu](https://wiki.genexus.com/commwiki/wiki?29681)
      * [Adding a Permission to a Role](https://wiki.genexus.com/commwiki/wiki?17963)
      * [Permission Access Type](https://wiki.genexus.com/commwiki/wiki?20603)
* [Users](https://wiki.genexus.com/commwiki/wiki?22082)
  + [Dynamic attributes](https://wiki.genexus.com/commwiki/wiki?21315)
  + [HowTo: reference GAM users](https://wiki.genexus.com/commwiki/wiki?16534)
  + [How to Solve Forgot Password](https://wiki.genexus.com/commwiki/wiki?16923)
* [Repository](https://wiki.genexus.com/commwiki/wiki?17568)
  + [Applications](https://wiki.genexus.com/commwiki/wiki?15910)
    - [Menus](https://wiki.genexus.com/commwiki/wiki?29681)
      * [API for Menus](https://wiki.genexus.com/commwiki/wiki?29742)
    - Samples
      * [Display a Menu using Jscookmenu UC](https://wiki.genexus.com/commwiki/wiki?29743)
  + [GAM configuration to send emails](https://wiki.genexus.com/commwiki/wiki?48421)
  + [Creating New Repositories](https://wiki.genexus.com/commwiki/wiki?18642)
  + [Repository connections](https://wiki.genexus.com/commwiki/wiki?16150)
    - [HowTo: Use an environment variable for repository connections](https://wiki.genexus.com/commwiki/wiki?59028)
  + [Multiple Repositories Scenarios](https://wiki.genexus.com/commwiki/wiki?18682)
* Sessions
  + [Methods for handling sessions in GAM](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?24367,,)
    - [GetSessionLog method](https://wiki.genexus.com/commwiki/wiki?34395)
    - [GetSessionLogsOrderBy method](https://wiki.genexus.com/commwiki/wiki?34396)
    - [GetSessionLogsCount method](https://wiki.genexus.com/commwiki/wiki?45864)
    - [GetAliveSessionCount method](https://wiki.genexus.com/commwiki/wiki?34397)
    - [KillSession method](https://wiki.genexus.com/commwiki/wiki?34398)
    - [LoginRetries and LoginRetryCount properties](https://wiki.genexus.com/commwiki/wiki?34399)
    - [FullLog property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?34402,,)
    - [UpdateExpiredSessionLog method](https://wiki.genexus.com/commwiki/wiki?44915)
  + [Anonymous Sessions in Web Applications](https://wiki.genexus.com/commwiki/wiki?16414)
  + [Security Session Management](https://wiki.genexus.com/commwiki/wiki?16338)
* [Security Policies](https://wiki.genexus.com/commwiki/wiki?18521)
* [Events subscription](https://wiki.genexus.com/commwiki/wiki?32698)
* Deployment
  + [Applications deployment](https://wiki.genexus.com/commwiki/wiki?21219)
  + [Cache Managment](https://wiki.genexus.com/commwiki/wiki?58220)
  + [GAM - Deploy Tool](https://wiki.genexus.com/commwiki/wiki?37764)
  + [Checklist for Applications](https://wiki.genexus.com/commwiki/wiki?18574)
* Services
  + [GAM Scopes](https://wiki.genexus.com/commwiki/wiki?55603)
  + [OAuth mobile service](https://wiki.genexus.com/commwiki/wiki?45320)
  + [Signout mobile service](https://wiki.genexus.com/commwiki/wiki?60753)
  + [Userinfo Service](https://wiki.genexus.com/commwiki/wiki?45316)
  + [HowTo: Use GAM as an OAuth 2.0 provider](https://wiki.genexus.com/commwiki/wiki?45493)
  + [OAuth 2.0 Endpoints to use GAM as Web IDP Server](https://wiki.genexus.com/commwiki/wiki?49817)
  + [OAuth 2.0 Endpoints to authenticate with GAM as REST IDP Server](https://wiki.genexus.com/commwiki/wiki?55623)
  + [SSORest of IDPs external to GAM](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?56057,,)
  + [Use OAuth 2.0 endpoints to authenticate a Mini App from a Super App](https://wiki.genexus.com/commwiki/wiki?56035)
  + [Use APIKey to request services from a Application](https://wiki.genexus.com/commwiki/wiki?56104)
  + [Single Sign on for Rest Services](https://wiki.genexus.com/commwiki/wiki?46492)
    - [Client-side configuration for SSO](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46499,,)
    - [Server-side configuration for SSO](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46496,,)
* Advanced
  + [Security Token Service Client Authorization](https://wiki.genexus.com/commwiki/wiki?43202)
  + [HowTo: Configure GAM to use Security Token Service](https://wiki.genexus.com/commwiki/wiki?43206)
  + [Change the objects targeted by the GAM Backend menu](https://wiki.genexus.com/commwiki/wiki?52816)
  + [HowTo: Invoke a Procedure with GAM API in Java](https://wiki.genexus.com/commwiki/wiki?54205)
* [Compatibility](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46282,,)
  + [Database version 4.0.2](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?29639,,)
  + [Database version 4.0.3](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?34457,,)
  + [Database version 4.0.4](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?39616,,)
  + [Database version 4.0.5](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?48526,,)
  + [Database version 4.0.6](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50063,,)
  + [Database version 4.0.7](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?53650,,)
  + [Database version 4.0.8](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?55665,,)
  + [Database version 4.0.9](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?55971,,)
  + [Database version 4.1.x](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?56263,,)
* Troubleshooting
  + [HowTo: Generate GAM trace](https://wiki.genexus.com/commwiki/wiki?50469)
  + [HowTo: Generate trace of GAM Deploy Tool](https://wiki.genexus.com/commwiki/wiki?26297)
  + [HowTo: Get the email address of a Facebook user](https://wiki.genexus.com/commwiki/wiki?25087)
  + [GAM Troubleshooting](https://wiki.genexus.com/commwiki/wiki?22815)
* Media
  + [GeneXus Access Manager in the media](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?44330,,)
* [Hardening of GeneXus Systems and Deployments](https://wiki.genexus.com/commwiki/wiki?47237)
  + [Good practices for secure development](https://wiki.genexus.com/commwiki/wiki?47241)
  + [Configuration for secure deployment](https://wiki.genexus.com/commwiki/wiki?47243)

---
