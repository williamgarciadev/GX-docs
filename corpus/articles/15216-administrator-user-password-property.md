---
title: "Administrator User Password property"
source_id: 15216
source_url: https://wiki.genexus.com/commwiki/wiki?15216
genexus_version: "18"
---

# Administrator User Password property

Enables password configuration for the Administrator User Name in order to access an application with the Enable Integrated Security property set to Yes.

### [Scope](#Scope)

**Level:** [Environment](https://wiki.genexus.com/commwiki/wiki?7115)

### [Description](#Description)

For prototyping purposes, the default value is **admin123**.

#### [Important](#Important)

The purpose of the [Administrator User Name property](https://wiki.genexus.com/commwiki/wiki?15215) is to facilitate prototyping. It's created only at GAM database initialization (when the [Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) is first checked).

Changing the properties [Administrator User Name](https://wiki.genexus.com/commwiki/wiki?15215) and Administrator User Passwordafter the GAM database has been initialized will not force the creation of a new user or the change of its password because they are only for initialization purposes.

All GeneXus applications are registered by this user in order to run within F5. Therefore:

* To change the Administrator password, run [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) and change the password as desired. This change will not affect GeneXus F5, so you will not need to change the [Administrator User Password property](https://wiki.genexus.com/commwiki/wiki?15216).
* If you delete this user in the Web Backoffice, or if you define another one, you should change the [Administrator User Name property](https://wiki.genexus.com/commwiki/wiki?15215) so that GeneXus Dashboards will be registered with this new user that you have defined.

Remember that the Administrator User is only for developing purposes, and it has default values to facilitate prototyping (admin / admin123). However, since it exists as a real administrator user in the GAM database, it is recommended that you change its password.

### [See Also](#See+Also)

[My first Native Mobile application with GAM](https://wiki.genexus.com/commwiki/wiki?15275)  
[Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706)  
[Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214)  
[Administrator User Name property](https://wiki.genexus.com/commwiki/wiki?15215)  
[Connection User Name property](https://wiki.genexus.com/commwiki/wiki?15217)  
[Connection User Password property](https://wiki.genexus.com/commwiki/wiki?15218)  
[Login Object for Web property](https://wiki.genexus.com/commwiki/wiki?15590)


|  |
| --- |
| **Backlinks** |
| [Administrator User Name property](https://wiki.genexus.com/commwiki/wiki?15215) | [Administrator User Password property](https://wiki.genexus.com/commwiki/wiki?15216) | [Change Password Object for SD property](https://wiki.genexus.com/commwiki/wiki?20013) |
| [Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) | [GAM - Troubleshooting](https://wiki.genexus.com/commwiki/wiki?22815) | [GAM repository creation for the first time from GeneXus](https://wiki.genexus.com/commwiki/wiki?29701) | [GAM repository management in GeneXus](https://wiki.genexus.com/commwiki/wiki?15769) |
| [HowTo: Create New Repositories using GAM](https://wiki.genexus.com/commwiki/wiki?18642) | [HowTo: Emulate SSO without using GAM remote authentication](https://wiki.genexus.com/commwiki/wiki?38116) | [HowTo: Use the same GAM Database by different applications](https://wiki.genexus.com/commwiki/wiki?16151) | [Login Object for SD property](https://wiki.genexus.com/commwiki/wiki?16589) |
| [Login Object for Web property](https://wiki.genexus.com/commwiki/wiki?15590) | [Not Authorized Object for SD property](https://wiki.genexus.com/commwiki/wiki?20018) |
| [Repository ID Environment property](https://wiki.genexus.com/commwiki/wiki?15802) |

---
