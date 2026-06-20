---
title: "GeneXus Standard Classes"
source_id: 18859
source_url: https://wiki.genexus.com/commwiki/wiki?18859
genexus_version: "18"
---

# GeneXus Standard Classes

The GeneXus Standard Classes are a set of routines, written in native code, that are referenced by the generated code. As an example, the code to send an e-mail is not generated in every object that sends e-mails. It is "packed" as part of the Standard Classes and referenced by the generated code.

Every GeneXus Generator has its set of Standard Classes.

### [Distribution](#Distribution)

The Standard Classes are distributed on every GeneXus version and are automatically installed.

**Note**: The Standard Classes for the .NET and Java Generators are installed when you make a build of the application.

### [Source code](#Source+code)

Standard Classes source code is \_not\_ distributed with GeneXus for many generators (see below). .NET Framework and .NET Standard Classes can be reached from <https://github.com/genexuslabs/DotNetClasses> and Java standard classes from <https://github.com/genexuslabs/JavaClasses>

#### [How to compile:](#How+to+compile%3A)

* Java  
  Refer to <https://github.com/genexuslabs/JavaClasses#how-to-compile>
* .NET Framework  
  Refer to <https://github.com/genexuslabs/DotNetClasses#how-to-build>
* .NET  
  Refer to <https://github.com/genexuslabs/DotNetClasses#how-to-build>

#### [Branches:](#Branches%3A)

* .NET Framework and .NET
  + <https://github.com/genexuslabs/DotNetClasses/tree/beta> corresponds to [GeneXus Beta Channel](https://wiki.genexus.com/commwiki/wiki?40580,,)
  + <https://github.com/genexuslabs/DotNetClasses/tree/master> corresponds to [GeneXus Preview Channel](https://wiki.genexus.com/commwiki/wiki?28877,,)
* Java
  + <https://github.com/genexuslabs/JavaClasses/tree/beta> corresponds to [GeneXus Beta Channel](https://wiki.genexus.com/commwiki/wiki?40580,,)
  + <https://github.com/genexuslabs/JavaClasses/tree/master> corresponds to [GeneXus Preview Channel](https://wiki.genexus.com/commwiki/wiki?28877,,)

Releases for each [GeneXus release](https://wiki.genexus.com/commwiki/wiki?28878,,):

* <https://github.com/genexuslabs/JavaClasses/releases>
* <https://github.com/genexuslabs/DotNetClasses/releases>

### [License](#License)

You can download (if required), change and redistribute the Standard Classes source code. For details see:

* <https://github.com/genexuslabs/DotNetClasses#license>
* <https://github.com/genexuslabs/JavaClasses#license>

### [Packaging](#Packaging)

Depending on the generator, those routines are packaged differently.

#### [Java](#Java)

Refer to <https://github.com/genexuslabs/JavaClasses#modules>.

#### [.NET Framework](#.NET+Framework)

Refer to <https://github.com/genexuslabs/DotNetClasses#modules>.  
The already packaged routines are located on the <GeneXus Installation>\gxnet folders as gx\*.dll.

#### [.NET](#.NET)

Refer to <https://github.com/genexuslabs/DotNetClasses#modules>.

More information:  [.NET Generator Standard Classes](https://wiki.genexus.com/commwiki/wiki?51442)

#### [iSeries Native](#iSeries+Native)

In order to execute any iSeries (Cobol|RPG) program, you need to install the [GeneXus iSeries Library](https://www.genexus.com/developers/downloadcenter?data=3047); the standard GeneXus routines used by the GeneXus Cobol and RPG programs.

#### [Android](#Android)

The GeneXus Standard Classes for Android together with what we call the Android FlexibleClient (which is a set of Android libraries) are packaged in binary format in a Maven Repository inside the GeneXus installation directory (in Android/m2Repository).

#### [iOS](#iOS)

The *GXFlexibleClient* framework is the iOS GeneXus Standard Classes deployed as a framework that is referenced in your Xcode project. You will notice it is copied and installed in the Mac computer during the compilation process.

### [See Also](#See+Also)

[Cobol requirements](https://wiki.genexus.com/commwiki/wiki?14124)  
[RPG requirements](https://wiki.genexus.com/commwiki/wiki?14095)  
[External utilities used by GeneXus generated applications](https://wiki.genexus.com/commwiki/wiki?25151)  
[iOS FAQ](https://wiki.genexus.com/commwiki/wiki?14925,,)


|  |
| --- |
| **Backlinks** |
| [Toc:.NET Applications Development](https://wiki.genexus.com/commwiki/wiki?53971) | [.NET Generator Standard Classes](https://wiki.genexus.com/commwiki/wiki?51442) | [A06:2021 - Vulnerable and outdated components](https://wiki.genexus.com/commwiki/wiki?50186) |
| [Calling a GeneXus generated program from other Environments](https://wiki.genexus.com/commwiki/wiki?21387) | [Comparing the .NET generator with the .NET Framework generator](https://wiki.genexus.com/commwiki/wiki?45778) | [Connection pooling and Datasource definitions](https://wiki.genexus.com/commwiki/wiki?18717) | [External Object: Java Session Bean](https://wiki.genexus.com/commwiki/wiki?6197) |
| [HowTo: Compile Android's FlexibleClient](https://wiki.genexus.com/commwiki/wiki?29656) | [Toc:Java Applications Development](https://wiki.genexus.com/commwiki/wiki?52358) |
| [Offline scenario of the .NET Generator](https://wiki.genexus.com/commwiki/wiki?53793) | [SRC Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?38589) | [Support for Jakarta EE and Java EE](https://wiki.genexus.com/commwiki/wiki?48018) |
|

---
