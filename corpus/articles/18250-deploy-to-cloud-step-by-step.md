---
title: "Deploy to cloud: Step by Step"
source_id: 18250
source_url: https://wiki.genexus.com/commwiki/wiki?18250
genexus_version: "18"
---

# Deploy to cloud: Step by Step

The aim behind [Cloud prototyping](https://wiki.genexus.com/commwiki/wiki?15046) is to provide a simple mechanism to prototype your applications in the [cloud](http://en.wikipedia.org/wiki/Cloud_computing).

This is a simple guide to help you deploy an application to the cloud using this mechanism and to know details that can be useful.

### [Context](#Context)

#### [Available platforms](#Available+platforms)

The deployment process packages the application and uploads it to GeneXus's cloud, based on Amazon servers. The developer is able to deploy Web or Mobile ([Apple](https://wiki.genexus.com/commwiki/wiki?14917) and
[Android](https://wiki.genexus.com/commwiki/wiki?14453)) applications, whose backend can be:

* [Java](https://wiki.genexus.com/commwiki/wiki?12258) using MySQL as DBMS.
* [.NET](https://wiki.genexus.com/commwiki/wiki?38604) using MySQL or SQLServer as DBMS.

**Warning**: This feature is available for prototyping purposes only; it should not be used to host applications in production that might require another SLA.

#### [GeneXus authentication](#GeneXus+authentication)

In order to deploy an application, the developer must be registered in GeneXus. If you don't have one, you can create it [here](https://www.genexus.com/en/developers/sign-in).

### [Setting the environment](#Setting+the+environment)

**1.** The process starts with an existing KB. You can use an existing environment or create a new one with [Java](https://wiki.genexus.com/commwiki/wiki?12258) or [.NET](https://wiki.genexus.com/commwiki/wiki?38604) generator. If you're creating a new one, don't forget to set it as the target environment.

**2.** You need to specify that you want to deploy your application to the cloud. This is done by setting the [Deploy to cloud property](https://wiki.genexus.com/commwiki/wiki?15041) to Yes as shown below.  
`[imagen omitida: wiki id 37598]`

**3.** Once this property is set, default values for Server and Virtual Directory are automatically set.  
`[imagen omitida: wiki id 37599]`

* The [Deploy Server URL property](https://wiki.genexus.com/commwiki/wiki?15042) set may vary depending on the generator and the GeneXus Version.  
  See [Servers available for Cloud prototyping](https://wiki.genexus.com/commwiki/wiki?26157,,) for more information.  
  **Tip:** You may want SSL, if so, read more about this at [Deploy Server URL property](https://wiki.genexus.com/commwiki/wiki?15042).
* The [Deploy Virtual Directory property](https://wiki.genexus.com/commwiki/wiki?18342) is set to an [GUID](https://wiki.genexus.com/commwiki/wiki?21842) which identifies the environment.  
  It may be changed to a friendlier name (availability is checked later in the process).

**4.** Also, [Data Store properties](https://wiki.genexus.com/commwiki/wiki?7117) values are automatically set.  
`[imagen omitida: wiki id 37600]`

* The [Database name property](https://wiki.genexus.com/commwiki/wiki?9080) is set to a [GUID](https://wiki.genexus.com/commwiki/wiki?21842) which identifies the database instance.
* The [Server Name Property](https://wiki.genexus.com/commwiki/wiki?9117) will be the same specified at [Deploy Server URL property](https://wiki.genexus.com/commwiki/wiki?15042), so it's set to the same value.  
  Do not change it because these are the available platforms; otherwise, errors may occur.
* [User Id](https://wiki.genexus.com/commwiki/wiki?9039,,) and [User password](https://wiki.genexus.com/commwiki/wiki?9040,,) properties are set to a generated value (the same value for both properties).  
  Please change them as soon as possible to avoid forgetting it, security problems, etc.

### [Notes](#Notes)

* The generators available are:  
  -
  [Java](https://wiki.genexus.com/commwiki/wiki?12258) using MySQL and  
  -
  [.NET](https://wiki.genexus.com/commwiki/wiki?38604)using MySQL or SQL Server (default).  
  Consider this when changing the properties.
* If more than one environment is used in the same KB, check the [Database name property](https://wiki.genexus.com/commwiki/wiki?9080) to avoid accidentally creating tables over existing data. Consider [Deploy Virtual Directory property](https://wiki.genexus.com/commwiki/wiki?18342) too.

### [Deploying the application](#Deploying+the+application)

A [GeneXus Developer Account](https://www.genexus.com/developers/) is needed to manage the applications deployed to the cloud, so when you run them for the first time, a dialog asking for it is displayed. If you don't have a user account, please create it [here](https://www.genexus.com/en/developers/sign-in).

Once the user's details are provided, the account is checked for existence using GeneXus's services. If it exists and it has the necessary privileges, the process continues checking Virtual Directory and Database Name availability. If these values are available, DB and Virtual Directory are created; if not, an error informing the issue is displayed.

The process continues creating the tables, generating and deploying the application to the server.

Finally, the application is run, that is, the browser is opened, the emulator is started, etc. (depending on the generators and configurations used).  
For further information about running the application, please check [Executing From QR Codes](https://wiki.genexus.com/commwiki/wiki?18260).

### [Under the hood](#Under+the+hood)

To learn more about the mechanism behind this process, please check [Deploy to GeneXus Prototyping Cloud - FAQ](https://wiki.genexus.com/commwiki/wiki?18292).

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Prototyping features and Deployment of applications for Smart Devices](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/prototyping-features-and-deployment-of-applications-for-smart-devices?p=3694)


|  |
| --- |
| **Backlinks** |
| [Category:Cloud prototyping](https://wiki.genexus.com/commwiki/wiki?15046) | [Deploy to cloud property](https://wiki.genexus.com/commwiki/wiki?15041) | [Deploy to GeneXus Prototyping Cloud - FAQ](https://wiki.genexus.com/commwiki/wiki?18292) |
| [Executing From QR Codes](https://wiki.genexus.com/commwiki/wiki?18260) | [My first Android application](https://wiki.genexus.com/commwiki/wiki?14555) | [My first iOS application](https://wiki.genexus.com/commwiki/wiki?14738) | [My first Offline Native Mobile application](https://wiki.genexus.com/commwiki/wiki?20249) |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Troubleshooting 'Execution failed' message when running a Web app](https://wiki.genexus.com/commwiki/wiki?49557) |

---
