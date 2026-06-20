---
title: "HowTo: Complete a Workitem from an Application associated with another activity"
source_id: 9989
source_url: https://wiki.genexus.com/commwiki/wiki?9989
genexus_version: "18"
---

# HowTo: Complete a Workitem from an Application associated with another activity

Suppose that from an application associated with activity "A" you want to complete the workitem associated with activity "B." In this case, the workflow context workitem is the one corresponding to activity "A" and not to activity "B." Consequently, you must iterate in the collection of workitems associated with the process instance to search for the one corresponding to activity "B." One of the processes to do this is shown below:

```
&workitems = &wfprocessinstance.Workitems
For &i = 1 to &workitems.Count
	&workitem = &workitems.Item(&i)
	&activity = &workitem.Activity
	If &activity.Name = 'B'
		&workitem.Complete()
		commit
	Endif
Endfor
```

Where the variable data is as follows:

```
&wfprocessInstance 	– WorkflowProcessInstance
&workitems 		– WorkflowWorkitem (collection property = yes)
&activity		– WorkflowActivity
&i			– Numeric(4)
```


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
