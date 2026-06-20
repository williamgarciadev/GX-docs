---
title: "HowTo: Prepare a Mac with an Intel processor for GeneXus"
source_id: 51408
source_url: https://wiki.genexus.com/commwiki/wiki?51408
genexus_version: "18"
---

# HowTo: Prepare a Mac with an Intel processor for GeneXus

This document provides the steps to install GeneXus, including considerations and existing restrictions regarding Apple CPUs with [Intel Core](https://en.wikipedia.org/wiki/Intel_Core) processors.

### [Step 1 - Install desktop virtualization software](#Step+1+-+Install+desktop+virtualization+software)

Since the [GeneXus IDE](https://wiki.genexus.com/commwiki/wiki?5272) runs on Windows, you need to install desktop virtualization software and create a virtual machine. In this case, installing [Parallels](https://www.parallels.com/mx/welcome-trial/) is suggested, and the following steps have been tested on it.

In addition to the [Parallels requirements](https://www.parallels.com/products/desktop/resources/), you need to take into account the [requirements associated with GeneXus](https://wiki.genexus.com/commwiki/wiki?30900).

### [Step 2 - Install Windows](#Step+2+-+Install+Windows)

You can use the Home version of Windows, which is suggested by Parallels.

Also, you can use Windows from Boot Camp, transfer your PC, or install Windows from your source.

### [Step 3 - Install Microsoft SQL Server (Any Edition)](#Step+3+-+Install+Microsoft+SQL+Server+%28Any+Edition%29)

GeneXus stores Knowledge Bases in Microsoft SQL Server. For this reason, you need to install [SQL Server Express LocalDB](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/sql-server-express-localdb?view=sql-server-ver16) or any other edition of SQL Server.

### [Step 4 - Install GeneXus](#Step+4+-+Install+GeneXus)

Follow the [GeneXus Installation Steps](https://wiki.genexus.com/commwiki/wiki?25842) described in the [GeneXus 18 Installation Manual](https://wiki.genexus.com/commwiki/wiki?31997).

### [Step 5 - Install the requirements for Application Prototyping](#Step+5+-+Install+the+requirements+for+Application+Prototyping)

GeneXus provides a variety of mechanisms to easily prototype applications, either with emulators or by executing directly on the device, depending on the selected mobile platform. Even though this scenario is ideal for [prototyping your iPhone or iPad application on your Mac](https://wiki.genexus.com/commwiki/wiki?14761), you can even [Prototyping in iOS with a compiled application](https://wiki.genexus.com/commwiki/wiki?17380).

If you also want to prototype your native mobile application for
[Android](https://wiki.genexus.com/commwiki/wiki?14453), you can follow the steps shown in [Run Android emulator](https://wiki.genexus.com/commwiki/wiki?31323,,)  or [Prototyping Android Apps with Genymotion](https://wiki.genexus.com/commwiki/wiki?28792,,).

Check [GeneXus 17 hardware and software requirements](https://wiki.genexus.com/commwiki/wiki?30900) for other requirements for prototyping applications.

### [See Also](#See+Also)

[HowTo: Prepare a Mac with ARM architecture for GeneXus](https://wiki.genexus.com/commwiki/wiki?51149)


|  |
| --- |
| **Backlinks** |
| [HowTo: Prepare a Mac with ARM architecture for GeneXus](https://wiki.genexus.com/commwiki/wiki?51149) |

---
