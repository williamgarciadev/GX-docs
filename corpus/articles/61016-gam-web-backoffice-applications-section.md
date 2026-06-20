---
title: "GAM Web Backoffice - Applications section"
source_id: 61016
source_url: https://wiki.genexus.com/commwiki/wiki?61016
genexus_version: "18"
---

# GAM Web Backoffice - Applications section

This article describes the Applications section of the [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935), which allows you to view and manage the [applications](https://wiki.genexus.com/commwiki/wiki?15910) defined in the repository.

Each listed application shows its name, description, Client ID, and status.

`[imagen omitida: wiki id 61017]`

## [ADD button](#ADD+button)

To add a new application to the repository, click on the ADD button and complete the displayed form.

`[imagen omitida: wiki id 61018]`

## [1. General](#1.+General)

This section contains basic information about the new application.

* **ID:** Displays the unique identifier for the application. This is automatically assigned once created.
* **GUID:** The Global Unique Identifier (GUID) for the application. This is generated once the application is created.
* **Name:** Field to enter the name of the application.
* **Description:** Field to write the description for the application.
* **Version:** Enter the application version.
* **Company:** Write the company name associated with the application.
* **Copyright:** Enter the copyright information for the application.
* **Use absolute URL by Environment:** Checkbox that lets you indicate whether to use absolute URLs by environment or not.
* **Home Object:** Enter the name of the home object for the application.
* **Account Activation Object:** Write the name of the account activation object.
* **Local Logout Object (specify an object or a URL):** Enter the name of the local logout object or a URL.

## [2. Menus](#2.+Menus)

This section contains menu-related settings for the application.

* **Return menu options without permission?** Click on the checkbox to return menu options without permission.
* **Main Menu:** A dropdown menu to select the main menu for the application.

## [3. Base Application](#3.+Base+Application)

The base application is used to group applications in the application list.

* **Is a base application?** Checkbox to indicate if the application is a base application or not.
* **Base application:** Select the base application from the dropdown menu.

## [4. Configuration](#4.+Configuration)

This section contains the configuration settings for the application. It has several tabs that are described below:

### [OAuth Authentication tab](#OAuth+Authentication+tab)

`[imagen omitida: wiki id 61019]`

* **Languages:** Configure the application's language settings for displaying OAuth-related messages and UI elements in the user's preferred language (all Configuration sections have this setting).
* **Status:** Displays the application status (For example: Online).
* **Client ID:** Enter the client ID for the OAuth authentication.
* **Client Secret:** Enter the client secret for the OAuth authentication.

**WEB (IDP using SSO, authorization code flow)**

This section contains settings related to web authentication.

* **Allow OAuth 2.0 (authorization code flow in /oauth/gam)?**Checkbox to enable the authorization code flow for web/identity provider (SSO) scenarios.

**REST services**

This section contains settings related to REST authentication.

* **Allow OAuth 2.0 (password grant flow in /oauth):** Checkbox to enable the password grant flow at /oauth.
* **Allow OAuth 2.0 (password grant flow in /oauth/gam/v2.0)?**Checkbox to enable the password grant flow at /oauth/gam/v2.0.

**Allowed user scopes (SSO REST, Mini App, API key, password grant flow)**

* **User data:** Checkbox that exposes the basic user profile information to the client.
* **User additional data:** Checkbox that exposes extended or custom user attributes beyond the basic profile to the client.
* **User roles:**Checkbox that exposes the roles assigned to the user to the client for authorization decisions.
* **Session initial properties:** Checkbox that, when enabled, includes initial session properties in the token/session.
* **Session application data:** Checkbox that includes application data in the session.
* **Additional REST scopes:** Input field for extra scopes to expose via REST.
* **Single-user access using OAuth 2.0:** Checkbox; when enabled, each user gets a single access token. See help text “Each new token expires the other old tokens”.
* **Authentication request must include user scopes?**Checkbox that enforces the requirement for authentication requests to specify user scopes.
* **Do not share user IDs:** Checkbox that prevents sharing user IDs in tokens.
* **Repository GUID:** Input field for the repository GUID associated with this OAuth configuration
* **Private encryption key:**Input field for the private key used to encrypt tokens or secrets.
* **GENERATE KEY:** Button to generate a new private encryption key.

### [Authorization tab](#Authorization+tab)

`[imagen omitida: wiki id 61020]`

* **Enable Authorization?** Checkbox to enable the OAuth authorization flow for this application.

### [SSO Rest tab](#SSO+Rest+tab)

`[imagen omitida: wiki id 61021]`

* **Enable SSO REST services?**Checkbox to enable SSO REST services for the application.

### [STS tab](#STS+tab)

`[imagen omitida: wiki id 61022]`

* **Enable STS protocol?**Checkbox to enable the STS protocol for the application.

### [Mini App tab](#Mini+App+tab)

`[imagen omitida: wiki id 61023]`

* **Enable work as MiniApp?** Checkbox to enable the application to function as a Mini App.

### [API Key tab](#API+Key+tab)

This tab contains settings related to the use of API keys for the application.

`[imagen omitida: wiki id 61024]`

* **Enable work with API keys:** A checkbox to enable the application to work with API keys.

### [Environment tab](#Environment+tab)

This section defines the GAM server environment configuration used by the application to connect to GAM services.

`[imagen omitida: wiki id 61025]`

* **Name:** Text input to identify this environment.
* **Is HTTPS?** Checkbox to indicate whether the environment uses HTTPS.
* **Host:** Text input for the GAM server hostname or IP address.
* **Port:** Numeric input to set the network port.
* **Virtual Directory:** Text input for the base path on the server.
* **Package:** Text input to specify the GAM package associated with this environment.
* **Extension:** Provides a text input for an optional URL extension.

### [Languages tab](#Languages+tab)

`[imagen omitida: wiki id 61026]`

The Languages tab defines the languages available for GAM Web Backoffice UI localization.

## [Editing an existing application](#Editing+an+existing+application)

To edit an application, go to Applications and select the application from the list:

`[imagen omitida: wiki id 61027]`

Next, click on the EDIT link.

`[imagen omitida: wiki id 61028]`

In addition to the edit form, there are two buttons: DELETE and MORE OPTIONS.

**DELETE:** Deletes the selected application.

**MORE OPTIONS:** This Combo Box menu includes advanced options for managing the application in the Web Backoffice:

* **Custom Properties:** Allows you to add custom properties related to the application.
* **Permissions:** Allows you to configure the specific permissions associated with the application.
* **Menus:**  Allows you to add menus in a particular application.
* **Revoke:** Deactivates the current application. Double-clicking on the link will reactivate the previously revoked application.
* **Copy:** Duplicates the current application with the same settings.
* **Translations:** Adds translations for the application in different languages.

### [See Also](#See+Also)

[GAM - Applications](https://wiki.genexus.com/commwiki/wiki?15910)


|  |
| --- |
| **Backlinks** |
| [GAM - Applications](https://wiki.genexus.com/commwiki/wiki?15910) | [GAM Web Backoffice - Main Menu](https://wiki.genexus.com/commwiki/wiki?61064) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
