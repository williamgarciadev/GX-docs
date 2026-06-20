---
title: "HowTo: Manage permissions to execute WW Lists and Panels"
source_id: 18064
source_url: https://wiki.genexus.com/commwiki/wiki?18064
genexus_version: "18"
---

# HowTo: Manage permissions to execute WW Lists and Panels

This article presents an example that gives permissions so that only authorized users can execute a [List](https://wiki.genexus.com/commwiki/wiki?15984) and its corresponding [Detail](https://wiki.genexus.com/commwiki/wiki?15985) of a [Work With object](https://wiki.genexus.com/commwiki/wiki?15974). The idea for [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s is the same.

**Note**: It is not possible to manage the List and Detail permissions independently (or all the sections of the Detail). That is to say, the permissions apply to all or none of them as a group.

Suppose you have a "Novel" [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) to which the [Work With pattern](https://wiki.genexus.com/commwiki/wiki?15974) has been applied. The purpose is to allow only authorized users to see the "Novels" List and view the detail.

1. Set [Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) to True.

2. Set the "WorkWithNovels" [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) to Authorization.

`[imagen omitida: wiki id 55263]`

3. Define a [Role](https://wiki.genexus.com/commwiki/wiki?17569) (for example, Role1) with a certain [Permission](https://wiki.genexus.com/commwiki/wiki?15912) (for example, with the default [Permission Access Type](https://wiki.genexus.com/commwiki/wiki?20603) ("Allow")). The permission name must be <prefix>\_execute, where the prefix is the value of the [Permission Prefix property](https://wiki.genexus.com/commwiki/wiki?17571) specified for the WW object (in this case: Novel\_Services).

`[imagen omitida: wiki id 55269]`

As a result, only users who have this role can execute the "Work With Novels" object in order to display the list of Novels and view the detail of each of them.

`[imagen omitida: wiki id 55268]`

User's role that allows executing the Work With Novels

`[imagen omitida: wiki id 55292]`  
GAMSDLogin execution

`[imagen omitida: wiki id 55288]`

### [What happens with [Menu object](https://wiki.genexus.com/commwiki/wiki?16321)s?](#What+happens+with+wiki%3F16321%2CCategory%253AMenu%2Bobject+Menu+objects%3F)

In the case of Menus, permissions are not verified. That's why the only available values for [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) are "none", and "Authentication" in this case.

If you configure the "Authentication" value in this property for Menu objects, the behavior is not the same as the behavior for Panels or WW Panels: when trying to execute the Menu for the first time, the object specified for the [Login Object for SD property](https://wiki.genexus.com/commwiki/wiki?16589) will execute. However, in the following executions, the validity of the session is not checked for Menus so the login object will display again only when the user tries to execute another private object that is called from the Menu.

Example: Suppose you have the following Menu object with three items:

`[imagen omitida: wiki id 55264]`

These objects (Panel1, WorkWithNovel, and WorkWithAuthor) check permissions independently, according to the settings of the [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) of each object.

If [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) = none, Authentication is not required to execute this object.

If [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) = Authentication, only authenticated users can execute the object. Authentication will be checked for the first time when executing the Menu; afterwards (when the session times out), Authentication is checked when this object is executed.

If [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) = Authorization, only authenticated and authorized users can execute the object. Authentication will be checked for the first time when executing the Menu; afterwards (when the session times out), Authentication is checked when this object is executed.

Any combination is valid.

If the three of them require Authorization, you need to define a Role where the corresponding permissions are defined, with the desired [Permission Access Type](https://wiki.genexus.com/commwiki/wiki?20603).

If the user is not authorized to execute "WorkWithAuthor", the following error will be shown on screen: "Unauthorized: Access is denied.".

Otherwise, the execution can be redirected to the object specified in [Not Authorized Object for SD property](https://wiki.genexus.com/commwiki/wiki?20018).

After configuring the permissions on the user's role, as the following figure shows:

`[imagen omitida: wiki id 55273]`

User's role permissions for executing WorkWithAuthor

The user will be able to execute WorkWithAuthor:

`[imagen omitida: wiki id 55289]`

Also, to execute the Detail and all its Sections:

`[imagen omitida: wiki id 55290]`

Note that the \_same permission\_ allows the user to execute the Detail and all the sections inside the Detail (view Section General and Section Novels).

**Note:**

The actions in the WW panels (insert, update, delete) are directly related to the Business Component associated with the WW and not the WW itself. This means that, if you apply Work With Pattern to a Transaction ("Novels"), the "Novels" Transaction is automatically saved as Business Component exposed as [REST Web Services](https://wiki.genexus.com/commwiki/wiki?14573). In order to control permissions over the actions insert, update, and delete, you need to declare permissions over the Business Component itself. See [HowTo: Permissions in SD Applications, CRUD Restricted](https://wiki.genexus.com/commwiki/wiki?17935) and [HowTo: Permissions in SD Applications, WW and CRUD Restricted](https://wiki.genexus.com/commwiki/wiki?17943) for details.

The permissions over the list and view of the item's list are managed in the WWSD object as shown in this paper.

### [See Also](#See+Also)

[GAM - Permissions](https://wiki.genexus.com/commwiki/wiki?15912)  
[Full Control Permissions and inheritance](https://wiki.genexus.com/commwiki/wiki?17664)  
[GAM Roles](https://wiki.genexus.com/commwiki/wiki?17569)  
[GAM Authorization Scenarios](https://wiki.genexus.com/commwiki/wiki?17583)


|  |
| --- |
| **Backlinks** |
| [GAM - Authorization Scenarios](https://wiki.genexus.com/commwiki/wiki?17583) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
