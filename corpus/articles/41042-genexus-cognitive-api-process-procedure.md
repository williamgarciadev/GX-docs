---
title: "GeneXus Cognitive API - Process procedure"
source_id: 41042
source_url: https://wiki.genexus.com/commwiki/wiki?41042
genexus_version: "18"
---

# GeneXus Cognitive API - Process procedure

Sends a video to be processed in order to be analyzed later by [GeneXus Cognitive API - Analyze procedure](https://wiki.genexus.com/commwiki/wiki?41041). This task is performed asynchronously due to the processing latency.

## [Parameters](#Parameters)

* **in**:&video :: [Video data type](https://wiki.genexus.com/commwiki/wiki?16608)  
  The video to be processed.
* **in**:&locale :: [Locale, GeneXusAI](https://wiki.genexus.com/commwiki/wiki?40450)  
  The language locale of the input speech.
* **in**:&callbackObject :: ObjectName, GeneXus  
  Optional object name to be called after the video has been processed (e.g. a Procedure object).
* **in**:&provider :: [Provider, GeneXusAI.Configuration](https://wiki.genexus.com/commwiki/wiki?40197)  
  A provider setting.
* **inout**:&Messages :: [Messages, GeneXus.Common](https://wiki.genexus.com/commwiki/wiki?40335)  
  A collection of warning and error messages returned by the task. You should check in your code if an error was returned. Refer to [error codes and descriptions](https://wiki.genexus.com/commwiki/wiki?40188) for more information.
* **out**:&videoId :: [VideoId, GeneXusAI.Video](https://wiki.genexus.com/commwiki/wiki?41109)  
  A video identifier to call [GeneXus Cognitive API - Analyze procedure](https://wiki.genexus.com/commwiki/wiki?41041) after the video has been processed.

## [Configuration](#Configuration)

The following table resumes the configuration properties (access credentials) you must set in order to use this AI task.

|  |  |  |  |
| --- | --- | --- | --- |
|  | **[PropertyKey](https://wiki.genexus.com/commwiki/wiki?40196)** | | |
| **[ProviderType](https://wiki.genexus.com/commwiki/wiki?40195)** | **Key** | **KeySecret** | **Account** |
| **Alibaba** | 内容安全 app-key | 用户AccessKey | 用户AccessKey |
| **Amazon** | - | - | - |
| **Baidu** | 视频内容分析 | 视频内容分析 |  |
| **Google** | Video Intelligence API | - | - |
| **IBM** | - | - | - |
| **Microsoft** | Video Indexer | - | Azure Connect |
| **SAP** | - | - | - |
| **Tencent** | - | - | - |

## [Sample](#Sample)

This section describes two alternatives for processing a video: synchronously or asynchronously. Once processed, you can get the analysis made by the provider. In other words, you need to use both Process and Analyze tasks.

### [Synchronous processing](#Synchronous+processing)

The way you process a video synchronously is by polling for the processing status. The example below shows how you can do it.

```
&callbackObject = "" // It's not necessary to indicate a callback object for this strategy
&VideoId = GeneXusAI.Video.Process(&video,&locale,&callbackObject,&provider,&Messages) 
if &Messages.Count > 0 
  <process_errors>
else
   do while True
      &outputAnalysis = GeneXusAI.Video.Analyze(&videoId,&provider,&Messages) // Polling
      if &outputAnalysis.Completed OR &Messages.Count > 0 
         exit // Exit from the loop
      endIf
     &x = Sleep(30) // Wait 30 seconds until poll again
   endDo
   if &Messages.Count > 0
       <process_errors> 
   else
       <analyze_result>
   endIf
endIf
```

Note that for large video files this strategy may take a long time. Consider using asynchronous strategy in these cases.

### [Asynchronous processing](#Asynchronous+processing)

The way you process a video asynchronously is by indicating a callback-object to this task.

For example, you can write a code as follows:

```
&callbackObject = Link(VideoHandler) // It gets the object name mantaining a reference to it
&VideoId = GeneXusAI.Video.Process(&video,&locale,&callbackObject,&provider,&Messages)
if &Messages.Count > 0
   <process_errors>
endIf
```

Where VideoHandler is a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) with [Expose as Web Service property](https://wiki.genexus.com/commwiki/wiki?36480) = True, and defined as follows:

```
Rules:
   parm(in:&videoId); // Mandatory :: video identifier
Source:
   &OutputAnalysis = GeneXusAI.Video.Analyze(&videoId,&provider,&Messages)
   if &Messages.Count > 0
       <process_errors>
   else
       <analyze_result>
   endIf
```

Alternatively, instead of getting the analysis in this object, you can send a notification and call the [GeneXus Cognitive API - Analyze procedure](https://wiki.genexus.com/commwiki/wiki?41041) on a Panel for Web or Smart Devices. This can be done by using [Server.Socket external object](https://wiki.genexus.com/commwiki/wiki?22442) for Web, or [Notification Provider API](https://wiki.genexus.com/commwiki/wiki?33687) for Smart Devices.

**Warning**: For testing your asynchronous solution, your application must be accessible for the external provider (e.g. your IP must be remotely accessible, or you can host your application on a real server -- Deploy To Cloud option can be a good alternative).

## [Notes](#Notes)

* For the asynchronous strategy, the **callback-object** must include a Parm rule with the incoming video identifier.

  ```
  parm(in:&videoId);
  ```
* Special considerations
  + For Microsoft:
    - To get the Key/Account, please refer to [this document](https://wiki.genexus.com/commwiki/wiki?40204).
    - Despite no region is filled up on the 'Faces' field items (top, left, width, height fields are zero -- or empty), you will have a property with '*thumbnail*' key whose value is a cropped image of the identified face.
  + For Baidu:
    - Only supports synchronous mode (not callback-url is available).

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |
| **Connectivity:** | Online |

## [Availability](#Availability)

This procedure is available as of [GeneXus 16 upgrade 1](https://wiki.genexus.com/commwiki/wiki?40782,,).

* As of [GeneXus 16 upgrade 3](https://wiki.genexus.com/commwiki/wiki?42129,,):  
  - Baidu AI is available.
* As of [GeneXus 16 upgrade 4](https://wiki.genexus.com/commwiki/wiki?42755,,):  
  - Alibaba AI is available.

## [See also](#See+also)

* [GeneXus Cognitive API - Analyze procedure](https://wiki.genexus.com/commwiki/wiki?41041)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXus Cognitive API - Analyze procedure](https://wiki.genexus.com/commwiki/wiki?41041) |
| [GeneXusAI Module Overview](https://wiki.genexus.com/commwiki/wiki?40315) | [HowTo: Get credentials from a cloud provider for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40204) | [Locale domain](https://wiki.genexus.com/commwiki/wiki?40450) |
| [Percentage domain](https://wiki.genexus.com/commwiki/wiki?41274) | [VideoId domain](https://wiki.genexus.com/commwiki/wiki?41109) |

---
