---
title: "GAM - Examples"
source_id: 21993
source_url: https://wiki.genexus.com/commwiki/wiki?21993
genexus_version: "18"
---

# GAM - Examples

When [activating GAM](https://wiki.genexus.com/commwiki/wiki?19946) in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836), you are asked to import some GeneXus objects (like [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916), [Panels](https://wiki.genexus.com/commwiki/wiki?24829), [Procedures](https://wiki.genexus.com/commwiki/wiki?6293)) that use the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535). They handle login, registration, changing passwords, and redirecting in case of an Authorization error.

The purpose of these objects is to help you learn how to use [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746). You can "Save as" these examples to reuse their logic (or to customize the look & feel). Note that these examples should not be used as they are distributed because they may be updated every time a new build is installed.

If you accept to import these objects, they will be available inside a folder called "GAM\_Examples".

### [GAM\_Examples folder](#GAM_Examples+folder)

Inside the "GAM\_Examples" folder there are other folders to organize the available objects.

`[imagen omitida: wiki id 55587]`

For example, a folder called "GAM\_Frontend" contains objects that implement several functionalities for**Web****Frontends**and **Mobile Frontends**.

As you can see in the image, there are Web Panel objects (like the GAMExampleLogin, GAMExampleNotAuthorized, GAMExampleRegisterUser, GAMHome, and others) that provide the Web Frontend facilities. Some of them are referenced from the properties listed below:

* [Login Object for Web property](https://wiki.genexus.com/commwiki/wiki?15590)
* [Not Authorized Object for Web property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?17551,,)

#### In addition, inside the "GAM\_Frontend" folder, there is a "GAM\_Mobile" folder that contains Panel objects to provide Frontend facilities, too. Some of those Panels are referenced from the following properties:

* [Login Object for SD property](https://wiki.genexus.com/commwiki/wiki?16589)
* [Change Password Object for SD property](https://wiki.genexus.com/commwiki/wiki?20013)
* [Not Authorized Object for SD property](https://wiki.genexus.com/commwiki/wiki?20018)

### GAM Backoffice examples

The objects that implement the GAM Backoffice must be imported into the Knowledge Base to be used.   
They are included in the GAM\_Web-Administration.xpz file, found in <GeneXus Installation>\Library\GAM.


|  |
| --- |
| **Backlinks** |
| [CacheTimeout property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?21863) | [GAM - Activation Process](https://wiki.genexus.com/commwiki/wiki?21973) | [GAM - API for Menus](https://wiki.genexus.com/commwiki/wiki?29742) |
| [GAM - Custom Authentication Type](https://wiki.genexus.com/commwiki/wiki?21751) | [GAM - External Authorization](https://wiki.genexus.com/commwiki/wiki?22898) |
| [GAM - External Web Services Authentication Type](https://wiki.genexus.com/commwiki/wiki?16512) | [GAM - Getting Started](https://wiki.genexus.com/commwiki/wiki?19946) | [GAM - Users](https://wiki.genexus.com/commwiki/wiki?22082) | [Category:GAM - Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) |
| [Category:GAM API](https://wiki.genexus.com/commwiki/wiki?16535) | [GAM Backend Application](https://wiki.genexus.com/commwiki/wiki?29699) | [GAM options in GeneXus toolbar](https://wiki.genexus.com/commwiki/wiki?19947) |
| [GAM repository creation for the first time from GeneXus](https://wiki.genexus.com/commwiki/wiki?29701) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |
| [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) | [HowTo: Change the objects targeted by the GAM Backend menu to GAM Examples](https://wiki.genexus.com/commwiki/wiki?52816) | [HowTo: Have an SSO behavior by using SAML Authentication](https://wiki.genexus.com/commwiki/wiki?44887) |
| [Identity Provider Configuration for GAM Remote Authentication](https://wiki.genexus.com/commwiki/wiki?37038) | [Identity Provider Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?57020) | [Identity Provider Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57694) |
| [Managing Roles in applications using SSO](https://wiki.genexus.com/commwiki/wiki?25538) | [Restricted access to GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?18495) | [Single Sign On in applications using GAM](https://wiki.genexus.com/commwiki/wiki?25385) |

---
