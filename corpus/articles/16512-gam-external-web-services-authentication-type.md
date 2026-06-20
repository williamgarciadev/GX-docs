---
title: "GAM - External Web Services Authentication Type"
source_id: 16512
source_url: https://wiki.genexus.com/commwiki/wiki?16512
genexus_version: "18"
---

# GAM - External Web Services Authentication Type

When using External Web Services [Authentication Type](https://wiki.genexus.com/commwiki/wiki?16508) there are two versions of the web services supported by GAM. The supported web services versions are 1.0 and 2.0. The version depends on the signature of the web service, that is, the data type of the "in" and "out" parameters it sends and receives. The web service can be generated with any tool, but it must meet some requirements, related to its soap message format.

* [External Authentication: version 1.0](https://wiki.genexus.com/commwiki/wiki?21548)
* [External Authentication: version 2.0](https://wiki.genexus.com/commwiki/wiki?21555)

This document explains how to give users the possibility to authenticate using [GeneXus Access Manager](https://wiki.genexus.com/commwiki/wiki?24746) external web services Authentication.

### How to authenticate using GAM external web services authentication type

#### [1. Define a new ([Authentication Type](https://wiki.genexus.com/commwiki/wiki?16508)) using [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935).](#1.+Define+a+new+%28wiki%3F16508%2CGAM%2B-%2BAuthentication%2BTypes+Authentication+Type%29+using+wiki%3F15935%2CCategory%253AGAM%2B-%2BWeb%2BBackoffice+GAM+Web+Backoffice.)

It has to be "External Web Services Authentication" Type.

`[imagen omitida: wiki id 51897]`

##### [Figure 1. Java external web service](#Figure+1.+Java+external+web+service)

`[imagen omitida: wiki id 51898]`

##### [Figure 2. Csharp external web service.](#Figure+2.+Csharp+external+web+service.)

As seen in figure 1 and 2, you have to specify the location of the web service, protocol, and all the necessary information to connect to the web service.

You need to specify the web service version (1.0 or 2.0)

The "Encryption Key" is useful in case of Genexus web services because the Encrypt64 function is used to encrypt the username and password when sent to the web service. You have to set the Encryption key used in the web service for decrypting the user and password received.

Note that the best way to protect the data is by using HTTPS.

#### [2. Program "External Web Services Authentication" login in the Native Mobile application](#2.+Program+%22External+Web+Services+Authentication%22+login+in+the+Native+Mobile+application)

The [login](https://wiki.genexus.com/commwiki/wiki?19269) External method of [Actions external object](https://wiki.genexus.com/commwiki/wiki?31350) is used. In this case, the first parameter sent to the method must be "ExternalWebService".

```
Event 'ExternalLogin'
 GeneXus.SD.Actions.LoginExternal(GAMAuthenticationTypes.ExternalWebService,&User,&Password,&AdditionalParameters)
EndEvent
```

#### [3. Program "External Web Services Authentication" login in the web application](#3.+Program+%22External+Web+Services+Authentication%22+login+in+the+web+application)

The following code is an example of executing the external login in web applications. In the case of Web Panels, the Login method of GAMRepository object is used. You need to define a variable of GAMLoginAdditionalParameters in order to specify the AuthenticationType, which is going to be used.

See the GAMExampleLogin Web Panel (which is part of the [GAM - Examples](https://wiki.genexus.com/commwiki/wiki?21993)), where this code is used:

```
&AdditionalParameter.AuthenticationTypeName = &LogOnTo //&LogOnTo is a combo box where the user selects the authentication type he wants to use. 
                                                       //This is the name of the Authentication Type. Using the example shown in figure 1 it would be "Testws2.0".
&LoginOK = GAMRepository.Login(&UserName, &UserPassword, &AdditionalParameter, &Errors )//&Errors is collection of GAMError
```

Note: Only one "External Web Service" Authentication Type can be defined for each GAM Repository.

### [LoginExternal method considerations](#LoginExternal+method+considerations)

As since GeneXus 15 in Native Mobile applications, the [Actions external object](https://wiki.genexus.com/commwiki/wiki?31350) adds the LoginExternal method, which supports the &AdditionalParameters parameter.

### [TroubleShooting](#TroubleShooting)

[GAM - How to debug errors when using External Web Service Authentication Type](https://wiki.genexus.com/commwiki/wiki?19715,,)

### [See Also](#See+Also)

[GAM - Custom Authentication Type](https://wiki.genexus.com/commwiki/wiki?21751)  
[Managing Roles through external authentication programs](https://wiki.genexus.com/commwiki/wiki?16929)  
[HowTo: Pass additional parameters to external authentication programs using GAM](https://wiki.genexus.com/commwiki/wiki?21752)


|  |
| --- |
| **Backlinks** |
| [Actions external object](https://wiki.genexus.com/commwiki/wiki?31350) |
| [GAM - Authentication Types](https://wiki.genexus.com/commwiki/wiki?16508) | [GAM - Auto-register anonymous users - How it works](https://wiki.genexus.com/commwiki/wiki?19909) | [GAM - Custom Authentication Type](https://wiki.genexus.com/commwiki/wiki?21751) | [GAM - External Authentication Type](https://wiki.genexus.com/commwiki/wiki?21755) |
| [GAM - External Authentication: version 1.0](https://wiki.genexus.com/commwiki/wiki?21548) | [GAM - External Authentication: version 2.0](https://wiki.genexus.com/commwiki/wiki?21555) | [GAM - Impersonation](https://wiki.genexus.com/commwiki/wiki?24241) | [GAM - Two Factor Authentication (2FA)](https://wiki.genexus.com/commwiki/wiki?48254) |
| [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: LDAP Authentication using GAM](https://wiki.genexus.com/commwiki/wiki?29474) | [HowTo: Pass additional parameters to external authentication programs using GAM](https://wiki.genexus.com/commwiki/wiki?21752) | [HowTo: Pass additional parameters to external authentication programs using GAM (GeneXus 18 Upgrade)](https://wiki.genexus.com/commwiki/wiki?55358) |
| [HowTo: Send and receive properties set at the login](https://wiki.genexus.com/commwiki/wiki?44824) | [Managing Roles through external authentication programs](https://wiki.genexus.com/commwiki/wiki?16929) |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
