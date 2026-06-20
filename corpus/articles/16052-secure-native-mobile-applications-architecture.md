---
title: "Secure Native Mobile applications architecture"
source_id: 16052
source_url: https://wiki.genexus.com/commwiki/wiki?16052
genexus_version: "18"
---

# Secure Native Mobile applications architecture

The architecture of a Native Mobile application consists basically of a "client application" which is installed on the device (depending on the device it will be an APK, IPA, or JAD), and a server application ([REST Web Services](https://wiki.genexus.com/commwiki/wiki?14573) which solve the business logic of the application).

The client application (APK, IPA, JAD) may be available in any application marketplace (depending on the platform).  
The server application may be installed on any host server.

### [Security considerations](#Security+considerations)

Depending on the characteristics of the application, in most cases, a very important issue is to be sure that the server application is only accessible by authorized users.

Besides, another prerequisite may be that REST Web Services be only accessible from the devices, not from other clients. If they are accessible from other clients, only authorized clients should access them.

In GeneXus Native Mobile applications, this security is implemented using [GeneXus Access Manager (GAM)]([Table of contents:GeneXus Access Manager (GAM)) with an [OAuth](http://www.google.com.uy/search?sourceid=navclient&ie=UTF-8&rlz=1T4GGHP_enUY417&q=oauth)-based mechanism.

See the basic architecture structure of these applications and the recommended way to deploy them.

`[imagen omitida: wiki id 50941]`

(1) [Client Id Information](https://wiki.genexus.com/commwiki/wiki?21484)

When the user installs a Native Mobile application, the corresponding APK, IPA, JAD is downloaded to the device.  
This package (APK, IPA, JAD) besides the client application itself, has a "client id" to connect to the server application.  
The user will also need to know an authorized username / password to be able to connect to the application.

So, in order to connect to a secure application that consists of REST Web Services, the final user will need to know an authorized username / password. These credentials will be used in conjunction with the client Id downloaded to the device when the application is installed, in order to establish the first connection to the server application.

(2) access\_token information

When the user tries to connect to the application, a login is presented to him. The first time he tries to connect, a POST is done to the server, using username, password, client Id and the HTTP Response returns an access\_token which will be used all over the connection from now on.  
The access\_ token can either remain unchanged while the user is connected or be reset regularly, depending on the value of the [OauthTokenExpire property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?18577) property.

The access\_token stores in the device cache, and while it’s valid (the user does not log out) the final user will not be presented the login again.

So, following the user admission, for every REST Web Service requested, the access\_token validates against the OAuth Server, and GAM for avoiding "unwanted" entries.

### [Recommendations for application deployment in production time](#Recommendations+for+application+deployment+in+production+time)

For applications requiring high security, it is highly recommended to use HTTPS.

See the following document related to this topic: [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574)

### [See Also](#See+Also)

[How to develop secure REST web services in GeneXus](https://wiki.genexus.com/commwiki/wiki?15918)


|  |
| --- |
| **Backlinks** |
| [GAM - Applications](https://wiki.genexus.com/commwiki/wiki?15910) | [GAM - Applications (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?57690) | [GAM architecture for Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?14978) |
| [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) | [HowTo: Develop Secure REST Web Services in GeneXus](https://wiki.genexus.com/commwiki/wiki?15918) | [Login Object for SD property](https://wiki.genexus.com/commwiki/wiki?16589) |
| [Security Session Management in Applications using GAM](https://wiki.genexus.com/commwiki/wiki?16338) |

---
