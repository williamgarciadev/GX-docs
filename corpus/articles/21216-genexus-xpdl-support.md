---
title: "GeneXus XPDL Support"
source_id: 21216
source_url: https://wiki.genexus.com/commwiki/wiki?21216
genexus_version: "18"
---

# GeneXus XPDL Support

### [What is XPDL?](#What+is+XPDL%3F)

[XPDL](http://www.wfmc.org/standards/xpdl) is a serialization format for [BPMN](http://en.wikipedia.org/wiki/Business_Process_Modeling_Notation). BPMN is a visual process notation standard from the [OMG](http://en.wikipedia.org/wiki/Object_Management_Group), endorsed by [Workflow Management Coalition](http://www.wfmc.org/), and broadly adopted across the industry. BPMN standard defines only the look of how the process definition is displayed on the screen. XPDL provides a file format that supports every aspect of the BPMN process definition notation including graphical descriptions of the diagram, as well as executable properties used at run time.

### [What is this for?](#What+is+this+for%3F)

This format allows storing and interchanging process definitions among [Business Process Modeling](http://en.wikipedia.org/wiki/Business_process_modeling#Business_process_modeling_tools) tools. With XPDL, a product can write out a process definition with full fidelity, and another product can read it in and reproduce the same diagram that was sent.

### [Which versions are supported by GeneXus?](#Which+versions+are+supported+by+GeneXus%3F)

XPDL 2.2 support was added to GeneXus X Evolution 2 Upgrade 2.

XPDL 2.1 support was added to GeneXus X Evolution 2 Upgrade 1.

### [See also](#See+also)

[Export to XPDL Option](https://wiki.genexus.com/commwiki/wiki?21177,,)  
[Import from XPDL Option](https://wiki.genexus.com/commwiki/wiki?21176,,)

### [Example](#Example)

```
<?xml version="1.0" encoding="utf-8"?>
<Package xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" Id="716fda9c-f689-49a1-a898-6d0cf6cc9460" Name="BPDiagram1" xmlns="http://www.wfmc.org/2009/XPDL2.2">
<PackageHeader>
  <XPDLVersion>2.2</XPDLVersion>
  <Vendor>GeneXus_Business_Process_Modeler</Vendor>
  <Created>23/01/2013 01:10:45 p.m.</Created>
  <ModificationDate>23/01/2013 01:10:45 p.m.</ModificationDate>
  <Description>BPDiagram1</Description>
  <Documentation />
</PackageHeader>
<RedefinableHeader>
  <Author>ARTECH\mdupont</Author>
  <Version>1.0</Version>
  <Countrykey>UY</Countrykey>
</RedefinableHeader>
<ExternalPackages />
<Participants />
<Pools>
  <Pool Id="f840edcc-490f-4ad3-9770-23f1edfdd2ae" Name="Main process" Process="716fda9c-f689-49a1-a898-6d0cf6cc9460" BoundaryVisible="false">
   <Lanes />
   <NodeGraphicsInfos>
    <NodeGraphicsInfo Height="0" Width="0">
     <Coordinates XCoordinate="0" YCoordinate="0" />
    </NodeGraphicsInfo>
   </NodeGraphicsInfos>
  </Pool>
</Pools>
<MessageFlows />
<Associations />
<Artifacts />
<WorkflowProcesses>
  <WorkflowProcess Id="716fda9c-f689-49a1-a898-6d0cf6cc9460">
   <ProcessHeader>
    <Created>23/01/2013 11:56:59 a.m.</Created>
    <Description></Description>
   </ProcessHeader>
   <RedefinableHeader>
    <Countrykey>UY</Countrykey>
   </RedefinableHeader>
   <ActivitySets />
   <Activities>
    <Activity Id="73038286-28ab-4471-b1f9-0754c7fc0493" Name="Task">
     <Description></Description>
     <Implementation>
      <Task>
       <TaskUser />
      </Task>
     </Implementation>
     <ExtendedAttributes />
     <NodeGraphicsInfos>
      <NodeGraphicsInfo ToolId="GeneXus_Business_Process_Modeler" Height="50" Width="130">
       <Coordinates XCoordinate="361" YCoordinate="181" />
      </NodeGraphicsInfo>
     </NodeGraphicsInfos>
    </Activity>
   </Activities>
   <Transitions />
  </WorkflowProcess>
</WorkflowProcesses>
</Package>
```

{{Category:GeneXus X Evolution 2 Help}}}


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [GeneXus Business Process Modeler](https://wiki.genexus.com/commwiki/wiki?20259) |

---
