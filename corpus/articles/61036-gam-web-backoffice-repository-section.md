---
title: "GAM Web Backoffice - Repository section"
source_id: 61036
source_url: https://wiki.genexus.com/commwiki/wiki?61036
genexus_version: "18"
---

# GAM Web Backoffice - Repository section

This article describes the [Repository](https://wiki.genexus.com/commwiki/wiki?17568) section of the [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935), which allows you to manage repositories and their related configurations.

Allows managing user roles, creating new repositories, configuring connections between them, exporting data, and managing user policies.

The Repository is divided into two main sections:

1. [Configuration](https://wiki.genexus.com/commwiki/wiki?61036)
2. [Connections](https://wiki.genexus.com/commwiki/wiki?61036)

`[imagen omitida: wiki id 61037]`

## [1. Configuration](#1.+Configuration+)

The Configuration section allows administrators to manage various settings related to security policies, user management, and repository properties.

It includes several sections such as General, Users, General Security Policy and Emails, as well as a MORE OPTIONS button.

`[imagen omitida: wiki id 61038]`

### [MORE OPTIONS button](#MORE+OPTIONS+button)

In the MORE OPTIONS combo, you can find the Custom Properties option. This option allows you to define and manage custom attributes or configurations for the repository.

### [General, Users, General Security Policy, and Emails tabs](#General%2C+Users%2C+General+Security+Policy%2C+and+Emails+tabs)

#### [General tab](#General+tab)

#### 

This tab contains the settings for the repository, including:

* **ID:** The unique identifier of the repository.
* **GUID:** A globally unique identifier for the repository.
* **Namespace:** This field shows the Knowledge Base's name. It is the namespace where the repository is being created.
* **Name:** Write the name of the repository.
* **Description:** Write a brief description of the repository's purpose.
* **Default authentication type:** Specifies the authentication method (for example: "Local" or other methods).
* **Default role:** The default User Role assigned when accessing the repository.
* **Default security policy:** Links the repository to a specific security policy.
* **Cache timeout (minutes):** Defines how long cached data is retained before expiring. In the GeneXus IDE, this corresponds to [CacheTimeout property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?21863).
* **Allow access by OAuth 2.0 protocol? (Mobile, GAMRemote, GAMRemoteRest, IDP, SSO):** Indicates whether the repository supports OAuth 2.0 for access.
* **Applications list group by (default value):** Sets how applications are grouped by default.
* **GAMRemote logout behavior (IDP):** Determines the logout behavior for Identity Providers (IDP) in GAMRemote.
* **Enable working as GAMManager repository:** Determines if the repository can operate as a GAMManager repository.
* **Enable tracing:** Controls whether tracing (debugging or logging) is enabled for the repository. For more information, see: [HowTo: Generate GAM trace](https://wiki.genexus.com/commwiki/wiki?50469).

#### [Users tab](#Users+tab)

The Users tab contains configurations related to user account management and behavior.

`[imagen omitida: wiki id 61041]`

* **User identification by:** Defines the method used to identify users during authentication. **Values:** Email or Name: Users can log in using their email address or username.

#### [Activation User](#Activation+User)

* **Method:** Specifies the method to activate user accounts. Values: Automatic: Accounts are activated without administrator intervention. Manual: Activation requires administrator approval or manual activation.

#### [Password Recovery](#Password+Recovery)

* **User recovery password key timeout (minutes):** Sets the expiration time for password recovery keys.
* **Maximum daily keys:** Limits the number of recovery keys a user can request per day.
* **Maximum monthly keys:** Limits the number of recovery keys a user can request per month.

#### [Block Access](#Block+Access)

* **Login retries to lock user:** Defines the number of failed login attempts allowed before a user account is temporarily locked. In the GeneXus IDE, this option corresponds to [LoginAttemptsToLockUser property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18592).
* **Timeout to reset countdown failed OAuth logins (minutes) (0= Does not block OAuth user):** Specifies the time (in minutes) a user must wait before their account is automatically unlocked after being locked due to failed login attempts.
* **Timeout to automatically unlock users (minutes):** Configures the behavior of the "Remember Me" feature for user sessions.

#### [Remember User](#Remember+User)

* **Type:** Specifies the method used to remember the user.
* **Timeout (days) (0=never):** Sets the duration (in days) for which the "Remember Me" feature will maintain the session active.

#### [Required Data](#Required+Data)

Specifies which user data fields are mandatory using checkboxes.

* **Password?** Specifies whether a password is required for user account creation or updates.
* **Email?**Specifies if an email address is required for user registration or updates.
* **First name?** Indicates if the user’s first name is a required field.
* **Last name?** Specifies if the user’s last name is a required field during registration.
* **Birthday?** If selected, the user’s date of birth must be provided during account creation or updates.
* **Gender?**Indicates if specifying the user’s gender is required.
* **Phone?** Specifies if providing a phone number is mandatory for user registration or updates.
* **Address?** Indicates if the user’s address is required when creating or updating an account.
* **City?** If selected, the user must provide their city as part of their profile information.
* **State?** Specifies whether the user’s state or region must be entered.
* **Postcode?** Defines if a postal or ZIP code is a required field.
* **Photo?** Indicates if uploading a profile picture is mandatory.
* **Language?**Specifies if the user must select a language.
* **Timezone?** If selected, the user must define their timezone in their profile settings.

#### [General Security Policy tab](#General+Security+Policy+tab)

The General Security Policy tab configures user session settings, login attempts, anonymous access, and session timeouts.

`[imagen omitida: wiki id 61042]`

* **Generate session statistics:** Allows the system to track and generate statistics related to user sessions. In the GeneXus IDE, this option corresponds to the Generate Session Statistics property of the GAM Repository. More information about this property: [Generate Session Statistics GAMRepository property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?24375,,).
* **User session cache timeout (seconds):** Sets the duration (in seconds) for which a user's session data is cached. In the GeneXus IDE, this option corresponds to [UserSessionCacheTimeout property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18582).
* **Give anonymous session (WEB)?** If selected, the system allows sessions for users without authentication (anonymous users). If cleared, all users must authenticate.
* **Expire the session when the IP changes (WEB)?** If selected, user sessions will automatically expire if their IP address changes.
* **Login attempts to lock session (WEB):** Defines the maximum number of failed login attempts before a session is locked. In the GeneXus IDE, this option corresponds to [LoginAttemptsToLockSession property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18593).
* **Minimum amount characters in login:** Sets the minimum number of characters required for a valid login ID.
* **Enable SSO REST access for undefined ClientIDs in exposed REST services?** If selected, this feature integrates security policies based on the user's domain.
* **Enable reuse of active user tokens:**Checkbox to enable reuse of active user tokens for authentication sessions. In the GeneXus IDE, this option corresponds to [EnableReusingActiveUserTokens property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?61084).
* **TOTP secret key length:**Numeric input to set the length of the TOTP secret key used to generate time-based one-time passwords.

#### [Timeouts](#Timeouts)

* **Timeout for user to change password after login (minutes):** Sets the time limit (in minutes) for a user to change the password after login.
* **Timeout to complete required user data after login (minutes):** Configures the time, in minutes, allowed for a user to complete the required data in the repository they want to access. In the GeneXus IDE, this option corresponds to [TimeoutToCompleteRequiredUserDataAfterLogin property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?58082).
* **Timeout to finish OAuth authentication (state) using an IDP (minutes):** Configures the time, in minutes, that the State will remain valid when a client authenticates using OAuth 2.0 to an Identity Provider (IDP). In the GeneXus IDE, this option corresponds to [TimeoutToFinishOAuthAuthenticationUsingIDP property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?58086).

#### [Integrated Security by domain](#Integrated+Security+by+domain)

* **Enable?**Allows users to authenticate using the domain's integrated security.

#### [Emails tab](#Emails+tab)

The GAM Web Backoffice allows you to configure email settings for various security-related events.

Here you can find all the different sections available in the **Emails** tab of the Repository configuration.

`[imagen omitida: wiki id 61043]`

#### [Email configuration](#Email+configuration)

This section allows you to configure the basic settings for your email server.

* **Server Host:** Specifies the hostname of your email server (For example: SMTP server)
* **Timeout (seconds):** Sets the maximum time, in seconds, to wait for a server response before the connection times out.
* **Server Port:** Defines the port number used to connect to the email server.
* **Secure:** If selected, the communication protocols for the email server are secure.
* **Sender Email Address:** Specifies the email address from which emails will be sent.
* **Sender Name:** Sets the name that will appear as the sender in emails.
* **Server Requires Authentication:** Indicates whether the email server requires authentication. If selected, you will need to provide authentication credentials.

#### [Account Activation](#Account+Activation)

This section allows you to configure whether to send an email notification when a user activates their account.

* **Send email when user activates account?**Checkbox. When selected, an email notification is sent to the user when the account is activated. For more information, see [GAM configuration to send emails](https://wiki.genexus.com/commwiki/wiki?48421).

#### [Change password](#Change+password)

This section allows you to configure whether to send an email notification when a user changes their password.

* **Send email when user changes password?** When selected, an email notification is sent to the user when their password is changed. For more information, see [GAM configuration to send emails](https://wiki.genexus.com/commwiki/wiki?48421).

#### [Change email/username](#Change+email%2Fusername)

This section allows you to configure whether to send an email notification when a user changes their email or username.

**Send email when user changes email/username?** When selected, an email notification is sent when the user updates their email or username. For more information, check [GAM configuration to send emails](https://wiki.genexus.com/commwiki/wiki?48421).

#### [Password Recovery](#Password+Recovery)

This section allows you to configure whether to send an email for password recovery purposes.

**Send email for password recovery?** When selected, an email is sent to users for password recovery purposes. For more information, see [GAM configuration to send emails](https://wiki.genexus.com/commwiki/wiki?48421).

### [MORE OPTIONS button (Combo Box)](#MORE+OPTIONS+button+%28Combo+Box%29)

Contains additional configuration options for Custom properties.

## [2. Connections section](#2.+Connections+section)

The **Connections** section allows you to manage the connections used by your GAM Repository. This is where you can define and configure connections to external systems or databases.

This section offers three important actions:

1. Add a repository connection
2. Keys for a repository connection
3. Edit a repository connection

`[imagen omitida: wiki id 61047]`

### [1. Add a repository connection](#1.+Add+a+repository+connection)

When clicking on the ADD button, you will be able to add new connections to a repository as shown below:

`[imagen omitida: wiki id 61048]`

#### [General](#General)

* **Connection Name:** Specifies a unique name for the connection.
* **Username:** Write the username for the connection.
* **User Password:** You can enter the password linked to the username.
* **Encryption key:** A field for entering an encryption key, which is used to encrypt the data exchanged through this connection.
  + **GENERATE ENCRYPTION KEY:** Clicking on this link automatically generates a secure encryption key for the user to use in the "Encryption Key" field.

### [2. Keys for a repository connection](#2.+Keys+for+a+repository+connection)

In this section, you can manage the connection keys.

`[imagen omitida: wiki id 61049]`

#### [Connection keys](#Connection+keys)

* **Add Connection Key:** You can enter a new connection key.
* **SAVE KEY button:** A button that saves the new connection key entered in the "Add Connection Key" field.
* **Connection Key:** Displays the current encryption key.
* **FILE link:** Provides the option to download or access the current encryption key in a file format.
* **DELETE link:** This allows you to delete the current key.

**USE AUTOMATIC KEY button:** Clicking on it generates and applies an automatically created encryption key for the connection.

**USE CURRENT KEY button:** Clicking on it applies the current encryption key already stored in the system.

### [3. Edit a repository connection](#3.+Edit+a+repository+connection)

`[imagen omitida: wiki id 61050]`

Note that some of the fields are similar to those found in the Keys link section.

#### [General](#General)

* **EDIT:** This button allows you to save the changes made to the connection.
* **DELETE:** This button allows you to delete the connection.
* **KEYS:** This button allows you to manage the API keys associated with the connection.

### [See Also](#See+Also)

[GAM - Repository](https://wiki.genexus.com/commwiki/wiki?17568)


|  |
| --- |
| **Backlinks** |
| [EnableReusingActiveUserTokens property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?61084) | [GAM - Repository](https://wiki.genexus.com/commwiki/wiki?17568) | [GAM Web Backoffice - Main Menu](https://wiki.genexus.com/commwiki/wiki?61064) |
| [GAM Web Backoffice - Repository section](https://wiki.genexus.com/commwiki/wiki?61036) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
