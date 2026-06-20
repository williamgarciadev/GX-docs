---
title: "On assignment change property (GeneXus 18 Upgrade 4 or prior)"
source_id: 55694
source_url: https://wiki.genexus.com/commwiki/wiki?55694
genexus_version: "18"
---

# On assignment change property (GeneXus 18 Upgrade 4 or prior)

Executes a Procedure when the assignment of a Task instance changes.

### [Scope](#Scope)

**Controls:** [Task](https://wiki.genexus.com/commwiki/wiki?17495), [Subprocess](https://wiki.genexus.com/commwiki/wiki?17268)   
**Level:** [Version](https://wiki.genexus.com/commwiki/wiki?7860)

### [Description](#Description)

The change in the assignment could be:

* Take Task

`[imagen omitida: wiki id 11553]`

Using workflow data types would be:

```
&workitem.Assign(user)
```

* Reassign Task

`[imagen omitida: wiki id 11554]`

Using workflow data types would be:

```
&workitem.Reassign(sourceUser, targetUser)
```

* Delegate Task

`[imagen omitida: wiki id 11633]`

Using workflow data types would be:

```
Delegate (user)
```

The procedures have the following parameters rule: parm(in:&wfevent);

where:  
&wfevent has the WorkflowAssignmentChangeEvent Data Type data type associated.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [See Also](#See+Also)

[HowTo: Work With Event Handlers](https://wiki.genexus.com/commwiki/wiki?11558)
