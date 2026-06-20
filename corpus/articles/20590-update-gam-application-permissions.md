---
title: "Update GAM Application Permissions"
source_id: 20590
source_url: https://wiki.genexus.com/commwiki/wiki?20590
genexus_version: "18"
---

# Update GAM Application Permissions

The GAMApplication object of [GeneXus Access Manager](https://wiki.genexus.com/commwiki/wiki?24746) Library provides methods that can be used to add, update, and delete [GAM Permissions](https://wiki.genexus.com/commwiki/wiki?15912) in the Application.

Before adding Permissions to Users or to [Roles](https://wiki.genexus.com/commwiki/wiki?17569), the Permission needs to be added in any of the [applications](https://wiki.genexus.com/commwiki/wiki?15910) of the Repository.

This can be done using the [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) or programmatically using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535).

### [AddPermission Method of GAMApplication Object](#AddPermission+Method+of+GAMApplication+Object)

#### [Syntax](#Syntax)

GAMApplication.AddPermission(in:GAMApplicationPermission,out:GAMError Collection): Boolean

#### [Sample](#Sample)

To add a new Permission in the Application, you need to define a GAMApplicationPermission object type variable.

```
&GAMApplicationPermission = new()
&GAMApplicationPermission.Name = 'MyPermission1'
&GAMApplicationPermission.Description = 'MyPermission1'
&GAMApplicationPermission.AccessType = GAMPermissionAccessTypeDefault.Restricted //Possible values are Allow, Deny, Restricted
&isok = &Application.AddPermission(&GAMApplicationPermission,&Errors)
if &isok
   commit
else
   For &Error in &Errors
       Msg(Format(!"%1 (GAM%2)", &Error.Message, &Error.Code))
   EndFor
endif
```

### [UpdatePermission Method of GAMApplication Object](#UpdatePermission+Method+of+GAMApplication+Object)

#### [Syntax](#Syntax)

GAMApplication.UpdatePermission(in:GAMApplicationPermission,out:GAMError Collection) : Boolean

### [DeletePermission Method of GAMApplication Object](#DeletePermission+Method+of+GAMApplication+Object)

#### [Syntax](#Syntax)

GAMApplication.DeletePermission(in:GAMApplicationPermission,out:GAMError Collection) : Boolean


|  |
| --- |
| **Backlinks** |
| [GAM - Permissions](https://wiki.genexus.com/commwiki/wiki?15912) | [Permission Access Type](https://wiki.genexus.com/commwiki/wiki?20603) | [Update GAM Role Permissions](https://wiki.genexus.com/commwiki/wiki?20593) |
| [Update GAM User Permissions](https://wiki.genexus.com/commwiki/wiki?20583) |

---
