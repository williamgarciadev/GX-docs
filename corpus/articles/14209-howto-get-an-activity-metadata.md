---
title: "HowTo: Get an Activity Metadata"
source_id: 14209
source_url: https://wiki.genexus.com/commwiki/wiki?14209
genexus_version: "18"
---

# HowTo: Get an Activity Metadata

The following code shows how to get the metadata of an activity:

```
&activity = &WorkflowContext.Workitem.Activity
&attributes = &activity.ExtendedAttributes
for &i = 1 to &attributes.Count
       &attribute = &attributes.Item(&i)
       &Name = &attribute.Name
       &Value = &attribute.Value
endfor
```

**Where:**

&activity (WorkflowActivity data type)

&WorkflowContext (Workflow Context data type)

&attributes (WorkflowAttribute data type, is collection)

&atribute (WorkflowAttribute data type)

&Name (Character data type)

&Value (Character data type)
