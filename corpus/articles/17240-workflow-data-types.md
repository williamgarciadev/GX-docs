---
title: "Workflow Data Types"
source_id: 17240
source_url: https://wiki.genexus.com/commwiki/wiki?17240
genexus_version: "18"
---

# Workflow Data Types

[GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) provides an [API](https://wiki.genexus.com/commwiki/wiki?51350) for handling Workflow data types, which are a series of objects that model the different entities of the Workflow system. Each object (data type) has a series of properties and methods that allow interaction with the system. The purpose of the following sessions is to describe the different objects, enumerating each one of their properties and methods.

### [Classes Hierarchy Chart](#Classes+Hierarchy+Chart+)

The following figure shows the chart corresponding to the Classes Hierarchy of the main data types:  
   
`[imagen omitida: wiki id 7569]`

See [Workflow Data Types: Programming best practices](https://wiki.genexus.com/commwiki/wiki?23318) in order to learn how to correctly use the *Workflow Data Types*.

**Important:** Be aware that when using any of the *Workflow Data Types* exclusively, GeneXus doesn't commit automatically. Meaning that *Workflow Data Types* don´t commit when used, so every time you use them to do an update, you must commit the changes. Also, take into consideration the [LUW](https://wiki.genexus.com/commwiki/wiki?2424) when using the *Workflow Data Types* and committing, so the changes are applied correctly.

### [Data Types](#Data+Types+)

* [Workflow ActionPerformedEvent](https://wiki.genexus.com/commwiki/wiki?12040)
* [WorkflowActivity](https://wiki.genexus.com/commwiki/wiki?17229)
* [WorkflowApplicationData](https://wiki.genexus.com/commwiki/wiki?10264,,)
* WorkflowApplicationParameter
* WorkflowApplicationParameterMapping
* [WorkflowAssignmentChangeEvent](https://wiki.genexus.com/commwiki/wiki?10279)
* [WorkflowAttribute](https://wiki.genexus.com/commwiki/wiki?10271)
* [WorkflowBusinessEvent](https://wiki.genexus.com/commwiki/wiki?12189)
* [WorkflowBusinessEventInstance](https://wiki.genexus.com/commwiki/wiki?12190)
* [WorkflowCalendar](https://wiki.genexus.com/commwiki/wiki?11609)
* [WorkflowContext](https://wiki.genexus.com/commwiki/wiki?12187)
* [WorkflowDataChangeEvent](https://wiki.genexus.com/commwiki/wiki?10278)
* [WorkflowDocumentDefinition](https://wiki.genexus.com/commwiki/wiki?10260)
* [Workflow Document Instance](https://wiki.genexus.com/commwiki/wiki?17282)
* [WorkflowDocumentRepository](https://wiki.genexus.com/commwiki/wiki?10272)
* [WorkflowError](https://wiki.genexus.com/commwiki/wiki?10283)
* [WorkflowEvent](https://wiki.genexus.com/commwiki/wiki?10275)
* [WorkflowEventRepository](https://wiki.genexus.com/commwiki/wiki?10274)
* [WorkflowFilter](https://wiki.genexus.com/commwiki/wiki?10282)
* [WorkflowObject](https://wiki.genexus.com/commwiki/wiki?10281)
* [WorkflowOrganizationalModel](https://wiki.genexus.com/commwiki/wiki?10266)
* [WorkflowOrganizationalUnitDefinition](https://wiki.genexus.com/commwiki/wiki?10269)
* [WorkflowOrganizationalUnit](https://wiki.genexus.com/commwiki/wiki?10270)
* [WorkflowPriorityChangeEvent](https://wiki.genexus.com/commwiki/wiki?10277)
* [WorkflowProcessDefinition](https://wiki.genexus.com/commwiki/wiki?17239)
* [WorkflowProcessInstance](https://wiki.genexus.com/commwiki/wiki?17771)
* [WorkflowRole](https://wiki.genexus.com/commwiki/wiki?17230)
* [WorkflowServer](https://wiki.genexus.com/commwiki/wiki?11671)
* [WorkflowSetting](https://wiki.genexus.com/commwiki/wiki?15084)
* [WorkflowStateChangeEvent](https://wiki.genexus.com/commwiki/wiki?10276)
* [WorkflowTimer](https://wiki.genexus.com/commwiki/wiki?15124)
* [WorkflowUser](https://wiki.genexus.com/commwiki/wiki?17273)
* [WorkflowWorkitem](https://wiki.genexus.com/commwiki/wiki?11731)

### [Notes](#Notes)

As from [GeneXus 17 upgrade 2](https://wiki.genexus.com/commwiki/wiki?47418,,), the possibility of referencing the names of a diagram in Procedures or events is added as follows:

`[imagen omitida: wiki id 47578]`


|  |
| --- |
| **Pages** |
| [Workflow Domains](https://wiki.genexus.com/commwiki/wiki?15734) | [Workflow Enumerated Domains](https://wiki.genexus.com/commwiki/wiki?11306) | [Workflow Server Data Type](https://wiki.genexus.com/commwiki/wiki?11671) |
| [Workflow Setting Data Type](https://wiki.genexus.com/commwiki/wiki?15084) | [WorkflowActionPerformedEvent Data Type](https://wiki.genexus.com/commwiki/wiki?12040) | [WorkflowActivity Data Type](https://wiki.genexus.com/commwiki/wiki?17229) |
| [WorkflowApplicationData Data Type](https://wiki.genexus.com/commwiki/wiki?10264,WorkflowApplicationData+Data+Type,) | [WorkflowAssignmentChangeEvent Data Type](https://wiki.genexus.com/commwiki/wiki?10279) | [WorkflowBusinessEvent Data Type](https://wiki.genexus.com/commwiki/wiki?12189) |
| [WorkflowBusinessEventInstance Data Type](https://wiki.genexus.com/commwiki/wiki?12190) | [WorkflowCalendar data type](https://wiki.genexus.com/commwiki/wiki?11609) | [WorkflowContext Data Type](https://wiki.genexus.com/commwiki/wiki?12187) |
| [WorkflowDataChangeEvent Data Type](https://wiki.genexus.com/commwiki/wiki?10278) | [WorkflowDocumentDefinition Data Type](https://wiki.genexus.com/commwiki/wiki?10260) | [WorkflowDocumentInstance Data Type](https://wiki.genexus.com/commwiki/wiki?17282) |
| [WorkflowError Data Type](https://wiki.genexus.com/commwiki/wiki?10283) | [WorkflowEvent Data Type](https://wiki.genexus.com/commwiki/wiki?10275) | [WorkflowEventRepository Data Type](https://wiki.genexus.com/commwiki/wiki?10274) |
| [WorkflowFilter Data Type](https://wiki.genexus.com/commwiki/wiki?10282) | [WorkflowGateway Data Type](https://wiki.genexus.com/commwiki/wiki?27131) | [WorkflowGatewayInstance Data Type](https://wiki.genexus.com/commwiki/wiki?27135) |
| [WorkflowNode Data Type](https://wiki.genexus.com/commwiki/wiki?27136) | [WorkflowNodeInstance Data Type](https://wiki.genexus.com/commwiki/wiki?27137) | [WorkflowObject Data Type](https://wiki.genexus.com/commwiki/wiki?10281) |
| [WorkflowOrganizationalModel data type](https://wiki.genexus.com/commwiki/wiki?10266) | [WorkflowOrganizationalUnit Data Type](https://wiki.genexus.com/commwiki/wiki?10270) | [WorkflowOrganizationalUnitDefinition Data Type](https://wiki.genexus.com/commwiki/wiki?10269) |
| [WorkflowPriorityChangeEvent Data Type](https://wiki.genexus.com/commwiki/wiki?10277) | [WorkflowProcessDefinition Data Type](https://wiki.genexus.com/commwiki/wiki?17239) | [WorkflowProcessInstance Data Type](https://wiki.genexus.com/commwiki/wiki?17771) |
| [WorkflowRestrictionDefinition Data Type](https://wiki.genexus.com/commwiki/wiki?12192) | [WorkflowRole Data Type](https://wiki.genexus.com/commwiki/wiki?17230) | [WorkflowStateChangeEvent Data Type](https://wiki.genexus.com/commwiki/wiki?10276) |
| [WorkflowTimer Data Type](https://wiki.genexus.com/commwiki/wiki?15124) | [WorkflowUser Data Type](https://wiki.genexus.com/commwiki/wiki?17273) | [WorkflowWorkitem Data Type](https://wiki.genexus.com/commwiki/wiki?11731) |

---
