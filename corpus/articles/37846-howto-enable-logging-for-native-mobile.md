---
title: "HowTo: Enable logging for Native Mobile"
source_id: 37846
source_url: https://wiki.genexus.com/commwiki/wiki?37846
genexus_version: "18"
---

# HowTo: Enable logging for Native Mobile

This document gives the first approach for debugging Native Mobile applications by inspecting log messages.

## [Step 1 - Enable Log level](#Step+1+-+Enable+Log+level)

The first thing you must do is to set the [Enable Logging property](https://wiki.genexus.com/commwiki/wiki?37876) in **True** (default value), and then indicate the log level to record for each feature.

This action can be made by setting the following properties at the [Native Mobile Main object](https://wiki.genexus.com/commwiki/wiki?17817)'s level:

* [Default Log Level property](https://wiki.genexus.com/commwiki/wiki?33333)
* [Offline Data Base Access Log Level property](https://wiki.genexus.com/commwiki/wiki?33330)
* [Http Connections Log Level property](https://wiki.genexus.com/commwiki/wiki?33332)
* [Offline Synchronization Log Level property](https://wiki.genexus.com/commwiki/wiki?33331)

## [Step 2 - Run the application](#Step+2+-+Run+the+application)

You must build and run your Native Mobile application ([Main Object](https://wiki.genexus.com/commwiki/wiki?5770)).

## [Step 3 - Inspect log messages](#Step+3+-+Inspect+log+messages)

### [Android environment](#Android+environment)

There are two ways to debug Android applications, all of them by using the LogCat tool.

> **1) By using Android Studio**  
> If you are using Android Studio, you can run [Android LogCat](https://developer.android.com/studio/debug/am-logcat#running) by navigating from **View > Tool Windows > Logcat** .
>
> `[imagen omitida: wiki id 50831]`

### [Apple environment](#Apple+environment)

There are three ways to check the generated logs in Apple applications.

> **1) By using XCode Debug Console**  
> The developer should open XCode and run the application from it. Then, log messages will be displayed on the [debug Console](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/debugging_with_xcode/chapters/debugging_tools.html).  
> `[imagen omitida: wiki id 37867]`
>
> **2) By inspecting application log files**  
> The application will generate \*.log files in its data path (accessible from [Directory.ApplicationDataPath](https://wiki.genexus.com/commwiki/wiki?27388)). Then, you can read it from the application and send a report, or simply display its contents on it. The following example displays log files and their contents directly on the application ([download it here](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?37866,,), and include it in your KB).  
> `[imagen omitida: wiki id 37868]`
>
> **3) By using logfile from simulator**  
> Once the application is launched in a simulator (e.g. by F5 from GeneXus), the developer can inspect the log by doing Debug > Open System Log... from the system bar (or ⌘+/ shortcut).

## [Notes](#Notes)

* With Apple applications, instead of setting logging properties with GeneXus, you can enable logging by going to Settings > <your\_app> and turn on Enable Log switch (and which log level desires).  
  `[imagen omitida: wiki id 37882]`

## [Scope](#Scope)

**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)

## [See Also](#See+Also)

[Download UILogging module](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?37866,,)  
[Apple Developer - Debugging Tools](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/debugging_with_xcode/chapters/debugging_tools.html)  
[Android Developer - Write and View Logs with Logcat](https://developer.android.com/studio/debug/am-logcat.html)


|  |
| --- |
| **Backlinks** |
| [Debugging in GeneXus](https://wiki.genexus.com/commwiki/wiki?9307) | [Enable Logging property](https://wiki.genexus.com/commwiki/wiki?37876) | [Log external object](https://wiki.genexus.com/commwiki/wiki?37872) |
| [Notification Provider API](https://wiki.genexus.com/commwiki/wiki?33687) | [Offline Synchronization Log Level property](https://wiki.genexus.com/commwiki/wiki?33331) |

---
