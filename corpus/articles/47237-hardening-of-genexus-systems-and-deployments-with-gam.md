---
title: "Hardening of GeneXus Systems and Deployments with GAM"
source_id: 47237
source_url: https://wiki.genexus.com/commwiki/wiki?47237
genexus_version: "18"
---

# Hardening of GeneXus Systems and Deployments with GAM

This article aims to inform developers and administrators about actions to take when developing and deploying GeneXus applications so that they are more secure against certain events that, by default, are not covered by configuration in the GeneXus IDE or otherwise are covered and are explained here.

It should be stressed that every development or configuration improvement implemented **must be tested before** it is deployed in a production environment. In particular, this applies to changes regarding server configuration.

## [Recommended GAM settings](#Recommended+GAM+settings)

Every deployment has its particular characteristics, so there is no fixed configuration recommended for everything that GAM offers. However, several elements should be checked and adjusted to recommended or appropriate values for the application. This section lists the essential tasks that must be performed when configuring GAM for safe deployment. For more details on each item, read the [documentation on recommended changes](https://wiki.genexus.com/commwiki/wiki?18574).

### [Default and test credentials](#Default+and+test+credentials)

* Change the password of the administrator user, “admin.”

Since the automatically created administrator users of the [GAM Repository](https://wiki.genexus.com/commwiki/wiki?17568) have a default password, this must be changed in the [GAM Backend](https://wiki.genexus.com/commwiki/wiki?29699).

* Change the password of the administrator user, “gamadmin.”

This is the password of the repository administrator. It has to be changed through the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535) using code, which must not be accessible to non-administrators.

* Create new connections (Repository Connections) or edit them in the repository.

By default, GAM creates a user for each connection named <version\_name> (name of the knowledge base version using that naming convention), with a default password. For example, in a version called “MY\_APP” the username will be “my\_app” and the password will be “my\_app123.” Creating new connections or at least editing the default password generated for production deployments is recommended.

* Delete all users intended for testing.

### [Confidentiality settings](#Confidentiality+settings)

* Only deploy metadata of Native mobile applications if it's strictly required. More information at [App Update property](https://wiki.genexus.com/commwiki/wiki?46540) and [Enable KBN property](https://wiki.genexus.com/commwiki/wiki?46541).
* The web server must not expose the connection.gam file.
* The GAM backend must be private, so that only users with the “Administrator” role can run its Panels.

[Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s already have the logic to comply with this restriction. However, if the backend binaries distributed by GAM are not used but the “GAM Examples” are compiled, keep in mind that the Panels GAMExampleRecoverPasswordStep1 and GAMExampleRecoverPasswordStep2 must be edited as indicated in the [GAM example article](https://wiki.genexus.com/commwiki/wiki?16923). They should not be deployed as they were distributed because they are sample Panels. The same applies to the Panels GAMExampleRegisterUser, GAMExampleUpdateRegisterUser and GAMExampleChangePassword.

### [Repository settings](#Repository+settings)

Configuring the following elements in the GAM repositories is recommended:

* User remember me type: The safest value is “None.”
* User remember me timeout (days): Depending on the security requirements, the recommended value may be a maximum of 30 days and decrease as the severity increases.
* User recovery password key timeout (minutes).
* Minimum amount characters in login.
* Login retries to lock user.
* Login attempts to lock session.
* Unblock user timeout (minutes).
* Give anonymous session?
* User session cache timeout (seconds): A value smaller than or equal to 30 seconds is recommended.
* Expire the session when the IP changes?
* User activation method: The “Automatic” value is not recommended.
* User automatic activation timeout (hours).
* Repository cache timeout (minutes).
* Check the repository's default values for the properties Repository default security policy and Repository default role.

### [Security Policy settings](#Security+Policy+settings)

Configuring the following elements regarding the GAM security policy is recommended:

* ONLY WEB
* Session time out (minutes).
* Allow multiple concurrent user sessions: The safest value is “No.”
* ONLY REST OAUTH (Mobile, GAMRemoteRest)
* Token Expire (minutes): There isn't a fixed recommended value; it is determined by the required security level (the lower this value, the safer the application).
* Token maximum renovations: To avoid entering credentials again, also set a maximum number of refresh tokens of at least 1.
* Period change password (days).
* Minimum waiting time between password changes (days).
* Minimum password length: The minimum length can be debatable, but a minimum of 8 is usually suggested if the password is complex enough.
* Minimum number of numeric characters in passwords.
* Minimum number of uppercase characters in passwords.
* Minimum number of special characters in passwords.
* Maximum password history entries.

## [Considerations and recommendations for mobile applications](#Considerations+and+recommendations+for+mobile+applications)

* In the case of mobile devices, in general, actions programmed by GeneXus developers are translated into calls to REST Web Services. REST services must be protected in the same way as objects for mobile development.

To find these services, search the KB for “Rest Protocol= True” and set the permissions on each one as appropriate (see section “Integrated Security Levels”).

* To the extent possible, avoid the use of cache in the mobile application client. In particular, make sure that the [Enable Data Caching property](https://wiki.genexus.com/commwiki/wiki?18302) in the [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s is set to False.
* Consider the [Single User Access property](https://wiki.genexus.com/commwiki/wiki?17242) when configuring the application in GAM.
* You must not deploy the backend of multiple [Offline Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?22237) in the same web app or [Deployment Unit object](https://wiki.genexus.com/commwiki/wiki?38886).


|  |
| --- |
| **Backlinks** |
| [Configuration for secure deployment using GAM](https://wiki.genexus.com/commwiki/wiki?47243) | [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
