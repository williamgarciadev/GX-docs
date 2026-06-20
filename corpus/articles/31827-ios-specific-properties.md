---
title: "iOS Specific properties"
source_id: 31827
source_url: https://wiki.genexus.com/commwiki/wiki?31827
genexus_version: "18"
---

# iOS Specific properties

## [Properties](#Properties)

### [Execution Type](#Execution+Type)

The purpose of this property is to set an execution option of the diversity offers by iOS. [Learn more](https://wiki.genexus.com/commwiki/wiki?18658).

|  |  |
| --- | --- |
| **Value** | **Description** |
| **Simulator (Mac)** | Runs the application on a Simulator in the Mac computer. |
| **iOS Device (Mac)** | Runs the application on a physical device connected on the Mac computer. |
| **iTunes Sync (Local) (\*)** | Compiles de application on the Mac computer, transfers the *\*.ipa* file generated  to the local computer and open iTunes in order to sync with some pysical device connected. |
| **Build IPA (Local) (\*)** | Same process described above but not open iTunes, only copy the *\*.ipa* generated file. |
| **Build for Distribution (Local) (\*)** | Compiles the application on a Mac computer using the distribution signature in order to generate an *\*.zip* file in the GeneXus model directory. |
| **Knowledge Base (Device)** - Default | Allows running the application in a physical device with KBN installed using the Service URL. |

**(\*)Deprecated**as from GeneXus 15 Upgrade 1.

### [Simulator](#Simulator)

Only available when Execution Type property is set in Simulator.  
There are several ways to prototype an application depending on the device hardware features.  
As a developer only need to indicate which device you want to run your application.

|  |
| --- |
| **Value** |
| **iPhone Retina (3.5-inch)** |
| **iPhone Retina (4-inch)** |
| **iPhone Retina (4-inch 64-bits)** |
| **iPhone Retina (4.7-inch 64-bits)** - Default |
| **iPhone Retina HD (5.5-inch 64-bits)** |
| **iPad** |
| **iPad Retina** |
| **iPad Retina (64-bits)** |

### [Simulator SDK](#Simulator+SDK)

Specifies which SDK the developers prefer to build their iOS application.  
It is recommendable not change the default value.

|  |  |
| --- | --- |
| **Value** | **Description** |
| **8.0** | Valid until iOS 8.0 |
| **Latest** - Default | Valid until the latest version of iOS (\*) |

Note: (\*) August 9th, 2016 - 9.1

### [Mac Host, Mac User & Mac Password](#Mac+Host%2C+Mac+User+%26+Mac+Password)

|  |  |
| --- | --- |
| **Mac Host** | Your Mac computer name (computer name property on the [Remote Login settings](https://wiki.genexus.com/commwiki/wiki?14761)) or its IP address. |
| **Mac User** | User to connect the Windows computer to the Mac computer (allowed previously on the [Remote Login settings](https://wiki.genexus.com/commwiki/wiki?14761) settings). |
| **Mac Password** | Mac user password. |


## [Swift generator](#Swift+generator)

Only for advanced users.

### [Name](#Name)

Custom name for the generator. By default is "Swift".

### [General](#General)

* **Use decimal arithmetic**  
  Refer to [Use decimal arithmetic property](https://wiki.genexus.com/commwiki/wiki?10324).

### [Data Access Information](#Data+Access+Information)

* **Transaction integrity**  
  Refer to [Transactional integrity property](https://wiki.genexus.com/commwiki/wiki?8957)
* **Initialize not referenced attributes**  
  Refer to [Initialize not referenced attributes property](https://wiki.genexus.com/commwiki/wiki?7946)

---

## [**Note**](#Note)

* The property **iOS Simulator = Last used simulator** is **not supported for UI testing on mobile**. Use this option only when running or debugging applications manually. Automated UI tests require selecting a specific simulator.

## 

## [Availability](#Availability)

This set of properties is available as from [GeneXus 15](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?28265,,).   
It might be differences in previous versions.

---
