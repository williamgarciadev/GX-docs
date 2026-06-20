---
title: "Integrated Security Level property (GeneXus 18 Upgrade 2 or prior)"
source_id: 54226
source_url: https://wiki.genexus.com/commwiki/wiki?54226
genexus_version: "18"
---

# Integrated Security Level property (GeneXus 18 Upgrade 2 or prior)

Establishes whether the object will have security enforced.

### [Values](#Values)

|  |  |
| --- | --- |
| **Authorization** | Security will be enforced. Object security checks will be done automatically at startup (in case of web objects, before the Start Event). Authentication and Authorization will be automatically checked. Permissions will be generated in the GAM Database. |
| **Authentication** | Security will be enforced. Object security checks will be done automatically at startup, and only Authentication will be checked. In case of web objects, the check is also done in every AJAX call which is executed. This is the default value at Version level. |
| **None** | Security will not be enforced. |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Version

### [Description](#Description)

The property at Version level allows establishing the default value for all the objects of the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

At object level, the property applies to:

* Main [Procedures](https://wiki.genexus.com/commwiki/wiki?6293) or non-main Procedures with [Expose as Web Service property](https://wiki.genexus.com/commwiki/wiki?36480) = True (Rest)
* [Data Providers](https://wiki.genexus.com/commwiki/wiki?5270)
* [Objects for Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?20087)
* Web objects ([Web Panels](https://wiki.genexus.com/commwiki/wiki?6916), [Web Components](https://wiki.genexus.com/commwiki/wiki?1864), [Transactions](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,))

If the property Integrated Security Level is set to "Authentication," the generated code will automatically make the security checks at startup.

If an object is configured with "None," it means that it's a public object of the application.

If the property is set to Authentication, it means that only an authenticated user can access it. If the user is not authenticated, a [Login Object for Web property](https://wiki.genexus.com/commwiki/wiki?15590) or [Login Object for SD property](https://wiki.genexus.com/commwiki/wiki?16589) will be displayed (depending on the application), in order to allow the user to authenticate and access the application.

**Notes**  
1) In Native Mobile applications, take into account that you will generally need to configure the same security level for all objects that are descendants of the entry point of the application, which requires Authentication.

Suppose you have an application with two modules; both are items of the main [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) of the application, but only one of them is going to be secure (that is to say, only one will need Authentication).

In general, you will set the same security level for all WW objects which are descendants of this object in the call tree, because it's the only way to force security to the [REST Web Services](https://wiki.genexus.com/commwiki/wiki?14573) related to these objects. Besides, when a session expires, you will probably need users to be asked to log in again, regardless of the point of the application where they are navigating (if they are inside the module which requires Authentication). As a result, the only way to achieve this is that all descendants of the entry point WW of the secure module have the same security level.

For objects configured with "None", security is not enforced, so REST Web Services will be publicly exposed.

If the property Integrated Security Level is set to "Authorization," users must be logged in, and they need to have rights to access the object they are trying to execute. This security check is automatic.

The application security will be checked automatically by means of [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746).

2) In a Menu object (and Objects for Native Mobile applications for which there isn't a Data Provider automatically generated to implement their business logic, because they do not execute anything on the server), permissions are not verified, and that's why the only available values for Integrated Security Level Property are "None," and "Authentication" in this case.

If you configure "Authentication" in this property, the behavior is not the same as the behavior for Panels or WW Panels: when trying to execute the Menu object for the first time, the Login Object for SD will execute. But in the next executions, session validity is not checked for Menus, so the login object will be displayed again only when the user tries to execute another private object which is called from the Menu.

3) Objects called by [API object](https://wiki.genexus.com/commwiki/wiki?46151) do not check security, since the calls to those objects are internal.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).
