---
title: "GeneXus Workstation Setup"
source_id: 25844
source_url: https://wiki.genexus.com/commwiki/wiki?25844
genexus_version: "18"
---

# GeneXus Workstation Setup

You must execute this option from each workstation that will use a GeneXus shared installation (already executed following this [GeneXus Installation Steps](https://wiki.genexus.com/commwiki/wiki?25842)).

1.   Execute GXNSetup.exe from the Nsetup directory located in the GeneXus installation directory.

**Note:**  If the directory where the new version is installed is mapped as a logical unit, this mapping must be kept after the execution of the Workstation Setup; otherwise the installation will not work properly. UNC paths are also supported.

2.   Prerequisites check. See point 2 of [Standalone Installation](https://wiki.genexus.com/commwiki/wiki?25842).  
3.   Register your name and company name in the dialog box displayed after the Welcome window.  
4.   After that, you will be able to indicate the Start Menu group, and whether you want to register the settings for your username only, or for all the users that share the PC.  
5.   Once the installation is complete, a dialog box with two options is displayed: Run GeneXus (launchs GeneXus) and Finish Setup.

### [Disadvantages of running a shared GeneXus installation](#Disadvantages+of+running+a+shared+GeneXus+installation)

* You may experience slower performance for some GeneXus operations
* If the server or the shared directory is not available, you cannot use GeneXus
