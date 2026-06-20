---
title: "Application ID property"
source_id: 18667
source_url: https://wiki.genexus.com/commwiki/wiki?18667
genexus_version: "18"
---

# Application ID property

Identifies the Web GAM Application GUID of the KB in GeneXus Access Manager security module.

### [Scope](#Scope)

**Level:** Version

### [Description](#Description)

The information is used when [permissions](https://wiki.genexus.com/commwiki/wiki?15912) are checked in runtime.

In F5 process, the "Application ID" information is copied to application.gam file (located in the virtual directory). See [GAM - Applications Registration option](https://wiki.genexus.com/commwiki/wiki?16288) for details on this process.

Only one web [GAM Application](https://wiki.genexus.com/commwiki/wiki?15910) can be specified for each KB. Nevertheless, there can exist many Web GAM Applications in a [repository](https://wiki.genexus.com/commwiki/wiki?17568) (see links below for more information).

When running a web application, [GeneXus Access Manager](https://wiki.genexus.com/commwiki/wiki?24746) checks that this application (identified by the Application ID) is defined within the repository where the user is connected to.

Because application.gam file stores the information of only one Web GAM Application, one physical web app is associated to one Web Application. So GAM retrieves the Application ID information and that is going to be used when permissions are checked. The permissions have to be defined for the Applications retrieved in application.gam file.

**Note:** For Native Mobile Applications, the Client Application data ([Client Id and Client Secret information](https://wiki.genexus.com/commwiki/wiki?21454,,)) of the Applications is used to implement the security mechanism using OAuth.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [See Also](#See+Also)

[GAM - Applications Registration option](https://wiki.genexus.com/commwiki/wiki?16288)  
[Managing GAM Repositories and GAM Applications in GX development time](https://wiki.genexus.com/commwiki/wiki?18685,,)


|  |
| --- |
| **Backlinks** |
| [GAM - Applications](https://wiki.genexus.com/commwiki/wiki?15910) | [GAM - Troubleshooting](https://wiki.genexus.com/commwiki/wiki?22815) | [GAM: A way to solve Forgot Password](https://wiki.genexus.com/commwiki/wiki?16923) |
| [HowTo: Configure GAM to use Security Token Service](https://wiki.genexus.com/commwiki/wiki?43206) |
|

---
