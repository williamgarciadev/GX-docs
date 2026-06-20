---
title: "HowTo: List Workitems filtered by Status"
source_id: 11439
source_url: https://wiki.genexus.com/commwiki/wiki?11439
genexus_version: "18"
---

# HowTo: List Workitems filtered by Status

The purpose of this article is to explain the necessary steps to make a list of workitems filtered by their Status.

First, you have to connect to the engine using the Connect method associated with the [Workflow Server Data Type](https://wiki.genexus.com/commwiki/wiki?11671). You need a user with Administrator role for this.  
  
Next, load the filter, which in this case is Status. To do so, use the enumerated domain WorkflowWorkitemState that has the following possible values:  
  
 OPEN  
 OPEN\_ACTIVE  
 OPEN\_ACTIVE\_READY  
 OPEN\_ACTIVE\_ASSIGNED  
 OPEN\_ACTIVE\_INPROCESS  
 OPEN\_SUSPENDED  
 CLOSED  
 CLOSED\_COMPLETED  
 CLOSED\_ABNORMAL  
 CLOSED\_ABNORMAL\_ABORTED  
 CLOSED\_ABNORMAL\_CANCELED  
 CLOSED\_ABNORMAL\_DELEGATED  
 CLOSED\_ABNORMAL\_EXPIRED  
 CLOSED\_ABNORMAL\_INTERRUPTED  
 CLOSED\_ABNORMAL\_SKIPPED  
 CLOSED\_ABNORMAL\_TERMINATED  
 CLOSED\_ABNORMAL\_UNDONE  
  
Use the ListWorkitems method associated with the [Workflow Server Data Type](https://wiki.genexus.com/commwiki/wiki?11671) by passing a parameter with the filter previously created.  
  
Below is the code to use when you want to list all the open and active workitems.

```
    &server.Connect('WFADMINISTRATOR','WFADMINISTRATOR')
    &filter.State = WorkflowWorkitemState.OPEN_ACTIVE
    &workitems = &server.ListWorkitems(&filter)
```

**Where:**

*&server*  
      Is a variable of WorkflowServer type  
  
*&filter*   Is a variable of WorkflowFilter type  
  
*WorkflowWorkitemState*  
      Is an enumerated domain

*&workitems*  
      Is a variable of WorkflowWorkitem type. It has to be marked as Collection.

If later you want to list, for example, the closed workitems which were aborted or expired, you should create two filters, obtain the list of workitems twice by using both filters and then run through the resulting collections.
