---
title: "Permission Prefix property"
source_id: 17571
source_url: https://wiki.genexus.com/commwiki/wiki?17571
genexus_version: "18"
---

# Permission Prefix property

Indicates the prefix to be used when generating permissions automatically for the Application to which the object belongs.

### [Scope](#Scope)

**Objects:** [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Business Component](https://wiki.genexus.com/commwiki/wiki?5846), [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Web Component](https://wiki.genexus.com/commwiki/wiki?1864), [Work With](https://wiki.genexus.com/commwiki/wiki?15974), [Dashboard](https://wiki.genexus.com/commwiki/wiki?36769), [Query](https://wiki.genexus.com/commwiki/wiki?9026), [API](https://wiki.genexus.com/commwiki/wiki?46151)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

This property is valid in applications where Authorization is going to be checked automatically using [GAM](https://wiki.genexus.com/commwiki/wiki?14960). That is to say, the [Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) is set to "True", and the [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) is set to "Authorization".

The property's default value is the name of the object. You can replace it with any string that follows the syntax for GeneXus object names.

It is available at object level in these particular cases:

* Web objects with URL access ([Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Transactions](https://wiki.genexus.com/commwiki/wiki?1908), [Web Components](https://wiki.genexus.com/commwiki/wiki?1864) with their [URL access property](https://wiki.genexus.com/commwiki/wiki?7868) set to Yes).
* [REST Web Services](https://wiki.genexus.com/commwiki/wiki?14573) ([Procedures](https://wiki.genexus.com/commwiki/wiki?6293), [Business Components](https://wiki.genexus.com/commwiki/wiki?5846), [Data Providers](https://wiki.genexus.com/commwiki/wiki?5270)).
* HTTP Procedures ([Main](https://wiki.genexus.com/commwiki/wiki?5770) Procedures with [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) = HTTP).
* Reporting objects: [Dashboard](https://wiki.genexus.com/commwiki/wiki?36769) and [Query](https://wiki.genexus.com/commwiki/wiki?9026).
* [API object](https://wiki.genexus.com/commwiki/wiki?46151)s.
* [Work With](https://wiki.genexus.com/commwiki/wiki?15974) objects.
* [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s.

In the case of Transactions, a set of permissions is created in the [GAM Repository](https://wiki.genexus.com/commwiki/wiki?17568). They are named as follows:

* <prefix>\_FullControl
* <prefix>\_Execute
* <prefix>\_Insert
* <prefix>\_Update
* <prefix>\_Delete

The "<prefix>\_FullControl" permission groups all permissions: See [Full Control Permissions](https://wiki.genexus.com/commwiki/wiki?17664) for details.

The "<prefix>\_Execute" permission enables you to display the data of the Transaction (display mode).

The other permissions execute an action over the Transaction (Insert, Update, or Delete).

In the case of Business Components exposed as a service, the following permissions are created in the GAM Repository:

* <prefix>\_Services.FullControl
* <prefix>\_Services\_Execute (reads the data, which implies a GET HTTP over the REST service).
* <prefix>\_Services\_Insert (implies a PUT HTTP over the REST service).
* <prefix>\_Services\_Update (implies a POST HTTP over the REST service).
* <prefix>\_Services\_Delete (implies a DELETE HTTP over the REST service).

In the case of Web Panels, Query, and Dashboard objects, the following permission is created in the GAM Repository:

* <prefix>\_Execute

In the case of APIs, the following permissions are created in the GAM Repository:

* <prefix>\_Services\_FullControl
* <prefix>\_Services\_<Method>

**Note:** The permissions of the API object methods can be redefined with the [SecurityPermission annotation](https://wiki.genexus.com/commwiki/wiki?55422).

This property can also be used to group different objects so that all the objects that have the same prefix (i.e. "xxx") will have the same permission names in the GAM Repository (xxx\_insert , xxx\_update, etc.). Thus, the roles to which the xxx\_insert , xxx\_update permissions are assigned will be able to execute all the objects with the **Permission Prefix property** ="xxx".

At runtime, these permissions will be checked automatically when the objects are executed.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

No action is required to apply the corresponding changes when the property value is configured.

### [See Also](#See+Also)

[GAM - Automatic Permissions generated by GeneXus](https://wiki.genexus.com/commwiki/wiki?17916)  
[GAM - Permissions Created by the User](https://wiki.genexus.com/commwiki/wiki?18501,,)  
[Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214)  
[Not Authorized Object for Web property](https://wiki.genexus.com/commwiki/wiki?17551,,)  
[GAM - Permissions](https://wiki.genexus.com/commwiki/wiki?15912)  
[GAM - Authorization Scenarios](https://wiki.genexus.com/commwiki/wiki?17583)  
[HowTo: Define an API object with a security scheme](https://wiki.genexus.com/commwiki/wiki?52840)


|  |
| --- |
| **Backlinks** |
| [Category:API object](https://wiki.genexus.com/commwiki/wiki?46151) | [GAM - Authorization Scenarios](https://wiki.genexus.com/commwiki/wiki?17583) | [GAM - Automatic Permissions generated by GeneXus](https://wiki.genexus.com/commwiki/wiki?17916) |
| [GAM - Automatic Permissions generated by GeneXus (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?53950) | [GAM - Full Control Permissions and inheritance](https://wiki.genexus.com/commwiki/wiki?17664) | [GAM - Main Role of a user](https://wiki.genexus.com/commwiki/wiki?21643) | [GAM - Permissions](https://wiki.genexus.com/commwiki/wiki?15912) |
| [HowTo: Define a Menu using GAM](https://wiki.genexus.com/commwiki/wiki?29681) | [HowTo: Define an API object with a security scheme](https://wiki.genexus.com/commwiki/wiki?52840) | [HowTo: Define an API object with a security scheme (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55404) | [HowTo: GAM Automatic Check of Access Permissions for Web Objects](https://wiki.genexus.com/commwiki/wiki?17585) |
| [HowTo: Implement GAM permissions in Transaction's Modes](https://wiki.genexus.com/commwiki/wiki?18046) | [HowTo: Manage permissions to execute WW Lists and Panels](https://wiki.genexus.com/commwiki/wiki?18064) | [HowTo: Permissions in SD Applications, CRUD Restricted](https://wiki.genexus.com/commwiki/wiki?17935) | [HowTo: Permissions in SD Applications, WW and CRUD Restricted](https://wiki.genexus.com/commwiki/wiki?17943) |
| [HowTo: Use Postman to access secure REST services defined via API Objects](https://wiki.genexus.com/commwiki/wiki?50055) | [Modules - Known Limitations](https://wiki.genexus.com/commwiki/wiki?22492) | [Permission Prefix property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?53928) | [Permission Prefix property (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55357) |
| [Permissions by Method in the API object](https://wiki.genexus.com/commwiki/wiki?55405) | [Permissions Over a User Action in SD Objects](https://wiki.genexus.com/commwiki/wiki?18173) | [Query Object Compatibility](https://wiki.genexus.com/commwiki/wiki?11032) |

---
