---
title: "HowTo: Close and complete a Workitem using the Workflow API"
source_id: 9990
source_url: https://wiki.genexus.com/commwiki/wiki?9990
genexus_version: "18"
---

# HowTo: Close and complete a Workitem using the Workflow API

Suppose that you want to complete the workitem automatically, once the associated application has been processed. In this case, you can execute the following code:

```
&WorkflowContext.Workitem.Complete()
commit
return
```

Where the data types variables are the following:

```
&WorkflowContext – WorkflowContext
```


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
