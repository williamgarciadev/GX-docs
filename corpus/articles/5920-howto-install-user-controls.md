---
title: "HowTo: Install User Controls"
source_id: 5920
source_url: https://wiki.genexus.com/commwiki/wiki?5920
genexus_version: "18"
---

# HowTo: Install User Controls

**Warning**: Since GeneXus 16, it is strongly recommended to create a [User Control object](https://wiki.genexus.com/commwiki/wiki?39356) instead of creating a [Web User Control](https://wiki.genexus.com/commwiki/wiki?27212).

This article describes the steps to install User Controls.

### [Automatic Installation](#Automatic+Installation)

**1.** Run GeneXus and find the user control you want in the Start Page  
(In the Start Page, go to the Marketplace tab and use the search bar to look for the control).

**2.** Click install

**3.** GeneXus will ask you whether you want to install the control, click YES

**4.** GeneXus will ask you whether it can restart, click YES

**5.** Check that the toolbox has added the new option under the User Controls section.

**6.** Enjoy!

### [Manual installation](#Manual+installation)

**1.** Download the control from [GeneXus Marketplace](http://marketplace.genexus.com/product.aspx?dropdowntabsmenu).

**2.** Unzip files

**3.** Copy the directory under the UserControls directory in the GeneXus installation.

**4.** Execute GeneXus with the /install parameter. For example: **<GX\_Installation\_Path>\GeneXus /install**

**5.** Check that the toolbox has added the new option under the User Controls section.

**6.** Enjoy!

### [How are the UCs copied to the application directory?](#How+are+the+UCs+copied+to+the+application+directory%3F)

UCs are installed in the GX installation directory (i.e. UserControls\UserControlName) and all the UCs being used by an application are automatically copied from the GeneXus Installation directory to the application directory (e.g. CSharpModel\Web\UserControlName).

**Note**: This copy is done during the build process. Once each User Control being used is copied, a file named “UserControlName.versionId.ver” is created in the application directory (e.g.  CSharpModel\Web) in order to avoid copying the UCs again.

When providing UCs, it is advisable to include the tag “<Version>Number</Version>” in the [UserControlName.control file](https://wiki.genexus.com/commwiki/wiki?13309,,). If this recommendation is followed, the newer version of the user control is copied to the application directory once the UC installation process is complete (i.e. “genexus /install” execution) and building the application.

### [How to update a User Control](#How+to+update+a+User+Control)

What happens when you download or receive a new version of a User Control?  
Follow the steps below :

**1.** Close GeneXus if it is open.

**2.** Replace the files of the User Control which have been updated in the User Control folder under GeneXus installation path.

**3.** Execute GeneXus with the */install* parameter. For example: **<GX\_Installation\_Path>\GeneXus /install**

**4.** Check that the toolbox has added the new option under the User Controls section.

**5.** Enjoy!

### [How to delete a User Control](#How+to+delete+a+User+Control)

Similar steps need to be followed to delete a User Control from your GeneXus installation.

**1.** Close GeneXus if it is open.

**2.** Delete (or move) the User Control folder under GeneXus installation path.

**3.** Execute GeneXus with the /install parameter. For example: **<GX\_Installation\_Path>\GeneXus /install**

**4.** Check that the User Controls is not present in the toolbox.

**Note**: Since [GeneXus 15 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?32886,,) if you run *genexus /install* (instead of genexus**.exe** /install) as an administrator, the result of the installation process is shown in the output.


|  |
| --- |
| **Backlinks** |
| [Gauge Control](https://wiki.genexus.com/commwiki/wiki?9896) | [HowTo: Display a GAM Menu using Jscookmenu UC](https://wiki.genexus.com/commwiki/wiki?29743) | [Map User Control](https://wiki.genexus.com/commwiki/wiki?5029) |
| [Silverlight Photo Gallery User Control](https://wiki.genexus.com/commwiki/wiki?5707) | [Toc:Web User Controls](https://wiki.genexus.com/commwiki/wiki?27212) |

---
