---
title: "Offline Native Mobile applications using GAM"
source_id: 23400
source_url: https://wiki.genexus.com/commwiki/wiki?23400
genexus_version: "18"
---

# Offline Native Mobile applications using GAM

This article is about special considerations to take into account in [Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?20286) when using [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746).

### [Login considerations](#Login+considerations)

The GAM login must be done when the application is online. Logging in while being offline, is not supported.

Anyway, after a successful login, the user can go on working offline, navigating through the panels which require Authentication, because the session stays valid until the user logs out.

### [Offline GAM API](#Offline+GAM+API)

The following static methods of the 'GAMUser' object can be invoked when the application is online or offline, from code that is being executed in the device.

* GetId, e.g: &GAMGUID = GAMUser.GetId()
* GetEmail, e.g: &email = GAMUser.GetEmail()
* GetExternalId, e.g: &externalId = GAMUser.GetExternalId()
* GetLogin, e.g: &login = GAMUser.GetLogin()
* GetName, e.g: &name= GAMUser.GetName()
* isAnonymous, e.g: &isAnonymous = GAMUser.isAnonymous()

### [Synchronization considerations](#Synchronization+considerations)

By default, if the Knowledge Base has already GAM installed, the synchronization programs given by GeneXus have an Authentication integrated security type, which means that only authenticated users on the application can run the synchronization programs correctly.

If you have to change these security settings, you can do it by changing the [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) of the main object and the one of its [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509).  
If the Main object's Integrated Security Level is 'Authorization', the corresponding execution permission is generated, and in runtime checked when [OfflineEventReplicator procedure](https://wiki.genexus.com/commwiki/wiki?26218) ([Synchronization.Send method](https://wiki.genexus.com/commwiki/wiki?23604))is invoked.  
if the Offline Database's Integrated Security Level is 'Authorization', the corresponding execution permission is generated, and in runtime checked when [Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22269) ([Receive](https://wiki.genexus.com/commwiki/wiki?23603)) is invoked

### [Other Restrictions](#Other+Restrictions)

- Authorization is only checked when accessing the Server-side, that is when accessing the synchronization services, or other REST Interfaces (Objects with Online [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911))  
- Non-static methods of 'GAMUser' object, e.g GAMUser.get(), or &GAMUser.GUID  
- Other GAM external objects, like GAMSession object.


|  |
| --- |
| **Backlinks** |
| [HowTo: Convert online applications into offline applications](https://wiki.genexus.com/commwiki/wiki?24591) | [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) |

---
