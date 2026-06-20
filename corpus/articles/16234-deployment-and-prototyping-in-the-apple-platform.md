---
title: "Deployment and Prototyping in the Apple Platform"
source_id: 16234
source_url: https://wiki.genexus.com/commwiki/wiki?16234
genexus_version: "18"
---

# Deployment and Prototyping in the Apple Platform

Applications can be distributed in two ways:

* App Store
* Enterprise Distribution

### App Store

It is used to distribute public applications through the Apple market (App Store), regardless of whether they are free or paid.

In this case, an iOS Developer Program license is required: <http://developer.apple.com/programs/ios/>.

[Here](https://wiki.genexus.com/commwiki/wiki?18958) you will find a complete guide to publish and distribute an application by the App Store.

### [Enterprise Distribution](#Enterprise+Distribution)

The second option is for internal distribution within a company, for instance, to distribute an application among the employees of the Sales department.

In this case, an iOS Enterprise Program license is required: <http://developer.apple.com/programs/ios/enterprise/>.

For both distribution methods, applications should be compiled with the SDK that is only available for the operating system in Mac OS.

Check the App Distribution Guide for more information.

<https://developer.apple.com/library/prerelease/ios/documentation/IDEs/Conceptual/AppDistributionGuide/DistributingEnterpriseProgramApps/DistributingEnterpriseProgramApps.html>

##### [OTA (Over The Air) distribution](#OTA+%28Over+The+Air%29+distribution)

To support "Over The Air" distribution, notice that when using the "Save for Enterprise Distribution" option; an .ipa file and a manifest (plist) file are generated.  
Upload both files to the same directory on your web server. You need to link to the plist file that was just created, using the following format link:

```
itms-services://?action=download-manifest&url=http://example.com/Application.plist
```

When using iOS 7, make sure to use https to point to the manifest (.plist) file.

[Distribute apps to your users](http://www.apple.com/business/accelerator/deploy/app-distribution.html)

### [iOS Prototyping](#iOS+Prototyping)

There are two options to prototype in iOS:

* [GeneXus Project Navigator](https://wiki.genexus.com/commwiki/wiki?14974)
* [Prototyping in iOS with a compiled application](https://wiki.genexus.com/commwiki/wiki?17380)

[Spanish Version](https://wiki.genexus.com/commwiki/wiki?16075,,)

### [See Also](#See+Also)

[Distributing Your Application In-House](https://developer.apple.com/library/prerelease/ios/documentation/IDEs/Conceptual/AppDistributionGuide/DistributingEnterpriseProgramApps/DistributingEnterpriseProgramApps.html)  
[Install in-house apps wirelessly](https://help.apple.com/deployment/ios/#/apda0e3426d7)


|  |
| --- |
| **Backlinks** |
| [Category:Apple platform](https://wiki.genexus.com/commwiki/wiki?14917) | [Apple Requirements](https://wiki.genexus.com/commwiki/wiki?19478) | [Distribution Method property](https://wiki.genexus.com/commwiki/wiki?50713) |
| [Enable KBN property](https://wiki.genexus.com/commwiki/wiki?46541) | [iOS Applications Wireless Prototyping](https://wiki.genexus.com/commwiki/wiki?15576) |

---
