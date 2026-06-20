---
title: "Deadline Checker"
source_id: 23379
source_url: https://wiki.genexus.com/commwiki/wiki?23379
genexus_version: "18"
---

# Deadline Checker

**Deprecated**: Since [GeneXus 16 upgrade 4](https://wiki.genexus.com/commwiki/wiki?42755,,). Replaced by [Timer Control](https://wiki.genexus.com/commwiki/wiki?43454).

The purpose of the *Deadline Checker* is to control the timestamp of Deadlines (GeneXus versions 9.0 or earlier) or Timers (GeneXus X version or later).  
The *Deadline Scheduler* is also used for this purpose but it executes once every certain amount of time as explained below.

So in order to reflect the changes made with the Timer Intermediate Events, the *Deadline Checker* must run to check when the timer events must take place (check if the deadlines have been met). To execute it you must do the following:

* **NET**

Execute the file apwfdeadlinescheduler.exe from a command line (Start - Run - cmd), specifing the time (time unit: seconds) between runs, for example:

```
C:\Models\<KB>\CSharpModel\Web\bin> apwfdeadlinescheduler.exe 60
```

Or you can execute from the directory (<KB>\CSharpModel\Web\bin) the apwfdeadlinechecker.exe that executes once.

```
C:\Models\<KB>\CSharpModel\Web\bin> apwfdeadlinechecker.exe
```

* **Java**

Execute the following command from a command line (Start - Run - cmd), specifing the time (time unit: seconds) between runs:

```
java -cp "classpath" com.gxflow.apwfdeadlinescheduler 60
```

Or as follows to execute it just once:

```
java -cp "classpath" com.gxflow.apwfdeadlinechecker
```

Example:

```
..\<application>\WEB-INF\classes>java -cp ".;..\lib\*" com.gxflow.apwfdeadlinechecker
```

```
..\<application>\WEB-INF\classes>java -cp ".;..\lib\*" com.gxflow.apwfdeadlinescheduler 60
```

* ### [**Linux**](#Linux)

```
java -cp ".:..\lib\*" com.gxflow.apwfdeadlinechecker 60
```

### [Note:](#Note%3A)

In case that GAM is enabled in the KB, consider the following:

* The location.gam and the application.gam files have to be located in the directory where the command is executed - in this example, in the "classes" directory.

#### [Scheduling on production environments](#Scheduling+on+production+environments)

Note that *apwfdeadlinescheduler* calls once every certain amount of time the *apwfdeadlinechecker* which actually checks for the deadlines and executes the corresponding events.  
The *apwfdeadlinescheduler* is especially useful when prototyping, but in production environments the *apwfdeadlinechecker*is the one recommended to be used. It's highly recommended to run the apwfdeadlinechecker using a task scheduler and not the *apwfdeadlinescheduler*.

For more information about how to schedule a task please see:

* [How To Schedule Tasks in Windows XP](http://support.microsoft.com/kb/308569)
* [Schedule a task](http://windows.microsoft.com/en-au/windows7/schedule-a-task) (for Windows 7)
* [Scheduling with Linux](http://www.ibm.com/developerworks/library/l-job-scheduling/index.html)


|  |
| --- |
| **Backlinks** |
| [How the Workflow engine evaluates Timers](https://wiki.genexus.com/commwiki/wiki?49293) |

---
