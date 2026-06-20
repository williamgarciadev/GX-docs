---
title: "HowTo: Set a user as out of office using the Workflow API"
source_id: 53541
source_url: https://wiki.genexus.com/commwiki/wiki?53541
genexus_version: "18"
---

# HowTo: Set a user as out of office using the Workflow API

This article describes how to set a user as out of office using the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

You can do it with the following code:

```
&workflowserver.Connect('<user>', '<password>')
&workflowUser = &workflowserver.GetOrganizationalModel().GetUserByName(&user)    
&workflowUser2 = &workflowserver.GetOrganizationalModel().GetUserByName(&substitute)
&workflowUser.SetOutOfOffice(&startDate, &returnDate,"",&workflowUser2)
commit
```

Where the data types variables are as follows:

```
&WorkflowServer – WorkflowServer
&workflowUser  – WorkflowUser 
&workflowUser2 – WorkflowUser
&startDate – Date
&returnDate – Date
&user – WorkflowName
&substitute – WorkflowName
```

The &startDate variable must be equal to today's date; otherwise, the user will not be set as out of office.

You can change the user's status to "in office" with the method WorkflowUser.DisableOutOfOffice()


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
