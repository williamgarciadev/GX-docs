---
title: "Transferring a GeneXus License"
source_id: 19792
source_url: https://wiki.genexus.com/commwiki/wiki?19792
genexus_version: "18"
---

# Transferring a GeneXus License

You can transfer GeneXus licenses between PCs, license servers, and also between PCs and license servers.

## [When to transfer a license](#When+to+transfer+a+license)

Below is a list of the situations in which you may need to transfer GeneXus licenses:

* From one license server to another (to upgrade the server machine)
* From a license server to a user PC (when someone in your organization needs to use GeneXus products off-site)
* From a user PC to a license server (the opposite of the previous case)
* From a user PC to another user PC (to upgrade a user PC)

## [Transfer methods](#Transfer+methods)

There are two ways to transfer GeneXus licenses:

### [1. Direct Transfer](#1.+Direct+Transfer)

This option enables you to transfer one or more licenses from a user PC or protection server to another located in the same network. The GeneXus Protection Server must be installed on the target server.

To perform a Direct Transfer:

* Open the License Manager and click on Select Computer... to connect to the source machine, that is to say, where the license is currently installed.
  + If the license to be transferred is on a PC, the Direct Transfer must be performed from the source machine. Otherwise, if the license is on a server, the transfer can be performed either from the source server or the target server.
* Click on the Transfer... button, select the Direct Transfer option, enter the target server name, and the number of copies to be transferred. When you have finished, click on OK.

**Note**: The process to transfer single-user licenses is different from that of concurrent licenses in that the user(s) to be transferred must be indicated in the transference dialog box.

### [2. Remote Transfer](#2.+Remote+Transfer)

This option is used for transferring one or more licenses between two machines. Transfers can occur between two servers, two PCs, a server and a PC, or vice versa.

Remote transfers involve three actions in the License Manager:

#### [**1. Register Transfer (on the target machine)**](#1.+Register+Transfer+%28on+the+target+machine%29)

When you click on Register Transfer, you are asked to choose between two modes:

* **Multiple:** Allows you to select several licenses to transfer at the same time.
* **Simple:** Creates a transfer file for a single license.

After selecting the mode, a .trf file is created in the selected path. This file must then be moved to the source machine.

#### [**2. Transfer Out (on the source machine)**](#2.+Transfer+Out+%28on+the+source+machine%29)

This action updates the .trf file created in the previous step with the license information. Depending on the selected mode, the file may include one or several licenses.

Move the file back to the target machine.

#### [**3. Transfer In (on the target machine)**](#3.+Transfer+In+%28on+the+target+machine%29)

This action imports the license information contained in the .trf file into the machine registry. The file may contain one or multiple licenses, based on the mode chosen during the Register Transfer step.

### [See Also](#See+Also)

[Authorization and uninstallation of GeneXus licences](https://wiki.genexus.com/commwiki/wiki?26075)


|  |
| --- |
| **Backlinks** |
| [GeneXus Protection Manual](https://wiki.genexus.com/commwiki/wiki?7353) |

---
