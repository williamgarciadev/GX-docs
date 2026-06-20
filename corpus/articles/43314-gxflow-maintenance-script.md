---
title: "GXflow Maintenance Script"
source_id: 43314
source_url: https://wiki.genexus.com/commwiki/wiki?43314
genexus_version: "18"
---

# GXflow Maintenance Script

The purpose of the *Maintenance Script* is to clean records that can accumulate by millions and that over time cease to be relevant. This script cleans these records from the WFSessions table that stores the user sessions.

The way to run the maintenance program is as follows:

* **NET**

Execute the file apwfmaintenance.exe from a command line (Start - Run - cmd), for example:

```
C:\Models\<KB>\CSharpModel\Web\bin> apwfmaintenance.exe
```

* **Netcore**

Execute the file apwfmaintenance.dll from a command line (Start - Run - cmd), for example:

```
C:\Models\<KB>\NetcoreModel\Web\bin>dotnet apwfmaintenance.dll
```

* **Java**

Execute the following command from a command line (Start - Run - cmd):

```
java -cp "classpath" com.gxflow.apwfmaintenance
```

Example:

```
..\<application>\WEB-INF\classes>java -cp "..\com\gxflow";.;"..\lib\*"; com.gxflow.apwfmaintenance
```

### [Important:](#Important%3A)

The program should be executed on a daily basis, on moments of lower activity.

It is recommended to run the program automatically using a Task Scheduler.

### [Availability](#Availability)

This feature is available since  [GeneXus 16 upgrade 4](https://wiki.genexus.com/commwiki/wiki?42755,,).

## [See Also](#See+Also)

* [GXflow Performance Tips](https://wiki.genexus.com/commwiki/wiki?29277)


|  |
| --- |
| **Backlinks** |
| [GXflow Performance Tips](https://wiki.genexus.com/commwiki/wiki?29277) |

---
