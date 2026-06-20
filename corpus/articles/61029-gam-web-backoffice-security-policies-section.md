---
title: "GAM Web Backoffice - Security Policies section"
source_id: 61029
source_url: https://wiki.genexus.com/commwiki/wiki?61029
genexus_version: "18"
---

# GAM Web Backoffice - Security Policies section

This article describes the Security Policies section of the [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935), which allows you to define and manage password [policies](https://wiki.genexus.com/commwiki/wiki?18521), account locking rules, and other security-related settings.

This section offers three important actions:

1. [Add a security policy](https://wiki.genexus.com/commwiki/wiki?61029)
2. [Copy a security policy](https://wiki.genexus.com/commwiki/wiki?61029)
3. [Edit a security policy](https://wiki.genexus.com/commwiki/wiki?61029)

`[imagen omitida: wiki id 61030]`

## [1. Add a security policy](#1.+Add+a+security+policy)

Press the ADD button to create a new security policy.

This action opens a form where you can configure all necessary settings, such as password requirements, account session settings, etc.

`[imagen omitida: wiki id 61031]`

### [General](#General)

* **ID:** Displays the unique identifier for the policy.
* **GUID:** The globally unique identifier for this security policy.
* **Name:** Write the name of the security policy.

### [Only Web](#Only+Web)

* **Allow multiple concurrent user sessions:** A dropdown menu allows you to select if various sessions from different IP addresses are allowed. In the GeneXus IDE, this option corresponds to the [AllowMultipleConcurrentWebSessions property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?18939).
* **Session timeout (minutes):** Defines the time of inactivity (in minutes) after which a session will automatically expire. In GeneXus, this option corresponds to the [WebSessionTimeOut property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?58396).

### [Only REST OAuth (Mobile, GAMRemoteRest)](#Only+REST+OAuth+%28Mobile%2C+GAMRemoteRest%29)

* **Token Expiration (minutes):** Specifies an OAuth token's duration (in minutes) before it becomes invalid. In the GeneXus IDE, this option corresponds to the [OauthTokenExpire property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?18577).
* **Token maximum renovations:** Defines the maximum number of times an OAuth token can be refreshed. In the GeneXus IDE, this option corresponds to the [OauthTokenMaximumRenovations property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?19324).
* **OAuth refresh\_token expiration (minutes):** Sets the time, in minutes, that a refresh\_token will remain active. In the GeneXus IDE, this option corresponds to the [OAuthRefreshTokenExpire property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?58097).
* **OAuth access\_code expiration (seconds):** Defines, in seconds, that an access code remains valid before expiring. In the GeneXus IDE, this option corresponds to the [OAuthAccessCodeExpire property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?58098).

### [Password Management](#Password+Management)

* **Period change password (minutes):** Specifies how often users are required to change their password (in minutes).
* **Minimum waiting time between password changes (minutes):** Minimum time before a user can change their password again. In the GeneXus IDE, this option corresponds to [MinimumTimeToChangePasswords property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?18942).
* **Minimum password length:** The shortest length allowed for passwords.
* **Minimum number of numeric characters in passwords:** Requires a minimum number of numbers in a password.
* **Minimum number of uppercase characters in passwords:** Sets the minimum of uppercase letters in the password.
* **Minimum number of special characters in passwords:** Requires a specified number of special characters (For example: @, #, $).
* **Maximum password history entries:** Limits how many previous passwords are remembered. In the GeneXus IDE, this option corresponds to [MaximumPasswordHistoryEntries property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?18579).

## [2. Copy a security policy](#2.+Copy+a+security+policy)

This link allows you to duplicate the existing security policy.

`[imagen omitida: wiki id 61068]`

After clicking on Copy to duplicate a policy, the message “INFORMATION: Security Policy was copied successfully!” is displayed.

`[imagen omitida: wiki id 61032]`

## [3. Edit a security policy](#3.+Edit+a+security+policy)

This link allows you to edit a specific security policy.

`[imagen omitida: wiki id 61069]`

After clicking on the Edit link, the following form is displayed:

`[imagen omitida: wiki id 61034]`

In the EDIT section of a Security Policy, you'll find two buttons:

* DELETE
* MORE OPTIONS

`[imagen omitida: wiki id 61035]`

* DELETE button: Removes the selected security policy from the Web Backoffice.
* MORE OPTIONS combo:
  + **Custom Properties:** Allows you to add custom properties for the security policy.
  + **Copy:** Creates a duplicate of the current security policy.
  + **Translations:** Adds translations of the Security Policy into different languages.

### [See Also](#See+Also)

[GAM - Security Policies](https://wiki.genexus.com/commwiki/wiki?18521)


|  |
| --- |
| **Backlinks** |
| [GAM - Security Policies](https://wiki.genexus.com/commwiki/wiki?18521) | [GAM Web Backoffice - Main Menu](https://wiki.genexus.com/commwiki/wiki?61064) | [GAM Web Backoffice - Security Policies section](https://wiki.genexus.com/commwiki/wiki?61029) |
| [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
