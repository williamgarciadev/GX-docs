---
title: "WorkflowWorkitem Data Type"
source_id: 11731
source_url: https://wiki.genexus.com/commwiki/wiki?11731
genexus_version: "18"
---

# WorkflowWorkitem Data Type

This Data Type, provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350), represents the execution of an activity in the context of a process instance (it is the equivalent of a task in the GXflow inbox).

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| Id | Numeric | Read | Identifier |
| ProcessDefinition | [WorkflowProcessDefinition](https://wiki.genexus.com/commwiki/wiki?11698,,) | Read | Process Definition |
| ProcessDefinitionId | Numeric | Read | Identifier of the process definition |
| Priority | Numeric ([WorkflowPriority](https://wiki.genexus.com/commwiki/wiki?10294,,)) | Read/ Write | Priority |
| Comments | Character | Read/ Write | Associated comments |
| State | Character | Read | State |
| Created | DateTime | Read | Creation date |
| Ended | DateTime | Read | Ending date |
| WarningTime | DateTime | Read/Write | Deadline warning date and time |
| DeadlineTime | DateTime | Read/Write | Deadline date and time |
| Activity | [WorkflowActivity](https://wiki.genexus.com/commwiki/wiki?10263,,) | Read | Activity |
| ActivityId | Numeric | Read | Activity Identifier |
| ProcessInstance | [WorkflowProcessInstance](https://wiki.genexus.com/commwiki/wiki?11702,,) | Read | Process Instance |
| ProcessInstanceId | Numeric | Read | Process instance identifier |
| isSubprocess | Boolean | Read | Indicates if it is a subprocess |
| isDocumentActionAuthorized | Boolean | Read | Indicates if a document action is authorized |
| isDocumentActionRequired | Boolean | Read | Indicates if a document action is needed |
| Subprocess | [WorkflowProcessInstance](https://wiki.genexus.com/commwiki/wiki?11702,,) | Read | Associated Subprocess |
| Participant | [WorkflowUser](https://wiki.genexus.com/commwiki/wiki?10268,,) | Read | Participant User (that has the workitem assigned) |
| ParticipantCandidates | Collection ([WorkflowUser](https://wiki.genexus.com/commwiki/wiki?10268,,)) | Read | Candidate users to participate in the workitem execution |
| DocumentInstances | Collection ([WorkflowDocumentInstance](https://wiki.genexus.com/commwiki/wiki?10273,,)) | Read | Associated document instances |
| States | Collection Character([WorkflowWorkitemState](https://wiki.genexus.com/commwiki/wiki?10294,,)) | Read | States that a workitem may take |
| Collaborators | Collection ([WorkflowUser](https://wiki.genexus.com/commwiki/wiki?10268,,)) | Read | It returns the list of users that participate in the workitem execution |
| Index | Numeric | Read | Workitem index when the task defining it is array type |
| PreviousActivity | [WorkflowActivity](https://wiki.genexus.com/commwiki/wiki?10263,,) | Read | Activity that was executed before |
| Previous | [WorkflowWorkitem](https://wiki.genexus.com/commwiki/wiki?11731) | Read | Workitem that was executed before |
| Error | [WorkflowError](https://wiki.genexus.com/commwiki/wiki?10283) | Read | Error |
| NodeInstance | [WorkflowNodeInstance](https://wiki.genexus.com/commwiki/wiki?27137) | Read | Node instance associated with the workitem |
| Duration | Numeric | Read | Workitem active time (in seconds) |
| ExtendedAtrributes | [WorkflowAttribute](https://wiki.genexus.com/commwiki/wiki?10271) | Read | Workitem extended attributes |

### [Methods](#Methods)

* **Load**

It allows loading a workitem from its Identifier.

Load (id)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Id | [WorkflowWorkitemId](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Workitem to be loaded identifier |

* **Complete**

Completes the workitem. Before completing the workitem, the method verifies that the corresponding post-conditions are completed. The ideal condition to execute Complete() is when the workitem is in process (open.active.in\_process state; see Workflow States document). Nevertheless, with the purpose of making the use of this method easier, in case the workitem is currently in assignment-pending or assigned state (but not in process), the method takes care of going through the intermediate states before the workitem is considered completed. If the workitem is in assignment-pending state, it is recommended to call the Assign()method previously, so that the user remains registered in the process history.

Complete ()

* **Assign**

Assigns the workitem to the specified user. If the workitem is assigned, it cannot be assigned to another user (in this case, see Reassign method).

Assign (User)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| User | [WorkflowUser](https://wiki.genexus.com/commwiki/wiki?10268,,) | Input | User to which the workitem will be assigned |

* **Unassign**

Unassigns a workitem that was already assigned to a user.

* **Reassign**

Reassigns a workitem that was already assigned to a user, to another user.

Reassign (sourceUser, targetUser)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| sourceUser | [WorkflowUser](https://wiki.genexus.com/commwiki/wiki?10268,,) | Input | User to which the workitem was assigned. |
| targetUser | [WorkflowUser](https://wiki.genexus.com/commwiki/wiki?10268,,) | Input | User to which the workitem will be assigned. |

* **ChangeState**

Changes workitem state. This method only works when the workitem is in certain states, for more information you can read: [Workflow Engine States](https://wiki.genexus.com/commwiki/wiki?17673).

ChangeState (state)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| State | Character ([WorkflowWorkitemState](https://wiki.genexus.com/commwiki/wiki?10294,,)) | Input | State that the workitem will take. |

* **SelectSuccessiveOptionalActivity**

Selects a successive optional activity. Once the workitem is completed, the instances of all the selected successive activities will be created.

SelectSuccesiveOptionalActivity (Activity)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Activity | [WorkflowActivity](https://wiki.genexus.com/commwiki/wiki?10263,,) | Input | Selected Successive Activity |

* **PostConditionFailed**

This method allows the programmer to determine if the postconditions of a task were fulfilled or not. The programmer must evaluate postconditions before the completion of the workitem. This method receives a string as a parameter which is the error message for the user who is attempting to complete the workitem.

PostConditionFailed (Message)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Message | Char | Input | Error Code |

* **Collaborate**

It allows adding collaborators to the workitem.

Collaborate (User) : WorkflowWorkitem

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| User | [WorkflowUser](https://wiki.genexus.com/commwiki/wiki?10268,,) | Input | User to be added as a collaborator |

* **AssignRole**

It allows assigning the workitem to a specified role.

AssignRole (Role)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Role | [WorkflowRole](https://wiki.genexus.com/commwiki/wiki?10267,,) | Input | Role to assign the workitem |

* **Delegate**

This method allows you to delegate a workitem to a specific user.

Delegate (User): WorkflowWorkitem

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| User | [WorkflowUser](https://wiki.genexus.com/commwiki/wiki?10268,,) | Input | User to which the workitem will be displayed |
| Workitem | [WorkflowWorkitem](https://wiki.genexus.com/commwiki/wiki?11731) | Input | Workitem to be delegated |

* **DelegateToRole**

This method allows you to delegate a workitem to a specific role so that all users with this role will be able to see the workitem.

DelegateToRole(Role): WorkflowWorkitem

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Role | [WorkflowRole](https://wiki.genexus.com/commwiki/wiki?10267,,) | Input | Role to which the workitem will be delegated |

* **AddAttribute**

This method allows adding an attribute to the workitem.

AddAttribute(Attribute)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Attribute | [WorkflowAttribute](https://wiki.genexus.com/commwiki/wiki?10271) | Input | Attribute to be added |

* **Skip**

This method allows skipping this workitem.

Skip()

* **Undo**

This method allows undoing this workitem.

Undo()

* **ThrowError**

This method allows throwing a message as an error.

ThrowError(error)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| error | Character | Input | Workitem error |

* **GetAttributeByName**

Returns the Attribute Data type object whose name coincides with the specified one.

GetAttributeByName(name): Attribute

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| name | Character | Input | Attribute name |

* **RemoveAttribute**

Removes an attribute from the process instance.

RemoveAttribute(attribute)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| attribute | [WorkflowAttribute](https://wiki.genexus.com/commwiki/wiki?10271) | Input | Attribute to be removed from the process instance |

### [See Also](#See+Also)

[Workflow Error Codes](https://wiki.genexus.com/commwiki/wiki?11746)


|  |
| --- |
| **Backlinks** |
| [Date expression procedure property](https://wiki.genexus.com/commwiki/wiki?47342) | [HowTo: Creating n instances of a task and automatically assigning them](https://wiki.genexus.com/commwiki/wiki?20635) | [Category:Workflow API](https://wiki.genexus.com/commwiki/wiki?51350) |
| [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) | [Workflow Data Types: Programming best practices](https://wiki.genexus.com/commwiki/wiki?23318) | [WorkflowContext Data Type](https://wiki.genexus.com/commwiki/wiki?12187) | [WorkflowDocumentInstance Data Type](https://wiki.genexus.com/commwiki/wiki?17282) |
| [WorkflowProcessInstance Data Type](https://wiki.genexus.com/commwiki/wiki?17771) | [WorkflowWorkitem Data Type](https://wiki.genexus.com/commwiki/wiki?11731) |

---
