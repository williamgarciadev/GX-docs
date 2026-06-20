---
title: "HowTo: Invoke a Main Procedure that uses GAM API in a Java environment"
source_id: 54205
source_url: https://wiki.genexus.com/commwiki/wiki?54205
genexus_version: "18"
---

# HowTo: Invoke a Main Procedure that uses GAM API in a Java environment

This article explains how you can invoke a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) set as [Main](https://wiki.genexus.com/commwiki/wiki?5770) that uses the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535) from the command line in a Java [environment](https://wiki.genexus.com/commwiki/wiki?7115).

### [**Setup**](#Setup)

* Install Java on your PC. You can follow this link and **[download Java](https://www.oracle.com/java/technologies/downloads/)** if you have any version of Java already installed.

Go to [Java Applications Development](https://wiki.genexus.com/commwiki/wiki?52358) to see the requirements to generate in Java with GeneXus.

* Set the [Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) to True.
* Set the Procedure [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) to Command Line, and the [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) to True**.**

### [**Call the Procedure from the KB Model:**](#Call+the+Procedure+from+the+KB+Model%3A)

* Navigate to the 'Web' directory from the command line.

```
C:\<path_to_KB>\<your_KB>\<environment>\web>
```

* Once you are there, execute java.exe with the following classpath:

```
-cp build\classes\java\main;"build\libs\*"
```

An example of execution could be as follows:

```
C:\<path_to_KB>\<your_KB>\<environment>\web>"C:\Program Files\Java\jdk-11.0.15\bin\java.exe"  -cp build\classes\java\main;"build\libs\*" com.kbname.aprocmain
```

**Note**: Make sure that connection.gam and application.gam are in the directory from which you are going to run this.

If your Procedure receives parameters, they must be written at the end of the line, as shown below:

```
.."build\libs\*" com.kbname.aprocmain “charAttribute” numberAttribute “charAttribute”
```

Pay attention to how these parameters must be written, depending on whether they are characters or numeric.

### [Call the Procedure from the Tomcat WebApp:](#Call+the+Procedure+from+the+Tomcat+WebApp%3A)

* Navigate to the 'WEB-INF' directory from the command line:

  ```
  C:\<path_to_Tomcat>\webapps\<your_webapp>\WEB-INF>
  ```
* Once you are there, execute java.exe with the following classpath:

  ```
  -cp classes\;"lib\*"
  ```

An example of execution could be as follows:

```
C:\Program Files\Apache Software Foundation\Tomcat 9.0\webapps\WebAppName\WEB-INF>"C:\Program Files\Java\jdk-11.0.17\bin\java.exe" -cp classes\;"lib\*" com.kbname.aprocmain
```

**Note**: Make sure that connection.gam and application.gam are in the directory from which you are going to run this.

If your Procedure receives parameters, they must be written at the end of the line, as shown below:

```
.."build\libs\*" com.kbname.aprocmain “charAttribute” numberAttribute “charAttributte”
```

Pay attention to how these parameters must be written, depending on whether they are characters or numeric.


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
