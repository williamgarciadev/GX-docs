---
title: "Log level property"
source_id: 36304
source_url: https://wiki.genexus.com/commwiki/wiki?36304
genexus_version: "18"
---

# Log level property

Configures how much detail has to be added to the log of the standard classes at runtime.

### [Values](#Values)

|  |  |
| --- | --- |
| **6. All** | The ALL Level has the lowest possible rank and is intended to turn on all logging. |
| **5. Debug** | The DEBUG Level designates fine-grained informational events that are most useful to debug an application. |
| **2. Error** | The ERROR Level designates error events that might still allow the application to continue running. |
| **1. Fatal** | The FATAL Level designates very severe error events that will presumably lead the application to abort. |
| **4. Info** | The INFO Level designates informational messages that highlight the progress of the application at coarse-grained level. |
| **0. Off** | The OFF Level has the highest possible rank and is intended to turn off logging. This is the default value. |
| **3. Warn** | The WARN Level designates potentially harmful situations. |

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Web Component](https://wiki.genexus.com/commwiki/wiki?1864), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

When using the [.NET Generator](https://wiki.genexus.com/commwiki/wiki?38604) and having the [Log output property](https://wiki.genexus.com/commwiki/wiki?39568) set to Console/File, the **Log level property** modifies the values of the <log4net threshold=...> tag of the Log.config and Log.Console.Config files. Additionally, it sets the <trace enabled=... /> tag of the Web.Configfile. These config files can be found in the web applications folder.

*Tip: The log*.config file is referenced by web.config (<log4net configSource="log.config"/>) and is used when running the web app. Log.Console.config file is referenced by Client.exe.config and is used for command line executions. For further information, check [Log4net configuration in GeneXus .Net application](https://wiki.genexus.com/commwiki/wiki?43303,,).

When using the [Java Generator](https://wiki.genexus.com/commwiki/wiki?12258), this property modifies the values of the <loggers=...> tag of the log4j.xml file. The log4j2.xml file can be found in the <webapp>\WEB-INF\classes folder.

The Log Level can also be set by defining an environment variable. See [Log settings with environment variables](https://wiki.genexus.com/commwiki/wiki?53361).

### [Advanced configuration](#Advanced+configuration)

To modify or extend log parameters, you can change values on the following templates:

* *rollingfile.console.config* which goes to the *log.console.config* file used in command-line programs.
* *rollingfile.web.config* which goes to the *log.config* file used in the web application.

Files are located in "GeneXusInstallFolder"\Log\Java\RollingFile and "GeneXusInstallFolder"\Log\Dotnet\RollingFile

To generate a log file for every day, change the template as follows:

```
 <appender  name="RollingFile" type="log4net.Appender.RollingFileAppender">
      <file  value="./"/>
      <appendToFile  value="true"/>
      <maximumFileSize  value="9000KB"/>
      <maxSizeRollBackups  value="0"/>
      <rollingStyle  value="Date"/>
      <staticLogFileName value="false" />
      <datePattern value="dd.MM.yyyy'.log'" />
      <layout  type="log4net.Layout.PatternLayout">
         <conversionPattern value="%d [%t] %-5p %c - %m%n" />
      </layout>
      <lockingModel  type="log4net.Appender.FileAppender+MinimalLock"/>
</appender>
```

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build any object.

### [See Also](#See+Also)

[Log output property](https://wiki.genexus.com/commwiki/wiki?39568)  
[Log external object](https://wiki.genexus.com/commwiki/wiki?37872)  
[HowTo: See trace information in applications hosted on .NET Cloud](https://wiki.genexus.com/commwiki/wiki?20541)  
[Log JDBC Activity property](https://wiki.genexus.com/commwiki/wiki?9135)


|  |
| --- |
| **Backlinks** |
| [A03:2021 - Injection](https://wiki.genexus.com/commwiki/wiki?50183) | [Chatbot Generator - Troubleshooting](https://wiki.genexus.com/commwiki/wiki?41260) |
| [External utilities used by GeneXus generated web applications](https://wiki.genexus.com/commwiki/wiki?15671) | [External utilities used by GeneXus generated web applications (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54956) | [External utilities used by GeneXus generated web applications (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55934) |
| [HowTo: Enable Log for GXflow runtime](https://wiki.genexus.com/commwiki/wiki?24568) | [HowTo: See trace information in applications hosted on .NET Cloud](https://wiki.genexus.com/commwiki/wiki?20541) | [Log external object](https://wiki.genexus.com/commwiki/wiki?37872) | [Log file property](https://wiki.genexus.com/commwiki/wiki?39601) |
| [Log level property (GeneXus 18 upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56151) | [Log output property](https://wiki.genexus.com/commwiki/wiki?39568) | [Log output property (GeneXus 18 Upgrade 0 or prior)](https://wiki.genexus.com/commwiki/wiki?53419) | [Log output property (GeneXus 18 upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56148) |
| [Log output property (GeneXus 18 Upgrade 7)](https://wiki.genexus.com/commwiki/wiki?57249) | [Log settings with environment variables](https://wiki.genexus.com/commwiki/wiki?53361) | [Log settings with environment variables (GeneXus 18 upgrade 1)](https://wiki.genexus.com/commwiki/wiki?53615) | [Log settings with environment variables (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56152) |
| [User Log level property](https://wiki.genexus.com/commwiki/wiki?42434) | [What is error 403?](https://wiki.genexus.com/commwiki/wiki?45483) |

---
