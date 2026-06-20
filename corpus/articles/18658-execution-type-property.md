---
title: "Execution Type property"
source_id: 18658
source_url: https://wiki.genexus.com/commwiki/wiki?18658
genexus_version: "18"
---

# Execution Type property

Specifies how the Apple application will be executed.

### [Values](#Values)

|  |  |
| --- | --- |
| **Build for Distribution (Local)** | Transfers the XCode project to a Mac and compiles the application using the distribution signature generating an \*.ipa file. Next, the file is copied to the KB environment folder. DEPRECATED from GeneXus 17 Upgrade 10, Distribution Method property should be used instead. |
| **Build IPA (Local)** | Transfers the XCode project to a Mac and compiles the application using the method specified in the Distribution Method property generating an \*.ipa file. Next, the file is copied to the KB environment folder. |
| **iOS Device (Mac)** | Transfers the XCode project to a Mac, compiles the application and executes it in the physical device connected to the Mac. The Development Team ID property must be set. |
| **iTunes Sync (Local)** | Transfers the XCode project to a Mac and compiles the application generating an \*.ipa file. Next, it copies it from the Mac to the development PC (note that the Output window of the GeneXus IDE shows the path where it was copied to), and automatically opens iTunes to show the application in the application catalog. |
| **Knowledge Base Navigator (Device)** | The application metadata is generated and if a device is specified in the Execution Device property, the application is opened in that device using the KBN (Knowledge Base Navigator). No Mac is needed in this process. |
| **Simulator (Mac)** | Transfers the XCode project to a Mac, compiles the application and executes it in the simulator specified in the iOS Simulator property. |

### [Scope](#Scope)

**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Level:** Generator

### [Description](#Description)

* An \*.ipa file is an iOS application archive file that stores an iOS app.
* GeneXus uses the XCode command-line tool package called *xcodebuild*to generate the application in the Mac environment.
* The generated Xcode project is created with the "Automatically manage signing" property enabled. This function only is useful when the application will be executed in a physical device and in order to make it properly work, the following must be considered:

  + [Development Team ID property](https://wiki.genexus.com/commwiki/wiki?30100) must be set.
  + A valid application signing profile and certificate must exist in Xcode or a proper account with the necessary permissions over profiles, app ids and certificate must be configured in Xcode accounts option.
* It is highly recommended that the developer stores the *build/<MainObjectName>.xcarchive* file in every release of the application. This is important if the developer wants to build and install an old version of the application, which may not be available anymore on the App Store or TestFlight.
* When building for executing in a device (Build for Distribution, Build IPA, iOS Device or iTunes Sync options), GeneXus may throw an error. You will need to go to the Mac Terminal and manually execute (only the first time) the sshExec command that is failing (it is the command that contains "-allowProvisioningUpdates"). This situation happen because the the ssh session where the command is being executed, is not interactive.
* Local building options are unavailable for GeneXus 15 [U1](https://wiki.genexus.com/commwiki/wiki?32288,,), [U2](https://wiki.genexus.com/commwiki/wiki?32886,,), [U3](https://wiki.genexus.com/commwiki/wiki?33278,,), [U4](https://wiki.genexus.com/commwiki/wiki?33798,,). In these cases, refer to [HowTo: Create an .ipa file from XCode](https://wiki.genexus.com/commwiki/wiki?34616,,) for creating it manually.
* When generating in GeneXus 17 Upgrade 9 or prior and building **In-House applications** you will need to perform the last steps of the application distribution in Xcode. A typical process would be to build the application with any of the availables execution types (excepting the one for KBN) and after that open the project in Xcode and continue the process of Archive and Distribute from there, following the indications from the [Apple documentation](https://support.apple.com/es-es/guide/deployment/depce7cefc4d/web).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

* [Distribution Method property](https://wiki.genexus.com/commwiki/wiki?50713)
* [Generate Apple property](https://wiki.genexus.com/commwiki/wiki?18656)
* [HowTo: Prototye an iOS Application on a Mac](https://wiki.genexus.com/commwiki/wiki?14761)


|  |
| --- |
| **Backlinks** |
| [Development Team ID property](https://wiki.genexus.com/commwiki/wiki?30100) | [Distribution Method property](https://wiki.genexus.com/commwiki/wiki?50713) | [Generate Apple property](https://wiki.genexus.com/commwiki/wiki?18656) |
| [HowTo: Configure Push Notifications in Apple Applications](https://wiki.genexus.com/commwiki/wiki?17451) | [HowTo: Configure Push Notifications in Apple Applications (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54517) |
| [HowTo: Publish an application to the Apple App Store](https://wiki.genexus.com/commwiki/wiki?18958) | [iOS Applications Wireless Prototyping](https://wiki.genexus.com/commwiki/wiki?15576) | [iOS Specific properties](https://wiki.genexus.com/commwiki/wiki?31827) |
| [My first iOS application](https://wiki.genexus.com/commwiki/wiki?14738) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Prototyping in iOS with a compiled application](https://wiki.genexus.com/commwiki/wiki?17380) |

---
