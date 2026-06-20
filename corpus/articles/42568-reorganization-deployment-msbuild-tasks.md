---
title: "Reorganization Deployment MSBuild Tasks"
source_id: 42568
source_url: https://wiki.genexus.com/commwiki/wiki?42568
genexus_version: "18"
---

# Reorganization Deployment MSBuild Tasks

You can do the [Export Reorganization](https://wiki.genexus.com/commwiki/wiki?34476) using MSBuild tasks   
This document tells you the syntax to use via command line, depending on the generator you are using.

The script to run is a file called **deploy****.****msbuild** and it's located at the root of your GeneXus installation (<Genexus Dir>)

The basic call has the following structure:

```
> MSBuild.exe "<GeneXus dir>\deploy.msbuild" /p:GX_PROGRAM_DIR=<GeneXus dir> /p:Generator=<Generator> /p:<DBMS>="true" /p:SourcePath=<Environment Dir> /p:ReorgDestination=<Destination Dir> /p:FileName=<Zipped reorg file> /t:ExportReorganization
```

### [Parameters](#Parameters)

GX\_PROGRAM\_DIR: This should be the path to your GeneXus installation

Generator: It can be "Java", "C#" or ".NET Core"

DBMS: The DBMS where the reorganization must run. Allowed values are: SQLServer, MySQL, PostgreSQL, Oracle

SourcePath: Absolut path to the environment directory (without the web directory)

ReorgDestination: Absolut path where the export will be placed.

FileName: Name of the file with the exported reorganization.

The Java generator requires some additional properties

JDBCDrivers: The type of driver as set in the Data Store property JDBC Driver/

PackageName: The package name set in the Generator property Java package name.

JavaPath: Absolut path to the Java JDK.

TargetJRE: The runtime version where the exported reorganization will run.

IncludeCFG: Include the reorg.cfg at the JAR of the reorganization.

## [Examples](#Examples)

```
C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe /nologo /verbosity:detailed /ToolsVersion:4.0 "C:\Development\Trunk3\Deploy\GeneXus\Debug\deploy.msbuild" /p:GX_PROGRAM_DIR="C:\Development\Trunk3\Deploy\GeneXus\Debug" /p:Generator=Java /p:SQLServer="true" /p:SourcePath="C:\models\Testdeploy3\JavaSQLServer003" /p:ReorgDestination="c:\temp\Reorgs" /p:FileName=myreorg.jar /p:JDBCDrivers="Microsoft JDBC Driver (Type 4)" /p:JavaPath="C:\Program Files\Java\jdk-15.0.2\bin" /p:TargetJRE="15" /p:PackageName="com.testdeploy3" /t:ExportReorganization

C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe /nologo /verbosity:detailed /ToolsVersion:4.0 "C:\Development\Trunk3\Deploy\GeneXus\Debug\deploy.msbuild" /p:GX_PROGRAM_DIR="C:\Development\Trunk3\Deploy\GeneXus\Debug" /p:Generator=Java /p:SQLServer="true" /p:SourcePath="C:\models\Testdeploy3\JavaSQLServer003" /p:ReorgDestination="c:\temp\Reorgs" /p:FileName=myreorg.jar /p:JDBCDrivers="Microsoft JDBC Driver (Type 4)" /p:JavaPath="C:\Program Files\Java\jdk-15.0.2\bin" /p:TargetJRE="15" /p:PackageName="com.testdeploy3" /p:IncludeCFG="true" /t:ExportReorganization
```

## [See Also](#See+Also)

* [Export Reorganization](https://wiki.genexus.com/commwiki/wiki?34476)
* [Application Deployment MSBuild tasks](https://wiki.genexus.com/commwiki/wiki?42073)


|  |
| --- |
| **Backlinks** |
| [Export Reorganization](https://wiki.genexus.com/commwiki/wiki?34476) |

---
