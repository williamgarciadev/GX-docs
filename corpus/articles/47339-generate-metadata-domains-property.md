---
title: "Generate Metadata Domains property"
source_id: 47339
source_url: https://wiki.genexus.com/commwiki/wiki?47339
genexus_version: "18"
---

# Generate Metadata Domains property

Generates enumerated domains with activity IDs and relevant data names.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [Business Process Diagram](https://wiki.genexus.com/commwiki/wiki?16486)

### [Description](#Description)

For some Workflow APIs, you need to use the Activity ID or a Relevant Data name. The purpose of this property is to enable the generation of enumerated domains that contain Activity IDs named with the Business Process Diagram Object name followed by ActivityIds, and another containing the Relevant Data name named with the Business Process Diagram Object name followed by RelevantData.

These domains are generated and updated every time you save changes in the diagram if this property is enabled.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Samples](#Samples)

If the Business Process Diagram object name is PurchaseOrder, the generated domains will be PurchaseOrderActivityIds and PurchaseOrderRelevantData.

If the PurchaseOrder diagram has a relevant data named POId then you can use &WorkflowProcessInstance.GetApplicationDataByName(PurchaseOrderRelevantData.POId) to get the value of the relevant data using the generated domain.

### [Availability](#Availability)

This property is available since [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/wiki?46852,,).
