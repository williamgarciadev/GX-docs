---
title: "GAM - Native Mobile Authentication"
source_id: 15222
source_url: https://wiki.genexus.com/commwiki/wiki?15222
genexus_version: "18"
---

# GAM - Native Mobile Authentication

Due to the [Online Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?14981), it's essential to have a security mechanism to restrict access only to users authorized to the application data.

In this architecture, it's through [REST Web Services](https://wiki.genexus.com/commwiki/wiki?14573) that data updates (PUT, POST, DELETE) and queries (GET) are performed. That's the reason why it's so important to have a security mechanism to prevent that such actions are performed by not authorized users.

The [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) automates the creation of this security mechanism.

To implement Native Mobile authentication using GeneXus Access Manager (GAM), follow these steps:

* [Enable Integrated Security Property](https://wiki.genexus.com/commwiki/wiki?14706): Configure this property in your GeneXus environment to automatically integrate security into your Native Mobile application.
* Configuring GAM Repository: Refer to [GAM repository creation for the first time from GeneXus](https://wiki.genexus.com/commwiki/wiki?29701) for detailed steps on setting up your GAM repository within GeneXus.

### [See Also](#See+Also)

[My first application with integrated security enabled](https://wiki.genexus.com/commwiki/wiki?15275)  
[GAM architecture for Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?14978)


|  |
| --- |
| **Backlinks** |
| [GAM - Authentication Scenarios](https://wiki.genexus.com/commwiki/wiki?15937) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [Table of contents:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
