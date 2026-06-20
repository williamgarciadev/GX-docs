---
title: "Prototyping in iOS with a compiled application"
source_id: 17380
source_url: https://wiki.genexus.com/commwiki/wiki?17380
genexus_version: "18"
---

# Prototyping in iOS with a compiled application

The first step is to [register](http://developer.apple.com/programs/ios/) yourself as an iOS developer.

Then you need to perform the following steps:

* **Access to the iOS Developer Program | Certificates, Identifiers & Profiles** **section**  
  From the iOS Dev Center, you can access at the right (under iOS Developer Program) and then the Certificates, Identifiers & Profiles option.
* **Create a Development Certificate**  
  This certificate will be used to sign the apps you will be testing. This certificate needs to be installed on the Mac where you will later compile the app.
* **Assign Apple Devices**  
  You can test your apps on up to 100 devices (500 if you have an Enterprise account). You need to register the UDID of these devices.
* **Create App IDs**  
  You have to create an App ID for each app you will be testing. An App ID is a combination of a unique ten-character string called the *Bundle Seed ID* and a traditional CF Bundle ID (or Bundle Identifier). This Bundle Identifier must be the same that the value of the Apple Bundle Identifier property, located under Main object properties > Apple group, on the properties of [Main object](https://wiki.genexus.com/commwiki/wiki?17817). The default value is **com.artech.<Object>**:
* **Create a Provisioning Profile**  
  This [Provisioning Profile](https://wiki.genexus.com/commwiki/wiki?17442) ties the information of the Development Certificate, the App ID, and the devices, and it will also be needed in the Mac where the app will be compiled, and in the device where the app will run.

All these steps are documented in the [Apple iOS Provisioning Portal page](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html), check the How-to's sections, that have detailed instructions and also videos.

After that, you are able to compile your app in the Mac. To do that, configure the following Smart Devices generator properties:

* [Generate Apple property](https://wiki.genexus.com/commwiki/wiki?18656) = True

In the iOS Specific node:

* [Execution Type property](https://wiki.genexus.com/commwiki/wiki?18658) = Build IPA (Local)
* [Mac Host property](https://wiki.genexus.com/commwiki/wiki?36371) = The name or IP of the Mac machine
* [Mac User property](https://wiki.genexus.com/commwiki/wiki?36372) = The Mac user for which you have installed the development certificate and provisioning profile
* [Mac Password property](https://wiki.genexus.com/commwiki/wiki?36373) = Password of the Mac user

`[imagen omitida: wiki id 37577]`

Then, when you press F5 in GeneXus, it will generate the Xcode project for the app, transfer it to the Mac, compile it remotely, and it will generate a **\*.ipa** package file, that it will transfer back to your development machine, and the path will be displayed in the Output window.

## [Notes](#Notes)

* The first time you run the application you will receive an error because the compilation requires an authorization that requires User interaction ('User interaction is not allowed'). You must copy the last command that appears in the output with the error and run it under a Terminal in your Mac using the same User that you configure to compile in GeneXus. The execution of that command will popup a Confirm window and you must select Always allow to don't have this error again.
* Another way to avoid this error is to open Keychain, two-fingers gesture (or right-click) over the Private Key you are using to sign, 'Get Info' option:  
  `[imagen omitida: wiki id 28522]`  
  and then go to 'Access Control', and select 'Allow all applications to access this item':  
  `[imagen omitida: wiki id 28523]`
* You can install that **.ipa** on a device, using iTunes or [iPhone Configuration Utility](https://wiki.genexus.com/commwiki/wiki?23039,,)

## [See Also](#See+Also)

[HowTo: Prototye an iOS Application on a Mac](https://wiki.genexus.com/commwiki/wiki?14761)

## [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Prototyping features and Deployment of applications for Smart Devices](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/prototyping-features-and-deployment-of-applications-for-smart-devices?p=3694)


|  |
| --- |
| **Backlinks** |
| [Category:Apple platform](https://wiki.genexus.com/commwiki/wiki?14917) | [Deployment and Prototyping in the Apple Platform](https://wiki.genexus.com/commwiki/wiki?16234) | [Development Team ID property](https://wiki.genexus.com/commwiki/wiki?30100) |
| [Executing From QR Codes](https://wiki.genexus.com/commwiki/wiki?18260) | [GeneXus Project Navigator](https://wiki.genexus.com/commwiki/wiki?14974) | [How to configure In-App Purchases in an iOS application](https://wiki.genexus.com/commwiki/wiki?20043) | [HowTo: Prepare a Mac with an Intel processor for GeneXus](https://wiki.genexus.com/commwiki/wiki?51408) |
| [Knowledge Base Navigator (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?56059) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
