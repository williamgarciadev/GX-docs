---
title: "GXflow - GAM Initialization"
source_id: 33095
source_url: https://wiki.genexus.com/commwiki/wiki?33095
genexus_version: "18"
---

# GXflow - GAM Initialization

When GXflow is integrated with [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746), it is necessary to execute an initialization process in order to create the permissions and roles, necessary for the correct operation of the gxflow runtime. When prototyping in genexus, the initialization process runs automatically, but to take it to production it may be necessary to execute the process manually.

### [How to run a manual initialization process](#How+to+run+a+manual+initialization+process)

To run a manual initialization, use the following command line:

### [.NET Framework](#.NET+Framework)

The initialization procedure is located in the \bin folder. You may run it as follows:

```
C:\Models\...\CSharpModel\web\bin\apwfinitializegam.exe
```

### [.NET Core](#.NET+Core)

The initialization procedure is located in the \bin folder. You may run it as follows:

```
C:\Models\...\NETModel\web\bin\dotnet apwfinitializegam.dll
```

### [Java](#Java)

The synchronization procedure is located in the <application>\WEB-INF\classes\com\gxflow folder. To run it, set the current working directory to "\classes" level folder and execute it as follows:

```
C:\..\<application>\WEB-INF\classes>java -cp ".\com\gxflow";.;"..\lib\*"; com.gxflow.apwfinitializegam
```

It may be necessary to include the ..\lib\joda-time-2.8.2.jar in the classpath also.

The artech.security-sql.jar file must be replaced with the corresponding one, depending on the DBMS used.

When using Java, make sure you have the connection.gam file under C:\..\<application>\WEB-INF\classes. Otherwise, these error message will be displayed:  "Error 2: Repository not found. Please contact the application administrator".

## [See Also](#See+Also)

[GXflow - GAM Integration](https://wiki.genexus.com/commwiki/wiki?18454)  
[GXflow Custom Client with GAM](https://wiki.genexus.com/commwiki/wiki?29533)  
[Business Process Deployer](https://wiki.genexus.com/commwiki/wiki?11607)


|  |
| --- |
| **Backlinks** |
| [Aspects to consider when using GeneXus BPM Suite with GAM](https://wiki.genexus.com/commwiki/wiki?43858) | [Table of contents:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [GXflow - GAM Integration](https://wiki.genexus.com/commwiki/wiki?18454) |

---
