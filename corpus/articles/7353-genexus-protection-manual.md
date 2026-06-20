---
title: "GeneXus Protection Manual"
source_id: 7353
source_url: https://wiki.genexus.com/commwiki/wiki?7353
genexus_version: "18"
---

# GeneXus Protection Manual

This document describes the protection system used by [GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) products.

### [Concurrent Licenses and Single User Licenses](#Concurrent+Licenses+and+Single+User+Licenses)

The GeneXus products use two types of licenses:

* **Concurrent Licenses**: A Concurrent License measures the number of network users running a product simultaneously. In this case, GeneXus keeps track of the number of PCs actually using it at any one time and limits this to the number of users you licensed. For example, if you purchased 10 concurrent licenses of one product, no more than 10 users will be able to use that product at the same time.
* [**Single-User License**](https://wiki.genexus.com/commwiki/wiki?24460,,): In this case, each single-user license is assigned to a specific user, the license owner, and only the license owner can use all the product’s features.

The following GeneXus products use concurrent licenses:

* GeneXus Development Environment and all the GeneXus Generators
* GeneXus for SAP Systems and all its components or generators
* GeneXus Server

The following GeneXus products use single-user licenses:

* GXquery
* GXflow Client

To view what type of license each product is using, open the GeneXus License Manager, a GeneXus utility that is automatically installed with GeneXus:

* When you authorize a product that uses single-user licenses, it prompts you for the license owner.
* In the Restriction column, the single-user license information is displayed. Besides, it indicates the number of unassigned copies if the product has licenses that haven’t been assigned.
* The Authorized Users button is enabled only when the license is already assigned to a user.

### [GeneXus License Authorization Overview](#GeneXus+License+Authorization+Overview)

GeneXus licenses are concurrent licenses i.e. if you have N licenses of one GeneXus component, no more than N users will be able to use that component simultaneously.

After installing GeneXus, you have to authorize the licenses of the GeneXus components that you have purchased, such as the GeneXus Developer Environment, GeneXus Generators, and other GeneXus products. Otherwise, you will get a protection error when trying to use those components and products.

To authorize a license, you need to request and install a file called **Site Key** in the machine where you will use the product (local installation) or in a license server (remote installation). The Site Key files have a **gxa** extension.

The process for requesting and installing Site Keys also referred to as requesting and installing GeneXus licenses, is performed using the GeneXus License Manager, a GeneXus utility that is automatically installed when you install GeneXus and any other GeneXus product.

To request a Site Key you will send a GeneXus-generated code, called **Site Code**, to your distributor. Your distributor will process it and send you the corresponding Site Key.

There are two ways to authorize GeneXus licenses:

* **Local Installation**: The Site Key is installed on the same PC where the licensed user will use the product. In this case, the license installation is local while the licensed product may be installed on the user PC (local) or on another machine.
* **Remote Installation**: The Site Key is installed on a different PC than the one where the licensed user will actually use the product. In this case, you need to install the [GeneXus Protection Server](https://wiki.genexus.com/commwiki/wiki?18887,,) on a license server. This option enables licensed users to use the product from any networked PC with access to the license server and is the recommended option for customers using several GeneXus licenses. Here again, the licensed product may be installed on the user PC or on another machine in the network.  
  In addition, the authorization process varies depending on whether or not there are previous versions of GeneXus installed on your PC.

### [GeneXus Protection Server](#GeneXus+Protection+Server)

The [GeneXus Protection Server](https://wiki.genexus.com/commwiki/wiki?18887,,) enables you to install and manage GeneXus licenses in a license server. This enables the GeneXus users in your organization to use GeneXus products on any workstation networked to the license server.

**If your company uses several GeneXus licenses, we strongly encourage you to install and use the GeneXus Protection Server.**

Before requesting your Site Key(s), you need to install [GeneXus Protection Server](https://wiki.genexus.com/commwiki/wiki?18887,,) on the machine that will be the license server. Next, use the GeneXus License Manager to request the Site Key(s), indicating the server name or IP address in the Select Computer option. Note that you can run the GeneXus License Manager from any computer in the license server network.

The GeneXus Protection Server is a service that runs on Windows 2000/XP or higher, and provides licenses to any network client, regardless of where the product is installed (on the server or on any other PC). Clients accessing this service must be under the same domain. Whether you have installed GeneXus locally o remotely, you have to enter the name or IP address of the license server in the Select Computer option of the License Manager.

#### [Downloading and Installing the GeneXus Protection Server](#Downloading+and+Installing+the+GeneXus+Protection+Server)

> 1. Download the latest version of [GeneXus Protection Server](https://wiki.genexus.com/commwiki/wiki?18887,,). GeneXus Protection Server is also available in the GeneXus CD, in the *Software\GeneXus Tools\Developer Tools\GeneXus Protection Server\* directory.  
> 2. Execute the **exe** file that you will find in the zip file that you have just downloaded.  
> 3. If you already have a previous version of the GeneXus Protection Server installed on your PC, a setup wizard from the previous version will be displayed with the Repair/Remove options.  
> 4. Select the Remove option and continue.  
> 5. Rerun the setup after the uninstall process is complete.

#### [Using the GeneXus Protection Server](#Using+the+GeneXus+Protection+Server)

For a detailed description of the GeneXus Protection Server refer to the GeneXus Protection Server documentation: <http://www.genexus.com/gxprotection>.

#### [Requirements](#Requirements)

|  |  |
| --- | --- |
|  | Recommended |
| **Hardware Requirements** | * Hard disk: 50 MB of disk space for the installation. * Processor: 1.0GHz single-core * Memory: 10 MB of RAM. |

|  |  |
| --- | --- |
| **Software Requirements** | * Windows 7 or higher(\*) * .NET Framework 4.7.1. |

(\*)Note: Windows 2000 - Windows 2003 supports up to 9.7.2.17 protection.

### [More Information](#More+Information)

* [Authorizing a GeneXus License for the First Time](https://wiki.genexus.com/commwiki/wiki?19789,,)
* [Authorizing a GeneXus Upgrade License](https://wiki.genexus.com/commwiki/wiki?19790,,)
* [Uninstalling a GeneXus License](https://wiki.genexus.com/commwiki/wiki?19791,,)
* [Transfering a GeneXus License](https://wiki.genexus.com/commwiki/wiki?19792,,)
* [Setting user permissions using remote licenses](https://wiki.genexus.com/commwiki/wiki?19985)

### [Centralized licenses administration scheme](#Centralized+licenses+administration+scheme)

If your company needs to allow the management of licenses only to a few users please read: [GXprotection: Centralized licenses administration scheme](https://wiki.genexus.com/commwiki/wiki?23933,,)

### [[Troubleshooting](https://wiki.genexus.com/commwiki/wiki?53402)](#wiki%3F53402%2CGeneXus%2BProtection%2Btroubleshooting+Troubleshooting)

### [FAQ](#FAQ)

Q: A Windows user makes a license request and when the licenses arrive, another Windows user enter them in License Manager. Will this process finish without problems?

A: Yes, the license authorization is managed through the site code and site key which not depend on the user logged. They depend mainly of the machine information.  
Take into account that both users must have permissions to modify the Windows registry in order to succeed in completing the authorization process.


|  |
| --- |
| **Backlinks** |
| [GXflow license scheme](https://wiki.genexus.com/commwiki/wiki?37204) | [HowTo: Work with GXflow license manager](https://wiki.genexus.com/commwiki/wiki?37207) |
| [License Activation Quick Guide](https://wiki.genexus.com/commwiki/wiki?7643) |

---
