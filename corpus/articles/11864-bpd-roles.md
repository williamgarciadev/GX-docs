---
title: "BPD Roles"
source_id: 11864
source_url: https://wiki.genexus.com/commwiki/wiki?11864
genexus_version: "18"
---

# BPD Roles

A role defines the different functions and responsibilities to perform within a business process.

Roles are defined independently of the natural persons to whom these roles will be assigned.

If you double-click on the "Roles" node displayed below [Workflow Preferences](https://wiki.genexus.com/commwiki/wiki?17839), the following dialog will appear:

`[imagen omitida: wiki id 7340]`

Once you run or build the KB, an automatic process is executed that updates the roles in the database. In addition, you can execute this process by selecting Deploy business processes. Note that roles will be created or updated during this process, but if you delete a role in the IDE it will not be deleted in the client—you must remove it manually from the [GXflow Roles](https://wiki.genexus.com/commwiki/wiki?10194,,) application.

Roles can also be created from the client, but unless you are using [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746), these roles will not appear in the IDE. For more information about GXflow-GAM synchronization, see this [article](https://wiki.genexus.com/commwiki/wiki?18454).

Role hierarchies defined in the [IDE](https://wiki.genexus.com/commwiki/wiki?5272) are for visualization purposes only, and not intended to inherit permissions.

Shortcuts

|  |  |
| --- | --- |
| **CTRL+I** | Sets a role as a child. |
| **CTRL+U** | Sets a role as a parent. |
| **CTRL+R** | Adds a role as a child of the selected one. |

### [Availability](#Availability)

These shortcuts are available since Genexus X Evolution 2 Upgrade 3.


|  |
| --- |
| **Pages** |
| [Roles Properties](https://wiki.genexus.com/commwiki/wiki?11865) | [Roles property in Task control](https://wiki.genexus.com/commwiki/wiki?11473) |

---
