---
title: "GAM API"
source_id: 16535
source_url: https://wiki.genexus.com/commwiki/wiki?16535
genexus_version: "18"
---

# GAM API

[GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) provides an API that allows you to handle data types and methods to add security (Authentication and Authorization) to GeneXus applications (both Web applications and Native Mobile applications).

So, when you enable GAM in a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) (by setting the [Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) to True), certain [external objects](https://wiki.genexus.com/commwiki/wiki?5669) are imported to allow interaction with the GAM API. External objects are the way to access the GAM API and are distributed in a module called GeneXusSecurity.  
  
The domains are distributed in the GeneXusSecurityCommon module.

GAMUser, GAMRepository, GAMPermission, GAMApplication, and GAMError are the names of some of the external objects.

External objects have properties and methods; in particular, they implement the same methods as a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846), as follows:

* Load()
* Save()
* Delete()
* Fail()
* Success()

If you change any properties in the GAM objects, you need to call the save() method and run the Commit command. 

GAM objects also have other methods implemented to create, update, or delete objects (see the AddPermission method in the example below). With these methods, the Commit command has to be used after the method is successfully executed. The only GAM methods that execute an implicit Commit are those related to the login, and they run on a new logical work unit (LWU). See [SAC 31253](https://www.genexus.com/en/developers/websac?data=31253;;).

If you are going to make changes in both ways (from a property and using a method) and need to cancel both changes—when an error occurs—you need to control it programmatically.

```
&PermissionAdd.ApplicationId= &AppId
&PermissionAdd.GUID = &Id
&PermissionAdd.Type = &Access
&isOK = &GAMRole.AddPermission(&PermissionAdd, &Errors)
If not &isOK
    For &Error in &Errors
       Msg(Format(!"%1 (GAM%2)", &Error.Message, &Error.Code))
    EndFor    
else
    commit 
Endif
```

### [How to use the GAM API](#How+to+use+the+GAM+API)

As explained before, the GAM API provides methods to extend the functionality of security mechanisms. You can read the [GAM - Examples](https://wiki.genexus.com/commwiki/wiki?21993) that offer a wide range of use cases solved. After enabling GAM in your KB, you can import these examples manually (they are present in GAM\_Web-Administration.xpz, found in <GeneXus Installation>\Library\GAM).

### [See Also](#See+Also)

[GAM - Activation Process](https://wiki.genexus.com/commwiki/wiki?21973)


|  |
| --- |
| **Sub Categories** |
| [Category:GAM - Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) |

---

|  |
| --- |
| **Pages** |
| [AllowMultipleConcurrentWebSessions property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?18939) | [Anonymous Sessions in GAM - Web Applications](https://wiki.genexus.com/commwiki/wiki?16414) | [ApplicationGoHome method of GAMRepository Object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46011,ApplicationGoHome+method+of+GAMRepository+Object,) |
| [Connection Challenge Expire (minutes)](https://wiki.genexus.com/commwiki/wiki?22023) | [Enable Biometrics property](https://wiki.genexus.com/commwiki/wiki?43466) | [Extensibility of GAM entity properties](https://wiki.genexus.com/commwiki/wiki?19634) |
| [FullLog property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?34402,FullLog+property,) | [GAM - API for Menus](https://wiki.genexus.com/commwiki/wiki?29742) | [GAM - Facebook Interaction Sample](https://wiki.genexus.com/commwiki/wiki?16569) |
| [GAM - Main Role of a user](https://wiki.genexus.com/commwiki/wiki?21643) | [GAM - Users](https://wiki.genexus.com/commwiki/wiki?22082) | [GAM Login Method](https://wiki.genexus.com/commwiki/wiki?19269) |
| [GAM: "User Missing Required Data" Form](https://wiki.genexus.com/commwiki/wiki?18920) | [GAM: A way to solve Forgot Password](https://wiki.genexus.com/commwiki/wiki?16923) | [GAMUnblockUserTimeout property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18926) |
| [Get GAM User Permissions](https://wiki.genexus.com/commwiki/wiki?20585) | [Get GAM User Roles](https://wiki.genexus.com/commwiki/wiki?20595) | [GetAgentServiceHeader method of GAM object](https://wiki.genexus.com/commwiki/wiki?43221) |
| [GetAliveSessionCount method](https://wiki.genexus.com/commwiki/wiki?34397) | [GetApplicationData and SetApplicationData method of GAMSession object](https://wiki.genexus.com/commwiki/wiki?21575) | [GetSessionLog method](https://wiki.genexus.com/commwiki/wiki?34395) |
| [GetSessionLogsCount method](https://wiki.genexus.com/commwiki/wiki?45864) | [GetSessionLogsOrderBy method](https://wiki.genexus.com/commwiki/wiki?34396) | [GetSTSAuthorizationAccessToken method of GAMRepository Object](https://wiki.genexus.com/commwiki/wiki?43218) |
| [GoHome method of GAMApplication Object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46012,GoHome+method+of+GAMApplication+Object,) | [HomeObject property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?34429,HomeObject+property,) | [How to: Customize a GAM Application when you have more than one](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?44929,How+to%3A+Customize+a+GAM+Application+when+you+have+more+than+one,) |
| [HowTo: Connect to GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18625) | [HowTo: Create New Repositories from a GAM deploy tool package](https://wiki.genexus.com/commwiki/wiki?20328) | [HowTo: Get all users which have a given set of Roles](https://wiki.genexus.com/commwiki/wiki?21268) |
| [HowTo: Get and Set GAM Repository Connections](https://wiki.genexus.com/commwiki/wiki?19245) | [HowTo: Get GAM Repository connection information and create a connection file](https://wiki.genexus.com/commwiki/wiki?19231) | [HowTo: Manage repositories using an admin user](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?44937,HowTo%3A+Manage+repositories+using+an+admin+user,) |
| [HowTo: Manage Roles through external authentication programs](https://wiki.genexus.com/commwiki/wiki?16929) | [HowTo: Map Application Users to GAM Users](https://wiki.genexus.com/commwiki/wiki?16552) | [HowTo: Map Application Users to GAM Users - Using ExternalID GAMUser property](https://wiki.genexus.com/commwiki/wiki?16565) |
| [HowTo: Pass additional parameters to external authentication programs using GAM](https://wiki.genexus.com/commwiki/wiki?21752) | [HowTo: Pass additional parameters to external authentication programs using GAM (GeneXus 18 Upgrade)](https://wiki.genexus.com/commwiki/wiki?55358) | [HowTo: Reference GAM users using the GAM API](https://wiki.genexus.com/commwiki/wiki?16534) |
| [HowTo: Send and receive properties set at the login](https://wiki.genexus.com/commwiki/wiki?44824) | [HowTo: Update a repository from a GAM deploy tool package](https://wiki.genexus.com/commwiki/wiki?20929) | [Implementing Authentication and Logout Using the GAM API](https://wiki.genexus.com/commwiki/wiki?15938) |
| [KillSession method](https://wiki.genexus.com/commwiki/wiki?34398) | [Login retries to lock user property (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58371) | [LoginAttemptsToLockSession property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18593) |
| [LoginAttemptsToLockUser property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18592) | [LoginRetries and LoginRetryCount properties](https://wiki.genexus.com/commwiki/wiki?34399) | [MaximumPasswordHistoryEntries property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?18579) |
| [Methods for handling sessions in GAM](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?24367,Methods+for+handling+sessions+in+GAM,) | [MinimumTimeToChangePasswords property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?18942) | [OAuth mobile service](https://wiki.genexus.com/commwiki/wiki?45320) |
| [OAuth Token expire (minutes) GAM Security Policy property (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58155) | [OauthTokenExpire property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?18577) | [OauthTokenMaximumRenovations property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?19324) |
| [Security Session Management in Applications using GAM](https://wiki.genexus.com/commwiki/wiki?16338) | [Session Expires On IP Change property](https://wiki.genexus.com/commwiki/wiki?18925) | [Single User Access property (for mobile apps with GAM)](https://wiki.genexus.com/commwiki/wiki?17242) |
| [Update GAM Application Permissions](https://wiki.genexus.com/commwiki/wiki?20590) | [Update GAM Role Permissions](https://wiki.genexus.com/commwiki/wiki?20593) | [Update GAM User Permissions](https://wiki.genexus.com/commwiki/wiki?20583) |
| [UpdateExpiredSessionLog method](https://wiki.genexus.com/commwiki/wiki?44915) | [User Activation Method Repository property](https://wiki.genexus.com/commwiki/wiki?18932) | [User Automatic Activate TimeOut property](https://wiki.genexus.com/commwiki/wiki?18934) |
| [User Identification](https://wiki.genexus.com/commwiki/wiki?21030) | [User Recovery Password Key Timeout property in GAMRepository](https://wiki.genexus.com/commwiki/wiki?18590) | [User Remember Me Timeout](https://wiki.genexus.com/commwiki/wiki?18586) |
| [Userinfo GAM Service](https://wiki.genexus.com/commwiki/wiki?45316) | [UserRememberMeType property](https://wiki.genexus.com/commwiki/wiki?18584) | [Users enabled or disabled in the GAM Repository](https://wiki.genexus.com/commwiki/wiki?21042) |
| [UserSessionCacheTimeout property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18582) | [WebSessionTimeOut property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?58396) |

---
