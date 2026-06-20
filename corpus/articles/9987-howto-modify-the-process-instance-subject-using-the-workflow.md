---
title: "HowTo: Modify the Process Instance Subject using the Workflow API"
source_id: 9987
source_url: https://wiki.genexus.com/commwiki/wiki?9987
genexus_version: "18"
---

# HowTo: Modify the Process Instance Subject using the Workflow API

The Subject is a very important property of Process Instances.

The importance of this property lies in the fact that it is used in the different GXflow Client application components as an association mechanism. The subject allows giving a descriptive name to the Process Instance, making its follow-up easier for Workflow users.

### [Sample](#Sample)

Suppose that in the ‘request’ Transaction associated with the ‘manufacturing’ task you want to update the Process Instance subject with the request description. This can be done by inserting the following line in the transaction rules:

```
&wfprocessinstance.Subject = RequestDescription on AfterValidate;
```

Where the variable data is:

```
&wfprocessInstance 	– WorkflowProcessInstance
```

An example can be downloaded from [here](http://wiki.gxtechnical.com/commwiki/servlet/hwiki?file%3AUseCase2_gxflow,).

### [Steps](#Steps)

**1.** Import the xpz file.

**2.** Run the business process diagram.

**3.** Once the Request Transaction is completed, the process instance subject changes as shown in the image below (suppose the description is "Request N°1").

`[imagen omitida: wiki id 52674]`


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
