---
title: "Connection User Name property"
source_id: 15217
source_url: https://wiki.genexus.com/commwiki/wiki?15217
genexus_version: "18"
---

# Connection User Name property

Sets the username to establish a security check (a logical connection) before executing any GAM API call or code.

### [Scope](#Scope)

**Level:** [Environment](https://wiki.genexus.com/commwiki/wiki?7115)

### [Description](#Description)

This property is available when [GAM is activated in your KB](https://wiki.genexus.com/commwiki/wiki?19946).

Multiple connections can be defined for each [GAM repository](https://wiki.genexus.com/commwiki/wiki?17568) to keep the GAM database safe.

When defining a [GAM repository connection](https://wiki.genexus.com/commwiki/wiki?16150), you are asked to enter the following:

- **Connection Username** (in this property)  
- **Connection User password**(in the [Connection User Password property](https://wiki.genexus.com/commwiki/wiki?15218))

The default value of this property is: <KB\_name>, for prototyping purposes. It can be changed before the GAM database is created. In this case, a new GAM repository connection will be created during the [activation process in GAM](https://wiki.genexus.com/commwiki/wiki?21973), and the connection user will have the settings provided in the Connection User Name property.

However, if the GAM database has already been created, only an existing connection user name can be specified in the Connection Username property.

**Notes:**

* If the Connection User Name propertyvalue changes, you need to build any object. The connection.gam file is updated with the information given in the Connection User Name property*.* For more information, read [SAC #30451](https://www.genexus.com/en/developers/websac?data=30451;;).

### [See Also](#See+Also)

[Connection User Password property](https://wiki.genexus.com/commwiki/wiki?15218)


|  |
| --- |
| **Backlinks** |
| [Administrator User Password property](https://wiki.genexus.com/commwiki/wiki?15216) | [Change Password Object for SD property](https://wiki.genexus.com/commwiki/wiki?20013) | [Connection User Password property](https://wiki.genexus.com/commwiki/wiki?15218) |
| [Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) | [GAM - Applications deployment](https://wiki.genexus.com/commwiki/wiki?21219) | [GAM - Repository Connections](https://wiki.genexus.com/commwiki/wiki?16150) |
| [GAM - Troubleshooting](https://wiki.genexus.com/commwiki/wiki?22815) | [GAM repository creation for the first time from GeneXus](https://wiki.genexus.com/commwiki/wiki?29701) | [GAM repository management in GeneXus](https://wiki.genexus.com/commwiki/wiki?15769) | [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) |
| [HowTo: Create New Repositories using GAM](https://wiki.genexus.com/commwiki/wiki?18642) | [HowTo: Emulate SSO without using GAM remote authentication](https://wiki.genexus.com/commwiki/wiki?38116) | [HowTo: Use the same GAM Database by different applications](https://wiki.genexus.com/commwiki/wiki?16151) | [Login Object for SD property](https://wiki.genexus.com/commwiki/wiki?16589) |
| [Login Object for Web property](https://wiki.genexus.com/commwiki/wiki?15590) | [Not Authorized Object for SD property](https://wiki.genexus.com/commwiki/wiki?20018) |
| [Repository ID Environment property](https://wiki.genexus.com/commwiki/wiki?15802) |

---
