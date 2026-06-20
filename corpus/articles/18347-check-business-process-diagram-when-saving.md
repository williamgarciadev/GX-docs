---
title: "Check Business Process Diagram when saving"
source_id: 18347
source_url: https://wiki.genexus.com/commwiki/wiki?18347
genexus_version: "18"
---

# Check Business Process Diagram when saving

During the saving of a process diagram a check process is performed to validate the diagram. The list that follows shows the message that can appear during the save of a Business Process Diagram.

|  |
| --- |
| **Message** |
| **warning: 'Condition rule' property is empty ('Diagram')** |
| No conditions were entered in the condition rules. |
|  |
| **warning: 'Application' property is empty ('Diagram,%1')** |
| No application was entered in the Application property in the User Task mentioned. |
|  |
| **warning: 'Procedure' property is empty ('Diagram,%1')** |
| No procedure was entered in the Procedure property in the Script Task mentioned. |
|  |
| **warning: 'Lapse expression rule' property is empty ('Diagram,IntermediateEvent')** |
| No expression was entered in the 'Lapse expression rule' property. |
|  |
| **warning: Only one start none event is allowed ('Diagram')** |
| Only one Start None Event is supported in a process. |
|  |
| **error: Activity  must have at least one incoming sequence flow connector and one outgoing sequence flow connector ('Diagram,Gateway)** |
| This error occurs when an Activity doesn't have at least one incoming sequence flow or one outgoing sequence flow connector. |
|  |
| **error: Gateway must have at least one incoming sequence flow connector and one outgoing sequence flow connector ('Diagram,Gateway')** |
| This error occurs when a Gateway doesn't have at least one incoming sequence flow or one outgoing sequence flow connector. |
|  |
| **error: End event must have at least one incoming sequence flow connector ('Diagram,EndEvent1')** |
| This error occurs when an End Event don't have at least one incoming sequence flow connector. |
|  |
| **error: Start event must have at least one outgoing sequence flow connector ('Diagram,StartEvent1')** |
| This error occurs when a Start Event doesn't have at least one outgoing sequence flow connector. |
|  |
| **error: Validation failed for 'Application' property: wrong number of parameter mappings ('Diagram,Request')** |
| This error occurs when the number of parameter differs between the Application and the Relevant Data. |
|  |
| **error: Type mismatch in mapping between parameter %1 and relevant data %2** |
| This error occurs when there is a type mismatch between the Application parameter and the relevant data. |
|  |
| **error: Embedded subprocess can only have one None start event ('Diagram,StartEvent1')** |
| This error occurs when an Embedded subprocess has more than one None Start Event. |
|  |
| **error: Validation failed for 'Condition procedure' property: ('Diagram,Task')** |
| This error occurs when the procedure associated to a condition has an invalid value. |
|  |
| **error:  Procedure has invalid signature, it must be like: 'parm(in: &process****[WorkflowProcessDefinition]****, in: &instance****[WorkflowProcessInstance]****, in: &workitem****[WorkflowWorkitem]****, out: code****[Numeric(4)]****);'** |
| This error occurs when the procedure parm rule differs from the expected value. |


|  |
| --- |
| **Backlinks** |
| [Category:Business Process Diagram object](https://wiki.genexus.com/commwiki/wiki?16486) | [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |
|

---
