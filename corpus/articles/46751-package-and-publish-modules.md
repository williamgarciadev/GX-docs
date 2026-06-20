---
title: "Package and Publish Modules"
source_id: 46751
source_url: https://wiki.genexus.com/commwiki/wiki?46751
genexus_version: "18"
---

# Package and Publish Modules

This article shows how to package and publish a [Module object](https://wiki.genexus.com/commwiki/wiki?22411) to a [Modules Server](https://wiki.genexus.com/commwiki/wiki?45933).

When you right-click on a module, you have two options for packaging and publishing

* Package Module ...
  + With this option, you can package and optionally also publish the module
* Publish Module ...
  + With this option, you can publish an already packaged module

### [Package a Module](#Package+a+Module)

When you package a module, you must add specific information for packaging and distribution.

In the information tab, you have to set several Module Object Properties to set.  
Also, you can define external resources ([File object](https://wiki.genexus.com/commwiki/wiki?5852)) to be added, in the Resources Tab.

Read more at [Module object](https://wiki.genexus.com/commwiki/wiki?22411) to know the meaning and objective of each property.

`[imagen omitida: wiki id 46753]`

The available platforms correspond to [Environments](https://wiki.genexus.com/commwiki/wiki?7115) (and the associated Generators) of the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836). You can select the Generators for the ones you want to package (i.e. [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917))

After setting all the properties, you can just Package, or Package & Publish.

#### [For Packaging, GeneXus does the following steps:](#For+Packaging%2C+GeneXus+does+the+following+steps%3A)

1. **Building**. GeneXus builds the Module for each selected environment. (GeneXus actually 'Rebuild's it)
2. **Packaging**. GeneXus creates a package that contains the binaries and module definition files.

In this specific case, it generated a "<Knowledge Base Directory>\modules\mymodule\_1.0.opc" file. (The 'opc' extension stands for Open Packaging Convention; it is a zip file)

The binary is created with the provided version and copyright information.

### [Publish a Module](#Publish+a+Module)

The 'Publish Module ...' option lets you publish a module that is already packaged. It opens the same dialog as the 'Package Module ...' option, with all fields read-only.

When you publish a module to a [Modules Server](https://wiki.genexus.com/commwiki/wiki?45933), GeneXus does one of the following, depending on the server's type:

* **Directory**: GeneXus copies the packaged module to the corresponding folder
* **Nexus**: GeneXus uploads the packaged module to the Nexus' maven or NuGet repository.

## [Troubleshooting](#Troubleshooting)

### [When Publishing, Maven gives an error 401](#When+Publishing%2C+Maven+gives+an+error+401)

Probably because the settings.xml file that indicates the key is not correct. Make sure that with that user and password you can log in on Nexus.

### [When Publishing, Maven gives an error 405](#When+Publishing%2C+Maven+gives+an+error+405)

Probably this is due to the fact that when configuring the Server Source the full URL of a Nexus repository was not set.


|  |
| --- |
| **Backlinks** |
| [Microservices systems](https://wiki.genexus.com/commwiki/wiki?55526) | [Toc:Modules](https://wiki.genexus.com/commwiki/wiki?22414) | [Modules Distribution in GeneXus](https://wiki.genexus.com/commwiki/wiki?31376) |
| [Modules Server](https://wiki.genexus.com/commwiki/wiki?45933) | [Modules Server (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55061) | [Package and Publish Modules (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55057) |

---
