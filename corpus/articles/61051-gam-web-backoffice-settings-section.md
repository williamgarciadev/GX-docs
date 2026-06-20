---
title: "GAM Web Backoffice - Settings section"
source_id: 61051
source_url: https://wiki.genexus.com/commwiki/wiki?61051
genexus_version: "18"
---

# GAM Web Backoffice - Settings section

This article describes the Settings section of the [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935), which provides options to configure general aspects of the repository.

The Settings section includes several nodes:

`[imagen omitida: wiki id 61052]`

1. [Authentication Types](https://wiki.genexus.com/commwiki/wiki?61051)
2. [Event Subscriptions](https://wiki.genexus.com/commwiki/wiki?61051)
3. [GAM Configuration](https://wiki.genexus.com/commwiki/wiki?61051)
4. [General](https://wiki.genexus.com/commwiki/wiki?61051)

## [1. Authentication Types](#1.+Authentication+Types)

This section allows you to define and update the authentication methods. You can add, test, edit and delete an Authentication type.

`[imagen omitida: wiki id 61053]`

Adding an authentication type

The **ADD** Combo Box allows you to add a new authentication type:

`[imagen omitida: wiki id 61054]`

The possible authentication types are:

* **API Key:** This authentication type uses a unique API key to identify and authorize users or applications.
* **Apple:** This authentication type allows users to authenticate using their Apple ID.
* **Custom:** Allows you to implement your own custom authentication method.
* **External Web Service:** Allows authentication through an external web service.
* **Facebook:** Enables the authentication using Facebook accounts.
* **GAM Remote:** This authentication type is used to authenticate against a remote GAM server.
* **GAM Remote REST:** This authentication type allows users to authenticate against a remote GAM server using a RESTful protocol.
* **Google:** This authentication allows users to authenticate through Google accounts.
* **OAuth 2.0:** This is an open standard for authorization. It allows users to grant limited access to their resources on one site to another site, without having to share their credentials.
* **One-Time Password:** An Authentication method based on one-time passwords (OTP).
* **SAML 2.0:** Authentication using the SAML standard.
* **Twitter:** This authentication type allows users to authenticate using their Twitter account.
* **WeChat:** This authentication type allows users to authenticate using their WeChat account.

In the authentication type list, you can perform the following actions:

`[imagen omitida: wiki id 61056]`

* **TEST:** Allows you to test the authentication method to ensure that it is working correctly.
* **EDIT:** Allows you to modify the specific settings of the selected authentication type.
* **DELETE:** Deletes the selected authentication type.

Once you select an authentication type from the list (in this case: “local”), you are offered a new section to manage this authentication type, as shown below:

`[imagen omitida: wiki id 61057]`

### [General Section](#General+Section+)

This section contains general information about the authentication type.

* **Type:** Indicates the type of authentication being used. In this case, it is set to local.
* **Name:** Displays the name assigned to this authentication type. In this case, it is also labeled as local.
* **Function:** Shows the role of this authentication type.
* **Enabled?**Checkbox that if clicked determines whether this authentication type is active or not.
* **Description:** Provides a brief description of the authentication type.
* **Small image name:** Displays the name of the small image associated with the authentication type.
* **Big image name:** Shows the name of the big image associated with the authentication type.

### [Configuration Section](#Configuration+Section+)

This section contains specific configuration options for the authentication type.

* **Enable Two Factor Authentication?** Checkbox to enable or disable Two-Factor Authentication (2FA) for this authentication type. If the checkbox is cleared, 2FA is not enabled for this authentication type.

### [EDIT, DELETE and MORE OPTIONS Buttons](#EDIT%2C+DELETE+and+MORE+OPTIONS+Buttons)

* **EDIT:** This button allows you to save the changes made to the authentication type.
* **DELETE:** This button allows you to delete the authentication type.
* **MORE OPTIONS:** This button, with a dropdown menu, provides an additional option.
  + **Custom Properties:**This option allows you to configure additional parameters that are specific to each authentication type.
  + **Translations:** This option allows you to manage the translations for the authentication type.

For more information, check [GAM - Authentication Types](https://wiki.genexus.com/commwiki/wiki?16508)

## [2. Event Subscriptions](#2.+Event+Subscriptions)

This article describes the **Event Subscriptions** section in the **Settings** node of the GAM Web Backoffice.

`[imagen omitida: wiki id 61058]`

This section allows you to run external code when specific GAM events occur, such as when a user is created, updated, or deleted. This enables you to trigger custom actions, such as sending notifications, updating external systems, or logging security events.

This section displays a list of event subscriptions (in the image above, the list is empty, indicating that no subscriptions have been created).

The list displays the following information for each subscription:

* **Event Description:** Provides the event that triggers the subscription.
* **Status:** Indicates the status of the Event Subscription (for example: Enabled/Disabled).
* **Event:** Identifies the event that triggers the subscription (For example: User Created, Password Changed).
* **File Name:** Specifies the name of the file containing the code to be executed when the event occurs.
* **ClassName:** Shows the name of the class containing the method to be executed.
* **Method Name:** Specifies the name of the method to be executed when the event occurs.

### [ADD button](#ADD+button)

This button allows you to add a new event subscription.

By clicking on this button, you can add a new event subscription.

`[imagen omitida: wiki id 61059]`

Events you may subscribe to:

* **User - Update:** Updates a GAM User.
* **User - Insert:** Inserts a GAM User.
* **User - Delete:** Deletes a GAM User.
* **User - Update Roles:** This event updates roles of a list of users.
* **User - Get Custom Information on GAMRemote Server:** This event allows customizing the information that the Identity Provider sends to the Client, and it’s executed when the Users authenticate (SSO Web) or request a token (OAuth 2.0). For this purpose, the Output of the Procedure must return a JSON. It’s recommended to use an SDT that has the structure of the information to be shared.
* **User - Save Custom Information on GAMRemote Client:** This event is executed on the client when the GAM Remote or Remote Rest Authentication type (OAuth 2.0) login is successfully finished.
* **Role - Insert:** Inserts a role.
* **Role - Update:** Updates a role.
* **Role - Delete:** Deletes a role.
* **Repository - Login:** This event is triggered when a GAM user successfully logs in using any supported authentication type.
* **Repository - Login Failed:** This event is triggered when a user login attempt fails due to a GAM Error 10, 11, or 18.
* **GAM\_Repository\_RememberAuthentication:** This event is triggered when the user's session doesn't exist or the token has expired, and only when the user was authenticated using 'Keep me logged in'.
* **Repository - Logout:** This event is triggered when a GAM user logs out from the repository.
* **Repository - External Authentication Response:**This event is triggered after receiving the authentication response from an external Identity Provider.
* **Application - Check Permission Fail:** This event is triggered when the user is checked for permission to access the object and does not have access.
* **User - One Time Password Valid User:** This event checks that the user who asked for an OTP code is allowed to do it.
* **User - One Time Password Generate Code:** Developer event to generate the OTP code.
* **User - One Time Password Send Code:** Developer event to send the OTP code.
* **User - One Time Password Validate Code:** Developer event to validate the OTP code.

Click on the CONFIRM button to add the new Event Subscription.

Read more at [GAM - Events subscription](https://wiki.genexus.com/commwiki/wiki?32698).

## [3. GAM Configuration](#3.+GAM+Configuration)

This section provides the necessary settings to configure GAM's functions, such as the database version, API version, and enable tracing.

`[imagen omitida: wiki id 61060]`

### [GAM Configuration](#GAM+Configuration)

This section displays information about the current GAM installation.

* **Database version:** Shows the version of the GAM database.
* **API version:** Indicates the version of the GAM API.
* **Enable tracing:** Provides a dropdown menu to enable or disable tracing. Tracing can be useful for debugging and troubleshooting issues with the GAM system.

## [4. General](#4.+General+)

This section allows administrators to manage and clean up outdated session data and cached information.

`[imagen omitida: wiki id 61062]`

### [General](#General)

### [Sessions](#Sessions)

Allows you to manage user session data.

* **Clean up to:** Provides a field to specify the time up to which sessions will be cleaned.
* **CLEAN TABLES button:** Allows you to clear session data tables.
* **UPDATE AS EXPIRED button:** Marks specific sessions as expired.

### [Cache](#Cache+)

This section manages cached data.

* **Clear Local Cache:** A button labeled CLEAR that removes stored cache data.
* **Clear URL Cache:** A button labeled CLEAR to remove cached data related to URLs.


|  |
| --- |
| **Backlinks** |
| [GAM Web Backoffice - Main Menu](https://wiki.genexus.com/commwiki/wiki?61064) | [GAM Web Backoffice - Settings section](https://wiki.genexus.com/commwiki/wiki?61051) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
