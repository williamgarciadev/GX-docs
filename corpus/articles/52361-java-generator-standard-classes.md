---
title: "Java Generator Standard Classes"
source_id: 52361
source_url: https://wiki.genexus.com/commwiki/wiki?52361
genexus_version: "18"
---

# Java Generator Standard Classes

The [Java Generator](https://wiki.genexus.com/commwiki/wiki?12258) Standard Classes with their dependencies are downloaded from the internet and installed automatically when [Building](https://wiki.genexus.com/commwiki/wiki?5692) any Object. This switches to a package manager scheme that only downloads the necessary binaries via [Gradle](https://wiki.genexus.com/commwiki/wiki?52359).

Moving the Standard Classes with their dependencies to a cloud package manager provides ease and speed when it is necessary to obtain a HotFix from GeneXus or third parties, since only the Standard Classes will have to be updated and not the entire version of GeneXus.

In addition, with the properties [Standard classes specific version](https://wiki.genexus.com/commwiki/wiki?51259) and [Standard classes update policy](https://wiki.genexus.com/commwiki/wiki?51258), it is possible to specify the version of the Standard Classes that Gradle should download.

### [File names of standard class packages](#File+names+of+standard+class+packages)

The names of the \*.jar files of the Standard Classes packages contain its version. Thus, for example, if the Standard Classes version is 2.8-SNAPSHOT the package is called gxclassR-2.8-SNAPSHOT.jar

### [Availability](#Availability)

This feature is available since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066).


|  |
| --- |
| **Backlinks** |
| [Toc:Java Applications Development](https://wiki.genexus.com/commwiki/wiki?52358) |

---
