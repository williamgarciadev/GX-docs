---
title: ".NET Generator Standard Classes - FAQ"
source_id: 51802
source_url: https://wiki.genexus.com/commwiki/wiki?51802
genexus_version: "18"
---

# .NET Generator Standard Classes - FAQ

Here are some frequently asked questions about [GeneXus .NET Generator](https://wiki.genexus.com/commwiki/wiki?38604) Standard Classes.

#### [**1. Where are Standard Classes downloaded from?**](#1.+Where+are+Standard+Classes+downloaded+from%3F)

Whenever a .NET Generator [Environment](https://wiki.genexus.com/commwiki/wiki?7115) in a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) is built for the first time, a set of standard classes are copied from the NuGet cache to the web\bin directory. This cache is populated with NuGet packages published in different cloud repositories. .NET Standard Classes in particular are published in two repositories: nuget.org and Azure packages. Both repositories are configured in the NuGet.config file in the Model directory. For example, at C:\Models\TestKB\NETSQLServer\NuGet.Config. As described in <https://docs.microsoft.com/en-us/nuget/consume-packages/configuring-nuget-behavior>, the feeds in NuGet.Config are added to the ones in user NuGet.Config.

To get the list of local caches, use this command:

```
dotnet nuget locals all --list
```

Output example:

```
http-cache: C:\Users\<user>\AppData\Local\NuGet\v3-cache
global-packages: C:\Users\<user>\.nuget\packages\
temp: C:\Users\<user>\AppData\Local\Temp\NuGetScratch
```

To clear all the NuGet package caches (the three directories in the previous example), use the following command:

```
dotnet nuget locals all --clear
```

**2. How can the version of the Standard Classes of a generated application be found?**

The version used is specified in the file Directory.build.props located in the model directory; for example, C:\Models\TestKB\NETSQLServer\Directory.Build.Props and it is the same as the value of the [Standard classes specific version property](https://wiki.genexus.com/commwiki/wiki?51259).  [Directory.build.props](https://learn.microsoft.com/en-us/visualstudio/msbuild/customize-your-build?view=vs-2022) is a known mechanism to customize the build process; for example, by defining global properties for projects (\*.csproj) in any subfolder.

**3. Build Error: NU1102: Unable to find package GeneXus.Classes.Web.Core with version (= 1.28.5)**

When an invalid version (1.28.5 in the example error) is specified in the [Standard classes specific version property](https://wiki.genexus.com/commwiki/wiki?51259), this error is printed in the build output. In that case, change the version property to a valid number. The list of available version numbers can be obtained as described in [Standard classes specific version property](https://wiki.genexus.com/commwiki/wiki?51259) or browsing [GeneXus.Classes.Core](https://www.nuget.org/packages/GeneXus.Classes.Core#versions-body-tab) package versions.

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?49972,,).

### [See Also](#See+Also)

[Deploy to GeneXus Prototyping Cloud: under the hood (FAQs)](https://wiki.genexus.com/commwiki/wiki?18292)


|  |
| --- |
| **Backlinks** |
| [Toc:.NET Applications Development](https://wiki.genexus.com/commwiki/wiki?53971) | [.NET Generator Standard Classes](https://wiki.genexus.com/commwiki/wiki?51442) | [Offline scenario of the .NET Generator](https://wiki.genexus.com/commwiki/wiki?53793) |

---
