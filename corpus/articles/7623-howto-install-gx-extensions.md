---
title: "HowTo: Install GX extensions"
source_id: 7623
source_url: https://wiki.genexus.com/commwiki/wiki?7623
genexus_version: "18"
---

# HowTo: Install GX extensions

There are several ways to install an extension. This document provides a brief overview about it.

### [Installing from GeneXus Start Page](#Installing+from+GeneXus+Start+Page)

In the Extensions area of the Start Page, you can see a list of extensions available for your GeneXus version. Each listed extension has an Installation link, which allows you to automatically download and install the extension.

### [Installing from GeneXus Extensions Manager](#Installing+from+GeneXus+Extensions+Manager)

Using the Extensions Manager (you can access it by selecting the option: *Tools > Extensions Manager* in the GeneXus menu), you can see all the installed extensions. An Add button in the upper right corner shows you a list of available extensions from which you may choose anyone to automatically download and install.

### [Manual installation](#Manual+installation)

You can manually download and install any GXextension by placing its corresponding *.dll* files in the Packages folder of your GeneXus installation path. For example: "C:\Program Files\ARTech\GeneXus\GeneXusX\Packages".

And finally running  GeneXus with the */install* parameter. For example: "C:\Program Files\ARTech\GeneXus\GeneXusX\genexus /install".  
This does not actually start GeneXus, but it makes it scan the Packages folder and install any extension it finds in it. Next time you start GeneXus, you should find the new extension listed in the Extensions Manager.


|  |
| --- |
| **Backlinks** |
| [GXtest 4 Releases - Public Channels](https://wiki.genexus.com/commwiki/wiki?42858) |

---
