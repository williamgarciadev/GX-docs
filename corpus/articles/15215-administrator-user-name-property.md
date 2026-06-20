---
title: "Administrator User Name property"
source_id: 15215
source_url: https://wiki.genexus.com/commwiki/wiki?15215
genexus_version: "18"
---

# Administrator User Name property

Establishes a default privileged user in order to access an application with Enable Integrated Security property set to True.

### [Scope](#Scope)

**Level:** [Environment](https://wiki.genexus.com/commwiki/wiki?7115)

### [Description](#Description)

Inside GeneXus, the administrator user is checked before performing the tasks related to [GAM Applications](https://wiki.genexus.com/commwiki/wiki?15910) registration and [GAM Permissions](https://wiki.genexus.com/commwiki/wiki?15912) generation in the F5 process.

A default administrator user is created during the [Activation Process](https://wiki.genexus.com/commwiki/wiki?21973) to facilitate the prototyping stage. The administrator user is granted all the permissions available for all GAM Applications in the KB.

Changing the properties Administrator User Name and [Administrator User Password](https://wiki.genexus.com/commwiki/wiki?15216) after the GAM database has been initialized will not force the creation of a new user or the change of its password. The property is only for initialization purposes.

This property has a default value—"admin"—for prototyping purposes. This user is defined to facilitate the developing stages of the application.

**Considerations**

* To change the Administrator password, run the [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) and change the password as desired.
* If you delete this user, or if you define another one, you should change the Administrator User Name property.

Remember that this user is only for developing purposes, and it has default values to facilitate prototyping. However, since it exists as a real administrator user in the GAM database, it is advisable to change its password before the application goes into production.

### [See Also](#See+Also)

[Administrator User Password property](https://wiki.genexus.com/commwiki/wiki?15216)  
[Creating the GAM repository for the first time from GeneXus](https://wiki.genexus.com/commwiki/wiki?19942,,)


|  |
| --- |
| **Backlinks** |
| [Administrator User Password property](https://wiki.genexus.com/commwiki/wiki?15216) | [Change Password Object for SD property](https://wiki.genexus.com/commwiki/wiki?20013) | [Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) |
| [GAM - Main Role of a user](https://wiki.genexus.com/commwiki/wiki?21643) | [GAM - Permissions Created by the User](https://wiki.genexus.com/commwiki/wiki?29723) | [GAM - Repository Connections](https://wiki.genexus.com/commwiki/wiki?16150) | [GAM - Troubleshooting](https://wiki.genexus.com/commwiki/wiki?22815) |
| [Category:GAM - Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) | [GAM repository creation for the first time from GeneXus](https://wiki.genexus.com/commwiki/wiki?29701) | [GAM repository management in GeneXus](https://wiki.genexus.com/commwiki/wiki?15769) | [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) |
| [HowTo: Create New Repositories using GAM](https://wiki.genexus.com/commwiki/wiki?18642) | [HowTo: Emulate SSO without using GAM remote authentication](https://wiki.genexus.com/commwiki/wiki?38116) | [HowTo: Use the same GAM Database by different applications](https://wiki.genexus.com/commwiki/wiki?16151) | [Login Object for SD property](https://wiki.genexus.com/commwiki/wiki?16589) |
| [Login Object for Web property](https://wiki.genexus.com/commwiki/wiki?15590) | [Not Authorized Object for SD property](https://wiki.genexus.com/commwiki/wiki?20018) |
| [Repository ID Environment property](https://wiki.genexus.com/commwiki/wiki?15802) |

---
