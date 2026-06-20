---
title: "Standard classes specific version property"
source_id: 51259
source_url: https://wiki.genexus.com/commwiki/wiki?51259
genexus_version: "18"
---

# Standard classes specific version property

Specifies the version of standard classes referenced by the generated application.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

.NET

The format must follow the [SemVer 2.0](https://semver.org/) specification of MAJOR.MINOR.PATCH plus the [specific notations supported by NuGet](https://docs.microsoft.com/en-us/nuget/concepts/package-versioning#version-ranges) that allow setting version ranges.

To see the available values, browser [GeneXus.Classes.Core](https://www.nuget.org/packages/GeneXus.Classes.Core#versions-body-tab) package versions or run the following command in a .NET model:

```
C:\Models\TestKnowledgeBase\NetCoreModel>nuget list GeneXus.Classes.Core -PreRelease -AllVersions
```

It will print a list of the versions of standard classes published on NuGet.org and Azure (both feeds are specified in NuGet.Config in .Net Core Model).

The printed list will look as follows:

```
GeneXus.Classes.Core 1.14.3
GeneXus.Classes.Core 1.14.2
GeneXus.Classes.Core 1.14.1
GeneXus.Classes.Core 1.14.0
GeneXus.Classes.Core 1.13.8
GeneXus.Classes.Core 1.13.7
GeneXus.Classes.Core 1.13.6
GeneXus.Classes.Core 1.13.5
GeneXus.Classes.Core 1.13.2
GeneXus.Classes.Core 1.13.1
GeneXus.Classes.Core 1.12.19
GeneXus.Classes.Core 1.12.18
GeneXus.Classes.Core 1.12.17
GeneXus.Classes.Core 1.12.10
GeneXus.Classes.Core 1.12.9
GeneXus.Classes.Core 1.12.8
GeneXus.Classes.Core 1.12.7
GeneXus.Classes.Core 1.12.5
GeneXus.Classes.Core 1.12.4
GeneXus.Classes.Core 1.12.1

.....

GeneXus.Classes.Core 101.14.0-trunk.20220519165945
GeneXus.Classes.Core 101.14.0-trunk.20220519141423
GeneXus.Classes.Core 101.14.0-trunk.20220518112620
....

GeneXus.Classes.Core 1.18.0-stable.20220517131004
GeneXus.Classes.Core 1.18.0-stable.20220516170539
GeneXus.Classes.Core 1.18.0-stable.20220513140654
```

All versions ending with "-stable" correspond to the GeneXus preview channel.

Those with "-trunk" correspond to the GeneXus Beta channel.

The rest of the versions correspond to Upgrade versions. The mapping between Standard Classes Versions and GeneXus upgrades can be found at [DotNetClasses Releases](https://github.com/genexuslabs/DotNetClasses/releases).

### [Samples](#Samples)

.NET

[1.19.0**-trunk**.20220628194351]  Refers to a specific version of Standard Classes on a GeneXus Preview.

[1.17.0] Is the version number for [GeneXus 17 Upgrade 9](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49956,,).

[1.17.1] Is the version number for GeneXus 17 Upgrade 9 HotFix 1.

1.17.\* Gets the highest HotFix of GeneXus 17 Upgrade 9.

Java

[102.8**-trunk**.20221007195012-SNAPSHOT] Refers to a specific version of Standard Classes on a GeneXus Preview.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

[Standard classes update policy property](https://wiki.genexus.com/commwiki/wiki?51258)

[Flexible client update policy property](https://wiki.genexus.com/commwiki/wiki?55890)

[Flexible client version property](https://wiki.genexus.com/commwiki/wiki?55856)


|  |
| --- |
| **Backlinks** |
| [.NET Generator Standard Classes](https://wiki.genexus.com/commwiki/wiki?51442) | [.NET Generator Standard Classes - FAQ](https://wiki.genexus.com/commwiki/wiki?51802) | [.NET Package Version property](https://wiki.genexus.com/commwiki/wiki?51648) |
| [Flexible client update policy property](https://wiki.genexus.com/commwiki/wiki?55890) | [Flexible client version property](https://wiki.genexus.com/commwiki/wiki?55856) | [Flexible client version property (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60725) |
| [Java Artifact Version property](https://wiki.genexus.com/commwiki/wiki?53866) | [Java Generator Standard Classes](https://wiki.genexus.com/commwiki/wiki?52361) | [Offline scenario of the .NET Generator](https://wiki.genexus.com/commwiki/wiki?53793) | [Standard classes update policy property](https://wiki.genexus.com/commwiki/wiki?51258) |

---
