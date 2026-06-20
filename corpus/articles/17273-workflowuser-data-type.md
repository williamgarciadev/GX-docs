---
title: "WorkflowUser Data Type"
source_id: 17273
source_url: https://wiki.genexus.com/commwiki/wiki?17273
genexus_version: "18"
---

# WorkflowUser Data Type

This data type, that it is provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350), represents a user of the organization.

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| Id | [WorkflowUserId](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Identifier (Login) |
| Name | [WorkflowName](https://wiki.genexus.com/commwiki/wiki?15734) | Read/ Write | Name |
| Email | [WorkflowEmail](https://wiki.genexus.com/commwiki/wiki?15734) | Read/ Write | E-mail address |
| Password | [WorkflowPassword](https://wiki.genexus.com/commwiki/wiki?15734) | Write | Password |
| Workload | Numeric | Read | Number of pending tasks |
| isConnected | Boolean | Read | Indicates if the user is connected |
| isBlocked | Boolean | Read | Indicates if the user is blocked |
| isOutOfOffice | Boolean | Read | Indicates if the user is out of office |
| isRebuildRequired | Boolean | Read | Indicates if the user worklist needs a rebuild |
| Roles | Collection ([WorkflowRole](https://wiki.genexus.com/commwiki/wiki?10267,,)) | Read | Associated functional roles |
| OrganizationalUnits | Collection ([WorkflowOrganizationalUnits](https://wiki.genexus.com/commwiki/wiki?10270)) | Read | Associated User Organizational Units |
| Error | [WorkflowError](https://wiki.genexus.com/commwiki/wiki?10283) | Read | Error |
| Access Level | [WorkflowAccessLevel](https://wiki.genexus.com/commwiki/wiki?10294,,) | Read | User Access Level |
| Restrictions (Deprecated) | Collection ([WorkflowRestriction](https://wiki.genexus.com/commwiki/wiki?12191)) | Read | Associated restrictions |
| Substitute | [WorkflowUser](https://wiki.genexus.com/commwiki/wiki?10268,,) | Read | Substitute User |
| LastGetWorklistCount | Numeric | Read | Returns the total number of records in the last call to the GetWorklist\* method ignoring paging filters if any (available since [GeneXus 16 upgrade 6](https://wiki.genexus.com/commwiki/wiki?43978,,)). |
| Settings | Collection ([WorkflowSetting](https://wiki.genexus.com/commwiki/wiki?15084)) | Read | Returns a Collection of WorkflowSettings for this User (available since [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242)) |

### [Methods](#Methods)

* **GetWorklist**

This method allows recovering the user Worklist matching the specified filter and in the specified order.  
The LastGetWorklistCount property is updated after executing the *GetWorklist* method with the total number of records, ignoring paging filters if any.

GetWorklist (filter): Collection (WorkflowWorkitem)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| filter | WorkflowFilter Valid Filters: Start, Limit, CreatedFrom, CreatedTo, State, ProcessInstance, Subject, ProcessDefinition, Activity, Role, Priority, WithWarning, Search, OrganizationalUnit, SetOrganizationalUnit, ApplicationDataName, ApplicationDataValue, SetApplicationData | Input | Filter |

Note: (\*) (\*\*)

* **GetWorklistOrderBy**

This method allows recovering the user Worklist matching the specified filter and in the specified order.  
The LastGetWorklistCount property is updated with the total number of records, ignoring paging filters if any.

GetWorklistOrderBy (filter, order): Collection (WorkflowWorkitem)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| filter | WorkflowFilter Valid Filters: Start, Limit, CreatedFrom, CreatedTo, State, ProcessInstance, Subject, ProcessDefinition, Activity, User, Role, Priority, WithWarning, Search, OrganizationalUnit, SetOrganizationalUnit, ApplicationDataName, ApplicationDataValue, SetApplicationData | Input | Filter |
| order | Numeric (WorkflowOrder.ID\_ASC, WorkflowOrder.ID\_DESC, WorkflowOrder.CREATED\_ASC, WorkflowOrder.CREATED\_DESC, WorkflowOrder.PRIORITY\_ASC, WorkflowOrder.PRIORITY\_DESC, WorkflowOrder.STATE\_ASC, WorkflowOrder.STATE\_DESC, WorkflowOrder.WITH\_WARNING\_ASC, WorkflowOrder.WITH\_WARNING\_DESC, WorkflowOrder.SUBJECT\_ASC, WorkflowOrder.SUBJECT\_DESC, WorkflowOrder.ACTIVITY\_ASC, WorkflowOrder.ACTIVITY\_DESC) | Input | Order |

Note: (\*) (\*\*)

* **ListCreatableProcessDefinitions**

This method returns a collection with the processes definitions based on which the user may create new instances matching the specified filters.

ListCreatableProcessDefinitions (filter): Collection (WorkflowProcessDefinition)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| filter | WorkflowFilter Valid Filters: Start, Limit, Name | Input | Filter |

Note: (\*)

* **ListCreatableProcessDefinitionsOrderBy**

This method returns a collection with the process definitions based on which the user may create new instances matching the specified filters in the specified order.

ListCreatableProcessDefinitionsOrderBy (filter, order): Collection (WorkflowProcessDefinition)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| filter | WorkflowFilter Valid Filters: Start, Limit, Name | Input | Filter |
| order | Numeric (WorkflowOrder.ID\_ASC, WorkflowOrder.ID\_DESC, WorkflowOrder.NAME\_ASC, WorkflowOrder.NAME\_DESC) | Input | Order |

Note: (\*)

* **GetOrganizationalUnitRoles**

This method allows getting the roles associated with an organizational unit.

GetOrganizationalUnitRoles (organizationalUnit): Collection (WorkflowRole)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| organizationalUnit | [WorkflowOrganizationalUnit](https://wiki.genexus.com/commwiki/wiki?10270) | Input | Reference Organizational Unit |

* **AssignRole**

This method allows assigning a role to the user.

AssignRole (role)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| role | [WorkflowRole](https://wiki.genexus.com/commwiki/wiki?10267,,) | Input | Role to be added |

* **AssignRoleToOrganizationalUnit**

This method allows assigning organizational units to a role.

AssignRoleToOrganizationalUnit (organizationalUnit, role)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| organizationalUnit | [WorkflowOrganizationalUnit](https://wiki.genexus.com/commwiki/wiki?10270) | Input | Organizational Unit |
| Role | [WorkflowRole](https://wiki.genexus.com/commwiki/wiki?10267,,) | Input | Role to be added |

* **UnassignRole**

This method allows to unassign a role to the user.

UnassignRole (role)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Role | [WorkflowRole](https://wiki.genexus.com/commwiki/wiki?10267,,) | Input | Role to be eliminated |

* **UnassignRoleFromOrganizationalUnit**

This method allows unassigning roles from an organizational unit.

UnassignRoleFromOrganizationalUnit (organizationalUnit)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| organizationalUnit | [WorkflowOrganizationalUnit](https://wiki.genexus.com/commwiki/wiki?10270) | Input | Organizational Unit to be eliminated |

* **AssignOrganizationalUnit**

This method allows assigning organizational units to the user.

AssignOrganizationalUnit (organizationalUnit)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| organizationalUnit | [WorkflowOrganizationalUnit](https://wiki.genexus.com/commwiki/wiki?10270) | Input | Organizational Unit to be added |

* **UnassignOrganizationalUnit**

This method allows unassigning an organizational unit from the user.

UnassignOrganizationalUnit (organizationalUnit)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| organizationalUnit | [WorkflowOrganizationalUnit](https://wiki.genexus.com/commwiki/wiki?10270) | Input | Organizational Unit to be eliminated |

* **RebuildWorklist**

This method rebuilds the worklist of a user.

RebuildWorklist ()

* **Block**

Locks the user

Block ()

* **Unblock**

Unlocks the user

Unblock ()

* **ResetPassword**

This method allows changing the password to a fixed password: "1234".

ResetPassword ()

* **ResetPasswordByMail**

This method generates a random password and emails it to the user.

ResetPasswordByMail ()

* **ChangePassword**

This method allows updating the user password.

ChangePassword (currentPassword, newPassword)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| currentPassword | Character | Input | Actual Password |
| newPassword | Character | Input | New Password |

* **AddRole (Deprecated)**

This method adds a functional role to the user.

AddRole (role)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| role | [WorkflowRole](https://wiki.genexus.com/commwiki/wiki?10267,,) | Input | Role to be added |

* **RemoveRole (Deprecated)**

This method allows dissociating a functional role from the user.

RemoveRole (role)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| role | [WorkflowRole](https://wiki.genexus.com/commwiki/wiki?10267,,) | Input | Role to be eliminated |

* **AddRestriction (Deprecated)**

This method allows adding a restriction to the user or to a specific role of the user (in case this role is specified).

AddRestriction(restriction, role)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| restriction | WorkflowRestriction | Input | Restriction to add |
| role | 0 / [WorkflowRole](https://wiki.genexus.com/commwiki/wiki?10267,,) | Input | If the value is 0, the restriction is added to the user (applies to all the user roles). If not, the restriction is added to the specified role. |

* **RemoveRestriction (Deprecated)**

This method allows removing a restriction from the user or from a specific user role (in case this role is specified).

RemoveRestriction (restriction, role)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| restriction | WorkflowRestriction | Input | Restriction to be eliminated |
| role | 0 / [WorkflowRole](https://wiki.genexus.com/commwiki/wiki?10267,,) | Input | If the value is 0, the restriction is eliminated at user level. If not the restriction is eliminated to the role specified. |

* **SetOutOfOffice**

This method allows updating the user's availability status.

SetOutOfOffice (startDate, ReturnDate, message, substitute)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| startDate | [Date](https://wiki.genexus.com/commwiki/wiki?7373) | Input | Indicates when starts being out of the office |
| returnDate | [Date](https://wiki.genexus.com/commwiki/wiki?7373) | Input | Indicates when returns to the office |
| message | [WorkflowMessage](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Allows to leave a message |
| substitute | [WorkflowUser](https://wiki.genexus.com/commwiki/wiki?10268,,) | Input | Indicates who is the substitute |

* **SetSettingValue**

This method allows modifying the value of a setting for the current user.

SetSettingValue(Id, Value)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Id | [WorkflowSettingId](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Workflow Setting identifier |
| Value | [WorkflowValue](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Value |

* **GetSettingById**

This method returns a [Workflow Setting](https://wiki.genexus.com/commwiki/wiki?15084) whose identifier coincides with the specified one.

GetSettingById (Id) : WorkflowSetting

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Id | WorkflowSettingId | Input | Workflow Setting identifier |

Note: (\*\*\*)

* **DisableOutOfOffice**

This method sets the user's status "in office". Beware task in substitute user's worklist will not be removed with this method, a RebuildWorklist is needed.

DisableOutOfOffice ()

(\*) Depends on [Fetch and Max Fetch properties.](https://wiki.genexus.com/commwiki/wiki?10119)

(\*\*) It only works with users obtained by [Connected User](https://wiki.genexus.com/commwiki/wiki?11671)

(\*\*\*) Currently, startDate must be set to today's date for the state change to take effect.

### [See Also](#See+Also)

[Workflow Error Codes](https://wiki.genexus.com/commwiki/wiki?11746)


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242) | [GXflow limits](https://wiki.genexus.com/commwiki/wiki?26716) |
| [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) | [WorkflowDataChangeEvent Data Type](https://wiki.genexus.com/commwiki/wiki?10278) | [WorkflowOrganizationalUnit Data Type](https://wiki.genexus.com/commwiki/wiki?10270) | [WorkflowProcessInstance Data Type](https://wiki.genexus.com/commwiki/wiki?17771) |

---
