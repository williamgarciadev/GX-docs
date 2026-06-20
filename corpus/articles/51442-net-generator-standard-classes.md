---
title: ".NET Generator Standard Classes"
source_id: 51442
source_url: https://wiki.genexus.com/commwiki/wiki?51442
genexus_version: "18"
---

# .NET Generator Standard Classes

The [.NET Generator](https://wiki.genexus.com/commwiki/wiki?38604) [Standard Classes](https://wiki.genexus.com/commwiki/wiki?18859) in an executable format (.dll or .exe) are downloaded from the internet and installed automatically when [building](https://wiki.genexus.com/commwiki/wiki?5692) any Object. In this way, a package manager mechanism is used to download the binaries via [NuGet](https://docs.microsoft.com/en-us/nuget/what-is-nuget).

The NuGet package manager does not necessarily access the internet every time you run a Build. The reason is that NuGet has a cache (located by default in <user>\.nuget\package), where packages are downloaded. If the cache is cleared (\*), the packages are downloaded again when you do the Build.

Moving Standard Classes and their dependencies to a cloud package manager, convenience and speed is provided when obtaining HotFixes from GeneXus or third parties (for example, Log4Net update). This is because only the Standard Classes need to be updated, not the entire software version.

The specific version of the Standard Classes can be specified through the [Standard classes specific version property](https://wiki.genexus.com/commwiki/wiki?51259), and the automatic update of HotFixes can be configured through the  [Standard classes update policy property](https://wiki.genexus.com/commwiki/wiki?51258).

## [Compatibility Aspects](#Compatibility+Aspects)

The compatibility of the generated code is guaranteed. However, you should consider the [offline scenario](https://wiki.genexus.com/commwiki/wiki?53793).

## [Availability](#Availability)

Since [GeneXus 17 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?49972,,).

## [See Also](#See+Also)

[GeneXus Standard Classes](https://wiki.genexus.com/commwiki/wiki?18859)  
[.NET Generator Standard Classes - FAQ](https://wiki.genexus.com/commwiki/wiki?51802)


|  |
| --- |
| **Backlinks** |
| [Toc:.NET Applications Development](https://wiki.genexus.com/commwiki/wiki?53971) | [Cloud-native with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51572) |
| [GeneXus Standard Classes](https://wiki.genexus.com/commwiki/wiki?18859) |

---
