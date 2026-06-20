---
title: "GAM Web Backoffice - Users section"
source_id: 60983
source_url: https://wiki.genexus.com/commwiki/wiki?60983
genexus_version: "18"
---

# GAM Web Backoffice - Users section

This article describes the Users section of the [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935), where you can manage all [users](https://wiki.genexus.com/commwiki/wiki?22082) registered in the repository.

In the Main Menu, select the Users option to perform the following actions:

1. [Create new users](https://wiki.genexus.com/commwiki/wiki?60983)
2. [Search users](https://wiki.genexus.com/commwiki/wiki?60983)
3. [Apply Roles, Permissions, and Edit specific users](https://wiki.genexus.com/commwiki/wiki?60983)

`[imagen omitida: wiki id 60985]`

## [1. Create new users](#1.+Create+new+users)

To create a new user, click on the NEW USER button and complete the form displayed:

`[imagen omitida: wiki id 60994]`

The image shows the "New user" form. Below, you'll find a description of each field.

### [General information](#General+information)

This section contains the basic information about the new user.

* **GUID:** Once the new user is created, the Globally Unique Identifier is shown.
* **Name space:** This field shows the Knowledge Base's name. It is the namespace where the user is being created.
* **Authentication Type:** Dropdown menu to select the authentication type for the user.
* **Username:** Field to enter the user's username.
* **EMail:** Field where you can enter the user's email address.
* **Password:** Field to enter the user's password.
* **Password confirmation:** The field where you can confirm the user's password.
* **First Name:** Field to enter the user's first name.
* **Last Name:** Field to enter the user's last name.
* **External ID:** Field to enter the user's external ID.
* **Phone:** Field where you can enter the user's phone number.

### [Security information](#Security+information)

This section contains security-related information about the new user.

* **Is the user blocked?** Checkbox where you can block the user.
* **Must change password?** Checkbox to force the user to change their password at the next login.
* **Security policy:** Dropdown menu where you can select a security policy to apply to the user.
* **Language:** Dropdown menu to select the user's language.
* **Theme:** Dropdown menu to select the user's theme.
* **Password never expires:** Checkbox that lets you indicate if the user's password should never expire.
* **Cannot change password:** Checkbox that prevents the user from changing their password.
* **Don't want to receive information:** Checkbox that prevents the user from receiving information.
* **Is the user enabled in repository?**Checkbox to enable the user in the repository.

### [Advanced information](#Advanced+information)

This section contains advanced information about the new user.

* **Birthday:** Enter the user's birthday here.
* **Gender:** Dropdown menu to select the user's gender.
* **Address:** Enter the user's address.
* **Address2:** Enter the user's second address.
* **City:** Field to enter the user's city.
* **State:** Enter the user's state.
* **Postal Code:** Field to enter the user's postal code.
* **Country:** Dropdown menu to select the user's country.
* **Timezone:** Dropdown menu to select the user's time zone.
* **URL image:** Enter the URL of the user's image.
* **URL profile:** Field to enter the URL of the user's profile.

## [2. Search users](#2.+Search+users)

If the list of users is long, use the Search box to find a specific user by name.

## [3. Apply Roles, Permissions, and Edit specific users](#3.+Apply+Roles%2C+Permissions%2C+and+Edit+specific+users)

Use the **ROLES**, **PERMISSIONS**, and **EDIT** links to assign roles, manage permissions, and modify user details.

`[imagen omitida: wiki id 60995]`

### [Users ROLES](#Users+ROLES+)

The ROLES link lets you manage a user's roles. You can view, add, or remove roles assigned to a user.

To edit a user's roles, locate the user in the Users section and click on the **ROLES** link.

`[imagen omitida: wiki id 60996]`

In this case, the "admin" user is assigned the Administrator (Main) role.

`[imagen omitida: wiki id 60998]`

You can ADD a new Role to that User, use the CUSTOM PROPERTIES link to set name/value attributes for an assigned role, or REMOVE the existing one.

* **Add new roles**: Click on the ADD button at the top right to assign new roles to the User.
* **Remove roles:** Use the REMOVE link next to an assigned Role to delete it.
* **Custom properties:** Allows you to define custom attributes for the selected role assigned to the user. When you click on Custom Properties, a dialog is displayed where you can add tokens and values associated with that user and that role.

### [Users PERMISSIONS](#Users+PERMISSIONS)

To manage a User's permissions, click on the **PERMISSIONS** link next to the user.

Once you click on the PERMISSIONS link of a User, you can manage the permissions for a specific user (in this case: “admin”).

`[imagen omitida: wiki id 60999]`

Select an application from the Application Combo Box to assign permissions for a specific application:

`[imagen omitida: wiki id 61000]`

Once you select the desired application, click on the ADD button to choose the permissions.

The following window is displayed:

`[imagen omitida: wiki id 61001]`

Upon selection, the desired permission will be displayed in the list for review.

`[imagen omitida: wiki id 61002]`

You will see detailed information about each assigned permission, including:

* **Permission name:** The name of the specific permission assigned.
* **Description:** An explanation of the permission.
* **Permissions options:**
  + **Allow:** Grants the user access.
  + **Deny:** Denies access.
  + **Restricted:** Limits access to the action under specific conditions.
* **Inherit:** Checkbox that indicates if the permission is inherited from another role or user group.

Click on the ADD button to assign the permissions.

### [Editing a User](#Editing+a+User)

To modify a User's details, click on the EDIT link next to the User.

`[imagen omitida: wiki id 61003]`

You can modify the user's preferences, including general information, security settings, and advanced details.

A form will open where you can update these details:

`[imagen omitida: wiki id 61005]`

### [EDIT ROLES and MORE OPTIONS buttons (inside Edit Link option)](#EDIT+ROLES+and+MORE+OPTIONS+buttons+%28inside+Edit+Link+option%29)

When editing a user, you also have two main buttons:

`[imagen omitida: wiki id 61006]`

* **EDIT ROLES** to modify roles.
* **MORE OPTIONS** for additional settings.

#### [EDIT ROLES](#EDIT+ROLES)

This button allows you to manage the roles associated with a user.

Clicking on this link opens a new section where you can add, remove, or modify the roles assigned to a particular user.

In addition, for each assigned role, you can use the Custom Properties link to define specific attributes for that user and that role.

`[imagen omitida: wiki id 61008]`

#### [MORE OPTIONS](#MORE+OPTIONS)

This Combo box menu contains several advanced options related to the user.

* **Custom Attributes:** Allows you to add or edit custom attributes specific to this User.
* **Edit Permissions:** Enables editing the User's direct permissions.
* **Change Password:** Allows changing the current User password.
* **GUID by Application (GAM\_UserGUIDbyApplication):**Allows displaying the user's GUIDs by application.
* **Application API KEY:** Allows generating an API key associated with the user.
* **Block user:** Temporarily blocks the User's access to the Web Backoffice.
* **Kill sessions:** Ends all active sessions of the User, forcing them to log in again.
* **Disable in repository:** Deactivates the User in the repository.
* **Delete User:** Permanently deletes the User from the Web Backoffice.

### [See Also](#See+Also)

[GAM - Users](https://wiki.genexus.com/commwiki/wiki?22082)


|  |
| --- |
| **Backlinks** |
| [GAM - Security Policies](https://wiki.genexus.com/commwiki/wiki?18521) | [GAM - Users](https://wiki.genexus.com/commwiki/wiki?22082) | [GAM Web Backoffice - Main Menu](https://wiki.genexus.com/commwiki/wiki?61064) |
| [GAM Web Backoffice - Users section](https://wiki.genexus.com/commwiki/wiki?60983) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
