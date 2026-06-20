---
title: "Integrated Security Level property"
source_id: 15214
source_url: https://wiki.genexus.com/commwiki/wiki?15214
genexus_version: "18"
---

# Integrated Security Level property

Establishes whether the object(s) will have security enforced.

### [Values](#Values)

|  |  |
| --- | --- |
| **Authorization** | Security will be enforced. Object security checks will be done automatically at startup (in the case of web objects, before the Start Event). Authentication and Authorization will be automatically checked. Permissions will be generated in the GAM Database. |
| **Authentication** | Security will be enforced. Object security checks will be done automatically at startup, and only Authentication will be checked. In the case of web objects, the check is also done in every AJAX call which is executed. This is the default value at Version level. |
| **None** | Security will not be enforced. |

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974), [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Component](https://wiki.genexus.com/commwiki/wiki?1864), [Query](https://wiki.genexus.com/commwiki/wiki?9026), [Dashboard](https://wiki.genexus.com/commwiki/wiki?36769)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** [Version](https://wiki.genexus.com/commwiki/wiki?7860)

### [Description](#Description)

At [Version level](https://wiki.genexus.com/commwiki/wiki?7860), the property allows establishing the default value for all the objects of the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

At object level, the property applies to:

* Main [Procedures](https://wiki.genexus.com/commwiki/wiki?6293) or non-main Procedures with [Expose as Web Service property](https://wiki.genexus.com/commwiki/wiki?36480) = True (Rest).
* [Data Providers](https://wiki.genexus.com/commwiki/wiki?5270).
* Objects for Native Mobile application development such as [Panels](https://wiki.genexus.com/commwiki/wiki?24829), [Menus](https://wiki.genexus.com/commwiki/wiki?16321), [Work with objects](https://wiki.genexus.com/commwiki/wiki?15974).
* Web objects ([Web Panels](https://wiki.genexus.com/commwiki/wiki?6916), [Web Components](https://wiki.genexus.com/commwiki/wiki?1864),[Transactions](https://wiki.genexus.com/commwiki/wiki?1908)).
* Reporting objects ([Query](https://wiki.genexus.com/commwiki/wiki?9026) and [Dashboard object](https://wiki.genexus.com/commwiki/wiki?36769)).

If the Integrated Security Level property is set to "Authentication", the generated code will automatically make the security checks at startup.

If an object is set to "None", it means that it's a public object of the application.

If the property is set to Authentication, it means that only an authenticated user can access it. If the user is not authenticated, a [Login Object for Web property](https://wiki.genexus.com/commwiki/wiki?15590) or [Login Object for SD property](https://wiki.genexus.com/commwiki/wiki?16589) will be displayed (depending on the application) in order to allow the user to authenticate and access the application.

**Notes**  
1) In objects for Native Mobile applications, take into account that you will generally need to configure the same security level for all objects that are descendants of the entry point of the application, which requires Authentication.

Suppose you have an application with two modules; both are items of the application's main [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) but only one of them is going to be secure (that is to say, only one will need Authentication).

In general, you will set the same security level for all WW objects which are descendants of this object in the call tree because it's the only way to force security to the [REST Web Services](https://wiki.genexus.com/commwiki/wiki?14573) related to these objects. In addition, when a session expires, you will probably need users to be asked to log in again regardless of the point of the application where they are navigating (if they are inside the module which requires Authentication). As a result, the only way to achieve this is that all descendants of the entry point WW of the secure module have the same security level.

For objects configured with "None", security is not enforced so REST Web Services will be publicly exposed.

If the Integrated Security Level property is set to "Authorization", users must be logged in and have rights to access the object they are trying to execute. This security check is automatic.

Application security will be checked automatically by means of the [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746).

2) In a Menu object (and Objects for Native Mobile applications for which there isn't a Data Provider automatically generated to implement their business logic because they do not execute anything on the server), permissions are not verified. That's why the only available values for Integrated Security Level Property are "None" and "Authentication" in this case.

If you configure "Authentication" in this property, the behavior is not the same as the behavior for Panels or WW Panels: when trying to execute the Menu object for the first time, the Login Object for SD will execute. However, in the following executions session validity is not checked for Menus; therefore, the login object will be displayed again only when the user tries to execute another private object that is called from the Menu.

3) Objects called by the [API object](https://wiki.genexus.com/commwiki/wiki?46151) do not check security because the calls to those objects are internal.

4) In Queries and Dashboards, security checks are performed in every service call (i.e. when retrieving data or metadata from the server).

5)In the Data Provider object, the permissions generated when the Integrated Security Level property is set to Authorization are only checked when this Data Provider is invoked from a Query Viewer or when it is exposed as a Web Service.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).


|  |
| --- |
| **Backlinks** |
| [Administrator User Password property](https://wiki.genexus.com/commwiki/wiki?15216) | [Anonymous Sessions in GAM - Web Applications](https://wiki.genexus.com/commwiki/wiki?16414) | [Category:API object](https://wiki.genexus.com/commwiki/wiki?46151) |
| [API object - Troubleshooting](https://wiki.genexus.com/commwiki/wiki?55436) | [API object security scheme](https://wiki.genexus.com/commwiki/wiki?52550) | [Auto-Registration in SD: What to do when a certain action requires the user to log in](https://wiki.genexus.com/commwiki/wiki?19835) | [Biometrics Reuse Duration property](https://wiki.genexus.com/commwiki/wiki?43467) |
| [Change Password Object for SD property](https://wiki.genexus.com/commwiki/wiki?20013) | [Enable Biometrics property](https://wiki.genexus.com/commwiki/wiki?43466) | [Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) | [GAM - Authentication Scenarios](https://wiki.genexus.com/commwiki/wiki?15937) |
| [GAM - Auto-register anonymous users - How it works](https://wiki.genexus.com/commwiki/wiki?19909) | [GAM - Automatic Permissions generated by GeneXus](https://wiki.genexus.com/commwiki/wiki?17916) | [GAM - Automatic Permissions generated by GeneXus (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?53950) | [GAM - External Authentication: version 1.0](https://wiki.genexus.com/commwiki/wiki?21548) |
| [GAM - External Authentication: version 2.0](https://wiki.genexus.com/commwiki/wiki?21555) | [GAM - GAMRemote Authentication Type](https://wiki.genexus.com/commwiki/wiki?25355) | [GAM - Getting Started](https://wiki.genexus.com/commwiki/wiki?19946) | [GAM - Permissions](https://wiki.genexus.com/commwiki/wiki?15912) |
| [GAM - Permissions Created by the User](https://wiki.genexus.com/commwiki/wiki?29723) | [GAM repository creation for the first time from GeneXus](https://wiki.genexus.com/commwiki/wiki?29701) | [GAM use Example: Private web application](https://wiki.genexus.com/commwiki/wiki?15923) | [GAM Use Example: Public Application With Some Private Components](https://wiki.genexus.com/commwiki/wiki?15772) |
| [GeneXus for SAP Systems Security](https://wiki.genexus.com/commwiki/wiki?33842) | [Good practices for secure development using GAM](https://wiki.genexus.com/commwiki/wiki?47241) | [HowTo: Access a Web Panel component using the Smart Devices GAM credentials](https://wiki.genexus.com/commwiki/wiki?33624) |
| [HowTo: Configure GAM to use Security Token Service](https://wiki.genexus.com/commwiki/wiki?43206) | [HowTo: Define an API object with a security scheme](https://wiki.genexus.com/commwiki/wiki?52840) | [HowTo: Define an API object with a security scheme (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55404) |
| [HowTo: Filter data by user using the GAM API](https://wiki.genexus.com/commwiki/wiki?15387) | [HowTo: GAM Automatic Check of Access Permissions for Web Objects](https://wiki.genexus.com/commwiki/wiki?17585) | [HowTo: Give Restricted Access to a Group of Web Objects](https://wiki.genexus.com/commwiki/wiki?18510) | [HowTo: Implement GAM permissions in Transaction's Modes](https://wiki.genexus.com/commwiki/wiki?18046) |
| [HowTo: Manage permissions to execute WW Lists and Panels](https://wiki.genexus.com/commwiki/wiki?18064) | [HowTo: Permissions in SD Applications, CRUD Restricted](https://wiki.genexus.com/commwiki/wiki?17935) | [HowTo: Permissions in SD Applications, WW and CRUD Restricted](https://wiki.genexus.com/commwiki/wiki?17943) | [HowTo: Use GAM and Windows Authentication](https://wiki.genexus.com/commwiki/wiki?24034) |
| [Integrated Security by Domain](https://wiki.genexus.com/commwiki/wiki?50682) | [Integrated Security Level property (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54226) |
| [Login Object for SD property](https://wiki.genexus.com/commwiki/wiki?16589) | [Login Object for Web property](https://wiki.genexus.com/commwiki/wiki?15590) | [Not Authorized Object for SD property](https://wiki.genexus.com/commwiki/wiki?20018) |
| [Offline Native Mobile applications using GAM](https://wiki.genexus.com/commwiki/wiki?23400) | [Permission Prefix property](https://wiki.genexus.com/commwiki/wiki?17571) | [Permission Prefix property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?53928) |
| [Permission Prefix property (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55357) | [Permissions by Method in the API object](https://wiki.genexus.com/commwiki/wiki?55405) | [Permissions Over a User Action in SD Objects](https://wiki.genexus.com/commwiki/wiki?18173) | [Query Object Compatibility](https://wiki.genexus.com/commwiki/wiki?11032) |
| [Repository ID Environment property](https://wiki.genexus.com/commwiki/wiki?15802) | [Require Access Permissions Application Property](https://wiki.genexus.com/commwiki/wiki?18512) | [Restricted access to GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?18495) | [Secure Application Content](https://wiki.genexus.com/commwiki/wiki?43468) |
| [Security considerations in Smooth models](https://wiki.genexus.com/commwiki/wiki?25356) | [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) | [Security Scanner built-in tool (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?52570) |
| [SecurityLevel annotation](https://wiki.genexus.com/commwiki/wiki?55437) | [SecurityPermission annotation](https://wiki.genexus.com/commwiki/wiki?55422) | [UserRememberMeType property](https://wiki.genexus.com/commwiki/wiki?18584) |

---
