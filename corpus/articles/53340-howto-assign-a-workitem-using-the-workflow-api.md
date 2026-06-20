---
title: "HowTo: Assign a Workitem Using the Workflow API"
source_id: 53340
source_url: https://wiki.genexus.com/commwiki/wiki?53340
genexus_version: "18"
---

# HowTo: Assign a Workitem Using the Workflow API

This article provides solutions to assign a Workitem to a user using the [Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240).

* If the Workitem has not been assigned yet, then you can use the following code:

```
&workitem.Assign(&user)
commit
return
```

Where the data types variables are:

```
&workitem – WorkflowWorkitem
&user – WorkflowUser
```

* If the Workitem has already been assigned, you can use the following code to assign it to another user:

```
&workitem.Reassign(&SourceUser,&TargetUser)
commit
return
```

Where the data types variables are:

```
&workitem – WorkflowWorkitem
&SourceUser – WorkflowUser
&TargetUser - WorkflowUser
```

For further information about the Workflow API, go to [Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
