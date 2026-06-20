---
title: "Necessary Rights to Work With AS/400"
source_id: 14127
source_url: https://wiki.genexus.com/commwiki/wiki?14127
genexus_version: "18"
---

# Necessary Rights to Work With AS/400

Users doing the transfer of sources to AS/400 must be duly authorized by the AS/400 security in order to:

* Create a library (CRTLIB command)
* Create physical files of sources (CRTSRCPF command)
* Create a Cobol program or RPG (depending on what has been selected at the time of installation)
* Create a CL program (CRTCLPGM command)
* Create a command (CRTCMD command)
* Create a physical file (CRTPF command)
* Create a Save File (CRTSAVF command)
* Restore Objects (RSTOBJ command)
* Change the property of objects (CHGOBJOWN command)
* Delete a program (DLTPGM command)
* Execute mandates by line of commands (CHGUSRPRF command)

At the time of installing the library, all the above permits are necessary, in addition to:

* Delete the GX library if it exists already (old versions)


|  |
| --- |
| **Backlinks** |
| [Generating in COBOL](https://wiki.genexus.com/commwiki/wiki?14124) | [Generating in RPG](https://wiki.genexus.com/commwiki/wiki?14095) |

---
