---
title: "HowTo: Get and Set a Relevant Data Value"
source_id: 11720
source_url: https://wiki.genexus.com/commwiki/wiki?11720
genexus_version: "18"
---

# HowTo: Get and Set a Relevant Data Value

In most cases, Workflow manages the relevant data between task automatically, but there are some cases where you need to retrieve the relevant data by program, for instance:

#### [Get](#Get)

```
&WorkflowApplicationData = &WorkflowContext.ProcessInstance.GetApplicationDataByName('<RelevanDataName>')
&Variable = &WorkflowApplicationData.NumericValue
```

#### [Set](#Set)

```
&WorkflowContext.ProcessInstance.GetApplicationDataByName('<RelevanDataName>').NumericValue = &Variable
Commit
```

**Where:**

*&WorkflowContext* (WorkflowContext data type)  
*&WorkflowApplicationData* (WorkflowApplicationData data type)  
*&Variable* (in this case Numeric but it could be another type)

### [See Also](#See+Also+)

[Workflow Context](https://wiki.genexus.com/commwiki/wiki?11416)  
[Workflow Process Instance Data Type](https://wiki.genexus.com/commwiki/wiki?11702,,)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [HowTo: Assign a GXflow task with relevant data](https://wiki.genexus.com/commwiki/wiki?51447) |
| [Workflow Relevant Data Editor](https://wiki.genexus.com/commwiki/wiki?11719) |

---
