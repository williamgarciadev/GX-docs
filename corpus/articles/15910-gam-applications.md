---
title: "GAM - Applications"
source_id: 15910
source_url: https://wiki.genexus.com/commwiki/wiki?15910
genexus_version: "18"
---

# GAM - Applications

As a security component, [GeneXus Access Manager](https://wiki.genexus.com/commwiki/wiki?24746) can be used by different applications (which can be Native Mobile applications, Web applications, or even Web Services).

Conceptually, GAM applications group [Permissions](https://wiki.genexus.com/commwiki/wiki?15912) which are related to GeneXus objects.

### GAM Applications that are automatically generated

* **WEB GAM application**  
    
  If the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) has at least one web [environment](https://wiki.genexus.com/commwiki/wiki?7115), a WEB GAM application is automatically generated including the permissions of all the web objects of the KB. This WEB GAM application is identified with a GUID assigned in the [Application ID property](https://wiki.genexus.com/commwiki/wiki?18667). The name of the WEB GAM application is the name of the KB.    
    
  The information of the WEB GAM application GUID is stored in the application.gam file, which is saved in the model directory and must be included in the deployment.  
    
  Note that only one WEB GAM application is automatically generated for the KB even if it has N environments.
* **GAM applications associated with each Native Mobile / Angular [Main Object](https://wiki.genexus.com/commwiki/wiki?5770)**  
     
  For each main object (like [Menus](https://wiki.genexus.com/commwiki/wiki?16321) or [Panels](https://wiki.genexus.com/commwiki/wiki?24829)) a GAM application is automatically generated.

GAM applications are defined within a [repository](https://wiki.genexus.com/commwiki/wiki?17568). Each repository can contain more than one GAM application.

Additionally, one Repository can store more than one GAM WEB application because from different KBs you can use a different [Application Id](https://wiki.genexus.com/commwiki/wiki?18667) to create a different GAM WEB application in the same repository.

### [What is the purpose of GAM applications?](#What+is+the+purpose+of+GAM+applications%3F)

First, the GAM application is checked at runtime at the moment of user authentication.

Another purpose of defining GAM applications within the GAM repository is to associate Permissions to these applications and to form groups of permissions.

At runtime, permissions are checked considering the application which is being executed. So, when the user logs in to a repository, and a permission is needed to execute an action, the permission must be defined in the GAM application he is executing (and he needs to have a [role](https://wiki.genexus.com/commwiki/wiki?17569) where this permission is allowed).

So the permissions which can be associated to a GAM application are all related in some sense.

By default, when F5 processes permissions, the following GAM applications are created in the repository:

* A GAM application for the WEB application of the KB. The WEB GAM application groups the permissions of all the web objects of the KB and its descendants.
* A GAM application for each main object for Native Mobile applications. The application groups the permissions of this main object and its descendants. So if you have Dashboard1, and Dashboard2 which are main, there will be a GAM application for each of them.

### [How can I work with GAM applications?](#How+can+I+work+with+GAM+applications%3F)

Each GAM application is identified by a GAM application GUID, and has *"*Client Application data*"*: [Client Id and Client Secret information](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?21454,,).

You can see the running [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) as an administrator, all the available GAM applications for the repository you've connected to, and you can also define new applications. See figure 1.

`[imagen omitida: wiki id 57691]`

###### [Figure 1.](#Figure+1.)

**Note:** To add a new application, you have to click on the [Applications section](https://wiki.genexus.com/commwiki/wiki?61016) and then click on the **ADD** button.

### [What happens at runtime?](#What+happens+at+runtime%3F)

When the user executes a web object, the GAM application Identifier is taken from application.gam file located in the virtual directory. See [Application ID property](https://wiki.genexus.com/commwiki/wiki?18667) in order to understand how this ID is automatically generated.

If the user executes a GeneXus object for Native Mobile and Angular application, the GAM application is identified by its *"*Client Application data" ([Client Id and Client Secret information](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?21454,,)). See [Secure Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?16052) to understand how this information is used at a low level, using OAuth protocol.

#### [**Notes:**](#Notes%3A)

* The *"*Client Application data*"* of GAM applications which have web object permissions is not used in GeneXus Evolution 3.
* At present only one [Application ID property](https://wiki.genexus.com/commwiki/wiki?18667) is referenced in application.gam file so all the permissions related to web objects have to be grouped in the same WEB GAM application in the web application deployment. Although you can have more than one WEB GAM application in a repository, you need to deploy a different web application for each of them.

### [See Also](#See+Also)

[GAM - Permissions](https://wiki.genexus.com/commwiki/wiki?15912)  
[GAM - Repository Connections](https://wiki.genexus.com/commwiki/wiki?16150)  
[GAM - Repository](https://wiki.genexus.com/commwiki/wiki?17568)  
[Require Access Permissions Application Property](https://wiki.genexus.com/commwiki/wiki?18512)  
[GAM Web Backoffice - Applications section](https://wiki.genexus.com/commwiki/wiki?61016)


|  |
| --- |
| **Backlinks** |
| [Administrator User Name property](https://wiki.genexus.com/commwiki/wiki?15215) | [API object security scheme](https://wiki.genexus.com/commwiki/wiki?52550) | [Application ID property](https://wiki.genexus.com/commwiki/wiki?18667) |
| [Auto-Registration in SD: What to do when a certain action requires the user to log in](https://wiki.genexus.com/commwiki/wiki?19835) | [CacheTimeout property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?21863) |
| [Extensibility of GAM entity properties](https://wiki.genexus.com/commwiki/wiki?19634) | [GAM - Applications (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?57690) | [GAM - Applications deployment](https://wiki.genexus.com/commwiki/wiki?21219) | [GAM - Applications Registration option](https://wiki.genexus.com/commwiki/wiki?16288) |
| [GAM - Authorization Scenarios](https://wiki.genexus.com/commwiki/wiki?17583) | [GAM - Automatic Permissions generated by GeneXus (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?53950) | [GAM - External Authorization](https://wiki.genexus.com/commwiki/wiki?22898) | [GAM - Grouping of permissions](https://wiki.genexus.com/commwiki/wiki?18536) |
| [GAM - Permissions](https://wiki.genexus.com/commwiki/wiki?15912) | [GAM - Repository](https://wiki.genexus.com/commwiki/wiki?17568) | [GAM - Roles](https://wiki.genexus.com/commwiki/wiki?17569) | [GAM Backend Application](https://wiki.genexus.com/commwiki/wiki?29699) |
| [GAM repository creation for the first time from GeneXus](https://wiki.genexus.com/commwiki/wiki?29701) | [GAM Web Backoffice - Applications section](https://wiki.genexus.com/commwiki/wiki?61016) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [GetSTSAuthorizationAccessToken method of GAMRepository Object](https://wiki.genexus.com/commwiki/wiki?43218) |
| [HowTo: Add a Permission to a Role using GAM](https://wiki.genexus.com/commwiki/wiki?17963) |
| [HowTo: Configure GAM to use Security Token Service](https://wiki.genexus.com/commwiki/wiki?43206) | [HowTo: Configure Single Sign-On (SSO) between a Super App and Mini App using GAM](https://wiki.genexus.com/commwiki/wiki?58884) | [HowTo: Create New Repositories from a GAM deploy tool package](https://wiki.genexus.com/commwiki/wiki?20328) | [HowTo: Define a Menu using GAM](https://wiki.genexus.com/commwiki/wiki?29681) |
| [HowTo: Develop Secure REST Web Services in GeneXus](https://wiki.genexus.com/commwiki/wiki?15918) | [HowTo: Emulate SSO without using GAM remote authentication](https://wiki.genexus.com/commwiki/wiki?38116) | [HowTo: GAM Automatic Check of Access Permissions for Web Objects](https://wiki.genexus.com/commwiki/wiki?17585) |
| [HowTo: Generate GAM trace](https://wiki.genexus.com/commwiki/wiki?50469) | [HowTo: Generate GAM trace (GeneXus 18 Upgrade 10 or prior)](https://wiki.genexus.com/commwiki/wiki?58291) | [HowTo: Give Restricted Access to a Group of Web Objects](https://wiki.genexus.com/commwiki/wiki?18510) |
| [HowTo: Manage a multi-language application using GAM.](https://wiki.genexus.com/commwiki/wiki?55986) | [HowTo: Update a repository from a GAM deploy tool package](https://wiki.genexus.com/commwiki/wiki?20929) |
| [HowTo: Use GAM as an OAuth 2.0 provider](https://wiki.genexus.com/commwiki/wiki?45493) | [Identity Provider Configuration for GAM Remote Authentication](https://wiki.genexus.com/commwiki/wiki?37038) | [Identity Provider Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60954) |
| [Identity Provider Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?57020) | [Identity Provider Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57694) | [Launchpad Tool Window (GeneXus 18 latest upgrade or prior)](https://wiki.genexus.com/commwiki/wiki?60884) |
| [Permissions Over a User Action in SD Objects](https://wiki.genexus.com/commwiki/wiki?18173) |
| [Require Access Permissions Application Property](https://wiki.genexus.com/commwiki/wiki?18512) | [Security Client ID property](https://wiki.genexus.com/commwiki/wiki?21484) | [Server side configuration for GAMRemoteREST Authentication type](https://wiki.genexus.com/commwiki/wiki?44840) |
| [Server side configuration for GAMRemoteREST Authentication type (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?57068) | [Single Sign On in applications using GAM](https://wiki.genexus.com/commwiki/wiki?25385) |
| [Single User Access property (for mobile apps with GAM)](https://wiki.genexus.com/commwiki/wiki?17242) | [Update GAM Application Permissions](https://wiki.genexus.com/commwiki/wiki?20590) | [Update GAM Role Permissions](https://wiki.genexus.com/commwiki/wiki?20593) | [Update GAM User Permissions](https://wiki.genexus.com/commwiki/wiki?20583) |
| [Userinfo GAM Service](https://wiki.genexus.com/commwiki/wiki?45316) | [Users enabled or disabled in the GAM Repository](https://wiki.genexus.com/commwiki/wiki?21042) |

---
