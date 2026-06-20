---
title: "HowTo: Upload a Mini App version to the Mini App Center"
source_id: 53318
source_url: https://wiki.genexus.com/commwiki/wiki?53318
genexus_version: "18"
---

# HowTo: Upload a Mini App version to the Mini App Center

To make a new version of the Mini App available to Super App users, you have to publish a new version in the [Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290). The Mini App version will go through some intermediate stages before becoming available.

Assumptions:

* The owner of the Super App has given you access (with the role of **Mini App Developer**) to the Mini App Center, so you can publish Mini Apps for their Super App.
* The Mini App (backend services) are already deployed.
* The Mini App is already defined in the Mini App Center (see [HowTo: Create a Mini App on the Mini App Center](https://wiki.genexus.com/commwiki/wiki?53317)[)](https://wiki.genexus.com/commwiki/wiki?53317).

The **Provisioning Administrator** user and members with the **Organization Administrator** or **Mini App Developer** role can create a new [Mini App](https://wiki.genexus.com/commwiki/wiki?50900,,) version.

To access this option, go to the main menu of the Mini App Center and click on **Mini Apps**. Next, select the Mini App for which you want to upload a new version and click on the **NEW VERSION** button.

`[imagen omitida: wiki id 56182]`

The following data is required:

* **Version Code:** It is generated automatically, but you can set what you need as an internal reference. It may be useful to map it to the version specified in the GeneXus Knowledge Base for that main application.
* **Super App:** Select among available options.
* **Main Type:** Select among available options, which can be "Panel" or "Menu". It corresponds to the executable object of the mobile application.
* **Main Name:** It corresponds to the name of the executable object of the mobile application.
* **Metadata****:** It is the file with a .gxsd extension corresponding to the packaging of the application (file generated in the gxmetadata directory for each platform when "[Enable KBN](https://wiki.genexus.com/commwiki/wiki?46541)" is enabled). It is important to upload the file instead of specifying the URL.
* [**Services URL**](https://wiki.genexus.com/commwiki/wiki?21146)**:** It is the URL where the backend services of the application are deployed. It is important that the Service URL corresponds to the metadata from the previous step.
* **Super App Compatibility:** Select the compatible versions with the attached metadata version.

`[imagen omitida: wiki id 56221]`

Once confirmed, the metadata is digitally signed with the Super App private key.

The new published version will be in **Pending**status.

See the Mini App status flow below:

`[imagen omitida: wiki id 56094]`

The next step is to submit it for review.


|  |
| --- |
| **Backlinks** |
| [HowTo: Publish a Web Mini App in the Mini App Center](https://wiki.genexus.com/commwiki/wiki?57425) | [Key elements to create a Mini App](https://wiki.genexus.com/commwiki/wiki?51289) | [Toc:Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290) |
| [Submit a Mini App version for review](https://wiki.genexus.com/commwiki/wiki?53314) |

---
