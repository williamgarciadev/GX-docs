---
title: "GeneXus Task MSBuild Error Codes and messages"
source_id: 51033
source_url: https://wiki.genexus.com/commwiki/wiki?51033
genexus_version: "18"
---

# GeneXus Task MSBuild Error Codes and messages

The list that follows shows the GTM messages that can be shown by the [MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?3908).

They can be displayed by batch processes that execute these tasks, such as automatic build workflows/pipes on a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) or the Build process itself that executes batch tasks.

|  |  |
| --- | --- |
| **Code** | **Message** |
| **gtm0006** | **'Neither Template or BulkCopyFile is null, only one of them must be set'.** |
|  | When executing the ['CreateKnowledgeBase' MSBuild Task](https://wiki.genexus.com/commwiki/wiki?3908) if you do not specify the Template nor the BulkCopyFile parameters, and the Default Template could not be obtained (because the entry is not defined in genexus.exe.config file or there is no Default Template indicated in that entry), this error message will be displayed. |
|  | |
| **gtm0007** | **'Template and BulkCopyFile are both null, at least one of them must be set'.** |
|  | When executing the ['CreateKnowledgeBase' MSBuild Task](https://wiki.genexus.com/commwiki/wiki?3908) if you specify both the Template and the BulkCopyFile parameters, this error message will be displayed. |
|  | |
| **gtm0092** | **Cannot find module '%1' to restore.** |
|  | When executing the ['RestoreModule' MSBuild Task](https://wiki.genexus.com/commwiki/wiki?46830) with the name of a non-installed module, this error message will be displayed. |
|  | |
|


|  |
| --- |
| **Backlinks** |
| [Toc:Coded Messages](https://wiki.genexus.com/commwiki/wiki?47288) |

---
