---
title: "HowTo: Work With Organizational Units"
source_id: 13650
source_url: https://wiki.genexus.com/commwiki/wiki?13650
genexus_version: "18"
---

# HowTo: Work With Organizational Units

This document explains how to work with Organizational Units and provides a brief overview about it.

This is an example of how organizational units are used:

### [Step 1](#Step+1)

Create a definition of what the Organizational Unit represents, for example, Agencies or Branches.

This is done from Organizational Model > Organizational Unit Definitions, as shown in the image below:

`[imagen omitida: wiki id 53813]`

Pressing the New button opens the following dialog box:

`[imagen omitida: wiki id 53814]`

It can be defined as *Propagable*, which means that the user's organizational unit will be inherited by the process. That is to say, when a user that belongs to branch "A" starts a process instance, it will be restricted to that branch and therefore branch "B" will not see that instance.

This property also indicates that subprocesses will inherit the same restriction of the parent instance.

Once the definition has been created, the values that this definition can take should be defined. In this case, they could be BRANCH A, B, C, etc. In order to do so, organizational units based on the previously created definition have to be created.

To this end, go to Organizational Model  > Organizational Units as shown in the image below:

`[imagen omitida: wiki id 53815]`

### [Step 2](#Step+2)

Next, the users have to be assigned to the Organizational Units, to specify in which branch each one works. To do so, select the organizational unit and assign the users by pressing the Members button.

`[imagen omitida: wiki id 53816]`

If you don't want to use the Propagable property but want to assign the organizational units to the process instances, you should do so through the API using the AssignOrganizationalUnit method of the process instance, for example, with the following code:

```
&WorkflowOrganizationalUnit.Load(<organizational_definition_name>, organizational_unit_name>)

&WorkflowProcessInstance.AssignOrganizationalUnit(&WorkflowOrganizationalUnit)
```

**Where:**

*&WorkflowProcessInstance*  
        Is a variable of the WorkflowProcessInstance type.

*&WorkflowOrganizationalUnit*  
        Is a variable of the WorkflowOrganizationalUnit type.

### [See Also](#See+Also)

[GXflow Organizational Units Definitions](https://wiki.genexus.com/commwiki/wiki?10195)  
[GXflow Organizational Units](https://wiki.genexus.com/commwiki/wiki?10196)


|  |
| --- |
| **Backlinks** |
| [GXflow Organizational Units](https://wiki.genexus.com/commwiki/wiki?10196) | [GXflow Organizational Units Definitions](https://wiki.genexus.com/commwiki/wiki?10195) |

---
