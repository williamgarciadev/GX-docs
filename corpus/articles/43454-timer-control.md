---
title: "Timer Control"
source_id: 43454
source_url: https://wiki.genexus.com/commwiki/wiki?43454
genexus_version: "18"
---

# Timer Control

The purpose of the **Timer Control**is to trigger Timer Events (see [Timer Intermediate Event](https://wiki.genexus.com/commwiki/wiki?12194) and [Timer Start Event in BPD](https://wiki.genexus.com/commwiki/wiki?43449)). If you don`t execute it, the Timer Events won't be triggered.

The *Timer Scheduler* is also used for this purpose but it executes once every certain amount of time as explained below.

So, to reflect the changes made with the Timer Events, the **Timer Control** must run to check when the Timer Events must take place. To execute it, you must do the following:

* ### [**NET**](#NET)

Execute the file apwftimerscheduler.exe from a command line (Start - Run - cmd), specifying the time (time unit: seconds) between runs, for example:

```
C:\Models\<KB>\CSharpModel\Web\bin> apwftimerscheduler.exe 60
```

Or you can execute from the directory (<KB>\CSharpModel\Web\bin) the apwftimercontrol.exe that executes once.

```
C:\Models\<KB>\CSharpModel\Web\bin> apwftimercontrol.exe
```

* ### [**NET Core**](#NET+Core)

Execute the file apwftimerscheduler.dll from a command line (Start - Run - cmd), specifying the time (time unit: seconds) between runs, for example:

```
C:\Models\<KB>\NetModel\Web\bin>dotnet apwftimerscheduler.dll 60
```

Or you can execute from the directory (<KB>\CSharpModel\Web\bin) the apwftimercontrol.dll that executes once.

```
C:\Models\<KB>\NetModel\Web\bin>dotnet apwftimercontrol.dll
```

* ### [**Java**](#Java)

Execute the following command from a command line (Start - Run - cmd), specifying the time (time unit: seconds) between runs:

```
java -cp "classpath" com.gxflow.apwftimerscheduler 60
```

Or as follows to execute it just once:

```
java -cp "classpath" com.gxflow.apwftimercontrol
```

Example:

```
..\<application>\WEB-INF\classes>java -cp ".\com\gxflow";.;"..\lib\*"; com.gxflow.apwftimerscheduler 60
```

* ### [**Linux**](#Linux)

```
<application>/WEB-INF/classes$ java -classpath ./com/gxflow:"../lib/*": com.gxflow.apwftimerscheduler 60
```

## Note

In case that GAM is enabled in the KB, consider the following:

The location.gam and the application.gam files have to be located in the directory where the command is executed - in this example, in the "classes" directory.

## Scheduling on production environments

Note that *apwftimerscheduler* calls once every certain amount of time the *apwftimercontrol* which actually checks for the deadlines and executes the corresponding events.  
The *apwftimerscheduler* is especially useful when prototyping, but in production environments, the *apwftimercontrol* one recommended to be used. It's highly recommended to run the *apwftimercontrol* using a task scheduler and not the *apwftimerscheduler*.

For more information about how to schedule a task please see:

* [How To Schedule Tasks in Windows XP](http://support.microsoft.com/kb/308569)
* [Schedule a task](http://windows.microsoft.com/en-au/windows7/schedule-a-task) (for Windows 7)
* [Scheduling with Linux](http://www.ibm.com/developerworks/library/l-job-scheduling/index.html)

## Availability

The Timer Control is available since [GeneXus 16 upgrade 4](https://wiki.genexus.com/commwiki/wiki?42755,,).

## [See Also](#See+Also)

[Timer Start Event in BPD](https://wiki.genexus.com/commwiki/wiki?43449)  
[Timer Intermediate Event in BPD](https://wiki.genexus.com/commwiki/wiki?12194)


|  |
| --- |
| **Backlinks** |
| [Deadline Checker](https://wiki.genexus.com/commwiki/wiki?23379) | [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [How the Workflow engine evaluates Timers](https://wiki.genexus.com/commwiki/wiki?49293) |
| [Timer expression type property](https://wiki.genexus.com/commwiki/wiki?47341) | [Timer Intermediate Event in BPD](https://wiki.genexus.com/commwiki/wiki?12194) | [Timer Start Event in BPD](https://wiki.genexus.com/commwiki/wiki?43449) |

---
