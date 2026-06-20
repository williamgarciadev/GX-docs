---
title: "WorkflowOrganizationalModel data type"
source_id: 10266
source_url: https://wiki.genexus.com/commwiki/wiki?10266
genexus_version: "18"
---

# WorkflowOrganizationalModel data type

Represents the company's organizational model and it is provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| Error | [WorkflowError](https://wiki.genexus.com/commwiki/wiki?10283) | Read | Error code |

### [Methods](#Methods)

#### **List Users**

This method returns a collection with all the organization's users matching the specified filter.  
ListUsers (filter): Collection ([WorkflowUser](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?10268,,))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | filter | [WorkflowFilter](https://wiki.genexus.com/commwiki/wiki?10282) Valid Filters : Role, Name, ProcessInstance, OrganizationalUnit | Input | Filter |

#### **ListUsersOrderBy**

This method returns a collection with all the organization's users matching the specified filter in the specified order.  
ListUsersOrderBy (filter, order): Collection ([WorkflowUser](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?10268,,))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | filter | [WorkflowFilter](https://wiki.genexus.com/commwiki/wiki?10282) Valid Filters: Role, Name, ProcessInstance, OrganizationalUnit | Input | Filter |
| 2 | order | [WorkflowOrder](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?10294,,) (WorkflowOrder.ID\_ASC,  WorkflowOrder.ID\_DESC,  WorkflowOrder.NAME\_ASC,  WorkflowOrder.NAME\_DESC) | Input | Order |

#### **ListRoles**

This method returns a collection with the organization functional roles matching the specified filter.  
ListRoles (filter): Collection ([WorkflowRole](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?10267,,))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | filter | [WorkflowFilter](https://wiki.genexus.com/commwiki/wiki?10282) Valid Filters: User, Activity, Process Definition, Name | Input | Filter |

#### [**ListRolesOrderBy**](#ListRolesOrderBy)

This method returns a collection with the organization's functional roles matching the specified filter in the specified order.  
ListRolesOrderBy (filter, order): Collection ([WorkflowRole](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?10267,,))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | ****Movement**** | **Description** |
| 1 | filter | [WorkflowFilter](https://wiki.genexus.com/commwiki/wiki?10282) Valid Filters: User, Activity, Process Definition, Name | Input | Filter |
| 2 | order | [WorkflowOrder](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?10294,,) (WorkflowOrder.NAME\_ASC, WorkflowOrder.NAME\_DESC) | Input | Order |

#### [**ListRestrictionDefinitions (Deprecated)**](#ListRestrictionDefinitions+%28Deprecated%29)

This method returns a collection with the restriction definitions matching the specified filter.  
ListRestrictionDefinitions (filter): Collection ([WorkflowRestrictionDefinition](https://wiki.genexus.com/commwiki/wiki?12192))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Name | Type | ****Movement**** | **Description** |
| 1 | filter | [WorkflowFilter](https://wiki.genexus.com/commwiki/wiki?10282) Valid Filters: None | Input | Filter |

#### [**ListRestrictionDefinitionsOrderBy (Deprecated)**](#ListRestrictionDefinitionsOrderBy+%28Deprecated%29)

This method returns a collection with the restriction definitions matching the specified filter in the specified order.  
ListRestrictionDefinitionsOrderBy (filter, order): Collection ([WorkflowRestrictionDefinition](https://wiki.genexus.com/commwiki/wiki?12192))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | ****Movement**** | **Description** |
| 1 | filter | [WorkflowFilter](https://wiki.genexus.com/commwiki/wiki?10282) Valid Filters : None | Input | Filter |
| 2 | order | [WorkflowOrder](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?10294,,) (WorkflowOrder.ID\_ASC,  WorkflowOrder.ID\_DESC,  WorkflowOrder.NAME\_ASC,  WorkflowOrder.NAME\_DESC) | Input | Order |

#### [**ListRestrictions (Deprecated)**](#ListRestrictions+%28Deprecated%29)

This method returns a collection with the restrictions matching the specified filter.  
ListRestrictions (filter): Collection ([WorkflowRestriction](https://wiki.genexus.com/commwiki/wiki?12191))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | filter | [WorkflowFilter](https://wiki.genexus.com/commwiki/wiki?10282) Valid Filters : Restriction | Input | Filter |

#### [**ListRestrictionsOrderBy (Deprecated)**](#ListRestrictionsOrderBy+%28Deprecated%29)

This method returns a collection with the restrictions matching the specified filter in the specified order.  
ListRestrictionsOrderBy (filter, order): Collection ([WorkflowRestriction](https://wiki.genexus.com/commwiki/wiki?12191))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | filter | [WorkflowFilter](https://wiki.genexus.com/commwiki/wiki?10282) Valid Filters: Restriction | Input | Filter |
| 2 | order | [WorkflowOrder](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?10294,,) (WorkflowOrder.ID\_ASC, WorkflowOrder.ID\_DESC, WorkflowOrder.NAME\_ASC,   WorkflowOrder.NAME\_DESC) | Input | Order |

#### [**GetUserById**](#GetUserById)

This method returns a User type object whose identifier coincides with the specified one.  
GetUserById (id): [WorkflowUser](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?10268,,)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | id | [WorkflowUserId](https://wiki.genexus.com/commwiki/wiki?15734) | Input | User Identifier |

#### [**GetUserByName**](#GetUserByName)

This method returns the first User type object whose name coincides with the specified one.  
GetUserByName (name): [WorkflowUser](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?10268,,)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | name | [WorkflowName](https://wiki.genexus.com/commwiki/wiki?15734) | Input | User name |

#### [**GetRoleById**](#GetRoleById)

This method returns a Role type object whose identifier coincides with the specified one.  
GetRoleById (id): [WorkflowRole](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?10267,,)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | ****Movement**** | **Description** |
| 1 | Id | [WorkflowRoleId](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Role Identifier |

#### [**GetRoleByName**](#GetRoleByName)

This method returns the first Role type object whose name coincides with the specified one.  
GetRoleByName (name): [WorkflowRole](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?10267,,)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | name | [WorkflowName](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Role name |

#### [**GetRoleWithGUID**](#GetRoleWithGUID)

This method returns a Role type object whose GUID coincides with the specified one.  
GetRoleWithGUID (GUID): [WorkflowRole](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?10267,,)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | ****Movement**** | **Description** |
| 1 | GUID | Character | Input | RoleGUID |

#### [**GetRestrictionDefinitionByName** (Deprecated)](#GetRestrictionDefinitionByName+%28Deprecated%29)

This method returns the first Restriction Definition type object whose name coincides with the specified one.  
GetRestrictionDefinitionByName (name): [WorkflowRestrictionDefinition](https://wiki.genexus.com/commwiki/wiki?12192)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | Name | [WorkflowName](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Name of restriction definition |

#### [**AddUser**](#AddUser)

This method adds a new user to the organization.  
AddUser (id, name, email, accessLevel, password): [WorkflowUser](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?10268,,)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | id | [WorkflowUserId](https://wiki.genexus.com/commwiki/wiki?15734) | Input | User Identifier (login) |
| 2 | name | [WorkflowName](https://wiki.genexus.com/commwiki/wiki?15734) | Input | User Name |
| 3 | email | [WorkflowEmail](https://wiki.genexus.com/commwiki/wiki?15734) | Input | E-mail address |
| 4 | password | [WorkflowPassword](https://wiki.genexus.com/commwiki/wiki?15734) | Input | User Password |

#### [**AddRole**](#AddRole)

This method adds a new role to the organization.  
AddRole (name): [WorkflowRole](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?10267,,)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | name | [WorkflowName](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Rol Name |

#### [**AddRestrictionDefinition (Deprecated)**](#AddRestrictionDefinition+%28Deprecated%29)

This method adds a new restriction definition.  
AddRestrictionDefinition (name, description, type): WorkflowRestrictionDefinition

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | name | [WorkflowName](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Restriction Name |
| 2 | description | [WorkflowDescription](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Restriction Description |
| 3 | type | [WorkflowRestrictionDefinitionType](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?10294,,) | Input | Restriction Type |

#### [**GetOrganizationalUnitDefinitionByName**](#GetOrganizationalUnitDefinitionByName+)

This method returns an organizational unit definition by name.  
GetOrganizationalUnitDefinitionByName(name): [WorkflowOrganizationalUnitDefinition](https://wiki.genexus.com/commwiki/wiki?10269)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Pasaje** | **Description** |
| 1 | name | [WorkflowName](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Name |

#### [**GetOrganizationalUnitByName**](#GetOrganizationalUnitByName+)

This method returns an organizational unit by name.  
GetOrganizationalUnitByName(name): [WorkflowOrganizationalUnit](https://wiki.genexus.com/commwiki/wiki?10270)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | name | [WorkflowName](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Name |

#### [**ListOrganizationalUnitDefinitions**](#ListOrganizationalUnitDefinitions+)

This method lists the organizational units definitions.  
ListOrganizationalUnitDefinitions (filter): Collection ([WorkflowOrganizationalUnitDefinition](https://wiki.genexus.com/commwiki/wiki?10269))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | filter | [WorkflowFilter](https://wiki.genexus.com/commwiki/wiki?10282) | Input | Filter |

#### [**ListOrganizationalUnitDefinitionsOrderBy**](#ListOrganizationalUnitDefinitionsOrderBy+)

This method lists the organizational units definitions. It is possible to sort the result.  
ListOrganizationalUnitDefinitions (filter, order): Collection ([WorkflowOrganizationalUnitDefinition](https://wiki.genexus.com/commwiki/wiki?10269))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Name | **Type** | **Movement** | **Description** |
| 1 | filter | [WorkflowFilter](https://wiki.genexus.com/commwiki/wiki?10282) | Input | Filter |
| 2 | Order | [WorkflowOrder](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?10294,,) | Input | Order |

#### [**ListOrganizationalUnits**](#ListOrganizationalUnits+)

This method lists the organizational units.  
ListOrganizationalUnits (filter): Collection ([WorkflowOrganizationalUnit](https://wiki.genexus.com/commwiki/wiki?10270))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | Filter | [WorkflowFilter](https://wiki.genexus.com/commwiki/wiki?10282) Valid Filters: Start, Limit | Input | Filter |

#### [**ListOrganizationalUnitsOrderBy**](#ListOrganizationalUnitsOrderBy)

This method returns the organizational units list. It is possible to sort the result.  
ListOrganizationalUnitsOrderBy (filter, order): Collection ([WorkflowOrganizationalUnit](https://wiki.genexus.com/commwiki/wiki?10270))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | filter | [WorkflowFilter](https://wiki.genexus.com/commwiki/wiki?10282) Valid Filters: Start, Limit | Input | Filter |
| 2 | Order | [WorkflowOrder](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?10294,,) | Input | Order |

#### [**AddOrganizationalUnitDefinition**](#AddOrganizationalUnitDefinition)

 This method adds an organizational unit definition.  
AddOrganizationalUnitDefinition(name,description, propagable): [WorkflowOrganizationalUnitDefinition](https://wiki.genexus.com/commwiki/wiki?10269)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | name | [WorkflowName](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Name |
| 2 | description | [WorkflowDescription](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Description |
| 3 | propagable | Boolean | Input | Indicates that the user's organizational unit will be inherited by the process |

#### [**AddOrganizationalUnit**](#AddOrganizationalUnit)

 This method adds an organizational unit.  
AddOrganizationalUnit(definition name, name,description): [WorkflowOrganizationalUnit](https://wiki.genexus.com/commwiki/wiki?10270)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | definition name | [WorkflowName](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Definition Name |
| 2 | name | [WorkflowName](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Name |
| 3 | description | [WorkflowDescription](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Description |

#### 

#### [**RemoveUser**](#RemoveUser)

This method allows to remove a user.  
RemoveUser(user)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | user | [WorkflowUser](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?10268,,) | Input | User to be removed |

#### [**RemoveRole**](#RemoveRole)

This method allows to remove a role.  
RemoveRole(role)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | role | [WorkflowRole Data Type](https://wiki.genexus.com/commwiki/wiki?17230) | Input | Role to be removed |

#### [**ListApplicationRoles**](#ListApplicationRoles)

This method returns a collection with the user roles matching the specified filter. It does not include the roles created from the [GeneXus IDE](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?5587,,).  
ListApplicationRoles (filter): Collection ([WorkflowRole](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?10267,,))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | filter | [WorkflowFilter](https://wiki.genexus.com/commwiki/wiki?10282) Valid Filters: User, Activity, Process Definition, Name | Input | Filter |

#### [**ListApplicationRolesOrderBy**](#ListApplicationRolesOrderBy)

This method returns a collection with the user roles matching the specified filter in the specified order. It does not include the roles created from the GeneXus IDE.  
ListApplicationRolesOrderBy (filter, order): Collection ([WorkflowRole](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?10267,,))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | ****Movement**** | **Description** |
| 1 | filter | [WorkflowFilter](https://wiki.genexus.com/commwiki/wiki?10282) Valid Filters: User, Activity, Process Definition, Name | Input | Filter |
| 2 | order | [WorkflowOrder](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?10294,,) (WorkflowOrder.NAME\_ASC, WorkflowOrder.NAME\_DESC) | Input | Order |

### [See Also](#See+Also)

[Workflow Error Codes](https://wiki.genexus.com/commwiki/wiki?11746)


|  |
| --- |
| **Backlinks** |
| [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) |

---
