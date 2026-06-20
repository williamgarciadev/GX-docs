---
title: "Keep GAM database updated property"
source_id: 21453
source_url: https://wiki.genexus.com/commwiki/wiki?21453
genexus_version: "18"
---

# Keep GAM database updated property

It indicates whether to save information in the [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) database during Build process.

The information saved in the GAM database is applied when the [GAM Registration process](https://wiki.genexus.com/commwiki/wiki?19964,,) takes place, and when [Automatic Permissions are generated](https://wiki.genexus.com/commwiki/wiki?17916).

### [Values](#Values)

|  |  |
| --- | --- |
| **True** | This is the default value. Saves information in the GAM database each time it is necessary. |
| **False** | Never saves information in the GAM database. |

### [Scope](#Scope)

**Level:** [Environment](https://wiki.genexus.com/commwiki/wiki?7115)

### [Description](#Description)

This property is available at Environment level when [Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) = True.

Take into consideration that when "Keep GAM database updated" is set to False, the GAM database is not reorganized (its structure is not changed).  
On the other hand, if "Keep GAM database updated" is set to True, but [Reorganize server tables property](https://wiki.genexus.com/commwiki/wiki?8955) is set to False, the GAM database should be updated with the applications and permissions registration information, but its structure cannot be changed because the Reorganize Server Tables property indicates not to do it.

The purpose of Keep GAM database updated property is to:

* Be able to make changes to a [KB](https://wiki.genexus.com/commwiki/wiki?2428) that uses a GAM database in production, making sure that this database is not altered.
* Be able to build a [KB](https://wiki.genexus.com/commwiki/wiki?2428) in the cloud ([Cloud prototyping](https://wiki.genexus.com/commwiki/wiki?15046)) without an internet connection.

### [Note](#Note)

* The connection.gam file is not generated when this property is set to False. In fact, the build process does not connect to GAM database.
* When the Keep GAM database updated property is set to False, the following warnings are displayed in the output during the Build process:  
       *Warning: The applications will not be registered. The target environment is set to not reorganize GAM database.*  
  And this error in runtime (on iOS simulator):  
       *Could not load Knowledge Base - Application model main entry point can't be nil.*

### [See Also](#See+Also)

[GAM Applications Registration process](https://wiki.genexus.com/commwiki/wiki?19964,,)  
[SAC #34689](http://www2.gxtechnical.com/portal/hgxppredirect.aspx?15,26,0,,,34689)


|  |
| --- |
| **Backlinks** |
| [Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) |

---
