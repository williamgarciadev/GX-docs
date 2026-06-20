---
title: "GXflow Users"
source_id: 10193
source_url: https://wiki.genexus.com/commwiki/wiki?10193
genexus_version: "18"
---

# GXflow Users

The Users application can be accessed from the GXFlow [GXflow Management Console](https://wiki.genexus.com/commwiki/wiki?9340).

`[imagen omitida: wiki id 53847]`

Users are managed from this application. It allows adding new users, updating their personal data, deleting users and assigning/removing [roles](https://wiki.genexus.com/commwiki/wiki?11864) to/from users.

The following figure shows this application interface:

`[imagen omitida: wiki id 52085]`

The following sections describe the different components making up this application.

### [Actions](#Actions)

New: This button allows accessing the new user dialog:  
  
`[imagen omitida: wiki id 52086]`

The logged user must specify the following information in this dialog:

* User: exclusive user identifier
* Name: user name
* Email: e-mail address associated to the user
* Password: user personal password to access the workflow system
* R. Password: a duplicate of the password entered in the previous field
* User must change password at next logon: defines if the user has to change the password in the next logon

If there are licenses available, the user will be automatically nominated.

**Remove:** To delete a user, the logged user must first select it from the list of users and then press this button. A dialog will be displayed asking the user to confirm the deletion. If the user is nominated, after being removed his/her license will be released.

**Edit:** To update a user data, the logged user must first select the corresponding user from the list of users and then press this button. The dialog displayed is essentially the same as the New user dialog, where he can update all user data with the exception of his identifier.     
If a user availability is changed from in office to out of office, the [GXflow Out of Office Assistant](https://wiki.genexus.com/commwiki/wiki?10205) will be displayed. It will allow the logged user to select a substitute user.

**Display:** To visualize the personal data of a specific user, the logged user must first select  the corresponding  user from the list of users and then press this button.

**Roles:** This button allows listing the system roles, the roles assigned to the user are in the right column. Roles can be added or deleted by selecting them from the list and pressing the "ADD" or "REMOVE" button.

**Organizational Units:** This button allows listing the restrictions associated to the user (the Organizational Units to which the user belongs).

**Toggle Blocked:** It allows blocking a user.

**Out of Office:**This button displays the days a user is out of office, it is only available if the user is currently out of office.

### [Users Grid](#Users+Grid)

This grid has the following options:

`[imagen omitida: wiki id 52012]` It allows selecting the columns wanted to be visible.

`[imagen omitida: wiki id 52013]` It allows refreshing the grid.

It is possible to sort some columns by clicking on their title.

This grid consists of the following columns:

* `[imagen omitida: wiki id 52087]`: Indicates if the user is blocked.
* `[imagen omitida: wiki id 52088]`: Indicates if the user is out of office.
* Id: User Id.
* Global Id: User global Id.
* Name: User name.
* Email: User email.
* Out of Office Start: Out of office start date.
* Out of Office End: Out of office end date.
* Substitute: The user who is currently replacing the user in this row.

### [See Also](#See+Also)

[GXflow Management Console](https://wiki.genexus.com/commwiki/wiki?9340)  
[GXflow Roles](https://wiki.genexus.com/commwiki/wiki?10194,,)  
[GXflow Organizational Units Definitions](https://wiki.genexus.com/commwiki/wiki?10195)  
[GXflow Organizational Units](https://wiki.genexus.com/commwiki/wiki?10196)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [GXflow Management Console](https://wiki.genexus.com/commwiki/wiki?9340) | [GXflow Organizational Units](https://wiki.genexus.com/commwiki/wiki?10196) |
| [GXflow Organizational Units Definitions](https://wiki.genexus.com/commwiki/wiki?10195) | [GXflow Out of Office Assistant](https://wiki.genexus.com/commwiki/wiki?10205) | [HowTo: Use GXflow Entry Point User Control](https://wiki.genexus.com/commwiki/wiki?10721) |

---
