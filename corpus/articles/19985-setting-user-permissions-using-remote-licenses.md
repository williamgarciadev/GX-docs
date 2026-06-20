---
title: "Setting user permissions using remote licenses"
source_id: 19985
source_url: https://wiki.genexus.com/commwiki/wiki?19985
genexus_version: "18"
---

# Setting user permissions using remote licenses

In some situations when you run GeneXus or the GeneXus License Manager using remote licenses, an error message: Access Denied is showed.  
While the causes may be different in each case, this document is a summary of a few steps to verify/perform in practice that have resolved most of the cases.

### [Cases](#Cases)

**A)** CASE OF License Server and PCs in the same Windows DOMAIN

1. Verify that both the PCs and the SERVER are on the same Windows DOMAIN.
2. If the SERVER has Windows Firewall active, add in exceptions:
   * TCP port 135 (DCOM)
   * The Protsrv.exe application (is in: common files\Artech\gxprot1)
3. If your PC has Windows Firewall active: add in exceptions TCP port 135 (DCOM).
4. In the CLIENT add in the Access Permissions section of dcomcnfg.exe, Remote Access permission to the Anonymous Logon user of Edit Limits. (See ref 2).
   * To access the tab "Access Permissions" once executed dcomcnfg.exe, expand the section "Component Services" -> "Computers" -> "My Computer", right click and select "My Computer". After this step can already solve the problem. Otherwise, proceed to the next step.
   * NOTE: In Windows 7 and Vista must run the Gxlmgr with "Run as administrator".
5. Add the network users that get the licenses on group "Artech Remote Protection Users" or "GeneXus Remote Protection Users" in the Windows user group of the SERVER.
6. If using Windows Server 2012 R2 or higher, add the network users to the group "Distributed COM Users" too.
7. If that still gives Access Denied, remove the PC of the domain and add it back (this may involve restart the PC). This has solved many of these problems.
   * Apparently in some cases trust relationship between the PC and the SERVER is not well established. When you add it again the problem is solved.
8. If this does not work, check the net properties of machine. If you changed the IP, check that the DNS is updated, etc.

**B)** CASE OF License Server and PCs in the same WORKGROUP

1. Verify that both the PCs and the SERVER are in the same WORKGROUP.
2. If the SERVER has Windows Firewall active, add in exceptions:
   * a. TCP port 135 (DCOM)
   * b. The Protsrv.exe application (is in: common files\Artech\gxprot1)
3. Define in the SERVER the users that will connect to it (same user and pass). When defining the user, check the option "Password never expires".
   * Pay attention that the user is not blocked. (See ref 3)
4. If the PC has Windows Firewall active: add in exceptions TCP port 135 (DCOM).
5. In the CLIENT add in the Access Permissions section of dcomcnfg.exe, Remote Access permission to the Anonymous Logon user of Edit Limits. (See ref 2).
   * After this step can already solve the problem. Otherwise, proceed to the next step.
6. Add the network users that get the licenses on group "Artech Remote Protection Users" or "GeneXus Remote Protection Users" in the Windows user group of the SERVER. (alternatively, add the user "Everyone") (See ref 1)
7. If using Windows Server 2012 R2 or higher, add the network users to the group "Distributed COM Users" too.
8. If this does not work, check the net properties of machine. If you changed the IP, check that the DNS is updated, etc.

### [References](#References)

* **(ref 1)** Adding the user "Everyone" in the group does not mean that it will accept any user, but those that are defined on that machine, so it is important the step 2.

* **(ref 2)** In some situations it was found that giving permissions to the anonymous user only "Remote Permissions" need not be replicated the user in the server (steps 4 and 5). The only downside is that you will not see the products in the License Manager, but GX works. In Win 7 or XP to set the DCOM permissions must execute: Dcomcnfg/MyComputer/Properties/COM security/Edit Limits.

* **(ref 3)** In some cases, changing this option on the Windows Explorer of the SERVER: "Tools -> Folder Options -> View -> Advanced Settings: Option" Use simple file sharing (recommended) " leaving it unchecked, does not require steps 4 and 5.

### [See also](#See+also)

[Access Denied when using remote licenses - Solution](https://wiki.genexus.com/commwiki/wiki?12481,,)

[Enabling centralized licenses scheme - checklist](https://wiki.genexus.com/commwiki/wiki?12482,,)


|  |
| --- |
| **Backlinks** |
| [GeneXus Protection Manual](https://wiki.genexus.com/commwiki/wiki?7353) | [GXflow license troubleshooting](https://wiki.genexus.com/commwiki/wiki?42990) |

---
