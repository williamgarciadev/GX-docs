---
title: "GXflow attributes description"
source_id: 27250
source_url: https://wiki.genexus.com/commwiki/wiki?27250
genexus_version: "18"
---

# GXflow attributes description

This document describes the different attributes of GXflow.

#### [Process definition](#Process+definition)

| Attribute | Type | Description |
| --- | --- | --- |
| WFPrcId | Numeric (6.0) | Process version ID |
| WFPrcName | Character (100) | Process name |
| WFPrcDsc | Character (254) | Process description |
| WFPrcCreated | DateTime | Creation date |
| WFPrcEnb | [CBool (enum)](https://wiki.genexus.com/commwiki/wiki?27267,,) | Process enabled |
| WFPrcEstDur | Numeric (10) | Estimated duration of the process |
| WFPrcUID | Character (40) | Process ID |

### [Process Instances](#Process+Instances)

| Attribute | Type | Description |
| --- | --- | --- |
| WFInsPrcId | Numeric (10) | Instance ID |
| WFInsPrcSubject | Character (120) | Short description |
| WFInsPrcInit | DateTime | Creation date |
| WFInsPrcEnd | DateTime | End date |
| WFInsPrcOSta | [NBool (enum)](https://wiki.genexus.com/commwiki/wiki?27267,,) | Active process instance |
| WFInsPrcSta | Instance process status (enum) | Process instance status |
| WFInsPrcDur | Numeric (10) | Process instance duration in seconds (finished instances) |
| WFInsPrcWarn | [CBool (enum)](https://wiki.genexus.com/commwiki/wiki?27267,,) | Warning occurrence indicator |
| WFInsPrcDeadline | [CBool (enum)](https://wiki.genexus.com/commwiki/wiki?27267,,) | Deadline occurrence indicator |
| WFInsPrcWrnTime | DateTime | Warning occurrence date |
| WFInsPrcDlnTime | DateTime | Deadline occurrence date |
| WFInsPrcPty | [Priority (enum)](https://wiki.genexus.com/commwiki/wiki?27267,,) | Priority |

### [Task definition](#Task+definition)

| Attribute | Type | Description |
| --- | --- | --- |
| WFTaskCod | Numeric (4.0) | Task ID |
| WFTaskName | Character (100) | Task name |
| WFTaskDsc | Character (254) | Task description |
| WFTaskCls | [TaskType (enum)](https://wiki.genexus.com/commwiki/wiki?27267,,) | Task Type |
| WFTaskEstDur | Numeric (10) | Estimated duration of the task |

### [Task Instances (WorkItems)](#Task+Instances+%28WorkItems%29)

| Attribute | Type | Description |
| --- | --- | --- |
| WFItemId | Numeric (10) | WorkItem ID |
| WFItemInit | DateTime | Creation date |
| WFItemEnd | DateTime | End date |
| WFItemDur | Numeric (10) | WorkItem duration in seconds (finished WorkItems) |
| WFItemStsAct | [NBool (enum)](https://wiki.genexus.com/commwiki/wiki?27267,,) | Active or closed |
| WFStsCod | [WorkItemStatus (enum)](https://wiki.genexus.com/commwiki/wiki?27267,,) | Status |
| WFItemUsrCod | Character (40) | ID of the assigned user |
| WFItemUsrName | Character (100) | Name of the assigned user |
| WFItemWarn | [CBool (enum)](https://wiki.genexus.com/commwiki/wiki?27267,,) | Warning occurrence indicator |
| WFItemDln | [CBool (enum)](https://wiki.genexus.com/commwiki/wiki?27267,,) | Deadline occurrence indicator |
| WFItemWrnTime | DateTime | Warning occurrence date |
| WFItemDlnTime | DateTime | Deadline occurrence date |
| WFItemPty | [Priority (enum)](https://wiki.genexus.com/commwiki/wiki?27267,,) | Priority |

### [Application Data](#Application+Data)

| Attribute | Type | Description |
| --- | --- | --- |
| WFAttId | Character (50) | Name of the application data |
| WFAttSVal | Character (50) | Value if it is shorter than 50 characters |
| WFAttBVal | Long Var Char (9999) | Value if it is longer than 50 characters |

### [Users](#Users)

| Attribute | Type | Description |
| --- | --- | --- |
| WFUsrCod | Character (40) | User ID |
| WFUsrName | Character (100) | User name |
| WFUsrBloc | [NBool (enum)](https://wiki.genexus.com/commwiki/wiki?27267,,) | Locked user |
| WFUsrOut | [NBool (enum)](https://wiki.genexus.com/commwiki/wiki?27267,,) | User out of office |
| WFUsrDel | [NBool (enum)](https://wiki.genexus.com/commwiki/wiki?27267,,) | Deleted user |
| WFUsrLstCon | DateTime | Last connection date |

### [Roles](#Roles)

| Attribute | Type | Description |
| --- | --- | --- |
| WFRolCod | Numeric (6.0) | Role ID |
| WFRolDsc | Character (100) | Role description |

### [Organizational Unit Definitions](#Organizational+Unit+Definitions)

| Attribute | Type | Description |
| --- | --- | --- |
| WFRstCod | Character (40) | Organizational Unit definition name |
| WFRstDsc | Character (254) | Organizational Unit definition description |

### [Organizational Units](#Organizational+Units)

| Attribute | Type | Description |
| --- | --- | --- |
| WFRstValue | Character (40) | Organizational Unit name |
| WFRstValDsc | Character (254) | Organizational Unit description |

### [Important](#Important)

* WFItemUsrCod (WorkItems) is a sub-type of WFUsrCod (Users)
* WFItemUsrName (WorkItems) is a sub-type of WFUsrName (Users)

### [See also](#See+also)

* [GXflow domains definitions](https://wiki.genexus.com/commwiki/wiki?27267,,)
* [HowTo: Set up GXflow metadata on GXquery 4.0](https://wiki.genexus.com/commwiki/wiki?27241,,)
