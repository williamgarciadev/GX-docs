---
title: "GeneXus Super App News and Roadmap"
source_id: 53536
source_url: https://wiki.genexus.com/commwiki/wiki?53536
genexus_version: "18"
---

# GeneXus Super App News and Roadmap

This log shows the most important news and features for creating a Super App + Mini App solution with GeneXus platform.

Since [GeneXus 18 Upgrade 13](https://wiki.genexus.com/commwiki/wiki?59630):

* Android: Removed non-applicable Java standard methods to reduce false positives in static code analysis and updated BouncyCastle dependency.

Since [GeneXus 18 Upgrade 12](https://wiki.genexus.com/commwiki/wiki?59446):

* Android 15 (API 35) support for Super App Render and Android Mini Apps.
* Xcode 16 support for Super App Render and iOS Mini Apps.
* Complete SSO solution for [Native Mobile Mini Apps](https://wiki.genexus.com/commwiki/wiki?58298). ([SAC #60471](https://www.genexus.com/es/developers/websac?data=60471))

Since [GeneXus 18 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?54245):

* Android 14 (API 34)support for Super App Render and Android Mini Apps.
* Flex Controls in Android Mini Apps now support the Autogrow property.
* Updated libraries for the VideoOperation External Object and Interop.PlayVideo, bringing several improvements.
* Native Support for the URLdecode() function in Mini Apps and GeneXus Super Apps.
* Security enhancements for Set and SecureSet methods in ClientStorage when used in Mini Apps (Android and iOS).

Since [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244):

* Compatibility Issues
  + Mini Apps generated with this version of GeneXus or higher require the GeneXus Super App to have an equal or higher version. For non-GeneXus Super Apps, the Super App Render used must be of a version equal to or higher than the one [corresponding to this upgrade](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?58156,,). See [SAC #54203](https://www.genexus.com/es/developers/websac?data=54203) for more details.
* Run and test a Mini App with a mock Super App (with GeneXus Project Navigator). More details [here](https://wiki.genexus.com/commwiki/wiki?58219).
* The method [Provisioning.GetByFilters](https://wiki.genexus.com/commwiki/wiki?57960) (to obtain from the Mini App Center a list of Mini Apps filtered by different attributes) is now supported in a iOS non-GeneXus Native Super Apps ([SAC #54379](https://www.genexus.com/es/developers/websac?data=54178)) and GeneXus Super Apps ([SAC #54381](https://www.genexus.com/es/developers/websac?data=54178))
* For Android, several improvements in the Super App Render (for non-GeneXus Super Apps) and to the GeneXus Super App generator, particularly when the context changes between Mini App and Super App ([SAC #54096](https://www.genexus.com/es/developers/websac?data=54096)).
* Metadata Versioning in Native Applications Developed with GeneXus ([SAC #54359](https://www.genexus.com/es/developers/websac?data=54359)).
* The Mini App Center now supports multiple languages: Portuguese and Japanese have been added (in addition to English). For more details on changes made to the Mini App Center, refer to [this link](https://wiki.genexus.com/commwiki/wiki?58035).

Since [GeneXus 18 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?54243):

* SSO for Mini Apps and Android Native Super App. ([SAC #54176](https://www.genexus.com/es/developers/websac?data=54176;;)).
* Through the new GetByFilter method, it is now possible to obtain from the Mini App Center a list of Mini Apps filtered by different attributes in a Native Android Super App ([SAC #54178](https://www.genexus.com/es/developers/websac?data=54178)).
* [Mini App Center - API Reference](https://wiki.genexus.com/commwiki/wiki?57742) Documentation

Since [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242):

* The Android Super App sample (for non-GeneXus Super App) now leverages Maven Central to integrate the Super App Render SDK. More details [here](https://github.com/genexus-books/gx-super-app/blob/main/Android/GeneXus%20Libraries/README.md).
* First bits of Single Sign-On (SSO) for Mini Apps and Native Super Apps on Android, simplifying the unique authentication process for Mini Apps that share login credentials with the Super App.
* First bits of Mocking Super App in Android, facilitating the development and testing process of a Mini App independently of the Super App.
* Mini App Center API: Through this API, you can seamlessly integrate with Mini App Center functionalities. This includes creating Mini Apps, publishing new versions, submitting versions for review, and more.

Since [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241):

* Mini App Center UI improvements for Mini App version management.
* KB Samples for GeneXus Super App and their Mini Apps.
* The GeneXusSuperApp Module includes a new property to [identify a Mini App at runtime](https://www.genexus.com/es/developers/websac?data=53726;;) and a method to [obtain a specific Mini App](http://backend.sac.genexusnet.com/backend.versac.aspx?53660) from the Mini App Center through its identifier.

Since [GeneXus 18 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?54240):

* [Implement the communication API](https://wiki.genexus.com/commwiki/wiki?50906) for Super Apps developed with GeneXus.
* Support Web Mini Apps.

Up to [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853), it is possible to:

* Convert a Native Mobile application (Android or Apple) into a Super App (full-featured).
* Create a Super App with GeneXus without the API interface for [Mini Apps](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50900,,).
* Model the Mini Apps for that Super App with GeneXus 18.
* Publish Mini Apps in a [Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290) specifically deployed for each organization or sandbox environment.


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242) | [Table of contents:GeneXus Super Apps and Mini Apps](https://wiki.genexus.com/commwiki/wiki?50899) |

---
