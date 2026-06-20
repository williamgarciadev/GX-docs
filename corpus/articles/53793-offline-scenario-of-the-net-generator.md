---
title: "Offline scenario of the .NET Generator"
source_id: 53793
source_url: https://wiki.genexus.com/commwiki/wiki?53793
genexus_version: "18"
---

# Offline scenario of the .NET Generator

Before starting to set the offline environment for the generator, check [SAC #60943](https://www.genexus.com/en/developers/websac?data=60943;;).

It is not possible to use the .NET Generator without internet access because the third-party dependencies and those of the application are downloaded at compilation time.

So, the packages that have to be downloaded in the offline scenario for the .NET Generator to work are as follows:

●    Standard Class packages, direct dependencies of the generated application, which are published in Azure and nuget.org. (More information: [GeneXus Standard Classes](https://wiki.genexus.com/commwiki/wiki?18859))   
●    Third-party packages, which are dependencies of the Standard Classes, published on nuget.org. (More information: [External utilities used by GeneXus-generated web applications](https://wiki.genexus.com/commwiki/wiki?15671))

To achieve this, it is necessary to use an [MSBuild Tasks](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?3908,,) called GoOfflineNetGenerator, which is located at <GeneXusHome>\GXDevTools.msbuild.

GoOfflineNetGenerator downloads the packages required by the .NET Generator to a local directory (by default this will be in the NuGet cache) so that you can then generate and compile KBs even with no internet connection.

The GoOfflineNetGenerator parameters are as follows:

*PackagesDirectory*  
     It’s an optional parameter that indicates the directory where the packages are going to be downloaded. The default value is <user>\.nuget\package.

*GenStdVersion*  
     Optional parameter that indicates the version of the Standard Classes to download. By default, it downloads those Defined by Generator (from the installed generator).

**Notes:**  
●    To use the GoOfflineNetGenerator task, the machine must be connected to the internet.   
●    You only need to run it once to be able to work offline.

### [(\*) List or clear the cache](#%28*%29+List+or+clear+the+cache)

To get the list of local caches, use this command:

```
dotnet nuget locals all --list
```

Example output:

```
http-cache: C:\Users\<user>\AppData\Local\NuGet\v3-cache
global-packages: C:\Users\<user>\.nuget\packages\
temp: C:\Users\<user>\AppData\Local\Temp\NuGetScratch
```

To clear all the NuGet package caches (the three directories in the previous example), use the following command:

```
dotnet nuget locals all --clear
```

## [Samples](#Samples+)

The samples shown below are executed by command lines.

### [Sample # 1](#Sample+%23+1)

Download all dependencies to the NuGet cache.

```
C:\Program Files\GeneXus>msbuild GXDevTools.msbuild /t:GoOfflineNetGenerator
```

The above line downloads all the packages used by the .NET Generator to the default NuGet cache directory (<user>\.nuget\packages).

### [Sample # 2](#Sample+%23+2)

Download all dependencies to a particular directory and then use it in another KB.

```
C:\Program Files\GeneXus>msbuild GXDevTools.msbuild /t:GoOfflineNetGenerator /p:PackagesDirectory="C:\GeneXus\NetOfflinePackages"
```

Download all the packages used by the .NET Generator to the directory C:\GeneXus\NetOfflinePackages.

●      To use that package source offline from a particular KB, the following value can be added to the KB generator in [MSBuild options property](https://wiki.genexus.com/commwiki/wiki?44168)*,*

```
--source "C:\GeneXus\NetOfflinePackages"
```

●      To use that package source from any KB on the machine, you can modify the user's NuGet.Config in this way:

```
dotnet nuget add source C:\GeneXus\NetOfflinePackages  --name NetGeneratorOfflinePackages
```

### [Sample # 3](#Sample+%23+3)

Download all the dependencies to a separate directory but for the Standard Classes Specific Version = 1.17.1

```
C:\Program Files\GeneXus>msbuild GXDevTools.msbuild /t:GoOfflineNetGenerator /p:PackagesDirectory="C:\GeneXus\NetOfflinePackages" /p:GenStdVersion=1.17.1
```

The list of available version numbers can be obtained as described in [Standard classes specific version property](https://wiki.genexus.com/commwiki/wiki?51259) or browsing [GeneXus.Classes.Core](https://www.nuget.org/packages/GeneXus.Classes.Core#versions-body-tab) package versions.

By disconnecting your machine from the internet, you can check that the packages were downloaded and the KB compiles correctly.

## [Availability](#Availability)

Since [GeneXus 17 Upgrade 11](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49972,,).

## [See Also](#See+Also)

[GeneXus Standard Classes](https://wiki.genexus.com/commwiki/wiki?18859)  
[.NET Generator Standard Classes - FAQ](https://wiki.genexus.com/commwiki/wiki?51802)


|  |
| --- |
| **Backlinks** |
| [Table of contents:.NET Applications Development](https://wiki.genexus.com/commwiki/wiki?53971) | [.NET Generator Standard Classes](https://wiki.genexus.com/commwiki/wiki?51442) |

---
