---
title: "Knowledge Base Navigator (GeneXus 18 Upgrade 5 or prior)"
source_id: 56059
source_url: https://wiki.genexus.com/commwiki/wiki?56059
genexus_version: "18"
---

# Knowledge Base Navigator (GeneXus 18 Upgrade 5 or prior)

The GeneXus Knowledge Base Navigator (KBN) is an iOS native application that allows GeneXus users to prototype the [iOS online applications](https://wiki.genexus.com/commwiki/wiki?14981) they create using GeneXus. It allows exploring the functionalities that a GeneXus [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) application exposes: Entities and Relationships.

### [Download](#Download)

You can [download the KBN](https://apps.apple.com/app/id1144118177) from the Apple Store.

### [Known limitations](#Known+limitations)

To prototype an application that uses any of the following features, [a compiled application is required](https://wiki.genexus.com/commwiki/wiki?17380).

#### [Offline generated code](#Offline+generated+code)

[Offline applications](https://wiki.genexus.com/commwiki/wiki?22221) cannot be prototyped with the KBN. This tool only supports interpreted metadata.

Calling offline objects (that is, objects with the [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911) set to Offline) is not supported either.

#### [User Controls and External Objects](#User+Controls+and+External+Objects)

Custom User Controls (or the standard AnimationView User Control) and External Objects are not supported in the KBN; only those provided natively by GeneXus can be used.

#### [Notifications](#Notifications)

Push notifications will not work when prototyping in the KBN.

#### [Resources](#Resources)

Embedded resources will not work when prototyping in the KBN. That includes:

* Embedded fonts; a default Helvetica font will be used instead;
* Images with varying resolutions are not supported;
* Other embedded resources will not work either; for example, custom Lottie animations.

### [See Also](#See+Also)

* [iOS Applications Wireless Prototyping](https://wiki.genexus.com/commwiki/wiki?15576)
* [Prototyping in iOS with a compiled application](https://wiki.genexus.com/commwiki/wiki?17380)
* [Execution for Android Using the Device](https://wiki.genexus.com/commwiki/wiki?14910)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Prototyping features and Deployment of applications for Smart Devices](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/prototyping-features-and-deployment-of-applications-for-smart-devices?p=3694)
