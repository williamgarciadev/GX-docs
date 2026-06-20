---
title: "Online Native Mobile applications architecture"
source_id: 14981
source_url: https://wiki.genexus.com/commwiki/wiki?14981
genexus_version: "18"
---

# Online Native Mobile applications architecture

Native Mobile applications installed on devices read Metadata in order to consume [REST Web Services](https://wiki.genexus.com/commwiki/wiki?14573) and generate the forms in the device. These applications create a UI that is also based on Resources, in addition to Metadata.

Basically, Resources contain the images that will be used by the application and are hosted in the application server; in turn, Metadata, which is contained in JSON files, has information related mainly to Patterns and Objects. For example, if the application uses Patterns, there will be Metadata containing the knowledge about those Patterns, such as menus, visual structures, behavior (given, for instance, by actions), and so on. The same happens with objects.

`[imagen omitida: wiki id 14996]`

**Running under Knowledge Base Navigator ([KBN](https://wiki.genexus.com/commwiki/wiki?14974)) control  (image above)**

The data required by the application residing in the device will be obtained by consuming REST services, which will access the user’s DB and return the requested information to the application. Note that this is different from what was said about Resources and Metadata, which are accessed as a simple GET via HTTP / HTTPS.

When the application is installed on the device (without [KBN](https://wiki.genexus.com/commwiki/wiki?18653) control), it doesn't need to access the server to obtain the metadata and resources which are compiled in the program.

`[imagen omitida: wiki id 15675]`

**Running directly from devices without the [KBN](https://wiki.genexus.com/commwiki/wiki?14974) control (image above)**

### [See Also](#See+Also)

[Offline Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?22221) (since GeneXus X Evolution 3)


|  |
| --- |
| **Backlinks** |
| [Android - FAQ and Common Issues](https://wiki.genexus.com/commwiki/wiki?14575) | [GAM - Native Mobile Authentication](https://wiki.genexus.com/commwiki/wiki?15222) | [GAM architecture for Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?14978) |
| [Getting Started with tvOS](https://wiki.genexus.com/commwiki/wiki?40787) | [Getting Started with watchOS](https://wiki.genexus.com/commwiki/wiki?40786) | [HowTo: Version Your Native Mobile Application](https://wiki.genexus.com/commwiki/wiki?17223) | [Knowledge Base Navigator (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?56059) |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |
| [Native Mobile Versioning Details](https://wiki.genexus.com/commwiki/wiki?19531) | [Offline Native Mobile Applications Generation](https://wiki.genexus.com/commwiki/wiki?22262) | [Permissions Over a User Action in SD Objects](https://wiki.genexus.com/commwiki/wiki?18173) | [Runtime external object](https://wiki.genexus.com/commwiki/wiki?33076) |
| [Services URL property](https://wiki.genexus.com/commwiki/wiki?21146) | [Tabs offered in Panel and Work With objects](https://wiki.genexus.com/commwiki/wiki?16847) |
|

---
