---
title: "Restricted access to GAM Backoffice"
source_id: 18495
source_url: https://wiki.genexus.com/commwiki/wiki?18495
genexus_version: "18"
---

# Restricted access to GAM Backoffice

In general, only [GAM Repository](https://wiki.genexus.com/commwiki/wiki?17568) administrators will be able to execute the [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935).

The restriction that only allows authorized users to access the GAM Backoffice is automatically implemented; the necessary code is automatically included in the backend objects, as we'll see in this document.

First, set the [GAM - Examples](https://wiki.genexus.com/commwiki/wiki?21993) [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) to "Authentication". The master page used checks that the user has a role that will allow him to access the GAM Backoffice objects.

To confirm that, edit the "GAMMasterpage" object (it's the Master Page object of "GamHome" Web Panel, which is the entry point of GAM Backoffice) and take a look at the code in the Start Event:

```
Event Start
    If GAMUser.CheckRoleByExternalId(!"is_gam_administrator")
        Header1.Object= GAMHeader.Create(ContHolder1.Pgmname)
        //OK
    Else
        GAMExampleNotAuthorized.Link()
    Endif    
EndEvent
```

So, the [CheckRoleByExternalId method](https://wiki.genexus.com/commwiki/wiki?20595) of the GAMUser object is used to check for the "is\_gam\_administrator" Role External Id.  
By default, the Administrator role (created automatically) has this Role External Id. The Role External Id for the Administrator role is updated in the GAM Applications registration (and in the initialization of the GAM metadata).

### [Compatibility](#Compatibility)

Note that in previous versions, the CheckPermission method was used to check if the user had access to the GAM Backoffice. In that case, the [Require Access Permissions Application Property](https://wiki.genexus.com/commwiki/wiki?18512) was required to be activated.

Now, this property isn't required because roles are checked and not permissions.

####


|  |
| --- |
| **Backlinks** |
| [GAM - Permissions Created by the User](https://wiki.genexus.com/commwiki/wiki?29723) | [Category:GAM - Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) | [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) |
| [HowTo: Create New Repositories using GAM](https://wiki.genexus.com/commwiki/wiki?18642) | [HowTo: Give Restricted Access to a Group of Web Objects](https://wiki.genexus.com/commwiki/wiki?18510) |

---
