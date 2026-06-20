---
title: "Log external object"
source_id: 37872
source_url: https://wiki.genexus.com/commwiki/wiki?37872
genexus_version: "18"
---

# Log external object

The Log external object allows you to write messages in the log system on different levels that will go to different streams.

|  |  |
| --- | --- |
|  |  |

## [Properties](#Properties)

Does not have any.

## [Methods](#Methods)

All of them allow you to indicate a "topic" value with the meaning of the data written.

### [Write method](#Write+method)

Writes a message in the log; optionally, you can indicate a topic and the desired log level.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Message:[VarChar(1000)](https://wiki.genexus.com/commwiki/wiki?6778) [ topic:[VarChar(40)](https://wiki.genexus.com/commwiki/wiki?6778) , logLevel:GeneXus.Common.LogLevel ] |
|  |  |

### [Fatal method](#Fatal+method)

Writes a fatal message in the log (through the errors flow channel).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Message:[VarChar(1000)](https://wiki.genexus.com/commwiki/wiki?6778) [ topic:[VarChar(40)](https://wiki.genexus.com/commwiki/wiki?6778) ] |
|  |  |

### [Error method](#Error+method)

Writes an error message in the log (through the errors flow channel).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Message:[VarChar(1000)](https://wiki.genexus.com/commwiki/wiki?6778) [ topic:[VarChar(40)](https://wiki.genexus.com/commwiki/wiki?6778) ] |
|  |  |

### [Warning method](#Warning+method)

Writes a warning message in the log (through the warnings flow channel).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Message:[VarChar(1000)](https://wiki.genexus.com/commwiki/wiki?6778) [ topic:[VarChar(40)](https://wiki.genexus.com/commwiki/wiki?6778) ] |
|  |  |

### [Info method](#Info+method)

Writes an info message in the log (through the info flow channel).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Message:[VarChar(1000)](https://wiki.genexus.com/commwiki/wiki?6778) [ topic:[VarChar(40)](https://wiki.genexus.com/commwiki/wiki?6778) ] |
|  |  |

### [Debug method](#Debug+method)

Writes a debug message in the log (through the debug flow channel).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Message:[VarChar(1000)](https://wiki.genexus.com/commwiki/wiki?6778) [ topic:[VarChar(40)](https://wiki.genexus.com/commwiki/wiki?6778) ] |
|  |  |

**Note**: If you pass a Topic that begins with $, the log message literally takes what follows the dollar sign as the topic. Otherwise, the topic will be the concatenation of the string "GeneXusUserLog" followed by the topic you passed as a parameter: GeneXusUserLog.

You can also change the "GeneXusUserLog" string for something else, defining an environment variable named USER\_LOG\_NAMESPACE.

## [Events](#Events)

Does not have any.

## [Domains](#Domains)

### [LogLevel domain](#LogLevel+domain)

Enumerated domain with the available log levels. In order of significance:

|  |  |
| --- | --- |
| **FATAL** | Fatal level |
| **ERROR** | Error level |
| **WARNING** | Warning level |
| **INFO** | Informational level |
| **DEBUG** | Debug level |
| **OFF** | Log disabled |
|  |  |

## [Samples](#Samples)

### [Native Mobile](#Native+Mobile)

Suppose you have the [Default Log Level property](https://wiki.genexus.com/commwiki/wiki?33333) set to "Warning" and the following code in a client event:

```
Event 'Test'
    Composite
        Log.Debug(!"Debug message",!"MyCompany.Test.TestSDLoggingDebug")
        Log.Info(!"Info message",!"MyCompany.Test.TestSDLoggingInfo")
        Log.Warning(!"Warning message",!"MyCompany.Test.TestSDLoggingWarning")
        Log.Error(!"Error message",!"MyCompany.Test.TestSDLoggingError")
    EndComposite
Endevent
```

Then, in Android's LogCat, you will see the following messages (refer to [HowTo: Enable logging for Native Mobile](https://wiki.genexus.com/commwiki/wiki?37846)).

`[imagen omitida: wiki id 37875]`

Note that it only displays Warning and Error messages due to the Log Level property. Other messages are ignored (Debug and Info).

**Note**: Remember that log messages will be displayed on LogCat/XCode in online applications only when the Log external object is executed on client-side events. In this case, the Start, Refresh, and Load events will print the log depending on the server-side configuration (as shown in the example below).

### [Web](#Web)

Suppose the [User Log level property](https://wiki.genexus.com/commwiki/wiki?42434) is set to "6.All" and the [Log output property](https://wiki.genexus.com/commwiki/wiki?39568) is set to "File". Then, if you write an event like this:

```
Event 'Test'
      Log.Write(!"Write message", !"MyCompany.Test.TestLoggingWrite",LogLEvel.DEBUG)
      Log.Debug(!"Debug message",!"MyCompany.Test.TestLoggingDebug")
      Log.Info(!"Info message",!"MyCompany.Test.TestLoggingInfo")
      Log.Warning(!"Warning message",!"MyCompany.Test.TestLoggingWarning")
      Log.Error(!"Error message",!"MyCompany.Test.TestLoggingError")
      Log.Fatal(!"Fatal message",!"MyCompany.Test.TestLoggingFatal")
Endevent
```

In the *client.log* file, you will see the following messages:

`[imagen omitida: wiki id 39455]`

**Notes:**

* The following statements are equivalent:

  ```
  msg(&string,status)
  Log.Debug(&string)
  Log.Write(&string,"",LogLevel.DEBUG)
  ```
* The topic by default is concatenated to a hardcoded string "GeneXusUserLog".

## [Scope](#Scope)

**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

## [Availability](#Availability)

This external object is available as of [GeneXus 15 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?38845,,)

## [Best practices](#Best+practices)

When using [Modules](https://wiki.genexus.com/commwiki/wiki?22414) for sharing GeneXus' interfaces (e.g. an API), it is highly recommended to follow these guidelines.

* Always include a log message on your operations, preferably in English and with no translation (using "!" notation, e.g. *!"My log message"*) to simplify filters and searches.
* Add a topic to each log message indicating which object produces the message. You can use the following convention:  
  !"<Company>.<Module>.<Object>"  
  For example:  
  !"GeneXus.GeneXus.Common.Notifications.SendNotification"  
  where GeneXus is the company, GeneXus.Common.Notifications is the module (from the root), and SendNotification is the object.
* Use Log API instead of msg("<My message>",status)

## [See Also](#See+Also)

[HowTo: Enable logging for Native Mobile](https://wiki.genexus.com/commwiki/wiki?37846)  
[Default Log Level property](https://wiki.genexus.com/commwiki/wiki?33333)  
[Log level property](https://wiki.genexus.com/commwiki/wiki?36304)  
[Download UILogging sample](https://wiki.genexus.com/commwiki/wiki?37866,,)  
[Apple Developer - Debugging Tools](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/debugging_with_xcode/chapters/debugging_tools.html)  
[Android Developer - Write and View Logs with Logcat](https://developer.android.com/studio/debug/am-logcat.html)  
[HowTo: See trace information in applications hosted on .NET Cloud](https://wiki.genexus.com/commwiki/wiki?20541)


|  |
| --- |
| **Backlinks** |
| [A03:2021 - Injection](https://wiki.genexus.com/commwiki/wiki?50183) |
| [External utilities used by GeneXus generated web applications](https://wiki.genexus.com/commwiki/wiki?15671) | [External utilities used by GeneXus generated web applications (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54956) | [External utilities used by GeneXus generated web applications (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55934) |
| [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) | [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) | [HowTo: Watch .NET logs using OpenTelemetry (with SigNoz)](https://wiki.genexus.com/commwiki/wiki?57281) |
| [Load balancing considerations](https://wiki.genexus.com/commwiki/wiki?45291) | [Log level property](https://wiki.genexus.com/commwiki/wiki?36304) | [Log level property (GeneXus 18 upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56151) | [Log settings with environment variables](https://wiki.genexus.com/commwiki/wiki?53361) |
| [Log settings with environment variables (GeneXus 18 upgrade 1)](https://wiki.genexus.com/commwiki/wiki?53615) | [Log settings with environment variables (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56152) | [Monolithic systems](https://wiki.genexus.com/commwiki/wiki?55516) | [Operation and Monitoring the DevOps process](https://wiki.genexus.com/commwiki/wiki?44706) |
| [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) | [User Log level property](https://wiki.genexus.com/commwiki/wiki?42434) |

---
