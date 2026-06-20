---
title: "HowTo: Call Processes Using the Workflow API"
source_id: 50695
source_url: https://wiki.genexus.com/commwiki/wiki?50695
genexus_version: "18"
---

# HowTo: Call Processes Using the Workflow API

This document shows how to call a process with the Workflow API by providing an example.

Suppose that you want to call a process automatically.

To do so, you can create the following diagrams:

`[imagen omitida: wiki id 50696]`

And execute the following code:

```
&ProcessDefinition = &Server.GetProcessDefinitionByName('BPDStarter')
&ProcessInstance = &ProcessDefinition.CreateInstance()
&ProcessInstance.Start()
&ProcessInstance.ThrowSignal('S1')
commit
return
```

**Note**: The Signal Intermediate Event needs to be active to listen to the signal.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
