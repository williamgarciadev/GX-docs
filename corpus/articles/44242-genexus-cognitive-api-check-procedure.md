---
title: "GeneXus Cognitive API - Check procedure"
source_id: 44242
source_url: https://wiki.genexus.com/commwiki/wiki?44242
genexus_version: "18"
---

# GeneXus Cognitive API - Check procedure

Checks the training state of a custom model.

## [Parameters](#Parameters)

* **in**:&model :: [Model, GeneXusAI.Custom](https://wiki.genexus.com/commwiki/wiki?44240)  
  The model information to be checked.
* **in**:&provider :: [Provider, GeneXusAI.Configuration](https://wiki.genexus.com/commwiki/wiki?40197)  
  Provider settings.
* **inout**:&Messages :: [Messages, GeneXus.Common](https://wiki.genexus.com/commwiki/wiki?40335)  
  A collection of warning and error messages returned by the task. You should check in your code if an error was returned. Refer to [error codes and descriptions](https://wiki.genexus.com/commwiki/wiki?40188) for more information.
* **out**:&State :: [State, GeneXusAI.Custom](https://wiki.genexus.com/commwiki/wiki?44235)  
  The training state (training, ready, aborted or unknown).

## [Configuration](#Configuration)

The following table resumes the configuration properties (access credentials) you must set in order to use this AI task.

|  |  |
| --- | --- |
|  | **[PropertyKey](https://wiki.genexus.com/commwiki/wiki?40196)** |
| **[ProviderType](https://wiki.genexus.com/commwiki/wiki?40195)** | **Key** |
| **Alibaba** | - |
| **Amazon** | - |
| **Baidu** | - |
| **Google** | Service Account JSON |
| **IBM** | Visual Recognition Key |
| **Microsoft** | Custom Vision Training Key |
| **SAP** | - |
| **Tencent** | - |

## [Sample](#Sample)

After triggering the [GeneXus Cognitive API - Train procedure](https://wiki.genexus.com/commwiki/wiki?44246), for example, you can check the training status as follows:

```
do while True
   &ret = Sleep(60) // wait 60 sec until re-poll
   &State = GeneXusAI.Custom.Check(&model, &provider, &Messages)
   if &State <> GeneXusAI.Custom.State.Training OR &Messages.Count > 0
      exit // break the loop if it is ready, had aborted or raises an error
   endIf
endDo
```

## [Notes](#Notes)

* Calling this task makes sense after you call the [GeneXus Cognitive API - Train procedure](https://wiki.genexus.com/commwiki/wiki?44246).
* Despite that the &State return variable belongs to [State domain](https://wiki.genexus.com/commwiki/wiki?44235), it could adopt another string value if the provider you are using introduces a new state.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |
| **Connectivity:** | Online |

## [Availability](#Availability)

This procedure is available as of [GeneXus 16 upgrade 6](https://wiki.genexus.com/commwiki/wiki?43978,,).

* As of [GeneXus 16 upgrade 8](https://wiki.genexus.com/commwiki/wiki?44913,,)  
  -  Google Auto ML is available.

## [See also](#See+also)

* [GeneXus Cognitive API - Train procedure](https://wiki.genexus.com/commwiki/wiki?44246)
* [HowTo: Build a custom model for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?43665)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXus Cognitive API - Deploy procedure](https://wiki.genexus.com/commwiki/wiki?44247) | [GeneXus Cognitive API - Evaluate procedure](https://wiki.genexus.com/commwiki/wiki?44244) |
| [GeneXus Cognitive API - Train procedure](https://wiki.genexus.com/commwiki/wiki?44246) | [GeneXusAI Module Overview](https://wiki.genexus.com/commwiki/wiki?40315) | [HowTo: Get credentials from a cloud provider for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40204) | [Model data type](https://wiki.genexus.com/commwiki/wiki?44240) |
| [State domain](https://wiki.genexus.com/commwiki/wiki?44235) |

---
