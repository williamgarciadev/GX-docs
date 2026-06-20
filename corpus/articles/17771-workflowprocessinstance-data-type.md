---
title: "WorkflowProcessInstance Data Type"
source_id: 17771
source_url: https://wiki.genexus.com/commwiki/wiki?17771
genexus_version: "18"
---

# WorkflowProcessInstance Data Type

This data type represents the execution of a process definition (it is the equivalent of a process instance in the GXflow inbox). It is provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| Id | [WorkflowProcessInstanceId](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Identifier |
| ProcessDefinition | [WorkflowProcessDefinition](https://wiki.genexus.com/commwiki/wiki?17239) | Read | Process definition |
| ProcessDefinitionId | [WorkflowProcessDefinitionId](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Process definition identifier |
| Subject | [WorkflowSubject](https://wiki.genexus.com/commwiki/wiki?15734) | Read/ Write | Subject |
| Comments | [WorkflowComment](https://wiki.genexus.com/commwiki/wiki?15734) | Read/ Write | Comments |
| Priority | [WorkflowPriority](https://wiki.genexus.com/commwiki/wiki?10294,,) | Read/ Write | Priority |
| Owner | [WorkflowUser](https://wiki.genexus.com/commwiki/wiki?10268,,) | Read/ Write | User that created the instance |
| State | [WorkflowProcessInstanceState](https://wiki.genexus.com/commwiki/wiki?10294,,) | Read | State |
| Created | [DateTime](https://wiki.genexus.com/commwiki/wiki?7370) | Read | Creation date and time |
| Ended | [DateTime](https://wiki.genexus.com/commwiki/wiki?7370) | Read | Ending date and time |
| WarningTime | [DateTime](https://wiki.genexus.com/commwiki/wiki?7370) | Read/ Write | Deadline warning date and time |
| DeadlineTime | [DateTime](https://wiki.genexus.com/commwiki/wiki?7370) | Read/ Write | Deadline date and time |
| hasParent | [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) | Read | Indicates if it is a subprocess |
| Parent | [WorkflowProcessInstance](https://wiki.genexus.com/commwiki/wiki?17771) | Read | Parent process instance |
| hasChildren | [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) | Read | Indicates if it has a subprocesss |
| Children | Collection ([WorkflowProcessInstance](https://wiki.genexus.com/commwiki/wiki?17771)) | Read | Collection with subprocesses of process instance |
| Workitems | Collection ([WorkflowWorkitem](https://wiki.genexus.com/commwiki/wiki?11731)) | Read | Collection with the workitems of the process instance |
| RecursiveWorkitems | Collection ([WorkflowWorkitem](https://wiki.genexus.com/commwiki/wiki?11731)) | Read | Collection with the workitems of the process instance and the workitems of their subprocesss, etc |
| States | Collection ([WorkflowProcessInstanceStates](https://wiki.genexus.com/commwiki/wiki?10294,,)) | Read | States that a process instance may have |
| Restrictions (Deprecated) | Collection ([WorkflowRestriction](https://wiki.genexus.com/commwiki/wiki?12191)) | Read | Associated restrictions, as this property is deprecated use [GXflow Organizational Units](https://wiki.genexus.com/commwiki/wiki?10196). |
| ApplicationData | Collection ([WorkflowApplicationData](https://wiki.genexus.com/commwiki/wiki?10264,,)) | Read | Associated application data |
| DocumentInstances | Collection (WorkflowDocumentInstance) | Read | Associated document instances |
| Participants | Collection ([WorkflowUser](https://wiki.genexus.com/commwiki/wiki?17273)) | Read | Users participating in the process instance |
| Calendar | [WorkflowCalendar](https://wiki.genexus.com/commwiki/wiki?11609) | Read/Write | Calendar associated to process instance |
| ParentWorkitem | [WorkflowWorkitem](https://wiki.genexus.com/commwiki/wiki?11731) | Read | Corresponding workitem in the parent process |
| ActiveWorkitems | Collection ([WorkflowWorkitem](https://wiki.genexus.com/commwiki/wiki?11731)) | Read | It obtains the active workitems of the process instance |
| RecursiveChildren | Collection ([WorkflowProcessInstance](https://wiki.genexus.com/commwiki/wiki?17771)) | Read | Returns all the subprocess associatedto the instance, recursively (children, etc) |
| OrganizationalUnits | Collection ([WorkflowOrganizationalUnit](https://wiki.genexus.com/commwiki/wiki?10270)) | Read | Organizational Units Collection |
| Error | [WorkflowError](https://wiki.genexus.com/commwiki/wiki?10283) | Read | Error |
| BusinessEventInstances | Collection ([WorkflowBusinessEventInstance](https://wiki.genexus.com/commwiki/wiki?12190)) | Read | Business Event Instances associated to the process instance |
| Duration | [WorkflowDuration](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Time in seconds since the process is active |
| ExtendedAtributes | Collection ([WorkflowAttribute](https://wiki.genexus.com/commwiki/wiki?10271) | Read | Process instance's attributes |
| NodeInstances | Collection [WorkflowNodeInstance](https://wiki.genexus.com/commwiki/wiki?27137) | Read | Process instance's nodes |

### [Methods](#Methods)

* **Load**

Allows loading a process instance from the identifier.

Load (id)

* **Start**

Process instance execution starts.

Start ()

* **StartFrom**

Process instance execution starts. The process execution starts as from the specified activity.

StartFrom (activity)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| activity | [WorkflowActivity](https://wiki.genexus.com/commwiki/wiki?10263,,) | Input | Activity with which you want to Start the process instance (must be one of the initial activities) |

* **Suspend**

Suspends the process instance.

Suspend ()

* **Resume**

Resumes the execution of the process instance.

Resume ()

* **Abort**

Aborts the process instance.

Abort ()

* **ChangeState**

Changes process instance states according to the specified value(see documentation on Workflow objects states).

ChangeState (state)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| state | [WorkflowProcessInstanceState](https://wiki.genexus.com/commwiki/wiki?10294,,) | Input | The states that you want to change |

* **GetApplicationDataByName**

Returns the Application Data type object whose name coincides with the specified one.

GetApplicationDataByName (name): applicationData

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| name | Character | Input | Name of the application data |

* **PreasignWorkitem**

It allows preassigning a workitem corresponding to the specified activity. It is considered a previous assignment since the workitem does not need to exist; in the future at the creation of a workitem corresponding to the activity, the workflow engine will make the assignment.

PreassignWorkitem (activity, user)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| activity | [WorkflowActivity](https://wiki.genexus.com/commwiki/wiki?10263,,) | Input | Activity |
| user | [WorkflowUser](https://wiki.genexus.com/commwiki/wiki?10268,,) | Input | User to be assigned |

* **GetWorkitemByActivity**

Returns the workitem object associated to the specified activity. If there is no workitem associated to this activity, an error is received back (801). If there are several workitems associated to the activity, the most recent workitem is received back.

GetWorkitemByActivity (activity): workitem

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| activity | [WorkflowActivity](https://wiki.genexus.com/commwiki/wiki?10263,,) | Input | Activity |

* **GetAttributeByName**

Returns the Attribute Data type object whose name coincides with the specified one.

GetAttributeByName(name): Attribute

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| name | Character | Input | Attribute name |

* **CreateWorkitem**

Creates a workitem associated to the specified activity (\*).

CreateWorkitem (activity): workitem

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| activity | [WorkflowActivity](https://wiki.genexus.com/commwiki/wiki?10263,,) | Input | Activity |

(\*) If there is already a workitem corresponding to the activity in active state, the already existing workitem is returned instead of creating a new one.

* **Reactivate**

Restarts from an activity, a terminated process instance.

Reactivate (activity)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| activity | [WorkflowActivity](https://wiki.genexus.com/commwiki/wiki?10263,,) | Input | Activity to restart |

* **AssignOrganizationalUnit**

Assigns the organizational unit to the process instance.

AssignOrganizationalUnit (organizationalUnit)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| organizationalUnit | [WorkflowOrganizationalUnit](https://wiki.genexus.com/commwiki/wiki?10270) | Input | Unit to be assigned |

* **UnassignOrganizationalUnit**

Unassign the organizational unit to the process instance.

UnassignOrganizationalUnit (organizationalUnit)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| organizationalUnit | [WorkflowOrganizationalUnit](https://wiki.genexus.com/commwiki/wiki?10270) | Input | Unit to be unassigned |

* **AddRestriction**

Adds a restriction to the process instance.

AddRestriction (restriction)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| restriction | [WorkflowRestriction](https://wiki.genexus.com/commwiki/wiki?12191) | Input | Restriction to be added to the process instance |

* **AddAttribute**

Adds an attribute to the process instance.

AddAttribute(attribute)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| attribute | [WorkflowAttribute](https://wiki.genexus.com/commwiki/wiki?10271) | Input | Attribute to be added to the process instance |

* **RemoveRestriction**

Removes a restriction from the process instance.

RemoveRestriction (restriction)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| restriction | [WorkflowRestriction](https://wiki.genexus.com/commwiki/wiki?12191) | Input | Restriction to be removed from the process instance |

* **RemoveAttribute**

Removes an attribute from the process instance.

RemoveAttribute(attribute)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| attribute | [WorkflowAttribute Data Type](https://wiki.genexus.com/commwiki/wiki?10271) | Input | Attribute to be removed from the process instance |

* **ThrowSignal**

Allows to throw a signal to the process instance.

ThrowSignal (signal)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| signal | [WorkflowName](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Signal Name to be thrown |

* **MigrateToActiveVersion**

Allows to migrate a process instance to the active version (available from [GeneXus X Evolution 3 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?29463,,)).

MigrateToActiveVersion ()

### [See Also](#See+Also)

[Workflow Error Codes](https://wiki.genexus.com/commwiki/wiki?11746)


|  |
| --- |
| **Backlinks** |
| [Date expression procedure property](https://wiki.genexus.com/commwiki/wiki?47342) | [Category:Workflow API](https://wiki.genexus.com/commwiki/wiki?51350) | [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) |
| [WorkflowProcessInstance Data Type](https://wiki.genexus.com/commwiki/wiki?17771) |

---
