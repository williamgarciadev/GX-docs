---
title: "HowTo: Create a Provisioning Profile for Apple Development"
source_id: 17442
source_url: https://wiki.genexus.com/commwiki/wiki?17442
genexus_version: "18"
---

# HowTo: Create a Provisioning Profile for Apple Development

This document explains how to create a Provisioning Profile for developing with
[Apple](https://wiki.genexus.com/commwiki/wiki?14917) and provides a brief overview about it.

A Provisioning Profile is a collection of assets which link a group of developers, a group of devices and one or more applications. Their purpose is to enable those devices to be used for testing the application while it is being developed. A single Provisioning Profile can be defined for more than one application using wildcards (\*) in the bundle identifier definition. When working with the [Apple Push Notifications Service](https://wiki.genexus.com/commwiki/wiki?35452,,), Provisioning Profiles have to be defined for only one bundle identifier (the one associated to the [APNS SSL Certificate](https://wiki.genexus.com/commwiki/wiki?17423,,)) which means that the use of wildcards is not allowed.

The steps needed to create and install the Provisioning Profile are as follows:

### [Step 1](#Step+1)

Go to the [iOS Dev Center](http://developer.apple.com/devcenter/ios/index.action) and login with a **team agent** or **team admin** [account](http://developer.apple.com/programs/roles/index.php).

### [Step 2](#Step+2)

Go to the Certificates, Identifiers & Profiles option and open the Provisioning Profiles section.

`[imagen omitida: wiki id 17443]`

### [Step 3](#Step+3)

Select  the *New Profile* option and enter the required data:

Type of the provisioning profile  
`[imagen omitida: wiki id 17444]`

The App ID [previously created](https://wiki.genexus.com/commwiki/wiki?17423,,).  
`[imagen omitida: wiki id 22251]`

List of authorized developers (Certificates)  
`[imagen omitida: wiki id 22252]`

List of devices authorized for testing the application  
`[imagen omitida: wiki id 22253]`

Name for the profile  
`[imagen omitida: wiki id 22254]`

`[imagen omitida: wiki id 22255]`

### [Step 4](#Step+4)

Click on *Generate* and the new Provisioning Profile will be created and listed in the iOS Provisioning Portal.

`[imagen omitida: wiki id 17445]`

**Note**: Right after being created, the profile status is *In Process*. Refresh the page after a few seconds until the status is *Active*.

### [Step 5](#Step+5)

Download the new Provisioning Profile and install it in the Xcode library in the MAC computer which will be used to build the application. For this purpose, after the download, open the Profile file (mobileprovision file) using Xcode.

`[imagen omitida: wiki id 17446]`

### [Step 6](#Step+6)

Check in Xcode that the new Provisioning Profile is installed in the Xcode Library (*XCode > Preferences > Accounts > Account Details*)

`[imagen omitida: wiki id 17447]`

### [Step 7](#Step+7)

Check that it is a valid development profile by opening the file with a text editor (the file is in XML structure) and in the *<Entitlements>* element, check that for the *<aps-environment>* the string value is *<development>*

`[imagen omitida: wiki id 17449]`


|  |
| --- |
| **Backlinks** |
| [HowTo: Configure Push Notifications in Apple Applications](https://wiki.genexus.com/commwiki/wiki?17451) | [HowTo: Configure Push Notifications in Apple Applications (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54517) | [Prototyping in iOS with a compiled application](https://wiki.genexus.com/commwiki/wiki?17380) |

---
