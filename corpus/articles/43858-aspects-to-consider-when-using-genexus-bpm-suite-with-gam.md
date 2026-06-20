---
title: "Aspects to consider when using GeneXus BPM Suite with GAM"
source_id: 43858
source_url: https://wiki.genexus.com/commwiki/wiki?43858
genexus_version: "18"
---

# Aspects to consider when using GeneXus BPM Suite with GAM

## [Introduction](#Introduction)

The objective of this document is to centralize the information related to the simultaneous use of GXflow and GAM.

## [Initialization of GXflow entities in GAM Repository](#Initialization+of+GXflow+entities+in+GAM+Repository)

GXflow uses certain default roles and permissions that must be available in the GAM repository for the runtime to work correctly. For this purpose, there is an initialization utility that must be executed.  
To learn more, read [GXflow - GAM Initialization](https://wiki.genexus.com/commwiki/wiki?33095).

## [Synchronization of Users and Roles](#Synchronization+of+Users+and+Roles)

The information of users and roles is duplicated in the GAM and GXflow tables. Any change on one side, either from the backend or via API, is automatically synchronized on the other. For more information, read [GXflow - GAM Integration](https://wiki.genexus.com/commwiki/wiki?18454).

## [Authentication and Session Management](#Authentication+and+Session+Management)

In a system based on GAM or GXflow, an active user session is required.  
GAM and GXflow sessions are independent of each other and each system requires the corresponding session.

The way to obtain a session is by means of an Authentication mechanism, for which different scenarios are presented.

### Login Scenarios

#### [1.    GAM Login](#1.+GAM+Login)

If the user authenticates using the GAM login (either the example or any other that uses the GAMRepository.Login API), a GAM session is automatically created. If the user then logs in to the GXflow Client, it detects the GAM session and tries to create its own session based on the previous one. The success of such an operation will depend on whether it meets any of the following conditions:

A.    The user already exists in GXflow and is nominated.  
B.    The user doesn't exist in GXflow but has the GXflow Public role assigned in GAM, and there are nominated licenses available in GXflow.  
If the client, instead of using the standard GXflow Client, uses a proprietary one based on the Custom Client, he/she can enable this mechanism by following [these steps](https://wiki.genexus.com/commwiki/wiki?29533).

#### [2.    GXflow Login](#2.+GXflow+Login)

When the GXflow Client login is used, internally authentication is delegated to GAM, sending the credentials (username and password) entered (\*). In case of success, both GAM and GXflow sessions are created.

(\*) Remember that the GXflow login does not allow specifying the type of GAM authentication, so the login will try to authenticate the user with the type of authentication configured as default in GAM.

#### [3.    API WorkflowServer.Connect](#3.+API+WorkflowServer.Connect)

When the API WorkflowServer.Connect is used, authentication is also delegated to GAM, but in this case, only the GXflow session is created.  
If there is an active GAM session for the same user indicated in the method parameter, the authentication is skipped and the session is immediately created. This means that when there is an active session the password doesn't have to be entered unless you want to create a connection with a different user.  
This can be confirmed in the code mentioned [here](https://wiki.genexus.com/commwiki/wiki?29533).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
